---
id: doc-03
number: 03
title: "Hardy (1914): Unendlich viele Nullstellen auf der kritischen Geraden"
category: partial-results
status: proven
tags: [hardy, critical-line, Z-function, theta-function]
source_file: 03_Hardy_1914_infinitely_many_zeros.md
lang: de
---

# Hardy (1914): Unendlich viele Nullstellen auf der kritischen Geraden

**Kategorie:** Partielles Resultat
**Autor / Jahr:** G. H. Hardy, 1914 (Erweiterungen: Hardy–Littlewood 1921, Selberg 1942)
**Typ:** Bewiesenes Teilresultat zur RH
**Status:** Bewiesen (echtes Theorem, nicht die volle RH)

## Zusammenfassung
1914 bewies Godfrey Harold Hardy, dass **unendlich viele** nicht-triviale Nullstellen der Riemannschen Zetafunktion exakt auf der kritischen Geraden Re(s) = 1/2 liegen. Dies war das erste rigorose Resultat, das die kritische Gerade als Ort von (unendlich vielen) Nullstellen auszeichnete — ein erster Schritt Richtung RH, aber weit von der vollen Aussage (*alle* Nullstellen) entfernt.

## Kernidee
- Hardy betrachtet die reellwertige **Hardysche Z-Funktion** Z(t), die so konstruiert ist, dass |Z(t)| = |ζ(1/2 + it)| und Z(t) reell ist. Nullstellen von Z(t) auf der reellen t-Achse entsprechen genau Nullstellen von ζ auf der kritischen Geraden.
- Mit Hilfe der **Transformationsformel der Jacobischen Theta-Funktion** zeigt Hardy, dass Z(t) unendlich oft das Vorzeichen wechselt → unendlich viele reelle Nullstellen → unendlich viele ζ-Nullstellen auf Re(s) = 1/2.

## Spätere Verschärfungen
- **Hardy–Littlewood (1921):** Mindestens K·T Nullstellen auf der kritischen Geraden bis zur Höhe T (K > 0 konstant) — d. h. ein *positiver linearer* Anteil der erwarteten Zahl.
- **Selberg (1942):** Verbesserung auf K·T·log T, also einen *positiven Bruchteil aller* N(T) ≈ (T/2π)log T Nullstellen. Selbergs Methode (Mollifier) wurde später von Levinson und Conrey weiterentwickelt (siehe Dok. 04).

## Bedeutung / Einordnung
- Erstes hartes Indiz für die Richtigkeit der RH.
- Liefert die Z-Funktion, die zum zentralen Werkzeug numerischer Verifikation wurde (Vorzeichenwechsel von Z(t) lokalisieren Nullstellen — Grundlage von Turing-Methode, Odlyzko etc., Dok. 24).
- Wichtig: "Unendlich viele auf der Geraden" schließt nicht aus, dass *auch* unendlich viele abseits liegen könnten — genau diese Lücke schließen erst die Anteilsresultate (Dok. 04) teilweise, die volle RH bleibt offen.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Die Hardysche Z-Funktion
Definiere die Riemann-Siegel-Theta-Funktion und Z(t):
```
θ(t) = arg Γ(1/4 + it/2) − (t/2) log π,    Z(t) = e^{iθ(t)} ζ(1/2 + it)
```
**Eigenschaften:** Z(t) ist reellwertig für reelles t, und |Z(t)| = |ζ(1/2 + it)|. Daher gilt: Z(t₀) = 0 ⟺ ζ hat eine Nullstelle bei 1/2 + it₀ auf der kritischen Geraden. Vorzeichenwechsel von Z ⇒ Nullstelle auf der Geraden.

### Hardys Satz und Beweisidee (1914)
**Satz (Hardy).** Z(t) besitzt unendlich viele reelle Nullstellen; also liegen unendlich viele Nullstellen von ζ auf Re(s) = 1/2.

**Beweisskizze (Momentenmethode mit Theta-Transformation).** Hardy betrachtet Integrale von Z(t) gegen Testkerne und nutzt die Funktionalgleichung der Jacobi-Theta-Funktion
```
ϑ(x) = Σ_{n=−∞}^∞ e^{−πn²x},    ϑ(1/x) = √x · ϑ(x).
```
Aus der Mellin-Darstellung von ξ gewinnt er, dass gewisse Mittel von Z(t) nicht für alle großen T dasselbe Vorzeichen behalten können: Wäre Z(t) ab einem Punkt vorzeichenfest, so widerspräche das asymptotische Verhalten der Integrale
```
∫_0^T Z(t) t^{2k} dt
```
(für geeignete k, ausgewertet über die Theta-Transformation an der Stelle, die der kritischen Geraden entspricht) der Annahme. Genauer zeigt Hardy, dass das Verhalten nahe x = 1 der Theta-Funktion erzwingt, dass Z unendlich oft das Vorzeichen wechselt.

### Quantitative Verschärfungen (mit Formeln)
Sei N₀(T) die Anzahl der Nullstellen *auf* der kritischen Geraden bis Höhe T, N(T) die Gesamtzahl (Dok. 02).
- **Hardy–Littlewood (1921):** N₀(T) > c·T für ein c > 0.
- **Selberg (1942):** N₀(T) > c·T log T, also N₀(T) > c·N(T) (positiver Bruchteil), via Mollifier-Mittel ∫ |ζ(1/2+it) M(1/2+it)|² dt mit Dirichlet-Polynom M.
- **Anteil κ := liminf N₀(T)/N(T):** Levinson κ ≥ 1/3, Conrey κ ≥ 2/5, heute κ > 0,41 (Dok. 04).

### Speiser-Äquivalenz (Hintergrund der Mollifier-Methode)
**Satz (Speiser 1934).** RH ⟺ ζ'(s) ≠ 0 für 0 < Re(s) < 1/2. Die Levinson-Methode zählt Nullstellen von ζ'·(Mollifier) und überträgt sie via dieser Äquivalenz auf ζ.

## Quellen
- [Hardy's function Z(t) — results and problems (arXiv 1601.06512)](https://arxiv.org/pdf/1601.06512)
- [A note on Hardy's theorem (HAL)](https://hal.science/hal-01425570v1/document)
- [The Riemann zeta function and its zeros — Russian Math Surveys](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=2762&what=fullteng)
- [Almost all of the nontrivial zeros of the Riemann zeta-function (arXiv 2205.09042)](https://arxiv.org/pdf/2205.09042)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `analytic` |
> | Implikation | `partial` |
> | Euler-Produkt | `partial` |
> | Positivität | `n/a` |
> | Strenge | `theorem` |
> | Evidenz | `n/a` |
> | Testbar | `medium` |
> | Formalisierbar | `high` |
> 
> **Offener Kernschritt:** Von 'unendlich viele' zu 'alle' - der Sprung ist qualitativ, nicht quantitativ.
> 
> **Hebel:** Erster Beweis, dass die Gerade überhaupt ausgezeichnet ist.
> 
> **Fehlermodi:** [[F13_error-term-ceiling|F13 Anteils-Decke der Mollifier-Methoden]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-03`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Anteils-Decke der Mollifier-Methoden** *(Tier 2)* — Levinson/Conrey-Technik liefert einen positiven Anteil, ist aber strukturell weit unter 100 % gedeckelt.
>   *Fluchtbedingung:* Ein Mechanismus, der ALLE Nullstellen erfasst statt einen Anteil — Anteilsmethoden können die RH prinzipiell nicht abschließen, auch nicht im Limes.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (2)
> - *ist Teilresultat für* → **Riemann-Vermutung (RH)** — Hardy: unendlich viele Nullstellen auf der Geraden.
> - ← *Spezialfall von* [[04_Levinson_Conrey_positive_proportion|04 · Levinson, Conrey & Co.]] — Quantifiziert Hardys Resultat (positiver Anteil).

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
