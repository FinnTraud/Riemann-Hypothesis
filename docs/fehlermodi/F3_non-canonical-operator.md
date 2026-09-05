---
id: blk-noncanonical-operator
f_mode: F3
title: "F3 — Nicht-kanonischer Operator"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F3 — Nicht-kanonischer Operator

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-noncanonical-operator`

> Ein Hilbert–Pólya-Operator wird konstruiert, um das richtige Spektrum zu haben, statt aus der Arithmetik zu entstehen.

Zu jeder reellen Folge existiert ein selbstadjungierter Operator mit genau dieser Folge als Spektrum. Wer also einen Operator angibt, dessen Eigenwerte die γ_n sind, hat nichts gezeigt — er hat die Realität der γ_n bereits vorausgesetzt. Der Blocker greift immer dann, wenn der Operator nicht mit einer unabhängig definierten Spurformel geliefert wird, die die Primzahlterme der expliziten Formel reproduziert.

## Diagnosefrage

**Wird die Realität des Spektrums benutzt, um die Selbstadjungiertheit zu begründen - oder umgekehrt?**

## Fluchtbedingung

Der Operator muss auf einem arithmetisch definierten Raum leben (Adele, arithmetic site, gefolierter Raum) UND eine Spurformel erfüllen, deren geometrische Seite die Primzahlterme der expliziten Formel liefert. Selbstadjungiertheit muss auf einem konkret angegebenen Definitionsbereich bewiesen sein, nicht behauptet.

## Betroffene Ansätze (6)

- [[05_Hilbert_Polya_conjecture]]
- [[08_Berry_Keating_xp_model]]
- [[09_Bender_Brody_Muller_2017_Hamiltonian]]
- [[11_Connes_Moscovici_prolate_spheroidal]]
- [[35_obstructions_barriers]]
- [[47_physics_layer_primon_gas_quantum_graphs]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
