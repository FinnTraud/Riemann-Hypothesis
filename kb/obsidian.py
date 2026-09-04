#!/usr/bin/env python3
"""Obsidian-Compiler: macht den kuratierten Graphen im Vault SICHTBAR.

Ausgangslage
------------
Der Wissensgraph dieses Projekts lebte vollstaendig in kb/graph/*.json:
104 typisierte Kanten, 12 Konzepte, Blocker, Luecken. Im Vault selbst war
davon nichts zu sehen -- die Dokumente enthielten null Wikilinks, es gab
kein .obsidian/, kein Canvas, kein Dataview. Graph View zeigte 55 isolierte
Punkte (docs/62, Befund 2).

Dieses Modul uebersetzt den Graphen in Obsidian-Bordmittel:

  1. WIKILINKS      Ein Block "Verknuepfungen (auto)" je Dokument, zwischen
                    Markern, aus edges.json + blockers.json + gaps.json.
                    Idempotent: erneuter Lauf ersetzt nur den Block.
  2. STATUSBOARD    docs/_Statusboard.md mit Dataview-Queries UND einer
                    statischen Tabelle als Fallback (Dataview ist ein
                    Community-Plugin und in diesem Repo nicht mitgeliefert).
  3. CANVAS         Canvas/Zeitachse_Motive.canvas   (Zeit x Leitmotiv)
                    Canvas/Obstruktionskarte.canvas  (Blocker <-> Ansaetze)
  4. KONFIG         .obsidian/ mit Graph-Farbgruppen nach Kategorie.

    python3 kb/obsidian.py             # alles erzeugen
    python3 kb/obsidian.py --links     # nur Wikilinks
    python3 kb/obsidian.py --check     # nichts schreiben, nur berichten
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
GRAPH = ROOT / "kb" / "graph"
CANVAS = ROOT / "Canvas"
OBSIDIAN = ROOT / ".obsidian"

BEGIN = "<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->"
END = "<!-- OBSIDIAN-LINKS:END -->"

#: Kantentyp -> (Anzeigename ausgehend, Anzeigename eingehend)
REL_LABEL = {
    "equivalent_to": ("äquivalent zu", "äquivalent zu"),
    "implies": ("impliziert", "wird impliziert von"),
    "reduces_to": ("reduziert sich auf", "ist Reduktionsziel von"),
    "refuted_by": ("widerlegt durch", "widerlegt"),
    "special_case_of": ("Spezialfall von", "verallgemeinert"),
    "generalizes": ("verallgemeinert", "Spezialfall von"),
    "obstruction_for": ("ist Obstruktion für", "wird obstruiert von"),
    "evidence_for": ("ist Evidenz für", "gestützt durch"),
    "models": ("modelliert", "modelliert von"),
    "blueprint_for": ("ist Blaupause für", "folgt Blaupause"),
    "uses": ("benutzt", "wird benutzt von"),
    "partial_result_for": ("ist Teilresultat für", "hat Teilresultat"),
    "weaker_than": ("schwächer als", "stärker als"),
    "attempts_transfer_of": ("versucht Transfer von", "Transferziel von"),
    "instance_of": ("ist Instanz von", "hat Instanz"),
}

#: Kategorie -> Farbe fuer Graph View und Canvas (Obsidian: "1".."6")
CAT_COLOR = {
    "foundations": "4", "partial-results": "4",
    "spectral": "5", "solution-program": "5",
    "criterion": "2", "analytic": "2",
    "proven-analogue": "3",
    "obstruction": "1", "failed-proof": "1",
    "breakthrough": "6", "frontier": "6",
}


# --------------------------------------------------------------------------
# Laden
# --------------------------------------------------------------------------

def _jload(name):
    return json.loads((GRAPH / name).read_text(encoding="utf-8"))


def parse_frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"([a-z_]+):\s*(.*)", line)
        if not mm:
            continue
        k, v = mm.group(1), mm.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        else:
            v = v.strip('"')
        fm[k] = v
    return fm


def load_docs():
    """doc-id -> {stem, path, frontmatter}."""
    out = {}
    for p in sorted(DOCS.glob("*.md")):
        if p.name.startswith("_"):
            continue
        fm = parse_frontmatter(p.read_text(encoding="utf-8"))
        did = fm.get("id")
        if not did:
            continue
        out[did] = {"stem": p.stem, "path": p, "fm": fm}
    return out


def link(docs, node_id):
    """Wikilink fuer einen Knoten; Konzepte bleiben Klartext."""
    if node_id in docs:
        d = docs[node_id]
        return f"[[{d['stem']}|{node_id.replace('doc-', '')} · {_short(d['fm'].get('title', node_id))}]]"
    return f"`{node_id}`"


def _short(t, n=52):
    t = str(t).split("(")[0].split(":")[0].split("—")[0].strip().strip('"')
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


# --------------------------------------------------------------------------
# 1. Wikilinks
# --------------------------------------------------------------------------

def build_link_blocks(docs):
    edges = _jload("edges.json")["edges"]
    concepts = {c["id"]: c for c in _jload("nodes.json")["concepts"]}
    blockers = _jload("blockers.json")["blockers"]
    gaps = _jload("gaps.json")["gaps"]

    out_e, in_e = defaultdict(list), defaultdict(list)
    for e in edges:
        out_e[e["from"]].append(e)
        in_e[e["to"]].append(e)
    blk_of = defaultdict(list)
    for b in blockers:
        for d in b["betrifft"]:
            blk_of[d].append(b)
    gap_of = {g["doc"]: g for g in gaps}

    blocks = {}
    for did, d in docs.items():
        lines = []

        bl = sorted(blk_of.get(did, []), key=lambda b: b["tier"])
        if bl:
            lines.append("> [!warning]- Blocker — woran dieser Ansatz hängt "
                         f"({len(bl)})")
            for b in bl:
                lines.append(f"> - **{b['name']}** *(Tier {b['tier']})* — {b['kurz']}")
                lines.append(f">   *Fluchtbedingung:* {b['fluchtbedingung']}")
            lines.append(f"> \n> Vollständige Matrix: [[55_failure_taxonomy]]")
            lines.append("")

        g = gap_of.get(did)
        if g:
            lines.append("> [!missing]- Die fehlende Aussage")
            lines.append(f"> **Bewiesen:** {g['bewiesen']}")
            lines.append(f"> **Es fehlt:** {g['fehlt']}")
            lines.append(f"> **Typ:** {g['luecken_typ'].replace('_', ' ')} · "
                         f"Bewertung: [[58_gap_registry_near_miss]]")
            lines.append("")

        rel = []
        for e in sorted(out_e.get(did, []), key=lambda e: e["type"]):
            lab = REL_LABEL.get(e["type"], (e["type"], e["type"]))[0]
            tgt = concepts.get(e["to"], {}).get("label") if e["to"] in concepts else None
            rel.append(f"> - *{lab}* → {tgt and f'**{tgt}**' or link(docs, e['to'])}"
                       + (f" — {e['note']}" if e.get("note") else ""))
        for e in sorted(in_e.get(did, []), key=lambda e: e["type"]):
            lab = REL_LABEL.get(e["type"], (e["type"], e["type"]))[1]
            src = concepts.get(e["from"], {}).get("label") if e["from"] in concepts else None
            rel.append(f"> - ← *{lab}* {src and f'**{src}**' or link(docs, e['from'])}"
                       + (f" — {e['note']}" if e.get("note") else ""))
        if rel:
            lines.append(f"> [!abstract]- Graph-Nachbarn ({len(rel)})")
            lines.extend(rel)
            lines.append("")

        lines.append("**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · "
                     "[[56_failure_autopsies|56 · Autopsien]] · "
                     "[[57_untried_directions|57 · Noch nicht versucht]] · "
                     "[[58_gap_registry_near_miss|58 · Lücken]] · "
                     "[[59_invariants_test_vectors|59 · Invarianten]] · "
                     "[[60_counterexample_oracle|60 · Orakel]] · "
                     "[[_Statusboard|Statusboard]]")

        # Der Navigationsfuss kommt immer; Dokumente ohne Kanten bekommen nur ihn.
        blocks[did] = "\n".join(lines).rstrip()
    return blocks


def inject_links(docs, blocks, dry=False):
    changed = 0
    for did, block in blocks.items():
        p = docs[did]["path"]
        text = p.read_text(encoding="utf-8")
        new_section = (f"\n## Verknüpfungen (auto)\n\n{BEGIN}\n\n{block}\n\n{END}\n")
        if BEGIN in text and END in text:
            pre, rest = text.split(BEGIN, 1)
            _, post = rest.split(END, 1)
            new = pre + BEGIN + "\n\n" + block + "\n\n" + END + post
        else:
            new = text.rstrip() + "\n" + new_section
        if new != text:
            changed += 1
            if not dry:
                p.write_text(new, encoding="utf-8")
    return changed


# --------------------------------------------------------------------------
# 2. Statusboard
# --------------------------------------------------------------------------

def build_statusboard(docs):
    blockers = _jload("blockers.json")["blockers"]
    gaps = _jload("gaps.json")["gaps"]
    claims = _jload("claims.json")["claims"]
    blk_count = defaultdict(int)
    for b in blockers:
        for d in b["betrifft"]:
            blk_count[d] += 1

    rows = []
    for did, d in sorted(docs.items()):
        fm = d["fm"]
        if fm.get("category") in ("index", "glossary"):
            continue
        rows.append((fm.get("number", ""), d["stem"], _short(fm.get("title", ""), 46),
                     fm.get("category", ""), fm.get("status", ""), blk_count.get(did, 0)))

    lines = [
        "---", "id: statusboard", "title: \"Statusboard\"", "category: index",
        "status: reference", "tags: [dashboard, dataview, overview]", "lang: de", "---",
        "", "# Statusboard", "",
        "> [!note] Erzeugt von `kb/obsidian.py` — nicht von Hand editieren.",
        "> Die Dataview-Blöcke unten brauchen das Community-Plugin **Dataview**.",
        "> Ist es nicht installiert, zeigt Obsidian den Code-Block als Text —",
        "> deshalb steht darunter jeweils eine statische Tabelle mit denselben Daten.",
        "",
        "## Nach Status (Dataview)", "",
        "```dataview", "TABLE status AS Status, category AS Kategorie, tags AS Tags",
        "FROM \"docs\"", "WHERE status != null", "SORT status ASC, number ASC", "```", "",
        "## Offene Ansätze mit den meisten Blockern (Dataview)", "",
        "```dataview", "TABLE category AS Kategorie, status AS Status",
        "FROM \"docs\"", "WHERE status = \"open\"", "SORT number ASC", "```", "",
        "## Alle Dokumente (statisch)", "",
        "| Nr | Dokument | Kategorie | Status | Blocker |", "|---|---|---|---|:-:|",
    ]
    for num, stem, title, cat, st, nb in rows:
        bar = "●" * nb if nb else "—"
        lines.append(f"| {num} | [[{stem}\\|{title}]] | `{cat}` | `{st}` | {bar} |")

    lines += [
        "", "## Lücken nach Near-Miss-Score", "",
        "Vollständige Bewertung und Rechenregel: [[58_gap_registry_near_miss]]", "",
        "| Score | Lücke | Dokument |", "|:-:|---|---|",
    ]
    import sys as _s
    _s.path.insert(0, str(ROOT / "kb"))
    import gaps as _g
    for g in sorted(gaps, key=lambda g: -_g.score(g)[0]):
        stem = docs.get(g["doc"], {}).get("stem", g["doc"])
        lines.append(f"| **{_g.score(g)[0]}** | {g['titel']} | [[{stem}]] |")

    from collections import Counter
    tr = Counter(c.get("trust", "?") for c in claims)
    lines += [
        "", "## Claims nach Verifikationsstufe", "",
        "Bedeutung der Stufen: [[64_trust_tiers_verification_levels]]", "",
        "| Stufe | Anzahl |", "|---|:-:|",
    ]
    for t in ["T0-lean-verified", "T1-kanonisch", "T2-peer-reviewed",
              "T3-preprint", "T4-repo-numerik", "T5-konsens"]:
        if tr.get(t):
            lines.append(f"| `{t}` | {tr[t]} |")
    lines += ["", f"*{sum(tr.values())} Claims gesamt · "
                  f"{sum(1 for c in claims if c.get('zugang') == 'sekundaer')} aus "
                  "Sekundärdarstellungen erfasst (siehe [[62_ai_division_of_labour_self_audit]], "
                  "Befund 1).*", "",
              "## Karten", "",
              "- [[Zeitachse_Motive.canvas|Zeitachse × Leitmotiv]] — wie sich die drei "
              "Leitmotive über 165 Jahre entwickelt haben",
              "- [[Obstruktionskarte.canvas|Obstruktionskarte]] — welche Ansätze an "
              "welchem Blocker hängen", ""]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# 3. Canvas
# --------------------------------------------------------------------------

def _node(nid, x, y, w, h, *, text=None, file=None, color=None, label=None):
    n = {"id": nid, "x": int(x), "y": int(y), "width": int(w), "height": int(h)}
    if file:
        n["type"], n["file"] = "file", file
    elif label is not None:
        n["type"], n["label"] = "group", label
    else:
        n["type"], n["text"] = "text", text or ""
    if color:
        n["color"] = color
    return n


#: (Jahr, Kürzel, doc-id, Motiv) — Motiv: A=Positivität, B=Spektral, C=Geometrie, D=analytisch/numerisch
TIMELINE = [
    (1859, "Riemann", "doc-01", "D"), (1896, "PNT", "doc-12", "D"),
    (1914, "Hardy", "doc-03", "D"), (1916, "Riesz", "doc-16", "A"),
    (1936, "Davenport–Heilbronn", "doc-35", "D"),
    (1948, "Weil 𝔽_q", "doc-18", "C"), (1952, "Weil-Positivität", "doc-14", "A"),
    (1955, "Nyman–Beurling", "doc-13", "A"), (1956, "Selberg-Spurformel", "doc-19", "B"),
    (1972, "Montgomery–Dyson", "doc-06", "B"), (1974, "Levinson", "doc-04", "D"),
    (1975, "Voronin", "doc-46", "D"), (1976, "de Bruijn–Newman", "doc-23", "A"),
    (1984, "Robin", "doc-15", "A"), (1986, "de Branges", "doc-20", "A"),
    (1995, "Bost–Connes", "doc-34", "C"), (1997, "Li-Kriterium", "doc-14", "A"),
    (1999, "Connes-Spurformel", "doc-10", "C"), (1999, "Berry–Keating", "doc-08", "B"),
    (2000, "Keating–Snaith", "doc-07", "B"), (2007, "𝔽₁ / arithmetic site", "doc-30", "C"),
    (2017, "Bender–Brody–Müller", "doc-09", "B"), (2018, "Rodgers–Tao Λ≥0", "doc-23", "A"),
    (2019, "GORZ Jensen", "doc-29", "A"), (2021, "Connes–Moscovici", "doc-11", "B"),
    (2022, "Zhang Landau–Siegel", "doc-32", "D"), (2024, "Guth–Maynard", "doc-22", "D"),
    (2025, "Weil-Truncation", "doc-52", "A"), (2025, "PCC ohne RH", "doc-53", "B"),
]
MOTIF = {"A": ("Positivität / Reellwurzeligkeit", "2", 0),
         "B": ("Spektrale Interpretation", "5", 1),
         "C": ("Geometrie-Transfer", "3", 2),
         "D": ("Analytisch / numerisch", "6", 3)}


def build_canvas_timeline(docs):
    nodes, edges = [], []
    col_w, row_h, x0, y0 = 320, 150, 0, 0
    years = sorted({y for y, *_ in TIMELINE})
    ypos = {y: y0 + i * row_h for i, y in enumerate(years)}

    for key, (label, color, col) in MOTIF.items():
        nodes.append(_node(f"hdr-{key}", x0 + col * col_w, y0 - 200, col_w - 40, 90,
                           text=f"## {label}\n\nLeitmotiv **{key}** · siehe [[41_synthesis_what_a_proof_needs]]",
                           color=color))
    for y in years:
        nodes.append(_node(f"yr-{y}", x0 - 200, ypos[y], 150, 60, text=f"### {y}"))

    prev_by_motif = {}
    for i, (yr, name, did, motif) in enumerate(TIMELINE):
        label, color, col = MOTIF[motif]
        nid = f"ev-{i}"
        stem = docs.get(did, {}).get("stem", did)
        nodes.append(_node(nid, x0 + col * col_w, ypos[yr], col_w - 40, 110,
                           text=f"**{name}**\n\n[[{stem}]]", color=color))
        if motif in prev_by_motif:
            edges.append({"id": f"e-{i}", "fromNode": prev_by_motif[motif],
                          "fromSide": "bottom", "toNode": nid, "toSide": "top",
                          "color": color})
        prev_by_motif[motif] = nid

    nodes.append(_node("legend", x0 + 4 * col_w + 60, y0, 460, 320, text=(
        "## Lesart\n\n"
        "Vier Spalten = die vier Leitmotive. Pfeile verbinden aufeinanderfolgende "
        "Arbeiten **innerhalb** eines Motivs.\n\n"
        "**Was auffällt:**\n"
        "- Spalte C (Geometrie) hat die wenigsten Einträge — und enthält die "
        "einzige *bewiesene* RH (1948, 𝔽_q).\n"
        "- Spalte A (Positivität) ist die vollste. Neun Ansätze hängen am selben "
        "Blocker: [[55_failure_taxonomy]].\n"
        "- Nach 2018 verdichtet sich alles bei A und B — die Front ist schmal "
        "geworden.\n\n"
        "Bewertung der jüngsten Einträge: [[58_gap_registry_near_miss]]")))
    return {"nodes": nodes, "edges": edges}


def build_canvas_blockers(docs):
    blockers = _jload("blockers.json")["blockers"]
    nodes, edges = [], []
    tier_x = {1: 0, 2: 1400, 3: 2800}
    tier_count = defaultdict(int)
    TCOL = {1: "1", 2: "6", 3: "4"}

    for t, x in tier_x.items():
        names = {1: "Tier 1 — harte Obstruktion (Gegenbeispiel existiert)",
                 2: "Tier 2 — strukturelle Lücke (Forschungsfront)",
                 3: "Tier 3 — Methodengrenze / Warnung"}[t]
        nodes.append(_node(f"t{t}", x, -260, 1200, 120, color=TCOL[t],
                           text=f"# {names}"))

    for b in sorted(blockers, key=lambda b: (b["tier"], -len(b["betrifft"]))):
        t = b["tier"]
        row = tier_count[t]
        tier_count[t] += 1
        by = row * 460
        bx = tier_x[t]
        bid = b["id"]
        nodes.append(_node(bid, bx, by, 560, 300, color=TCOL[t], text=(
            f"## {b['name']}\n\n{b['kurz']}\n\n"
            f"**Fluchtbedingung:** {b['fluchtbedingung']}\n\n"
            f"*{len(b['betrifft'])} Ansätze betroffen*"
            + (f" · maschinell prüfbar: `{b['orakel_test']}` "
               "([[60_counterexample_oracle]])" if b.get("orakel_test") else ""))))
        for j, did in enumerate(b["betrifft"]):
            stem = docs.get(did, {}).get("stem")
            if not stem:
                continue
            nid = f"{bid}--{did}"
            nodes.append(_node(nid, bx + 640, by + j * 105, 480, 90, file=f"docs/{stem}.md"))
            edges.append({"id": f"e-{nid}", "fromNode": bid, "fromSide": "right",
                          "toNode": nid, "toSide": "left", "color": TCOL[t]})
    return {"nodes": nodes, "edges": edges}


# --------------------------------------------------------------------------
# 4. Obsidian-Konfiguration
# --------------------------------------------------------------------------

def write_obsidian_config(dry=False):
    files = {
        "app.json": {"attachmentFolderPath": "attachments", "newLinkFormat": "shortest",
                     "useMarkdownLinks": False, "alwaysUpdateLinks": True,
                     "showLineNumber": True, "readableLineLength": True},
        "appearance.json": {"accentColor": "", "theme": "moonstone"},
        "core-plugins.json": ["file-explorer", "global-search", "switcher", "graph",
                              "backlink", "outgoing-link", "tag-pane", "page-preview",
                              "note-composer", "command-palette", "outline",
                              "word-count", "canvas", "bookmarks"],
        "community-plugins.json": [],
        "graph.json": {
            "collapse-filter": False, "search": "", "showTags": True,
            "showAttachments": False, "hideUnresolved": True, "showOrphans": True,
            "collapse-color-groups": False,
            "colorGroups": [
                {"query": "path:docs/ tag:#obstruction OR file:(35 OR 55 OR 56 OR 59 OR 60)",
                 "color": {"a": 1, "rgb": 14701138}},
                {"query": "path:docs/ category:spectral", "color": {"a": 1, "rgb": 5431378}},
                {"query": "path:docs/ category:criterion", "color": {"a": 1, "rgb": 11621088}},
                {"query": "path:docs/ category:proven-analogue", "color": {"a": 1, "rgb": 5099334}},
                {"query": "path:docs/ category:failed-proof", "color": {"a": 1, "rgb": 14701138}},
                {"query": "path:docs/ category:meta", "color": {"a": 1, "rgb": 8355711}},
            ],
            "collapse-display": False, "showArrow": True, "textFadeMultiplier": 0,
            "nodeSizeMultiplier": 1.2, "lineSizeMultiplier": 1,
            "collapse-forces": False, "centerStrength": 0.5, "repelStrength": 12,
            "linkStrength": 1, "linkDistance": 260, "scale": 0.7,
        },
    }
    if not dry:
        OBSIDIAN.mkdir(exist_ok=True)
        for name, data in files.items():
            (OBSIDIAN / name).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return list(files)


# --------------------------------------------------------------------------

def main(argv=None):
    p = argparse.ArgumentParser(description="Obsidian-Schicht aus dem Graphen erzeugen")
    p.add_argument("--links", action="store_true", help="nur Wikilinks injizieren")
    p.add_argument("--check", action="store_true", help="nichts schreiben, nur berichten")
    a = p.parse_args(argv)
    dry = a.check

    docs = load_docs()
    print(f"{len(docs)} Dokumente mit Frontmatter gefunden.")

    blocks = build_link_blocks(docs)
    n = inject_links(docs, blocks, dry=dry)
    print(f"Wikilink-Blöcke: {len(blocks)} erzeugt, {n} Dateien "
          f"{'würden geändert' if dry else 'geändert'}.")
    if a.links:
        return

    board = build_statusboard(docs)
    if not dry:
        (DOCS / "_Statusboard.md").write_text(board, encoding="utf-8")
    print(f"Statusboard: docs/_Statusboard.md ({board.count(chr(10))} Zeilen)")

    if not dry:
        CANVAS.mkdir(exist_ok=True)
    for name, builder in (("Zeitachse_Motive", build_canvas_timeline),
                          ("Obstruktionskarte", build_canvas_blockers)):
        c = builder(docs)
        if not dry:
            (CANVAS / f"{name}.canvas").write_text(
                json.dumps(c, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Canvas: Canvas/{name}.canvas ({len(c['nodes'])} Knoten, "
              f"{len(c['edges'])} Kanten)")

    cfg = write_obsidian_config(dry=dry)
    print(f".obsidian/: {', '.join(cfg)}")


if __name__ == "__main__":
    main()
