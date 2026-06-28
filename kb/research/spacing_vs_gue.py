#!/usr/bin/env python3
"""
spacing_vs_gue.py — Flaggschiff-Experiment: Folgen die Abstände der ζ-Nullstellen
der GUE-Statistik der Zufallsmatrixtheorie (Montgomery–Odlyzko-Gesetz, docs/06)?

Methode (reproduzierbar, mpmath-genau):
  - erste N Nullstellen γ_k, lokal auf mittleren Abstand 1 normiert,
  - empirische Statistik (Mittel, Varianz, kleinste-Abstände-Anteil),
  - Vergleich mit GUE (Wigner-Surmise) und Poisson,
  - KS-artige Maximaldistanz der kumulativen Verteilungen.

Ergebnis wird ins Experiment-Logbuch geschrieben und als Research-Note gespeichert.
Aufruf:  python3 kb/research/spacing_vs_gue.py [N]
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mpmath as mp
import compute, experiment

def wigner_pdf(s):      # GUE (β=2) Näherung
    return (32/math.pi**2) * s*s * math.exp(-4*s*s/math.pi)

def wigner_cdf(s, steps=400):
    h = s/steps; acc = 0.0
    for i in range(steps):
        x = (i+0.5)*h; acc += wigner_pdf(x)*h
    return acc

def run(N=500):
    mp.mp.dps = 25
    gammas = [float(mp.im(compute._zero(k))) for k in range(1, N+1)]
    # lokale Normierung mit mittlerer Dichte (log(γ/2π))/2π
    spac = []
    for i in range(1, N):
        g = gammas[i]
        dens = math.log(g/(2*math.pi))/(2*math.pi)
        spac.append((gammas[i]-gammas[i-1]) * dens)
    spac.sort()
    M = len(spac)
    mean = sum(spac)/M
    var = sum((x-mean)**2 for x in spac)/M
    frac_small = sum(1 for x in spac if x < 0.5)/M     # Niveau-Abstoßung: wenige kleine Abstände
    # KS-Distanz zur GUE-CDF
    ks = 0.0
    for i, x in enumerate(spac):
        emp = (i+1)/M
        ks = max(ks, abs(emp - wigner_cdf(x)))
    # GUE-Referenzwerte
    gue_var = 0.1781   # Var der GUE-Abstände (β=2), ~0.178
    poisson_var = 1.0
    result = {
        "num_zeros": N, "num_spacings": M,
        "mean_spacing": round(mean, 4),
        "variance": round(var, 4),
        "gue_variance_ref": gue_var, "poisson_variance_ref": poisson_var,
        "closer_to": "GUE" if abs(var-gue_var) < abs(var-poisson_var) else "Poisson",
        "fraction_spacings_below_0.5": round(frac_small, 4),
        "ks_distance_to_GUE": round(ks, 4),
    }
    return result, gammas

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    result, _ = run(N)
    print("Ergebnis:")
    for k, v in result.items():
        print(f"  {k}: {v}")
    log = experiment.log_experiment(
        hypothesis=("Die normierten Abstände der Riemann-Nullstellen folgen der GUE-Statistik "
                    "(Montgomery–Odlyzko-Gesetz), nicht der Poisson-Statistik."),
        method="erste N Nullstellen (mpmath), lokale Normierung, Var/KS gegen GUE & Poisson",
        params={"N": N},
        result=result,
        conclusion=(f"Varianz {result['variance']} liegt näher an GUE ({result['gue_variance_ref']}) "
                    f"als an Poisson (1.0); KS-Distanz zur GUE-CDF = {result['ks_distance_to_GUE']}. "
                    "Konsistent mit dem Zufallsmatrix-Bild der RH (Evidenz, kein Beweis)."),
        tags=["gue", "montgomery-odlyzko", "paarkorrelation", "flaggschiff"])
    print("\nProtokolliert:", log["id"], "->", log["markdown"])

if __name__ == "__main__":
    main()
