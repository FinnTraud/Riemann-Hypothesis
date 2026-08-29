---
id: doc-04
title: "Levinson, Conrey & Co.: Positiver Anteil der Nullstellen auf der kritischen Geraden"
nummer: "04"
kategorie: Partielle Resultate
status: BEWIESEN
typ: dokument
aliases:
  - "doc-04"
  - "Dok. 04"
tags:
  - "dokument"
  - "kategorie/partial-results"
  - "status/proven"
  - "thema/conrey"
  - "thema/levinson"
  - "thema/mollifier"
  - "thema/positive-proportion"
  - "thema/speiser"
quelle: docs/04_Levinson_Conrey_positive_proportion.md
---

> [!info] Navigation
> **Karte:** [[MOC B – Partielle Resultate (Nullstellen auf der kritischen Geraden)]] · **Kategorie:** Partielle Resultate · **Status:** `BEWIESEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/04_Levinson_Conrey_positive_proportion.md`

# Levinson, Conrey & Co.: Positiver Anteil der Nullstellen auf der kritischen Geraden

**Kategorie:** Partielles Resultat
**Autoren / Jahre:** Norman Levinson (1974), J. Brian Conrey (1989), Conrey–Iwaniec–Soundararajan u. a. (>2010)
**Typ:** Bewiesene quantitative Teilresultate zur RH
**Status:** Bewiesen; aktuell >41 % nachgewiesen, volle RH (100 %) offen

## Zusammenfassung
Eine Reihe von Arbeiten beweist, dass ein *positiver Bruchteil* aller nicht-trivialen Nullstellen auf der kritischen Geraden liegt — quantitativ deutlich mehr als Hardys "unendlich viele". Die Entwicklung der nachgewiesenen Untergrenze:
- **Selberg (1942):** ein positiver (kleiner) Anteil.
- **Levinson (1974):** mindestens **1/3** (≈ 33,3 %).
- **Conrey (1989):** mindestens **2/5** (= 40 %).
- **Spätere Arbeiten (Bui–Conrey–Young, Feng, Pratt–Robles u. a., ab ~2011):** **über 41 %**.

## Kernidee: die Levinson–Conrey-Mollifier-Methode
- Man zählt nicht direkt die Nullstellen von ζ auf der Geraden, sondern nutzt einen Zusammenhang zwischen Nullstellen von ζ und Nullstellen seiner Ableitung ζ′ (bzw. einer modifizierten Funktion).
- Ein **Mollifier** (ein geschickt gewähltes Dirichlet-Polynom) "glättet" die Zetafunktion in der Nähe der kritischen Geraden, sodass man die relevanten Vorzeichenwechsel / das Argumentprinzip kontrollieren und die Anzahl der Nullstellen auf der Geraden von unten abschätzen kann.
- Verfeinerungen bestehen vor allem in raffinierteren Mollifiern (längere Dirichlet-Polynome, zweistufige Mollifier) und schärferer asymptotischer Analyse der entstehenden Momentintegrale.

## Verwandtes: Speiser-Theorem
- Speiser (1934) zeigte: Die RH ist äquivalent dazu, dass ζ′(s) keine Nullstellen im Streifen 0 < Re(s) < 1/2 besitzt. Die Levinson-Methode nutzt diesen Zusammenhang zwischen Nullstellen von ζ und ζ′ aus.

## Bedeutung / Einordnung
- Stärkstes Resultat *in Richtung* RH mit klassischen Methoden: Über 41 % aller Nullstellen liegen nachweislich auf der Geraden.
- Grenze der Methode: Mollifier-Techniken scheinen einen Anteil deutlich unter 100 % nicht überschreiten zu können — sie liefern prinzipiell **keinen** Weg zur vollen RH (man bräuchte exakt 100 % *und* den Ausschluss jeglicher Ausnahme).
- Eng verbunden mit der Random-Matrix-Theorie (Momente von ζ, Dok. [[07 Keating–Snaith – Momente der Zetafunktion via charakteristische Polynome (CUE)|07]]) und Dichte-Abschätzungen (Dok. [[17 Lindelöf-Hypothese & Dichte-Hypothese|17]]).

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Levinsons Methode (1974) — Formeln
Zentrale Größe: Zähle Nullstellen über das Argumentprinzip für eine modifizierte Funktion. Levinson betrachtet
```
G(s) = ξ(s) + (Korrektur),   bzw. die Funktion  B(s) = ½ + (1/log T)·ζ'(s)/ζ(s)
```
und nutzt **Speisers Äquivalenz** (RH ⟺ ζ'(s) ≠ 0 für Re(s) < 1/2). Schlüssel ist ein **Mollifier** — ein Dirichlet-Polynom
```
M(s) = Σ_{n ≤ y} μ(n) P(log(y/n)/log y) · n^{−(s−1/2)}/ ...,   y = T^θ
```
der |ζ| nahe der Geraden „glättet". Man zeigt, dass die Anzahl der Vorzeichenwechsel (bzw. reellen Nullstellen) einer zugehörigen reellen Funktion mindestens
```
N₀(T) ≥ κ · N(T),   κ = 1 − (1/R) log( (1/(2πi)) ∮ ... )
```
ergibt, wobei R = log(y)/log(T) (Mollifier-Länge) und ein Mittelwertintegral
```
I = (1/T) ∫_0^T |V·M (1/2 + it)|² dt
```
asymptotisch ausgewertet wird (V eine Linearkombination von ζ und ζ'). Levinson erhält κ = 1/3 mit θ = 1/2 − ε.

### Conrey (1989) und darüber hinaus
- Conrey verlängerte den Mollifier auf θ = 4/7 − ε (mittels Kloosterman-Summen-Abschätzungen) ⇒ **κ ≥ 2/5 = 0,40**.
- Zweistufige Mollifier M = M₁ + M₂ (Feng; Bui–Conrey–Young; Pratt–Robles–Zaharescu) ⇒ **κ > 0,41** (aktueller Rekordbereich ~0,4172).
- Allgemeine Form des auszuwertenden Hauptterms (Mollified second moment):
```
(1/T)∫_0^T |ζ(1/2+it)|² |M(1/2+it)|² dt ~ c(P) · log T
```
mit einem Funktional c(P) im Mollifier-Polynom P, das man variationsrechnerisch optimiert (Euler–Lagrange-Gleichung für P).

### Warum die Methode bei < 100 % blockiert
Die Mollifier-Länge θ ist durch die verfügbaren Mittelwertsätze (zweite/vierte Momente, Large Sieve) begrenzt; selbst θ → 1 (unter starken Vermutungen) liefert κ deutlich unter 1. Es gibt also keinen bekannten Weg, über Mollifier zu κ = 1 *und* dem Ausschluss aller Ausnahmen zu gelangen.

## Quellen
- [More than 41% of the zeros of the zeta function are on the critical line (ResearchGate)](https://www.researchgate.net/publication/45902466_More_than_41_of_the_zeros_of_the_zeta_function_are_on_the_critical_line)
- [Zeros on the Critical Line — E. Naslund (UBC)](https://personal.math.ubc.ca/~gerg/teaching/613-Winter2011/ZerosCriticalLine.pdf)
- [On a choice of the mollified function in the Levinson-Conrey method (arXiv 1403.5786)](https://arxiv.org/pdf/1403.5786)
- [Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Riemann_hypothesis)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Teilresultat für** → [[Riemann-Vermutung (RH)]] — *Levinson/Conrey: >41% auf der Geraden.*
- **verallgemeinert** → [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden]] — *Quantifiziert Hardys Resultat (positiver Anteil).*

### Eingehende Relationen

- **ist stärker als** ← [[53 Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-]] — *Die 100-%-Aussagen sind bedingt; unbedingt sind bislang nur ~41 % (Conrey).*

### Belegte Aussagen (Claims)

- `[BEWIESEN]` [[claim-proportion]] — Über 41% aller nicht-trivialen Nullstellen liegen auf der kritischen Geraden.

### Im Text erwähnt

- [[07 Keating–Snaith – Momente der Zetafunktion via charakteristische Polynome (CUE)]]
- [[17 Lindelöf-Hypothese & Dichte-Hypothese]]
