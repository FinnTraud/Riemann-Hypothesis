#!/usr/bin/env python3
"""Gegenbeispiel-Orakel: Kriterien gegen eine RH-VERLETZENDE Funktion testen.

Motivation (docs/35, docs/60)
----------------------------
Jede numerische Bestaetigung an zeta(s) ist schwach: sie bestaetigt nur, was
wir ohnehin glauben. Die schaerfere Frage lautet umgekehrt:

    Wuerde mein Argument / mein Kriterium eine Funktion, fuer die die RH
    NACHWEISLICH FALSCH ist, als "RH-konform" durchwinken?

Die Davenport-Heilbronn-Funktion ist genau dieser Testfall. Sie hat
Funktionalgleichung, analytische Fortsetzung, Wachstum vom zeta-Typ,
reelle Dirichlet-Koeffizienten -- aber Nullstellen abseits der kritischen
Geraden. Was sie NICHT hat: ein Euler-Produkt.

Dieses Modul stellt beide Funktionen (zeta und Davenport-Heilbronn) hinter
derselben Schnittstelle bereit und laesst eine Testbatterie ueber beide
laufen. Ein Test ist nur dann informativ, wenn er die beiden TRENNT.

Definition (Hurwitz-Form)
-------------------------
    tau  = (sqrt(10 - 2 sqrt 5) - 2) / (sqrt 5 - 1)      ~ 0.2840790438
    f(s) = 5^{-s} [ z(s,1/5) + tau z(s,2/5) - tau z(s,3/5) - z(s,4/5) ]

mit der Hurwitz-Zetafunktion z(s,a). Aequivalent ist f die Dirichlet-Reihe
mit mod-5-periodischen Koeffizienten a(n) = [0, 1, tau, -tau, -1][n mod 5].

CLI
---
    python3 kb/counterexample.py all           # ganze Batterie, T=120
    python3 kb/counterexample.py all -T 200
    python3 kb/counterexample.py fe            # Funktionalgleichung
    python3 kb/counterexample.py euler         # Multiplikativitaet
    python3 kb/counterexample.py offline       # Nullstellen abseits der Geraden
    python3 kb/counterexample.py deficit -T 120  # Vorzeichenwechsel-Defizit
    python3 kb/counterexample.py rightof1 -T 120

Benoetigt mpmath (kb/requirements.txt).
"""

from __future__ import annotations

import argparse
import json
import sys

try:
    from mpmath import mp, mpf, mpc, sqrt, zeta, gamma, loggamma, pi, findroot, fabs
except ImportError:  # pragma: no cover
    print("Dieses Modul braucht mpmath:  pip install -r kb/requirements.txt", file=sys.stderr)
    raise

mp.dps = 20

# --------------------------------------------------------------------------
# Die beiden Funktionen hinter einer gemeinsamen Schnittstelle
# --------------------------------------------------------------------------

TAU = (sqrt(10 - 2 * sqrt(5)) - 2) / (sqrt(5) - 1)

#: Dirichlet-Koeffizienten von f, periodisch mod 5 (Index = n mod 5)
DH_COEFFS = [mpf(0), mpf(1), TAU, -TAU, mpf(-1)]


def dh_f(s):
    """Davenport-Heilbronn-Funktion f(s) ueber Hurwitz-Zeta."""
    s = mpc(s)
    return 5 ** (-s) * (
        zeta(s, mpf(1) / 5)
        + TAU * zeta(s, mpf(2) / 5)
        - TAU * zeta(s, mpf(3) / 5)
        - zeta(s, mpf(4) / 5)
    )


def dh_xi(s):
    """Vervollstaendigte DH-Funktion; Gamma-Faktor eines UNGERADEN Charakters mod 5.

    xi_f(s) = (5/pi)^{(s+1)/2} Gamma((s+1)/2) f(s),  xi_f(s) = xi_f(1-s).
    """
    s = mpc(s)
    return (mpf(5) / pi) ** ((s + 1) / 2) * gamma((s + 1) / 2) * dh_f(s)


def zeta_f(s):
    return mp.zeta(mpc(s))


def zeta_xi(s):
    """Riemannsche xi-Funktion: xi(s) = s(s-1)/2 * pi^{-s/2} Gamma(s/2) zeta(s)."""
    s = mpc(s)
    return s * (s - 1) / 2 * pi ** (-s / 2) * gamma(s / 2) * mp.zeta(s)


def dh_theta(T):
    """Riemann-Siegel-Analogon theta_f(T) = Im log[(5/pi)^{(s+1)/2} Gamma((s+1)/2)], s=1/2+iT."""
    s = mpc(mpf(1) / 2, T)
    return mp.im(((s + 1) / 2) * mp.log(mpf(5) / pi) + loggamma((s + 1) / 2))


def zeta_theta(T):
    """Riemann-Siegel-Theta: Im log[pi^{-s/2} Gamma(s/2)], s = 1/2 + iT."""
    s = mpc(mpf(1) / 2, T)
    return mp.im(-(s / 2) * mp.log(pi) + loggamma(s / 2))


#: Registry: name -> (f, xi, theta, hat_pol, hat_euler_produkt)
FUNCS = {
    "zeta": dict(f=zeta_f, xi=zeta_xi, theta=zeta_theta, pole=True, euler=True,
                 label="Riemannsche zeta-Funktion"),
    "dh": dict(f=dh_f, xi=dh_xi, theta=dh_theta, pole=False, euler=False,
               label="Davenport-Heilbronn-Funktion"),
}


def _coeff(name, n):
    """n-ter Dirichlet-Koeffizient."""
    if name == "zeta":
        return mpf(1)
    return DH_COEFFS[n % 5]


# --------------------------------------------------------------------------
# T1 -- Funktionalgleichung
# --------------------------------------------------------------------------

def test_functional_equation(name, points=((2, 1), (0.3, 4.0), (1.7, -2.5))):
    """Prueft xi(s) = xi(1-s) an mehreren Punkten.

    ERWARTUNG: beide bestehen. Genau deshalb kann kein Beweis, der nur
    Funktionalgleichung + Fortsetzung + Wachstum benutzt, die RH liefern.
    """
    xi = FUNCS[name]["xi"]
    worst = mpf(0)
    samples = []
    for re_, im_ in points:
        s = mpc(re_, im_)
        a, b = xi(s), xi(1 - s)
        rel = fabs(a - b) / max(fabs(a), mpf(10) ** -30)
        worst = max(worst, rel)
        samples.append({"s": f"{re_}+{im_}i", "rel_abweichung": mp.nstr(rel, 3)})
    ok = worst < mpf(10) ** -15
    return {
        "test": "T1 Funktionalgleichung xi(s)=xi(1-s)",
        "funktion": name,
        "bestanden": bool(ok),
        "max_rel_abweichung": mp.nstr(worst, 3),
        "punkte": samples,
        "trennt_zeta_von_dh": False,
        "lehre": "Nicht trennend: die Funktionalgleichung ist KEIN RH-Indikator.",
    }


# --------------------------------------------------------------------------
# T2 -- Euler-Produkt / Multiplikativitaet der Koeffizienten
# --------------------------------------------------------------------------

def test_euler_product(name, pairs=((2, 3), (2, 7), (3, 4), (4, 9), (2, 11))):
    """Prueft a(mn) = a(m)a(n) fuer teilerfremde m,n.

    ERWARTUNG: zeta besteht, DH faellt durch. Das ist der TRENNENDE Test --
    und exakt die Eigenschaft, die docs/35 als unverzichtbar ausweist.
    """
    viol = []
    for m, n in pairs:
        lhs = _coeff(name, m * n)
        rhs = _coeff(name, m) * _coeff(name, n)
        if fabs(lhs - rhs) > mpf(10) ** -15:
            viol.append({
                "m": m, "n": n, "mn": m * n,
                "a(mn)": mp.nstr(lhs, 10),
                "a(m)a(n)": mp.nstr(rhs, 10),
            })
    return {
        "test": "T2 Multiplikativitaet a(mn)=a(m)a(n)  (Euler-Produkt)",
        "funktion": name,
        "bestanden": not viol,
        "verletzungen": viol,
        "trennt_zeta_von_dh": True,
        "lehre": ("Trennend. Die einzige der vier Struktureigenschaften, die DH "
                  "fehlt -- und damit die einzige, an der ein RH-Beweis ansetzen kann."),
    }


# --------------------------------------------------------------------------
# T3 -- Nullstellen abseits der kritischen Geraden
# --------------------------------------------------------------------------

#: Startwerte aus der Literatur (Balanzario/Sanchez-Ortiz, Math. Comp. 76 (2007))
DH_OFFLINE_SEEDS = [(0.808, 85.70), (0.651, 114.16), (0.574, 166.48), (0.724, 176.70)]


def test_offline_zeros(name, seeds=None, tol_dps=20):
    """Sucht per findroot Nullstellen mit Re(s) != 1/2.

    ERWARTUNG: fuer DH werden welche gefunden, fuer zeta divergiert die
    Iteration auf die kritische Gerade zurueck (bis heute keine Ausnahme bekannt).
    """
    f = FUNCS[name]["f"]
    seeds = seeds or DH_OFFLINE_SEEDS
    found = []
    for sr, si in seeds:
        try:
            r = findroot(f, mpc(sr, si), tol=mpf(10) ** (-tol_dps))
        except Exception:
            continue
        abweichung = fabs(mp.re(r) - mpf(1) / 2)
        found.append({
            "nullstelle": mp.nstr(r, 15),
            "Re": mp.nstr(mp.re(r), 15),
            "Im": mp.nstr(mp.im(r), 15),
            "abstand_zur_kritischen_geraden": mp.nstr(abweichung, 6),
            "residuum_|f|": mp.nstr(fabs(f(r)), 3),
            "abseits": bool(abweichung > mpf(10) ** -8),
        })
    off = [z for z in found if z["abseits"]]
    return {
        "test": "T3 Nullstellen abseits der kritischen Geraden",
        "funktion": name,
        "rh_verletzung_nachgewiesen": bool(off),
        "gefunden": found,
        "trennt_zeta_von_dh": True,
        "lehre": ("DH verletzt die RH nicht knapp, sondern deutlich "
                  "(Re bis ~0.81 statt 0.5)."),
    }


# --------------------------------------------------------------------------
# T4 -- Vorzeichenwechsel-Defizit (der eigentliche Detektor)
# --------------------------------------------------------------------------

def _arg_path(f, path, unwrap_start=mpf(0)):
    """Stetig fortgesetztes Argument von f entlang einer Punktliste."""
    total = unwrap_start
    prev = mp.arg(f(path[0]))
    acc = prev
    for s in path[1:]:
        cur = mp.arg(f(s))
        d = cur - prev
        while d > pi:
            d -= 2 * pi
        while d < -pi:
            d += 2 * pi
        acc += d
        prev = cur
    return acc - mp.arg(f(path[0])) + total


def count_zeros_argument_principle(name, T, n_vert=None, n_horiz=60):
    """Exakte Nullstellenzahl N(T) im Streifen 0 < Im(s) < T via Argumentprinzip.

    N(T) = (1/pi) [ theta(T) + Delta arg f entlang 2 -> 2+iT -> 1/2+iT ]  (+1 bei Pol).

    Der Gamma-Anteil wird analytisch (loggamma) genommen, nur arg f wird
    numerisch stetig fortgesetzt -- dort ist f nahe 1, das Argument also klein
    und gutartig.
    """
    cfg = FUNCS[name]
    f, theta = cfg["f"], cfg["theta"]
    n_vert = n_vert or max(80, int(T * 2))
    vert = [mpc(2, mpf(T) * k / n_vert) for k in range(n_vert + 1)]
    horiz = [mpc(2 - mpf(3) / 2 * k / n_horiz, T) for k in range(n_horiz + 1)]
    darg = _arg_path(f, vert + horiz[1:])
    n = (theta(T) + darg) / pi
    if cfg["pole"]:
        n += 1
    return n


def count_sign_changes(name, T, h=0.1):
    """Vorzeichenwechsel der reellwertigen Funktion Z(t) = xi(1/2+it) auf (0, T]."""
    xi = FUNCS[name]["xi"]
    steps = int(mpf(T) / h)
    prev_t = mpf(h)
    prev = mp.re(xi(mpc(mpf(1) / 2, prev_t)))
    changes = []
    for k in range(2, steps + 1):
        t = mpf(k) * h
        cur = mp.re(xi(mpc(mpf(1) / 2, t)))
        if prev * cur < 0:
            changes.append((float(prev_t), float(t)))
        prev, prev_t = cur, t
    return changes


def test_sign_change_deficit(name, T=120, h=0.1):
    """Der Kern des Orakels.

    Z(t) = xi(1/2+it) ist fuer BEIDE Funktionen reellwertig. Jede Nullstelle
    AUF der Geraden erzeugt (generisch) einen Vorzeichenwechsel von Z.
    Das Argumentprinzip zaehlt dagegen ALLE Nullstellen im Streifen.

        Defizit := N(T) - #Vorzeichenwechsel(0,T]

    Defizit 0  -> alle gezaehlten Nullstellen liegen auf der Geraden.
    Defizit > 0 -> es fehlen Nullstellen auf der Geraden, d.h. sie liegen
                   abseits. Bei reellen Koeffizienten treten diese in Paaren
                   (rho, 1-conj(rho)) auf, das Defizit ist also gerade.

    Genau dieses Verfahren (Turings Idee) ist das, was numerische
    RH-Verifikation ueberhaupt zu einem Beweis fuer endliche Hoehen macht --
    und es ist der einzige Test hier, der die Verletzung SELBST FINDET,
    ohne dass man ihm die Nullstelle vorher zeigt.
    """
    n_t = count_zeros_argument_principle(name, T)
    n_round = int(mp.nint(n_t))
    changes = count_sign_changes(name, T, h)
    deficit = n_round - len(changes)
    return {
        "test": "T4 Vorzeichenwechsel-Defizit (Turing-Methode)",
        "funktion": name,
        "T": T,
        "schrittweite_h": float(h),
        "N(T)_argumentprinzip": mp.nstr(n_t, 12),
        "N(T)_gerundet": n_round,
        "rundungsabstand": mp.nstr(fabs(n_t - n_round), 3),
        "vorzeichenwechsel_von_Z": len(changes),
        "defizit": deficit,
        "rh_verletzung_detektiert": bool(deficit > 0),
        "trennt_zeta_von_dh": True,
        "lehre": ("Der einzige Test der Batterie, der die Verletzung von sich aus "
                  "findet. Ein positives Defizit ist ein Existenzbeweis fuer "
                  "Nullstellen abseits der Geraden -- ohne sie zu lokalisieren."),
        "vorbehalt": (f"Schrittweite h={float(h)}; sehr enge Nullstellenpaare "
                      "(Lehmer-Paare, docs/23) koennen ein Paar Vorzeichenwechsel "
                      "verschlucken und ein Defizit VORTAEUSCHEN. h halbieren "
                      "und nachpruefen."),
    }


# --------------------------------------------------------------------------
# T5 -- Nullstellen rechts von Re(s)=1
# --------------------------------------------------------------------------

def test_zeros_right_of_1(name, T=120, sigma_max=1.20, dsigma=0.02, dt=0.5):
    """Rastert |f| im Bereich 1 < Re(s) <= sigma_max, 0 < Im(s) <= T.

    Fuer zeta ist Nullstellenfreiheit dort ein SATZ (Euler-Produkt: das
    Produkt konvergiert und kein Faktor verschwindet). Fuer DH ist bekannt,
    dass unendlich viele Nullstellen mit Re(s) > 1 existieren -- sie liegen
    aber deutlich hoeher als der hier gerasterte Bereich.
    """
    f = FUNCS[name]["f"]
    best = None
    sigma = mpf(1) + dsigma
    while sigma <= sigma_max + mpf(10) ** -9:
        t = mpf(dt)
        while t <= T:
            v = fabs(f(mpc(sigma, t)))
            if best is None or v < best[0]:
                best = (v, sigma, t)
            t += dt
        sigma += dsigma
    zeros = []
    if best is not None:
        try:
            r = findroot(f, mpc(best[1], best[2]), tol=mpf(10) ** -18)
            if mp.re(r) > 1 and fabs(f(r)) < mpf(10) ** -12:
                zeros.append(mp.nstr(r, 15))
        except Exception:
            pass
    return {
        "test": "T5 Nullstellen mit Re(s) > 1",
        "funktion": name,
        "gerasterter_bereich": f"Re in (1, {sigma_max}], Im in (0, {T}]",
        "kleinstes_|f|_im_raster": mp.nstr(best[0], 6) if best else None,
        "an_stelle": (f"{mp.nstr(best[1], 6)}+{mp.nstr(best[2], 6)}i") if best else None,
        "gefundene_nullstellen": zeros,
        "trennt_zeta_von_dh": False,
        "lehre": ("Im gerasterten Bereich findet der Test NICHTS -- fuer beide "
                  "Funktionen. Fuer zeta ist das ein Satz, fuer DH nur eine "
                  "Reichweitengrenze des Rasters (die Nullstellen mit Re>1 "
                  "liegen sehr viel hoeher). Musterbeispiel dafuer, dass ein "
                  "negatives numerisches Ergebnis KEINE Struktureigenschaft "
                  "belegt -- vgl. Mertens/Skewes, docs/35."),
    }


# --------------------------------------------------------------------------
# T6 -- Nachweisgrenze des Li-Kriteriums (Sensitivitaetsanalyse)
# --------------------------------------------------------------------------

def li_growth_rate(beta, gamma):
    """|1 - 1/rho| fuer rho = beta + i*gamma.

    Der Beitrag einer Nullstelle rho zum Li-Koeffizienten lambda_n enthaelt
    den Term -(1 - 1/rho)^n. Es gilt

        |1 - 1/rho| > 1   <==>   beta < 1/2,

    denn |1-1/rho|^2 = ((beta-1)^2+gamma^2)/(beta^2+gamma^2) und
    (beta-1)^2 > beta^2 <=> beta < 1/2. Eine Nullstelle LINKS der kritischen
    Geraden treibt lambda_n also exponentiell nach -unendlich -- das ist der
    Mechanismus des Li-Kriteriums. Entscheidend ist die RATE:

        |1 - 1/rho| = 1 + (1-2 beta)/(2 gamma^2) + O(gamma^-4),

    sie faellt also quadratisch mit der Hoehe.
    """
    b, g = mpf(beta), mpf(gamma)
    return mp.sqrt(((b - 1) ** 2 + g ** 2) / (b ** 2 + g ** 2))


def _li_main_term(n):
    """Groessenordnung von lambda_n bei RH-konformem Verhalten: ~ (n/2)(log n - 1 - log 2pi)."""
    n = mpf(n)
    return (n / 2) * (mp.log(n) - 1 - mp.log(2 * pi))


def li_detection_threshold(beta, gamma, n_start=100, n_max=10 ** 15):
    """Kleinstes n, bei dem der Beitrag einer Nullstelle beta+i*gamma den Hauptterm erreicht.

    Das ist die Groessenordnung, ab der lambda_n die Verletzung ueberhaupt
    SEHEN kann. Rueckgabe None, falls beta >= 1/2 (kein exponentielles Wachstum)
    oder n_max ueberschritten.
    """
    r = li_growth_rate(beta, gamma)
    if r <= 1:
        return None
    hi = n_start
    while r ** hi < _li_main_term(hi):
        hi *= 2
        if hi > n_max:
            return None
    lo = max(n_start, hi // 2)
    if r ** lo >= _li_main_term(lo):
        return lo
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if r ** mid >= _li_main_term(mid):
            hi = mid
        else:
            lo = mid
    return hi


def li_reach(n_budget, beta=0.4, gamma_max=10 ** 7):
    """Umkehrung: bis zu welcher Hoehe gamma schliesst lambda_1..lambda_n Nullstellen abseits aus?"""
    lo, hi = mpf("0.05"), mpf(gamma_max)
    for _ in range(200):
        mid = mp.sqrt(lo * hi)
        t = li_detection_threshold(beta, mid)
        if t is not None and t <= n_budget:
            lo = mid
        else:
            hi = mid
    return lo


def test_li_sensitivity(offline_zeros=None, budgets=(10, 100, 1000, 10 ** 4, 10 ** 6, 10 ** 9)):
    """Wie weit traegt numerische Evidenz aus lambda_n >= 0 wirklich?

    Angewandt auf die tatsaechlichen DH-Nullstellen (deren Spiegelpartner
    1 - conj(rho) links der Geraden liegt) und als allgemeine Reichweitentabelle.
    Ergebnis siehe docs/57: die Reichweite skaliert wie gamma^2, weshalb selbst
    n ~ 10^9 nur bis gamma ~ 2000 traegt -- gegenueber gamma ~ 3e12 bei direkter
    Nullstellenberechnung (docs/24).
    """
    if offline_zeros is None:
        offline_zeros = [(1 - sr, si) for sr, si in DH_OFFLINE_SEEDS]
    konkret = []
    for b, g in offline_zeros:
        n = li_detection_threshold(b, g)
        konkret.append({
            "rho": f"{float(b):.6f}+{float(g):.4f}i",
            "wachstumsrate_minus_1": mp.nstr(li_growth_rate(b, g) - 1, 4),
            "n_min": n,
        })
    reichweite = [{"n_budget": n, "gamma_max": mp.nstr(li_reach(n), 5)} for n in budgets]
    return {
        "test": "T6 Nachweisgrenze des Li-Kriteriums",
        "erklaerung": ("Der Beitrag einer Nullstelle links der Geraden waechst wie "
                       "(1 + (1-2beta)/(2 gamma^2))^n. Die Rate faellt quadratisch mit "
                       "der Hoehe, die noetige Ordnung n waechst daher wie gamma^2."),
        "dh_nullstellen": konkret,
        "reichweite_je_budget": reichweite,
        "trennt_zeta_von_dh": False,
        "lehre": ("Numerische Li-Positivitaet ist als RH-Evidenz um Groessenordnungen "
                  "schwaecher als direkte Nullstellenberechnung. Ein Budget von n <= 1000 "
                  "schliesst Nullstellen abseits nur unterhalb der ERSTEN zeta-Nullstelle "
                  "aus. Das ist kein Mangel der Rechnung, sondern der Sensitivitaet des "
                  "Kriteriums."),
    }


# --------------------------------------------------------------------------
# Batterie
# --------------------------------------------------------------------------

def run_all(T=120, h=0.1, funcs=("zeta", "dh")):
    out = {"parameter": {"T": T, "h": h, "mp_dps": mp.dps}, "ergebnisse": {}}
    for name in funcs:
        out["ergebnisse"][name] = {
            "label": FUNCS[name]["label"],
            "T1_funktionalgleichung": test_functional_equation(name),
            "T2_euler_produkt": test_euler_product(name),
            "T3_offline_nullstellen": test_offline_zeros(name),
            "T4_vorzeichenwechsel_defizit": test_sign_change_deficit(name, T, h),
            "T5_rechts_von_1": test_zeros_right_of_1(name, T=min(T, 120)),
        }
    out["T6_li_sensitivitaet"] = test_li_sensitivity()
    out["fazit"] = _verdict(out["ergebnisse"])
    return out


def _verdict(res):
    if not {"zeta", "dh"} <= set(res):
        return "Beide Funktionen noetig fuer das Trennungsurteil."
    lines = []
    for key in ("T1_funktionalgleichung", "T2_euler_produkt", "T3_offline_nullstellen",
                "T4_vorzeichenwechsel_defizit", "T5_rechts_von_1"):
        z, d = res["zeta"][key], res["dh"][key]
        lines.append({
            "test": z["test"],
            "zeta": _short(z),
            "dh": _short(d),
            "trennend": z.get("trennt_zeta_von_dh", False),
        })
    return lines


def _short(r):
    for k in ("bestanden", "rh_verletzung_nachgewiesen", "rh_verletzung_detektiert"):
        if k in r:
            return f"{k}={r[k]}"
    z = r.get("gefundene_nullstellen")
    if z is not None:
        return f"gefundene_nullstellen={len(z)}"
    return "-"


def main(argv=None):
    p = argparse.ArgumentParser(description="Gegenbeispiel-Orakel (Davenport-Heilbronn)")
    p.add_argument("test", nargs="?", default="all",
                   choices=["all", "fe", "euler", "offline", "deficit", "rightof1", "lisens"])
    p.add_argument("-T", type=float, default=120.0, help="Hoehe T (Standard 120)")
    p.add_argument("--h", type=float, default=0.1, help="Schrittweite fuer Z-Abtastung")
    p.add_argument("--func", default="", help="nur eine Funktion: zeta | dh")
    args = p.parse_args(argv)

    names = (args.func,) if args.func else ("zeta", "dh")
    if args.test == "all":
        res = run_all(T=args.T, h=args.h, funcs=names)
    else:
        fn = {"fe": lambda n: test_functional_equation(n),
              "euler": lambda n: test_euler_product(n),
              "offline": lambda n: test_offline_zeros(n),
              "deficit": lambda n: test_sign_change_deficit(n, args.T, args.h),
              "rightof1": lambda n: test_zeros_right_of_1(n, T=args.T),
              "lisens": lambda n: test_li_sensitivity()}[args.test]
        res = {n: fn(n) for n in names}
    print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
