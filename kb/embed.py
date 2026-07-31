"""
embed.py — Semantic search layer (complements BM25 in core.search).

Strategy (automatic, with clean fallback):
  1. If `sentence-transformers` is installed -> real neural embeddings.
  2. Otherwise -> TF-IDF cosine over the already-built chunks (numpy, NO download).

This way semantic search works immediately and automatically improves as soon as an
embedding model is installed. Used by core.search (hybrid: α·BM25 + (1-α)·cos).
"""
import os, re, json, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_JSON = os.path.join(ROOT, "kb", "index", "kb.json")
WORD = re.compile(r"[A-Za-zÀ-ÿ0-9]+")

_STATE = {"backend": None, "ready": False}
_TFIDF = {"vecs": None, "cids": None, "idf": None}
_ST = {"model": None, "emb": None, "cids": None}

def _tok(s):
    return [w.lower() for w in WORD.findall(s)]

def _load_kb():
    return json.load(open(KB_JSON, encoding="utf-8"))

# ---------- Backend selection ----------
def init():
    if _STATE["ready"]:
        return _STATE["backend"]
    try:
        from sentence_transformers import SentenceTransformer  # noqa
        _init_st()
        _STATE["backend"] = "sentence-transformers"
    except Exception:
        _init_tfidf()
        _STATE["backend"] = "tfidf-cosine"
    _STATE["ready"] = True
    return _STATE["backend"]

# ---------- TF-IDF fallback (no download) ----------
def _init_tfidf():
    import numpy as np
    K = _load_kb()
    idf = K["idf"]
    chunks = K["chunks"]
    vocab = {t: i for i, t in enumerate(idf.keys())}
    V = len(vocab)
    cids, rows = [], []
    for c in chunks:
        v = np.zeros(V, dtype="float32")
        for t, f in c["tf"].items():
            j = vocab.get(t)
            if j is not None:
                v[j] = (1 + math.log(f)) * idf.get(t, 0.0)
        n = np.linalg.norm(v)
        if n > 0:
            v /= n
        rows.append(v); cids.append(c["cid"])
    _TFIDF["vecs"] = np.vstack(rows)
    _TFIDF["cids"] = cids
    _TFIDF["idf"] = idf
    _TFIDF["vocab"] = vocab

def _scores_tfidf(query):
    import numpy as np
    vocab = _TFIDF["vocab"]; idf = _TFIDF["idf"]
    q = np.zeros(len(vocab), dtype="float32")
    from collections import Counter
    for t, f in Counter(_tok(query)).items():
        j = vocab.get(t)
        if j is not None:
            q[j] = (1 + math.log(f)) * idf.get(t, 0.0)
    n = np.linalg.norm(q)
    if n == 0:
        return {}
    q /= n
    sims = _TFIDF["vecs"] @ q
    return {cid: float(s) for cid, s in zip(_TFIDF["cids"], sims)}

# ---------- Neural embeddings (if installed) ----------
def _init_st():
    import numpy as np
    from sentence_transformers import SentenceTransformer
    model_name = os.environ.get("RH_EMBED_MODEL", "all-MiniLM-L6-v2")
    model = SentenceTransformer(model_name)
    K = _load_kb()
    texts, cids = [], []
    for c in K["chunks"]:
        texts.append((c["doc_title"] + ". " + c["heading"] + ". " + c["text"])[:1000])
        cids.append(c["cid"])
    emb = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
    _ST["model"] = model; _ST["emb"] = np.asarray(emb, dtype="float32"); _ST["cids"] = cids

def _scores_st(query):
    import numpy as np
    q = _ST["model"].encode([query], normalize_embeddings=True)[0]
    sims = _ST["emb"] @ np.asarray(q, dtype="float32")
    return {cid: float(s) for cid, s in zip(_ST["cids"], sims)}

# ---------- public API ----------
def semantic_scores(query):
    """cid -> cosine similarity (0..1). Backend chosen automatically."""
    backend = init()
    return _scores_st(query) if backend == "sentence-transformers" else _scores_tfidf(query)

def backend_name():
    return init()
