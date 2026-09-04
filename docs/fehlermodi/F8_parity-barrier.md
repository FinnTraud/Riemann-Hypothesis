---
id: blk-parity
f_mode: F8
title: "F8 — Paritätsbarriere"
type: blocker
tier: 1
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F8 — Paritätsbarriere

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 1** · Blocker-ID `blk-parity`

> Siebmethoden können gerade und ungerade Primfaktorzahl prinzipiell nicht trennen — genau das misst μ(n).

Selbergs Paritätsproblem ist ein bewiesenes Negativresultat über die Reichweite von Siebmethoden. Da 1/ζ(s) = Σ μ(n) n^{-s} und μ(n) = (−1)^{Ω(n)} genau die Parität misst, kann kein reines Siebargument die für M(x) nötige Kontrolle liefern. Tier 1, weil es dazu explizite Konstruktionen gibt (Siebgrenzen-Beispiele), nicht nur Erfahrungswerte.

## Diagnosefrage

**Beruht das Argument auf Sieben oder auf gemittelten Korrelationen? Dann kann es die Einzelsumme nicht erreichen.**

## Fluchtbedingung

Ein bilinearer Input (Typ-II-Summen), ein Spektralinput (automorphe Formen) oder eine andere Quelle von Kancellation, die nicht aus dem Sieb selbst kommt.

## Abweichende Einstufung

Die unabhaengige Klassifikation aus PR#5 stuft diesen Modus als Tier 3 ein, diese hier als Tier 1. Beide Lesarten sind vertretbar; siehe docs/55, Abschnitt 'Wie robust ist die Tier-Einstufung?'.

## Betroffene Ansätze (5)

- [[12_zero_free_regions]]
- [[16_Mertens_function_Riesz_criterion]]
- [[32_Landau_Siegel_zeros_Zhang]]
- [[35_obstructions_barriers]]
- [[69_Mobius_randomness_Chowla_Sarnak]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
