---
id: doc-14
number: 14
title: "Li-Kriterium, Bombieri–Lagarias & Weil-Positivität"
category: criterion
status: open
tags: [li-criterion, bombieri-lagarias, weil-positivity, positivity]
source_file: 14_Li_criterion_Bombieri_Lagarias_Weil_positivity.md
lang: de
---

# Li-Kriterium, Bombieri–Lagarias & Weil-Positivität

**Kategorie:** Äquivalentes Kriterium (Positivität)
**Autoren / Jahre:** André Weil (1952), Xian-Jin Li (1997), Enrico Bombieri & Jeffrey Lagarias (1999)
**Typ:** Zur RH äquivalente Positivitätsbedingungen
**Status:** Äquivalenzen bewiesen; Positivität allgemein unbewiesen

## Zusammenfassung
Eine Familie eng verwandter Kriterien formuliert die RH als **Positivitätsaussage**. Weils Kriterium nutzt die explizite Formel als quadratische Form; Lis Kriterium übersetzt die RH in die Nicht-Negativität einer expliziten Zahlenfolge λ_n; Bombieri–Lagarias zeigen, dass beide dasselbe bedeuten und geben eine arithmetische Formel.

## Li-Kriterium (1997)
- Definiere die **Li-Koeffizienten**:

```
λ_n = Σ_ρ [ 1 − (1 − 1/ρ)^n ]   (Summe über alle nicht-trivialen Nullstellen ρ)
```

- **Satz (Li):** Die RH ist äquivalent zu **λ_n ≥ 0 für alle n ≥ 1**.
- Die λ_n lassen sich auch über logarithmische Ableitungen der ξ-Funktion an ihren Nullstellen ausdrücken und sind numerisch berechenbar; alle bisher berechneten Werte sind positiv (konsistent mit RH), ein allgemeiner Beweis der Positivität fehlt.

## Bombieri–Lagarias (1999)
- Verallgemeinerten das Li-Kriterium auf beliebige Multimengen komplexer Zahlen mit gewissen Eigenschaften.
- Lieferten eine **arithmetische Formel** für die λ_n über die **Guinand–Weil-explizite Formel** und zeigten: Die Positivität der λ_n hat **dieselbe Bedeutung** wie Weils Positivitätskriterium.

## Weil-Positivität (Weils Kriterium, 1952)
- Weils explizite Formel verbindet eine Summe über Nullstellen mit einer Summe über Primzahlen plus archimedischen Termen.
- **Weils Kriterium:** Die RH gilt genau dann, wenn eine bestimmte zugehörige **quadratische Form positiv (semidefinit)** ist — die "Weil-Positivität".
- Diese Positivität ist der analytische Kern auch von **Connes' Spurformel-Programm** (Dok. 10): Connes' Reduktion der RH läuft letztlich auf den Nachweis genau dieser Positivität hinaus (vgl. Connes–Consani "Weil positivity and trace formula", 2021).

## Bedeutung / Einordnung
- Bündelt mehrere Programme (explizite Formel, Connes, de Branges) unter einem gemeinsamen **Positivitäts-Leitmotiv**.
- Macht die RH zu einer konkreten, prüfbaren (numerisch stark gestützten) Ungleichungsaussage.
- **Offen:** Der Nachweis der Positivität für *alle* n bzw. für die volle quadratische Form ist genauso schwer wie die RH selbst.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Definition der Li-Koeffizienten
Mit der vollständigen ξ-Funktion (ξ(s) = ½ s(s−1)π^{−s/2}Γ(s/2)ζ(s)) setze
```
λ_n = (1/(n−1)!) d^n/ds^n [ s^{n−1} log ξ(s) ] |_{s=1}     (n ≥ 1).
```
Äquivalente Summe über die Nullstellen (paarweise ρ, 1−ρ zusammengefasst):
```
λ_n = Σ_ρ [ 1 − (1 − 1/ρ)^n ].
```

### Li-Kriterium (1997)
```
RH  ⟺  λ_n ≥ 0   für alle n ≥ 1.
```
**Beweisidee:** Die Abbildung ρ ↦ 1/ρ schickt die kritische Gerade Re(s)=1/2 auf den Kreis |z − 1| = 1. Schreibe z = 1/ρ. Dann ist 1 − (1−1/ρ)^n = 1 − (1−z)^n. Man zeigt: Re(λ_n) ≥ 0 ∀n ⟺ alle ρ liegen in |1 − 1/ρ| ≤ 1 ⟺ Re(ρ) ≤ 1/2 — und mit der Funktionalgleichung (Symmetrie ρ ↔ 1−ρ) ⟺ Re(ρ) = 1/2. Die Positivität für alle n erzwingt also die kritische Gerade.

### Bombieri–Lagarias (1999): Verallgemeinerung
Für eine beliebige Multimenge R = {ρ} komplexer Zahlen mit Σ (1+|ρ|)^{−2} < ∞ und Symmetrie ρ ↔ 1−ρ gilt:
```
Re(ρ) ≤ 1/2  ∀ρ   ⟺   λ_n := Σ_ρ [1 − (1 − 1/ρ)^n] ≥ 0  ∀n ≥ 1.
```
Plus arithmetische Formel via Guinand–Weil:
```
λ_n = Σ_{j=1}^n binom(n,j) (−1)^{j+1} ... = n(γ + log(4π))/2 − ... − Σ_{k} (arithm. Beiträge von Λ(m))
```
(explizit: λ_n drückt sich durch von-Mangoldt-Λ und archimedische Γ-Terme aus).

### Weils Positivitätskriterium (1952)
Für eine Testfunktion g (gerade, glatt, kompakter Träger) mit ĝ(t)=∫ g(x)e^{ixt}dx definiere die **Weil-Funktional**
```
W(g) = Σ_ρ ĝ(−i(ρ − 1/2))
     = ĝ-Hauptterm(Pole)  −  Σ_{n≥1} Λ(n)/√n · g(log n)  −  (1/2π)∫ ĝ(t) [Γ'/Γ-Term] dt.
```
**Weil-Kriterium:** RH ⟺ W(g ⋆ ḡ*) ≥ 0 für alle solche g (positiv-semidefinite quadratische Form). Genau diese Form ist die spektrale Seite in Connes' Spurformel (Dok. 10).

### Numerik
λ_1 = 1 + γ/2 − log(4π)/2 ≈ 0,0230957 > 0; alle bisher berechneten λ_n > 0 und wachsen ~ (n/2)(log n − 1 + γ − log 2π) unter RH.

## Quellen
- [Complements to Li's Criterion for the Riemann Hypothesis — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022314X99923922)
- [On the explicit formula in the theory of prime numbers (World Scientific)](https://www.worldscientific.com/doi/10.1142/S1793042112500327)
- [An arithmetic interpretation of generalized Li's criterion (arXiv 1305.1421)](https://arxiv.org/pdf/1305.1421)
- [Li coefficients as norms of functions in a model space (arXiv 2301.05779)](https://arxiv.org/pdf/2301.05779)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_criterion|Äquivalente Kriterien]]

| Achse | Wert |
|---|---|
| Familie | criterion |
| Implikation | `equivalent` |
| Euler-Produkt | `essential` |
| Positivität | `must-prove` |
| Strenge | `theorem` · Evidenz `medium` |
| Testbar / formalisierbar | `high` / `medium` |

**Offener Kernschritt:** λ_n >= 0 für alle n zeigen, ohne die Nullstellenlage zu benutzen.

**Hebel (was er liefern würde):** Verbindet Numerik (λ_n berechenbar) mit der Positivitätsfrage.

**Typische Fehlermodi:** [[F2_positivity-assumed|F2 Positivität angenommen statt bewiesen]] · [[F11_criterion-restates|F11 Äquivalenz ohne neuen Zugriff]]

**Vergleichbar mit:** [[13_Nyman_Beurling_Baez_Duarte|Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]] · [[16_Mertens_function_Riesz_criterion|Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]] · [[29_Jensen_Polya_Laguerre_Polya_GORZ|Jensen–Pólya-Programm: Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-14 doc-13 doc-16 doc-29`

**Ausgehende Beziehungen**
- *ist äquivalent zu* (`equivalent_to`) → [[concept_RH|Riemann-Vermutung (RH)]] — Li-Koeffizienten λ_n≥0 ⟺ RH.
- *benutzt* (`uses`) → [[13_Nyman_Beurling_Baez_Duarte|13 — Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]] — Beide Positivitäts-/Dichtekriterien, gemeinsames Leitmotiv.
- *ist Instanz von* (`instance_of`) → [[concept_positivity|Positivität / Reellwurzeligkeit]] — Weil-/Li-Positivität.

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[52_Connes_truncated_Weil_spectral_realization|52 — Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)]] — Baut direkt auf Weil-Positivitaet / der Weilschen Quadratform auf.
- *ist Blaupause für* (`blueprint_for`) → [[60_standard_conjectures_motives_positivity|60 — Grothendiecks Standardvermutungen & Motive: die Herkunft der Positivität]] — Weil-Positivität ist im geometrischen Fall der Hodge-Index-Satz.

**Thematisch benachbart (gemeinsame Tags):** [[60_standard_conjectures_motives_positivity|Grothendiecks Standardvermutungen & Motive: die Herkunft der Positivität]] · [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)]] · [[41_synthesis_what_a_proof_needs|Synthese: Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]] · [[10_Connes_noncommutative_geometry|Alain Connes: Spurformel & nichtkommutative Geometrie]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
