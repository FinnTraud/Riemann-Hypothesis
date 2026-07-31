"""
visualize.py — Graphical rendering of the RH (matplotlib, Agg backend).
Saves PNGs to kb/figures/ and returns the path.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(FIG, exist_ok=True)

def _save(fig, name):
    path = os.path.join(FIG, name)
    fig.savefig(path, dpi=130, bbox_inches="tight")
    plt.close(fig)
    return path

def plot_Z_and_zeros(t0=0.0, t1=50.0, n=1200, name="hardyZ.png"):
    """Hardy Z(t) over [t0,t1]; sign changes = zeros on the line."""
    ts = np.linspace(t0, t1, n)
    zs = [float(mp.siegelz(t)) for t in ts]
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.axhline(0, color="black", lw=0.7)
    ax.plot(ts, zs, lw=1.0)
    # mark zero crossings
    for i in range(1, len(zs)):
        if zs[i-1] * zs[i] < 0:
            tz = ts[i-1] - zs[i-1]*(ts[i]-ts[i-1])/(zs[i]-zs[i-1])
            ax.plot(tz, 0, "ro", ms=4)
    ax.set_xlabel("t"); ax.set_ylabel("Z(t)")
    ax.set_title(f"Hardy Z-function and zeros on Re(s)=1/2, t∈[{t0},{t1}]")
    return _save(fig, name)

def plot_zeros_on_line(count=30, name="zeros_line.png"):
    """First `count` non-trivial zeros as points on the critical line."""
    gammas = [float(mp.im(mp.zetazero(k))) for k in range(1, count+1)]
    fig, ax = plt.subplots(figsize=(4, 8))
    ax.axvline(0.5, color="red", lw=1.2, label="critical line Re=1/2")
    ax.plot([0.5]*len(gammas), gammas, "o", ms=5)
    for g in gammas:
        ax.plot([0.5], [g], "o", ms=5, color="C0")
    ax.set_xlim(0, 1); ax.set_xlabel("Re(s)"); ax.set_ylabel("Im(s)=γ")
    ax.set_title(f"First {count} non-trivial zeros")
    ax.legend(loc="upper right", fontsize=8)
    return _save(fig, name)

def plot_zeta_abs_strip(t0=0.0, t1=50.0, sig0=0.0, sig1=1.0, res=200, name="zeta_strip.png"):
    """Heatmap of |ζ(σ+it)| in the critical strip; dark points = zeros."""
    sig = np.linspace(sig0, sig1, res//2)
    ts = np.linspace(t0, t1, res)
    Zmag = np.zeros((len(ts), len(sig)))
    for i, t in enumerate(ts):
        for j, s in enumerate(sig):
            if abs(s - 1.0) < 1e-9 and abs(t) < 1e-9:  # avoid the pole at s=1
                Zmag[i, j] = 1e6
                continue
            Zmag[i, j] = float(abs(mp.zeta(mp.mpc(s, t))))
    fig, ax = plt.subplots(figsize=(5, 9))
    im = ax.imshow(np.log(Zmag+1e-6), origin="lower", aspect="auto",
                   extent=[sig0, sig1, t0, t1], cmap="viridis")
    ax.axvline(0.5, color="red", lw=1.0)
    ax.set_xlabel("Re(s)=σ"); ax.set_ylabel("Im(s)=t")
    ax.set_title("log|ζ(σ+it)| — zeros as dark minima on Re=1/2")
    fig.colorbar(im, ax=ax, label="log|ζ|")
    return _save(fig, name)

def plot_pair_correlation(num_zeros=300, name="pair_correlation.png"):
    """Nearest-neighbor spacings of the zeros (normalized) vs. GUE prediction (docs/06)."""
    gammas = [float(mp.im(mp.zetazero(k))) for k in range(1, num_zeros+1)]
    # local normalization with mean density log(γ/2π)/2π
    spac = []
    for i in range(1, len(gammas)):
        g = gammas[i]
        dens = float(mp.log(g/(2*mp.pi))/(2*mp.pi))
        spac.append((gammas[i]-gammas[i-1])*dens)
    s = np.array(spac)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(s, bins=30, density=True, alpha=0.6, label="zeros (normalized)")
    xs = np.linspace(0, 3, 200)
    # Wigner surmise (GUE approximation)
    gue = (32/np.pi**2)*xs**2*np.exp(-4*xs**2/np.pi)
    ax.plot(xs, gue, "r-", lw=2, label="GUE (Wigner surmise)")
    poisson = np.exp(-xs)
    ax.plot(xs, poisson, "g--", lw=1.2, label="Poisson (uncorrelated)")
    ax.set_xlabel("normalized spacing s"); ax.set_ylabel("p(s)")
    ax.set_title(f"Zero spacings vs. GUE ({num_zeros} zeros)")
    ax.legend()
    return _save(fig, name)

def plot_li_coefficients(n_max=20, name="li_coefficients.png"):
    """λ_n for n=1..n_max (RH ⟺ all λ_n≥0, docs/14). Approximation via zero sum."""
    import compute
    ns = list(range(1, n_max+1))
    vals = [compute.li_coefficient(n, num_zeros=800)["lambda"] for n in ns]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.axhline(0, color="black", lw=0.8)
    ax.bar(ns, vals, color=["C0" if v>=0 else "red" for v in vals])
    ax.set_xlabel("n"); ax.set_ylabel("λ_n")
    ax.set_title("Li coefficients λ_n (RH ⟺ all ≥ 0)")
    return _save(fig, name)

def plot_psi_convergence(x=30.0, max_zeros=200, name="psi_convergence.png"):
    """ψ(x) approximation (explicit formula) against the number of zeros used (docs/02)."""
    import compute
    xs_n = list(range(5, max_zeros+1, 5))
    approx = [compute.psi_explicit(x, m)["psi_explicit_approx"] for m in xs_n]
    true = compute.psi_explicit(x, 5).get("psi_true")
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(xs_n, approx, "o-", ms=3, label="ψ(x) explicit formula")
    if true is not None:
        ax.axhline(true, color="red", ls="--", label=f"true ψ({x:g})={true:.3f}")
    ax.set_xlabel("number of zeros used"); ax.set_ylabel(f"ψ({x:g})")
    ax.set_title("Convergence of the explicit formula (zeros control the primes)")
    ax.legend()
    return _save(fig, name)

def plot_counting_N(T=100.0, name="counting_N.png"):
    """N(T) exact (staircase) vs. smooth Riemann–von Mangoldt approximation."""
    gammas = []
    k = 1
    while True:
        g = float(mp.im(mp.zetazero(k)))
        if g > T: break
        gammas.append(g); k += 1
    ts = np.linspace(1, T, 600)
    smooth = [float(mp.siegeltheta(t)/mp.pi + 1) for t in ts]
    exact = [sum(1 for g in gammas if g <= t) for t in ts]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.step(ts, exact, where="post", label="N(T) exact", lw=1.2)
    ax.plot(ts, smooth, "--", color="red", label="smooth: θ(T)/π+1")
    ax.set_xlabel("T"); ax.set_ylabel("N(T)")
    ax.set_title("Zero-counting function N(T): exact vs. smooth")
    ax.legend()
    return _save(fig, name)
