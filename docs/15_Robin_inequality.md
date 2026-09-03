---
id: doc-15
number: 15
title: "Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)"
category: criterion
status: open
tags: [robin, lagarias, divisor-function, elementary]
source_file: 15_Robin_inequality.md
lang: de
---

# Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)

**Kategorie:** Äquivalentes Kriterium (arithmetisch/elementar)
**Autoren / Jahre:** Guy Robin (1984), Jeffrey Lagarias (2002); Grundlage Ramanujan / Gronwall
**Typ:** Zur RH äquivalente elementare Ungleichungen
**Status:** Äquivalenzen bewiesen; Ungleichungen allgemein unbewiesen

## Zusammenfassung
Bemerkenswert an diesen Kriterien ist, dass sie die RH **vollständig elementar** — ohne komplexe Analysis — als Ungleichung über die Teilersummenfunktion σ(n) ausdrücken. σ(n) = Σ_{d|n} d ist die Summe aller Teiler von n.

## Robins Ungleichung (1984)
- **Satz (Robin):** Die RH ist äquivalent zur Ungleichung

```
σ(n) < e^γ · n · log(log n)   für alle n > 5040
```

  wobei γ ≈ 0,5772 die Euler–Mascheroni-Konstante ist.
- Robin zeigte: Gilt die Ungleichung für alle n > 5040, so folgt die RH; gilt sie *nicht*, so ist die RH falsch (und es gäbe ein konkretes Gegenbeispiel n).
- Die Ungleichung ist für viele Klassen von n bewiesen (z. B. ungerade n, viele "kolossal abundante" Zahlen); nur ein potenzielles Versagen würde die RH widerlegen.

## Lagarias' elementares Kriterium (2002)
- **Satz (Lagarias):** Mit der harmonischen Zahl H_n = Σ_{k=1}^n 1/k ist die RH äquivalent zu

```
σ(n) ≤ H_n + e^{H_n} · log(H_n)   für alle n ≥ 1,
```

  mit Gleichheit nur für n = 1.
- Gilt als eines der "elementarsten" bekannten zur RH äquivalenten Statements — formulierbar mit Schulmathematik, aber genauso schwer zu beweisen.

## Hintergrund (Gronwall / Ramanujan)
- Gronwalls Satz: limsup σ(n)/(n log log n) = e^γ. Robins Ungleichung verschärft dies zu einer für *alle* großen n gültigen Schranke — und genau diese Verschärfung ist die RH.
- Ramanujan hatte verwandte Resultate über "highly composite" / "superior highly composite" Zahlen (teils erst posthum publiziert), die Robins Arbeit vorwegnahmen.

## Bedeutung / Einordnung
- Eindrucksvolle Demonstration, wie tief die RH in elementare Arithmetik (Teilersummen) hineinreicht.
- Didaktisch wertvoll (kein Apparat der komplexen Analysis nötig).
- **Offen:** Die scheinbar "einfache" Ungleichung allgemein zu beweisen ist äquivalent zur vollen RH — also genauso schwer.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Robins Satz (1984)
Mit σ(n) = Σ_{d|n} d und γ ≈ 0,5772156649 (Euler–Mascheroni):
```
RH  ⟺  σ(n) < e^γ · n · log log n   für alle n > 5040.
```
**Beweisrichtung „RH ⇒ Ungleichung" (Skizze):** Robin nutzt explizite Abschätzungen der Chebyshev-Funktion θ(x)=Σ_{p≤x} log p, die unter RH den Fehlerterm θ(x) = x + O(√x log²x) (Dok. 02) haben. Für „kolossal abundante" Zahlen (die σ(n)/(n log log n) maximieren) übersetzt sich dieser Fehlerterm in die scharfe Konstante e^γ. **Gegenrichtung:** Wäre RH falsch (Nullstelle mit β>1/2), so konstruiert man eine Folge von n, die die Ungleichung verletzt.

### Gronwalls Satz (1913, Hintergrund)
```
limsup_{n→∞} σ(n)/(n log log n) = e^γ.
```
Robin verschärft dies von „limsup = e^γ" zu „strikt < e^γ für alle n > 5040" — und genau diese Verschärfung ist äquivalent zur RH. Das größte bekannte n mit σ(n) ≥ e^γ n log log n ist n = 5040 selbst (sowie kleinere Ausnahmen 3,4,5,6,8,9,10,12,16,18,20,24,30,36,48,60,72,84,120,180,240,360,720,840,2520,5040).

### Lagarias' Variante (2002)
Mit der harmonischen Zahl H_n = Σ_{k=1}^n 1/k:
```
RH  ⟺  σ(n) ≤ H_n + exp(H_n) · log(H_n)   für alle n ≥ 1,
```
mit Gleichheit nur bei n = 1. **Herleitung:** Da H_n = log n + γ + O(1/n) und exp(H_n) = e^γ n (1+o(1)), ist exp(H_n) log H_n = e^γ n (log log n + log(1 + γ/log n + …)). Lagarias zeigt, dass die Robin-Schranke äquivalent in diese für *alle* n ≥ 1 gültige, gleichungsscharfe Form gebracht werden kann.

### Verwandte arithmetische Kriterien
- **Nicolas (1983):** RH ⟺ ∏_{p≤x}(p/(p−1)) > e^γ log θ(x) für alle Primorial-artigen Argumente (über die Funktion n/φ(n), φ = Euler-Totient).

## Quellen
- [Robin's Inequality & the Riemann Hypothesis — Emergent Mind](https://www.emergentmind.com/topics/robin-s-inequality)
- [Criteria equivalent to the Riemann Hypothesis (arXiv 0808.0640)](https://arxiv.org/pdf/0808.0640)
- [Riemann hypothesis — Wikipedia (Abschnitt: Consequences and equivalents)](https://en.wikipedia.org/wiki/Riemann_hypothesis)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Äquivalenz-Falle** *(Tier 2)* — Ein Kriterium ist zur RH äquivalent und damit exakt gleich schwer — die Umformulierung erzeugt den Anschein von Fortschritt, ohne die Beweislast zu senken.
>   *Fluchtbedingung:* Eine der beiden Richtungen muss in STRIKT SCHWÄCHERER Form unbedingt bewiesen werden, oder es muss eine quantitative Größe geben, die sich unabhängig von der RH bewegen lässt (Λ ≤ 0.22, Anteil > 41 %, d_N-Raten). Nur solche Bewegungen zählen als Fortschritt — siehe docs/58.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!missing]- Die fehlende Aussage
> **Bewiesen:** Äquivalenz zur RH (Robin 1984); Lagarias' elementare Variante.
> **Es fehlt:** Die Ungleichung selbst. Es gibt kein unbedingtes Teilresultat, das ihr näherkommt.
> **Typ:** aequivalenz · Bewertung: [[58_gap_registry_near_miss]]

> [!abstract]- Graph-Nachbarn (1)
> - *äquivalent zu* → **Riemann-Vermutung (RH)** — Robin/Lagarias-Ungleichung ⟺ RH.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
