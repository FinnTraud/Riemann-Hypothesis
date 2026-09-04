---
id: statusboard
title: "Statusboard"
category: index
status: reference
tags: [dashboard, dataview, overview]
lang: de
---

# Statusboard

> [!note] Erzeugt von `kb/obsidian.py` — nicht von Hand editieren.
> Die Dataview-Blöcke unten brauchen das Community-Plugin **Dataview**.
> Ist es nicht installiert, zeigt Obsidian den Code-Block als Text —
> deshalb steht darunter jeweils eine statische Tabelle mit denselben Daten.

## Nach Status (Dataview)

```dataview
TABLE status AS Status, category AS Kategorie, tags AS Tags
FROM "docs"
WHERE status != null
SORT status ASC, number ASC
```

## Offene Ansätze mit den meisten Blockern (Dataview)

```dataview
TABLE category AS Kategorie, status AS Status
FROM "docs"
WHERE status = "open"
SORT number ASC
```

## Alle Dokumente (statisch)

| Nr | Dokument | Kategorie | Status | Blocker |
|---|---|---|---|:-:|
| 01 | [[01_Riemann_1859_original_paper\|Riemanns Originalarbeit]] | `foundations` | `reference` | — |
| 02 | [[02_Riemann_von_Mangoldt_formula_explicit_formula\|Riemann–von-Mangoldt-Formel und die explizite…]] | `foundations` | `reference` | ● |
| 03 | [[03_Hardy_1914_infinitely_many_zeros\|Hardy]] | `partial-results` | `proven` | ● |
| 04 | [[04_Levinson_Conrey_positive_proportion\|Levinson, Conrey & Co.]] | `partial-results` | `proven` | ● |
| 05 | [[05_Hilbert_Polya_conjecture\|Die Hilbert–Pólya-Vermutung]] | `spectral` | `open` | ●● |
| 06 | [[06_Montgomery_pair_correlation_RMT\|Montgomery-Paarkorrelation & Random-Matrix-Th…]] | `spectral` | `open` | ●● |
| 07 | [[07_Keating_Snaith_moments\|Keating–Snaith]] | `spectral` | `open` | ●● |
| 08 | [[08_Berry_Keating_xp_model\|Berry–Keating H = xp Modell]] | `spectral` | `open` | ●● |
| 09 | [[09_Bender_Brody_Muller_2017_Hamiltonian\|Bender–Brody–Müller]] | `spectral` | `open` | ●● |
| 10 | [[10_Connes_noncommutative_geometry\|Alain Connes]] | `spectral` | `open` | ●● |
| 11 | [[11_Connes_Moscovici_prolate_spheroidal\|Connes–Moscovici]] | `spectral` | `open` | ●●● |
| 12 | [[12_zero_free_regions\|Nullstellenfreie Regionen]] | `analytic` | `open` | ● |
| 13 | [[13_Nyman_Beurling_Baez_Duarte\|Nyman–Beurling-Kriterium & Báez-Duarte-Versch…]] | `criterion` | `open` | ●●● |
| 14 | [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity\|Li-Kriterium, Bombieri–Lagarias & Weil-Positi…]] | `criterion` | `open` | ●● |
| 15 | [[15_Robin_inequality\|Robins Ungleichung & Lagarias' elementares Kr…]] | `criterion` | `open` | ● |
| 16 | [[16_Mertens_function_Riesz_criterion\|Mertens-Funktion & Riesz-Kriterium]] | `criterion` | `open` | ●●● |
| 17 | [[17_Lindelof_density_hypothesis\|Lindelöf-Hypothese & Dichte-Hypothese]] | `analytic` | `open` | ● |
| 18 | [[18_Weil_conjectures_function_fields_Deligne\|Weil-Vermutungen]] | `proven-analogue` | `proven` | ● |
| 19 | [[19_Selberg_trace_formula_zeta\|Selberg-Spurformel & Selberg-Zetafunktion]] | `proven-analogue` | `proven` | — |
| 20 | [[20_de_Branges_Hilbert_spaces\|Louis de Branges]] | `analytic` | `refuted` | ●● |
| 21 | [[21_GRH_Selberg_class_grand_RH\|Verallgemeinerte, Große Riemann-Vermutung & S…]] | `generalization` | `open` | — |
| 22 | [[22_Guth_Maynard_2024\|Guth–Maynard]] | `breakthrough` | `proven` | ● |
| 23 | [[23_de_Bruijn_Newman_constant_Polymath15\|De-Bruijn–Newman-Konstante]] | `breakthrough` | `open` | ●● |
| 24 | [[24_computational_verification\|Numerische Verifikation der Riemann-Vermutung]] | `numerical` | `reference` | ● |
| 25 | [[25_Atiyah_2018_failed_proof\|Michael Atiyah]] | `failed-proof` | `refuted` | ●●● |
| 26 | [[26_Nash_failed_attempt\|John Nash]] | `failed-proof` | `refuted` | ●● |
| 27 | [[27_other_disputed_claimed_proofs\|Weitere umstrittene, zurückgezogene & fehlerh…]] | `failed-proof` | `refuted` | ●●●● |
| 28 | [[28_AI_and_RH\|KI / Machine Learning und die Riemann-Vermutu…]] | `ai-context` | `meta` | — |
| 29 | [[29_Jensen_Polya_Laguerre_Polya_GORZ\|Jensen–Pólya-Programm]] | `solution-program` | `open` | ●●● |
| 30 | [[30_F1_field_one_element_arithmetic_site\|Der Körper mit einem Element]] | `solution-program` | `open` | ● |
| 31 | [[31_Deninger_cohomology_foliated_dynamical\|Deningers Kohomologie-Programm & dynamische S…]] | `solution-program` | `open` | ● |
| 32 | [[32_Landau_Siegel_zeros_Zhang\|Landau–Siegel-Nullstellen]] | `solution-program` | `open` | ●● |
| 33 | [[33_statistical_mechanics_Lee_Yang\|Statistische Mechanik & Lee–Yang-Analogie]] | `solution-program` | `open` | ●● |
| 34 | [[34_Bost_Connes_system\|Bost–Connes-System]] | `spectral` | `proven` | ● |
| 35 | [[35_obstructions_barriers\|Obstruktionen & Barrieren]] | `obstruction` | `meta` | ●●●● |
| 36 | [[36_consequences_of_RH\|Konsequenzen der Riemann-Vermutung]] | `context` | `reference` | — |
| 37 | [[37_formalization_lean_proof_assistants\|Formalisierung]] | `verification` | `reference` | ● |
| 38 | [[38_Bombieri_official_problem_statement\|Bombieris offizielle Clay-Problemstellung]] | `reference` | `reference` | — |
| 39 | [[39_Cramer_probabilistic_model\|Cramér-Modell & probabilistische Heuristiken…]] | `heuristic` | `open` | ●● |
| 41 | [[41_synthesis_what_a_proof_needs\|Synthese]] | `synthesis` | `meta` | ● |
| 42 | [[42_timeline_and_reading_list\|Zeittafel & kanonische Leseliste]] | `reference` | `reference` | — |
| 43 | [[43_Epstein_zeta_Selberg_class_rigidity\|Epstein-Zetafunktionen & Selberg-Klassen-Rigi…]] | `obstruction` | `meta` | ●● |
| 44 | [[44_Lapidus_fractal_strings_spectral_operator\|Lapidus]] | `solution-program` | `open` | ●● |
| 45 | [[45_further_equivalent_criteria\|Weitere äquivalente Kriterien]] | `criterion` | `open` | ●● |
| 46 | [[46_Voronin_universality\|Voronin-Universalität]] | `obstruction` | `meta` | ●● |
| 47 | [[47_physics_layer_primon_gas_quantum_graphs\|Physik-Schicht]] | `spectral` | `open` | ●● |
| 48 | [[48_Meyer_Kurokawa_algebraic_programs\|Weitere algebraische/spektrale Programme]] | `solution-program` | `open` | ● |
| 49 | [[49_live_analytic_frontier\|Live-Front der analytischen Zahlentheorie]] | `frontier` | `open` | ● |
| 50 | [[50_reasoning_protocol\|Denkprotokoll]] | `meta` | `meta` | — |
| 51 | [[51_collaboration_brief\|Kollaborations-Leitfaden]] | `meta` | `meta` | — |
| 52 | [[52_Connes_truncated_Weil_spectral_realization\|Abgeschnittene Weil-Quadratform & Zeta-Spektr…]] | `spectral` | `open` | ●● |
| 53 | [[53_pair_correlation_alternative_hypothesis\|Paarkorrelation ohne RH & die Alternative Hyp…]] | `partial-results` | `open` | ● |
| 54 | [[54_machine_assisted_number_theory_ANTEDB_Lean\|Maschinengestützte Zahlentheorie]] | `meta` | `reference` | ●● |
| 55 | [[55_failure_taxonomy\|Muster im Scheitern]] | `meta` | `meta` | — |
| 56 | [[56_failure_autopsies\|Fehler-Autopsien]] | `meta` | `meta` | — |
| 57 | [[57_untried_directions\|Noch nicht Versuchtes]] | `meta` | `open` | — |
| 58 | [[58_gap_registry_near_miss\|GAP-Registry & Near-Miss-Bewertung]] | `meta` | `meta` | — |
| 59 | [[59_invariants_test_vectors\|Invarianten & Testvektoren]] | `obstruction` | `meta` | — |
| 60 | [[60_counterexample_oracle\|Das Gegenbeispiel-Orakel]] | `verification` | `reference` | — |
| 61 | [[61_negative_space_if_rh_is_false\|Negativraum]] | `meta` | `open` | ● |
| 62 | [[62_ai_division_of_labour_self_audit\|KI-Arbeitsteilung & Selbstaudit dieser Wissen…]] | `ai-context` | `meta` | — |
| 63 | [[63_experiment_decision_value\|Entscheidungswert von Experimenten]] | `meta` | `meta` | — |
| 64 | [[64_trust_tiers_verification_levels\|Trust-Tiers]] | `meta` | `reference` | — |
| 65 | [[65_criterion_sensitivity\|Sensitivität der Kriterien]] | `verification` | `reference` | ●● |
| 66 | [[66_Speiser_zeros_of_zeta_prime\|Speisers Satz & die Nullstellen von ζ′]] | `criterion` | `proven` | ● |
| 67 | [[67_Turan_power_sums_partial_sums\|Turáns Potenzsummen-Programm & die Partialsum…]] | `failed-proof` | `refuted` | ●● |
| 68 | [[68_Beurling_generalized_primes\|Beurlingsche verallgemeinerte Primzahlen]] | `obstruction` | `proven` | — |
| 69 | [[69_Mobius_randomness_Chowla_Sarnak\|Möbius-Zufälligkeit]] | `solution-program` | `open` | ● |
| 70 | [[70_Langlands_functoriality_automorphic\|Langlands-Funktorialität & automorphe L-Funkt…]] | `solution-program` | `open` | — |
| 71 | [[71_standard_conjectures_motives_positivity\|Grothendiecks Standardvermutungen & Motive]] | `solution-program` | `open` | ●● |
| 72 | [[72_Arakelov_geometry_SpecZ_compactification\|Arakelov-Geometrie & die Kompaktifizierung vo…]] | `solution-program` | `open` | ● |
| 73 | [[73_Tate_thesis_adelic_analysis\|Tates These & adelische Analysis]] | `foundations` | `proven` | ● |
| 74 | [[74_hybrid_Euler_Hadamard_product\|Hybrides Euler–Hadamard-Produkt]] | `heuristic` | `open` | ● |
| 75 | [[75_extreme_values_FHK_multiplicative_chaos\|Extremwerte von ζ]] | `frontier` | `open` | ● |
| 76 | [[76_higher_correlations_Rudnick_Sarnak\|Höhere Korrelationen]] | `partial-results` | `proven` | ● |
| 77 | [[77_Bagchi_strong_recurrence\|Bagchis Satz]] | `criterion` | `proven` | ● |
| 78 | [[78_approach_comparison_matrix\|Vergleichsmatrix der Ansätze]] | `meta` | `meta` | — |

## Lücken nach Near-Miss-Score

Vollständige Bewertung und Rechenregel: [[58_gap_registry_near_miss]]

| Score | Lücke | Dokument |
|:-:|---|---|
| **6** | Grenzübergang der abgeschnittenen Weil-Quadratform | [[52_Connes_truncated_Weil_spectral_realization]] |
| **6** | Schließen der Lücke 0 ≤ Λ ≤ 0,22 | [[23_de_Bruijn_Newman_constant_Polymath15]] |
| **6** | Hyperbolizität der Jensen-Polynome im gemeinsamen Regime d ~ n | [[29_Jensen_Polya_Laguerre_Polya_GORZ]] |
| **3** | Von >41 % auf alle Nullstellen | [[04_Levinson_Conrey_positive_proportion]] |
| **3** | Von der Nullstellendichte zur Dichte-Hypothese | [[22_Guth_Maynard_2024]] |
| **3** | Ausschluss von Landau–Siegel-Nullstellen | [[32_Landau_Siegel_zeros_Zhang]] |
| **3** | Ausschluss der Alternativen Hypothese | [[53_pair_correlation_alternative_hypothesis]] |
| **3** | Unbedingte obere Schranke für d_N | [[13_Nyman_Beurling_Baez_Duarte]] |
| **2** | Invertierbarkeit des Spektraloperators außerhalb Re(s)=1/2 | [[44_Lapidus_fractal_strings_spectral_operator]] |
| **0** | Weil-Positivität unabhängig beweisen | [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity]] |
| **0** | Kanonische Konstruktion des Hilbert–Pólya-Operators | [[05_Hilbert_Polya_conjecture]] |
| **0** | Geometrie über Spec(ℤ) mit Positivität | [[30_F1_field_one_element_arithmetic_site]] |
| **0** | M(x) = O(x^{1/2+ε}) | [[16_Mertens_function_Riesz_criterion]] |
| **0** | Robins Ungleichung für alle n > 5040 | [[15_Robin_inequality]] |

## Claims nach Verifikationsstufe

Bedeutung der Stufen: [[64_trust_tiers_verification_levels]]

| Stufe | Anzahl |
|---|:-:|
| `T0-lean-verified` | 1 |
| `T1-kanonisch` | 46 |
| `T2-peer-reviewed` | 6 |
| `T3-preprint` | 9 |
| `T4-repo-numerik` | 5 |
| `T5-konsens` | 1 |

*68 Claims gesamt · 63 aus Sekundärdarstellungen erfasst (siehe [[62_ai_division_of_labour_self_audit]], Befund 1).*

## Karten

- [[Zeitachse_Motive.canvas|Zeitachse × Leitmotiv]] — wie sich die drei Leitmotive über 165 Jahre entwickelt haben
- [[Obstruktionskarte.canvas|Obstruktionskarte]] — welche Ansätze an welchem Blocker hängen
