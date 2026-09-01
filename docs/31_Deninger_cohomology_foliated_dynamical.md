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

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_algebraic_geometric|Algebraisch-geometrische Ansätze]]

| Achse | Wert |
|---|---|
| Familie | algebraic-geometric |
| Implikation | `conditional` |
| Euler-Produkt | `essential` |
| Positivität | `must-prove` |
| Strenge | `program` · Evidenz `medium` |
| Testbar / formalisierbar | `low` / `low` |

**Offener Kernschritt:** Den dynamischen Raum mit R-Fluss tatsächlich konstruieren (bisher nur axiomatisch gefordert).

**Hebel (was er liefern würde):** Formal perfekte Uebersetzung: Nullstellen = Eigenwerte des Flusses.

**Typische Fehlermodi:** [[F10_analogy-transfer-gap|F10 Analogie ohne Trägerobjekt (Geometrie-Transfer)]] · [[F2_positivity-assumed|F2 Positivität angenommen statt bewiesen]]

**Vergleichbar mit:** [[30_F1_field_one_element_arithmetic_site|Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site]] · [[10_Connes_noncommutative_geometry|Alain Connes: Spurformel & nichtkommutative Geometrie]] · [[59_Langlands_functoriality_automorphic|Langlands-Funktorialität & automorphe L-Funktionen: Weg zur GRH?]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-31 doc-30 doc-10 doc-59`

**Ausgehende Beziehungen**
- *modelliert* (`models`) → [[concept_hilbert-polya|Hilbert–Pólya / spektrale Interpretation]] — Deninger: Frobenius-artiger Operator auf hypothetischer Kohomologie.
- *versucht Transfer von* (`attempts_transfer_of`) → [[concept_geometry-transfer|Geometrie-Transfer (Funktionenkörper→ℤ)]] — Deninger-Kohomologie.
- *benutzt* (`uses`) → [[concept_explicit-formula|Explizite Formel (Primzahlen↔Nullstellen)]] — Lefschetz-Spurformel = explizite Formel.

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[61_Arakelov_geometry_SpecZ_compactification|61 — Arakelov-Geometrie & die Kompaktifizierung von Spec ℤ]] — Deningers Fluss ersetzt den fehlenden Frobenius.

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
