---
id: doc-32
title: "Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)"
nummer: "32"
kategorie: Lösungsprogramme
status: OFFEN
typ: dokument
aliases:
  - "doc-32"
  - "Dok. 32"
tags:
  - "dokument"
  - "kategorie/solution-program"
  - "status/open"
  - "thema/2022"
  - "thema/exceptional-zeros"
  - "thema/grh"
  - "thema/landau-siegel"
  - "thema/yitang-zhang"
quelle: docs/32_Landau_Siegel_zeros_Zhang.md
---

> [!info] Navigation
> **Karte:** [[MOC L – Weitere aktive Lösungsprogramme (potenziell beweisrelevant)]] · **Kategorie:** Lösungsprogramme · **Status:** `OFFEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/32_Landau_Siegel_zeros_Zhang.md`

# Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)

**Kategorie:** RH-nahes Lösungsfeld (Ausnahme-Nullstellen / GRH)
**Autoren / Jahre:** Landau, Siegel (1930er); Yitang Zhang (2022)
**Typ:** Angriff auf potenzielle Gegenbeispiele zur (G)RH
**Status:** Existenz der Landau–Siegel-Nullstellen offen; Zhang liefert starke (effektive) Schranke

## Zusammenfassung
Eine **Landau–Siegel-Nullstelle** (Ausnahme-Nullstelle) ist eine hypothetische reelle Nullstelle einer Dirichlet-L-Funktion *sehr nahe* bei s = 1 — ein potenzielles Gegenbeispiel zur Generalisierten Riemann-Vermutung (GRH, Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]). Ihre **Nicht-Existenz** zu beweisen, ist ein zentrales Teilziel auf dem Weg zur GRH/RH. Yitang Zhang (berühmt für die beschränkten Primzahllücken 2013) legte 2022 ein vielbeachtetes Preprint vor, das die Frage substanziell vorantreibt.

## Was ist eine Landau–Siegel-Nullstelle?
- Für einen reellen primitiven Charakter χ mod D könnte L(s, χ) eine reelle Nullstelle β sehr nahe bei 1 haben (β = 1 − ε mit winzigem ε).
- Eine solche Nullstelle widerspräche der GRH (die β = 1/2 verlangt) und würde die klassische nullstellenfreie Region (Dok. [[12 Nullstellenfreie Regionen (klassischer analytischer Ansatz)|12]]) "durchbrechen".
- Siegels Satz schließt sie aus, aber **ineffektiv** (die Konstante ist nicht berechenbar) — ein berüchtigtes Ärgernis der analytischen Zahlentheorie.
- Äquivalent: Eine Landau–Siegel-Nullstelle existiert genau dann (asymptotisch), wenn L(1, χ) "zu klein" ist.

## Yitang Zhang (2022): "Discrete mean estimates and the Landau–Siegel zero"
- **Resultat:** Für reelle primitive χ mod D gilt L(1, χ) ≫ (log D)^{−2022}, mit **absoluter, effektiv berechenbarer** impliziter Konstante.
- **Methode:** Die untere Schranke für L(1, χ) wird mit der Verteilung der Nullstellen einer **Familie** von Dirichlet-L-Funktionen in einem bestimmten Bereich verknüpft (Abstände aufeinanderfolgender Nullstellen). Auswertung gewisser **diskreter Mittelwerte vom Large-Sieve-Typ** erzeugt einen Widerspruch, falls L(1, χ) zu klein wäre.
- Das ~150-seitige Preprint (arXiv 2211.02515) wurde intensiv geprüft; es liefert kein vollständiges Ausschließen der Ausnahme-Nullstelle, aber eine wesentlich stärkere effektive Kontrolle als zuvor.

## Bedeutung / Einordnung
- Landau–Siegel-Nullstellen sind die **konkretesten potenziellen Gegenbeispiele** im (G)RH-Umfeld; ihr Ausschluss ist ein realistisches Etappenziel mit enormen Konsequenzen (Klassenzahlen, Primzahlen in Progressionen, Twin-Prime-Heuristiken).
- Paradoxerweise hätte sogar die *Existenz* einer Siegel-Nullstelle starke (teils GRH-artige) Konsequenzen ("illusory world") — ein vieluntersuchtes Phänomen.
- Verbindet sich mit Dichte-/nullstellenfreien Abschätzungen (Dok. [[12 Nullstellenfreie Regionen (klassischer analytischer Ansatz)|12]], [[17 Lindelöf-Hypothese & Dichte-Hypothese|17]]) und der GRH (Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]).

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Definition der Ausnahme-Nullstelle
Für χ reeller primitiver Charakter mod D besagt die klassische nullstellenfreie Region (Page/Landau): L(s,χ) ≠ 0 in
```
σ > 1 − c/log(D(|t|+2)),
```
**außer** möglicherweise einer einzigen reellen, einfachen **Siegel-Nullstelle** β mit
```
β > 1 − c/log D.
```

### Äquivalenz Siegel-Nullstelle ⟺ kleines L(1,χ)
Über die Klassenzahlformel / Mittelwertbeziehung gilt:
```
β nahe 1   ⟺   L(1, χ) klein,   genauer  1 − β  ≍  L(1,χ)/log D.
```
Eine untere Schranke für L(1,χ) hält β von 1 fern.

### Siegels (ineffektiver) Satz vs. effektive Schranken
```
Siegel (1935):  L(1,χ) ≫_ε D^{−ε}   — aber die Konstante ist NICHT berechenbar.
Klassisch effektiv (Goldfeld–Gross–Zagier-Umfeld):  L(1,χ) ≫ (log D)^{−1}·(...)  nur unter Zusatzannahmen.
```

### Yitang Zhang (2022) — das Resultat
```
L(1, χ) ≫ (log D)^{−2022},   mit absoluter, EFFEKTIV berechenbarer Konstante.
```
Äquivalent: jede Siegel-Nullstelle erfüllt 1 − β ≫ (log D)^{−2023} (effektiv).

### Beweisstrategie (Skizze)
1. Verknüpfe die untere Schranke für L(1,χ) mit der **Verteilung der Nullstellen** einer Familie von Dirichlet-L-Funktionen L(s, ψ) in einem Bereich nahe s = 1; eine Siegel-Nullstelle erzwingt anomale Nullstellen-Cluster (Deuring–Heilbronn-Phänomen: eine Ausnahme-Nullstelle stößt andere Nullstellen weg).
2. Werte **diskrete Mittelwerte vom Large-Sieve-Typ** aus:
```
Σ_{ψ mod Q}^* | Σ_{n ~ N} a_n ψ(n) |²  ≪  (Q + N) Σ |a_n|²,
```
über geeignete Familien und Gewichte (Zhang konstruiert spezielle Mollifier/Gewichte a_n).
3. Wäre L(1,χ) zu klein, so ergäben sich aus 1.+2. zwei unvereinbare Schätzungen desselben diskreten Mittels ⇒ **Widerspruch**.

### Bedeutung der Formeln
Die effektive Schranke ist schwächer als „keine Siegel-Nullstelle" (das wäre 1−β ≫ 1/log D), aber stärker und effektiv gegenüber Siegel. Ausschluss der Siegel-Nullstelle hätte u. a. zur Folge: GRH-artige Schranken für kleinste Primzahlen in Progressionen, Klassenzahl-1-Probleme, Twin-Prime-Konstanten.

## Quellen
- [Discrete mean estimates and the Landau-Siegel zero — Y. Zhang (arXiv 2211.02515)](https://arxiv.org/abs/2211.02515)
- [Discrete mean estimates and the Landau-Siegel zero (PDF)](https://arxiv.org/pdf/2211.02515)
- [Landau–Siegel zero — Wikipedia](https://en.wikipedia.org/wiki/Landau%E2%80%93Siegel_zero)
- [Generalized Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Teilresultat für** → [[Verallgemeinerte∕Große RH]] — *Zhang: Landau-Siegel-Nullstellen (Ausnahmen zur GRH) eingeschränkt.*

### Eingehende Relationen

- **wird modelliert von** ← [[Alternative Hypothese (AH)]] — *Landau-Siegel-Ausnahmenullstellen erzwingen AH-artige Starrheit im Abstandsspektrum.*

### Belegte Aussagen (Claims)

- `[BEWIESEN]` [[claim-zhang]] — L(1,χ) ≫ (log D)^{-2022}, effektiv (Landau-Siegel-Nullstellen eingeschränkt).

### Im Text erwähnt

- [[12 Nullstellenfreie Regionen (klassischer analytischer Ansatz)]]
- [[17 Lindelöf-Hypothese & Dichte-Hypothese]]
- [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse]]
