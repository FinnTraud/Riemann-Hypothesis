---
id: doc-36
title: "Konsequenzen der Riemann-Vermutung (was folgt, wenn sie wahr ist)"
nummer: "36"
kategorie: Kontext
status: REFERENZ
typ: dokument
aliases:
  - "doc-36"
  - "Dok. 36"
tags:
  - "dokument"
  - "kategorie/context"
  - "status/reference"
  - "thema/class-numbers"
  - "thema/consequences"
  - "thema/grh-applications"
  - "thema/miller-rabin"
  - "thema/prime-gaps"
quelle: docs/36_consequences_of_RH.md
---

> [!info] Navigation
> **Karte:** [[MOC M – Meta ∕ 'Bulletproof'-Schicht (Obstruktionen, Synthese, Verifikation)]] · **Kategorie:** Kontext · **Status:** `REFERENZ`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/36_consequences_of_RH.md`

# Konsequenzen der Riemann-Vermutung (was folgt, wenn sie wahr ist)

**Kategorie:** Kontext / Implikationen
**Typ:** Übersicht der Folgerungen
**Status:** Bedingte Sätze (gelten unter RH / GRH)

## Zusammenfassung
Hunderte Sätze sind „bedingt unter RH" bewiesen — sie würden sofort unbedingt gelten, sobald die RH bewiesen ist. Diese Liste zeigt, *warum* die RH so zentral ist, und liefert einem RH-Assistenten den Anwendungs-/Konsequenzkontext. Manche Folgerungen brauchen die **GRH** (Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]), nicht nur die klassische RH — das ist jeweils vermerkt.

## Mathematischer Kern (Formeln & Sätze)

### Primzahlverteilung (RH)
```
π(x) = Li(x) + O(√x log x)        (Koch 1901; bestmöglicher Fehlerterm)
ψ(x) = x + O(√x log²x)
|π(x) − Li(x)| < (1/8π) √x log x   für x ≥ 2657 (Schoenfeld, explizit unter RH)
```

### Primzahllücken (RH)
```
p_{n+1} − p_n = O(√(p_n) log p_n).
```
(Cramér unter RH; unbedingt ist man weit davon entfernt. Beachte: die *Cramér-Vermutung* p_{n+1}−p_n = O(log²p_n) ist stärker und folgt NICHT aus RH, Dok. [[39 Cramér-Modell & probabilistische Heuristiken der Primzahlen|39]].)

### Mertens- / Möbius-Summen (RH)
```
M(x) = Σ_{n≤x} μ(n) = O(x^{1/2+ε}),   Σ_{n≤x} μ(n)/n = O(x^{−1/2+ε}).
```

### Miller–Rabin / Primzahltests (GRH)
Unter GRH ist der **deterministische** Miller-Test in Polynomzeit korrekt: Eine zusammengesetzte Zahl n besitzt einen Zeugen a ≤ 2(log n)². (Unbedingt liefert erst AKS 2002 deterministisch polynomiell — aber langsamer.)

### Kleinste quadratische Nicht-Reste / Klassenzahlen (GRH)
```
Kleinster quadratischer Nichtrest mod p  ≪ (log p)²   (Ankeny, unter GRH).
Effektive untere Schranken für Klassenzahlen h(−d) (keine Siegel-Nullstelle, Dok. 32).
```

### Goldbach & additive Probleme
- Die **ternäre** Goldbach-Vermutung (jede ungerade Zahl > 5 ist Summe dreier Primzahlen) wurde 2013 von **Helfgott unbedingt** bewiesen — gestützt auf rigorose RH-Verifikation in endlicher Höhe (Platt, Dok. [[24 Numerische Verifikation der Riemann-Vermutung|24]]). Frühe Beweise (Hardy–Littlewood) waren bedingt unter GRH.

### Lindelöf & Momente (RH ⇒)
```
ζ(1/2 + it) = O(t^ε)   (Lindelöf, Dok. 17).
```

### Wachstum von ζ und 1/ζ auf der 1-Linie (RH)
```
1/ζ(1+it) = O(log log t),   |ζ(1+it)| ≍ log log t   (scharfe Konstanten unter RH; Littlewood).
```

## Bedeutung / Einordnung
- Die RH ist ein **„Master-Schlüssel"**: ein Beweis würde Hunderte bedingter Resultate auf einen Schlag unbedingt machen.
- Viele praktische/algorithmische Konsequenzen brauchen die **GRH** (Dirichlet-L), nicht nur die klassische RH.
- Umgekehrt zeigt die Liste, *warum* ein Beweis so wertvoll (und gesucht) ist.

## Quellen
- [Riemann hypothesis — Wikipedia (Consequences)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
- [The Riemann Hypothesis — E. Bombieri (Clay)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
- [Generalized Riemann hypothesis — Wikipedia (Consequences)](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **nutzt** → [[Riemann-Vermutung (RH)]] — *Konsequenzen der RH (Anwendungskontext).*

### Im Text erwähnt

- [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse]]
- [[24 Numerische Verifikation der Riemann-Vermutung]]
- [[39 Cramér-Modell & probabilistische Heuristiken der Primzahlen]]
