---
id: blk-positivity-circular
f_mode: F2
title: "F2 — Zirkuläre Positivität"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F2 — Zirkuläre Positivität

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-positivity-circular`

> Die RH wird auf eine Positivitätsaussage reduziert, die selbst nur als äquivalent, nie unabhängig bewiesen ist.

Der mit Abstand häufigste Blocker. Ein Ansatz zeigt: RH ⟺ (quadratische Form ≥ 0) bzw. (Funktion hat nur reelle Nullstellen). Das ist ein echter Erkenntnisgewinn über die STRUKTUR der Aussage, aber kein Fortschritt in der Beweisstärke: die Positivität ist genau so schwer wie die RH. Ein Beweis entsteht erst, wenn die Positivität aus einer unabhängigen Quelle folgt (Schnitttheorie, Spektralsatz, Darstellungstheorie) — nicht aus der Nullstellenlage, die man beweisen will.

## Diagnosefrage

**Woher genau kommt das Vorzeichen? Gibt es eine polarisierte Geometrie, die es erzwingt?**

## Fluchtbedingung

Die Positivität muss aus einer Struktur folgen, die unabhängig von der Nullstellenlage definiert ist. Im bewiesenen Fall 𝔽_q (doc-18) leistet das die Schnittform auf der Fläche C×C — dort ist Positivität ein Satz der Geometrie, nicht eine Umformulierung des Ziels.

## Betroffene Ansätze (11)

- [[10_Connes_noncommutative_geometry]]
- [[13_Nyman_Beurling_Baez_Duarte]]
- [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity]]
- [[20_de_Branges_Hilbert_spaces]]
- [[23_de_Bruijn_Newman_constant_Polymath15]]
- [[25_Atiyah_2018_failed_proof]]
- [[29_Jensen_Polya_Laguerre_Polya_GORZ]]
- [[33_statistical_mechanics_Lee_Yang]]
- [[45_further_equivalent_criteria]]
- [[52_Connes_truncated_Weil_spectral_realization]]
- [[71_standard_conjectures_motives_positivity]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
