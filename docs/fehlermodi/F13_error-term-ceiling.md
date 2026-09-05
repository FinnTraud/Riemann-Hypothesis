---
id: blk-proportion-ceiling
f_mode: F13
title: "F13 — Anteils-Decke der Mollifier-Methoden"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F13 — Anteils-Decke der Mollifier-Methoden

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-proportion-ceiling`

> Levinson/Conrey-Technik liefert einen positiven Anteil, ist aber strukturell weit unter 100 % gedeckelt.

Die Mollifier-Methode zeigt, dass ein positiver Anteil der Nullstellen auf der Geraden liegt (Levinson 1/3, Conrey 2/5, heute >41 %). Die Schranke wächst seit 50 Jahren in Zehntelprozentschritten. Der Grund ist strukturell: die Länge des Mollifiers ist durch die verfügbaren Momentenschätzungen begrenzt, und selbst ein idealer Mollifier liefert nicht 100 %. Wichtig: 100 % im Dichtesinn wäre ohnehin NICHT die RH — eine Nullstellenmenge der Dichte 0 abseits der Geraden bliebe zulässig.

## Diagnosefrage

**Welcher Mittelwertsatz begrenzt die Methode, und was wäre nötig, um 100 Prozent zu erreichen?**

## Fluchtbedingung

Ein Mechanismus, der ALLE Nullstellen erfasst statt einen Anteil — Anteilsmethoden können die RH prinzipiell nicht abschließen, auch nicht im Limes.

## Abweichende Einstufung

Die unabhaengige Klassifikation aus PR#5 stuft diesen Modus als Tier 3 ein, diese hier als Tier 2. Beide Lesarten sind vertretbar; siehe docs/55, Abschnitt 'Wie robust ist die Tier-Einstufung?'.

## Betroffene Ansätze (6)

- [[03_Hardy_1914_infinitely_many_zeros]]
- [[04_Levinson_Conrey_positive_proportion]]
- [[07_Keating_Snaith_moments]]
- [[17_Lindelof_density_hypothesis]]
- [[22_Guth_Maynard_2024]]
- [[66_Speiser_zeros_of_zeta_prime]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
