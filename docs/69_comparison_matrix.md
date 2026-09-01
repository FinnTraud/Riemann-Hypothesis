---
id: doc-69
number: 69
title: "Vergleichsmatrix der Ansätze: Achsen, Lesarten, Auswahlhilfe"
category: synthesis
status: meta
tags: [comparison, matrix, axes, decision-support, meta, synthesis]
source_file: 69_comparison_matrix.md
lang: de
---

# Vergleichsmatrix der RH-Ansätze

**Kategorie:** Meta / Synthese
**Typ:** Systematischer Vergleich aller profilierten Ansätze entlang fester Achsen
**Datenquelle:** `kb/graph/approaches.json` (kuratiert) — die Tabelle unten ist **generiert**
**Werkzeuge:** `python3 kb/compare.py compare doc-10 doc-31` · `bridge` · `list family=spectral` · MCP-Tools `compare_approaches`, `bridge_approaches`, `list_approaches`

## Warum Achsen statt Ranglisten?
Eine Rangliste („welcher Ansatz ist der beste?") wäre unehrlich: niemand weiß, welcher Weg trägt. Sinnvoll vergleichbar sind Ansätze nur **achsenweise** — und genau diese Achsen sind es, die im Gespräch sonst untergehen.

| Achse | Frage | Warum sie entscheidet |
|---|---|---|
| `family` | Spektral, analytisch, algebraisch-geometrisch, probabilistisch, physikalisch, Kriterium, rechnerisch | Bestimmt Werkzeugkasten und Fehlerprofil |
| `equivalence` | `equivalent` / `conditional` / `partial` / `model` / `none` | **Die wichtigste Achse.** Nur `equivalent` und `conditional` haben überhaupt einen Implikationspfeil zur RH |
| `euler_product` | `essential` / `partial` / `none` | `none` ⇒ Davenport–Heilbronn (`F1`) erledigt jeden Beweisanspruch (Dok. 35, 57) |
| `positivity` | `proves` / `assumes` / `must-prove` / `n/a` | `assumes` ⇒ zirkulär; `must-prove` markiert die lebenden Fronten (Dok. 14, 60) |
| `rigor` | `theorem` / `program` / `model` / `heuristic` / `refuted` | Trennt Bewiesenes von Erhofftem |
| `evidence` | Stärke der numerischen/strukturellen Evidenz | Evidenz ≠ Beweis (Dok. 35, 67) |
| `testable` | Wie gut experimentell prüfbar? | Entscheidet, woran man *heute* arbeiten kann (Dok. 51) |
| `formalizable` | Lean/mathlib-Chance für Teilresultate | Der einzige halluzinationsfreie Fortschrittspfad (Dok. 37, 54) |

## Die Matrix
*Automatisch erzeugt — `python3 kb/build_obsidian.py`. Änderungen bitte in `kb/graph/approaches.json`.*

<!-- AUTO:MATRIX START (kb/build_obsidian.py) -->
| Ansatz | Familie | Status | Implikation | Euler-Produkt | Positivität | Strenge | Testbar | Fehlermodi |
|---|---|---|---|---|---|---|---|---|
| [[18_Weil_conjectures_function_fields_Deligne|Weil-Vermutungen / RH über endlichen Körpern]] | alg.-geom. | proven | partial | essential | proves | theorem | low | `F10` |
| [[30_F1_field_one_element_arithmetic_site|Körper mit einem Element / arithmetic site]] | alg.-geom. | open | conditional | essential | must-prove | program | low | `F10` `F2` |
| [[31_Deninger_cohomology_foliated_dynamical|Deninger: Kohomologie gefolierter Räume]] | alg.-geom. | open | conditional | essential | must-prove | program | low | `F10` `F2` |
| [[59_Langlands_functoriality_automorphic|Langlands-Funktorialität]] | alg.-geom. | open | none | essential | n/a | program | low | `F10` |
| [[60_standard_conjectures_motives_positivity|Standardvermutungen / Motive]] | alg.-geom. | open | partial | essential | proves | theorem | low | `F10` |
| [[61_Arakelov_geometry_SpecZ_compactification|Arakelov-Geometrie / Spec ℤ]] | alg.-geom. | open | conditional | essential | proves | theorem | low | `F10` |
| [[03_Hardy_1914_infinitely_many_zeros|Hardy: unendlich viele Nullstellen auf der Geraden]] | analytisch | proven | partial | partial | n/a | theorem | medium | `F13` |
| [[04_Levinson_Conrey_positive_proportion|Levinson/Conrey: positiver Anteil (>41%)]] | analytisch | proven | partial | essential | n/a | theorem | medium | `F13` |
| [[12_zero_free_regions|Nullstellenfreie Regionen]] | analytisch | proven | partial | essential | n/a | theorem | high | `F13` `F12` |
| [[17_Lindelof_density_hypothesis|Lindelöf- & Dichte-Hypothese]] | analytisch | open | partial | essential | n/a | theorem | medium | `F13` |
| [[22_Guth_Maynard_2024|Guth-Maynard: Dichteschranke (2024)]] | analytisch | proven | partial | essential | n/a | theorem | medium | `F13` |
| [[23_de_Bruijn_Newman_constant_Polymath15|de-Bruijn-Newman-Konstante / Polymath15]] | analytisch | proven | conditional | essential | must-prove | theorem | high | `F9` |
| [[29_Jensen_Polya_Laguerre_Polya_GORZ|Jensen-Pólya / Laguerre-Pólya (GORZ)]] | analytisch | open | equivalent | partial | must-prove | theorem | high | `F11` `F13` |
| [[32_Landau_Siegel_zeros_Zhang|Landau-Siegel-Nullstellen (Zhang 2022)]] | analytisch | open | partial | essential | n/a | theorem | low | `F12` |
| [[46_Voronin_universality|Voronin-Universalität]] | analytisch | proven | none | essential | n/a | theorem | medium | `F7` |
| [[56_Turan_power_sums_partial_sums|Turán: Partialsummen von ζ]] | analytisch | refuted | conditional | none | n/a | refuted | high | `F9` `F1` |
| [[57_Beurling_generalized_primes|Beurling-Systeme (Obstruktion)]] | analytisch | proven | none | essential | n/a | theorem | medium | `F1` |
| [[24_computational_verification|Numerische Verifikation (Odlyzko, Platt)]] | rechner. | proven | none | partial | n/a | theorem | high | `F6` |
| [[37_formalization_lean_proof_assistants|Formalisierung in Lean/mathlib]] | rechner. | open | none | partial | n/a | theorem | high | `F15` |
| [[13_Nyman_Beurling_Baez_Duarte|Nyman-Beurling / Baez-Duarte]] | Kriterium | open | equivalent | partial | n/a | theorem | high | `F11` |
| [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|Li-Kriterium / Weil-Positivität]] | Kriterium | open | equivalent | essential | must-prove | theorem | high | `F2` `F11` |
| [[15_Robin_inequality|Robins Ungleichung (Teilersumme)]] | Kriterium | open | equivalent | partial | n/a | theorem | high | `F11` `F6` |
| [[16_Mertens_function_Riesz_criterion|Mertens-Funktion / Riesz-Kriterium]] | Kriterium | open | equivalent | essential | n/a | theorem | high | `F8` `F11` `F6` |
| [[20_de_Branges_Hilbert_spaces|de Branges: Hilberträume ganzer Funktionen]] | Kriterium | refuted | conditional | none | assumes | refuted | low | `F2` `F1` `F15` |
| [[55_Speiser_zeros_of_zeta_prime|Speiser: Nullstellen von ζ′]] | Kriterium | open | equivalent | partial | n/a | theorem | high | `F11` `F13` |
| [[66_Bagchi_strong_recurrence|Bagchi: starke Rekurrenz]] | Kriterium | open | equivalent | none | n/a | theorem | medium | `F7` `F11` |
| [[08_Berry_Keating_xp_model|Berry-Keating H = xp]] | physikal. | open | conditional | none | must-prove | heuristic | low | `F4` `F3` `F1` |
| [[09_Bender_Brody_Muller_2017_Hamiltonian|Bender-Brody-Müller PT-Hamiltonian]] | physikal. | refuted | conditional | none | assumes | refuted | low | `F3` `F4` `F1` |
| [[33_statistical_mechanics_Lee_Yang|Statistische Mechanik / Lee-Yang]] | physikal. | open | model | partial | must-prove | heuristic | medium | `F14` `F1` |
| [[06_Montgomery_pair_correlation_RMT|Montgomery-Paarkorrelation / GUE]] | probab. | proven | model | essential | n/a | theorem | high | `F14` `F13` |
| [[07_Keating_Snaith_moments|Keating-Snaith: Momente via CUE]] | probab. | open | model | essential | n/a | heuristic | high | `F14` |
| [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH / Alternative Hypothese]] | probab. | open | partial | essential | n/a | theorem | high | `F14` `F13` |
| [[58_Mobius_randomness_Chowla_Sarnak|Möbius-Zufälligkeit (Chowla/Sarnak)]] | probab. | open | none | essential | n/a | theorem | high | `F8` `F14` |
| [[63_hybrid_Euler_Hadamard_product|Hybrides Euler-Hadamard-Produkt]] | probab. | open | model | essential | n/a | theorem | high | `F14` |
| [[64_extreme_values_FHK_multiplicative_chaos|Extremwerte / FHK / multiplikatives Chaos]] | probab. | open | model | essential | n/a | theorem | high | `F14` |
| [[65_higher_correlations_Rudnick_Sarnak|Höhere Korrelationen (Rudnick-Sarnak)]] | probab. | proven | model | essential | n/a | theorem | high | `F14` `F13` |
| [[05_Hilbert_Polya_conjecture|Hilbert-Pólya: selbstadjungierter Operator]] | spektral | open | conditional | partial | must-prove | program | low | `F3` `F4` |
| [[10_Connes_noncommutative_geometry|Connes: NKG-Spurformel]] | spektral | open | conditional | essential | must-prove | program | low | `F2` `F10` |
| [[11_Connes_Moscovici_prolate_spheroidal|Connes-Moscovici: prolate Operatoren]] | spektral | open | partial | essential | must-prove | program | medium | `F9` `F2` |
| [[19_Selberg_trace_formula_zeta|Selberg-Spurformel / Selberg-Zeta]] | spektral | proven | partial | essential | proves | theorem | medium | `F10` |
| [[34_Bost_Connes_system|Bost-Connes-Quantenstatistik]] | spektral | open | model | essential | n/a | theorem | low | `F14` `F10` |
| [[44_Lapidus_fractal_strings_spectral_operator|Lapidus: fraktale Saiten / Spektraloperator]] | spektral | open | equivalent | partial | n/a | theorem | medium | `F11` `F9` |
| [[48_Meyer_Kurokawa_algebraic_programs|Meyer (Distributionen) / Kurokawa (absolute Zeta)]] | spektral | open | partial | essential | must-prove | program | low | `F3` `F10` |
| [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform (Connes-van Suijlekom)]] | spektral | open | conditional | essential | must-prove | theorem | high | `F9` `F2` |
| [[62_Tate_thesis_adelic_analysis|Tates These / adelische Analysis]] | spektral | proven | none | essential | n/a | theorem | low | `F1` |
<!-- AUTO:MATRIX END -->

## Sechs Lesarten der Matrix

### 1. Wer hat überhaupt einen Implikationspfeil?
Nur `equivalence ∈ {equivalent, conditional}`. Alles mit `model` oder `none` ist — wie gut auch immer — **kein Beweisweg** (`F14`). Das betrifft GUE (06), Keating–Snaith (07), Hybridprodukt (63), FHK (64), höhere Korrelationen (65), Bost–Connes (34), Lee–Yang (33), Möbius-Zufälligkeit (58), Langlands (59), Tate (62), Voronin (46).
```bash
python3 kb/compare.py list equivalence=conditional
```

### 2. Wer benutzt das Euler-Produkt nicht?
`euler_product = none`: Berry–Keating (08), Bender–Brody–Müller (09), de Branges (20), Turán (56), Bagchi (66). Vier davon sind **widerlegt oder selbstbezüglich** — die Achse ist damit empirisch die trennschärfste des ganzen Datensatzes.

### 3. Wo sitzt die Positivität?
- `proves` — Weil/Deligne (18), Selberg (19), Standardvermutungen (60), Arakelov (61): **dort ist bekannt, woher das Vorzeichen kommt** (Schnittform, Hodge-Index).
- `must-prove` — Connes (10, 52), Deninger (31), 𝔽₁ (30), Li/Weil (14), Jensen–Pólya (29), Hilbert–Pólya (05): **die lebenden Fronten**.
- `assumes` — de Branges (20), BBM (09): **zirkulär, deshalb gescheitert**.

### 4. Was ist heute tatsächlich bearbeitbar?
`testable = high` **und** `equivalence ≠ none`: Nyman–Beurling/`d_N` (13), Li-Koeffizienten (14), Robin (15), de-Bruijn–Newman (23), Jensen–Pólya (29), abgeschnittene Weil-Form (52), Speiser (55), Turán-Partialsummen als Lehrbeispiel (56). Das ist die realistische Projektliste für eine Zusammenarbeit (Dok. 51).

### 5. Was ist formalisierbar?
`formalizable = high`: Hardy (03), Robin (15), Speiser (55), Lean-Infrastruktur (37). Kandidaten für verifizierte, publizierbare Teilergebnisse (Dok. 37, 54).

### 6. Wer scheitert am gleichen Punkt?
Die Spalte „Fehlermodi" ist der eigentliche Verknüpfungsschlüssel. Beispiele:
```bash
python3 kb/compare.py bridge doc-52 doc-56   # F9: beide hängen am Grenzübergang
python3 kb/compare.py bridge doc-10 doc-31   # F2+F10: beide brauchen dieselbe Geometrie
python3 kb/compare.py bridge doc-13 doc-15   # F11: beide sind Äquivalenzen ohne neuen Zugriff
python3 kb/compare.py bridge doc-06 doc-63   # F14: beide sind Modelle, nicht Beweiswege
```
Vollständige Auswertung: Dok. 68.

## Drei Cluster, die die Matrix sichtbar macht
1. **Positivitäts-Cluster** (10, 14, 20, 29, 30, 31, 52, 60, 61) — alle brauchen dieselbe Aussage, in verschiedenen Sprachen. Ein Beweis der Weil-Positivität würde mehrere Programme gleichzeitig abschließen. **Das ist der größte Hebel im gesamten Feld.**
2. **Modell-Cluster** (06, 07, 39, 53, 63, 64, 65) — hervorragende Vorhersagekraft, kein Implikationspfeil. Wert: Konsistenztests und Falsifikationsversuche (Dok. 67).
3. **Kriterien-Cluster** (13, 14, 15, 16, 29, 44, 45, 55, 66) — bewiesene Äquivalenzen. Wert: Numerik und Formalisierung. Nur Speiser (55) hat historisch echten Fortschritt erzeugt.

## Grenzen
Die Achsenwerte sind **kuratierte Einschätzungen**, keine Sätze. Sie fassen zusammen, wie die Literatur den jeweiligen Stand beschreibt. Wer einen Wert für falsch hält, ändert ihn in `kb/graph/approaches.json` und begründet es dort — die Dokumente aktualisieren sich dann automatisch.

## Verwandte Dokumente
Dok. 41 (Was ein Beweis braucht) · Dok. 68 (Fehler-Anatomie) · Dok. 35 (Obstruktionen) · Dok. 51 (Kollaboration) · Dok. 70 (Netzwerk-Leitfaden)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *benutzt* (`uses`) → [[concept_failure-modes|Fehlermodi (Scheiterns-Taxonomie)]] — Verknüpft Ansätze über gemeinsame Fehlermodi.
- *verallgemeinert* (`generalizes`) → [[41_synthesis_what_a_proof_needs|41 — Synthese: Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]] — Achsenbasierter Vergleich statt Einzelbewertung.
- *ist Blaupause für* (`blueprint_for`) → [[51_collaboration_brief|51 — Kollaborations-Leitfaden: sinnvoll mit einer Fachperson an der RH arbeiten]] — Liefert die realistische Projektliste (testable=high).

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[68_failure_anatomy|68 — Anatomie des Scheiterns: Taxonomie der Fehlermodi F1–F15]] — Fehlermodi sind eine Spalte der Vergleichsmatrix.
- *benutzt* (`uses`) → [[70_obsidian_network_guide|70 — Obsidian-Netzwerk: Aufbau, Linktypen, Graph-Ansicht & Dataview]] — Erklärt, wie Vergleich und Matrix erzeugt werden.

**Thematisch benachbart (gemeinsame Tags):** [[68_failure_anatomy|Anatomie des Scheiterns: Taxonomie der Fehlermodi F1–F15]] · [[41_synthesis_what_a_proof_needs|Synthese: Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
