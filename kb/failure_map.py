#!/usr/bin/env python3
"""Scheiternskarte: wo welcher Versuch haengt und wie weit er gekommen ist.

Der Obsidian-Graph (kb/obsidian.py) zeigt, WAS mit WAS verbunden ist. Er
zeigt nicht, woran ein Versuch scheitert und wie weit er vorher kommt. Dieses
Modul legt genau diese zwei Informationen auf das Netzwerk:

  REICHWEITE   je Versuch eine von fuenf Stufen (STAGES), deterministisch aus
               approaches.json abgeleitet (reach()). Keine Rangliste des
               Werts -- nur der erreichte Endstand (vgl. docs/78).
  SCHEITERN    Kante Versuch -> Blocker (F1-F15) aus approaches.json
               (failure_modes) vereinigt mit blockers.json (betrifft).

Ausgaben:
  viz/scheiternskarte.html   interaktives Netzwerk mit Farblegende (ohne
                             Abhaengigkeiten, offline lauffaehig)
  docs/_Scheiternskarte.md   Legende + Liste im Vault
  Obsidian-Graph             Tags #reichweite/... und #scheitert-an/... in den
                             Auto-Bloecken + Farbgruppen in .obsidian/graph.json
                             (beides erzeugt kb/obsidian.py ueber die Funktionen
                             hier)

    python3 kb/failure_map.py            # HTML + Legendennotiz schreiben
    python3 kb/failure_map.py --summary  # nur Stufen-Statistik ausgeben

Nur Python-Stdlib.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
GRAPH = ROOT / "kb" / "graph"
TEMPLATE = ROOT / "kb" / "failure_map_template.html"
OUT_HTML = ROOT / "viz" / "scheiternskarte.html"
OUT_NOTE = DOCS / "_Scheiternskarte.md"

#: Reichweite-Stufen, aufsteigend. Farben: einfarbige Ordinalskala (blau),
#: validiert mit dem dataviz-Validator (--ordinal) gegen #fcfcfb bzw. #1a1a19.
#: Fuenf Stufen, weil die helle Skala sechs nicht mehr unterscheidbar traegt.
STAGES = [
    {"n": 0, "slug": "0-widerlegt", "label": "Widerlegt / zurückgezogen",
     "rule": "Status oder Strenge `refuted`: die Beweisbehauptung bzw. das Modell ist nachweislich falsch.",
     "light": "#86b6ef", "dark": "#184f95"},
    {"n": 1, "slug": "1-heuristik", "label": "Heuristik",
     "rule": "Strenge `heuristic`: Plausibilitätsargument, kein Satz.",
     "light": "#5598e7", "dark": "#2a78d6"},
    {"n": 2, "slug": "2-offen", "label": "Offenes Programm",
     "rule": "Offen, ohne bewiesene Reduktion der RH: der Rahmen steht, der Kernschritt fehlt.",
     "light": "#2a78d6", "dark": "#5598e7"},
    {"n": 3, "slug": "3-umformulierung", "label": "Umformulierung bewiesen",
     "rule": "Offen, aber `RH ⇔ X` bzw. `X ⇒ RH` ist ein Satz (Implikation `equivalent`/`conditional`). X ist so schwer wie die RH.",
     "light": "#1c5cab", "dark": "#86b6ef"},
    {"n": 4, "slug": "4-bewiesen", "label": "Teilresultat / Analogon bewiesen",
     "rule": "Status `proven`: echter Satz, der nicht bis zur ganzen RH reicht (Teilaussage oder Analogon).",
     "light": "#104281", "dark": "#cde2fb"},
]

#: Blocker-Knoten (Identitaet, kein Rang): Kategorie-Slot 2 der Referenzpalette.
BLOCKER_COLOR = {"light": "#eb6834", "dark": "#d95926"}

#: Dokumentkategorien, die keine Versuche sind (Meta, Referenz, Front-Ueberblick).
NON_ATTEMPT = {"meta", "obstruction", "synthesis", "foundations", "frontier",
               "verification", "reference"}

FAMILY_LABEL = {
    "spectral": "spektral", "analytic": "analytisch", "algebraic-geometric": "alg.-geometrisch",
    "probabilistic": "probabilistisch", "physical": "physikalisch", "criterion": "Kriterium",
    "computational": "rechnerisch", "meta": "meta", "failed-proof": "gescheiterter Beweis",
    "heuristic": "probabilistisch",
}


def _jload(name):
    return json.loads((GRAPH / name).read_text(encoding="utf-8"))


def _frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    fm = {}
    for line in (m.group(1).splitlines() if m else []):
        mm = re.match(r"([a-z_]+):\s*(.*)", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm


def _docs():
    """doc-id -> {stem, fm}; dieselbe Auswahl wie obsidian.load_docs()."""
    out = {}
    for p in sorted(DOCS.glob("*.md")):
        if p.name.startswith("_"):
            continue
        fm = _frontmatter(p.read_text(encoding="utf-8"))
        if fm.get("id"):
            out[fm["id"]] = {"stem": p.stem, "fm": fm}
    return out


def _short(t, n=60):
    t = str(t).split("(")[0].split(":")[0].split("—")[0].strip().strip('"')
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def reach(profile=None, fm=None):
    """Reichweite-Stufe (0-4) eines Versuchs.

    profile: Eintrag aus approaches.json (bevorzugt); fm: Frontmatter als
    Rueckfall fuer Versuche, die nur ueber blockers.json erfasst sind.
    """
    p = profile or {}
    fm = fm or {}
    status = p.get("status") or fm.get("status")
    rigor = p.get("rigor")
    if status == "refuted" or rigor == "refuted":
        return 0
    if rigor == "heuristic" or (not p and fm.get("category") == "heuristic"):
        return 1
    if status == "proven":
        return 4
    if p:
        if rigor == "theorem" and p.get("equivalence") in ("equivalent", "conditional"):
            return 3
        return 2
    return 3 if fm.get("category") == "criterion" else 2


def build():
    """Alle Versuche, Blocker und Querkanten als ein Datenobjekt."""
    docs = _docs()
    approaches = {a["doc"]: a for a in _jload("approaches.json")["approaches"]}
    blockers = _jload("blockers.json")["blockers"]
    by_f = {b["f_mode"]: b for b in blockers}

    hits = defaultdict(set)
    for did, a in approaches.items():
        hits[did].update(a.get("failure_modes", []))
    for b in blockers:
        for did in b["betrifft"]:
            hits[did].add(b["f_mode"])

    attempts = []
    for did in sorted(set(approaches) | set(hits), key=lambda d: int(d.split("-")[1])):
        d = docs.get(did)
        if not d:
            continue
        a = approaches.get(did)
        fm = d["fm"]
        if not a and (fm.get("category") in NON_ATTEMPT or fm.get("status") in ("meta", "reference")):
            continue
        fam = (a or {}).get("family") or fm.get("category", "")
        attempts.append({
            "id": did,
            "label": a["label"] if a else _short(fm.get("title", did)),
            "file": f"docs/{d['stem']}.md",
            "family": FAMILY_LABEL.get(fam, fam),
            "stage": reach(a, fm),
            "status": (a or {}).get("status") or fm.get("status", ""),
            "rigor": (a or {}).get("rigor", ""),
            "equivalence": (a or {}).get("equivalence", ""),
            "open_step": (a or {}).get("open_step", ""),
            "lever": (a or {}).get("lever", ""),
            "blockers": sorted(hits[did], key=lambda f: int(f[1:])),
        })

    ids = {x["id"] for x in attempts}
    links = [{"s": e["from"], "t": e["to"], "type": e["type"]}
             for e in _jload("edges.json")["edges"]
             if e["from"] in ids and e["to"] in ids and e["from"] != e["to"]]

    count = Counter(f for x in attempts for f in x["blockers"])
    blk = [{
        "id": f, "name": b["name"], "tier": b["tier"], "kurz": b["kurz"],
        "flucht": b["fluchtbedingung"], "frage": b.get("diagnosefrage", ""),
        "file": f"docs/fehlermodi/{f}_{b.get('f_slug', '')}.md", "n": count[f],
    } for f, b in sorted(by_f.items(), key=lambda kv: int(kv[0][1:]))]

    return {"stages": STAGES, "blocker_color": BLOCKER_COLOR,
            "attempts": attempts, "blockers": blk, "links": links}


# --------------------------------------------------------------------------
# Obsidian-Anbindung (aufgerufen von kb/obsidian.py)
# --------------------------------------------------------------------------

def obsidian_tag_line(did, data=None):
    """Tag-Zeile fuer den Auto-Block eines Versuchs, sonst None."""
    data = data or build()
    a = next((x for x in data["attempts"] if x["id"] == did), None)
    if not a:
        return None
    st = STAGES[a["stage"]]
    tags = " ".join(f"#scheitert-an/{f}" for f in a["blockers"])
    return (f"**[[_Scheiternskarte|Scheiternskarte]]:** #reichweite/{st['slug']} "
            f"({st['label']})" + (f" · scheitert an {tags}" if tags else ""))


def obsidian_color_groups():
    """Farbgruppen fuer .obsidian/graph.json -- erste passende Gruppe gewinnt."""
    def rgb(h):
        return {"a": 1, "rgb": int(h.lstrip("#"), 16)}
    groups = [{"query": f"tag:#reichweite/{s['slug']}", "color": rgb(s["light"])} for s in STAGES]
    groups.append({"query": "path:docs/fehlermodi", "color": rgb(BLOCKER_COLOR["light"])})
    return groups


# --------------------------------------------------------------------------
# Ausgaben
# --------------------------------------------------------------------------

def write_html(data):
    html = TEMPLATE.read_text(encoding="utf-8").replace(
        "/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    OUT_HTML.parent.mkdir(exist_ok=True)
    OUT_HTML.write_text(html, encoding="utf-8")
    return OUT_HTML


def write_note(data):
    by_stage = defaultdict(list)
    for a in data["attempts"]:
        by_stage[a["stage"]].append(a)
    stems = {a["id"]: Path(a["file"]).stem for a in data["attempts"]}
    L = ["---", "id: scheiternskarte", 'title: "Scheiternskarte — Reichweite & Blocker je Versuch"',
         "status: reference", "tags: [dashboard, netzwerk, scheitern]", "lang: de", "---", "",
         "# Scheiternskarte", "",
         "> [!note] Generiert von `python3 kb/failure_map.py` aus `kb/graph/`. "
         "Änderungen dort vornehmen.", "",
         "Die Karte legt zwei Informationen auf das Netzwerk: **wie weit** ein Versuch "
         "gekommen ist (Farbe) und **woran** er hängt (Kante zum Blocker). "
         "Die Stufen beschreiben den erreichten Endstand, keine Rangliste des Werts "
         "(vgl. [[78_approach_comparison_matrix]]).", "",
         "**Interaktiv:** `viz/scheiternskarte.html` im Browser öffnen. "
         "**Im Graph View:** die Farbgruppen unten sind in `.obsidian/graph.json` hinterlegt; "
         "die Tags `#reichweite/…` und `#scheitert-an/…` stehen in jedem Versuchsdokument.", "",
         "## Legende", "",
         "| Farbe | Reichweite | Regel | Versuche |", "|---|---|---|---|"]
    for s in STAGES:
        L.append(f"| <span style=\"color:{s['light']}\">●</span> | `#reichweite/{s['slug']}` "
                 f"{s['label']} | {s['rule']} | {len(by_stage[s['n']])} |")
    L.append(f"| <span style=\"color:{BLOCKER_COLOR['light']}\">◆</span> | Blocker "
             "(`docs/fehlermodi/`) | Wiederkehrender Scheiterngrund F1–F15, "
             "siehe [[55_failure_taxonomy]] | 15 |")
    for s in reversed(STAGES):
        L += ["", f"## {s['label']} ({len(by_stage[s['n']])})", "",
              "| Versuch | scheitert an |", "|---|---|"]
        for a in by_stage[s["n"]]:
            bl = " · ".join(f"[[{Path(b['file']).stem}\\|{b['id']}]]"
                            for b in data["blockers"] if b["id"] in a["blockers"])
            L.append(f"| [[{stems[a['id']]}\\|{a['label']}]] | {bl or '—'} |")
    L += ["", "## Blocker nach Häufigkeit", "", "| Blocker | Tier | Versuche |", "|---|---|---|"]
    for b in sorted(data["blockers"], key=lambda b: (-b["n"], b["tier"])):
        L.append(f"| [[{Path(b['file']).stem}\\|{b['id']} {b['name']}]] | {b['tier']} | {b['n']} |")
    OUT_NOTE.write_text("\n".join(L) + "\n", encoding="utf-8")
    return OUT_NOTE


def summary(data):
    c = Counter(a["stage"] for a in data["attempts"])
    print(f"{len(data['attempts'])} Versuche, {len(data['blockers'])} Blocker, "
          f"{len(data['links'])} Querkanten")
    for s in STAGES:
        print(f"  {s['n']} {s['label']:<34} {c[s['n']]:>3}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Scheiternskarte erzeugen")
    p.add_argument("--summary", action="store_true", help="nur Statistik, nichts schreiben")
    a = p.parse_args(argv)
    data = build()
    summary(data)
    if a.summary:
        return
    print(f"HTML: {write_html(data).relative_to(ROOT)}")
    print(f"Notiz: {write_note(data).relative_to(ROOT)}")


if __name__ == "__main__":
    main()
