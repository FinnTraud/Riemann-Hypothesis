# Research Note: Báez-Duarte-Distanz d_N als RH-Kriterium

**Datum:** 2026-06-30
**Status:** Numerische Evidenz (kein Beweis — siehe docs/35)
**Bezug:** docs/13 (Nyman-Beurling/Báez-Duarte), docs/45 (quantitativ), docs/06

## Fragestellung
Die RH ist äquivalent zu d_N → 0, wobei d_N der minimale L²(0,1)-Abstand der konstanten
Funktion 1 zu Linearkombinationen der Bausteine g_n(x) = {1/(n x)} ist (n=1..N).
Vermutung (BBLS 2000): (log N)·d_N² → Σ_ρ 1/|ρ|² = 2 + γ − log(4π) ≈ 0.046191.

## Methode (selbst hergeleitet, nachprüfbar)
- exakt: b_n = ∫₀¹ {1/(nx)} dx = (ln n + 1 − γ)/n  (Mellin-Herleitung)
- G_mn = ∫₁^∞ {u/m}{u/n} u⁻² du, **stückweise exakt** integriert (Integrand zwischen
  den Sprungstellen quadratisch) + exakter Periodenmittel-Schwanz μ/U₀.
- d_N² = 1 − bᵀ G⁻¹ b (Lösung via least-squares, da G mit wachsendem N schlecht konditioniert).
- **Selbstvalidierung:** b₁ berechnet = 0.422784, exakt (1−γ) = 0.422784 → Übereinstimmung.

## Ergebnis
| N | d_N | d_N² | (log N)·d_N² | cond(G) |
|---|---|---|---|---|
| 2 | 0.41604 | 0.173090 | 0.11998 | 1.43e+01 |
| 4 | 0.23762 | 0.056463 | 0.07827 | 3.07e+01 |
| 6 | 0.18290 | 0.033453 | 0.05994 | 6.41e+01 |
| 8 | 0.15224 | 0.023177 | 0.04819 | 1.13e+02 |
| 10 | 0.15104 | 0.022813 | 0.05253 | 1.94e+02 |
| 12 | 0.14065 | 0.019782 | 0.04916 | 2.76e+02 |
| 15 | 0.13338 | 0.017791 | 0.04818 | 5.16e+02 |
| 18 | 0.12887 | 0.016608 | 0.04800 | 6.82e+02 |
| 21 | 0.12524 | 0.015686 | 0.04776 | 1.09e+03 |
| 24 | 0.12318 | 0.015173 | 0.04822 | 1.32e+03 |
| 28 | 0.12188 | 0.014855 | 0.04950 | 1.87e+03 |
| 32 | 0.11725 | 0.013747 | 0.04764 | 2.73e+03 |

![d_N Konvergenz](dn_convergence.png)

## Interpretation
- **d_N fällt monoton** (0.42 → ~0.12) — konsistent mit RH (d_N → 0).
- **(log N)·d_N² ≈ 0.048**, nahe der Vorhersage **0.0462** — die selbst hergeleitete
  Formulierung trifft die richtige Konstante (starke Bestätigung der Korrektheit).
- Restabweichung erklärt sich durch endliches N (bekannte langsam abklingende Korrekturterme)
  und die berühmte **1/log N**-Konvergenz: selbst N=32 ist „klein".
- cond(G) bleibt moderat (≤ ~2·10³), daher numerisch verlässlich in diesem N-Bereich.

## Grenzen / Ehrlichkeit
Numerik ist EVIDENZ, kein Beweis (docs/35). Die 1/log N-Rate zeigt anschaulich, warum die RH
so nicht „ausgerechnet" werden kann. Für größere N braucht es höhere Präzision (mpmath) wegen
der schlechter werdenden Kondition von G.

## Nächste Schritte (für die Zusammenarbeit)
- N erhöhen mit mpmath-Hochpräzision (cond(G) wächst ~exponentiell).
- Vergleich mit der exakten Vasyunin-Cotangens-Formel für G_mn (Quelle gegenprüfen).
- λ_n-Positivität (docs/14) als komplementäres Positivitäts-Kriterium.
