---
id: doc-21
number: 21
title: "Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse"
category: generalization
status: open
tags: [GRH, selberg-class, grand-RH, automorphic-L-functions, langlands]
source_file: 21_GRH_Selberg_class_grand_RH.md
lang: de
---

# Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse

**Kategorie:** Verallgemeinerungen
**Autoren / Jahre:** Dirichlet/Hecke (L-Funktionen), Atle Selberg (Selberg-Klasse, 1989/1992), Langlands (automorphe L-Funktionen)
**Typ:** Verallgemeinerte Vermutungen
**Status:** Alle offen; klassische RH ist Spezialfall

## Zusammenfassung
Die Riemann-Vermutung ist der Spezialfall einer ganzen Hierarchie von Vermutungen über die Nullstellen allgemeinerer "zeta-/L-Funktionen". Diese Verallgemeinerungen sind teils aus Anwendungssicht sogar wichtiger (z. B. die GRH in der algorithmischen Zahlentheorie).

## Verallgemeinerte Riemann-Vermutung (GRH)
- Erweitert die RH auf **Dirichlet-L-Funktionen** L(s, χ) zu Dirichlet-Charakteren χ.
- **Aussage:** Alle nicht-trivialen Nullstellen *jeder* Dirichlet-L-Funktion haben Realteil 1/2.
- **Anwendungen:** Unter GRH folgen u. a. Schranken für die kleinste quadratische Nicht-Reste, deterministische Primzahltests (Miller-Test), Resultate über Primzahlen in arithmetischen Progressionen.

## Selberg-Klasse (1989/1992)
- Selbergs **axiomatischer** Zugang: Statt einzelner Funktionen definiert man eine **Klasse** von Dirichlet-Reihen über charakterisierende Eigenschaften (Euler-Produkt, analytische Fortsetzung, Funktionalgleichung, Ramanujan-Bedingung).
- Für alle Funktionen dieser Klasse wird ein RH-Analogon erwartet ("RH für die Selberg-Klasse").
- Es existieren Riesz-Typ- und Li-Typ-Kriterien speziell für die Selberg-Klasse (vgl. Dok. 14, 16).

## Große Riemann-Vermutung (Grand RH, GRH)
- **Allgemeinste Fassung:** Alle nicht-trivialen Nullstellen *aller* **automorphen L-Funktionen** (Mellin-Transformierte von Hecke-Eigenformen etc.) liegen auf der kritischen Geraden.
- Verallgemeinert sowohl die klassische RH als auch die GRH für Dirichlet-L-Funktionen.

## Zusammenhang / offenes Strukturproblem
- Es wird vermutet, dass die **Selberg-Klasse = Klasse der automorphen L-Funktionen** ist — dann wären "RH für Selberg-Klasse" und "Große RH" äquivalent. Diese Gleichheit ist selbst ein wichtiges offenes Problem und Teil des **Langlands-Programms**.

## Bedeutung / Einordnung
- Zeigt, dass die RH kein Einzelphänomen ist, sondern Teil eines universellen Musters über eine ganze Welt von L-Funktionen.
- Random-Matrix-Statistik (Katz–Sarnak) sagt für *Familien* von L-Funktionen unterschiedliche Symmetrietypen (unitär, symplektisch, orthogonal) voraus — starke struktur­übergreifende Evidenz.
- Praktisch: Viele zahlentheoretische/algorithmische Resultate hängen an GRH, nicht nur an der klassischen RH.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Dirichlet-L-Funktionen (GRH)
Für einen Dirichlet-Charakter χ mod q:
```
L(s, χ) = Σ_{n=1}^∞ χ(n)/n^s = ∏_p (1 − χ(p) p^{−s})^{−1}   (Re s > 1).
```
**GRH:** Alle nicht-trivialen Nullstellen von L(s,χ) (für jedes primitive χ) haben Re(s) = 1/2.

### Axiome der Selberg-Klasse 𝒮
Eine Dirichlet-Reihe F(s) = Σ a_n n^{−s} gehört zu 𝒮, falls:
1. **Ramanujan-Bedingung:** a_n ≪_ε n^ε.
2. **Analytische Fortsetzung:** (s−1)^m F(s) ganz für ein m ≥ 0.
3. **Funktionalgleichung:** Φ(s) = Q^s ∏_j Γ(λ_j s + μ_j) F(s) erfüllt Φ(s) = ω Φ̄(1 − s̄), |ω| = 1.
4. **Euler-Produkt:** log F(s) = Σ_n b_n n^{−s} mit b_n = 0 außer für Primzahlpotenzen, b_n ≪ n^θ (θ < 1/2).
Definierende Invarianten: **Grad** d_F = 2 Σ_j λ_j (vermutet stets ∈ ℤ_{≥0}); Beispiele: ζ (Grad 1), L(s,χ) (Grad 1), automorphe L (Grad n).

### RH für die Selberg-Klasse
```
Für alle F ∈ 𝒮 liegen alle nicht-trivialen Nullstellen auf Re(s) = 1/2.
```

### Automorphe L-Funktionen (Große RH)
Für eine automorphe Darstellung π von GL_n(𝔸_ℚ):
```
L(s, π) = ∏_p ∏_{i=1}^n (1 − α_{i,p} p^{−s})^{−1}.
```
**Große RH:** alle nicht-trivialen Nullstellen von L(s,π) auf Re(s) = 1/2 (für alle π).

### Strukturhierarchie & offene Identität
```
{Dirichlet/Hecke-L} ⊂ {automorphe L-Funktionen} ⊆? Selberg-Klasse 𝒮.
```
Vermutung (Teil des Langlands-Programms): 𝒮 = {automorphe L-Funktionen}. Bekannt: Elemente von 𝒮 vom Grad 0 sind konstant 1; Grad zwischen 0 und 1 existiert nicht (Conrey–Ghosh / Kaczorowski–Perelli-Klassifikation der niedrigen Grade).

### Katz–Sarnak-Symmetrietypen (Random-Matrix, Dok. 06/07)
Familien von L-Funktionen zeigen je nach Symmetrie verschiedene Niedrig-Nullstellen-Statistiken:
```
unitär (U)  →  ζ, Dirichlet-L;   symplektisch (USp)  →  quadratische L;   orthogonal (O)  →  elliptische Kurven-L.
```
Diese strukturübergreifende Universalität ist starke Evidenz für die Große RH.

## Quellen
- [Generalized Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)
- [Grand Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Grand_Riemann_hypothesis)
- [On relations equivalent to the generalized Riemann hypothesis for the Selberg class (arXiv 1511.04603)](https://arxiv.org/pdf/1511.04603)
- [Equivalent criteria for the Riemann hypothesis for a general class of L-functions (arXiv 2409.17708)](https://arxiv.org/pdf/2409.17708)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *ist Instanz von* (`instance_of`) → [[concept_GRH|Verallgemeinerte/Große RH]] — GRH/Selberg-Klasse/Große RH.

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[43_Epstein_zeta_Selberg_class_rigidity|43 — Epstein-Zetafunktionen & Selberg-Klassen-Rigidität: Welche Eigenschaft erzwingt die kritische Gerade?]] — Selberg-Klassen-Klassifikation (Kaczorowski–Perelli).
- *benutzt* (`uses`) → [[59_Langlands_functoriality_automorphic|59 — Langlands-Funktorialität & automorphe L-Funktionen: Weg zur GRH?]] — Selberg-Klasse als axiomatische Schattenversion der automorphen Welt.

**Thematisch benachbart (gemeinsame Tags):** [[59_Langlands_functoriality_automorphic|Langlands-Funktorialität & automorphe L-Funktionen: Weg zur GRH?]] · [[32_Landau_Siegel_zeros_Zhang|Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
