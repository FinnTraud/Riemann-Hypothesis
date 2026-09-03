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

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (7)
> - *ist Evidenz für* → **Euler-Produkt (Multiplikativität)** — Davenport–Heilbronn: ohne Euler-Produkt Off-Line-Nullstellen ⇒ Euler-Produkt nötig.
> - *ist Obstruktion für* → **Riemann-Vermutung (RH)** — Sammlung der Barrieren (Parität, Mertens/Skewes-Warnung).
> - ← *gestützt durch* [[16_Mertens_function_Riesz_criterion|16 · Mertens-Funktion & Riesz-Kriterium]] — Widerlegte Mertens-Vermutung: numerische Evidenz täuscht (Warnung).
> - ← *gestützt durch* [[39_Cramer_probabilistic_model|39 · Cramér-Modell & probabilistische Heuristiken der Pr…]] — Maier-Satz: probabilistisches Modell im Detail falsch (Warnung).
> - ← *wird benutzt von* [[55_failure_taxonomy|55 · Muster im Scheitern]] — Aggregiert die Obstruktionen zu einer Blocker-Taxonomie (Grund -> Ansaetze).
> - ← *wird benutzt von* [[59_invariants_test_vectors|59 · Invarianten & Testvektoren]] — Ergaenzt die Anti-Crackpot-Checkliste um die Ueberschuss-Pruefung.
> - ← *wird benutzt von* [[60_counterexample_oracle|60 · Das Gegenbeispiel-Orakel]] — Macht die Davenport-Heilbronn-Obstruktion maschinell pruefbar.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
