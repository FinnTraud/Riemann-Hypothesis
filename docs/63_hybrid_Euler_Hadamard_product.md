---
id: doc-63
number: 63
title: "Hybrides Euler–Hadamard-Produkt (Gonek–Hughes–Keating)"
category: heuristic
status: open
tags: [gonek-hughes-keating, hybrid-model, moments, splitting-conjecture, arithmetic-factor, random-matrix]
source_file: 63_hybrid_Euler_Hadamard_product.md
lang: de
---

# Hybrides Euler–Hadamard-Produkt — die Nahtstelle zwischen Arithmetik und Zufallsmatrix

**Kategorie:** Modell / Heuristik mit bewiesenem Kern
**Autoren / Jahre:** Gonek–Hughes–Keating (2007); Bui–Keating, Gonek (2010er); Heap, Harper (Momente)
**Typ:** Faktorisierung von ζ in einen „Primzahl-Teil" und einen „Nullstellen-Teil"
**Status:** Faktorisierung als Satz (unter milden Bedingungen) bewiesen; die daraus gezogene **Splitting-Vermutung** offen

## Zusammenfassung
Warum sagt Zufallsmatrixtheorie (Dok. 06/07) die Statistik der ζ-Nullstellen so gut voraus — und warum reicht sie trotzdem nicht? Das hybride Euler–Hadamard-Produkt beantwortet beides: Es zerlegt ζ **beweisbar** in ein kurzes Euler-Produkt über Primzahlen p ≤ X und ein Hadamard-artiges Produkt über die Nullstellen im Abstand ≲ 1/log X. Die Arithmetik sitzt im ersten Faktor, die Zufallsmatrix im zweiten. Die Momentenvermutungen von Keating–Snaith bekommen damit eine **strukturelle Erklärung** — und die offene Stelle wird exakt lokalisierbar.

## Mathematischer Kern

### Die Faktorisierung (GHK 2007)
Sei u eine glatte, nichtnegative Testfunktion mit `∫u = 1`, Träger in [0,1], und
```
U(z) = ∫_0^∞ u(x) E_1(z log x) dx      (E_1 = Exponentialintegral).
```
Dann gilt für `s = σ + it` im kritischen Streifen (unter milder Wachstumsbedingung, bewiesen für X = O((log t)^{2−ε}) und allgemeiner unter RH):
```
ζ(s)  =  P_X(s) · Z_X(s) · (1 + o(1)),
```
mit dem **Primzahl-Faktor**
```
P_X(s) = exp( Σ_{n ≤ X}  Λ(n) / (log n · n^{s}) )        (glatt abgeschnitten),
```
und dem **Nullstellen-Faktor**
```
Z_X(s) = exp( − Σ_ρ  U( (s − ρ) log X ) ).
```
`P_X` „kennt" nur Primzahlen bis X; `Z_X` „kennt" nur Nullstellen in einem Fenster der Breite ~1/log X um s.

### Die Splitting-Vermutung
Für die 2k-ten Momente auf der kritischen Geraden:
```
(1/T) ∫_0^T |ζ(1/2+it)|^{2k} dt  ~  a_k · g_k · (log T)^{k²},
```
wobei
```
a_k = ∏_p ( (1−1/p)^{k²} Σ_{m≥0} (Γ(m+k)/(m! Γ(k)))² p^{−m} )      (arithmetischer Faktor),
g_k = G(1+k)²/G(1+2k)                                                (Zufallsmatrix-Faktor, Barnes-G).
```
**Splitting-Vermutung (GHK):** Die Momente faktorisieren asymptotisch entlang der Hybridzerlegung,
```
(1/T)∫ |ζ|^{2k}  ~  [ (1/T)∫ |P_X|^{2k} ] · [ (1/T)∫ |Z_X|^{2k} ],
```
und dabei liefert `P_X` genau `a_k (log X)^{k²}`, `Z_X` genau `g_k (log(T)/log X)^{k²}`. Das erklärt **warum** in der Keating–Snaith-Vermutung (Dok. 07) das Produkt `a_k · g_k` steht: der eine Faktor ist rein arithmetisch, der andere rein spektral, und sie sind (vermutlich) unabhängig.

### Was bewiesen ist
- Die **Faktorisierung selbst** ist ein Satz (mit expliziten Fehlertermen).
- Die Momente von `P_X` sind berechenbar (rein arithmetisch).
- Die Momente von `Z_X` sind unter RMT-Annahmen berechenbar.
- **Offen:** die Unabhängigkeit (das „Splitting") und damit der Schluss auf die ζ-Momente. Bewiesen sind nur k = 1, 2 (Hardy–Littlewood, Ingham) plus untere Schranken der richtigen Ordnung für alle k (Radziwiłł–Soundararajan, Heap–Radziwiłł–Soundararajan) und obere Schranken unter RH (Soundararajan, Harper).

### Warum das Modell die RH nicht liefert (Fehlermodus `F14`)
Das Hybridmodell ist **symmetrisch in der Nullstellenlage**: `Z_X` ist über *die* Nullstellen definiert, wo immer sie liegen. Setzte man eine Nullstelle abseits der Geraden ein, bliebe die Faktorisierung gültig; nur die Statistik von `Z_X` änderte sich. Das Modell **beschreibt** also, es **erzwingt** nicht. Es hat keinen Implikationspfeil `Modell ⇒ RH` — genau wie GUE (Dok. 06) und Cramér (Dok. 39).

**Aber:** es liefert einen *Testrahmen*. Beobachtete Abweichungen der ζ-Momente von `a_k g_k` wären ein ernstes Signal; bis heute stimmen numerische Momente (Odlyzko-Daten, Hiary–Odlyzko) mit der Vorhersage überein.

## Bedeutung / Einordnung
- **Konzeptuell die sauberste Antwort auf „warum funktioniert RMT hier?"** — und damit ein Muss für jeden, der aus GUE-Evidenz mehr machen will, als sie hergibt.
- Verbindungsknoten: Dok. 06 (Paarkorrelation), 07 (Momente), 64 (Extremwerte, benutzt genau diese Zerlegung), 39 (Modelle ≠ Beweise).
- **Experiment (billig):** `P_X`, `Z_X` für kleine X numerisch auswerten und mit ζ vergleichen — zeigt anschaulich, welcher Faktor die Oszillationen trägt. Kandidat fürs Experiment-Logbuch (Dok. 51).

## Quellen
- [S. M. Gonek, C. P. Hughes, J. P. Keating, *A hybrid Euler–Hadamard product for the Riemann zeta function*, Duke Math. J. 136 (2007) (arXiv:math/0511269)](https://arxiv.org/abs/math/0511269)
- [J. P. Keating, N. C. Snaith, *Random matrix theory and ζ(1/2+it)*, Comm. Math. Phys. 214 (2000)](https://link.springer.com/article/10.1007/s002200000261)
- [A. Harper, *Sharp conditional bounds for moments of the Riemann zeta function* (arXiv:1305.4618)](https://arxiv.org/abs/1305.4618)
- [Heap–Radziwiłł–Soundararajan, *Sharp upper bounds for fractional moments* (arXiv:1901.06342)](https://arxiv.org/abs/1901.06342)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_probabilistic|Probabilistische Modelle & Statistik]]

| Achse | Wert |
|---|---|
| Familie | probabilistic |
| Implikation | `model` |
| Euler-Produkt | `essential` |
| Positivität | `n/a` |
| Strenge | `theorem` · Evidenz `strong` |
| Testbar / formalisierbar | `high` / `low` |

**Offener Kernschritt:** Splitting-Vermutung (Unabhängigkeit von Primzahl- und Nullstellenfaktor).

**Hebel (was er liefern würde):** Erklärt strukturell, warum RMT funktioniert und wo die Arithmetik sitzt.

**Typische Fehlermodi:** [[F14_model-without-implication|F14 Modell ohne Implikationspfeil]]

**Vergleichbar mit:** [[64_extreme_values_FHK_multiplicative_chaos|Extremwerte von ζ: Fyodorov–Hiary–Keating & multiplikatives Chaos]] · [[06_Montgomery_pair_correlation_RMT|Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]] · [[07_Keating_Snaith_moments|Keating–Snaith: Momente der Zetafunktion via charakteristische Polynome (CUE)]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-63 doc-64 doc-06 doc-07`

**Ausgehende Beziehungen**
- *ist Instanz von* (`instance_of`) → [[concept_moments|Momente & Zufallsmatrix-Modelle]] — Erklärt die Faktorisierung a_k·g_k der Momentenvermutung.
- *reduziert sich auf* (`reduces_to`) → [[07_Keating_Snaith_moments|07 — Keating–Snaith: Momente der Zetafunktion via charakteristische Polynome (CUE)]] — Strukturelle Begründung der Keating–Snaith-Vorhersage.
- *modelliert* (`models`) → [[06_Montgomery_pair_correlation_RMT|06 — Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]] — Trennt arithmetischen von spektralem Anteil der Statistik.
- *benutzt* (`uses`) → [[concept_euler-product|Euler-Produkt (Multiplikativität)]] — Kurzes Euler-Produkt P_X als arithmetischer Faktor.

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[64_extreme_values_FHK_multiplicative_chaos|64 — Extremwerte von ζ: Fyodorov–Hiary–Keating & multiplikatives Chaos]] — Zerlegung in Primzahl- und Nullstellenanteil ist der technische Kern.

**Thematisch benachbart (gemeinsame Tags):** [[07_Keating_Snaith_moments|Keating–Snaith: Momente der Zetafunktion via charakteristische Polynome (CUE)]] · [[06_Montgomery_pair_correlation_RMT|Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
