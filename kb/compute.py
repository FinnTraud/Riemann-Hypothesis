"""
compute.py — Numerischer Kern (mpmath) für RH-Experimente.
Alle Funktionen geben JSON-fähige Dicts zurück. Hohe Präzision via mpmath.

Wichtig (Ehrlichkeit): Numerik ist EVIDENZ, kein Beweis (siehe docs/35).
"""
import mpmath as mp
from functools import lru_cache

mp.mp.dps = 30  # Dezimalstellen Präzision

@lru_cache(maxsize=20000)
def _zero(n):
    """Gecachte n-te Nullstelle (mpmath.zetazero) — beschleunigt λ_n, ψ(x), Plots stark."""
    return mp.zetazero(n)

def _c(z):
    """komplexe mpmath-Zahl -> [re, im] als float."""
    z = mp.mpc(z)
    return [float(mp.re(z)), float(mp.im(z))]

def zeta(sigma, t=0.0):
    """Riemann ζ(σ+it)."""
    s = mp.mpc(sigma, t)
    val = mp.zeta(s)
    return {"s": [float(sigma), float(t)], "zeta": _c(val), "abs": float(abs(val))}

def hardy_Z(t):
    """Hardysche Z-Funktion (reell); |Z(t)|=|ζ(1/2+it)|. Vorzeichenwechsel = Nullstelle."""
    z = mp.siegelz(t)
    return {"t": float(t), "Z": float(z), "theta": float(mp.siegeltheta(t))}

def nth_zero(n):
    """n-te nicht-triviale Nullstelle ρ=1/2+iγ (mpmath.zetazero)."""
    rho = _zero(n)
    gamma = float(mp.im(rho))
    re = float(mp.re(rho))
    return {"n": n, "rho": _c(rho), "gamma": gamma, "re": re,
            "on_critical_line": abs(re - 0.5) < 1e-12}

def first_zeros(count=10):
    """Die ersten `count` nicht-trivialen Nullstellen (γ-Werte)."""
    out = []
    for n in range(1, count + 1):
        rho = _zero(n)
        out.append({"n": n, "gamma": float(mp.im(rho)), "re": float(mp.re(rho))})
    return {"count": count, "zeros": out,
            "all_on_line": all(abs(z["re"] - 0.5) < 1e-12 for z in out)}

def verify_rh_range(n_start=1, n_end=50):
    """Prüft (numerisch), dass die Nullstellen n_start..n_end exakt auf Re=1/2 liegen.
    Liefert max. Abweichung von 1/2. EVIDENZ, kein Beweis."""
    max_dev = 0.0
    worst = None
    for n in range(n_start, n_end + 1):
        rho = _zero(n)
        dev = abs(float(mp.re(rho)) - 0.5)
        if dev > max_dev:
            max_dev, worst = dev, n
    return {"range": [n_start, n_end], "max_deviation_from_half": max_dev,
            "worst_n": worst, "all_on_line": max_dev < 1e-10,
            "note": "Numerische Evidenz, kein Beweis (siehe docs/35)."}

def count_zeros(T):
    """N(T): exakte Anzahl Nullstellen mit 0<γ≤T (über zetazero) vs. glatte Riemann-von-Mangoldt-Näherung."""
    # glatter Hauptterm: theta(T)/pi + 1
    smooth = float(mp.siegeltheta(T) / mp.pi + 1)
    # exakt zählen, bis γ>T
    n = 0
    while True:
        g = float(mp.im(_zero(n + 1)))
        if g > T:
            break
        n += 1
        if n > 100000:
            break
    return {"T": float(T), "exact_count": n, "smooth_estimate": smooth,
            "S_T_times_pi": (n - smooth)}

def li_coefficient(n, num_zeros=2000):
    """Li-Koeffizient λ_n. n=1 geschlossen; n≥2 Näherung via Nullstellensumme
    λ_n=Σ_ρ[1-(1-1/ρ)^n] (über ρ und ρ̄). RH ⟺ λ_n≥0 ∀n (docs/14)."""
    if n == 1:
        gamma = mp.euler
        val = 1 + gamma / 2 - mp.log(4 * mp.pi) / 2
        return {"n": 1, "lambda": float(val), "exact": True,
                "formula": "1 + γ/2 − ½·log(4π)", "nonneg": float(val) >= 0}
    total = mp.mpf(0)
    for k in range(1, num_zeros + 1):
        rho = _zero(k)
        for r in (rho, mp.conj(rho)):
            total += 1 - (1 - 1 / r) ** n
    val = mp.re(total)
    return {"n": n, "lambda": float(val), "exact": False,
            "approx_zeros_used": num_zeros, "nonneg": float(val) >= 0,
            "note": "Näherung (endliche Nullstellensumme, langsame Konvergenz)."}

def psi_explicit(x, num_zeros=200):
    """Explizite Formel: ψ(x) ≈ x − Σ_ρ x^ρ/ρ − log(2π) − ½log(1−x⁻²).
    Demonstriert, wie Nullstellen die Primzahlverteilung steuern (docs/02).
    Vergleicht mit echtem ψ(x)=Σ_{n≤x} Λ(n)."""
    x = mp.mpf(x)
    approx = x - mp.log(2 * mp.pi) - mp.mpf("0.5") * mp.log(1 - x ** -2)
    for k in range(1, num_zeros + 1):
        rho = _zero(k)
        for r in (rho, mp.conj(rho)):
            approx -= x ** r / r
    # echtes psi(x) = Σ_{n≤x} Λ(n)  (reine Python-Siebung, keine Extra-Abhängigkeit)
    try:
        real = float(sum(float(mp.log(p)) for p in _prime_powers(int(x))))
    except Exception:
        real = None
    out = {"x": float(x), "psi_explicit_approx": float(mp.re(approx)),
           "num_zeros": num_zeros}
    if real is not None:
        out["psi_true"] = real
        out["abs_error"] = abs(float(mp.re(approx)) - real)
    return out

def _prime_powers(N):
    """Λ(n)-Träger ≤ N: alle Primzahlpotenzen p^k ≤ N (für ψ(x))."""
    sieve = [True] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, N + 1, i):
                sieve[j] = False
    for p in primes:
        pk = p
        while pk <= N:
            yield p
            pk *= p

def set_precision(dps):
    mp.mp.dps = int(dps)
    return {"dps": mp.mp.dps}
