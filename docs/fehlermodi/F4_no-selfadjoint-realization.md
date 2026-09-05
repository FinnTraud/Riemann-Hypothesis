---
id: blk-no-selfadjoint-realization
f_mode: F4
title: "F4 — Fehlende selbstadjungierte Realisierung"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F4 — Fehlende selbstadjungierte Realisierung

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-no-selfadjoint-realization`

> Der Operator ist formal hingeschrieben, aber ohne Definitionsbereich, Randbedingungen und Nachweis eines diskreten Spektrums.

Feiner als blk-noncanonical-operator und deshalb getrennt gefuehrt: dort ist der Operator zirkulaer KONSTRUIERT, hier ist er moeglicherweise kanonisch, aber schlicht nicht rigoros definiert. Berry-Keating (doc-08) ist der Musterfall: H = xp ist klassisch elegant und reproduziert die Zaehlfunktion, besitzt aber auf natuerlichen Definitionsbereichen keine wesentlich selbstadjungierte Realisierung mit diskretem Spektrum. Diesen Blocker hat erst die unabhaengige Klassifikation aus PR#5 (dort F4) sichtbar gemacht -- er war in blk-noncanonical-operator subsumiert und dadurch unsichtbar.

## Diagnosefrage

**Auf welchem Hilbertraum, mit welchem Definitionsbereich, ist der Operator wesentlich selbstadjungiert und hat diskretes Spektrum?**

## Fluchtbedingung

Hilbertraum, Definitionsbereich und Randbedingungen explizit angeben und wesentliche Selbstadjungiertheit sowie Diskretheit des Spektrums beweisen -- nicht behaupten.

## Betroffene Ansätze (5)

- [[05_Hilbert_Polya_conjecture]]
- [[08_Berry_Keating_xp_model]]
- [[09_Bender_Brody_Muller_2017_Hamiltonian]]
- [[11_Connes_Moscovici_prolate_spheroidal]]
- [[47_physics_layer_primon_gas_quantum_graphs]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
