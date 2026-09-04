---
id: blk-limit-interchange
f_mode: F9
title: "F9 — Konvergenz- / Grenzübergangslücke"
type: blocker
tier: 2
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F9 — Konvergenz- / Grenzübergangslücke

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 2** · Blocker-ID `blk-limit-interchange`

> Für jede endliche Abschneidung bewiesen — der Grenzübergang ist offen.

Ein technisch eigener Blocker, der oft mit blk-positivity-circular verwechselt wird. Hier ist die Aussage für jeden Cutoff Λ (bzw. jedes N, jedes d) ein Satz; was fehlt, ist gleichmäßige Kontrolle beim Grenzübergang. Das ist qualitativ anders als eine bloße Äquivalenz: es gibt eine Folge bewiesener Aussagen, die auf das Ziel zuläuft, und die verbleibende Lücke ist eine Kompaktheits- bzw. Gleichmäßigkeitsaussage. Deshalb liefern Ansätze mit diesem Blocker die ehrlichsten Near-Miss-Kandidaten (siehe docs/58).

## Diagnosefrage

**Gibt es eine gleichmäßige, von N unabhängige Schranke - oder nur punktweise Resultate pro N?**

## Fluchtbedingung

Eine von Λ (bzw. N, d) UNABHÄNGIGE Schranke — Kompaktheit, gleichgradige Stetigkeit oder eine explizite Fehlerabschätzung, die den Grenzübergang erlaubt.

## Betroffene Ansätze (6)

- [[11_Connes_Moscovici_prolate_spheroidal]]
- [[13_Nyman_Beurling_Baez_Duarte]]
- [[29_Jensen_Polya_Laguerre_Polya_GORZ]]
- [[44_Lapidus_fractal_strings_spectral_operator]]
- [[52_Connes_truncated_Weil_spectral_realization]]
- [[67_Turan_power_sums_partial_sums]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
