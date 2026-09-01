---
id: doc-32
number: 32
title: "Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)"
category: solution-program
status: open
tags: [landau-siegel, exceptional-zeros, yitang-zhang, GRH, 2022]
source_file: 32_Landau_Siegel_zeros_Zhang.md
lang: de
---

# Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)

**Kategorie:** RH-nahes Lösungsfeld (Ausnahme-Nullstellen / GRH)
**Autoren / Jahre:** Landau, Siegel (1930er); Yitang Zhang (2022)
**Typ:** Angriff auf potenzielle Gegenbeispiele zur (G)RH
**Status:** Existenz der Landau–Siegel-Nullstellen offen; Zhang liefert starke (effektive) Schranke

## Zusammenfassung
Eine **Landau–Siegel-Nullstelle** (Ausnahme-Nullstelle) ist eine hypothetische reelle Nullstelle einer Dirichlet-L-Funktion *sehr nahe* bei s = 1 — ein potenzielles Gegenbeispiel zur Generalisierten Riemann-Vermutung (GRH, Dok. 21). Ihre **Nicht-Existenz** zu beweisen, ist ein zentrales Teilziel auf dem Weg zur GRH/RH. Yitang Zhang (berühmt für die beschränkten Primzahllücken 2013) legte 2022 ein vielbeachtetes Preprint vor, das die Frage substanziell vorantreibt.

## Was ist eine Landau–Siegel-Nullstelle?
- Für einen reellen primitiven Charakter χ mod D könnte L(s, χ) eine reelle Nullstelle β sehr nahe bei 1 haben (β = 1 − ε mit winzigem ε).
- Eine solche Nullstelle widerspräche der GRH (die β = 1/2 verlangt) und würde die klassische nullstellenfreie Region (Dok. 12) "durchbrechen".
- Siegels Satz schließt sie aus, aber **ineffektiv** (die Konstante ist nicht berechenbar) — ein berüchtigtes Ärgernis der analytischen Zahlentheorie.
- Äquivalent: Eine Landau–Siegel-Nullstelle existiert genau dann (asymptotisch), wenn L(1, χ) "zu klein" ist.

## Yitang Zhang (2022): "Discrete mean estimates and the Landau–Siegel zero"
- **Resultat:** Für reelle primitive χ mod D gilt L(1, χ) ≫ (log D)^{−2022}, mit **absoluter, effektiv berechenbarer** impliziter Konstante.
- **Methode:** Die untere Schranke für L(1, χ) wird mit der Verteilung der Nullstellen einer **Familie** von Dirichlet-L-Funktionen in einem bestimmten Bereich verknüpft (Abstände aufeinanderfolgender Nullstellen). Auswertung gewisser **diskreter Mittelwerte vom Large-Sieve-Typ** erzeugt einen Widerspruch, falls L(1, χ) zu klein wäre.
- Das ~150-seitige Preprint (arXiv 2211.02515) wurde intensiv geprüft; es liefert kein vollständiges Ausschließen der Ausnahme-Nullstelle, aber eine wesentlich stärkere effektive Kontrolle als zuvor.

## Bedeutung / Einordnung
- Landau–Siegel-Nullstellen sind die **konkretesten potenziellen Gegenbeispiele** im (G)RH-Umfeld; ihr Ausschluss ist ein realistisches Etappenziel mit enormen Konsequenzen (Klassenzahlen, Primzahlen in Progressionen, Twin-Prime-Heuristiken).
- Paradoxerweise hätte sogar die *Existenz* einer Siegel-Nullstelle starke (teils GRH-artige) Konsequenzen ("illusory world") — ein vieluntersuchtes Phänomen.
- Verbindet sich mit Dichte-/nullstellenfreien Abschätzungen (Dok. 12, 17) und der GRH (Dok. 21).

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

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_analytic|Analytische Ansätze]]

| Achse | Wert |
|---|---|
| Familie | analytic |
| Implikation | `partial` |
| Euler-Produkt | `essential` |
| Positivität | `n/a` |
| Strenge | `theorem` · Evidenz `medium` |
| Testbar / formalisierbar | `low` / `low` |

**Offener Kernschritt:** Ausschluss reeller Ausnahmennullstellen; Siegels Satz bleibt ineffektiv.

**Hebel (was er liefern würde):** Wichtig für GRH-Anwendungen; Fortschritt ist quantifizierbar.

**Typische Fehlermodi:** [[F12_ineffective-nonuniform|F12 Ineffektive oder nicht gleichmäßige Konstanten]]

**Vergleichbar mit:** [[17_Lindelof_density_hypothesis|Lindelöf-Hypothese & Dichte-Hypothese]] · [[34_Bost_Connes_system|Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)]] · [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-32 doc-17 doc-34 doc-53`

**Ausgehende Beziehungen**
- *ist Teilresultat für* (`partial_result_for`) → [[concept_GRH|Verallgemeinerte/Große RH]] — Zhang: Landau-Siegel-Nullstellen (Ausnahmen zur GRH) eingeschränkt.

**Eingehende Beziehungen**
- *modelliert* (`models`) → [[concept_alternative-hypothesis|Alternative Hypothese (AH)]] — Landau-Siegel-Ausnahmenullstellen erzwingen AH-artige Starrheit im Abstandsspektrum.
- *ist Obstruktion für* (`obstruction_for`) → [[59_Langlands_functoriality_automorphic|59 — Langlands-Funktorialität & automorphe L-Funktionen: Weg zur GRH?]] — Landau–Siegel-Nullstellen bleiben mit voller Funktorialität verträglich.

**Thematisch benachbart (gemeinsame Tags):** [[59_Langlands_functoriality_automorphic|Langlands-Funktorialität & automorphe L-Funktionen: Weg zur GRH?]] · [[21_GRH_Selberg_class_grand_RH|Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
