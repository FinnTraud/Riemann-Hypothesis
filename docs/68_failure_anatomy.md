---
id: doc-68
number: 68
title: "Anatomie des Scheiterns: Taxonomie der Fehlermodi F1–F15"
category: obstruction
status: meta
tags: [failure-modes, taxonomy, obstructions, anti-crackpot, diagnosis, meta]
source_file: 68_failure_anatomy.md
lang: de
---

# Anatomie des Scheiterns — woran RH-Ansätze tatsächlich scheitern

**Kategorie:** Meta / Diagnose-Schicht
**Typ:** Taxonomie mit 15 Fehlermodi, maschinenlesbar in `kb/graph/failure_modes.json`
**Status:** Meta — jede einzelne Aussage hier ist in den referenzierten Dokumenten belegt
**Werkzeuge:** `python3 kb/compare.py stats | mode F2 | diagnose "<Idee>"`; MCP-Tools `failure_statistics`, `failure_mode`, `diagnose_idea`

## Warum eine Taxonomie?
Dok. 35 sammelt die *Obstruktionen* (Sätze, die ganze Ansatzklassen ausschließen). Dieses Dokument ist die **Diagnose-Ebene darüber**: Es klassifiziert, an **welcher Stelle** ein Ansatz konkret bricht — und macht das quantitativ. Der Nutzen ist dreifach:

1. **Diagnose statt Meinung.** Statt „der Ansatz wirkt schwach" sagt man „`F9`: das abgeschnittene Modell ist bewiesen, der gleichmäßige Limes fehlt — wie bei Turán (Dok. 56), wo genau dieser Schritt beweisbar scheitert."
2. **Verknüpfung.** Zwei Ansätze mit demselben Fehlermodus hängen an **demselben** Problem. Ein Fortschritt dort wirkt auf beide. Zwei Ansätze mit disjunkten Modi sind **komplementär** — der eine kann als unabhängige Gegenprobe dienen.
3. **Priorisierung.** Die Häufigkeitsverteilung zeigt, wo die echten Engpässe der Forschung liegen (siehe Statistik unten).

## Die drei Tiers
| Tier | Bedeutung | Konsequenz |
|---|---|---|
| **1 — fatal** | Ein bekanntes Gegenbeispiel oder ein Beweisfehler erledigt die Idee sofort | Der Ansatz ist **falsch**, nicht nur unvollständig |
| **2 — blockierend** | Der Ansatz ist strukturell in Ordnung, aber ein präziser Kernschritt ist offen | Der Ansatz **lebt** — man weiß genau, was zu tun ist |
| **3 — strukturell** | Die Methode kann prinzipiell nicht mehr liefern als sie liefert | Der Ansatz ist **nützlich, aber kein Beweisweg** |

Ein häufiger Denkfehler ist, Tier 3 mit Tier 1 zu verwechseln: GUE-Statistik (Dok. 06) ist **kein Fehler** — sie ist exzellente Mathematik ohne Implikationspfeil. Und umgekehrt: Ein Tier-2-Ansatz wie Connes' Programm ist nicht „gescheitert", sondern **blockiert an einem benennbaren Satz**.

## Die 15 Fehlermodi

### Tier 1 — fatal
- **`F1` Euler-Produkt nicht wesentlich benutzt.** Davenport–Heilbronn (Dok. 35, 43): eine Dirichlet-Reihe mit Funktionalgleichung, Fortsetzung, unendlich vielen Nullstellen auf der Geraden **und** Nullstellen abseits davon. Wer sie nicht unterscheiden kann, hat keinen Beweis. Ergänzt durch Beurling-Systeme (Dok. 57): auch Euler-Produkt **allein** genügt nicht.
- **`F5` Unerlaubte Vertauschung.** Die Nullstellensumme der expliziten Formel konvergiert nur bedingt und paarweise symmetrisch. Der häufigste technische Fehler in falschen Beweisen (Dok. 27).
- **`F6` Endliche Numerik als Beweis.** Mertens-Vermutung (bis 10^14 „bestätigt", falsch), Skewes-Zahl ~10^316 (Dok. 16, 67).
- **`F7` Weiche Funktionentheorie.** Voronin-Universalität (Dok. 46): Was aus allgemeinen holomorphen Eigenschaften folgt, gilt für zu viele Funktionen. Bagchi (Dok. 66) ist die schärfste Formulierung davon.
- **`F15` Zusammenbruch in der Verifikation.** de Branges (Dok. 20), Atiyah (Dok. 25), diverse Preprints (Dok. 27). Signatur: zentrale Lemmas ohne Beweis, undefinierte Objekte, keine Vorab-Prüfung durch Fachleute.

### Tier 2 — blockierend (die interessantesten)
- **`F2` Positivität angenommen statt bewiesen.** Weil-/Li-/de-Branges-Positivität ist RH-äquivalent. Im **bewiesenen** Fall stammt sie aus dem Hodge-Index-Satz (Dok. 60) — also aus polarisierter Geometrie. Fehlt die Geometrie, ist die Positivität eine Annahme.
- **`F3` Operator ad hoc.** Zu jeder reellen Folge gibt es einen selbstadjungierten Operator mit dieser Folge als Spektrum. Hilbert–Pólya verlangt deshalb einen **kanonisch aus der Arithmetik** stammenden Operator (Dok. 05, 09).
- **`F4` Keine selbstadjungierte Realisierung.** `H = xp` ist formal symmetrisch, hat aber auf L²(ℝ) kontinuierliches Spektrum. Diskretheit entsteht erst durch eine Wahl (Randbedingungen, Abschneidung) — und die ist bisher nicht kanonisch (Dok. 08, 11, 47).
- **`F9` Abgeschnitten bewiesen, Limes offen.** Der methodisch wichtigste Modus der Gegenwart: Connes–van Suijlekom (Dok. 52) beweisen die Nullstellenlage **pro Cutoff**. Turán (Dok. 56) ist der Präzedenzfall, in dem der Limes nachweislich **nicht** vererbt — daher ist `F9` nicht nur eine Formalie.
- **`F10` Analogie ohne Trägerobjekt.** Weils Beweis lebt auf der Fläche C × C mit Frobenius und Schnittform. Über ℤ fehlen: zweite Dimension, Frobenius, Polarisierung (Dok. 18, 30, 31, 60, 61).
- **`F12` Ineffektive/nicht gleichmäßige Konstanten.** Siegels Satz, Landau–Siegel-Nullstellen (Dok. 32, 54).

### Tier 3 — strukturell
- **`F8` Paritätsbarriere.** Siebe sehen die Möbius-Parität nicht; gemittelte Korrelationsresultate (Chowla, Sarnak, Matomäki–Radziwiłł) erreichen die Einzelsummen-Schranke nicht (Dok. 58, 16).
- **`F11` Äquivalenz ohne neuen Zugriff.** Nyman–Beurling, Robin, Li, Riesz, Bagchi: bewiesen äquivalent, aber genauso schwer. **Ausnahme: Speiser** (Dok. 55) — daraus floss über Levinson echter quantitativer Fortschritt. Das ist der Maßstab: eine Äquivalenz ist nur wertvoll, wenn ihre neue Seite **andere Methoden** zulässt.
- **`F13` Strukturelle Decke des Fehlerterms.** Levinsons Methode ist bei ~41 % gedeckelt (Mollifier-Länge ↔ bekannte Momente), nicht „noch nicht optimiert" (Dok. 04, 55).
- **`F14` Modell ohne Implikationspfeil.** GUE, Cramér, hybrides Euler–Hadamard-Produkt, FHK: alle mit RH konsistent, keines erzwingt sie. Testfrage: *Was am Modell bräche, wenn eine Nullstelle abseits läge?* Antwort meist: nichts (Dok. 06, 39, 63, 64, 65).

## Statistik: woran scheitert es am häufigsten?
*Automatisch erzeugt aus `kb/graph/approaches.json` (45 profilierte Ansätze) — `python3 kb/compare.py stats`.*

<!-- AUTO:FEHLERKARTE START (kb/build_obsidian.py) -->
| # | Fehlermodus | Tier | betroffen | Anteil | Prüffrage |
|---|---|---|---|---|---|
| `F13` | Strukturelle Decke des Fehlerterms | 3 | 10 | 22.2 % | Welcher Mittelwertsatz begrenzt die Methode, und was wäre nötig, um 100 Prozent zu erreichen? |
| `F10` | Analogie ohne Trägerobjekt (Geometrie-Transfer) | 2 | 10 | 22.2 % | Welche Fläche, welcher Frobenius, welche Polarisierung? Wenn eines fehlt, ist das Argument leer. |
| `F14` | Modell ohne Implikationspfeil | 3 | 9 | 20.0 % | Was am Modell würde brechen, wenn eine Nullstelle abseits der Geraden läge? Wenn nichts: kein Beweisweg. |
| `F11` | Äquivalenz ohne neuen Zugriff | 3 | 8 | 17.8 % | Kann man die neue Seite der Äquivalenz mit Methoden angreifen, die auf ζ nicht anwendbar wären? |
| `F1` | Euler-Produkt nicht wesentlich benutzt | 1 | 7 | 15.6 % | Würde derselbe Beweis für die Davenport-Heilbronn-Funktion durchgehen? |
| `F2` | Positivität angenommen statt bewiesen | 2 | 7 | 15.6 % | Woher genau kommt das Vorzeichen? Gibt es eine polarisierte Geometrie, die es erzwingt? |
| `F9` | Abgeschnittenes Modell bewiesen, Limes offen | 2 | 5 | 11.1 % | Gibt es eine gleichmäßige, von N unabhängige Schranke - oder nur punktweise Resultate pro N? |
| `F3` | Operator ad hoc konstruiert (nicht kanonisch aus der Arithmetik) | 2 | 4 | 8.9 % | Wird die Realität des Spektrums benutzt, um die Selbstadjungiertheit zu begründen - oder umgekehrt? |
| `F4` | Keine rigorose selbstadjungierte Realisierung (Definitionsbereich fehlt) | 2 | 3 | 6.7 % | Auf welchem Hilbertraum, mit welchem Definitionsbereich, ist der Operator wesentlich selbstadjungiert und hat diskretes Spektrum? |
| `F6` | Endliche Numerik als Beweis behandelt | 1 | 3 | 6.7 % | Existiert ein Argument, das ohne die numerische Tabelle auskommt? |
| `F12` | Ineffektive oder nicht gleichmäßige Konstanten | 2 | 2 | 4.4 % | Sind alle Konstanten explizit und gleichmäßig in T und im Führer q? |
| `F8` | Paritätsbarriere (Sieb-/Multiplikativitätsmethoden) | 3 | 2 | 4.4 % | Beruht das Argument auf Sieben oder auf gemittelten Korrelationen? Dann kann es die Einzelsumme nicht erreichen. |
| `F15` | Zusammenbruch in der Verifikation | 1 | 2 | 4.4 % | Ist jeder Schritt maschinen- oder fachprüfbar? Gibt es ein Minimalbeispiel, an dem das Argument scheitern müsste, wenn es falsch wäre? |
| `F7` | Weiche Funktionentheorie (zu allgemein) | 1 | 2 | 4.4 % | Würde das Argument auch für Hurwitz-ζ mit transzendentem Parameter gelten? |

- **`F13` Strukturelle Decke des Fehlerterms** (10): [[03_Hardy_1914_infinitely_many_zeros|Hardy: unendlich viele Nullstellen auf der Geraden]], [[04_Levinson_Conrey_positive_proportion|Levinson/Conrey: positiver Anteil (>41%)]], [[06_Montgomery_pair_correlation_RMT|Montgomery-Paarkorrelation / GUE]], [[12_zero_free_regions|Nullstellenfreie Regionen]], [[17_Lindelof_density_hypothesis|Lindelöf- & Dichte-Hypothese]], [[22_Guth_Maynard_2024|Guth-Maynard: Dichteschranke (2024)]], [[29_Jensen_Polya_Laguerre_Polya_GORZ|Jensen-Pólya / Laguerre-Pólya (GORZ)]], [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH / Alternative Hypothese]], [[55_Speiser_zeros_of_zeta_prime|Speiser: Nullstellen von ζ′]], [[65_higher_correlations_Rudnick_Sarnak|Höhere Korrelationen (Rudnick-Sarnak)]]
- **`F10` Analogie ohne Trägerobjekt (Geometrie-Transfer)** (10): [[10_Connes_noncommutative_geometry|Connes: NKG-Spurformel]], [[18_Weil_conjectures_function_fields_Deligne|Weil-Vermutungen / RH über endlichen Körpern]], [[19_Selberg_trace_formula_zeta|Selberg-Spurformel / Selberg-Zeta]], [[30_F1_field_one_element_arithmetic_site|Körper mit einem Element / arithmetic site]], [[31_Deninger_cohomology_foliated_dynamical|Deninger: Kohomologie gefolierter Räume]], [[34_Bost_Connes_system|Bost-Connes-Quantenstatistik]], [[48_Meyer_Kurokawa_algebraic_programs|Meyer (Distributionen) / Kurokawa (absolute Zeta)]], [[59_Langlands_functoriality_automorphic|Langlands-Funktorialität]], [[60_standard_conjectures_motives_positivity|Standardvermutungen / Motive]], [[61_Arakelov_geometry_SpecZ_compactification|Arakelov-Geometrie / Spec ℤ]]
- **`F14` Modell ohne Implikationspfeil** (9): [[06_Montgomery_pair_correlation_RMT|Montgomery-Paarkorrelation / GUE]], [[07_Keating_Snaith_moments|Keating-Snaith: Momente via CUE]], [[33_statistical_mechanics_Lee_Yang|Statistische Mechanik / Lee-Yang]], [[34_Bost_Connes_system|Bost-Connes-Quantenstatistik]], [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH / Alternative Hypothese]], [[58_Mobius_randomness_Chowla_Sarnak|Möbius-Zufälligkeit (Chowla/Sarnak)]], [[63_hybrid_Euler_Hadamard_product|Hybrides Euler-Hadamard-Produkt]], [[64_extreme_values_FHK_multiplicative_chaos|Extremwerte / FHK / multiplikatives Chaos]], [[65_higher_correlations_Rudnick_Sarnak|Höhere Korrelationen (Rudnick-Sarnak)]]
- **`F11` Äquivalenz ohne neuen Zugriff** (8): [[13_Nyman_Beurling_Baez_Duarte|Nyman-Beurling / Baez-Duarte]], [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|Li-Kriterium / Weil-Positivität]], [[15_Robin_inequality|Robins Ungleichung (Teilersumme)]], [[16_Mertens_function_Riesz_criterion|Mertens-Funktion / Riesz-Kriterium]], [[29_Jensen_Polya_Laguerre_Polya_GORZ|Jensen-Pólya / Laguerre-Pólya (GORZ)]], [[44_Lapidus_fractal_strings_spectral_operator|Lapidus: fraktale Saiten / Spektraloperator]], [[55_Speiser_zeros_of_zeta_prime|Speiser: Nullstellen von ζ′]], [[66_Bagchi_strong_recurrence|Bagchi: starke Rekurrenz]]
- **`F1` Euler-Produkt nicht wesentlich benutzt** (7): [[08_Berry_Keating_xp_model|Berry-Keating H = xp]], [[09_Bender_Brody_Muller_2017_Hamiltonian|Bender-Brody-Müller PT-Hamiltonian]], [[20_de_Branges_Hilbert_spaces|de Branges: Hilberträume ganzer Funktionen]], [[33_statistical_mechanics_Lee_Yang|Statistische Mechanik / Lee-Yang]], [[56_Turan_power_sums_partial_sums|Turán: Partialsummen von ζ]], [[57_Beurling_generalized_primes|Beurling-Systeme (Obstruktion)]], [[62_Tate_thesis_adelic_analysis|Tates These / adelische Analysis]]
- **`F2` Positivität angenommen statt bewiesen** (7): [[10_Connes_noncommutative_geometry|Connes: NKG-Spurformel]], [[11_Connes_Moscovici_prolate_spheroidal|Connes-Moscovici: prolate Operatoren]], [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|Li-Kriterium / Weil-Positivität]], [[20_de_Branges_Hilbert_spaces|de Branges: Hilberträume ganzer Funktionen]], [[30_F1_field_one_element_arithmetic_site|Körper mit einem Element / arithmetic site]], [[31_Deninger_cohomology_foliated_dynamical|Deninger: Kohomologie gefolierter Räume]], [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform (Connes-van Suijlekom)]]
- **`F9` Abgeschnittenes Modell bewiesen, Limes offen** (5): [[11_Connes_Moscovici_prolate_spheroidal|Connes-Moscovici: prolate Operatoren]], [[23_de_Bruijn_Newman_constant_Polymath15|de-Bruijn-Newman-Konstante / Polymath15]], [[44_Lapidus_fractal_strings_spectral_operator|Lapidus: fraktale Saiten / Spektraloperator]], [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform (Connes-van Suijlekom)]], [[56_Turan_power_sums_partial_sums|Turán: Partialsummen von ζ]]
- **`F3` Operator ad hoc konstruiert (nicht kanonisch aus der Arithmetik)** (4): [[05_Hilbert_Polya_conjecture|Hilbert-Pólya: selbstadjungierter Operator]], [[08_Berry_Keating_xp_model|Berry-Keating H = xp]], [[09_Bender_Brody_Muller_2017_Hamiltonian|Bender-Brody-Müller PT-Hamiltonian]], [[48_Meyer_Kurokawa_algebraic_programs|Meyer (Distributionen) / Kurokawa (absolute Zeta)]]
- **`F4` Keine rigorose selbstadjungierte Realisierung (Definitionsbereich fehlt)** (3): [[05_Hilbert_Polya_conjecture|Hilbert-Pólya: selbstadjungierter Operator]], [[08_Berry_Keating_xp_model|Berry-Keating H = xp]], [[09_Bender_Brody_Muller_2017_Hamiltonian|Bender-Brody-Müller PT-Hamiltonian]]
- **`F6` Endliche Numerik als Beweis behandelt** (3): [[15_Robin_inequality|Robins Ungleichung (Teilersumme)]], [[16_Mertens_function_Riesz_criterion|Mertens-Funktion / Riesz-Kriterium]], [[24_computational_verification|Numerische Verifikation (Odlyzko, Platt)]]
- **`F12` Ineffektive oder nicht gleichmäßige Konstanten** (2): [[12_zero_free_regions|Nullstellenfreie Regionen]], [[32_Landau_Siegel_zeros_Zhang|Landau-Siegel-Nullstellen (Zhang 2022)]]
- **`F8` Paritätsbarriere (Sieb-/Multiplikativitätsmethoden)** (2): [[16_Mertens_function_Riesz_criterion|Mertens-Funktion / Riesz-Kriterium]], [[58_Mobius_randomness_Chowla_Sarnak|Möbius-Zufälligkeit (Chowla/Sarnak)]]
- **`F15` Zusammenbruch in der Verifikation** (2): [[20_de_Branges_Hilbert_spaces|de Branges: Hilberträume ganzer Funktionen]], [[37_formalization_lean_proof_assistants|Formalisierung in Lean/mathlib]]
- **`F7` Weiche Funktionentheorie (zu allgemein)** (2): [[46_Voronin_universality|Voronin-Universalität]], [[66_Bagchi_strong_recurrence|Bagchi: starke Rekurrenz]]
<!-- AUTO:FEHLERKARTE END -->

### Lesart der Statistik
- **`F10`, `F13`, `F14` dominieren** — und das sind gerade **keine** Fehler im Sinne von „falsch". Die RH-Forschung besteht überwiegend aus (a) exzellenten Modellen ohne Implikationspfeil, (b) Methoden an ihrer strukturellen Decke, (c) Analogien ohne Trägerobjekt. **Das ist die eigentliche Diagnose des Feldes.**
- **`F1` (7×) ist der Killer für neue Ideen von außen.** Fast jeder eingereichte „elementare Beweis" scheitert hier. Erste Prüffrage bleibt: *Würde das Argument für Davenport–Heilbronn durchgehen?*
- **Die Tier-2-Modi `F2`, `F9`, `F10` markieren die lebenden Fronten.** Wer heute etwas beitragen will, arbeitet dort — nicht an einer neuen Äquivalenz (`F11` ist gesättigt).

## Anwendung: Diagnose einer Beweisidee
```bash
python3 kb/compare.py diagnose "Ich konstruiere einen Operator, dessen Spektrum die Nullstellen sind"
python3 kb/compare.py mode F9          # wen trifft dieser Modus noch?
python3 kb/compare.py bridge doc-52 doc-56   # gemeinsame Blockade sichtbar machen
```
Der MCP-Server stellt dieselben Funktionen als Tools bereit (`diagnose_idea`, `failure_mode`, `failure_statistics`, `bridge_approaches`). Ergänzend bleibt `evaluate_proof_idea` (Dok. 35/41) als Checklisten-Gate.

## Grenzen dieser Taxonomie
- Die Zuordnung Ansatz → Fehlermodus ist **kuratiert**, nicht bewiesen; sie fasst die Einschätzung der Literatur zusammen. Änderungen gehören in `kb/graph/approaches.json`, nicht in diesen Text.
- `diagnose()` arbeitet mit Stichwort-Heuristik — sie ersetzt keine Prüfung, sie schlägt Prüffragen vor.
- Ein Ansatz ohne bekannten Fehlermodus ist **nicht** dadurch ein Beweis. Die Abwesenheit einer Diagnose ist keine Bestätigung.

## Quellen
Alle Einzelbelege stehen in den referenzierten Dokumenten; die zentralen sind Dok. 35 (Obstruktionen), 41 (Synthese), 43 (Selberg-Rigidität), 46 (Voronin), 56 (Turán), 57 (Beurling), 60 (Standardvermutungen), 67 (RH falsch?).

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *ist Instanz von* (`instance_of`) → [[concept_failure-modes|Fehlermodi (Scheiterns-Taxonomie)]] — Prosa-Ebene der Taxonomie F1–F15.
- *verallgemeinert* (`generalizes`) → [[35_obstructions_barriers|35 — Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN]] — Diagnose-Ebene über den Obstruktionen.
- *benutzt* (`uses`) → [[41_synthesis_what_a_proof_needs|41 — Synthese: Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]] — Ergänzt das Bewertungsraster um Fehlermodi.
- *benutzt* (`uses`) → [[69_comparison_matrix|69 — Vergleichsmatrix der Ansätze: Achsen, Lesarten, Auswahlhilfe]] — Fehlermodi sind eine Spalte der Vergleichsmatrix.

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[70_obsidian_network_guide|70 — Obsidian-Netzwerk: Aufbau, Linktypen, Graph-Ansicht & Dataview]] — Erklärt die Fehlermodus-Notizen im Graphen.

**Thematisch benachbart (gemeinsame Tags):** [[69_comparison_matrix|Vergleichsmatrix der Ansätze: Achsen, Lesarten, Auswahlhilfe]] · [[35_obstructions_barriers|Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
