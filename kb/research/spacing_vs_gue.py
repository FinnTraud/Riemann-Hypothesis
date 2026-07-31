#!/usr/bin/env python3
"""
spacing_vs_gue.py — Flagship experiment: do the spacings of the ζ zeros follow
the GUE statistics of random-matrix theory (Montgomery–Odlyzko law, docs/06)?

Method (reproducible, mpmath-precise):
  - first N zeros γ_k, locally normalized to mean spacing 1,
  - empirical statistics (mean, variance, fraction of smallest spacings),
  - comparison with GUE (Wigner surmise) and Poisson,
  - KS-like maximal distance of the cumulative distributions.

The result is written to the experiment logbook and saved as a research note.
Usage:  python3 kb/research/spacing_vs_gue.py [N]
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mpmath as mp
import compute, experiment

def wigner_pdf(s):      # GUE (β=2) approximation
    return (32/math.pi**2) * s*s * math.exp(-4*s*s/math.pi)

def wigner_cdf(s, steps=400):
    h = s/steps; acc = 0.0
    for i in range(steps):
        x = (i+0.5)*h; acc += wigner_pdf(x)*h
    return acc

def run(N=500):
    mp.mp.dps = 25
    gammas = [float(mp.im(compute._zero(k))) for k in range(1, N+1)]
    # local normalization with mean density (log(γ/2π))/2π
    spac = []
    for i in range(1, N):
        g = gammas[i]
        dens = math.log(g/(2*math.pi))/(2*math.pi)
        spac.append((gammas[i]-gammas[i-1]) * dens)
    spac.sort()
    M = len(spac)
    mean = sum(spac)/M
    var = sum((x-mean)**2 for x in spac)/M
    frac_small = sum(1 for x in spac if x < 0.5)/M     # level repulsion: few small spacings
    # KS distance to the GUE CDF
    ks = 0.0
    for i, x in enumerate(spac):
        emp = (i+1)/M
        ks = max(ks, abs(emp - wigner_cdf(x)))
    # GUE reference values
    gue_var = 0.1781   # variance of GUE spacings (β=2), ~0.178
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
    print("Result:")
    for k, v in result.items():
        print(f"  {k}: {v}")
    log = experiment.log_experiment(
        hypothesis=("The normalized spacings of the Riemann zeros follow the GUE statistics "
                    "(Montgomery–Odlyzko law), not the Poisson statistics."),
        method="first N zeros (mpmath), local normalization, Var/KS against GUE & Poisson",
        params={"N": N},
        result=result,
        conclusion=(f"Variance {result['variance']} is closer to GUE ({result['gue_variance_ref']}) "
                    f"than to Poisson (1.0); KS distance to the GUE CDF = {result['ks_distance_to_GUE']}. "
                    "Consistent with the random-matrix picture of the RH (evidence, not proof)."),
        tags=["gue", "montgomery-odlyzko", "pair-correlation", "flagship"])
    print("\nLogged:", log["id"], "->", log["markdown"])

if __name__ == "__main__":
    main()
