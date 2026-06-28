#!/usr/bin/env python3
"""
query.py — CLI zum Testen des Wissensgraph-RAG (ohne MCP, nur Stdlib).

Beispiele:
  python3 kb/query.py search "spektraler Operator Nullstellen" -k 5
  python3 kb/query.py neighbors concept-hilbert-polya
  python3 kb/query.py path doc-19 concept-RH
  python3 kb/query.py status refuted
  python3 kb/query.py claim "Mertens"
  python3 kb/query.py evaluate "Ich nutze die Funktionalgleichung und Wachstum von zeta"
  python3 kb/query.py stats
"""
import sys, json, argparse
import core

def show(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=2))

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("-k", type=int, default=6)
    s.add_argument("--status"); s.add_argument("--category")
    n = sub.add_parser("neighbors"); n.add_argument("node"); n.add_argument("--rel")
    pa = sub.add_parser("path"); pa.add_argument("a"); pa.add_argument("b"); pa.add_argument("--depth", type=int, default=5)
    st = sub.add_parser("status"); st.add_argument("status")
    cl = sub.add_parser("claim"); cl.add_argument("query")
    do = sub.add_parser("doc"); do.add_argument("node")
    ev = sub.add_parser("evaluate"); ev.add_argument("text")
    sub.add_parser("stats")
    a = p.parse_args()

    if a.cmd == "search":      show(core.search(a.query, a.k, a.status, a.category))
    elif a.cmd == "neighbors": show(core.graph_neighbors(a.node, a.rel))
    elif a.cmd == "path":      show(core.find_path(a.a, a.b, a.depth))
    elif a.cmd == "status":    show(core.list_by_status(a.status))
    elif a.cmd == "claim":     show(core.get_claim(a.query))
    elif a.cmd == "doc":       show(core.get_document(a.node))
    elif a.cmd == "evaluate":  show(core.evaluate_proof_idea(a.text))
    elif a.cmd == "stats":     show(core.stats())

if __name__ == "__main__":
    main()
