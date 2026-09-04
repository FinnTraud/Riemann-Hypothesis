#!/usr/bin/env python3
"""Konsistenzpruefung des Wissensgraphen.

Prueft alle kuratierten JSON-Dateien gegen die Dokumente und gegeneinander:
Selbstschleifen, ins Leere zeigende Kanten, unbekannte Relationstypen,
Blocker/Luecken auf nicht existierende Dokumente, fehlende Pflichtfelder,
doppelte IDs, Dokumente ohne Frontmatter-ID.

Der Anlass: eine Selbstschleife doc-20 -> doc-20 stand unbemerkt im Graphen,
bis der Obsidian-Compiler sie als sinnlosen Wikilink ausgab (docs/62,
Befund 8). Datenfehler dieser Art fallen ohne Validator nicht auf.

    python3 kb/validate.py           # Bericht, Exit 1 bei Fehlern
    python3 kb/validate.py --quiet   # nur Zusammenfassung
"""
from __future__ import annotations
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "kb" / "graph"
DOCS = ROOT / "docs"

REL_TYPES = {
    "equivalent_to", "implies", "reduces_to", "refuted_by", "special_case_of",
    "generalizes", "obstruction_for", "evidence_for", "models", "blueprint_for",
    "uses", "partial_result_for", "weaker_than", "attempts_transfer_of", "instance_of",
}
TRUST_TIERS = {"T0-lean-verified", "T1-kanonisch", "T2-peer-reviewed",
               "T3-preprint", "T4-repo-numerik", "T5-konsens"}


def _load(name):
    return json.loads((GRAPH / name).read_text(encoding="utf-8"))


def doc_ids():
    ids, no_id = set(), []
    for p in sorted(DOCS.glob("*.md")):
        if p.name.startswith("_"):
            continue
        m = re.search(r"^id:\s*(\S+)", p.read_text(encoding="utf-8"), re.M)
        if m:
            ids.add(m.group(1))
        else:
            no_id.append(p.name)
    return ids, no_id


def validate():
    err, warn = [], []
    docs, no_id = doc_ids()
    for n in no_id:
        err.append(f"docs/{n}: keine 'id' im Frontmatter")

    concepts = {c["id"] for c in _load("nodes.json")["concepts"]}
    known = docs | concepts

    edges = _load("edges.json")["edges"]
    for i, e in enumerate(edges):
        where = f"edges.json[{i}] {e.get('from')} -{e.get('type')}-> {e.get('to')}"
        if e["from"] == e["to"]:
            err.append(f"{where}: Selbstschleife")
        for side in ("from", "to"):
            if e[side] not in known:
                err.append(f"{where}: '{e[side]}' ist kein bekannter Knoten")
        if e.get("type") not in REL_TYPES:
            err.append(f"{where}: unbekannter Relationstyp")
        if not e.get("note"):
            warn.append(f"{where}: ohne 'note'")
    seen = Counter((e["from"], e["to"], e["type"]) for e in edges)
    for k, n in seen.items():
        if n > 1:
            warn.append(f"edges.json: Kante {k} kommt {n}x vor")

    blockers = _load("blockers.json")["blockers"]
    ids = Counter(b["id"] for b in blockers)
    for k, n in ids.items():
        if n > 1:
            err.append(f"blockers.json: doppelte ID '{k}'")
    for b in blockers:
        for f in ("id", "name", "kurz", "tier", "beschreibung", "betrifft", "fluchtbedingung"):
            if not b.get(f) and b.get(f) != 0:
                err.append(f"blockers.json/{b.get('id')}: Feld '{f}' fehlt")
        if b.get("tier") not in (1, 2, 3):
            err.append(f"blockers.json/{b.get('id')}: tier muss 1, 2 oder 3 sein")
        for d in b.get("betrifft", []):
            if d not in docs:
                err.append(f"blockers.json/{b['id']}: betrifft unbekanntes '{d}'")

    gaps = _load("gaps.json")["gaps"]
    ids = Counter(g["id"] for g in gaps)
    for k, n in ids.items():
        if n > 1:
            err.append(f"gaps.json: doppelte ID '{k}'")
    blk_ids = {b["id"] for b in blockers}
    for g in gaps:
        if g.get("doc") not in docs:
            err.append(f"gaps.json/{g.get('id')}: doc '{g.get('doc')}' existiert nicht")
        for a in ("A", "B", "C", "D", "E"):
            v = g.get(a, 0)
            if v not in (0, 1):
                err.append(f"gaps.json/{g['id']}: Achse {a} muss 0 oder 1 sein, ist {v!r}")
            if v == 1 and not g.get(f"{a}_begruendung"):
                warn.append(f"gaps.json/{g['id']}: Achse {a}=1 ohne Begründung")
        for b in g.get("blocker", []):
            if b not in blk_ids:
                err.append(f"gaps.json/{g['id']}: unbekannter Blocker '{b}'")
        if "score" in g:
            err.append(f"gaps.json/{g['id']}: 'score' darf NICHT in den Daten stehen "
                       "(wird von kb/gaps.py berechnet)")

    claims = _load("claims.json")["claims"]
    ids = Counter(c["id"] for c in claims)
    for k, n in ids.items():
        if n > 1:
            err.append(f"claims.json: doppelte ID '{k}'")
    for c in claims:
        if c.get("doc") not in docs:
            err.append(f"claims.json/{c['id']}: doc '{c.get('doc')}' existiert nicht")
        if c.get("status") not in ("proven", "open", "refuted"):
            err.append(f"claims.json/{c['id']}: ungültiger status {c.get('status')!r}")
        if c.get("trust") not in TRUST_TIERS:
            err.append(f"claims.json/{c['id']}: trust fehlt oder unbekannt "
                       f"({c.get('trust')!r}) — siehe docs/64")
        if c.get("zugang") not in ("sekundaer", "primaer", "eigene_rechnung"):
            err.append(f"claims.json/{c['id']}: zugang fehlt oder unbekannt")

    inv = _load("invariants.json")
    for t in inv["testvektoren"]:
        if t.get("doc") not in docs:
            err.append(f"invariants.json/{t['id']}: doc '{t.get('doc')}' existiert nicht")
    for c in inv["ueberschuss_tests"]:
        if c.get("doc") not in docs:
            err.append(f"invariants.json/{c['id']}: doc '{c.get('doc')}' existiert nicht")

    isolated = sorted(docs - {e["from"] for e in edges} - {e["to"] for e in edges}
                      - {d for b in blockers for d in b["betrifft"]}
                      - {g["doc"] for g in gaps})
    return {"dokumente": len(docs), "kanten": len(edges), "blocker": len(blockers),
            "luecken": len(gaps), "claims": len(claims),
            "fehler": err, "warnungen": warn, "ohne_jede_verknuepfung": isolated}


def main(argv=None):
    p = argparse.ArgumentParser(description="Wissensgraph auf Konsistenz prüfen")
    p.add_argument("--quiet", action="store_true")
    a = p.parse_args(argv)
    r = validate()
    print(f"{r['dokumente']} Dokumente · {r['kanten']} Kanten · {r['blocker']} Blocker · "
          f"{r['luecken']} Lücken · {r['claims']} Claims")
    if not a.quiet:
        for label, key in (("FEHLER", "fehler"), ("Warnungen", "warnungen")):
            if r[key]:
                print(f"\n{label} ({len(r[key])}):")
                for m in r[key]:
                    print(f"  - {m}")
        if r["ohne_jede_verknuepfung"]:
            print(f"\nOhne jede Verknüpfung ({len(r['ohne_jede_verknuepfung'])}): "
                  + ", ".join(r["ohne_jede_verknuepfung"]))
    print(f"\n{'FEHLGESCHLAGEN' if r['fehler'] else 'OK'} — "
          f"{len(r['fehler'])} Fehler, {len(r['warnungen'])} Warnungen")
    return 1 if r["fehler"] else 0


if __name__ == "__main__":
    sys.exit(main())
