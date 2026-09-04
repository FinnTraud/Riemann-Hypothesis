---
id: blk-model-circularity
f_mode: F14
title: "F14 — Zirkularität der Modellannahme"
type: blocker
tier: 3
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F14 — Zirkularität der Modellannahme

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 3** · Blocker-ID `blk-model-circularity`

> Zufallsmatrix- und probabilistische Modelle setzen die RH voraus, um überhaupt formuliert werden zu können.

Die GUE-Statistik der Nullstellen wird nach 'Entfaltung' (unfolding) formuliert — dazu braucht man die Nullstellen als reelle Folge, was die RH bereits benutzt. Montgomerys Paarkorrelationssatz ist unter RH bewiesen. Cramérs Modell ist eine Heuristik und wurde von Maier in einem wichtigen Regime widerlegt. Modelle liefern also Vorhersagen und Plausibilität, aber keine Implikationsrichtung zur RH hin. Ausnahme und deshalb bemerkenswert: doc-53 zeigt Paarkorrelationsresultate OHNE RH.

## Diagnosefrage

**Was am Modell würde brechen, wenn eine Nullstelle abseits der Geraden läge? Wenn nichts: kein Beweisweg.**

## Fluchtbedingung

Unbedingte Formulierung: Aussagen über Nullstellen ohne die Annahme, dass sie auf der Geraden liegen (doc-53 ist der Prototyp).

## Betroffene Ansätze (8)

- [[06_Montgomery_pair_correlation_RMT]]
- [[07_Keating_Snaith_moments]]
- [[33_statistical_mechanics_Lee_Yang]]
- [[39_Cramer_probabilistic_model]]
- [[53_pair_correlation_alternative_hypothesis]]
- [[74_hybrid_Euler_Hadamard_product]]
- [[75_extreme_values_FHK_multiplicative_chaos]]
- [[76_higher_correlations_Rudnick_Sarnak]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
