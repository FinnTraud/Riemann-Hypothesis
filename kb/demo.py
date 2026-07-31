#!/usr/bin/env python3
"""
demo.py — Guided tour through the RH research server (for beginners).
Generates figures in kb/figures/, shows example queries, and logs an experiment.

Usage:  python3 kb/demo.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core

def section(t): print("\n" + "="*70 + f"\n{t}\n" + "="*70)

def main():
    section("1) KNOWLEDGE — search + graph")
    r = core.search("spectral operator zeros", k=2)
    for h in r["hits"]:
        print(f"  [{h['status']}] {h['doc_title']}  ({h['heading']})")
    print("  Graph-related:", [g["to"] for g in r["graph_related"][:4]])

    section("2) STATUS — what is proven / refuted?")
    for st in ("proven", "refuted"):
        d = core.list_by_status(st)
        print(f"  {st}: {len(d['documents'])} documents, claims:",
              [c["id"] for c in d["claims"]][:4])

    section("3) REASONING — structured protocol")
    sc = core.reasoning_scaffold("I want to prove the RH")
    print("  Mode:", sc["mode_note"][:70])
    print("  Steps:", " → ".join(s["name"] for s in sc["protocol"]))

    section("4) OBSTRUCTION — check a proof idea")
    ev = core.evaluate_proof_idea("Proof using only the functional equation and growth of zeta")
    print("  missing signals:", ev["missing_count"], "→", ev["summary"][:60])

    try:
        import compute, visualize, experiment
    except Exception as e:
        print("\n(Numerics/plots require mpmath+matplotlib:", e, ")"); return

    section("5) COMPUTE — real numbers (mpmath)")
    print("  1st zero γ =", compute.nth_zero(1)["gamma"])
    print("  λ_1 =", compute.li_coefficient(1)["lambda"], "(RH requires ≥0)")
    print("  N(50): exact", compute.count_zeros(50)["exact_count"])

    section("6) VISUALIZE — generate figures")
    for fn in (visualize.plot_Z_and_zeros(0, 50),
               visualize.plot_zeros_on_line(30),
               visualize.plot_counting_N(80)):
        print("  ", fn)

    section("7) EXPERIMENT LOGBOOK — reproducible")
    res = compute.verify_rh_range(1, 50)
    log = experiment.log_experiment(
        "The first 50 zeros lie on Re=1/2.",
        "mpmath.zetazero, max. deviation", {"n_start": 1, "n_end": 50},
        res, "Evidence confirmed; not a proof.", ["demo", "numerics"])
    print("  saved:", log["id"], "->", log["markdown"])

    print("\nDone. Figures in kb/figures/, log in kb/experiments/.")

if __name__ == "__main__":
    main()
