#!/usr/bin/env python3
"""
build_obsidian.py — Baut aus der Wissensbasis einen **Obsidian-Vault** (`obsidian/`),
in dem jeder Ansatz eine eigene Notiz ist und alle Verknüpfungen als [[Wikilinks]]
vorliegen. Damit wird der Wissensgraph in Obsidians Graph-Ansicht sichtbar.

Quellen:
  - docs/*.md            Inhalt + Frontmatter (Dokument-Notizen)
  - manifest.json        Metadaten (Kategorie, Status, Tags)
  - docs/00_INDEX.md     kuratierte Themen-Gliederung (A–O) -> Karten/MOC-Notizen
  - kb/graph/nodes.json  Konzept-/Motiv-Knoten
  - kb/graph/edges.json  typisierte Relationen (equivalent_to, uses, obstruction_for, …)
  - kb/graph/claims.json atomare Aussagen mit Status

Erzeugt:
  obsidian/Riemann-Wissensnetz.md      Zentrale Übersichtsnotiz (Einstiegspunkt)
  obsidian/Dokumente/                  55 Dokument-Notizen (voller Text + Verknüpfungen)
  obsidian/Konzepte/                   Konzept-/Motiv-Notizen
  obsidian/Claims/                     atomare Claims mit Status
  obsidian/Karten/                     Themen-Karten (MOC) + Relations-Legende
  obsidian/.obsidian/                  Vault-Konfiguration inkl. Graph-Farbgruppen

Nur Python-Stdlib.  Aufruf:  python3 kb/build_obsidian.py
"""
import os, re, json, shutil, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
VAULT = os.path.join(ROOT, "obsidian")

DIR_DOCS = "Dokumente"
DIR_CONCEPTS = "Konzepte"
DIR_CLAIMS = "Claims"
DIR_MAPS = "Karten"

HUB = "Riemann-Wissensnetz"
LEGEND = "Relationstypen (Legende)"

# ---------------------------------------------------------------- Vokabular

REL_DE = {
    "equivalent_to":      ("ist äquivalent zu",        "ist äquivalent zu"),
    "implies":            ("impliziert",               "wird impliziert von"),
    "reduces_to":         ("reduziert sich auf",       "ist Reduktionsziel von"),
    "refuted_by":         ("wird widerlegt durch",     "widerlegt"),
    "special_case_of":    ("ist Spezialfall von",      "hat als Spezialfall"),
    "generalizes":        ("verallgemeinert",          "wird verallgemeinert von"),
    "obstruction_for":    ("ist Obstruktion für",      "hat als Obstruktion"),
    "evidence_for":       ("ist Evidenz für",          "wird gestützt durch"),
    "models":             ("modelliert",               "wird modelliert von"),
    "blueprint_for":      ("ist Blaupause für",        "hat als Blaupause"),
    "uses":               ("nutzt",                    "wird genutzt von"),
    "partial_result_for": ("ist Teilresultat für",     "hat als Teilresultat"),
    "weaker_than":        ("ist schwächer als",        "ist stärker als"),
    "attempts_transfer_of": ("versucht Transfer von",  "wird zu übertragen versucht von"),
    "instance_of":        ("ist Instanz von",          "hat als Instanz"),
}

STATUS_DE = {
    "open": "OFFEN", "proven": "BEWIESEN", "refuted": "WIDERLEGT",
    "reference": "REFERENZ", "meta": "META",
}

CATEGORY_DE = {
    "index": "Index", "foundations": "Fundamente", "partial-results": "Partielle Resultate",
    "spectral": "Spektrale Ansätze", "analytic": "Analytische Ansätze", "criterion": "Äquivalente Kriterien",
    "proven-analogue": "Bewiesene Analoga", "generalization": "Verallgemeinerungen",
    "breakthrough": "Durchbrüche", "numerical": "Numerik", "failed-proof": "Gescheiterte Beweise",
    "ai-context": "KI-Kontext", "solution-program": "Lösungsprogramme", "obstruction": "Obstruktionen",
    "meta": "Meta", "reference": "Referenz", "verification": "Verifikation",
    "heuristic": "Heuristik", "glossary": "Glossar", "synthesis": "Synthese",
    "frontier": "Aktuelle Front", "context": "Kontext",
}

# Farbgruppen der Graph-Ansicht (Kategorie -> RGB)
CATEGORY_COLOR = {
    "foundations": 0x4C8DFF, "partial-results": 0x4CC9F0, "spectral": 0x9B6BFF,
    "analytic": 0x2EC4B6, "criterion": 0x00B894, "proven-analogue": 0x3DDC84,
    "generalization": 0x7BDFF2, "breakthrough": 0xFFB703, "numerical": 0xB0BEC5,
    "failed-proof": 0xE63946, "obstruction": 0xFF5C8A, "solution-program": 0xF77F00,
    "frontier": 0xFFD166, "meta": 0x8D99AE, "synthesis": 0xEF476F,
}

# ---------------------------------------------------------------- Hilfen

ILLEGAL = re.compile(r'[\\:*?<>|\[\]#^]')
# Ersatzzeichen, damit Titel lesbar bleiben (z. B. „Re(s)=1/2", „Meta / Synthese")
REPLACE = {"—": "–", ":": " –", "/": "\u2215", '"': "'", "„": "'", "“": "'", "”": "'"}

def sanitize(name):
    """Dateinamen-taugliche Fassung eines Titels (Obsidian/Windows-sicher)."""
    for a, b in REPLACE.items():
        name = name.replace(a, b)
    name = ILLEGAL.sub("", name)
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name[:110].strip()

def parse_frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
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
    return fm, m.group(2)

def yaml_list(items):
    return "".join("\n  - %s" % json.dumps(i, ensure_ascii=False) for i in items)

def slug_tag(s):
    s = s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    s = re.sub(r"[^a-z0-9/_-]+", "-", s).strip("-")
    return s

def write(relpath, text, keep_existing=False):
    path = os.path.join(VAULT, relpath)
    if keep_existing and os.path.exists(path):
        return
    os.makedirs(os.path.dirname(path) or VAULT, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

# ---------------------------------------------------------------- Laden

def load():
    man = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    nodes = json.load(open(os.path.join(ROOT, "kb", "graph", "nodes.json"), encoding="utf-8"))
    edges = json.load(open(os.path.join(ROOT, "kb", "graph", "edges.json"), encoding="utf-8"))["edges"]
    claims = json.load(open(os.path.join(ROOT, "kb", "graph", "claims.json"), encoding="utf-8"))["claims"]
    docs = {}
    for d in man["documents"]:
        path = os.path.join(ROOT, d["file"])
        raw = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        fm, body = parse_frontmatter(raw)
        d = dict(d)
        d["body"] = body.strip()
        d["fm"] = fm
        docs[d["id"]] = d
    return man, docs, nodes["concepts"], edges, claims

def index_sections():
    """Themen-Gliederung (A–O) aus docs/00_INDEX.md: [(Buchstabe, Titel, [doc-NN])]."""
    txt = open(os.path.join(DOCS, "00_INDEX.md"), encoding="utf-8").read()
    out, cur = [], None
    for line in txt.splitlines():
        h = re.match(r"###\s+([A-Z])\.\s+(.+)", line)
        if h:
            cur = (h.group(1), h.group(2).strip(), [])
            out.append(cur)
            continue
        m = re.match(r"-\s+`(\d{2})_", line)
        if m and cur:
            cur[2].append("doc-" + m.group(1))
    return out

# ---------------------------------------------------------------- Wikilinks

def build_link_index(docs, concepts):
    """doc-NN / concept-id  ->  (Notizname, Anzeigename)."""
    link = {}
    for did, d in docs.items():
        title = d["title"]
        # Doppelte Nummer im Titel vermeiden
        name = sanitize("%s %s" % (d["number"], title))
        link[did] = (name, "Dok. %s" % d["number"])
    for c in concepts:
        link[c["id"]] = (sanitize(c["label"]), c["label"])
    return link

FENCE = re.compile(r"```.*?```", re.S)

def autolink(body, self_id, link, docs):
    """Wandelt Querverweise („Dok. 05", `docs/35`) in [[Wikilinks]].
    Code-Blöcke bleiben unangetastet; erwähnte Dokumente werden zurückgemeldet."""
    mentioned = set()

    def note_for(num):
        did = "doc-%s" % num
        if did == self_id or did not in docs:
            return None
        mentioned.add(did)
        return link[did][0]

    # 1) Code-Fences maskieren
    fences = []
    def mask(m):
        fences.append(m.group(0))
        return "\x00FENCE%d\x00" % (len(fences) - 1)
    body = FENCE.sub(mask, body)

    # 2) `docs/NN…` (inline-Code) -> Wikilink mit sichtbarem Originaltext
    def repl_code_docs(m):
        n = note_for(m.group(1))
        return "[[%s|docs/%s]]" % (n, m.group(1)) if n else m.group(0)
    body = re.sub(r"`docs/(\d{2})[^`]*`", repl_code_docs, body)
    body = re.sub(r"(?<![`\w/])docs/(\d{2})[A-Za-z0-9_.\-]*",
                  lambda m: (lambda n: "[[%s|docs/%s]]" % (n, m.group(1)) if n else m.group(0))(note_for(m.group(1))),
                  body)

    # 3) restliche Inline-Code-Spans maskieren
    spans = []
    def mask_span(m):
        spans.append(m.group(0))
        return "\x00CODE%d\x00" % (len(spans) - 1)
    body = re.sub(r"`[^`\n]+`", mask_span, body)

    # 4) „Dok. 05", „Dok. 06–08", „Dok. 10, 31", „Doc. 44"
    NUMS = r"\d{2}(?:\s*(?:,|/|–|—|-|\bund\b|\bbis\b)\s*\d{2})*"
    def repl_dok(m):
        prefix, nums = m.group(1), m.group(2)
        def one(mm):
            n = note_for(mm.group(0))
            return "[[%s|%s]]" % (n, mm.group(0)) if n else mm.group(0)
        return prefix + m.group(0)[len(prefix):len(m.group(0)) - len(nums)] + re.sub(r"\d{2}", one, nums)
    body = re.sub(r"(Dok\.|Dokumente|Dokument|Doc\.|Docs)\s*(%s)" % NUMS, repl_dok, body)

    # 5) Masken zurück
    body = re.sub(r"\x00CODE(\d+)\x00", lambda m: spans[int(m.group(1))], body)
    body = re.sub(r"\x00FENCE(\d+)\x00", lambda m: fences[int(m.group(1))], body)
    return body, mentioned

# ---------------------------------------------------------------- Notizen

def rel_lines(node_id, edges, link, outgoing=True):
    lines = []
    for e in edges:
        src, dst = (e["from"], e["to"]) if outgoing else (e["to"], e["from"])
        if src != node_id or dst not in link:
            continue
        label = REL_DE.get(e["type"], (e["type"], e["type"]))[0 if outgoing else 1]
        arrow = "→" if outgoing else "←"
        note = (" — *%s*" % e["note"]) if e.get("note") else ""
        lines.append("- **%s** %s [[%s]]%s" % (label, arrow, link[dst][0], note))
    return sorted(set(lines))

def graph_section(node_id, edges, link, claims_by_doc=None, mentioned=None, link_docs=None):
    out = ["\n---\n", "## 🔗 Wissensgraph"]
    for title, ls in (("### Ausgehende Relationen", rel_lines(node_id, edges, link, True)),
                      ("### Eingehende Relationen", rel_lines(node_id, edges, link, False))):
        if ls:
            out += ["", title, ""] + ls
    if claims_by_doc:
        cl = claims_by_doc.get(node_id, [])
        if cl:
            out += ["", "### Belegte Aussagen (Claims)", ""]
            out += ["- `[%s]` [[%s]] — %s" % (STATUS_DE.get(c["status"], c["status"]),
                                              sanitize(c["id"]), c["statement"]) for c in cl]
    if mentioned:
        linked = {e["to"] for e in edges if e["from"] == node_id} | {e["from"] for e in edges if e["to"] == node_id}
        extra = sorted(mentioned - linked)
        if extra:
            out += ["", "### Im Text erwähnt", ""]
            out += ["- [[%s]]" % link[d][0] for d in extra if d in link]
    return "\n".join(out) + "\n"

def doc_note(d, edges, link, claims_by_doc, section_of):
    body, mentioned = autolink(d["body"], d["id"], link, {k: v for k, v in link.items() if k.startswith("doc-")})
    cat = d.get("category", "")
    tags = ["dokument", "kategorie/" + slug_tag(cat), "status/" + slug_tag(d.get("status", ""))]
    tags += ["thema/" + slug_tag(t) for t in d.get("tags", []) if t]
    sec = section_of.get(d["id"])
    fm = ["---",
          "id: %s" % d["id"],
          'title: %s' % json.dumps(d["title"], ensure_ascii=False),
          "nummer: \"%s\"" % d["number"],
          "kategorie: %s" % (CATEGORY_DE.get(cat, cat) or "—"),
          "status: %s" % STATUS_DE.get(d.get("status", ""), d.get("status", "")),
          "typ: dokument",
          "aliases:" + yaml_list([d["id"], "Dok. %s" % d["number"]]),
          "tags:" + yaml_list(sorted(set(tags))),
          "quelle: %s" % d["file"],
          "---", ""]
    head = ["> [!info] Navigation",
            "> **Karte:** %s · **Kategorie:** %s · **Status:** `%s`" % (
                "[[%s]]" % sec if sec else "[[%s]]" % HUB,
                CATEGORY_DE.get(cat, cat) or "—", STATUS_DE.get(d.get("status", ""), "—")),
            "> **Zentrale Notiz:** [[%s]] · **Original:** `%s`" % (HUB, d["file"]), "", ""]
    tail = graph_section(d["id"], edges, link, claims_by_doc, mentioned)
    return "\n".join(fm + head) + body.strip() + "\n" + tail

def concept_note(c, edges, link, docs):
    kind = "Motiv" if c.get("type") == "motif" else "Konzept"
    fm = ["---",
          "id: %s" % c["id"],
          'title: %s' % json.dumps(c["label"], ensure_ascii=False),
          "typ: %s" % kind.lower(),
          "aliases:" + yaml_list([c["id"]]),
          "tags:" + yaml_list(["konzept", "typ/" + slug_tag(kind)]),
          "---", "",
          "# %s" % c["label"], "",
          "> [!abstract] %s" % kind,
          "> %s" % c.get("summary", ""), "",
          "**Zentrale Notiz:** [[%s]]" % HUB, ""]
    return "\n".join(fm) + graph_section(c["id"], edges, link)

def claim_note(c, link):
    doc = link.get(c.get("doc", ""))
    fm = ["---",
          "id: %s" % c["id"],
          "typ: claim",
          "status: %s" % STATUS_DE.get(c["status"], c["status"]),
          "art: %s" % c.get("kind", ""),
          "tags:" + yaml_list(["claim", "claim-status/" + slug_tag(c["status"]),
                               "claim-art/" + slug_tag(c.get("kind", ""))]),
          "quelle: %s" % json.dumps(c.get("source", ""), ensure_ascii=False),
          "---", "",
          "# %s" % c["id"], "",
          "> [!%s] Status: %s" % ({"proven": "success", "refuted": "failure"}.get(c["status"], "question"),
                                  STATUS_DE.get(c["status"], c["status"])),
          "> %s" % c["statement"], "",
          "- **Art:** %s" % c.get("kind", "—"),
          "- **Quelle:** %s" % (c.get("source") or "—"),
          "- **Beleg-Dokument:** %s" % ("[[%s]]" % doc[0] if doc else "—"),
          "- **Zentrale Notiz:** [[%s]]" % HUB, ""]
    return "\n".join(fm)

def moc_note(letter, title, ids, docs, link, edges):
    name = sanitize("MOC %s – %s" % (letter, title))
    fm = ["---",
          'title: %s' % json.dumps("MOC %s. %s" % (letter, title), ensure_ascii=False),
          "typ: karte",
          "tags:" + yaml_list(["moc"]),
          "---", "",
          "# %s. %s" % (letter, title), "",
          "> [!map] Themen-Karte — Teil von [[%s]]" % HUB, "",
          "## Dokumente dieser Gruppe", ""]
    for did in ids:
        d = docs.get(did)
        if not d:
            continue
        deg = sum(1 for e in edges if did in (e["from"], e["to"]))
        fm.append("- [[%s]] — `%s` · %d Verknüpfung%s" % (
            link[did][0], STATUS_DE.get(d.get("status", ""), "—"), deg, "" if deg == 1 else "en"))
    return name, "\n".join(fm) + "\n"

# ---------------------------------------------------------------- Übersicht

def short_label(title, width=32):
    """Kurzes, an Wortgrenzen abgeschnittenes Label für Mermaid-Knoten."""
    t = title.split("—")[0].split(":")[0].strip().replace('"', "'")
    if len(t) <= width:
        return t
    cut = t[:width].rsplit(" ", 1)[0]
    return cut + "…"

def mermaid_overview(docs, concepts, edges, link):
    """Kompakte Mermaid-Karte: Konzepte/Motive und ihre direkten Dokument-Relationen."""
    def nid(x):
        return re.sub(r"[^A-Za-z0-9]", "_", x)
    lines = ["```mermaid", "graph LR"]
    for c in concepts:
        lines.append('  %s(["%s"])' % (nid(c["id"]), c["label"].replace('"', "'")))
    seen = set()
    for e in edges:
        if not (e["from"].startswith("concept") or e["to"].startswith("concept")):
            continue
        a, b = e["from"], e["to"]
        if a not in link or b not in link:
            continue
        for x in (a, b):
            if x.startswith("doc-") and x not in seen:
                seen.add(x)
                lines.append('  %s["%s %s"]' % (nid(x), docs[x]["number"], short_label(docs[x]["title"])))
        lines.append("  %s -->|%s| %s" % (nid(a), REL_DE.get(e["type"], (e["type"],))[0], nid(b)))
    lines.append("```")
    return "\n".join(lines)

OVERVIEW = "Gesamtüberblick (EN) – Alle Ansätze in einem Dokument"

def overview_note(link, docs):
    """Die englische Gesamtübersicht (Repo-Wurzel) als eigene, verlinkte Notiz."""
    raw = open(os.path.join(ROOT, "Riemann_Hypothesis_Proof_Approaches.md"), encoding="utf-8").read()
    _, body = parse_frontmatter(raw)
    body, mentioned = autolink(body, "", link, {k: v for k, v in link.items() if k.startswith("doc-")})
    head = ["---", 'title: %s' % json.dumps(OVERVIEW, ensure_ascii=False), "typ: uebersicht",
            "tags:" + yaml_list(["uebersicht", "sprache/en"]),
            "quelle: Riemann_Hypothesis_Proof_Approaches.md", "---", "",
            "> [!abstract] Gesamtüberblick",
            "> Die zusammenfassende Gesamtübersicht aller Ansätze in einem Stück (englisch).",
            "> Die vertiefte, verlinkte Fassung liegt in `Dokumente/` — Einstieg: [[%s]]." % HUB, "", ""]
    tail = ["\n---\n", "## 🔗 Wissensgraph", "", "### Im Text erwähnt", ""]
    tail += ["- [[%s]]" % link[d][0] for d in sorted(mentioned) if d in link]
    tail += ["", "**Zentrale Notiz:** [[%s]]" % HUB, ""]
    return "\n".join(head) + body.strip() + "\n" + "\n".join(tail)

def hub_note(docs, concepts, edges, claims, link, sections, moc_names):
    deg = collections.Counter()
    for e in edges:
        deg[e["from"]] += 1
        deg[e["to"]] += 1
    cats = collections.Counter(d.get("category", "") for d in docs.values())
    rels = collections.Counter(e["type"] for e in edges)

    L = ["---",
         'title: "Riemann-Wissensnetz"',
         "typ: hub",
         "tags:" + yaml_list(["hub", "moc"]),
         "---", "",
         "# 🕸️ Riemann-Wissensnetz", "",
         "> [!tip] Einstiegspunkt",
         "> Diese Notiz bündelt **alle** Dokumente, Konzepte und Aussagen dieser Wissensbasis.",
         "> Öffne die **Graph-Ansicht** (`Strg/Cmd + G`), um zu sehen, welcher Ansatz mit welchem",
         "> verknüpft ist. Farben = Kategorien (siehe [[%s]])." % LEGEND, "",
         "**Bestand:** %d Dokumente · %d Konzepte/Motive · %d typisierte Relationen · %d Claims" % (
             len(docs), len(concepts), len(edges), len(claims)), "",
         "## 🗺️ Themen-Karten", ""]
    for (letter, title, ids), name in zip(sections, moc_names):
        L.append("- [[%s]] — %d %s" % (name, len(ids), "Dokument" if len(ids) == 1 else "Dokumente"))

    L.append("- [[%s]] — englische Gesamtübersicht in einem Stück" % OVERVIEW)

    L += ["", "## 🧭 Konzepte & Querschnittsmotive", ""]
    for c in concepts:
        L.append("- [[%s]] — %s *(%d Verknüpfungen)*" % (link[c["id"]][0], c.get("summary", ""), deg[c["id"]]))

    L += ["", "## 🔭 Karte der Ansätze (Mermaid)", "",
          mermaid_overview(docs, concepts, edges, link), ""]

    L += ["## ⭐ Am stärksten vernetzte Dokumente", ""]
    top = sorted((d for d in docs.values()), key=lambda d: -deg[d["id"]])[:12]
    for d in top:
        L.append("- [[%s]] — %d Verknüpfungen · `%s`" % (
            link[d["id"]][0], deg[d["id"]], STATUS_DE.get(d.get("status", ""), "—")))

    L += ["", "## 📚 Alle Dokumente (00–54)", ""]
    for did in sorted(docs, key=lambda x: docs[x]["number"]):
        d = docs[did]
        L.append("- `%s` [[%s]] — %s · `%s`" % (
            d["number"], link[did][0], CATEGORY_DE.get(d.get("category", ""), d.get("category", "")),
            STATUS_DE.get(d.get("status", ""), "—")))

    L += ["", "## 🧪 Aussagen nach Status", ""]
    by_status = collections.defaultdict(list)
    for c in claims:
        by_status[c["status"]].append(c)
    for st in ("proven", "open", "refuted"):
        if st not in by_status:
            continue
        L.append("### %s (%d)" % (STATUS_DE.get(st, st), len(by_status[st])))
        L.append("")
        for c in by_status[st]:
            L.append("- [[%s]] — %s" % (sanitize(c["id"]), c["statement"]))
        L.append("")

    L += ["## 📊 Verteilung", "",
          "| Kategorie | Dokumente |", "| --- | --- |"]
    for cat, n in cats.most_common():
        L.append("| %s | %d |" % (CATEGORY_DE.get(cat, cat), n))
    L += ["", "| Relationstyp | Kanten |", "| --- | --- |"]
    for r, n in rels.most_common():
        L.append("| %s (`%s`) | %d |" % (REL_DE.get(r, (r,))[0], r, n))
    L += ["", "---", "",
          "Bedienhinweise zum Vault: [[README]] · Kantentypen & Farben: [[%s]]" % LEGEND, "",
          "*Automatisch erzeugt von `kb/build_obsidian.py` — Änderungen am Inhalt bitte in `docs/` "
          "bzw. `kb/graph/` vornehmen und neu bauen.*", ""]
    return "\n".join(L)

def legend_note(edges):
    cnt = collections.Counter(e["type"] for e in edges)
    L = ["---", 'title: "Relationstypen (Legende)"', "typ: legende",
         "tags:" + yaml_list(["legende"]), "---", "",
         "# Relationstypen & Farben", "",
         "> [!note] Wie das Netz zu lesen ist",
         "> Jede Kante im Wissensgraph ist **typisiert**. Die Richtung steht in den Abschnitten",
         "> *Ausgehende / Eingehende Relationen* jeder Notiz.", "",
         "## Kantentypen", "", "| Typ | Bedeutung | Umkehrung | Anzahl |", "| --- | --- | --- | --- |"]
    for t, (fw, bw) in REL_DE.items():
        L.append("| `%s` | %s | %s | %d |" % (t, fw, bw, cnt.get(t, 0)))
    L += ["", "## Farbgruppen der Graph-Ansicht", "", "| Farbe (Tag) | Kategorie |", "| --- | --- |"]
    for cat, col in CATEGORY_COLOR.items():
        L.append("| `#kategorie/%s` — #%06X | %s |" % (slug_tag(cat), col, CATEGORY_DE.get(cat, cat)))
    L += ["", "## Status-Tags", "",
          "| Tag | Bedeutung |", "| --- | --- |"] + \
         ["| `#status/%s` | %s |" % (slug_tag(k), v) for k, v in STATUS_DE.items()] + \
         ["", "Zurück zu [[%s]]." % HUB, ""]
    return "\n".join(L)

# ---------------------------------------------------------------- Vault-Konfig

def obsidian_config():
    # keep_existing: eigene Obsidian-Einstellungen überleben ein Neubauen
    write(".obsidian/app.json", json.dumps({
        "alwaysUpdateLinks": True, "newLinkFormat": "shortest", "useMarkdownLinks": False,
        "attachmentFolderPath": "./", "showLineNumber": False, "readableLineLength": True,
    }, indent=2) + "\n", keep_existing=True)
    write(".obsidian/appearance.json", json.dumps(
        {"accentColor": "#9B6BFF", "theme": "obsidian"}, indent=2) + "\n", keep_existing=True)
    write(".obsidian/core-plugins.json", json.dumps({
        "file-explorer": True, "global-search": True, "switcher": True, "graph": True,
        "backlink": True, "outgoing-link": True, "tag-pane": True, "page-preview": True,
        "note-composer": True, "command-palette": True, "outline": True,
        "word-count": True, "file-recovery": True, "bookmarks": True,
    }, indent=2) + "\n", keep_existing=True)
    groups = [{"query": "tag:#kategorie/%s" % slug_tag(cat), "color": {"a": 1, "rgb": col}}
              for cat, col in CATEGORY_COLOR.items()]
    groups += [
        {"query": "path:%s/" % DIR_CONCEPTS, "color": {"a": 1, "rgb": 0xFFFFFF}},
        {"query": "path:%s/" % DIR_CLAIMS, "color": {"a": 1, "rgb": 0x7A8290}},
        {"query": "path:%s/" % DIR_MAPS, "color": {"a": 1, "rgb": 0x00D1FF}},
    ]
    write(".obsidian/graph.json", json.dumps({
        "collapse-filter": False, "search": "", "showTags": False, "showAttachments": False,
        "hideUnresolved": True, "showOrphans": True,
        "collapse-color-groups": False, "colorGroups": groups,
        "collapse-display": False, "showArrow": True, "textFadeMultiplier": -0.8,
        "nodeSizeMultiplier": 1.3, "lineSizeMultiplier": 1.1,
        "collapse-forces": False, "centerStrength": 0.42, "repelStrength": 11.5,
        "linkStrength": 0.85, "linkDistance": 210, "scale": 0.55, "close": False,
    }, indent=2) + "\n", keep_existing=True)

def vault_readme():
    return """# Obsidian-Vault: Riemann-Wissensnetz

Dieser Ordner **ist** ein fertiger Obsidian-Vault.

## Öffnen
1. Obsidian starten → *Ordner als Vault öffnen* → diesen Ordner (`obsidian/`) wählen.
2. Notiz **[[Riemann-Wissensnetz]]** öffnen (Einstiegspunkt).
3. Graph-Ansicht: `Strg/Cmd + G` — Farben zeigen die Kategorien, Pfeile die Relationsrichtung.

## Struktur
| Ordner | Inhalt |
| --- | --- |
| `Riemann-Wissensnetz.md` | Zentrale Übersicht: alle Dokumente, Konzepte, Claims, Statistik, Mermaid-Karte |
| `Dokumente/` | Je eine Notiz pro Wissensdokument (voller Text + typisierte Verknüpfungen) |
| `Konzepte/` | Konzepte und Querschnittsmotive (RH, Euler-Produkt, Positivität, Hilbert–Pólya …) |
| `Claims/` | Atomare Aussagen mit Status (BEWIESEN / OFFEN / WIDERLEGT) |
| `Karten/` | Themen-Karten (MOC) nach der Gliederung A–O + Relations-Legende |

## Neu erzeugen
```bash
python3 kb/build_obsidian.py
```
Der Vault wird vollständig aus `docs/`, `manifest.json` und `kb/graph/` regeneriert
(eigene Notizen daher **nicht** in diesem Ordner ablegen, sondern im Quellmaterial pflegen).

## Tipps für die Graph-Ansicht
- **Filter** `path:Dokumente` blendet Claims/Karten aus (reines Ansatz-Netz).
- **Filter** `tag:#status/offen` zeigt nur die noch offenen Programme.
- **Lokaler Graph** (`Strg/Cmd + P` → *Open local graph*) mit Tiefe 2 zeigt die Nachbarschaft
  eines einzelnen Ansatzes.
"""

# ---------------------------------------------------------------- main

def main():
    man, docs, concepts, edges, claims = load()
    link = build_link_index(docs, concepts)

    claims_by_doc = collections.defaultdict(list)
    for c in claims:
        claims_by_doc[c.get("doc", "")].append(c)

    sections = index_sections()
    section_of = {}
    moc_names = []
    for letter, title, ids in sections:
        name, _ = moc_note(letter, title, ids, docs, link, edges)
        moc_names.append(name)
        for did in ids:
            section_of[did] = name

    for sub in (DIR_DOCS, DIR_CONCEPTS, DIR_CLAIMS, DIR_MAPS):
        d = os.path.join(VAULT, sub)
        if os.path.isdir(d):
            shutil.rmtree(d)
    os.makedirs(VAULT, exist_ok=True)

    for did, d in docs.items():
        write("%s/%s.md" % (DIR_DOCS, link[did][0]), doc_note(d, edges, link, claims_by_doc, section_of))
    for c in concepts:
        write("%s/%s.md" % (DIR_CONCEPTS, link[c["id"]][0]), concept_note(c, edges, link, docs))
    for c in claims:
        write("%s/%s.md" % (DIR_CLAIMS, sanitize(c["id"])), claim_note(c, link))
    for (letter, title, ids), name in zip(sections, moc_names):
        _, text = moc_note(letter, title, ids, docs, link, edges)
        write("%s/%s.md" % (DIR_MAPS, name), text)

    write("%s/%s.md" % (DIR_MAPS, LEGEND), legend_note(edges))
    write("%s/%s.md" % (DIR_MAPS, sanitize(OVERVIEW)), overview_note(link, docs))
    write("%s.md" % HUB, hub_note(docs, concepts, edges, claims, link, sections, moc_names))
    write("README.md", vault_readme())
    obsidian_config()

    n = sum(len(fs) for _, _, fs in os.walk(VAULT))
    print("obsidian/ gebaut: %d Dateien (%d Dokumente, %d Konzepte, %d Claims, %d Karten)"
          % (n, len(docs), len(concepts), len(claims), len(moc_names) + 1))

if __name__ == "__main__":
    main()
