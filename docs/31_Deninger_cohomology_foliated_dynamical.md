---
id: doc-31
number: 31
title: "Deningers Kohomologie-Programm & dynamische Systeme auf gefolierten Räumen"
category: solution-program
status: open
tags: [deninger, cohomology, foliated-spaces, dynamical-systems, regularized-determinant]
source_file: 31_Deninger_cohomology_foliated_dynamical.md
lang: de
---

# Deningers Kohomologie-Programm & dynamische Systeme auf gefolierten Räumen

**Kategorie:** Aktives Lösungsprogramm (arithmetische Geometrie / Dynamik)
**Autor / Jahre:** Christopher Deninger (ab frühen 1990ern); verwandt Flach–Morin, Leichtnam
**Typ:** Konjekturales kohomologisches/dynamisches Programm zur RH
**Status:** Offen; konjekturaler Rahmen, Schlüsselobjekte noch nicht konstruiert

## Zusammenfassung
Christopher Deninger schlug ein **kohomologisches Programm** vor, in dem Zetafunktionen als **regularisierte Determinanten** geometrischer/dynamischer Operatoren ausgedrückt werden. Ziel: die explizite Formel der Zahlentheorie (Dok. 02) als **Lefschetz-Spurformel** zu interpretieren und die RH als **spektrale Symmetriebedingung** — in direkter Analogie zum bewiesenen Weil/Deligne-Fall (Dok. 18).

## Die Leitidee
- Im Funktionenkörper-Fall ist ζ ein Quotient charakteristischer Polynome des Frobenius auf étaler Kohomologie; die RH ist eine Aussage über die Eigenwerte dieses Operators.
- **Deningers Wunsch:** Finde für Spec(ℤ) (bzw. arithmetische Schemata) eine **Kohomologietheorie** mit einem "Frobenius-artigen" Fluss/Operator, sodass:

```
ζ(s) "=" det_∞( (s − Θ) / 2π | H^•_{?} )^{±1}
```

  (regularisierte Determinante eines Operators Θ auf hypothetischen Kohomologiegruppen).
- Die **nicht-trivialen Nullstellen** wären dann Eigenwerte von Θ auf H¹; die **RH = Selbstadjungiertheit / spektrale Symmetrie** von Θ (eine Hilbert–Pólya-Realisierung, Dok. 05).

## Dynamische Systeme auf gefolierten Räumen
- Da die gesuchte Kohomologie für arithmetische Schemata (noch) nicht existiert, sucht Deninger nach **Modellen**: dynamische Systeme auf **gefolierten Mannigfaltigkeiten** (foliated spaces), deren **blattweise (leafwise) Kohomologie** mehrere der erwarteten Struktureigenschaften besitzt.
- In diesen Modellen entsprechen:
  - geschlossene Orbits ↔ Primzahlen,
  - Längen der Orbits ↔ log p,
  - die Lefschetz-Spurformel des Flusses ↔ Weils explizite Formel.
- **Flach–Morin** und andere haben Deningers Vermutungen über **Weil-Arakelov-Kohomologie** präzisiert und teilweise formalisiert.

## Bedeutung / Einordnung
- Liefert eine **konzeptuelle Brücke** zwischen dem bewiesenen geometrischen Fall und der analytischen RH — und eine geometrische Erklärung, *warum* die RH wahr sein sollte (spektrale Symmetrie eines natürlichen Operators).
- Eng verwandt und teils komplementär zu Connes' Adèle/𝔽₁-Programm (Dok. 10, 30): beide suchen die "fehlende Geometrie über ℤ", aber mit unterschiedlichen Werkzeugen (Dynamik/Foliation vs. nichtkommutative Geometrie/Topos).
- **Status:** Programmatisch und konjektural — die zentrale Kohomologietheorie samt Operator ist nicht konstruiert. Kein Beweis, aber ein einflussreicher struktureller Kompass.

## Mathematischer Kern (Formeln, Konstruktionen, Analogien)

### Zeta als regularisierte Determinante
Deningers Leitformel (konjektural) drückt die vollständige Zetafunktion als zeta-regularisierte Determinanten eines Flusserzeugers Θ auf hypothetischen Kohomologiegruppen H^i aus:
```
ξ(s) "="  ∏_{i=0}^{2}  det_∞( (s·Id − Θ) / 2π | H^i(X̄, ·) )^{(−1)^{i+1}}.
```
Die regularisierte Determinante ist über die Spektral-Zeta definiert:
```
det_∞(A) = exp(−ζ_A'(0)),   ζ_A(z) = Σ_λ λ^{−z}  (λ Eigenwerte von A).
```
Beispiel-Konsistenz (archimedischer Faktor):
```
det_∞( (s − Θ)/2π | H ) liefert  Γ_ℝ(s) = π^{−s/2}Γ(s/2)  für den ∞-Faktor.
```

### Nullstellen = Eigenwerte (Hilbert–Pólya-Realisierung)
Die nicht-trivialen Nullstellen ρ wären die Eigenwerte von Θ auf H¹:
```
Spektrum(Θ | H¹) = { ρ : ξ(ρ) = 0 }.
```
RH ⟺ Θ hat (nach geeigneter Verschiebung um 1/2) **rein imaginäres** Spektrum, d. h. eine spektrale Symmetrie/Selbstadjungiertheit — eine geometrische Hilbert–Pólya-Aussage (Dok. 05).

### Lefschetz-Spurformel als explizite Formel
Für den Fluss φ^t mit Erzeuger Θ gilt (konjektural) eine Lefschetz-Spurformel
```
Σ_i (−1)^i Tr(φ^{t*} | H^i)  =  Σ_{γ geschl. Orbit}  (Länge ℓ(γ)) Σ_k δ(t − k ℓ(γ)) / |det(1 − D φ)|,
```
deren Auswertung **Weils explizite Formel** (Dok. 02) reproduziert: geschlossene Orbits ↔ Primzahlen, ℓ(γ) ↔ log p.

### Modell: gefolierte Räume
Da X für Spec(ℤ) fehlt, studiert Deninger **3-dimensionale gefolierte Mannigfaltigkeiten** (M, ℱ) mit einem Fluss transversal zur Blätterung. Die **reduzierte blattweise Kohomologie** H̄^•_ℱ trägt eine Θ-Wirkung mit den strukturellen Eigenschaften (Poincaré-Dualität, Lefschetz), die für den arithmetischen Fall gewünscht sind. Geschlossene Orbits des Flusses ↔ Primzahlen; ihre Längen ↔ log p.

### Status
Die Kohomologietheorie H^i für arithmetische Schemata **existiert nicht** (Flach–Morin formalisieren Teile als Weil-Arakelov-Kohomologie). Die Formeln sind ein konjekturaler Kompass, kein Beweis — aber sie erklären *strukturell*, warum RH = spektrale Symmetrie gelten sollte.

## Quellen
- [Arithmetic Geometry and Analysis on Foliated Spaces — C. Deninger (Arizona Winter School)](https://swc-math.github.io/dls/DLSDeninger.pdf)
- [Analogies between analysis on foliated spaces and arithmetic geometry (arXiv 0709.2801)](https://arxiv.org/pdf/0709.2801)
- [Deninger's conjectures and Weil-Arakelov cohomology — Flach & Morin](https://www.math.u-bordeaux.fr/~bmorin/Deninger-WA5.pdf)
- [Dynamical systems for arithmetic schemes — Deninger (ResearchGate)](https://www.researchgate.net/publication/381101198_Dynamical_systems_for_arithmetic_schemes)
- [The Riemann Hypothesis: Arithmetic and Geometry — J. Lagarias](https://websites.umich.edu/~lagarias//doc/mt-holyoke-rev.pdf)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `algebraic-geometric` |
> | Implikation | `conditional` |
> | Euler-Produkt | `essential` |
> | Positivität | `must-prove` |
> | Strenge | `program` |
> | Evidenz | `medium` |
> | Testbar | `low` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Den dynamischen Raum mit R-Fluss tatsächlich konstruieren (bisher nur axiomatisch gefordert).
> 
> **Hebel:** Formal perfekte Uebersetzung: Nullstellen = Eigenwerte des Flusses.
> 
> **Fehlermodi:** [[F10_analogy-transfer-gap|F10 Fehlende Geometrie über Spec(ℤ)]] · [[F2_positivity-assumed|F2 Zirkuläre Positivität]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-31`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Fehlende Geometrie über Spec(ℤ)** *(Tier 2)* — Der bewiesene Funktionenkörperfall braucht eine Fläche C×_𝔽 C; das Analogon Spec(ℤ)×_{𝔽₁}Spec(ℤ) existiert nicht.
>   *Fluchtbedingung:* Konstruktion einer Kohomologietheorie über Spec(ℤ) mit (a) Lefschetz-Formel, die die explizite Formel reproduziert, (b) Poincaré-Dualität, (c) einem Positivitäts-/Index-Satz (Hodge-Index-Analogon). Alle drei, nicht nur (a).
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (4)
> - *versucht Transfer von* → **Geometrie-Transfer (Funktionenkörper→ℤ)** — Deninger-Kohomologie.
> - *modelliert* → **Hilbert–Pólya / spektrale Interpretation** — Deninger: Frobenius-artiger Operator auf hypothetischer Kohomologie.
> - *benutzt* → **Explizite Formel (Primzahlen↔Nullstellen)** — Lefschetz-Spurformel = explizite Formel.
> - ← *wird benutzt von* [[72_Arakelov_geometry_SpecZ_compactification|72 · Arakelov-Geometrie & die Kompaktifizierung von Spec…]] — Deningers Fluss ersetzt den fehlenden Frobenius.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
