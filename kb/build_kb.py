#!/usr/bin/env python3
"""
build_kb.py — Builds the combined knowledge index kb/index/kb.json from:
  - docs/*.md          (frontmatter + content, chunked per ## section)
  - manifest.json      (document metadata -> document nodes)
  - kb/graph/nodes.json, edges.json, claims.json  (curated graph + claims)

Python stdlib only. Output is a single JSON that is loaded by core.py.
Usage:  python3 kb/build_kb.py
"""
import os, re, json, glob, math, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
KB   = os.path.join(ROOT, "kb")
OUT  = os.path.join(KB, "index", "kb.json")

WORD = re.compile(r"[A-Za-zÀ-ÿ0-9]+")
def tokenize(text):
    return [w.lower() for w in WORD.findall(text)]

def parse_frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.splitlines():
        mm = re.match(r"([a-z_]+):\s*(.*)", line)
        if not mm:
            continue
        k, v = mm.group(1), mm.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        else:
            v = v.strip('"')
        fm[k] = v
    return fm, body

def chunk_by_section(body):
    """Splits the body into chunks per ## heading (H2)."""
    chunks = []
    # everything before the first ## is the 'intro' chunk
    parts = re.split(r"\n(?=## )", body)
    for part in parts:
        h = re.match(r"##\s+(.+)", part)
        heading = h.group(1).strip() if h else "intro"
        text = part.strip()
        if len(text) < 15:
            continue
        chunks.append({"heading": heading, "text": text})
    return chunks

def main():
    # 1) Document nodes from manifest
    manifest_path = os.path.join(ROOT, "manifest.json")
    doc_nodes = {}
    if os.path.exists(manifest_path):
        man = json.load(open(manifest_path, encoding="utf-8"))
        for d in man["documents"]:
            nid = d["id"]
            doc_nodes[nid] = {
                "id": nid, "type": "document", "number": d["number"],
                "label": d["title"], "category": d["category"],
                "status": d["status"], "tags": d["tags"],
                "file": d["file"], "summary": d.get("summary", ""),
            }

    # 2) Chunks + BM25 statistics from the markdown documents
    chunks = []
    for path in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        fm, body = parse_frontmatter(open(path, encoding="utf-8").read())
        nid = fm.get("id") or ("doc-" + os.path.basename(path)[:2])
        for i, ch in enumerate(chunk_by_section(body)):
            cid = f"{nid}#{i}"
            toks = tokenize(ch["heading"] + " " + ch["text"] + " " + " ".join(fm.get("tags", [])))
            chunks.append({
                "cid": cid, "node": nid, "number": fm.get("number", ""),
                "doc_title": fm.get("title", ""), "heading": ch["heading"],
                "category": fm.get("category", ""), "status": fm.get("status", ""),
                "tags": fm.get("tags", []), "file": "docs/" + os.path.basename(path),
                "text": ch["text"], "tokens": toks,
            })

    # BM25 precomputation: df, idf, avgdl
    N = len(chunks)
    df = collections.Counter()
    for c in chunks:
        for t in set(c["tokens"]):
            df[t] += 1
    idf = {t: math.log(1 + (N - n + 0.5) / (n + 0.5)) for t, n in df.items()}
    avgdl = sum(len(c["tokens"]) for c in chunks) / max(N, 1)
    # store term frequencies per chunk (don't duplicate the tokens themselves)
    for c in chunks:
        c["tf"] = dict(collections.Counter(c["tokens"]))
        c["len"] = len(c["tokens"])
        del c["tokens"]

    # 3) Concept nodes + curated edges + claims
    concept_nodes = {}
    nodes_file = os.path.join(KB, "graph", "nodes.json")
    if os.path.exists(nodes_file):
        for c in json.load(open(nodes_file, encoding="utf-8")).get("concepts", []):
            concept_nodes[c["id"]] = c
    edges = []
    edges_file = os.path.join(KB, "graph", "edges.json")
    if os.path.exists(edges_file):
        edges = json.load(open(edges_file, encoding="utf-8")).get("edges", [])
    claims = []
    claims_file = os.path.join(KB, "graph", "claims.json")
    if os.path.exists(claims_file):
        claims = json.load(open(claims_file, encoding="utf-8")).get("claims", [])

    nodes = {**doc_nodes, **concept_nodes}

    # Validation: all edge endpoints exist as nodes
    missing = set()
    for e in edges:
        for end in (e["from"], e["to"]):
            if end not in nodes:
                missing.add(end)
    if missing:
        print("WARN: edges reference unknown nodes:", sorted(missing))

    kb = {
        "meta": {"chunks": N, "nodes": len(nodes), "edges": len(edges),
                 "claims": len(claims), "avgdl": avgdl},
        "idf": idf, "avgdl": avgdl,
        "chunks": chunks, "nodes": nodes, "edges": edges, "claims": claims,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(kb, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"OK -> {OUT}")
    print(f"   chunks={N}  nodes={len(nodes)}  edges={len(edges)}  claims={len(claims)}")

if __name__ == "__main__":
    main()
