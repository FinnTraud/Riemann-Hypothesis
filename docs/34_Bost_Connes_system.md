---
id: doc-34
number: 34
title: "Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)"
category: spectral
status: proven
tags: [bost-connes, KMS-states, phase-transition, partition-function, quantum-statistical]
source_file: 34_Bost_Connes_system.md
lang: de
---

# Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)

**Kategorie:** Spektraler/algebraischer Ansatz (Quantenstatistische Mechanik)
**Autoren / Jahr:** Jean-Benoît Bost & Alain Connes (1995); Verallgemeinerungen Connes–Marcolli, Laca–Raeburn u. a.
**Typ:** C*-dynamisches System mit arithmetischer Symmetrie
**Status:** Bewiesenes Phasenübergangsphänomen; kein direkter RH-Beweis, aber strukturell zentral für das 𝔽₁/NCG-Programm

## Zusammenfassung
Das Bost–Connes-System ist ein **quantenstatistisches dynamisches System**, dessen **Zustandssumme (partition function) exakt die Riemannsche ζ-Funktion** ist und dessen Symmetrien die **abelsche Galoisgruppe** Gal(ℚ^ab/ℚ) realisieren. Es verbindet Quantenstatistik, Klassenkörpertheorie und die ζ-Funktion und ist ein Schlüsselbaustein von Connes' nichtkommutativem Programm (Dok. 10) und der 𝔽₁-Geometrie (Dok. 30).

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Konstruktion
Eine C*-Algebra A mit einer Ein-Parameter-Gruppe von Automorphismen σ_t (Zeitentwicklung), erzeugt von einem Hamiltonian H mit Spektrum {log n : n ≥ 1}:
```
H e_n = (log n) e_n,   σ_t(a) = e^{itH} a e^{−itH}.
```
Die **Zustandssumme** bei inverser Temperatur β:
```
Z(β) = Tr(e^{−βH}) = Σ_{n=1}^∞ e^{−β log n} = Σ_{n=1}^∞ n^{−β} = ζ(β).
```

### KMS-Zustände und Phasenübergang
Gleichgewichtszustände sind die **KMS_β-Zustände** (Kubo–Martin–Schwinger). **Satz (Bost–Connes 1995):**
- Für **β ≤ 1** (hohe Temperatur): ein **eindeutiger** KMS-Zustand (symmetrische Phase).
- Für **β > 1** (tiefe Temperatur): **mehrere** extremale KMS-Zustände; ihre Zustandssumme ist ζ(β), und die Galoisgruppe Gal(ℚ^ab/ℚ) ≅ Ẑ* wirkt **frei transitiv** auf ihnen.
- **Phasenübergang bei β = 1** — genau am Pol von ζ.

### Arithmetische Symmetrie
Auf den Grundzuständen (β → ∞) wirkt die absolute abelsche Galoisgruppe; die Werte des Zustands auf bestimmten Elementen erzeugen den maximalen abelschen Körper ℚ^ab (Kronecker–Weber: Kreisteilungskörper). Das System „kennt" also die explizite Klassenkörpertheorie von ℚ.

### Verallgemeinerung (Dedekind-ζ)
Für einen Zahlkörper K liefert das Connes–Marcolli-System die **Dedekind-Zetafunktion** ζ_K als Zustandssumme; KMS-Zustände kodieren die Klassenkörpertheorie von K.

## Bedeutung / Einordnung für die RH
- Liefert eine **natürliche thermodynamische Realisierung** von ζ — ζ erscheint als Zustandssumme eines konkreten Operators H mit Spektrum {log n}.
- **Wichtig:** Dieses H hat Spektrum {log n} (Primzahlen/ganze Zahlen), **nicht** {γ_n} (Nullstellen). Es ist also *nicht* direkt der gesuchte Hilbert–Pólya-Operator (Dok. 05), sondern realisiert die *geometrische* Seite. Der Übergang zur spektralen Seite (Nullstellen) ist genau Connes' Spurformel-Schritt (Dok. 10).
- Strukturelles Fundament für 𝔽₁ (Dok. 30): das System trägt die Galois-/Frobenius-Symmetrie, die man für ein „Spec(ℤ) über 𝔽₁" braucht.

## Quellen
- [Bost–Connes system — Wikipedia](https://en.wikipedia.org/wiki/Bost%E2%80%93Connes_system)
- [The dynamical system problem studied by Bost–Connes — AIM](https://aimath.org/WWN/rh/articles/html/101a/)
- [Bost–Connes Systems in Arithmetic and Quantum Theory — Emergent Mind](https://www.emergentmind.com/topics/bost-connes-systems)
- [Dedekind Zeta Functions and Quantum Statistical Mechanics (ESI preprint 617)](https://www.esi.ac.at/preprints/esi617.pdf)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_spectral|Spektrale Ansätze]]

| Achse | Wert |
|---|---|
| Familie | spectral |
| Implikation | `model` |
| Euler-Produkt | `essential` |
| Positivität | `n/a` |
| Strenge | `theorem` · Evidenz `medium` |
| Testbar / formalisierbar | `low` / `low` |

**Offener Kernschritt:** Der Phasenübergang kodiert die Klassenkörpertheorie, nicht die Nullstellenlage.

**Hebel (was er liefern würde):** ζ als Zustandssumme - konzeptuell schönste Realisierung.

**Typische Fehlermodi:** [[F14_model-without-implication|F14 Modell ohne Implikationspfeil]] · [[F10_analogy-transfer-gap|F10 Analogie ohne Trägerobjekt (Geometrie-Transfer)]]

**Vergleichbar mit:** [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)]] · [[58_Mobius_randomness_Chowla_Sarnak|Möbius-Zufälligkeit: Chowla-Vermutung, Sarnak-Disjunktheit & die Paritätsbarriere]] · [[59_Langlands_functoriality_automorphic|Langlands-Funktorialität & automorphe L-Funktionen: Weg zur GRH?]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-34 doc-53 doc-58 doc-59`

**Ausgehende Beziehungen**
- *benutzt* (`uses`) → [[concept_hilbert-polya|Hilbert–Pólya / spektrale Interpretation]] — Bost–Connes: Operator mit Spektrum {log n} (geometrische Seite).

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[30_F1_field_one_element_arithmetic_site|30 — Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site]] — Bost–Connes liefert Galois-/Frobenius-Symmetrie fürs 𝔽₁-Programm.
- *ist Blaupause für* (`blueprint_for`) → [[62_Tate_thesis_adelic_analysis|62 — Tates These & adelische Analysis: warum die Funktionalgleichung „billig\" ist]] — Bost–Connes lebt auf demselben adelischen Objekt.

**Thematisch benachbart (gemeinsame Tags):** [[30_F1_field_one_element_arithmetic_site|Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
