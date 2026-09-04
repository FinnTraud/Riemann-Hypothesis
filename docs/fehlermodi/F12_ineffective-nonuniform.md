---
id: blk-ineffective-constants
f_mode: F12
title: "F12 — Ineffektive oder nicht gleichmaessige Konstanten"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F12 — Ineffektive oder nicht gleichmaessige Konstanten

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-ineffective-constants`

> Schranken sind nicht explizit oder nicht gleichmaessig in Hoehe und Fuehrer.

Ein Resultat mit ineffektiver Konstante laesst sich nicht in eine Rechnung uebersetzen und nicht mit anderen Schranken kombinieren. Betrifft insbesondere das Umfeld der Landau-Siegel-Nullstellen (doc-32), wo Ineffektivitaet historisch die zentrale Huerde ist, und die explizite Front (doc-49, doc-54), deren gesamter Zweck darin besteht, Konstanten effektiv zu machen. Aus der unabhaengigen Klassifikation in PR#5 uebernommen (dort F12); in dieser Taxonomie fehlte er.

## Diagnosefrage

**Sind alle Konstanten explizit und gleichmäßig in T und im Führer q?**

## Fluchtbedingung

Alle Konstanten explizit angeben und Gleichmaessigkeit in T und im Fuehrer q nachweisen. Genau das leistet das ANTEDB-Programm (doc-54).

## Betroffene Ansätze (3)

- [[32_Landau_Siegel_zeros_Zhang]]
- [[49_live_analytic_frontier]]
- [[54_machine_assisted_number_theory_ANTEDB_Lean]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
