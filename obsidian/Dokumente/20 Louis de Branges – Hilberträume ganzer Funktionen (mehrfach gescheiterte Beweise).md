---
id: doc-20
title: "Louis de Branges: Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)"
nummer: "20"
kategorie: Analytische Ansätze
status: WIDERLEGT
typ: dokument
aliases:
  - "doc-20"
  - "Dok. 20"
tags:
  - "dokument"
  - "kategorie/analytic"
  - "status/refuted"
  - "thema/conrey-li"
  - "thema/de-branges"
  - "thema/failed"
  - "thema/hilbert-spaces-entire-functions"
quelle: docs/20_de_Branges_Hilbert_spaces.md
---

> [!info] Navigation
> **Karte:** [[MOC F – de Branges]] · **Kategorie:** Analytische Ansätze · **Status:** `WIDERLEGT`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/20_de_Branges_Hilbert_spaces.md`

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
- Verwandt mit anderen Positivitäts-/Hilbertraum-Kriterien (Nyman–Beurling Dok. [[13 Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung|13]], Weil-Positivität Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]).

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
Die de-Branges-Bedingung ist eng verwandt mit Weil-Positivität (Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]) und Nyman–Beurling (Dok. [[13 Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung|13]]) — alle verlangen die Positivität einer quadratischen Form / Reellwurzeligkeit; alle stoßen an dieselbe ungelöste Kernhürde.

## Quellen
- [The Riemann hypothesis for Hilbert spaces of entire functions — de Branges (Purdue)](https://www.math.purdue.edu/~branges/riemann-hilbert.pdf)
- [A Proof of the Riemann Hypothesis — de Branges (2017 draft, Purdue)](https://www.math.purdue.edu/~branges/proof-riemann-2017-04.pdf)
- [The Strange Case of Louis de Branges — Karl Sabbagh, London Review of Books](https://www.lrb.co.uk/the-paper/v26/n14/karl-sabbagh/the-strange-case-of-louis-de-branges)
- [The early historical roots of Lee-Yang theorem (arXiv 1410.6450, Kontext Hermite-Klasse)](https://arxiv.org/pdf/1410.6450)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Instanz von** → [[Positivität ∕ Reellwurzeligkeit]] — *de Branges: Positivitätsbedingung (für ζ widerlegt).*
- **wird widerlegt durch** → [[20 Louis de Branges – Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)]] — *Conrey–Li (2000): de Branges' Positivitätsbedingung für ζ verletzt.*

### Eingehende Relationen

- **widerlegt** ← [[20 Louis de Branges – Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)]] — *Conrey–Li (2000): de Branges' Positivitätsbedingung für ζ verletzt.*

### Belegte Aussagen (Claims)

- `[WIDERLEGT]` [[claim-debranges]] — de Branges' Positivitätsbedingung impliziert RH und gilt für ζ.

### Im Text erwähnt

- [[13 Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]]
- [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]]
