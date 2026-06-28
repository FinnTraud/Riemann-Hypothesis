#!/usr/bin/env python3
"""
demo.py — Geführte Tour durch den RH-Forschungs-Server (für Einsteiger).
Erzeugt Figuren in kb/figures/, zeigt Beispielabfragen und protokolliert ein Experiment.

Aufruf:  python3 kb/demo.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core

def section(t): print("\n" + "="*70 + f"\n{t}\n" + "="*70)

def main():
    section("1) WISSEN — Suche + Graph")
    r = core.search("spektraler Operator Nullstellen", k=2)
    for h in r["hits"]:
        print(f"  [{h['status']}] {h['doc_title']}  ({h['heading']})")
    print("  Graph-Verwandte:", [g["to"] for g in r["graph_related"][:4]])

    section("2) STATUS — was ist bewiesen / widerlegt?")
    for st in ("proven", "refuted"):
        d = core.list_by_status(st)
        print(f"  {st}: {len(d['documents'])} Dokumente, Claims:",
              [c["id"] for c in d["claims"]][:4])

    section("3) DENKEN — strukturiertes Protokoll")
    sc = core.reasoning_scaffold("Ich will die RH beweisen")
    print("  Modus:", sc["mode_note"][:70])
    print("  Schritte:", " → ".join(s["name"] for s in sc["protocol"]))

    section("4) OBSTRUKTION — Beweisidee prüfen")
    ev = core.evaluate_proof_idea("Beweis nur mit Funktionalgleichung und Wachstum von zeta")
    print("  fehlende Signale:", ev["missing_count"], "→", ev["summary"][:60])

    try:
        import compute, visualize, experiment
    except Exception as e:
        print("\n(Numerik/Plots benötigen mpmath+matplotlib:", e, ")"); return

    section("5) RECHNEN — echte Zahlen (mpmath)")
    print("  1. Nullstelle γ =", compute.nth_zero(1)["gamma"])
    print("  λ_1 =", compute.li_coefficient(1)["lambda"], "(RH verlangt ≥0)")
    print("  N(50): exakt", compute.count_zeros(50)["exact_count"])

    section("6) VISUALISIEREN — Figuren erzeugen")
    for fn in (visualize.plot_Z_and_zeros(0, 50),
               visualize.plot_zeros_on_line(30),
               visualize.plot_counting_N(80)):
        print("  ", fn)

    section("7) EXPERIMENT-LOGBUCH — reproduzierbar")
    res = compute.verify_rh_range(1, 50)
    log = experiment.log_experiment(
        "Erste 50 Nullstellen liegen auf Re=1/2.",
        "mpmath.zetazero, max. Abweichung", {"n_start": 1, "n_end": 50},
        res, "Evidenz bestätigt; kein Beweis.", ["demo", "numerik"])
    print("  gespeichert:", log["id"], "->", log["markdown"])

    print("\nFertig. Figuren in kb/figures/, Protokoll in kb/experiments/.")

if __name__ == "__main__":
    main()
