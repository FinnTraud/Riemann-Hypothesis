---
id: doc-38
number: 38
title: "Bombieris offizielle Clay-Problemstellung (Millennium-Problem)"
category: reference
status: reference
tags: [bombieri, clay, millennium-problem, official-statement]
source_file: 38_Bombieri_official_problem_statement.md
lang: de
---

# Bombieris offizielle Clay-Problemstellung (Millennium-Problem)

**Kategorie:** Referenz / autoritative Problemstellung
**Autor / Jahr:** Enrico Bombieri, 2000 (Clay Mathematics Institute)
**Typ:** Offizielle Formulierung des Millennium-Preisproblems
**Status:** Maßgebliche Referenz; Preis (1 Mio USD) unvergeben

## Zusammenfassung
Enrico Bombieri verfasste die **offizielle Problembeschreibung** der Riemann-Vermutung für die Millennium-Preisprobleme des Clay Mathematics Institute (2000). Sie ist die autoritative Referenz für die exakte Formulierung, den Kontext und die akzeptierten äquivalenten Fassungen.

## Mathematischer Kern (Formeln & Sätze)

### Offizielle Aussage
Die ζ-Funktion (Re s > 1: ζ(s) = Σ n^{−s} = ∏_p (1−p^{−s})^{−1}), fortgesetzt auf ℂ, erfüllt mit der vervollständigten Funktion
```
ξ(s) = (1/2) s(s−1) π^{−s/2} Γ(s/2) ζ(s),   ξ(s) = ξ(1−s),
```
**Riemann-Vermutung:** Alle Nullstellen von ξ(s) haben Re(s) = 1/2.

### Bombieris äquivalente Formulierung (ξ auf der kritischen Geraden)
Setze die reelle Funktion auf der Geraden:
```
Ξ(t) = ξ(1/2 + it)   (reellwertig für reelles t).
```
**RH ⟺** alle lokalen Maxima von Ξ(t) sind positiv und alle lokalen Minima sind negativ (d. h. zwischen je zwei aufeinanderfolgenden Extrema ein Vorzeichenwechsel ⇒ alle Nullstellen reell ⇒ auf der Geraden).

### Funktionalgleichung & Hadamard-Produkt (in der offiziellen Darstellung)
```
ξ(s) = ξ(0) ∏_ρ (1 − s/ρ)   (Produkt über nicht-triviale Nullstellen, geeignet gepaart),
ζ(s) = π^{s/2} / (Γ(s/2)) · ξ(s) / ((1/2)s(s−1)).
```

### Verbindung zu Primzahlen (von-Mangoldt, in der Problembeschreibung)
```
ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − (1/2)log(1−x^{−2}),
RH ⟺ ψ(x) = x + O(√x log²x).
```

## Bedeutung / Einordnung
- **Autoritative Quelle** für exakte Formulierung und akzeptierte Äquivalenzen — ideal als „ground truth" im MCP-Server.
- Enthält Bombieris Diskussion des Funktionenkörper-Falls (Weil/Deligne, Dok. 18) als Motivation und der spektralen Interpretation (Hilbert–Pólya, Dok. 05).
- Definiert implizit die Akzeptanzkriterien des Clay-Instituts (Publikation + 2 Jahre Bewährung, vgl. Dok. 27).

## Quellen
- [Problems of the Millennium: the Riemann Hypothesis — E. Bombieri (Clay, PDF)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
- [Riemann Hypothesis — Clay Mathematics Institute](https://www.claymath.org/millennium/riemann-hypothesis/)
- [The Riemann Hypothesis — E. Bombieri (UC Davis Mirror)](https://www.math.ucdavis.edu/~tracy/courses/math205A/riemann.pdf)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *ist Instanz von* (`instance_of`) → [[concept_RH|Riemann-Vermutung (RH)]] — Offizielle Clay-Problemstellung der RH.

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
