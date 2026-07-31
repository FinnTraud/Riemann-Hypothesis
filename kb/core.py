"""
core.py — Shared query logic over the built index (kb/index/kb.json).
Used by query.py (CLI) and server.py (MCP). Python stdlib only.

Functions:
  search(query, k, status, category)      -> hybrid BM25 hits (+ graph neighbors)
  get_document(node_id)                    -> full markdown + metadata
  graph_neighbors(node_id, rel)            -> typed neighbors
  find_path(a, b, max_depth)               -> shortest relation path
  list_by_status(status)                   -> documents/claims by status
  get_claim(query)                         -> matching atomic claims (with status)
  evaluate_proof_idea(text)                -> obstruction checklist (Doc 35/41/43/46)
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
            raise RuntimeError("Index missing. Run 'python3 kb/build_kb.py' first.")
        _KB = json.load(open(KB_JSON, encoding="utf-8"))
    return _KB

def _tok(s):
    return [w.lower() for w in WORD.findall(s)]

# ---------- Hybrid retrieval (BM25 + semantics + graph expansion) ----------
def search(query, k=6, status=None, category=None, expand_graph=True, semantic=True, alpha=0.6):
    """Hybrid: alpha·BM25 + (1-alpha)·semantics (embeddings/TF-IDF), then graph expansion.
    semantic=False switches to purely lexical (BM25). alpha weights BM25 vs. semantics."""
    K = kb(); idf = K["idf"]; avgdl = K["avgdl"]; b, k1 = 0.75, 1.5
    q = _tok(query)
    bm25 = {}
    for c in K["chunks"]:
        if status and c["status"] != status:      continue
        if category and c["category"] != category: continue
        s = 0.0
        for t in q:
            if t in c["tf"]:
                f = c["tf"][t]
                s += idf.get(t, 0.0) * (f*(k1+1)) / (f + k1*(1 - b + b*c["len"]/avgdl))
        if s > 0:
            bm25[c["cid"]] = s
    # semantic scores (optional)
    sem = {}
    backend = None
    if semantic:
        try:
            import embed
            backend = embed.backend_name()
            sem = embed.semantic_scores(query)
        except Exception:
            sem = {}
    # normalize and blend
    def _norm(d):
        if not d: return {}
        mx = max(d.values()) or 1.0
        return {k_: v/mx for k_, v in d.items()}
    bn, sn = _norm(bm25), _norm(sem)
    cmap = {c["cid"]: c for c in K["chunks"]}
    combined = {}
    cand = set(bm25) | (set(sem) & set(cmap))
    for cid in cand:
        c = cmap.get(cid)
        if not c: continue
        if status and c["status"] != status:      continue
        if category and c["category"] != category: continue
        combined[cid] = alpha*bn.get(cid, 0.0) + (1-alpha)*sn.get(cid, 0.0)
    scored = sorted(((v, cmap[cid]) for cid, v in combined.items()), key=lambda x: -x[0])
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
    return {"query": query, "retrieval": f"hybrid(bm25+{backend or 'none'})",
            "hits": hits, "graph_related": related[:12]}

def _snippet(text, n=320):
    t = re.sub(r"\s+", " ", text).strip()
    return t[:n] + ("…" if len(t) > n else "")

# ---------- Documents ----------
def get_document(node_id):
    K = kb(); n = K["nodes"].get(node_id)
    if not n: return {"error": f"unknown node: {node_id}"}
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
        return {"error": f"unknown node: {node_id}"}
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
        return {"error": "unknown node"}
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
    return {"path": None, "note": f"no path ≤{max_depth} steps"}

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

# ---------- Check a proof idea against known obstructions ----------
_CHECKS = [
    ("euler_product",
     "Does the idea make essential use of the Euler product / multiplicativity?",
     ["euler", "product", "prime", "multiplicative", "p^"],
     "If NO: probably wrong — Davenport–Heilbronn/Epstein (Doc 35/43) share the same soft properties but have off-line zeros.",
     "doc-43"),
    ("positivity_proved",
     "Is a positivity (Li/Weil/de Branges) proved rather than assumed?",
     ["positive", "positivity", "nonnegative", "λ_n", "lambda", "quadratic form"],
     "If positivity is only ASSUMED: circular (Conrey–Li refuted exactly that for de Branges, Doc 20).",
     "doc-14"),
    ("operator_canonical",
     "Does any operator arise CANONICALLY from arithmetic?",
     ["operator", "self-adjoint", "selfadjoint", "spectrum", "eigenvalue", "hamiltonian"],
     "An ad-hoc operator with spectrum {γ_n} is circular (gap in Bender–Brody–Müller, Doc 09).",
     "doc-05"),
    ("not_only_numeric",
     "Does the idea rest on more than just finite numerics?",
     ["numeric", "numerical", "computed", "verified up to", "10^"],
     "Finite numerics prove nothing: Mertens conjecture (OK up to 10^14, yet false) and Skewes (Doc 35).",
     "doc-35"),
    ("not_soft_function_theory",
     "Does the idea avoid purely 'soft' function theory to the right of Re=1/2?",
     ["growth", "approximation", "continuous", "holomorphic", "modulus", "magnitude"],
     "Voronin universality (Doc 46): ζ approximates every zero-free function there ⇒ soft arguments cannot pin down the location of the zeros.",
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
            "verdict": "ok-signal present" if present else "MISSING — check",
            "warning_if_missing": None if present else warning,
            "see": ref,
        })
    flags = [r for r in results if not r["signal_found"]]
    summary = ("Several obstruction signals are missing — most likely "
               "not a valid proof." if len(flags) >= 2 else
               "Basic signals present — still check rigorously against Doc 35/41/43/46 "
               "and ideally verify in Lean (Doc 37).")
    return {"idea": text[:500], "checklist": results,
            "missing_count": len(flags), "summary": summary,
            "always_see": ["doc-35", "doc-41", "doc-43", "doc-46", "doc-37"]}

def stats():
    K = kb()
    by_status = collections.Counter(n.get("status") for n in K["nodes"].values() if n.get("type") == "document")
    return {"meta": K["meta"], "documents_by_status": dict(by_status)}

# ---------- Structured reasoning protocol ----------
def reasoning_scaffold(task=""):
    """Returns the 7-step protocol (docs/50), tailored to the task:
    enforces classification, assumptions, status separation, obstruction check, experiment."""
    t = (task or "").lower()
    is_proof = any(w in t for w in ["proof", "prove", "show", "follows", "impl"])
    steps = [
        {"step": 1, "name": "Make the question precise",
         "do": "Note the claim formally (ζ, ξ, ρ=β+iγ). RH/GRH/criterion/partial result?",
         "tools": ["get_claim", "search"]},
        {"step": 2, "name": "Classify the leitmotiv",
         "do": "Positivity(A)/spectral(B)/geometry(C)? Find related approaches.",
         "tools": ["graph_neighbors", "find_path"]},
        {"step": 3, "name": "Make assumptions explicit",
         "do": "Mark prerequisites; check the status of each one.",
         "tools": ["get_claim"]},
        {"step": 4, "name": "Separate status",
         "do": "[PROVEN]/[OPEN]/[EVIDENCE]/[HEURISTIC]. Never use refuted results as a building block.",
         "tools": ["list_by_status"]},
        {"step": 5, "name": "Obstruction check",
         "do": "Euler product? Positivity proved? Operator canonical? only numerics? Voronin?",
         "tools": ["evaluate_proof_idea", "get_document(doc-35)", "get_document(doc-43)"]},
        {"step": 6, "name": "Experiment/verification",
         "do": "Test numerically, state falsifiably, formalize in Lean if possible.",
         "tools": ["compute_first_zeros", "compute_li_coefficient", "compute_count_zeros", "plot_*"]},
        {"step": 7, "name": "Honest conclusion",
         "do": "established / open / next testable step. No overselling.",
         "tools": []},
    ]
    note = ("PROOF MODE: step 5 is MANDATORY; do not speak of a 'proof' "
            "without a passed obstruction check."
            if is_proof else
            "Analysis mode: still separate status cleanly and provide tool-backed evidence.")
    return {"task": task, "protocol": steps, "mode_note": note,
            "answer_template": ("QUESTION(formal) / CLASS / ASSUMPTIONS[status] / "
                                "ANALYSIS[PROVEN|OPEN|EVIDENCE] / OBSTRUCTION CHECK / "
                                "EXPERIMENT / CONCLUSION"),
            "see": "docs/50_reasoning_protocol.md"}
