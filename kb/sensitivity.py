#!/usr/bin/env python3
"""Sensitivitaetsanalyse der RH-Kriterien: wie weit traegt numerische Evidenz?

Die Frage
---------
Ein aequivalentes Kriterium ist logisch genau so stark wie die RH (docs/58).
Numerisch ist es das NICHT: jedes Kriterium hat eine eigene Aufloesung, und
die entscheidet, ob eine Rechnung ueberhaupt etwas ausschliessen kann.

    "lambda_n >= 0 fuer n <= 1000" klingt nach Bestaetigung.
    Tatsaechlich schliesst es Nullstellen abseits der Geraden nur bis
    Hoehe gamma ~ 3.6 aus -- unterhalb der ERSTEN zeta-Nullstelle (14.13).

Dieses Modul beantwortet dieselbe Frage fuer die anderen Kriterien der
Wissensbasis. Es ist Experiment (2) aus docs/63 (bestes Aufwand-Nutzen-
Verhaeltnis der dortigen Rangliste). Ergebnisse: docs/65.

Was hier gerechnet wird
-----------------------
  ROBIN     Kolossal abundante Zahlen werden konstruiert und die Marge
            1 - sigma(n)/(e^gamma n loglog n) GEMESSEN. Keine Annahme --
            reine Rechnung. Daraus ein empirisches Abklinggesetz.
  d_N       Aufloesungsgrenze aus der BBLS-Asymptotik d_N^2 ~ C/log N mit
            C = 2 + gamma - log(4 pi). ACHTUNG: diese Asymptotik ist eine
            VERMUTUNG (BBLS 2000) unter RH mit einfachen Nullstellen, kein
            Satz -- die Reichweitentabelle ist entsprechend bedingt.
  Li        aus kb/counterexample.py (T6), hier nur zum Vergleich.
  Lambda    strukturell anders; siehe die Notiz in compare().

CLI
---
    python3 kb/sensitivity.py robin            # CA-Zahlen rechnen, Marge messen
    python3 kb/sensitivity.py robin --max-logn 550000
    python3 kb/sensitivity.py dn               # Aufloesungsgrenze d_N
    python3 kb/sensitivity.py compare          # Gesamtvergleich
    python3 kb/sensitivity.py all --json
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

EULER = 0.5772156649015328606
#: BBLS-Konstante  Sum_rho 1/|rho|^2  =  2 + gamma - log(4 pi)
C_BBLS = 2 + EULER - math.log(4 * math.pi)


# --------------------------------------------------------------------------
# Robin: kolossal abundante Zahlen
# --------------------------------------------------------------------------

def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i, v in enumerate(s) if v]


def ca_exponents(eps, primes):
    """Exponenten der kolossal abundanten Zahl zum Parameter eps.

    a_p(eps) = floor( log( (p^(1+eps) - 1) / (p^eps - 1) ) / log p ) - 1

    Kolossal abundante Zahlen sind die Kandidaten fuer Robin-Verletzungen:
    verletzt irgendein n Robins Ungleichung, dann auch eine CA-Zahl. Sie sind
    also der schaerfste Testort -- und ihre Faktorisierung ist bekannt, was
    die Rechnung ueberhaupt erst moeglich macht (siehe Kompressions-Hinweis
    in compare()).
    """
    out = []
    for p in primes:
        lp = math.log(p)
        # log((p^(1+e)-1)/(p^e-1)) numerisch stabil
        num = math.log(math.expm1((1 + eps) * lp))
        den = math.log(math.expm1(eps * lp))
        a = int(math.floor((num - den) / lp)) - 1
        if a <= 0:
            break
        out.append((p, a))
    return out


def robin_point(eps, primes):
    """Ein Messpunkt: (log n, sigma(n)/n, Verhaeltnis R, Marge, omega)."""
    ex = ca_exponents(eps, primes)
    if not ex:
        return None
    log_n = 0.0
    log_sigma_over_n = 0.0
    for p, a in ex:
        lp = math.log(p)
        log_n += a * lp
        # (p^(a+1)-1) / (p^a (p-1))  =  (1 - p^-(a+1)) / (1 - p^-1)
        log_sigma_over_n += math.log1p(-math.exp(-(a + 1) * lp)) - math.log1p(-1.0 / p)
    if log_n < math.e:
        return None
    sigma_over_n = math.exp(log_sigma_over_n)
    rhs = math.exp(EULER) * math.log(log_n)
    R = sigma_over_n / rhs
    return {"eps": eps, "omega": len(ex), "groesster_primfaktor": ex[-1][0],
            "log_n": log_n, "stellen_von_n": log_n / math.log(10),
            "sigma_n_durch_n": sigma_over_n, "e_gamma_loglog_n": rhs,
            "verhaeltnis_R": R, "marge": 1.0 - R,
            "robin_erfuellt": R < 1.0}


def robin_scan(eps_list=None, max_logn=60000):
    """Misst die Robin-Marge entlang kolossal abundanter Zahlen."""
    if eps_list is None:
        eps_list = [5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3, 5e-4, 2e-4, 1e-4,
                    5e-5, 2e-5, 1e-5, 5e-6, 2e-6, 1e-6]
    # log n ~ 0.11/eps  =>  groesster benoetigter Primfaktor ~ log n
    limit = max(1000, int(max_logn * 1.3))
    primes = sieve(limit)
    rows = []
    for eps in eps_list:
        r = robin_point(eps, primes)
        if r and r["log_n"] <= max_logn:
            rows.append(r)
    return rows


def robin_fit(rows, min_logn=100.0):
    """Fit  marge ~ K / (sqrt(log n) * log log n).

    Die Form ist nicht geraten: sie folgt aus der bekannten Gestalt der
    Robin-Schranke, bei der die absolute Luecke e^gamma loglog n - sigma(n)/n
    wie 1/sqrt(log n) abklingt. Der Fit prueft genau das nach.
    """
    used = [r for r in rows if r["log_n"] >= min_logn and r["marge"] > 0]
    if not used:
        return None
    ks = [r["marge"] * math.sqrt(r["log_n"]) * math.log(r["log_n"]) for r in used]
    K = sum(ks) / len(ks)
    spread = (max(ks) - min(ks)) / K if K else float("inf")
    return {"K": K, "streuung_relativ": spread, "punkte": len(used),
            "log_n_bereich": [used[0]["log_n"], used[-1]["log_n"]],
            "formel": "marge ~ K / (sqrt(log n) * log log n)",
            "absolute_luecke": ("e^gamma loglog n - sigma(n)/n ~ K * e^gamma / sqrt(log n) "
                                f"= {K * math.exp(EULER):.3f} / sqrt(log n)")}


def robin_reach(K, target_margin):
    """Welches log n gehoert zu einer Ziel-Marge? (Umkehrung des Fits)"""
    lo, hi = math.e + 1e-9, 1e18
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        if math.sqrt(mid) * math.log(mid) * target_margin < K:
            lo = mid
        else:
            hi = mid
    log_n = hi
    # Rechenkosten: die CA-Zahl braucht alle Primzahlen bis ~ log n (Chebyshev)
    omega = log_n / math.log(log_n) if log_n > math.e else 0
    return {"marge": target_margin, "log_n": log_n,
            "stellen_von_n": log_n / math.log(10),
            "benoetigte_primzahlen_ca": omega}


# --------------------------------------------------------------------------
# d_N: Aufloesungsgrenze
# --------------------------------------------------------------------------

def dn_value(N):
    """Erwartetes d_N nach der BBLS-Asymptotik d_N^2 ~ C/log N. VERMUTUNG, kein Satz."""
    return math.sqrt(C_BBLS / math.log(N)) if N > 1 else float("nan")


def dn_reach(delta):
    """Welche Dimension N braucht es, damit d_N unter delta faellt?"""
    log_N = C_BBLS / delta ** 2
    return {"aufloesung_delta": delta, "log_N": log_N,
            "stellen_von_N": log_N / math.log(10)}


def dn_table(deltas=(0.2, 0.1, 0.05, 0.01, 1e-3, 1e-6)):
    return [dn_reach(d) for d in deltas]


# --------------------------------------------------------------------------
# Vergleich
# --------------------------------------------------------------------------

def compare(robin_K=None):
    if robin_K is None:
        robin_K = robin_fit(robin_scan(max_logn=20000))["K"]
    try:
        import counterexample as _cx
        li_reach_1e9 = float(_cx.li_reach(10 ** 9))
        li_reach_1e6 = float(_cx.li_reach(10 ** 6))
    except Exception:
        li_reach_1e9 = li_reach_1e6 = None

    return {
        "frage": ("Wie gross muss das Rechenbudget sein, damit ein Kriterium eine "
                  "RH-Verletzung ueberhaupt SEHEN koennte?"),
        "kriterien": [
            {"kriterium": "Direkte Nullstellenberechnung (docs/24)",
             "budget_parameter": "Hoehe T",
             "kostengesetz": "linear in T (Riemann-Siegel / Turing-Zertifikat)",
             "erreicht": "gamma ~ 3e12 rigoros verifiziert (Platt)",
             "kompressibel": False,
             "urteil": "Referenzmassstab. Alles andere wird hieran gemessen."},
            {"kriterium": "Li-Koeffizienten lambda_n (docs/14)",
             "budget_parameter": "Ordnung n",
             "kostengesetz": "n ~ gamma^2 (aus |1-1/rho| = 1 + (1-2beta)/(2 gamma^2))",
             "erreicht": (f"Budget n<=1e6 traegt bis gamma ~ {li_reach_1e6:.0f}; "
                          f"n<=1e9 bis gamma ~ {li_reach_1e9:.0f}"
                          if li_reach_1e6 else "siehe kb/counterexample.py lisens"),
             "kompressibel": False,
             "urteil": "Um 9 Groessenordnungen schwaecher als direkte Rechnung."},
            {"kriterium": "Robins Ungleichung (docs/15)",
             "budget_parameter": "Groesse n (kolossal abundant)",
             "kostengesetz": "marge ~ K/(sqrt(log n) log log n), "
                             f"K = {robin_K:.3f} (hier gemessen)",
             "erreicht": "Marge ~1e-3 bei log n ~ 8600 -- hier gerechnet",
             "kompressibel": True,
             "urteil": ("Nominal astronomisch, praktisch aber weit tragfaehiger als es "
                        "aussieht: CA-Zahlen speichert man als Exponentenvektor, die "
                        "Kosten wachsen nur wie pi(log n).")},
            {"kriterium": "Baez-Duarte-Distanz d_N (docs/13)",
             "budget_parameter": "Dimension N des Least-Squares-Problems",
             "kostengesetz": "d_N^2 ~ C/log N, C = 2+gamma-log(4pi) = %.6f "
                             "(BBLS-VERMUTUNG, kein Satz)" % C_BBLS,
             "erreicht": "N=32, d_N=0.117 (kb/research/results/dn_experiment_note.md)",
             "kompressibel": False,
             "urteil": ("Schlechtestes Kriterium der Sammlung. d_N < 0.01 verlangt "
                        "N ~ 1e201 -- und N ist die DIMENSION einer Matrix, nicht die "
                        "Groesse einer Zahl. Nicht komprimierbar, also endgueltig.")},
            {"kriterium": "de-Bruijn-Newman-Konstante Lambda (docs/23)",
             "budget_parameter": "kein Rechenbudget",
             "kostengesetz": "nicht anwendbar -- siehe Bemerkung",
             "erreicht": "0 <= Lambda <= 0.22 (Rodgers-Tao 2018 / Polymath15 2019)",
             "kompressibel": None,
             "urteil": ("Strukturell anders und deshalb hier der interessanteste Fall: "
                        "Lambda ist keine Aufloesungsfrage. Die Methode gewinnt ihre "
                        "Kraft aus der Glaettung bei t > 0, und genau die verschwindet "
                        "bei t -> 0. Es ist keine Wand aus Rechenzeit, sondern eine "
                        "Wand aus Methode: mehr Rechnen hilft grundsaetzlich nicht.")},
        ],
        "rangfolge_schaerfe": ["direkte Nullstellenberechnung", "Li-Kriterium",
                               "Robin", "d_N"],
        "kernaussage": ("Alle vier Kriterien sind LOGISCH aequivalent zur RH und "
                        "NUMERISCH um viele Groessenordnungen verschieden scharf. "
                        "Wer 'das Kriterium wurde numerisch bestaetigt' liest, muss "
                        "fragen: bis zu welcher Hoehe eigentlich?"),
        "siehe": ["docs/65", "docs/57", "docs/59", "docs/63"],
    }


# --------------------------------------------------------------------------

def _print_robin(rows, fit):
    print("Robin-Marge entlang kolossal abundanter Zahlen (gemessen, keine Annahme)\n")
    print("      eps   omega  groesster p        log n     Stellen  sigma(n)/n   "
          "e^g lglg n      R(n)        Marge")
    for r in rows:
        flag = "" if r["robin_erfuellt"] else "   <-- ROBIN VERLETZT"
        print(f"  {r['eps']:.0e} {r['omega']:7d} {r['groesster_primfaktor']:12d} "
              f"{r['log_n']:12.2f} {r['stellen_von_n']:11.4g} {r['sigma_n_durch_n']:11.6f} "
              f"{r['e_gamma_loglog_n']:12.6f} {r['verhaeltnis_R']:11.8f} "
              f"{r['marge']:12.8f}{flag}")
    if fit:
        print(f"\n  Fit: {fit['formel']}")
        print(f"       K = {fit['K']:.4f}  (relative Streuung {fit['streuung_relativ']:.1%} "
              f"ueber {fit['punkte']} Punkte, log n in "
              f"[{fit['log_n_bereich'][0]:.0f}, {fit['log_n_bereich'][1]:.0f}])")
        print(f"       {fit['absolute_luecke']}")
        print("\n  Reichweite (Umkehrung des Fits):")
        print("     Ziel-Marge      log n     Stellen von n   benoetigte Primzahlen")
        for t in (1e-3, 1e-4, 1e-6, 1e-8):
            r = robin_reach(fit["K"], t)
            print(f"       {t:.0e}   {r['log_n']:12.6g}   10^{r['stellen_von_n']:<12.4g} "
                  f"{r['benoetigte_primzahlen_ca']:12.4g}")


def _print_dn():
    print("Baez-Duarte d_N: Aufloesungsgrenze")
    print(f"  Asymptotik (BBLS-VERMUTUNG, kein Satz): d_N^2 ~ C/log N, "
          f"C = 2+gamma-log(4pi) = {C_BBLS:.9f}\n")
    print("     Aufloesung      log N        N")
    for row in dn_table():
        print(f"       d_N < {row['aufloesung_delta']:<8g} {row['log_N']:12.6g}   "
              f"10^{row['stellen_von_N']:.6g}")
    print("\n  Im Repo erreicht: N=32, d_N=0.117 "
          "(kb/research/results/dn_experiment_note.md)")
    print("  N ist die DIMENSION eines Least-Squares-Problems mit wachsender "
          "Kondition —\n  nicht die Groesse einer Zahl. Es gibt hier keine Kompression.")


def _print_compare(c):
    print(c["frage"] + "\n")
    for k in c["kriterien"]:
        print(f"  {k['kriterium']}")
        print(f"     Budget:   {k['budget_parameter']}")
        print(f"     Gesetz:   {k['kostengesetz']}")
        print(f"     Erreicht: {k['erreicht']}")
        if k["kompressibel"] is not None:
            print(f"     Testobjekte komprimierbar: {'ja' if k['kompressibel'] else 'nein'}")
        print(f"     -> {k['urteil']}\n")
    print("  " + c["kernaussage"])


def main(argv=None):
    p = argparse.ArgumentParser(description="Sensitivitaet der RH-Kriterien")
    p.add_argument("was", nargs="?", default="all",
                   choices=["all", "robin", "dn", "compare"])
    p.add_argument("--max-logn", type=float, default=20000.0,
                   help="obere Grenze fuer log n bei Robin (Standard 20000)")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)

    out = {}
    if a.was in ("all", "robin"):
        rows = robin_scan(max_logn=a.max_logn)
        fit = robin_fit(rows)
        out["robin"] = {"messpunkte": rows, "fit": fit,
                        "reichweite": [robin_reach(fit["K"], t)
                                       for t in (1e-3, 1e-4, 1e-6, 1e-8)] if fit else []}
        if not a.json:
            _print_robin(rows, fit)
            print()
    if a.was in ("all", "dn"):
        out["dn"] = {"C_BBLS": C_BBLS, "reichweite": dn_table(),
                     "vorbehalt": ("d_N^2 ~ C/log N ist die BBLS-VERMUTUNG unter RH mit "
                                   "einfachen Nullstellen, kein Satz.")}
        if not a.json:
            _print_dn()
            print()
    if a.was in ("all", "compare"):
        K = out.get("robin", {}).get("fit", {}).get("K") if out.get("robin") else None
        c = compare(robin_K=K)
        out["vergleich"] = c
        if not a.json:
            _print_compare(c)
    if a.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
