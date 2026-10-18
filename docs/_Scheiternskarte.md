---
id: scheiternskarte
title: "Scheiternskarte — Reichweite & Blocker je Versuch"
status: reference
tags: [dashboard, netzwerk, scheitern]
lang: de
---

# Scheiternskarte

> [!note] Generiert von `python3 kb/failure_map.py` aus `kb/graph/`. Änderungen dort vornehmen.

Die Karte legt zwei Informationen auf das Netzwerk: **wie weit** ein Versuch gekommen ist (Farbe) und **woran** er hängt (Kante zum Blocker). Die Stufen beschreiben den erreichten Endstand, keine Rangliste des Werts (vgl. [[78_approach_comparison_matrix]]).

**Interaktiv:** `viz/scheiternskarte.html` im Browser öffnen. **Im Graph View:** die Farbgruppen unten sind in `.obsidian/graph.json` hinterlegt; die Tags `#reichweite/…` und `#scheitert-an/…` stehen in jedem Versuchsdokument.

## Legende

| Farbe | Reichweite | Regel | Versuche |
|---|---|---|---|
| <span style="color:#86b6ef">●</span> | `#reichweite/0-widerlegt` Widerlegt / zurückgezogen | Status oder Strenge `refuted`: die Beweisbehauptung bzw. das Modell ist nachweislich falsch. | 6 |
| <span style="color:#5598e7">●</span> | `#reichweite/1-heuristik` Heuristik | Strenge `heuristic`: Plausibilitätsargument, kein Satz. | 4 |
| <span style="color:#2a78d6">●</span> | `#reichweite/2-offen` Offenes Programm | Offen, ohne bewiesene Reduktion der RH: der Rahmen steht, der Kernschritt fehlt. | 17 |
| <span style="color:#1c5cab">●</span> | `#reichweite/3-umformulierung` Umformulierung bewiesen | Offen, aber `RH ⇔ X` bzw. `X ⇒ RH` ist ein Satz (Implikation `equivalent`/`conditional`). X ist so schwer wie die RH. | 11 |
| <span style="color:#104281">●</span> | `#reichweite/4-bewiesen` Teilresultat / Analogon bewiesen | Status `proven`: echter Satz, der nicht bis zur ganzen RH reicht (Teilaussage oder Analogon). | 13 |
| <span style="color:#eb6834">◆</span> | Blocker (`docs/fehlermodi/`) | Wiederkehrender Scheiterngrund F1–F15, siehe [[55_failure_taxonomy]] | 15 |

## Teilresultat / Analogon bewiesen (13)

| Versuch | scheitert an |
|---|---|
| [[03_Hardy_1914_infinitely_many_zeros\|Hardy: unendlich viele Nullstellen auf der Geraden]] | [[F13_error-term-ceiling\|F13]] |
| [[04_Levinson_Conrey_positive_proportion\|Levinson/Conrey: positiver Anteil (>41%)]] | [[F13_error-term-ceiling\|F13]] |
| [[06_Montgomery_pair_correlation_RMT\|Montgomery-Paarkorrelation / GUE]] | [[F6_numerics-as-proof\|F6]] · [[F13_error-term-ceiling\|F13]] · [[F14_model-without-implication\|F14]] |
| [[12_zero_free_regions\|Nullstellenfreie Regionen]] | [[F8_parity-barrier\|F8]] · [[F12_ineffective-nonuniform\|F12]] · [[F13_error-term-ceiling\|F13]] |
| [[18_Weil_conjectures_function_fields_Deligne\|Weil-Vermutungen / RH über endlichen Körpern]] | [[F10_analogy-transfer-gap\|F10]] |
| [[19_Selberg_trace_formula_zeta\|Selberg-Spurformel / Selberg-Zeta]] | [[F10_analogy-transfer-gap\|F10]] |
| [[22_Guth_Maynard_2024\|Guth-Maynard: Dichteschranke (2024)]] | [[F13_error-term-ceiling\|F13]] |
| [[23_de_Bruijn_Newman_constant_Polymath15\|de-Bruijn-Newman-Konstante / Polymath15]] | [[F2_positivity-assumed\|F2]] · [[F6_numerics-as-proof\|F6]] · [[F9_truncation-limit-gap\|F9]] |
| [[24_computational_verification\|Numerische Verifikation (Odlyzko, Platt)]] | [[F6_numerics-as-proof\|F6]] |
| [[46_Voronin_universality\|Voronin-Universalität]] | [[F1_no-euler-product\|F1]] · [[F7_soft-function-theory\|F7]] |
| [[68_Beurling_generalized_primes\|Beurling-Systeme (Obstruktion)]] | [[F1_no-euler-product\|F1]] |
| [[73_Tate_thesis_adelic_analysis\|Tates These / adelische Analysis]] | [[F1_no-euler-product\|F1]] |
| [[76_higher_correlations_Rudnick_Sarnak\|Höhere Korrelationen (Rudnick-Sarnak)]] | [[F13_error-term-ceiling\|F13]] · [[F14_model-without-implication\|F14]] |

## Umformulierung bewiesen (11)

| Versuch | scheitert an |
|---|---|
| [[13_Nyman_Beurling_Baez_Duarte\|Nyman-Beurling / Baez-Duarte]] | [[F2_positivity-assumed\|F2]] · [[F9_truncation-limit-gap\|F9]] · [[F11_criterion-restates\|F11]] |
| [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity\|Li-Kriterium / Weil-Positivität]] | [[F2_positivity-assumed\|F2]] · [[F11_criterion-restates\|F11]] |
| [[15_Robin_inequality\|Robins Ungleichung (Teilersumme)]] | [[F6_numerics-as-proof\|F6]] · [[F11_criterion-restates\|F11]] |
| [[16_Mertens_function_Riesz_criterion\|Mertens-Funktion / Riesz-Kriterium]] | [[F6_numerics-as-proof\|F6]] · [[F8_parity-barrier\|F8]] · [[F11_criterion-restates\|F11]] |
| [[29_Jensen_Polya_Laguerre_Polya_GORZ\|Jensen-Pólya / Laguerre-Pólya (GORZ)]] | [[F2_positivity-assumed\|F2]] · [[F9_truncation-limit-gap\|F9]] · [[F11_criterion-restates\|F11]] · [[F13_error-term-ceiling\|F13]] |
| [[44_Lapidus_fractal_strings_spectral_operator\|Lapidus: fraktale Saiten / Spektraloperator]] | [[F9_truncation-limit-gap\|F9]] · [[F11_criterion-restates\|F11]] |
| [[45_further_equivalent_criteria\|Weitere äquivalente Kriterien]] | [[F2_positivity-assumed\|F2]] · [[F11_criterion-restates\|F11]] |
| [[52_Connes_truncated_Weil_spectral_realization\|Abgeschnittene Weil-Quadratform (Connes-van Suijlekom)]] | [[F2_positivity-assumed\|F2]] · [[F9_truncation-limit-gap\|F9]] |
| [[66_Speiser_zeros_of_zeta_prime\|Speiser: Nullstellen von ζ′]] | [[F11_criterion-restates\|F11]] · [[F13_error-term-ceiling\|F13]] |
| [[72_Arakelov_geometry_SpecZ_compactification\|Arakelov-Geometrie / Spec ℤ]] | [[F10_analogy-transfer-gap\|F10]] |
| [[77_Bagchi_strong_recurrence\|Bagchi: starke Rekurrenz]] | [[F7_soft-function-theory\|F7]] · [[F11_criterion-restates\|F11]] |

## Offenes Programm (17)

| Versuch | scheitert an |
|---|---|
| [[05_Hilbert_Polya_conjecture\|Hilbert-Pólya: selbstadjungierter Operator]] | [[F3_non-canonical-operator\|F3]] · [[F4_no-selfadjoint-realization\|F4]] |
| [[10_Connes_noncommutative_geometry\|Connes: NKG-Spurformel]] | [[F2_positivity-assumed\|F2]] · [[F10_analogy-transfer-gap\|F10]] |
| [[11_Connes_Moscovici_prolate_spheroidal\|Connes-Moscovici: prolate Operatoren]] | [[F2_positivity-assumed\|F2]] · [[F3_non-canonical-operator\|F3]] · [[F4_no-selfadjoint-realization\|F4]] · [[F9_truncation-limit-gap\|F9]] |
| [[17_Lindelof_density_hypothesis\|Lindelöf- & Dichte-Hypothese]] | [[F13_error-term-ceiling\|F13]] |
| [[30_F1_field_one_element_arithmetic_site\|Körper mit einem Element / arithmetic site]] | [[F2_positivity-assumed\|F2]] · [[F10_analogy-transfer-gap\|F10]] |
| [[31_Deninger_cohomology_foliated_dynamical\|Deninger: Kohomologie gefolierter Räume]] | [[F2_positivity-assumed\|F2]] · [[F10_analogy-transfer-gap\|F10]] |
| [[32_Landau_Siegel_zeros_Zhang\|Landau-Siegel-Nullstellen (Zhang 2022)]] | [[F8_parity-barrier\|F8]] · [[F12_ineffective-nonuniform\|F12]] |
| [[34_Bost_Connes_system\|Bost-Connes-Quantenstatistik]] | [[F10_analogy-transfer-gap\|F10]] · [[F14_model-without-implication\|F14]] |
| [[37_formalization_lean_proof_assistants\|Formalisierung in Lean/mathlib]] | [[F15_verification-collapse\|F15]] |
| [[47_physics_layer_primon_gas_quantum_graphs\|Physik-Schicht]] | [[F3_non-canonical-operator\|F3]] · [[F4_no-selfadjoint-realization\|F4]] |
| [[48_Meyer_Kurokawa_algebraic_programs\|Meyer (Distributionen) / Kurokawa (absolute Zeta)]] | [[F3_non-canonical-operator\|F3]] · [[F10_analogy-transfer-gap\|F10]] |
| [[53_pair_correlation_alternative_hypothesis\|Paarkorrelation ohne RH / Alternative Hypothese]] | [[F13_error-term-ceiling\|F13]] · [[F14_model-without-implication\|F14]] |
| [[69_Mobius_randomness_Chowla_Sarnak\|Möbius-Zufälligkeit (Chowla/Sarnak)]] | [[F8_parity-barrier\|F8]] · [[F14_model-without-implication\|F14]] |
| [[70_Langlands_functoriality_automorphic\|Langlands-Funktorialität]] | [[F10_analogy-transfer-gap\|F10]] |
| [[71_standard_conjectures_motives_positivity\|Standardvermutungen / Motive]] | [[F2_positivity-assumed\|F2]] · [[F10_analogy-transfer-gap\|F10]] |
| [[74_hybrid_Euler_Hadamard_product\|Hybrides Euler-Hadamard-Produkt]] | [[F14_model-without-implication\|F14]] |
| [[75_extreme_values_FHK_multiplicative_chaos\|Extremwerte / FHK / multiplikatives Chaos]] | [[F14_model-without-implication\|F14]] |

## Heuristik (4)

| Versuch | scheitert an |
|---|---|
| [[07_Keating_Snaith_moments\|Keating-Snaith: Momente via CUE]] | [[F13_error-term-ceiling\|F13]] · [[F14_model-without-implication\|F14]] |
| [[08_Berry_Keating_xp_model\|Berry-Keating H = xp]] | [[F1_no-euler-product\|F1]] · [[F3_non-canonical-operator\|F3]] · [[F4_no-selfadjoint-realization\|F4]] |
| [[33_statistical_mechanics_Lee_Yang\|Statistische Mechanik / Lee-Yang]] | [[F1_no-euler-product\|F1]] · [[F2_positivity-assumed\|F2]] · [[F14_model-without-implication\|F14]] |
| [[39_Cramer_probabilistic_model\|Cramér-Modell & probabilistische Heuristiken der Primzahlen]] | [[F6_numerics-as-proof\|F6]] · [[F14_model-without-implication\|F14]] |

## Widerlegt / zurückgezogen (6)

| Versuch | scheitert an |
|---|---|
| [[09_Bender_Brody_Muller_2017_Hamiltonian\|Bender-Brody-Müller PT-Hamiltonian]] | [[F1_no-euler-product\|F1]] · [[F3_non-canonical-operator\|F3]] · [[F4_no-selfadjoint-realization\|F4]] |
| [[20_de_Branges_Hilbert_spaces\|de Branges: Hilberträume ganzer Funktionen]] | [[F1_no-euler-product\|F1]] · [[F2_positivity-assumed\|F2]] · [[F15_verification-collapse\|F15]] |
| [[25_Atiyah_2018_failed_proof\|Michael Atiyah]] | [[F1_no-euler-product\|F1]] · [[F2_positivity-assumed\|F2]] · [[F15_verification-collapse\|F15]] |
| [[26_Nash_failed_attempt\|John Nash]] | [[F5_limit-interchange\|F5]] · [[F15_verification-collapse\|F15]] |
| [[27_other_disputed_claimed_proofs\|Weitere umstrittene, zurückgezogene & fehlerhafte Beweisbeh…]] | [[F1_no-euler-product\|F1]] · [[F5_limit-interchange\|F5]] · [[F7_soft-function-theory\|F7]] · [[F15_verification-collapse\|F15]] |
| [[67_Turan_power_sums_partial_sums\|Turán: Partialsummen von ζ]] | [[F1_no-euler-product\|F1]] · [[F9_truncation-limit-gap\|F9]] |

## Blocker nach Häufigkeit

| Blocker | Tier | Versuche |
|---|---|---|
| [[F2_positivity-assumed\|F2 Zirkuläre Positivität]] | 2 | 14 |
| [[F13_error-term-ceiling\|F13 Anteils-Decke der Mollifier-Methoden]] | 2 | 11 |
| [[F1_no-euler-product\|F1 Euler-Blindheit]] | 1 | 10 |
| [[F10_analogy-transfer-gap\|F10 Fehlende Geometrie über Spec(ℤ)]] | 2 | 10 |
| [[F14_model-without-implication\|F14 Zirkularität der Modellannahme]] | 3 | 10 |
| [[F11_criterion-restates\|F11 Äquivalenz-Falle]] | 2 | 9 |
| [[F9_truncation-limit-gap\|F9 Konvergenz- / Grenzübergangslücke]] | 2 | 7 |
| [[F3_non-canonical-operator\|F3 Nicht-kanonischer Operator]] | 2 | 6 |
| [[F6_numerics-as-proof\|F6 Numerische Extrapolation]] | 3 | 6 |
| [[F4_no-selfadjoint-realization\|F4 Fehlende selbstadjungierte Realisierung]] | 2 | 5 |
| [[F15_verification-collapse\|F15 Nicht-Verifizierbarkeit]] | 3 | 5 |
| [[F8_parity-barrier\|F8 Paritätsbarriere]] | 1 | 4 |
| [[F7_soft-function-theory\|F7 Weichheitsbarriere (Voronin)]] | 1 | 3 |
| [[F5_limit-interchange\|F5 Unerlaubte Vertauschung]] | 1 | 2 |
| [[F12_ineffective-nonuniform\|F12 Ineffektive oder nicht gleichmaessige Konstanten]] | 2 | 2 |
