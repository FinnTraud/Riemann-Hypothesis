---
id: doc-78
number: 78
title: "Vergleichsmatrix der Ansätze: Achsen statt Ranglisten"
category: meta
status: meta
tags: [comparison, axes, matrix, selection, approaches]
source_file: 78_approach_comparison_matrix.md
lang: de
---

# Vergleichsmatrix der Ansätze: Achsen statt Ranglisten

**Kategorie:** Meta / Auswahlhilfe
**Datenquelle:** `kb/graph/approaches.json` (45 Ansätze × 8 Achsen) · Werkzeuge: `python3 kb/compare.py`
**Verwandt:** `docs/55` (Blocker) · `docs/58` (Near-Miss) · `docs/41` (Leitmotive) · `docs/51` (Kollaboration)
**Herkunft:** aus PR #5 übernommen; Fehlermodus-Spalte auf die zusammengeführte Taxonomie umgestellt.

## Warum Achsen statt Ranglisten?

Eine Rangliste („welcher Ansatz ist der beste?") wäre unehrlich — niemand weiß,
welcher Weg trägt. Sinnvoll vergleichbar sind Ansätze nur **achsenweise**, und
genau diese Achsen gehen im Gespräch sonst unter.

| Achse | Werte | Warum sie entscheidet |
|---|---|---|
| `family` | spektral · analytisch · alg.-geometrisch · probabilistisch · physikalisch · Kriterium · rechnerisch | Bestimmt Werkzeugkasten und Fehlerprofil |
| `equivalence` | `equivalent` · `conditional` · `partial` · `model` · `none` | **Die wichtigste Achse.** Nur `equivalent` und `conditional` haben überhaupt einen Implikationspfeil zur RH |
| `euler_product` | `essential` · `partial` · `none` | `none` ⇒ Davenport–Heilbronn erledigt jeden Beweisanspruch (`docs/35`, `docs/60`, `docs/68`) |
| `positivity` | `proves` · `assumes` · `must-prove` · `n/a` | `assumes` ⇒ zirkulär; `must-prove` markiert die lebenden Fronten (`docs/14`, `docs/71`) |
| `rigor` | `theorem` · `program` · `model` · `heuristic` · `refuted` | Trennt Bewiesenes von Erhofftem |
| `evidence` | Stärke der numerischen/strukturellen Evidenz | Evidenz ≠ Beweis — wie stark genau, sagt `docs/65` |
| `testable` | Wie gut experimentell prüfbar? | Entscheidet, woran man *heute* arbeiten kann (`docs/51`, `docs/63`) |
| `formalizable` | Lean/mathlib-Chance für Teilresultate | Der einzige halluzinationsfreie Fortschrittspfad (`docs/37`, `docs/54`) |

## Die Matrix

<!-- COMPARE-MATRIX:BEGIN (generiert von kb/compare.py --write) -->

| Ansatz | Familie | Status | Implikation | Euler-Produkt | Positivität | Strenge | Testbar | Fehlermodi |
|---|---|---|---|---|---|---|---|---|
| [[18_Weil_conjectures_function_fields_Deligne|Weil-Vermutungen / RH über endlichen Körpern]] | alg.-geom. | proven | partial | essential | proves | theorem | low | `F10` |
| [[30_F1_field_one_element_arithmetic_site|Körper mit einem Element / arithmetic site]] | alg.-geom. | open | conditional | essential | must-prove | program | low | `F10` `F2` |
| [[31_Deninger_cohomology_foliated_dynamical|Deninger: Kohomologie gefolierter Räume]] | alg.-geom. | open | conditional | essential | must-prove | program | low | `F10` `F2` |
| [[70_Langlands_functoriality_automorphic|Langlands-Funktorialität]] | alg.-geom. | open | none | essential | n/a | program | low | `F10` |
| [[71_standard_conjectures_motives_positivity|Standardvermutungen / Motive]] | alg.-geom. | open | partial | essential | proves | theorem | low | `F10` |
| [[72_Arakelov_geometry_SpecZ_compactification|Arakelov-Geometrie / Spec ℤ]] | alg.-geom. | open | conditional | essential | proves | theorem | low | `F10` |
| [[03_Hardy_1914_infinitely_many_zeros|Hardy: unendlich viele Nullstellen auf der Geraden]] | analytisch | proven | partial | partial | n/a | theorem | medium | `F13` |
| [[04_Levinson_Conrey_positive_proportion|Levinson/Conrey: positiver Anteil (>41%)]] | analytisch | proven | partial | essential | n/a | theorem | medium | `F13` |
| [[12_zero_free_regions|Nullstellenfreie Regionen]] | analytisch | proven | partial | essential | n/a | theorem | high | `F13` `F12` |
| [[17_Lindelof_density_hypothesis|Lindelöf- & Dichte-Hypothese]] | analytisch | open | partial | essential | n/a | theorem | medium | `F13` |
| [[22_Guth_Maynard_2024|Guth-Maynard: Dichteschranke (2024)]] | analytisch | proven | partial | essential | n/a | theorem | medium | `F13` |
| [[23_de_Bruijn_Newman_constant_Polymath15|de-Bruijn-Newman-Konstante / Polymath15]] | analytisch | proven | conditional | essential | must-prove | theorem | high | `F9` |
| [[29_Jensen_Polya_Laguerre_Polya_GORZ|Jensen-Pólya / Laguerre-Pólya (GORZ)]] | analytisch | open | equivalent | partial | must-prove | theorem | high | `F11` `F13` |
| [[32_Landau_Siegel_zeros_Zhang|Landau-Siegel-Nullstellen (Zhang 2022)]] | analytisch | open | partial | essential | n/a | theorem | low | `F12` |
| [[46_Voronin_universality|Voronin-Universalität]] | analytisch | proven | none | essential | n/a | theorem | medium | `F7` |
| [[67_Turan_power_sums_partial_sums|Turán: Partialsummen von ζ]] | analytisch | refuted | conditional | none | n/a | refuted | high | `F9` `F1` |
| [[68_Beurling_generalized_primes|Beurling-Systeme (Obstruktion)]] | analytisch | proven | none | essential | n/a | theorem | medium | `F1` |
| [[24_computational_verification|Numerische Verifikation (Odlyzko, Platt)]] | rechner. | proven | none | partial | n/a | theorem | high | `F6` |
| [[37_formalization_lean_proof_assistants|Formalisierung in Lean/mathlib]] | rechner. | open | none | partial | n/a | theorem | high | `F15` |
| [[13_Nyman_Beurling_Baez_Duarte|Nyman-Beurling / Baez-Duarte]] | Kriterium | open | equivalent | partial | n/a | theorem | high | `F11` |
| [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|Li-Kriterium / Weil-Positivität]] | Kriterium | open | equivalent | essential | must-prove | theorem | high | `F2` `F11` |
| [[15_Robin_inequality|Robins Ungleichung (Teilersumme)]] | Kriterium | open | equivalent | partial | n/a | theorem | high | `F11` `F6` |
| [[16_Mertens_function_Riesz_criterion|Mertens-Funktion / Riesz-Kriterium]] | Kriterium | open | equivalent | essential | n/a | theorem | high | `F8` `F11` `F6` |
| [[20_de_Branges_Hilbert_spaces|de Branges: Hilberträume ganzer Funktionen]] | Kriterium | refuted | conditional | none | assumes | refuted | low | `F2` `F1` `F15` |
| [[66_Speiser_zeros_of_zeta_prime|Speiser: Nullstellen von ζ′]] | Kriterium | open | equivalent | partial | n/a | theorem | high | `F11` `F13` |
| [[77_Bagchi_strong_recurrence|Bagchi: starke Rekurrenz]] | Kriterium | open | equivalent | none | n/a | theorem | medium | `F7` `F11` |
| [[08_Berry_Keating_xp_model|Berry-Keating H = xp]] | physikal. | open | conditional | none | must-prove | heuristic | low | `F4` `F3` `F1` |
| [[09_Bender_Brody_Muller_2017_Hamiltonian|Bender-Brody-Müller PT-Hamiltonian]] | physikal. | refuted | conditional | none | assumes | refuted | low | `F3` `F4` `F1` |
| [[33_statistical_mechanics_Lee_Yang|Statistische Mechanik / Lee-Yang]] | physikal. | open | model | partial | must-prove | heuristic | medium | `F14` `F1` |
| [[06_Montgomery_pair_correlation_RMT|Montgomery-Paarkorrelation / GUE]] | probab. | proven | model | essential | n/a | theorem | high | `F14` `F13` |
| [[07_Keating_Snaith_moments|Keating-Snaith: Momente via CUE]] | probab. | open | model | essential | n/a | heuristic | high | `F14` |
| [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH / Alternative Hypothese]] | probab. | open | partial | essential | n/a | theorem | high | `F14` `F13` |
| [[69_Mobius_randomness_Chowla_Sarnak|Möbius-Zufälligkeit (Chowla/Sarnak)]] | probab. | open | none | essential | n/a | theorem | high | `F8` `F14` |
| [[74_hybrid_Euler_Hadamard_product|Hybrides Euler-Hadamard-Produkt]] | probab. | open | model | essential | n/a | theorem | high | `F14` |
| [[75_extreme_values_FHK_multiplicative_chaos|Extremwerte / FHK / multiplikatives Chaos]] | probab. | open | model | essential | n/a | theorem | high | `F14` |
| [[76_higher_correlations_Rudnick_Sarnak|Höhere Korrelationen (Rudnick-Sarnak)]] | probab. | proven | model | essential | n/a | theorem | high | `F14` `F13` |
| [[05_Hilbert_Polya_conjecture|Hilbert-Pólya: selbstadjungierter Operator]] | spektral | open | conditional | partial | must-prove | program | low | `F3` `F4` |
| [[10_Connes_noncommutative_geometry|Connes: NKG-Spurformel]] | spektral | open | conditional | essential | must-prove | program | low | `F2` `F10` |
| [[11_Connes_Moscovici_prolate_spheroidal|Connes-Moscovici: prolate Operatoren]] | spektral | open | partial | essential | must-prove | program | medium | `F9` `F2` |
| [[19_Selberg_trace_formula_zeta|Selberg-Spurformel / Selberg-Zeta]] | spektral | proven | partial | essential | proves | theorem | medium | `F10` |
| [[34_Bost_Connes_system|Bost-Connes-Quantenstatistik]] | spektral | open | model | essential | n/a | theorem | low | `F14` `F10` |
| [[44_Lapidus_fractal_strings_spectral_operator|Lapidus: fraktale Saiten / Spektraloperator]] | spektral | open | equivalent | partial | n/a | theorem | medium | `F11` `F9` |
| [[48_Meyer_Kurokawa_algebraic_programs|Meyer (Distributionen) / Kurokawa (absolute Zeta)]] | spektral | open | partial | essential | must-prove | program | low | `F3` `F10` |
| [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform (Connes-van Suijlekom)]] | spektral | open | conditional | essential | must-prove | theorem | high | `F9` `F2` |
| [[73_Tate_thesis_adelic_analysis|Tates These / adelische Analysis]] | spektral | proven | none | essential | n/a | theorem | low | `F1` |

<!-- COMPARE-MATRIX:END -->

## Sechs Lesarten

### 1. Wer hat überhaupt einen Implikationspfeil?
Nur `equivalence ∈ {equivalent, conditional}`. Alles mit `model` oder `none` ist —
wie gut auch immer — **kein Beweisweg** (`blk-model-circularity` / `F14`). Das
betrifft GUE (`docs/06`), Keating–Snaith (`docs/07`), das Hybridprodukt
(`docs/74`), FHK (`docs/75`), höhere Korrelationen (`docs/76`), Bost–Connes
(`docs/34`), Lee–Yang (`docs/33`), Möbius-Zufälligkeit (`docs/69`), Langlands
(`docs/70`), Tate (`docs/73`), Voronin (`docs/46`).

```bash
python3 kb/compare.py list equivalence=conditional
```

### 2. Wer benutzt das Euler-Produkt nicht?
`euler_product = none`: Berry–Keating (`docs/08`), Bender–Brody–Müller
(`docs/09`), de Branges (`docs/20`), Turán (`docs/67`), Bagchi (`docs/77`).
**Vier davon sind widerlegt oder selbstbezüglich** — die Achse ist damit
empirisch die trennschärfste des ganzen Datensatzes. Genau das ist die These,
die `docs/60` maschinell prüfbar macht.

### 3. Wo sitzt die Positivität?
- `proves` — Weil/Deligne (`docs/18`), Selberg (`docs/19`), Standardvermutungen
  (`docs/71`), Arakelov (`docs/72`): **dort ist bekannt, woher das Vorzeichen
  kommt** (Schnittform, Hodge-Index).
- `must-prove` — Connes (`docs/10`, `docs/52`), Deninger (`docs/31`), 𝔽₁
  (`docs/30`), Li/Weil (`docs/14`), Jensen–Pólya (`docs/29`), Hilbert–Pólya
  (`docs/05`): **die lebenden Fronten**.
- `assumes` — de Branges (`docs/20`), BBM (`docs/09`): **zirkulär, deshalb
  gescheitert** (Autopsien A1 und A4 in `docs/56`).

### 4. Was ist heute tatsächlich bearbeitbar?
`testable = high` **und** `equivalence ≠ none`: d_N (`docs/13`), Li-Koeffizienten
(`docs/14`), Robin (`docs/15`), de-Bruijn–Newman (`docs/23`), Jensen–Pólya
(`docs/29`), abgeschnittene Weil-Form (`docs/52`), Speiser (`docs/66`), Turáns
Partialsummen als Lehrbeispiel (`docs/67`).

> **Einschränkung aus `docs/65`:** „bearbeitbar" heißt *rechenbar*, nicht
> *aussagekräftig*. Für d_N, Robin und die Li-Koeffizienten ist inzwischen
> gemessen, dass die Rechnung als RH-Evidenz nichts trägt. Diese Spalte ist
> eine Projektliste, keine Erkenntnisliste — und `docs/63` sagt, welches
> Projekt sich lohnt.

### 5. Was ist formalisierbar?
`formalizable = high`: Hardy (`docs/03`), Robin (`docs/15`), Speiser
(`docs/66`), Lean-Infrastruktur (`docs/37`). Kandidaten für verifizierte,
publizierbare Teilergebnisse — und die einzige Achse, auf der sich `docs/64`
(Trust-Tier T0) überhaupt bewegen lässt.

### 6. Wer scheitert am gleichen Punkt?
Die Fehlermodus-Spalte ist der eigentliche Verknüpfungsschlüssel:

```bash
python3 kb/compare.py bridge doc-52 doc-67   # F9  beide hängen am Grenzübergang
python3 kb/compare.py bridge doc-10 doc-31   # F2+F10  beide brauchen dieselbe Geometrie
python3 kb/compare.py bridge doc-13 doc-15   # F11 beide sind Äquivalenzen ohne neuen Zugriff
python3 kb/compare.py bridge doc-06 doc-74   # F14 beide sind Modelle, nicht Beweiswege
```

Vollständige Auswertung: `docs/55`.

## Drei Cluster

1. **Positivitäts-Cluster** — `docs/10`, `14`, `20`, `29`, `30`, `31`, `52`,
   `71`, `72`. Alle brauchen dieselbe Aussage, in verschiedenen Sprachen. Ein
   Beweis der Weil-Positivität schlösse mehrere Programme gleichzeitig ab.
   **Der größte Hebel im gesamten Feld.**
2. **Modell-Cluster** — `docs/06`, `07`, `39`, `53`, `74`, `75`, `76`.
   Hervorragende Vorhersagekraft, kein Implikationspfeil. Wert: Konsistenztests
   und Falsifikationsversuche (`docs/61`).
3. **Kriterien-Cluster** — `docs/13`, `14`, `15`, `16`, `29`, `44`, `45`, `66`,
   `77`. Bewiesene Äquivalenzen. Wert: Numerik und Formalisierung. **Nur
   Speiser (`docs/66`) hat historisch echten Fortschritt erzeugt** — er ist die
   Maschine hinter Levinsons Anteilsresultat.

### Eine unabhängige Bestätigung
Cluster 1 wurde hier aus den Achsenwerten von `approaches.json` abgelesen.
`docs/55` kommt über einen völlig anderen Weg — die Blocker-Zuordnung — zu
demselben Ergebnis: neun Ansätze hängen an `blk-positivity-circular`, und
`docs/58` gibt der zugehörigen Lücke `gap-weil-positivity` den niedrigsten
Near-Miss-Score bei zugleich größter Tragweite.

**Zwei unabhängig erstellte Datensätze, zwei verschiedene Methoden, dasselbe
Ergebnis.** Das ist der stärkste Hinweis dieser Wissensbasis darauf, dass die
Positivitätsfrage tatsächlich der Engpass ist — und kein Artefakt einer
bestimmten Klassifikation.

## Grenzen

Die Achsenwerte sind **kuratierte Einschätzungen, keine Sätze.** Sie fassen
zusammen, wie die Literatur den jeweiligen Stand beschreibt. Wer einen Wert für
falsch hält, ändert ihn in `kb/graph/approaches.json` und begründet es dort —
die Dokumente aktualisieren sich dann automatisch.

Nach `docs/64` sind diese Einschätzungen als `T1`–`T3` einzustufen, je nach
zugrunde liegender Arbeit — die Achsenwerte selbst tragen **keine** eigene
Verifikationsstufe. Sie sind Navigation, nicht Aussage.

## Quellen
Keine eigenen mathematischen Behauptungen. Alle Achsenwerte fassen die in
`docs/01`–`docs/77` belegten Aussagen zusammen; Belege stehen jeweils dort.

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (6)
> - *ist Blaupause für* → [[51_collaboration_brief|51 · Kollaborations-Leitfaden]] — Liefert die Auswahlhilfe fuer realistische Teilprojekte.
> - *ist Evidenz für* → [[58_gap_registry_near_miss|58 · GAP-Registry & Near-Miss-Bewertung]] — Bestaetigt den Positivitaets-Engpass unabhaengig ueber die Achsenwerte.
> - *verallgemeinert* → [[41_synthesis_what_a_proof_needs|41 · Synthese]] — Erweitert die drei Leitmotive zu acht vergleichbaren Achsen ueber 45 Ansaetze.
> - *ist Instanz von* → **Fehlermodi (Scheiterns-Taxonomie)** — Ordnet jedem Ansatz seine Fehlermodi zu.
> - *benutzt* → [[55_failure_taxonomy|55 · Muster im Scheitern]] — Die Fehlermodus-Spalte verweist auf die zusammengefuehrte Blocker-Taxonomie.
> - ← *wird benutzt von* [[55_failure_taxonomy|55 · Muster im Scheitern]] — Die Matrix ordnet Ansaetze nach Achsen, die Blocker nach Huerden -- komplementaere Sichten.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
