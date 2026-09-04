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

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Fehlende Geometrie über Spec(ℤ)** *(Tier 2)* — Der bewiesene Funktionenkörperfall braucht eine Fläche C×_𝔽 C; das Analogon Spec(ℤ)×_{𝔽₁}Spec(ℤ) existiert nicht.
>   *Fluchtbedingung:* Konstruktion einer Kohomologietheorie über Spec(ℤ) mit (a) Lefschetz-Formel, die die explizite Formel reproduziert, (b) Poincaré-Dualität, (c) einem Positivitäts-/Index-Satz (Hodge-Index-Analogon). Alle drei, nicht nur (a).
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (2)
> - *benutzt* → **Hilbert–Pólya / spektrale Interpretation** — Bost–Connes: Operator mit Spektrum {log n} (geometrische Seite).
> - ← *wird benutzt von* [[30_F1_field_one_element_arithmetic_site|30 · Der Körper mit einem Element]] — Bost–Connes liefert Galois-/Frobenius-Symmetrie fürs 𝔽₁-Programm.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
