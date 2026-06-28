"""
core.py — Gemeinsame Abfragelogik über den gebauten Index (kb/index/kb.json).
Genutzt von query.py (CLI) und server.py (MCP). Nur Python-Stdlib.

Funktionen:
  search(query, k, status, category)      -> Hybrid-BM25-Treffer (+ Graph-Nachbarn)
  get_document(node_id)                    -> volles Markdown + Metadaten
  graph_neighbors(node_id, rel)            -> typisierte Nachbarn
  find_path(a, b, max_depth)               -> kürzester Beziehungspfad
  list_by_status(status)                   -> Dokumente/Claims nach Status
  get_claim(query)                         -> passende atomare Claims (mit Status)
  evaluate_proof_idea(text)                -> Obstruktions-Checkliste (Doc 35/41/43/46)
"""
import os, re, json, math, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_JSON = os.path.join(ROOT, "kb", "index", "kb.json")
WORD = re.compile(r"[A-Za-zÀ-ÿ0-9]+")

_KB = None
def kb():
    global _KB
    if _KB is None:
        if not os.path.exists(KB_JSON):
            raise RuntimeError("Index fehlt. Erst 'python3 kb/build_kb.py' ausführen.")
        _KB = json.load(open(KB_JSON, encoding="utf-8"))
    return _KB

def _tok(s):
    return [w.lower() for w in WORD.findall(s)]

# ---------- Hybrid-Retrieval (BM25 + Graph-Expansion) ----------
def search(query, k=6, status=None, category=None, expand_graph=True):
    K = kb(); idf = K["idf"]; avgdl = K["avgdl"]; b, k1 = 0.75, 1.5
    q = _tok(query)
    scored = []
    for c in K["chunks"]:
        if status and c["status"] != status:      continue
        if category and c["category"] != category: continue
        s = 0.0
        for t in q:
            if t in c["tf"]:
                f = c["tf"][t]
                s += idf.get(t, 0.0) * (f*(k1+1)) / (f + k1*(1 - b + b*c["len"]/avgdl))
        if s > 0:
            scored.append((s, c))
    scored.sort(key=lambda x: -x[0])
    hits = []
    seen = set()
    for s, c in scored[:k]:
        hits.append({
            "score": round(s, 3), "node": c["node"], "doc_title": c["doc_title"],
            "heading": c["heading"], "status": c["status"], "category": c["category"],
            "file": c["file"], "snippet": _snippet(c["text"]),
        })
        seen.add(c["node"])
    related = []
    if expand_graph and hits:
        top_nodes = [h["node"] for h in hits[:3]]
        for nid in top_nodes:
            for e in _edges_of(nid):
                other = e["to"] if e["from"] == nid else e["from"]
                if other in seen: continue
                seen.add(other)
                n = K["nodes"].get(other, {})
                related.append({"from": nid, "type": e["type"], "to": other,
                                "label": n.get("label", other), "note": e.get("note", "")})
    return {"query": query, "hits": hits, "graph_related": related[:12]}

def _snippet(text, n=320):
    t = re.sub(r"\s+", " ", text).strip()
    return t[:n] + ("…" if len(t) > n else "")

# ---------- Dokumente ----------
def get_document(node_id):
    K = kb(); n = K["nodes"].get(node_id)
    if not n: return {"error": f"unbekannter Knoten: {node_id}"}
    out = dict(n)
    if n.get("type") == "document" and n.get("file"):
        p = os.path.join(ROOT, n["file"])
        if os.path.exists(p):
            out["content"] = open(p, encoding="utf-8").read()
    out["neighbors"] = graph_neighbors(node_id)["neighbors"]
    return out

# ---------- Graph ----------
def _edges_of(nid):
    return [e for e in kb()["edges"] if e["from"] == nid or e["to"] == nid]

def graph_neighbors(node_id, rel=None):
    K = kb()
    if node_id not in K["nodes"]:
        return {"error": f"unbekannter Knoten: {node_id}"}
    out = []
    for e in _edges_of(node_id):
        if rel and e["type"] != rel: continue
        direction = "out" if e["from"] == node_id else "in"
        other = e["to"] if direction == "out" else e["from"]
        n = K["nodes"].get(other, {})
        out.append({"direction": direction, "type": e["type"], "node": other,
                    "label": n.get("label", other), "status": n.get("status", ""),
                    "note": e.get("note", "")})
    return {"node": node_id, "label": K["nodes"][node_id].get("label", node_id),
            "neighbors": out}

def find_path(a, b, max_depth=5):
    K = kb()
    if a not in K["nodes"] or b not in K["nodes"]:
        return {"error": "unbekannter Knoten"}
    adj = collections.defaultdict(list)
    for e in K["edges"]:
        adj[e["from"]].append((e["to"], e["type"], "→"))
        adj[e["to"]].append((e["from"], e["type"], "←"))
    # BFS
    q = collections.deque([[ (a, None, None) ]])
    seen = {a}
    while q:
        path = q.popleft()
        cur = path[-1][0]
        if cur == b:
            return {"path": [{"node": n, "via": t, "dir": d,
                              "label": K["nodes"].get(n, {}).get("label", n)}
                             for (n, t, d) in path]}
        if len(path) > max_depth: continue
        for (nxt, typ, d) in adj[cur]:
            if nxt in seen: continue
            seen.add(nxt)
            q.append(path + [(nxt, typ, d)])
    return {"path": None, "note": f"kein Pfad ≤{max_depth} Schritte"}

# ---------- Status / Claims ----------
def list_by_status(status):
    K = kb()
    docs = [{"node": n["id"], "label": n["label"], "category": n.get("category", "")}
            for n in K["nodes"].values() if n.get("status") == status and n.get("type") == "document"]
    claims = [c for c in K["claims"] if c["status"] == status]
    return {"status": status, "documents": docs, "claims": claims}

def get_claim(query):
    K = kb(); q = set(_tok(query))
    scored = []
    for c in K["claims"]:
        toks = set(_tok(c["statement"] + " " + c.get("source", "") + " " + c["id"]))
        overlap = len(q & toks)
        if overlap:
            scored.append((overlap, c))
    scored.sort(key=lambda x: -x[0])
    return {"query": query, "claims": [c for _, c in scored[:8]]}

# ---------- Beweis-Idee gegen Obstruktionen prüfen ----------
_CHECKS = [
    ("euler_product",
     "Nutzt die Idee das Euler-Produkt / die Multiplikativität wesentlich?",
     ["euler", "produkt", "product", "prime", "primzahl", "multiplikativ", "p^"],
     "Wenn NEIN: vermutlich falsch — Davenport–Heilbronn/Epstein (Doc 35/43) haben dieselben weichen Eigenschaften, aber Off-Line-Nullstellen.",
     "doc-43"),
    ("positivity_proved",
     "Wird eine Positivität (Li/Weil/de Branges) bewiesen statt angenommen?",
     ["positiv", "positivity", "nichtnegativ", "λ_n", "lambda", "quadratische form"],
     "Wenn Positivität nur ANGENOMMEN wird: zirkulär (Conrey–Li widerlegten genau das bei de Branges, Doc 20).",
     "doc-14"),
    ("operator_canonical",
     "Stammt ein etwaiger Operator KANONISCH aus der Arithmetik?",
     ["operator", "selbstadjung", "self-adjoint", "spektrum", "eigenwert", "hamilton"],
     "Ein ad-hoc-Operator mit Spektrum {γ_n} ist zirkulär (Lücke bei Bender–Brody–Müller, Doc 09).",
     "doc-05"),
    ("not_only_numeric",
     "Beruht die Idee NICHT nur auf endlicher Numerik?",
     ["numerisch", "numerical", "computed", "verifiziert bis", "10^"],
     "Endliche Numerik beweist nichts: Mertens-Vermutung (bis 10^14 ok, dennoch falsch) und Skewes (Doc 35).",
     "doc-35"),
    ("not_soft_function_theory",
     "Vermeidet die Idee rein 'weiche' Funktionentheorie rechts von Re=1/2?",
     ["wachstum", "growth", "approximation", "stetig", "holomorph", "betrag"],
     "Voronin-Universalität (Doc 46): ζ approximiert dort jede nullstellenfreie Funktion ⇒ weiche Argumente können die Nullstellenlage nicht festlegen.",
     "doc-46"),
]
def evaluate_proof_idea(text):
    t = text.lower()
    results = []
    for key, question, kws, warning, ref in _CHECKS:
        present = any(kw in t for kw in kws)
        results.append({
            "check": key, "question": question,
            "signal_found": present,
            "verdict": "ok-Signal vorhanden" if present else "FEHLT — prüfen",
            "warning_if_missing": None if present else warning,
            "see": ref,
        })
    flags = [r for r in results if not r["signal_found"]]
    summary = ("Mehrere Obstruktions-Signale fehlen — mit hoher Wahrscheinlichkeit "
               "kein gültiger Beweis." if len(flags) >= 2 else
               "Grundsignale vorhanden — dennoch streng gegen Doc 35/41/43/46 prüfen "
               "und idealerweise in Lean (Doc 37) verifizieren.")
    return {"idea": text[:500], "checklist": results,
            "missing_count": len(flags), "summary": summary,
            "always_see": ["doc-35", "doc-41", "doc-43", "doc-46", "doc-37"]}

def stats():
    K = kb()
    by_status = collections.Counter(n.get("status") for n in K["nodes"].values() if n.get("type") == "document")
    return {"meta": K["meta"], "documents_by_status": dict(by_status)}
