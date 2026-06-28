"""
visualize.py — Grafische Darstellung der RH (matplotlib, Agg-Backend).
Speichert PNGs nach kb/figures/ und gibt den Pfad zurück.
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
    """Hardysche Z(t) über [t0,t1]; Vorzeichenwechsel = Nullstellen auf der Geraden."""
    ts = np.linspace(t0, t1, n)
    zs = [float(mp.siegelz(t)) for t in ts]
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.axhline(0, color="black", lw=0.7)
    ax.plot(ts, zs, lw=1.0)
    # Nulldurchgänge markieren
    for i in range(1, len(zs)):
        if zs[i-1] * zs[i] < 0:
            tz = ts[i-1] - zs[i-1]*(ts[i]-ts[i-1])/(zs[i]-zs[i-1])
            ax.plot(tz, 0, "ro", ms=4)
    ax.set_xlabel("t"); ax.set_ylabel("Z(t)")
    ax.set_title(f"Hardysche Z-Funktion und Nullstellen auf Re(s)=1/2, t∈[{t0},{t1}]")
    return _save(fig, name)

def plot_zeros_on_line(count=30, name="zeros_line.png"):
    """Erste `count` nicht-triviale Nullstellen als Punkte auf der kritischen Geraden."""
    gammas = [float(mp.im(mp.zetazero(k))) for k in range(1, count+1)]
    fig, ax = plt.subplots(figsize=(4, 8))
    ax.axvline(0.5, color="red", lw=1.2, label="kritische Gerade Re=1/2")
    ax.plot([0.5]*len(gammas), gammas, "o", ms=5)
    for g in gammas:
        ax.plot([0.5], [g], "o", ms=5, color="C0")
    ax.set_xlim(0, 1); ax.set_xlabel("Re(s)"); ax.set_ylabel("Im(s)=γ")
    ax.set_title(f"Erste {count} nicht-triviale Nullstellen")
    ax.legend(loc="upper right", fontsize=8)
    return _save(fig, name)

def plot_zeta_abs_strip(t0=0.0, t1=50.0, sig0=0.0, sig1=1.0, res=200, name="zeta_strip.png"):
    """Heatmap von |ζ(σ+it)| im kritischen Streifen; dunkle Punkte = Nullstellen."""
    sig = np.linspace(sig0, sig1, res//2)
    ts = np.linspace(t0, t1, res)
    Zmag = np.zeros((len(ts), len(sig)))
    for i, t in enumerate(ts):
        for j, s in enumerate(sig):
            if abs(s - 1.0) < 1e-9 and abs(t) < 1e-9:  # Pol bei s=1 meiden
                Zmag[i, j] = 1e6
                continue
            Zmag[i, j] = float(abs(mp.zeta(mp.mpc(s, t))))
    fig, ax = plt.subplots(figsize=(5, 9))
    im = ax.imshow(np.log(Zmag+1e-6), origin="lower", aspect="auto",
                   extent=[sig0, sig1, t0, t1], cmap="viridis")
    ax.axvline(0.5, color="red", lw=1.0)
    ax.set_xlabel("Re(s)=σ"); ax.set_ylabel("Im(s)=t")
    ax.set_title("log|ζ(σ+it)| — Nullstellen als dunkle Minima auf Re=1/2")
    fig.colorbar(im, ax=ax, label="log|ζ|")
    return _save(fig, name)

def plot_pair_correlation(num_zeros=300, name="pair_correlation.png"):
    """Nächste-Nachbar-Abstände der Nullstellen (normiert) vs. GUE-Vorhersage (docs/06)."""
    gammas = [float(mp.im(mp.zetazero(k))) for k in range(1, num_zeros+1)]
    # lokale Normierung mit mittlerer Dichte log(γ/2π)/2π
    spac = []
    for i in range(1, len(gammas)):
        g = gammas[i]
        dens = float(mp.log(g/(2*mp.pi))/(2*mp.pi))
        spac.append((gammas[i]-gammas[i-1])*dens)
    s = np.array(spac)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(s, bins=30, density=True, alpha=0.6, label="Nullstellen (normiert)")
    xs = np.linspace(0, 3, 200)
    # Wigner-Surmise (GUE-Näherung)
    gue = (32/np.pi**2)*xs**2*np.exp(-4*xs**2/np.pi)
    ax.plot(xs, gue, "r-", lw=2, label="GUE (Wigner-Surmise)")
    poisson = np.exp(-xs)
    ax.plot(xs, poisson, "g--", lw=1.2, label="Poisson (unkorreliert)")
    ax.set_xlabel("normierter Abstand s"); ax.set_ylabel("p(s)")
    ax.set_title(f"Nullstellenabstände vs. GUE ({num_zeros} Nullstellen)")
    ax.legend()
    return _save(fig, name)

def plot_li_coefficients(n_max=20, name="li_coefficients.png"):
    """λ_n für n=1..n_max (RH ⟺ alle λ_n≥0, docs/14). Näherung via Nullstellensumme."""
    import compute
    ns = list(range(1, n_max+1))
    vals = [compute.li_coefficient(n, num_zeros=800)["lambda"] for n in ns]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.axhline(0, color="black", lw=0.8)
    ax.bar(ns, vals, color=["C0" if v>=0 else "red" for v in vals])
    ax.set_xlabel("n"); ax.set_ylabel("λ_n")
    ax.set_title("Li-Koeffizienten λ_n (RH ⟺ alle ≥ 0)")
    return _save(fig, name)

def plot_psi_convergence(x=30.0, max_zeros=200, name="psi_convergence.png"):
    """ψ(x)-Näherung (explizite Formel) gegen Zahl der genutzten Nullstellen (docs/02)."""
    import compute
    xs_n = list(range(5, max_zeros+1, 5))
    approx = [compute.psi_explicit(x, m)["psi_explicit_approx"] for m in xs_n]
    true = compute.psi_explicit(x, 5).get("psi_true")
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(xs_n, approx, "o-", ms=3, label="ψ(x) explizite Formel")
    if true is not None:
        ax.axhline(true, color="red", ls="--", label=f"echtes ψ({x:g})={true:.3f}")
    ax.set_xlabel("Anzahl genutzter Nullstellen"); ax.set_ylabel(f"ψ({x:g})")
    ax.set_title("Konvergenz der expliziten Formel (Nullstellen steuern Primzahlen)")
    ax.legend()
    return _save(fig, name)

def plot_counting_N(T=100.0, name="counting_N.png"):
    """N(T) exakt (Treppe) vs. glatte Riemann-von-Mangoldt-Näherung."""
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
    ax.step(ts, exact, where="post", label="N(T) exakt", lw=1.2)
    ax.plot(ts, smooth, "--", color="red", label="glatt: θ(T)/π+1")
    ax.set_xlabel("T"); ax.set_ylabel("N(T)")
    ax.set_title("Nullstellen-Zählfunktion N(T): exakt vs. glatt")
    ax.legend()
    return _save(fig, name)
