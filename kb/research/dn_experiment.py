#!/usr/bin/env python3
"""
dn_experiment.py — Báez-Duarte/Nyman-Beurling-Distanz d_N (RH-Kriterium, docs/13/45).

Selbst hergeleitete, nachprüfbare Formulierung (Mellin-Transformation):
  Raum:      L²(0,1) (Lebesgue)
  Bausteine: g_n(x) = {1/(n x)},  n = 1..N
  Ziel:      konstante Funktion 1
  Distanz:   d_N² = min_c ||1 - Σ c_n g_n||²  =  1 - bᵀ G⁻¹ b
  exakt:     b_n = ∫₀¹ {1/(nx)} dx = (ln n + 1 - γ)/n
             G_mn = ∫₀¹ {1/(mx)}{1/(nx)} dx = ∫₁^∞ {u/m}{u/n} u⁻² du   (Subst. u=1/x)

G_mn wird STÜCKWEISE EXAKT integriert: zwischen den Sprungstellen (Vielfachen von m,n)
ist der Integrand (u/m-a)(u/n-b)u⁻² mit Stammfunktion in geschlossener Form; der Schwanz
∫_U0^∞ wird über den exakten Periodenmittelwert μ als μ/U0 angenähert (Restfehler O(1/U0²)).

RH-Kriterium (Báez-Duarte 2003): RH ⟺ d_N → 0.  Vermutung (BBLS 2000):
  (log N) · d_N²  →  Σ_ρ 1/|ρ|²  =  2 + γ - log(4π) ≈ 0.0462.

Numerik ist EVIDENZ, kein Beweis (docs/35). Aufruf: python3 kb/research/dn_experiment.py
"""
import os, sys, math
import numpy as np

GAMMA = 0.5772156649015328606
C_CONJ = 2 + GAMMA - math.log(4*math.pi)   # ≈ 0.0461914

def b_exact(n):
    """b_n = ∫₀¹ {1/(nx)} dx = (ln n + 1 - γ)/n  (exakt hergeleitet)."""
    return (math.log(n) + 1 - GAMMA) / n

def _period_mean(m, n):
    """Exakter Mittelwert von {u/m}{u/n} über eine Periode L=lcm(m,n)."""
    L = m*n // math.gcd(m, n)
    bps = sorted(set(list(range(0, L+1, 1))))  # 1er-Schritte genügen (Integrand stückw. linear an Ganzzahl-Vielfachen von m,n ⊂ Ganzzahlen)
    acc = 0.0
    for i in range(len(bps)-1):
        p, q = bps[i], bps[i+1]
        um = ((p+q)/2)/m; un = ((p+q)/2)/n
        # auf [p,q] linear: {u/m}=u/m-a, {u/n}=u/n-b
        a = math.floor(p/m + 1e-9); bb = math.floor(p/n + 1e-9)
        # ∫_p^q (u/m-a)(u/n-b) du  (ohne u⁻², reiner Mittelwert)
        f = lambda u: (u/m - a)*(u/n - bb)
        # exaktes Integral eines quadratischen Polynoms via Simpson (exakt für Grad≤2)
        acc += (q-p)/6 * (f(p) + 4*f((p+q)/2) + f(q))
    return acc / L

def G_entry(m, n, U0=3000):
    """G_mn = ∫₁^∞ {u/m}{u/n} u⁻² du, stückweise exakt bis U0 + Schwanz μ/U0."""
    bps = set([1.0, float(U0)])
    k = 1
    while k*m <= U0:
        if k*m > 1: bps.add(float(k*m))
        k += 1
    k = 1
    while k*n <= U0:
        if k*n > 1: bps.add(float(k*n))
        k += 1
    bps = sorted(bps)
    total = 0.0
    for i in range(len(bps)-1):
        p, q = bps[i], bps[i+1]
        mid = (p+q)/2
        a = math.floor(mid/m); bb = math.floor(mid/n)
        # ∫_p^q [1/(mn) - (bb/m + a/n)/u + a*bb/u²] du
        total += (q-p)/(m*n)
        total += -(bb/m + a/n)*(math.log(q) - math.log(p))
        total += a*bb*(1.0/p - 1.0/q)
    # Schwanz: ∫_{U0}^∞ {u/m}{u/n} u⁻² du ≈ μ * ∫_{U0}^∞ u⁻² du = μ/U0
    total += _period_mean(m, n) / U0
    return total

def run(Ns=(2,4,6,8,10,12,15,18,21,24), U0=3000):
    Nmax = max(Ns)
    # b-Vektor exakt + Validierung
    b = np.array([b_exact(n) for n in range(1, Nmax+1)])
    # Gram-Matrix (symmetrisch)
    G = np.zeros((Nmax, Nmax))
    for i in range(Nmax):
        for j in range(i, Nmax):
            g = G_entry(i+1, j+1, U0)
            G[i, j] = G[j, i] = g
    results = []
    for N in Ns:
        GN = G[:N, :N]; bN = b[:N]
        # G⁻¹b stabil via lstsq (G kann schlecht konditioniert sein)
        x, *_ = np.linalg.lstsq(GN, bN, rcond=None)
        d2 = 1.0 - float(bN @ x)          # ||1||²=1
        d2 = max(d2, 0.0)
        cond = float(np.linalg.cond(GN))
        results.append({"N": N, "d_N^2": d2, "d_N": math.sqrt(d2),
                        "logN_times_d2": math.log(N)*d2, "cond_G": cond})
    return {"results": results, "constant_conjectured": C_CONJ,
            "b_validation_b1": (b[0], b_exact(1))}

if __name__ == "__main__":
    out = run()
    print(f"Vermutete Grenzkonstante  2+γ-log(4π) = {C_CONJ:.6f}\n")
    print(f"{'N':>4} {'d_N':>10} {'d_N^2':>12} {'(logN)·d_N^2':>14} {'cond(G)':>12}")
    for r in out["results"]:
        print(f"{r['N']:>4} {r['d_N']:>10.5f} {r['d_N^2']:>12.6f} "
              f"{r['logN_times_d2']:>14.5f} {r['cond_G']:>12.2e}")
