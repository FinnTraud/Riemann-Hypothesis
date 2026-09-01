#!/usr/bin/env python3
"""
compare.py — Vergleichs- und Fehleranalyse-Schicht über den RH-Ansätzen.

Datenquellen (kuratiert, ohne Index-Build nutzbar):
  kb/graph/approaches.json     strukturierte Profile je Ansatz (Achsen siehe dort)
  kb/graph/failure_modes.json  Taxonomie der Fehlermodi F1..F15

Funktionen:
  list_approaches(**filter)      -> gefilterte Ansatzliste
  approach_profile(key)          -> ein Profil (id | doc-id | Titelfragment)
  compare_approaches([keys])     -> Achsen-Tabelle + Gemeinsamkeiten/Unterschiede
  bridge(a, b)                   -> Verknüpfung zweier Ansätze (Achsen, Fehlermodi, Graphpfad)
  failure_modes()                -> Taxonomie
  failure_mode(mode_id)          -> ein Modus + betroffene Ansätze
  failure_statistics()           -> woran Ansätze am häufigsten scheitern (aggregiert)
  diagnose(text)                 -> freie Beweisidee gegen alle Fehlermodi prüfen
  matrix_markdown()              -> Vergleichsmatrix als Markdown (für docs/69)
  failure_map_markdown()         -> Ansatz→Fehlermodus-Landkarte als Markdown (für docs/68)

Nur Python-Stdlib. CLI: python3 kb/compare.py <befehl> [args]
"""
import os, re, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH = os.path.join(ROOT, "kb", "graph")

_A = _F = None

def _data():
    global _A, _F
    if _A is None:
        _A = json.load(open(os.path.join(GRAPH, "approaches.json"), encoding="utf-8"))
        _F = json.load(open(os.path.join(GRAPH, "failure_modes.json"), encoding="utf-8"))
    return _A, _F

def approaches():
    return _data()[0]["approaches"]

def modes():
    return _data()[1]["modes"]

def axes():
    return _data()[0]["axes"]

def _mode_index():
    return {m["id"]: m for m in modes()}

# ---------------------------------------------------------------- Auflösung
def resolve(key):
    """Findet einen Ansatz über app-ID, doc-ID ('doc-10'), Dokumentnummer ('10')
    oder ein Fragment des Labels."""
    if not key:
        return None
    k = str(key).strip().lower()
    if re.fullmatch(r"\d{1,2}", k):
        k = "doc-%02d" % int(k)
    for a in approaches():
        if a["id"].lower() == k or a["doc"].lower() == k:
            return a
    hits = [a for a in approaches() if k in a["label"].lower()]
    if len(hits) == 1:
        return hits[0]
    if hits:
        return hits[0]
    return None

def list_approaches(family=None, status=None, equivalence=None, euler_product=None,
                    positivity=None, rigor=None, testable=None, formalizable=None,
                    failure_mode=None):
    """Filtert Ansätze über beliebige Achsen (alle Argumente optional)."""
    want = {"family": family, "status": status, "equivalence": equivalence,
            "euler_product": euler_product, "positivity": positivity, "rigor": rigor,
            "testable": testable, "formalizable": formalizable}
    out = []
    for a in approaches():
        if any(v and a.get(kk) != v for kk, v in want.items()):
            continue
        if failure_mode and failure_mode.upper() not in a["failure_modes"]:
            continue
        out.append({"id": a["id"], "doc": a["doc"], "label": a["label"],
                    "family": a["family"], "status": a["status"],
                    "equivalence": a["equivalence"], "failure_modes": a["failure_modes"]})
    return {"count": len(out), "filter": {k: v for k, v in
            list(want.items()) + [("failure_mode", failure_mode)] if v}, "approaches": out}

def approach_profile(key):
    a = resolve(key)
    if not a:
        return {"error": f"kein Ansatz gefunden für '{key}'",
                "hint": "IDs siehe list_approaches()"}
    MI = _mode_index()
    prof = dict(a)
    prof["failure_modes_detail"] = [
        {"id": f, "label": MI[f]["label"], "tier": MI[f]["tier"],
         "short": MI[f]["short"], "diagnostic": MI[f]["diagnostic"]}
        for f in a["failure_modes"] if f in MI]
    prof["blocking_tier"] = min([MI[f]["tier"] for f in a["failure_modes"] if f in MI] or [9])
    prof["see"] = ["docs/68_failure_anatomy.md", "docs/69_comparison_matrix.md", a["doc"]]
    return prof

# ---------------------------------------------------------------- Vergleich
COMPARE_AXES = ["family", "status", "equivalence", "euler_product", "positivity",
                "rigor", "evidence", "testable", "formalizable"]

def compare_approaches(keys, axes_wanted=None):
    """Stellt 2+ Ansätze achsenweise gegenüber und trennt Gemeinsames von Trennendem."""
    ax = axes_wanted or COMPARE_AXES
    items = []
    for k in keys:
        a = resolve(k)
        if not a:
            return {"error": f"kein Ansatz gefunden für '{k}'"}
        items.append(a)
    rows = []
    same, diff = [], []
    for x in ax:
        vals = [i.get(x, "") for i in items]
        rows.append({"axis": x, "values": vals, "identical": len(set(vals)) == 1})
        (same if len(set(vals)) == 1 else diff).append(x)
    fm_sets = [set(i["failure_modes"]) for i in items]
    shared_fm = set.intersection(*fm_sets) if fm_sets else set()
    MI = _mode_index()
    return {
        "approaches": [{"id": i["id"], "doc": i["doc"], "label": i["label"]} for i in items],
        "axes": rows,
        "identical_axes": same,
        "differing_axes": diff,
        "shared_failure_modes": [{"id": f, "label": MI[f]["label"], "tier": MI[f]["tier"]}
                                 for f in sorted(shared_fm)],
        "distinct_failure_modes": {i["id"]: sorted(set(i["failure_modes"]) - shared_fm)
                                   for i in items},
        "open_steps": {i["id"]: i["open_step"] for i in items},
        "levers": {i["id"]: i["lever"] for i in items},
        "reading": ("Gleiche Fehlermodi ⇒ die Ansätze scheitern am selben Punkt; "
                    "ein Fortschritt dort hilft beiden. Verschiedene Fehlermodi ⇒ "
                    "die Ansätze sind komplementär und können sich gegenseitig absichern."),
    }

def bridge(a_key, b_key, max_depth=5):
    """Verknüpft zwei Ansätze: gemeinsame Achsen, gemeinsame Fehlermodi, gemeinsame
    Graph-Nachbarn und (falls Index gebaut) der kürzeste Beziehungspfad im Wissensgraphen."""
    a, b = resolve(a_key), resolve(b_key)
    if not a or not b:
        return {"error": "Ansatz nicht gefunden"}
    MI = _mode_index()
    shared_fm = sorted(set(a["failure_modes"]) & set(b["failure_modes"]))
    shared_ax = {x: a[x] for x in COMPARE_AXES if a.get(x) == b.get(x)}
    out = {
        "from": {"id": a["id"], "doc": a["doc"], "label": a["label"]},
        "to": {"id": b["id"], "doc": b["doc"], "label": b["label"]},
        "shared_axes": shared_ax,
        "shared_failure_modes": [{"id": f, "label": MI[f]["label"], "tier": MI[f]["tier"],
                                  "diagnostic": MI[f]["diagnostic"]} for f in shared_fm],
    }
    # Graph-Ebene (optional, benötigt gebauten Index)
    try:
        import core
        out["graph_path"] = core.find_path(a["doc"], b["doc"], max_depth).get("path")
        na = {n["node"] for n in core.graph_neighbors(a["doc"])["neighbors"]}
        nb = {n["node"] for n in core.graph_neighbors(b["doc"])["neighbors"]}
        K = core.kb()
        out["shared_neighbors"] = [
            {"node": n, "label": K["nodes"].get(n, {}).get("label", n)} for n in sorted(na & nb)]
    except Exception as e:
        out["graph_path"] = None
        out["graph_note"] = f"Graph-Ebene nicht verfügbar ({e.__class__.__name__}); " \
                            "erst 'python3 kb/build_kb.py' ausführen."
    if shared_fm:
        out["verdict"] = ("Gemeinsame Blockade: beide Ansätze hängen an "
                          + ", ".join(f"{f} ({MI[f]['label']})" for f in shared_fm)
                          + ". Ein Durchbruch dort wirkt auf beide.")
    else:
        out["verdict"] = ("Komplementär: keine gemeinsamen Fehlermodi — der eine Ansatz "
                          "kann als unabhängige Gegenprobe für den anderen dienen.")
    return out

# ---------------------------------------------------------------- Fehlermodi
def failure_modes():
    return {"count": len(modes()), "modes": modes(),
            "tiers": {1: "fatal (widerlegt die Idee sofort)",
                      2: "blockierend (offener Kernschritt)",
                      3: "strukturell (kann prinzipiell nicht implizieren)"}}

def failure_mode(mode_id):
    MI = _mode_index()
    m = MI.get(str(mode_id).upper())
    if not m:
        by_slug = {x["slug"]: x for x in modes()}
        m = by_slug.get(str(mode_id).lower())
    if not m:
        return {"error": f"unbekannter Fehlermodus '{mode_id}'",
                "known": [x["id"] for x in modes()]}
    affected = [{"id": a["id"], "doc": a["doc"], "label": a["label"], "status": a["status"]}
                for a in approaches() if m["id"] in a["failure_modes"]]
    return {"mode": m, "affected_count": len(affected), "affected": affected}

def failure_statistics():
    """Aggregiert: woran scheitern Ansätze am häufigsten? Nach Häufigkeit, Tier und Familie."""
    A = approaches(); MI = _mode_index()
    cnt = collections.Counter()
    per_family = collections.defaultdict(collections.Counter)
    for a in A:
        for f in a["failure_modes"]:
            cnt[f] += 1
            per_family[a["family"]][f] += 1
    ranked = [{"id": f, "label": MI[f]["label"], "slug": MI[f]["slug"], "tier": MI[f]["tier"],
               "count": c, "share": round(100.0 * c / len(A), 1),
               "diagnostic": MI[f]["diagnostic"]}
              for f, c in cnt.most_common()]
    tier = collections.Counter()
    for f, c in cnt.items():
        tier[MI[f]["tier"]] += c
    # Familien-Signatur: der jeweils dominante Fehlermodus
    fam_sig = {}
    for fam, c in per_family.items():
        top = c.most_common(1)[0]
        fam_sig[fam] = {"dominant_mode": top[0], "label": MI[top[0]]["label"], "count": top[1],
                        "n_approaches": sum(1 for a in A if a["family"] == fam)}
    # Ansätze ohne Tier-1/2-Blocker = die "sauberen" (meist bewiesene Teilresultate)
    clean = [a["id"] for a in A
             if not any(MI[f]["tier"] <= 2 for f in a["failure_modes"])]
    return {
        "n_approaches": len(A),
        "ranked_failure_modes": ranked,
        "top3": [r["id"] + " " + r["label"] for r in ranked[:3]],
        "by_tier": {str(k): v for k, v in sorted(tier.items())},
        "by_family": fam_sig,
        "no_tier12_blocker": clean,
        "interpretation": (
            "Die drei häufigsten Modi sind die eigentlichen Engpässe der RH-Forschung: "
            "solange sie nicht adressiert werden, ist jeder neue Ansatz eine Variante "
            "eines bekannten Scheiterns. Siehe docs/68."),
    }

# ---------------------------------------------------------------- Diagnose
def diagnose(text):
    """Prüft eine frei formulierte Beweisidee gegen ALLE Fehlermodi (Stichwort-Heuristik).
    Ergänzt core.evaluate_proof_idea um die Fehlermodus-Ebene."""
    t = (text or "").lower()
    KW = {
        "F1": ["funktionalgleichung", "functional equation", "symmetrie", "s ↔ 1-s", "spiegel"],
        "F2": ["positiv", "positivity", "quadratische form", "spur", "trace"],
        "F3": ["operator", "spektrum", "eigenwert", "hamilton"],
        "F4": ["selbstadjungiert", "hilbertraum", "definitionsbereich", "randbedingung", "xp"],
        "F5": ["summe über nullstellen", "vertausch", "umordn", "grenzwert", "kontur"],
        "F6": ["numerisch", "berechnet", "computer", "bis 10", "verifiziert"],
        "F7": ["holomorph", "ganze funktion", "wachstum", "maximumprinzip", "approximation"],
        "F8": ["möbius", "mobius", "sieb", "sieve", "parität", "liouville", "mertens"],
        "F9": ["abgeschnitten", "truncat", "endlich", "matrix", "galerkin", "partialsumme", "cutoff"],
        "F10": ["funktionenkörper", "geometri", "frobenius", "kohomolog", "motiv", "arakelov", "f1"],
        "F11": ["äquivalent", "kriterium", "equivalent", "umformul"],
        "F12": ["konstante", "explizit", "gleichmäßig", "führer", "siegel"],
        "F13": ["anteil", "proportion", "mollifier", "mittelwert", "dichte"],
        "F14": ["zufallsmatrix", "gue", "statistik", "modell", "heuristik", "wahrscheinlich"],
        "F15": ["beweis", "proof", "theorem", "zeige"],
    }
    MI = _mode_index()
    hits, checks = [], []
    for m in modes():
        hit = any(kw in t for kw in KW.get(m["id"], []))
        checks.append({"mode": m["id"], "label": m["label"], "tier": m["tier"],
                       "triggered": hit, "diagnostic": m["diagnostic"],
                       "why": m["short"] if hit else None})
        if hit:
            hits.append(m)
    tier1 = [m["id"] for m in hits if m["tier"] == 1]
    return {
        "idea": (text or "")[:500],
        "triggered_modes": [{"id": m["id"], "label": m["label"], "tier": m["tier"],
                             "diagnostic": m["diagnostic"]} for m in hits],
        "checks": checks,
        "must_answer": [m["diagnostic"] for m in hits if m["tier"] <= 2],
        "summary": (
            "Tier-1-Modi berührt (" + ", ".join(tier1) + ") — diese Fragen MÜSSEN "
            "beantwortet werden, sonst ist die Idee bereits durch bekannte Gegenbeispiele "
            "erledigt." if tier1 else
            "Keine Tier-1-Modi erkannt (Stichwort-Heuristik!). Trotzdem docs/35, 41, 43, 57, 68 "
            "durchgehen und core.evaluate_proof_idea ergänzend nutzen."),
        "see": ["docs/68_failure_anatomy.md", "docs/35_obstructions_barriers.md",
                "docs/57_Beurling_generalized_primes.md"],
    }

# ---------------------------------------------------------------- Markdown-Export
_LABEL_SHORT = {"algebraic-geometric": "alg.-geom.", "probabilistic": "probab.",
                "computational": "rechner.", "spectral": "spektral", "analytic": "analytisch",
                "criterion": "Kriterium", "physical": "physikal."}

def _doclink(a, nav):
    """[[Dateiname|Label]] falls Datei bekannt, sonst nur Label."""
    fn = nav.get(a["doc"])
    return f"[[{fn}|{a['label']}]]" if fn else a["label"]

def _docnames():
    """doc-NN -> Dateiname ohne .md (für Obsidian-Wikilinks)."""
    out = {}
    docs = os.path.join(ROOT, "docs")
    for f in sorted(os.listdir(docs)):
        if f.endswith(".md") and re.match(r"\d\d_", f):
            out["doc-" + f[:2]] = f[:-3]
    return out

def matrix_markdown():
    """Vergleichsmatrix aller Ansätze als Markdown-Tabelle (Obsidian-Wikilinks)."""
    nav = _docnames()
    A = sorted(approaches(), key=lambda x: (x["family"], x["doc"]))
    lines = []
    lines.append("| Ansatz | Familie | Status | Implikation | Euler-Produkt | Positivität | Strenge | Testbar | Fehlermodi |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for a in A:
        lines.append("| {ln} | {fam} | {st} | {eq} | {ep} | {pos} | {rig} | {test} | {fm} |".format(
            ln=_doclink(a, nav), fam=_LABEL_SHORT.get(a["family"], a["family"]),
            st=a["status"], eq=a["equivalence"], ep=a["euler_product"], pos=a["positivity"],
            rig=a["rigor"], test=a["testable"], fm=" ".join("`%s`" % f for f in a["failure_modes"])))
    return "\n".join(lines)

def failure_map_markdown():
    """Fehlermodus → betroffene Ansätze, nach Häufigkeit sortiert (Markdown)."""
    nav = _docnames()
    stats = failure_statistics()
    MI = _mode_index()
    lines = []
    lines.append("| # | Fehlermodus | Tier | betroffen | Anteil | Prüffrage |")
    lines.append("|---|---|---|---|---|---|")
    for r in stats["ranked_failure_modes"]:
        lines.append("| `{id}` | {lab} | {t} | {c} | {s} % | {q} |".format(
            id=r["id"], lab=r["label"], t=r["tier"], c=r["count"], s=r["share"],
            q=r["diagnostic"]))
    lines.append("")
    for r in stats["ranked_failure_modes"]:
        aff = failure_mode(r["id"])["affected"]
        names = ", ".join(_doclink(resolve(a["id"]), nav) for a in aff)
        lines.append(f"- **`{r['id']}` {r['label']}** ({r['count']}): {names}")
    return "\n".join(lines)

# ---------------------------------------------------------------- CLI
def _print(x):
    print(json.dumps(x, ensure_ascii=False, indent=2))

def main(argv):
    if len(argv) < 2:
        print(__doc__)
        print("Befehle: list | profile <key> | compare <k1> <k2> [...] | bridge <a> <b> | "
              "modes | mode <F#> | stats | diagnose <text> | matrix | failuremap")
        return
    cmd, args = argv[1], argv[2:]
    if cmd == "list":
        _print(list_approaches(**dict(a.split("=", 1) for a in args)))
    elif cmd == "profile":
        _print(approach_profile(args[0]))
    elif cmd == "compare":
        _print(compare_approaches(args))
    elif cmd == "bridge":
        _print(bridge(args[0], args[1]))
    elif cmd == "modes":
        _print(failure_modes())
    elif cmd == "mode":
        _print(failure_mode(args[0]))
    elif cmd == "stats":
        _print(failure_statistics())
    elif cmd == "diagnose":
        _print(diagnose(" ".join(args)))
    elif cmd == "matrix":
        print(matrix_markdown())
    elif cmd == "failuremap":
        print(failure_map_markdown())
    else:
        print("unbekannter Befehl:", cmd)

if __name__ == "__main__":
    import sys
    main(sys.argv)
