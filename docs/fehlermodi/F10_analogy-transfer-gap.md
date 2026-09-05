---
id: blk-missing-base-geometry
f_mode: F10
title: "F10 — Fehlende Geometrie über Spec(ℤ)"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F10 — Fehlende Geometrie über Spec(ℤ)

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-missing-base-geometry`

> Der bewiesene Funktionenkörperfall braucht eine Fläche C×_𝔽 C; das Analogon Spec(ℤ)×_{𝔽₁}Spec(ℤ) existiert nicht.

Weil/Deligne beweisen die RH über 𝔽_q mit Geometrie: Kohomologie, Lefschetz-Fixpunktformel, Positivität der Schnittform auf einer Fläche über einer Basis. Über ℤ fehlt die Basis — es gibt kein Objekt, über dem Spec(ℤ) eine 'Kurve' wäre. Alle Transferprogramme (𝔽₁, Deninger, arithmetic site) arbeiten an genau diesem einen fehlenden Objekt.

## Diagnosefrage

**Welche Fläche, welcher Frobenius, welche Polarisierung? Wenn eines fehlt, ist das Argument leer.**

## Fluchtbedingung

Konstruktion einer Kohomologietheorie über Spec(ℤ) mit (a) Lefschetz-Formel, die die explizite Formel reproduziert, (b) Poincaré-Dualität, (c) einem Positivitäts-/Index-Satz (Hodge-Index-Analogon). Alle drei, nicht nur (a).

## Betroffene Ansätze (8)

- [[10_Connes_noncommutative_geometry]]
- [[18_Weil_conjectures_function_fields_Deligne]]
- [[30_F1_field_one_element_arithmetic_site]]
- [[31_Deninger_cohomology_foliated_dynamical]]
- [[34_Bost_Connes_system]]
- [[48_Meyer_Kurokawa_algebraic_programs]]
- [[71_standard_conjectures_motives_positivity]]
- [[72_Arakelov_geometry_SpecZ_compactification]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
