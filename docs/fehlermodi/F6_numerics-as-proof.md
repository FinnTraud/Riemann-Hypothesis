---
id: blk-finite-evidence
f_mode: F6
title: "F6 — Numerische Extrapolation"
type: blocker
tier: 3
tags: [blocker, fehlermodus, netzwerk]
lang: de
---

# F6 — Numerische Extrapolation

> [!note] Generiert aus `kb/graph/blockers.json` durch `python3 kb/obsidian.py`.
> Inhaltliche Änderungen dort vornehmen, nicht hier.

**Tier 3** · Blocker-ID `blk-finite-evidence`

> Aus endlicher Rechnung wird auf asymptotisches Verhalten geschlossen — die RH-Landschaft hat dafür berüchtigte Gegenbeispiele.

Kein Hindernis für einen Beweis, sondern eine Fehlerquelle bei der Bewertung von Evidenz. Die Mertens-Vermutung galt bis 10^14 und ist falsch. π(x) < Li(x) gilt für jedes berechenbare x und kehrt sich bei ~10^316 um. S(T) ist im Mittel klein, unter RH aber unbeschränkt. Numerik ist im RH-Kontext systematisch irreführend, weil die relevanten Effekte mit log log x skalieren. docs/65 vermisst diesen Blocker erstmals quantitativ: fuer vier Kriterien wird angegeben, bis zu welcher Hoehe numerische Evidenz ueberhaupt traegt -- bei dreien lautet die Antwort praktisch: gar nicht.

## Diagnosefrage

**Existiert ein Argument, das ohne die numerische Tabelle auskommt?**

## Fluchtbedingung

Nicht überwindbar, nur vermeidbar: Numerik darf Hypothesen erzeugen und widerlegen, aber nie stützen. Ein rigoroses Intervall-Zertifikat (doc-54) ist etwas anderes als eine Stichprobe.

## Abweichende Einstufung

Die unabhaengige Klassifikation aus PR#5 stuft diesen Modus als Tier 1 ein, diese hier als Tier 3. Beide Lesarten sind vertretbar; siehe docs/55, Abschnitt 'Wie robust ist die Tier-Einstufung?'.

## Maschinell prüfbar

Dieser Blocker ist als einziger als Test implementiert: `kb/counterexample.py` → `T5_rechts_von_1` (siehe [[60_counterexample_oracle]]).

## Betroffene Ansätze (8)

- [[06_Montgomery_pair_correlation_RMT]]
- [[16_Mertens_function_Riesz_criterion]]
- [[23_de_Bruijn_Newman_constant_Polymath15]]
- [[24_computational_verification]]
- [[35_obstructions_barriers]]
- [[39_Cramer_probabilistic_model]]
- [[61_negative_space_if_rh_is_false]]
- [[65_criterion_sensitivity]]

## Einordnung

- Vollständige Matrix: [[55_failure_taxonomy]]
- Autopsien konkreter Fälle: [[56_failure_autopsies]]
- Achsenvergleich der Ansätze: [[78_approach_comparison_matrix]]
