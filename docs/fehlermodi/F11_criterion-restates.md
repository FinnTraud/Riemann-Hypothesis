---
id: blk-equivalence-trap
f_mode: F11
title: "F11 — Äquivalenz-Falle"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F11 — Äquivalenz-Falle

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-equivalence-trap`

> Ein Kriterium ist zur RH äquivalent und damit exakt gleich schwer — die Umformulierung erzeugt den Anschein von Fortschritt, ohne die Beweislast zu senken.

Der logisch elementarste und zugleich am häufigsten übersehene Blocker. 'RH ⟺ X' heißt: X ist genau so schwer wie die RH. Eine Sammlung äquivalenter Kriterien wächst deshalb, ohne dass sich die Distanz zum Beweis verringert. Der Wert solcher Kriterien liegt woanders — sie machen die RH in verschiedenen Sprachen (Arithmetik, Kombinatorik, Funktionalanalysis) angreifbar und erhöhen so die Chance, dass EINE dieser Sprachen eine unabhängige Struktur mitbringt. Aber ein neues Äquivalent ist per se kein Fortschritt. blk-positivity-circular ist der wichtigste Spezialfall; dieser Blocker ist die allgemeine Form.

## Diagnosefrage

**Kann man die neue Seite der Äquivalenz mit Methoden angreifen, die auf ζ nicht anwendbar wären?**

## Fluchtbedingung

Eine der beiden Richtungen muss in STRIKT SCHWÄCHERER Form unbedingt bewiesen werden, oder es muss eine quantitative Größe geben, die sich unabhängig von der RH bewegen lässt (Λ ≤ 0.22, Anteil > 41 %, d_N-Raten). Nur solche Bewegungen zählen als Fortschritt — siehe docs/58.

## Abweichende Einstufung

Die unabhaengige Klassifikation aus PR#5 stuft diesen Modus als Tier 3 ein, diese hier als Tier 2. Beide Lesarten sind vertretbar; siehe docs/55, Abschnitt 'Wie robust ist die Tier-Einstufung?'.

## Betroffene Ansätze (9)

- [[13_Nyman_Beurling_Baez_Duarte]]
- [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity]]
- [[15_Robin_inequality]]
- [[16_Mertens_function_Riesz_criterion]]
- [[29_Jensen_Polya_Laguerre_Polya_GORZ]]
- [[41_synthesis_what_a_proof_needs]]
- [[44_Lapidus_fractal_strings_spectral_operator]]
- [[45_further_equivalent_criteria]]
- [[65_criterion_sensitivity]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
