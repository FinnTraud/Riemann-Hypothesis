---
id: doc-20
number: 20
title: "Louis de Branges: Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)"
category: analytic
status: refuted
tags: [de-branges, hilbert-spaces-entire-functions, conrey-li, failed]
source_file: 20_de_Branges_Hilbert_spaces.md
lang: de
---

# Louis de Branges: Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)

**Kategorie:** Analytischer Ansatz / prominenter gescheiterter Beweis
**Autor / Jahre:** Louis de Branges (Theorie ab ~1959; RH-Ansatz ab 1986; Beweisbehauptungen u. a. 2004, 2009, 2014, 2017)
**Typ:** Funktionalanalytischer Ansatz + wiederholt fehlerhafte Beweisbehauptungen
**Status:** ❌ Alle Beweisbehauptungen mit Lücken/Fehlern; Ansatz als solcher offen

## Zusammenfassung
Louis de Branges (berühmt für seinen *korrekten* Beweis der Bieberbach-Vermutung 1984) entwickelte eine umfangreiche Theorie der **Hilberträume ganzer Funktionen** und schlug ab 1986 einen darauf basierenden Zugang zur (verallgemeinerten) RH vor. Über Jahrzehnte veröffentlichte er mehrere **Beweisbehauptungen**, die jedoch alle als **lückenhaft oder fehlerhaft** befunden wurden. Es ist der prominenteste Fall eines technisch ernsthaften, vielfach überarbeiteten — aber nicht akzeptierten — RH-Beweisversuchs.

## Kernidee des Ansatzes
- De Branges' Theorie (Ende 1950er/1960er) verallgemeinert den Teil der Fourier-Analysis um Fourier-Transformation und Plancherel-Formel auf **Hilberträume, deren Elemente ganze Funktionen sind**.
- Wurzeln im Ansatz von **Stieltjes**, die RH zu beweisen; Übergang zu unendlich vielen Dimensionen über die **Hermite-Klasse** ganzer Funktionen (Grenzwerte von Polynomen mit nullstellenfreier Halbebene).
- **RH-Strategie (1986):** Eine **Positivitätsbedingung** auf bestimmten **gewichteten Hardy-Räumen** / Stieltjes-Räumen ganzer Funktionen ("Riemann-Hypothese für Hilberträume ganzer Funktionen") würde — angewandt auf den zur Euler-Zetafunktion gehörenden Raum — die (verallgemeinerte) RH implizieren. Die analytische Gewichtsfunktion darf in einer größeren Halbebene keine Nullstellen haben.

## Warum die Beweise scheiterten
- Mehrere veröffentlichte Versionen ("A Proof of the Riemann Hypothesis", Purdue-Preprints, u. a. 2004, 2009, 2014, 2017) wurden von der Fachwelt geprüft.
- **Typische Probleme:** Die geforderte Positivitätsbedingung wurde nicht wirklich etabliert; der konkret konstruierte Raum erfüllt die benötigten Axiome nicht; Gegenbeispiele (Conrey–Li, 2000) zeigten, dass die hinreichenden Bedingungen in der vorgeschlagenen Form für ζ **nicht** gelten, sodass der Ansatz in dieser Fassung die RH nicht liefern kann.
- **Conrey & Li (2000)** publizierten eine einflussreiche Kritik ("A note on some positivity conditions related to zeta and L-functions"), die zeigte, dass de Branges' Positivitätskriterien nicht auf die Zetafunktion anwendbar sind.

## Bedeutung / Einordnung
- Lehrbeispiel: Auch ein hochrangiger Mathematiker mit echtem früheren Großerfolg kann an der RH wiederholt scheitern — die Mathematik-Community verifiziert streng.
- Die zugrunde liegende **Theorie der Hilberträume ganzer Funktionen** ist eigenständig wertvoll und korrekt; nur die *Anwendung* auf die RH gelang nicht.
- Verwandt mit anderen Positivitäts-/Hilbertraum-Kriterien (Nyman–Beurling Dok. 13, Weil-Positivität Dok. 14).

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### de-Branges-Räume H(E)
Ausgangspunkt ist eine **Hermite–Biehler-Funktion** E(z): ganz, mit |E(z̄)| < |E(z)| für Im(z) > 0 (alle Nullstellen in der unteren Halbebene). Der zugehörige Raum:
```
H(E) = { f ganz : ‖f‖² = ∫_{−∞}^∞ |f(x)/E(x)|² dx < ∞,  und f/E, f*/E ∈ H²(obere Halbebene) }
```
H(E) ist ein **reproduzierender Kern-Hilbertraum** mit Kern
```
K(w, z) = ( E(z) E*(w̄) − E*(z) E(w̄) ) / ( 2πi (w̄ − z) ).
```

### Struktursatz & Schrumpfungsbedingung
De Branges' Strukturtheorie ordnet einer Kette ineinander geschachtelter Räume H(E_a) eine **Phasenfunktion** φ(x) zu (E(x) = |E(x)| e^{−iφ(x)}), mit φ'(x) > 0. Die Zugehörigkeit von Funktionen zu solchen Ketten wird durch Monotonie-/Positivitätsbedingungen geregelt.

### Anwendung auf ζ: die ξ-Funktion als E
Man möchte E so wählen, dass die zur ξ-Funktion gehörige Struktur entsteht. Schreibe ξ(1/2 + iz) als Funktion mit reellen Nullstellen (genau dann, wenn RH gilt). De Branges' **Positivitätskriterium** (vereinfacht): Wenn für die zugehörige Gewichtsfunktion W(z) (analytisch, nullstellenfrei in einer Halbebene) gilt
```
(de-Branges-Bedingung)   ∫ |f(x)|² / W(x) dx ≥ 0  bzw. die Phasen-Monotonie  φ'(x) ≥ 0
```
für alle f des Raumes, dann liegen die Nullstellen von ξ auf der reellen Achse ⇒ RH.

### Warum es für ζ scheitert — Conrey–Li (2000)
Conrey und Li zeigten **konkret**, dass die von de Branges geforderte Positivitäts-/Strukturbedingung für die Euler-ζ-Funktion **verletzt** ist: Sie konstruierten explizite Gegenbeispiele zu den hinreichenden Bedingungen, indem sie zeigten, dass eine gewisse, von de Branges als positiv-definit angenommene Funktion (im Zusammenhang mit der ζ zugeordneten E) bei numerischer/analytischer Prüfung **negative** Werte annimmt. Damit ist der Ansatz in der vorgeschlagenen Form nicht auf ζ anwendbar — die wiederholten Beweisversuche (2004–2017) umgehen diese Obstruktion nicht.

### Bezug zu anderen Positivitätskriterien
Die de-Branges-Bedingung ist eng verwandt mit Weil-Positivität (Dok. 14) und Nyman–Beurling (Dok. 13) — alle verlangen die Positivität einer quadratischen Form / Reellwurzeligkeit; alle stoßen an dieselbe ungelöste Kernhürde.

## Quellen
- [The Riemann hypothesis for Hilbert spaces of entire functions — de Branges (Purdue)](https://www.math.purdue.edu/~branges/riemann-hilbert.pdf)
- [A Proof of the Riemann Hypothesis — de Branges (2017 draft, Purdue)](https://www.math.purdue.edu/~branges/proof-riemann-2017-04.pdf)
- [The Strange Case of Louis de Branges — Karl Sabbagh, London Review of Books](https://www.lrb.co.uk/the-paper/v26/n14/karl-sabbagh/the-strange-case-of-louis-de-branges)
- [The early historical roots of Lee-Yang theorem (arXiv 1410.6450, Kontext Hermite-Klasse)](https://arxiv.org/pdf/1410.6450)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `criterion` |
> | Implikation | `conditional` |
> | Euler-Produkt | `none` |
> | Positivität | `assumes` |
> | Strenge | `refuted` |
> | Evidenz | `weak` |
> | Testbar | `low` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Die benutzte Positivitätsbedingung ist für ζ nachweislich verletzt (Conrey-Li-Gegenbeispiel).
> 
> **Hebel:** Der Apparat selbst ist korrekt und wertvoll - nur der RH-Schluss nicht.
> 
> **Fehlermodi:** [[F2_positivity-assumed|F2 Zirkuläre Positivität]] · [[F1_no-euler-product|F1 Euler-Blindheit]] · [[F15_verification-collapse|F15 Nicht-Verifizierbarkeit]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-20`

> [!warning]- Blocker — woran dieser Ansatz hängt (2)
> - **Zirkuläre Positivität** *(Tier 2)* — Die RH wird auf eine Positivitätsaussage reduziert, die selbst nur als äquivalent, nie unabhängig bewiesen ist.
>   *Fluchtbedingung:* Die Positivität muss aus einer Struktur folgen, die unabhängig von der Nullstellenlage definiert ist. Im bewiesenen Fall 𝔽_q (doc-18) leistet das die Schnittform auf der Fläche C×C — dort ist Positivität ein Satz der Geometrie, nicht eine Umformulierung des Ziels.
> - **Nicht-Verifizierbarkeit** *(Tier 3)* — Es existiert kein prüfbarer Beweistext — entweder gar keiner, oder einer, dessen Grundlage unpubliziert ist, oder einer, den niemand mehr nachprüft.
>   *Fluchtbedingung:* Ein vollständiger, öffentlicher, selbsttragender Beweistext — im Idealfall maschinengeprüft. Das ist die einzige Fluchtbedingung der Sammlung, die heute schon technisch erreichbar ist.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (2)
> - *ist Instanz von* → **Positivität / Reellwurzeligkeit** — de Branges: Positivitätsbedingung (für ζ widerlegt).
> - ← *wird benutzt von* [[56_failure_autopsies|56 · Fehler-Autopsien]] — Autopsie A1: Bruchstelle bei der Positivitaetsbedingung (Conrey-Li).

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
