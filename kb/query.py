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

Vergleich & Fehleranalyse (siehe auch: python3 kb/compare.py):
  python3 kb/query.py compare doc-10 doc-31
  python3 kb/query.py bridge doc-52 doc-56
  python3 kb/query.py profile doc-13
  python3 kb/query.py failures                 # woran Ansätze am häufigsten scheitern
  python3 kb/query.py mode F9
  python3 kb/query.py diagnose "Ich konstruiere einen Operator mit den Nullstellen als Spektrum"
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
    sc = sub.add_parser("scaffold"); sc.add_argument("task", nargs="?", default="")
    z = sub.add_parser("zero"); z.add_argument("n", type=int)
    vr = sub.add_parser("verify"); vr.add_argument("start", type=int); vr.add_argument("end", type=int)
    li = sub.add_parser("li"); li.add_argument("n", type=int)
    sub.add_parser("stats")
    cp = sub.add_parser("compare"); cp.add_argument("keys", nargs="+")
    br = sub.add_parser("bridge"); br.add_argument("a"); br.add_argument("b")
    pr = sub.add_parser("profile"); pr.add_argument("key")
    sub.add_parser("failures")
    md = sub.add_parser("mode"); md.add_argument("mode_id")
    dg = sub.add_parser("diagnose"); dg.add_argument("text")
    la = sub.add_parser("approaches"); la.add_argument("filters", nargs="*",
        help="z. B. family=spectral equivalence=conditional failure_mode=F9")
    a = p.parse_args()

    if a.cmd in ("compare", "bridge", "profile", "failures", "mode", "diagnose", "approaches"):
        import compare
        if a.cmd == "compare":    show(compare.compare_approaches(a.keys)); return
        if a.cmd == "bridge":     show(compare.bridge(a.a, a.b)); return
        if a.cmd == "profile":    show(compare.approach_profile(a.key)); return
        if a.cmd == "failures":   show(compare.failure_statistics()); return
        if a.cmd == "mode":       show(compare.failure_mode(a.mode_id)); return
        if a.cmd == "diagnose":   show(compare.diagnose(a.text)); return
        if a.cmd == "approaches":
            show(compare.list_approaches(**dict(f.split("=", 1) for f in a.filters))); return

    if a.cmd in ("zero", "verify", "li"):
        import compute
        if a.cmd == "zero":   show(compute.nth_zero(a.n)); return
        if a.cmd == "verify": show(compute.verify_rh_range(a.start, a.end)); return
        if a.cmd == "li":     show(compute.li_coefficient(a.n)); return
    if a.cmd == "scaffold":
        show(core.reasoning_scaffold(a.task)); return

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
