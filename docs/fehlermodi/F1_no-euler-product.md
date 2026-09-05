---
id: blk-euler-blindness
f_mode: F1
title: "F1 — Euler-Blindheit"
type: blocker
tier: 1
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F1 — Euler-Blindheit

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 1** · Blocker-ID `blk-euler-blindness`

> Das Argument benutzt nur Funktionalgleichung, Fortsetzung und Wachstum — es würde für Davenport–Heilbronn genauso gelten und ist damit falsch.

Die härteste bekannte Obstruktion, weil sie ein explizites GEGENBEISPIEL hat. Die Davenport–Heilbronn-Funktion hat Funktionalgleichung vom ζ-Typ, analytische Fortsetzung, reelle Dirichlet-Koeffizienten und ζ-artiges Wachstum — und Nullstellen abseits der kritischen Geraden. Jeder Beweis, der nur diese Eigenschaften nutzt, ist damit widerlegt, bevor man ihn liest. Dieser Blocker ist als einziger MASCHINELL PRÜFBAR: kb/counterexample.py lässt das Argument gegen DH laufen.

## Diagnosefrage

**Würde derselbe Beweis für die Davenport-Heilbronn-Funktion durchgehen?**

## Fluchtbedingung

Mindestens ein Beweisschritt muss eine Eigenschaft benutzen, die für Davenport–Heilbronn NACHWEISLICH FALSCH ist — praktisch immer: Multiplikativität der Koeffizienten / Euler-Produkt.

## Maschinell prüfbar

Dieser Blocker ist als einziger als Test implementiert: `kb/counterexample.py` → `T2_euler_produkt` (siehe [[60_counterexample_oracle]]).

## Betroffene Ansätze (7)

- [[25_Atiyah_2018_failed_proof]]
- [[27_other_disputed_claimed_proofs]]
- [[35_obstructions_barriers]]
- [[43_Epstein_zeta_Selberg_class_rigidity]]
- [[46_Voronin_universality]]
- [[67_Turan_power_sums_partial_sums]]
- [[73_Tate_thesis_adelic_analysis]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
