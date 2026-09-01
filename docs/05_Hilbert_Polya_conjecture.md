---
id: doc-05
number: 05
title: "Die Hilbert–Pólya-Vermutung (spektraler Ansatz)"
category: spectral
status: open
tags: [hilbert-polya, self-adjoint-operator, spectral]
source_file: 05_Hilbert_Polya_conjecture.md
lang: de
---

# Die Hilbert–Pólya-Vermutung (spektraler Ansatz)

**Kategorie:** Spektraler Ansatz (Dachprogramm)
**Autoren / Jahr:** David Hilbert, George Pólya (um 1912–1914, mündlich überliefert)
**Typ:** Strategische Leitvermutung
**Status:** Offen; kein passender Operator konstruiert

## Zusammenfassung
Die Hilbert–Pólya-Vermutung besagt: Die Imaginärteile γ der nicht-trivialen Nullstellen ρ = 1/2 + iγ der Zetafunktion sind die **Eigenwerte eines selbstadjungierten (hermiteschen) Operators**. Da selbstadjungierte Operatoren stets *reelle* Eigenwerte besitzen, würde die Existenz eines solchen Operators (richtig an ζ gekoppelt) sofort bedeuten, dass alle γ reell sind — also alle Nullstellen auf Re(s) = 1/2 liegen. Damit wäre die RH bewiesen.

## Kernidee
- Schreibe ρ = 1/2 + iγ. Die RH ist äquivalent zur Aussage: **alle γ sind reell**.
- Finde einen Hilbertraum und einen selbstadjungierten Operator H, dessen Spektrum genau die Menge {γ} ist. Selbstadjungiertheit ⇒ reelles Spektrum ⇒ RH.
- Pólya (um 1913) vermutete, die Nullstellen seien Eigenwerte eines natürlich auftretenden, unbeschränkten selbstadjungierten Operators; Hilbert prägte den Begriff "Spektrum" für die Eigenwerte eines äquivalenten hermiteschen Operators.

## Status & Ausprägungen
- **Kein** solcher Operator wurde für die echten ζ-Nullstellen rigoros konstruiert — das ist *die* zentrale offene strategische Frage des Feldes.
- Indirekte Evidenz: Die statistische Verteilung der Nullstellen passt exakt zu Eigenwert-Statistiken großer Zufallsmatrizen (GUE), was mit der Existenz eines "chaotischen" selbstadjungierten Operators konsistent ist (siehe Dok. 06).
- Konkrete Operator-Kandidaten / Teil-Realisierungen:
  - **Berry–Keating H = xp** Modell (Dok. 08).
  - **Bender–Brody–Müller** PT-symmetrischer Hamiltonian (Dok. 09).
  - **Connes'** spektrale Realisierung in der nichtkommutativen Geometrie (Dok. 10).
  - **Connes–Moscovici** Prolate-Spheroidal-Operator als "konkrete annähernde Lösung der Hilbert–Pólya-Vermutung" (Dok. 11).

## Bedeutung / Einordnung
- Liefert den vielleicht meistverfolgten *strategischen* Rahmen für einen RH-Beweis.
- Verbindet Zahlentheorie mit Funktionalanalysis, Quantenphysik und Quantenchaos.
- Schwäche: Statistische Übereinstimmung (GUE) ist *Evidenz*, kein Beweismechanismus — ein tatsächlicher Operator fehlt.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Präzise Formulierung
Schreibe die nicht-trivialen Nullstellen als ρ_n = 1/2 + i γ_n. Gesucht ist ein Hilbertraum H und ein **selbstadjungierter Operator** Ĥ (unbeschränkt) mit
```
Ĥ ψ_n = γ_n ψ_n
```
für ein vollständiges System von Eigenfunktionen ψ_n. Da Ĥ = Ĥ* selbstadjungiert ist, gilt Spektrum(Ĥ) ⊂ ℝ, also γ_n ∈ ℝ für alle n. Wegen ξ(ρ) = 0 und ξ(s) = ξ(1−s), ξ(s)=ξ(s̄) ist γ_n ∈ ℝ **äquivalent** zu Re(ρ_n) = 1/2. Damit:
```
(∃ selbstadj. Ĥ mit Spektrum {γ_n})  ⟹  RH
```

### Warum „selbstadjungiert" der Schlüssel ist
Für einen symmetrischen Operator garantiert erst die **Selbstadjungiertheit** (gleiche Defektindizes, reeller Spektralsatz) ein reelles Spektrum. Hermitesche Form: ⟨Ĥψ, φ⟩ = ⟨ψ, Ĥφ⟩ ⇒ Eigenwerte reell, Eigenfunktionen zu verschiedenen Eigenwerten orthogonal. Genau diese Reellheit „erzwingt" die kritische Gerade.

### Verbindung zur Spurformel (Heuristik)
Gäbe es Ĥ, so verbände eine Spurformel die Spektralsumme mit einer geometrischen Summe:
```
Σ_n h(γ_n) = (glatter Term) + Σ_{periodische Orbits p} (Beitrag mit Länge log p)
```
Vergleich mit Weils expliziter Formel (Dok. 02) ⇒ die „periodischen Orbits" entsprechen den Primzahlen, Längen = log p. Das ist die strukturelle Brücke, die Berry–Keating (Dok. 08), Connes (Dok. 10) und Deninger (Dok. 31) konkret zu realisieren versuchen.

### Pólyas analytischer Vorläufer (Laguerre–Pólya)
Eine dazu äquivalente, operatorfreie Fassung (Dok. 29): RH ⟺ ξ liegt in der **Laguerre–Pólya-Klasse** (ganze Funktionen mit nur reellen Nullstellen, Grenzwerte von Polynomen ∏(1 − x/x_k) mit x_k ∈ ℝ). „Reelles Spektrum" und „reelle Nullstellen von ξ" sind dieselbe Aussage in zwei Sprachen.

## Quellen
- [Hilbert–Pólya conjecture — Wikipedia](https://en.wikipedia.org/wiki/Hilbert%E2%80%93P%C3%B3lya_conjecture)
- [The Riemann zeros as spectrum and the Riemann hypothesis (arXiv 1601.01797)](https://arxiv.org/pdf/1601.01797)
- [On Hilbert-Polya conjecture: Hermitian operator naturally associated to L-functions (arXiv 1105.1500)](https://arxiv.org/pdf/1105.1500)
- [The Hilbert-Pólya Conjecture and the Prolate Spheroidal Operator (TU Delft)](https://repository.tudelft.nl/file/File_a03b023e-2ba7-45fb-bde9-6fcc7a53d306)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_spectral|Spektrale Ansätze]]

| Achse | Wert |
|---|---|
| Familie | spectral |
| Implikation | `conditional` |
| Euler-Produkt | `partial` |
| Positivität | `must-prove` |
| Strenge | `program` · Evidenz `strong` |
| Testbar / formalisierbar | `low` / `low` |

**Offener Kernschritt:** Einen kanonisch aus der Arithmetik stammenden Operator konstruieren, dessen Selbstadjungiertheit unabhängig beweisbar ist.

**Hebel (was er liefern würde):** Würde RH sofort liefern; erklärt die GUE-Statistik.

**Typische Fehlermodi:** [[F3_non-canonical-operator|F3 Operator ad hoc konstruiert (nicht kanonisch aus der Arithmetik)]] · [[F4_no-selfadjoint-realization|F4 Keine rigorose selbstadjungierte Realisierung (Definitionsbereich fehlt)]]

**Vergleichbar mit:** [[08_Berry_Keating_xp_model|Berry–Keating H = xp Modell (Quantenchaos-Ansatz)]] · [[10_Connes_noncommutative_geometry|Alain Connes: Spurformel & nichtkommutative Geometrie]] · [[48_Meyer_Kurokawa_algebraic_programs|Weitere algebraische/spektrale Programme: Meyer (Distributionen) & Kurokawa (absolute Zeta)]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-05 doc-08 doc-10 doc-48`

**Ausgehende Beziehungen**
- *ist Instanz von* (`instance_of`) → [[concept_hilbert-polya|Hilbert–Pólya / spektrale Interpretation]] — Hilbert–Pólya-Vermutung selbst.

**Thematisch benachbart (gemeinsame Tags):** [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)]] · [[41_synthesis_what_a_proof_needs|Synthese: Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
