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

## Quellen
- [Robin's Inequality & the Riemann Hypothesis — Emergent Mind](https://www.emergentmind.com/topics/robin-s-inequality)
- [Criteria equivalent to the Riemann Hypothesis (arXiv 0808.0640)](https://arxiv.org/pdf/0808.0640)
- [Riemann hypothesis — Wikipedia (Abschnitt: Consequences and equivalents)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
