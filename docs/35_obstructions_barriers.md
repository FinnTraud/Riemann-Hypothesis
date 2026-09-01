---
id: doc-35
number: 35
title: "Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN"
category: obstruction
status: meta
tags: [obstructions, davenport-heilbronn, parity-problem, mertens-warning, skewes, checklist]
source_file: 35_obstructions_barriers.md
lang: de
---

# Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN

**Kategorie:** Meta / Negativresultate (entscheidend für „bulletproof")
**Autoren / Jahre:** Davenport–Heilbronn (1936); Bombieri; Ivić („Reasons for doubting", 2003); diverse
**Typ:** Bekannte Hindernisse, die jeder Beweisversuch überwinden muss
**Status:** Etablierte Negativresultate / Warnschilder

## Zusammenfassung
Dieses Dokument sammelt die **bekannten Gründe, warum ganze Klassen von Beweisansätzen nicht funktionieren können**. Für einen RH-Assistenten ist das die wichtigste „Schutzschicht": Es erlaubt, vorgeschlagene Beweisideen sofort gegen bekannte Obstruktionen zu testen und Sackgassen zu erkennen.

## 1. Die Davenport–Heilbronn-Funktion — der „fast-ζ"-Gegenbeweis
**Fakt (Davenport–Heilbronn 1936).** Es gibt eine Dirichlet-Reihe f(s), die
- eine **Funktionalgleichung** vom ζ-Typ erfüllt (s ↔ 1−s),
- eine analytische Fortsetzung besitzt,
- **unendlich viele Nullstellen auf** der kritischen Geraden hat,
- aber **auch Nullstellen ABSEITS** der Geraden (sogar im Bereich Re(s) > 1) besitzt — das RH-Analogon ist also FALSCH.

### Konstruktion (Formel)
Mit einem nicht-prinzipalen Charakter mod 5 und einer Phase ξ wählt man
```
f(s) = (1 − i τ)/2 · L(s, χ) + (1 + i τ)/2 · L(s, χ̄),   τ = (√(10 − 2√5) − 2)/(√5 − 1),
```
eine Linearkombination zweier Dirichlet-L-Funktionen mit gemeinsamer Funktionalgleichung.

### Die entscheidende Lehre: Euler-Produkt ist unverzichtbar
f(s) hat **kein Euler-Produkt** (die Linearkombination zweier L-Funktionen ist nicht mehr multiplikativ). **Konsequenz:**
> Jeder RH-Beweis, der nur Funktionalgleichung + analytische Fortsetzung + Wachstumsverhalten benutzt, MUSS scheitern — denn f hätte dieselben Eigenschaften, verletzt aber die RH. Ein gültiger Beweis muss das **Euler-Produkt** (Multiplikativität / Primzahlstruktur) WESENTLICH verwenden.

Dies ist die schärfste bekannte Obstruktion. Sie disqualifiziert sofort viele „elementare" und rein funktionentheoretische Beweisversuche (vgl. Dok. 27).

## 2. Die Selberg-Klasse-Schranke
In der Selberg-Klasse (Dok. 21) wird die RH nur für Funktionen **mit Euler-Produkt** erwartet. Funktionen mit Grad 1 ohne Euler-Produkt (wie Davenport–Heilbronn) sind Gegenbeispiele. ⇒ Jeder Beweis muss zwischen „mit" und „ohne" Euler-Produkt unterscheiden können.

## 3. Das Paritätsproblem (Sieb-Methoden)
Klassische Siebmethoden (Brun, Selberg) können **prinzipiell** nicht zwischen Zahlen mit gerader und ungerader Anzahl von Primfaktoren unterscheiden (Paritätsbarriere, Selberg). Da die Möbius-Funktion μ(n) = (−1)^{Ω(n)} genau diese Parität misst und 1/ζ = Σ μ(n)/n^s, können reine Siebargumente die für die RH nötige Kontrolle über M(x) (Dok. 16) nicht liefern.

## 4. Gründe zum Zweifeln (Ivić 2003) — Vorsicht vor „zu schöner" Evidenz
- **Mertens-Vermutung widerlegt** (Dok. 16): |M(x)| < √x scheint bis 10^{14} zu gelten, ist aber falsch. Numerik täuscht.
- **Skewes-Zahl:** π(x) < Li(x) gilt für alle berechenbaren x, kehrt sich aber bei ~10^{316} um (Littlewood: unendlich oft beide Vorzeichen). ⇒ „Computergestützte Bestätigung bis 10^{N}" beweist nichts.
- **S(T)-Wachstum:** Der Argumentterm S(T) (Dok. 02) ist im Mittel klein, wird aber (unter RH) unbeschränkt — sehr hohe Nullstellen könnten unerwartetes Verhalten zeigen, das bei heutigen Höhen unsichtbar ist.
- Sehr nahe Nullstellenpaare (**Lehmer-Paare**, Dok. 23) zeigen, dass die RH (falls wahr) nur „knapp" gilt — keine komfortable Marge.

## 5. Warum spektrale Ansätze nicht „geschenkt" sind
- Ein Hilbert–Pólya-Operator (Dok. 05) muss **kanonisch aus der Arithmetik** kommen; ein ad-hoc-Operator mit Spektrum {γ_n} zu „erfinden" beweist nichts (man kann zu jeder reellen Folge einen selbstadjungierten Operator angeben — zirkulär, wenn man die Realität schon annimmt). Genau das ist die Lücke bei Bender–Brody–Müller (Dok. 09).
- Connes' Programm umgeht dies, indem die Positivität *unabhängig* gezeigt werden müsste — und genau das ist offen (Dok. 10).

## Checkliste für vorgeschlagene Beweise (Anti-Crackpot-Filter)
1. **Nutzt der Beweis das Euler-Produkt wesentlich?** Falls nein → fast sicher falsch (Davenport–Heilbronn).
2. **Würde dasselbe Argument für eine L-Funktion ohne Euler-Produkt gelten?** Falls ja → falsch.
3. **Wird Positivität (Li/Weil/de Branges) angenommen oder bewiesen?** Annahme → zirkulär (Dok. 14, 20).
4. **Beruht die Evidenz nur auf endlicher Numerik?** → kein Beweis (Mertens, Skewes).
5. **Vertauscht der Beweis Limes/Summe über die nicht absolut konvergente Nullstellensumme?** → Fehler (Dok. 27).

## Quellen
- [Zeros of the Davenport-Heilbronn Counterexample (AMS Math. Comp.)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)
- [On some reasons for doubting the Riemann hypothesis — A. Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- [On Davenport and Heilbronn-Type of Functions (arXiv 1602.06328)](https://arxiv.org/abs/1602.06328)
- [The Riemann Hypothesis — E. Bombieri (Clay official problem description)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *ist Evidenz für* (`evidence_for`) → [[concept_euler-product|Euler-Produkt (Multiplikativität)]] — Davenport–Heilbronn: ohne Euler-Produkt Off-Line-Nullstellen ⇒ Euler-Produkt nötig.
- *ist Obstruktion für* (`obstruction_for`) → [[concept_RH|Riemann-Vermutung (RH)]] — Sammlung der Barrieren (Parität, Mertens/Skewes-Warnung).

**Eingehende Beziehungen**
- *ist Evidenz für* (`evidence_for`) → [[16_Mertens_function_Riesz_criterion|16 — Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]] — Widerlegte Mertens-Vermutung: numerische Evidenz täuscht (Warnung).
- *ist Evidenz für* (`evidence_for`) → [[39_Cramer_probabilistic_model|39 — Cramér-Modell & probabilistische Heuristiken der Primzahlen]] — Maier-Satz: probabilistisches Modell im Detail falsch (Warnung).
- *widerlegt durch* (`refuted_by`) → [[56_Turan_power_sums_partial_sums|56 — Turáns Potenzsummen-Programm & die Partialsummen von ζ (widerlegter Ansatz)]] — Montgomery 1983: ζ_N hat Nullstellen rechts von Re=1 — Prämisse falsch.
- *verallgemeinert* (`generalizes`) → [[57_Beurling_generalized_primes|57 — Beurlingsche verallgemeinerte Primzahlen: Euler-Produkt allein genügt nicht]] — Zweite Säule neben Davenport–Heilbronn: auch Multiplikativität allein genügt nicht.
- *benutzt* (`uses`) → [[58_Mobius_randomness_Chowla_Sarnak|58 — Möbius-Zufälligkeit: Chowla-Vermutung, Sarnak-Disjunktheit & die Paritätsbarriere]] — Paritätsproblem (Selberg) als strukturelle Grenze.
- *ist Evidenz für* (`evidence_for`) → [[62_Tate_thesis_adelic_analysis|62 — Tates These & adelische Analysis: warum die Funktionalgleichung „billig\" ist]] — Erklärt begrifflich, warum die Funktionalgleichung allein nichts erzwingt.
- *ist Evidenz für* (`evidence_for`) → [[66_Bagchi_strong_recurrence|66 — Bagchis Satz: RH als starke Rekurrenz (Universalität als Kriterium)]] — Schärfste Formulierung, warum weiche Funktionentheorie nicht reicht.
- *verallgemeinert* (`generalizes`) → [[68_failure_anatomy|68 — Anatomie des Scheiterns: Taxonomie der Fehlermodi F1–F15]] — Diagnose-Ebene über den Obstruktionen.

**Thematisch benachbart (gemeinsame Tags):** [[68_failure_anatomy|Anatomie des Scheiterns: Taxonomie der Fehlermodi F1–F15]] · [[67_what_if_RH_is_false|Was wäre, wenn die RH falsch ist? Θ, Oszillationen & numerische Signaturen]] · [[43_Epstein_zeta_Selberg_class_rigidity|Epstein-Zetafunktionen & Selberg-Klassen-Rigidität: Welche Eigenschaft erzwingt die kritische Gerade?]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
