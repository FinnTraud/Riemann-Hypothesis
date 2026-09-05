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
Aufruf:  python3 kb/research/spacing_vs_gue.py [N]           # rechnen + protokollieren
         python3 kb/research/spacing_vs_gue.py [N] --figure  # zusaetzlich die Abbildung
         python3 kb/research/spacing_vs_gue.py [N] --figure-only  # nur Abbildung, kein Logbuch

Die berechneten gamma_k werden nach kb/research/results/zeros_gamma.json gecacht, damit
die Abbildung ohne erneute (teure) mpmath-Nullstellensuche neu erzeugt werden kann.
"""
import os, sys, math, json
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

RESULTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
ZEROS_CACHE = os.path.join(RESULTS, "zeros_gamma.json")

def _load_gammas(N):
    """γ_1..γ_N aus dem Cache, sonst via mpmath (und Cache auffuellen)."""
    cached = []
    if os.path.exists(ZEROS_CACHE):
        with open(ZEROS_CACHE, encoding="utf-8") as f:
            cached = json.load(f)["gammas"]
    if len(cached) >= N:
        return cached[:N]
    mp.mp.dps = 25
    gammas = [float(mp.im(compute._zero(k))) for k in range(1, N+1)]
    os.makedirs(RESULTS, exist_ok=True)
    with open(ZEROS_CACHE, "w", encoding="utf-8") as f:
        json.dump({"count": len(gammas), "dps": 25,
                   "note": "Imaginaerteile der ersten Nullstellen, mpmath.zetazero",
                   "gammas": gammas}, f, indent=1)
    return gammas

def normalized_spacings(gammas):
    """Abstaende, lokal auf mittleren Abstand 1 normiert: Dichte (log(γ/2π))/2π."""
    spac = []
    for i in range(1, len(gammas)):
        g = gammas[i]
        dens = math.log(g/(2*math.pi))/(2*math.pi)
        spac.append((gammas[i]-gammas[i-1]) * dens)
    return spac

def figure(gammas, name=None):
    """Abbildung: Abstandsverteilung gegen GUE (Wigner) und Poisson + kumulativer Vergleich."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    N = len(gammas)
    spac = sorted(normalized_spacings(gammas))
    M = len(spac)
    name = name or f"gue_spacing_N{N}.png"
    xs = [i*0.01 for i in range(1, 400)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6))
    ax1.hist(spac, bins=30, range=(0, 3.5), density=True,
             color="#9dc3e6", edgecolor="white", label=f"ζ-Nullstellen (N={N})")
    ax1.plot(xs, [wigner_pdf(x) for x in xs], color="#c00000", lw=2,
             label="GUE (Wigner-Vermutung)")
    ax1.plot(xs, [math.exp(-x) for x in xs], color="#404040", lw=1.6, ls="--",
             label="Poisson (unkorreliert)")
    ax1.set_xlim(0, 3.5)
    ax1.set_xlabel("normierter Abstand s"); ax1.set_ylabel("Dichte")
    ax1.set_title("Abstandsverteilung: Niveau-Abstoßung bei s→0")
    ax1.legend(fontsize=8)
    emp = [(i+1)/M for i in range(M)]
    gue = [wigner_cdf(x) for x in spac]
    ks_i = max(range(M), key=lambda i: abs(emp[i]-gue[i]))
    ax2.plot(spac, emp, color="#1f4e79", lw=1.8, label="empirisch")
    ax2.plot(xs, [wigner_cdf(x) for x in xs], color="#c00000", lw=1.6, label="GUE")
    ax2.plot(xs, [1-math.exp(-x) for x in xs], color="#404040", lw=1.4, ls="--",
             label="Poisson")
    ax2.vlines(spac[ks_i], min(emp[ks_i], gue[ks_i]), max(emp[ks_i], gue[ks_i]),
               color="black", lw=1.2)
    ax2.annotate(f"KS = {abs(emp[ks_i]-gue[ks_i]):.3f}",
                 xy=(spac[ks_i], (emp[ks_i]+gue[ks_i])/2), xytext=(8, -4),
                 textcoords="offset points", fontsize=8)
    ax2.set_xlim(0, 3.5); ax2.set_xlabel("normierter Abstand s"); ax2.set_ylabel("kumulativ")
    ax2.set_title("Kumulative Verteilung gegen GUE und Poisson")
    ax2.legend(fontsize=8)
    fig.suptitle("Abstände der ζ-Nullstellen folgen der GUE-Statistik (Montgomery–Odlyzko)",
                 fontsize=11)
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, name)
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path

def run(N=500):
    gammas = _load_gammas(N)
    spac = sorted(normalized_spacings(gammas))
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
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    N = int(args[0]) if args else 500
    if "--figure-only" in flags:
        print("Abbildung:", figure(_load_gammas(N)))
        return
    result, gammas = run(N)
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
    if "--figure" in flags:
        print("Abbildung:  ", figure(gammas))

if __name__ == "__main__":
    main()
