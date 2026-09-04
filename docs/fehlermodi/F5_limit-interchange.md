---
id: blk-limit-exchange
f_mode: F5
title: "F5 — Unerlaubte Vertauschung"
type: blocker
tier: 1
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F5 — Unerlaubte Vertauschung

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 1** · Blocker-ID `blk-limit-exchange`

> Bedingt konvergente Nullstellensummen, Konturen oder Doppelreihen werden frei umgeordnet.

Der haeufigste TECHNISCHE Fehler in fehlerhaften Beweisen; bislang nur als Fehlerform in docs/35 und docs/56 (Autopsie A6) gefuehrt, nicht als eigener Blocker. Sum_rho konvergiert nur bedingt und paarweise symmetrisch (rho <-> 1-conj(rho)); jede Umordnung aendert den Wert. Tier 1, weil der Fehler nachweisbar ist, sobald man ihn sucht -- er ist kein offenes Problem, sondern ein Rechenfehler.

## Diagnosefrage

**Ist jede Vertauschung durch dominierte Konvergenz / gleichmäßige Konvergenz gerechtfertigt?**

## Fluchtbedingung

Jede Vertauschung von Limes, Summe und Integral einzeln durch dominierte oder gleichmaessige Konvergenz rechtfertigen; die Paarung rho <-> 1-conj(rho) durchgaengig beibehalten.

## Betroffene Ansätze (3)

- [[02_Riemann_von_Mangoldt_formula_explicit_formula]]
- [[26_Nash_failed_attempt]]
- [[27_other_disputed_claimed_proofs]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
