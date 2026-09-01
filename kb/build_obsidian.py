#!/usr/bin/env python3
"""
build_obsidian.py — Baut die Obsidian-Netzwerkschicht über der Wissensbasis.

Erzeugt (idempotent, alles überschreibbar):
  1. In JEDEM docs/NN_*.md einen Block "## 🔗 Vernetzung" zwischen AUTO-Markern:
     typisierte Kanten (aus kb/graph/edges.json) als [[Wikilinks]], Konzept-Links,
     Fehlermodus-Links, Ansatz-Profil, die drei ähnlichsten Ansätze zum Vergleich
     und Tag-Nachbarn.
  2. docs/concepts/   — je ein Hub-Note pro Konzept (aus nodes.json)
  3. docs/fehlermodi/ — je ein Note pro Fehlermodus F1..F15 (aus failure_modes.json)
  4. docs/moc/        — Maps of Content pro Ansatz-Familie + Hub
  5. Die AUTO-Blöcke in docs/68 (Fehler-Landkarte) und docs/69 (Vergleichsmatrix)

Damit entsteht in Obsidian ein echtes Netzwerk: Dokumente ↔ Konzepte ↔ Fehlermodi ↔ MOCs.
Handgeschriebener Text außerhalb der Marker bleibt unangetastet.

Aufruf:  python3 kb/build_obsidian.py [--dry-run]
"""
import os, re, sys, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
GRAPH = os.path.join(ROOT, "kb", "graph")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compare as C

START = "<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->"
END = "<!-- AUTO:VERNETZUNG END -->"
BSTART = "<!-- AUTO:%s START (kb/build_obsidian.py) -->"
BEND = "<!-- AUTO:%s END -->"

REL_DE = {
    "equivalent_to": "ist äquivalent zu", "implies": "impliziert",
    "reduces_to": "reduziert sich auf", "refuted_by": "widerlegt durch",
    "special_case_of": "Spezialfall von", "generalizes": "verallgemeinert",
    "obstruction_for": "ist Obstruktion für", "evidence_for": "ist Evidenz für",
    "models": "modelliert", "blueprint_for": "ist Blaupause für", "uses": "benutzt",
    "partial_result_for": "ist Teilresultat für", "weaker_than": "ist schwächer als",
    "attempts_transfer_of": "versucht Transfer von", "instance_of": "ist Instanz von",
}
TIER_DE = {
    1: "fatal — widerlegt die Idee sofort",
    2: "blockierend — offener Kernschritt",
    3: "strukturell — kann prinzipiell nicht implizieren",
}
FAMILY_DE = {
    "spectral": "Spektrale Ansätze", "analytic": "Analytische Ansätze",
    "algebraic-geometric": "Algebraisch-geometrische Ansätze",
    "probabilistic": "Probabilistische Modelle & Statistik",
    "physical": "Physikalische Modelle", "criterion": "Äquivalente Kriterien",
    "computational": "Rechnerische & formale Verifikation", "meta": "Meta",
}

# ------------------------------------------------------------------ Laden
def load():
    nodes = json.load(open(os.path.join(GRAPH, "nodes.json"), encoding="utf-8"))["concepts"]
    edges = json.load(open(os.path.join(GRAPH, "edges.json"), encoding="utf-8"))["edges"]
    man = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))["documents"]
    return nodes, edges, man

def docfiles():
    return sorted(f for f in os.listdir(DOCS) if re.match(r"\d\d_.*\.md$", f))

def docmap():
    """doc-NN -> (dateiname_ohne_md, titel)"""
    out = {}
    for f in docfiles():
        title = ""
        with open(os.path.join(DOCS, f), encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r'title:\s*"?(.*?)"?\s*$', line)
                if m:
                    title = m.group(1); break
        out["doc-" + f[:2]] = (f[:-3], title or f[:-3])
    return out

def conceptfile(cid):
    return "concept_" + cid.replace("concept-", "")

def modefile(m):
    return f"{m['id']}_{m['slug']}"

def mocfile(family):
    return "MOC_" + family.replace("-", "_")

# ------------------------------------------------------------------ Helfer
def link(target, label=None):
    return f"[[{target}|{label}]]" if label else f"[[{target}]]"

def doclink(did, DM, short=False):
    if did in DM:
        fn, title = DM[did]
        lbl = f"{did[-2:]} — {title}" if not short else title
        return link(fn, lbl)
    return did

def write(path, text, dry=False):
    if dry:
        print("[dry] würde schreiben:", os.path.relpath(path, ROOT)); return False
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old == text:
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
    return True

def replace_block(text, name, body):
    """Ersetzt (oder hängt an) einen AUTO-Block."""
    s, e = (BSTART % name, BEND % name) if name != "VERNETZUNG" else (START, END)
    block = f"{s}\n{body}\n{e}"
    if s in text and e in text:
        return re.sub(re.escape(s) + r".*?" + re.escape(e), lambda m: block, text, flags=re.S)
    return text.rstrip() + "\n\n" + block + "\n"

# ------------------------------------------------------------------ Ähnlichkeit
def similarity(a, b):
    """Wie vergleichbar sind zwei Ansätze? Achsenübereinstimmung + gemeinsame Fehlermodi."""
    s = sum(1 for x in C.COMPARE_AXES if a.get(x) == b.get(x))
    s += 1.5 * len(set(a["failure_modes"]) & set(b["failure_modes"]))
    return s

def nearest(a, n=3):
    others = [x for x in C.approaches() if x["id"] != a["id"]]
    return sorted(others, key=lambda b: -similarity(a, b))[:n]

# ------------------------------------------------------------------ 1) Vernetzungsblöcke
def vernetzung_body(did, DM, edges, concepts, tagmap):
    A = {x["doc"]: x for x in C.approaches()}
    MI = {m["id"]: m for m in C.modes()}
    L = []
    L.append("## 🔗 Vernetzung")
    L.append("> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. "
             "Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.")
    L.append("")

    app = A.get(did)
    if app:
        L.append(f"**Karte:** {link(mocfile(app['family']), FAMILY_DE.get(app['family'], app['family']))}")
        L.append("")
        L.append("| Achse | Wert |")
        L.append("|---|---|")
        L.append(f"| Familie | {app['family']} |")
        L.append(f"| Implikation | `{app['equivalence']}` |")
        L.append(f"| Euler-Produkt | `{app['euler_product']}` |")
        L.append(f"| Positivität | `{app['positivity']}` |")
        L.append(f"| Strenge | `{app['rigor']}` · Evidenz `{app['evidence']}` |")
        L.append(f"| Testbar / formalisierbar | `{app['testable']}` / `{app['formalizable']}` |")
        L.append("")
        L.append(f"**Offener Kernschritt:** {app['open_step']}")
        L.append("")
        L.append(f"**Hebel (was er liefern würde):** {app['lever']}")
        L.append("")
        if app["failure_modes"]:
            fm = " · ".join(link(modefile(MI[f]), f"{f} {MI[f]['label']}")
                            for f in app["failure_modes"] if f in MI)
            L.append(f"**Typische Fehlermodi:** {fm}")
            L.append("")
        nb = nearest(app)
        if nb:
            cmp_ = " · ".join(doclink(b["doc"], DM, short=True) for b in nb)
            L.append(f"**Vergleichbar mit:** {cmp_}")
            L.append(f"> Vergleich abrufen: `python3 kb/compare.py compare {did} " +
                     " ".join(b["doc"] for b in nb) + "`")
            L.append("")

    outg = [e for e in edges if e["from"] == did]
    inc = [e for e in edges if e["to"] == did]
    cnames = {c["id"]: c["label"] for c in concepts}

    def fmt(e, other):
        if other.startswith("concept-"):
            tgt = link(conceptfile(other), cnames.get(other, other))
        else:
            tgt = doclink(other, DM)
        note = f" — {e['note']}" if e.get("note") else ""
        return f"- *{REL_DE.get(e['type'], e['type'])}* (`{e['type']}`) → {tgt}{note}"

    if outg:
        L.append("**Ausgehende Beziehungen**")
        L += [fmt(e, e["to"]) for e in outg]
        L.append("")
    if inc:
        L.append("**Eingehende Beziehungen**")
        L += [fmt(e, e["from"]) for e in inc]
        L.append("")

    rel = tagmap.get(did, [])
    if rel:
        L.append("**Thematisch benachbart (gemeinsame Tags):** " +
                 " · ".join(doclink(d, DM, short=True) for d in rel))
        L.append("")
    L.append(f"**Navigation:** {link('00_INDEX', 'Index')} · "
             f"{link('MOC_00_Hub', 'Netzwerk-Hub')} · "
             f"{link('68_failure_anatomy', 'Fehler-Anatomie')} · "
             f"{link('69_comparison_matrix', 'Vergleichsmatrix')}")
    return "\n".join(L)

def build_tagmap(man, k=5):
    """Dokumente mit den meisten gemeinsamen Tags (ohne Graph-Kante)."""
    tags = {d["id"]: set(d.get("tags", [])) for d in man}
    out = {}
    for a in tags:
        sc = [(len(tags[a] & tags[b]), b) for b in tags if b != a and tags[a] & tags[b]]
        sc.sort(reverse=True)
        out[a] = [b for n, b in sc[:k] if n >= 1]
    return out

# ------------------------------------------------------------------ 2) Konzept-Notes
def build_concepts(concepts, edges, DM, dry):
    n = 0
    for c in concepts:
        cid = c["id"]
        rel_out = [e for e in edges if e["from"] == cid]
        rel_in = [e for e in edges if e["to"] == cid]
        body = [
            "---", f"id: {cid}", f"title: \"{c['label']}\"", "type: concept",
            "tags: [concept, netzwerk]", "lang: de", "---", "",
            f"# {c['label']}", "",
            f"> **Konzept-Hub.** {c.get('summary','')}", "",
            "*Automatisch erzeugt (`kb/build_obsidian.py`) aus `kb/graph/nodes.json` + `edges.json`.*", "",
        ]
        if rel_in:
            body.append("## Dokumente, die hierher zeigen")
            for e in rel_in:
                body.append(f"- {doclink(e['from'], DM)} — *{REL_DE.get(e['type'], e['type'])}*"
                            + (f" — {e['note']}" if e.get("note") else ""))
            body.append("")
        if rel_out:
            body.append("## Von hier ausgehend")
            for e in rel_out:
                tgt = (link(conceptfile(e["to"]), e["to"]) if e["to"].startswith("concept-")
                       else doclink(e["to"], DM))
                body.append(f"- *{REL_DE.get(e['type'], e['type'])}* → {tgt}"
                            + (f" — {e['note']}" if e.get("note") else ""))
            body.append("")
        body.append(f"**Navigation:** {link('MOC_00_Hub','Netzwerk-Hub')} · {link('00_INDEX','Index')}")
        if write(os.path.join(DOCS, "concepts", conceptfile(cid) + ".md"),
                 "\n".join(body) + "\n", dry):
            n += 1
    return n

# ------------------------------------------------------------------ 3) Fehlermodus-Notes
def build_modes(DM, dry):
    n = 0
    stats = C.failure_statistics()
    rank = {r["id"]: r for r in stats["ranked_failure_modes"]}
    for m in C.modes():
        aff = C.failure_mode(m["id"])["affected"]
        r = rank.get(m["id"], {"count": 0, "share": 0.0})
        body = [
            "---", f"id: fm-{m['id']}", f"title: \"{m['id']} — {m['label']}\"",
            "type: failure-mode", f"tier: {m['tier']}",
            "tags: [fehlermodus, obstruktion]", "lang: de", "---", "",
            f"# {m['id']} — {m['label']}", "",
            f"**Tier {m['tier']}** ({TIER_DE[m['tier']]})  ",
            f"**Betroffene Ansätze:** {r['count']} von {stats['n_approaches']} ({r['share']} %)", "",
            f"> {m['short']}", "",
            "## Worum es geht", m["description"], "",
            "## Prüffrage", f"> **{m['diagnostic']}**", "",
        ]
        if m.get("cases"):
            body += ["## Historische Fälle",
                     " · ".join(doclink(d, DM) for d in m["cases"]), ""]
        if m.get("docs"):
            body += ["## Belege / Hintergrund",
                     " · ".join(doclink(d, DM) for d in m["docs"]), ""]
        if aff:
            body.append("## Betroffene Ansätze")
            for a in aff:
                body.append(f"- {doclink(a['doc'], DM)} — `{a['status']}`")
            body.append("")
        body.append(f"**Navigation:** {link('68_failure_anatomy','Fehler-Anatomie')} · "
                    f"{link('69_comparison_matrix','Vergleichsmatrix')} · {link('MOC_00_Hub','Hub')}")
        if write(os.path.join(DOCS, "fehlermodi", modefile(m) + ".md"),
                 "\n".join(body) + "\n", dry):
            n += 1
    return n

# ------------------------------------------------------------------ 4) MOCs
def build_mocs(DM, man, dry):
    n = 0
    fams = collections.defaultdict(list)
    for a in C.approaches():
        fams[a["family"]].append(a)
    MI = {m["id"]: m for m in C.modes()}
    for fam, apps in fams.items():
        apps = sorted(apps, key=lambda x: x["doc"])
        cnt = collections.Counter(f for a in apps for f in a["failure_modes"])
        body = [
            "---", f"id: moc-{fam}", f"title: \"MOC — {FAMILY_DE.get(fam, fam)}\"",
            "type: moc", "tags: [moc, netzwerk]", "lang: de", "---", "",
            f"# MOC — {FAMILY_DE.get(fam, fam)}", "",
            f"*{len(apps)} Ansätze. Automatisch erzeugt aus `kb/graph/approaches.json`.*", "",
            "| Ansatz | Status | Implikation | offener Kernschritt |", "|---|---|---|---|",
        ]
        for a in apps:
            body.append(f"| {doclink(a['doc'], DM, short=True)} | `{a['status']}` | "
                        f"`{a['equivalence']}` | {a['open_step']} |")
        body += ["", "## Typische Fehlermodi dieser Familie", ""]
        for f, c in cnt.most_common():
            lbl = MI[f]["label"]
            body.append("- " + link(modefile(MI[f]), f"{f} {lbl}") + f" — {c}×")
        body += ["", f"**Navigation:** {link('MOC_00_Hub','Netzwerk-Hub')} · "
                     f"{link('69_comparison_matrix','Vergleichsmatrix')} · {link('00_INDEX','Index')}"]
        if write(os.path.join(DOCS, "moc", mocfile(fam) + ".md"), "\n".join(body) + "\n", dry):
            n += 1

    # Hub
    stats = C.failure_statistics()
    hub = [
        "---", "id: moc-hub", "title: \"MOC — Netzwerk-Hub\"", "type: moc",
        "tags: [moc, netzwerk, einstieg]", "lang: de", "---", "",
        "# MOC — Netzwerk-Hub", "",
        "Einstiegspunkt für die Graph-Ansicht. Alles hier ist generiert "
        "(`python3 kb/build_obsidian.py`).", "",
        "## Ansatz-Familien", "",
    ]
    for fam in sorted(fams):
        hub.append(f"- {link(mocfile(fam), FAMILY_DE.get(fam, fam))} — {len(fams[fam])} Ansätze")
    hub += ["", "## Fehlermodi (nach Häufigkeit)", "",
            "| Modus | Tier | betroffen |", "|---|---|---|"]
    MI2 = {m["id"]: m for m in C.modes()}
    for r in stats["ranked_failure_modes"]:
        hub.append(f"| {link(modefile(MI2[r['id']]), r['id'] + ' ' + r['label'])} | "
                   f"{r['tier']} | {r['count']} ({r['share']} %) |")
    hub += ["", "## Konzept-Hubs", ""]
    for c in json.load(open(os.path.join(GRAPH, "nodes.json"), encoding="utf-8"))["concepts"]:
        hub.append(f"- {link(conceptfile(c['id']), c['label'])}")
    hub += ["", "## Meta-Dokumente", "",
            f"- {link('00_INDEX', 'Dokumenten-Index')}",
            f"- {link('68_failure_anatomy', '68 — Anatomie des Scheiterns')}",
            f"- {link('69_comparison_matrix', '69 — Vergleichsmatrix')}",
            f"- {link('70_obsidian_network_guide', '70 — Netzwerk-Leitfaden')}",
            f"- {link('41_synthesis_what_a_proof_needs', '41 — Was ein Beweis braucht')}",
            f"- {link('35_obstructions_barriers', '35 — Obstruktionen')}", ""]
    if write(os.path.join(DOCS, "moc", "MOC_00_Hub.md"), "\n".join(hub) + "\n", dry):
        n += 1
    return n

# ------------------------------------------------------------------ main
def main(dry=False):
    concepts, edges, man = load()
    DM = docmap()
    tagmap = build_tagmap(man)
    changed = []

    for f in docfiles():
        did = "doc-" + f[:2]
        p = os.path.join(DOCS, f)
        text = open(p, encoding="utf-8").read()
        body = vernetzung_body(did, DM, edges, concepts, tagmap)
        new = replace_block(text, "VERNETZUNG", body)
        if write(p, new, dry):
            changed.append(f)

    # AUTO-Blöcke in 68 / 69
    for fname, block, gen in [("68_failure_anatomy.md", "FEHLERKARTE", C.failure_map_markdown),
                              ("69_comparison_matrix.md", "MATRIX", C.matrix_markdown)]:
        p = os.path.join(DOCS, fname)
        if os.path.exists(p):
            t = open(p, encoding="utf-8").read()
            t2 = replace_block(t, block, gen())
            # Vernetzungsblock danach neu anhängen (Reihenfolge egal)
            if write(p, t2, dry):
                changed.append(fname + f" [{block}]")

    nc = build_concepts(concepts, edges, DM, dry)
    nm = build_modes(DM, dry)
    nk = build_mocs(DM, man, dry)

    print(f"OK  Vernetzungsblöcke aktualisiert: {len(changed)}")
    print(f"    Konzept-Notes:   {nc} (docs/concepts/)")
    print(f"    Fehlermodus-Notes: {nm} (docs/fehlermodi/)")
    print(f"    MOC-Notes:       {nk} (docs/moc/)")
    if changed:
        print("    geändert:", ", ".join(changed[:8]) + (" …" if len(changed) > 8 else ""))

if __name__ == "__main__":
    main(dry="--dry-run" in sys.argv)
