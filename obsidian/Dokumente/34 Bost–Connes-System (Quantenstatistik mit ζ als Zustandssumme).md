---
id: doc-34
title: "Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)"
nummer: "34"
kategorie: Spektrale Ansätze
status: BEWIESEN
typ: dokument
aliases:
  - "doc-34"
  - "Dok. 34"
tags:
  - "dokument"
  - "kategorie/spectral"
  - "status/proven"
  - "thema/bost-connes"
  - "thema/kms-states"
  - "thema/partition-function"
  - "thema/phase-transition"
  - "thema/quantum-statistical"
quelle: docs/34_Bost_Connes_system.md
---

> [!info] Navigation
> **Karte:** [[MOC L – Weitere aktive Lösungsprogramme (potenziell beweisrelevant)]] · **Kategorie:** Spektrale Ansätze · **Status:** `BEWIESEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/34_Bost_Connes_system.md`

# Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)

**Kategorie:** Spektraler/algebraischer Ansatz (Quantenstatistische Mechanik)
**Autoren / Jahr:** Jean-Benoît Bost & Alain Connes (1995); Verallgemeinerungen Connes–Marcolli, Laca–Raeburn u. a.
**Typ:** C*-dynamisches System mit arithmetischer Symmetrie
**Status:** Bewiesenes Phasenübergangsphänomen; kein direkter RH-Beweis, aber strukturell zentral für das 𝔽₁/NCG-Programm

## Zusammenfassung
Das Bost–Connes-System ist ein **quantenstatistisches dynamisches System**, dessen **Zustandssumme (partition function) exakt die Riemannsche ζ-Funktion** ist und dessen Symmetrien die **abelsche Galoisgruppe** Gal(ℚ^ab/ℚ) realisieren. Es verbindet Quantenstatistik, Klassenkörpertheorie und die ζ-Funktion und ist ein Schlüsselbaustein von Connes' nichtkommutativem Programm (Dok. [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]]) und der 𝔽₁-Geometrie (Dok. [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site|30]]).

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
- **Wichtig:** Dieses H hat Spektrum {log n} (Primzahlen/ganze Zahlen), **nicht** {γ_n} (Nullstellen). Es ist also *nicht* direkt der gesuchte Hilbert–Pólya-Operator (Dok. [[05 Die Hilbert–Pólya-Vermutung (spektraler Ansatz)|05]]), sondern realisiert die *geometrische* Seite. Der Übergang zur spektralen Seite (Nullstellen) ist genau Connes' Spurformel-Schritt (Dok. [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]]).
- Strukturelles Fundament für 𝔽₁ (Dok. [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site|30]]): das System trägt die Galois-/Frobenius-Symmetrie, die man für ein „Spec(ℤ) über 𝔽₁" braucht.

## Quellen
- [Bost–Connes system — Wikipedia](https://en.wikipedia.org/wiki/Bost%E2%80%93Connes_system)
- [The dynamical system problem studied by Bost–Connes — AIM](https://aimath.org/WWN/rh/articles/html/101a/)
- [Bost–Connes Systems in Arithmetic and Quantum Theory — Emergent Mind](https://www.emergentmind.com/topics/bost-connes-systems)
- [Dedekind Zeta Functions and Quantum Statistical Mechanics (ESI preprint 617)](https://www.esi.ac.at/preprints/esi617.pdf)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **nutzt** → [[Hilbert–Pólya ∕ spektrale Interpretation]] — *Bost–Connes: Operator mit Spektrum {log n} (geometrische Seite).*

### Eingehende Relationen

- **wird genutzt von** ← [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site]] — *Bost–Connes liefert Galois-/Frobenius-Symmetrie fürs 𝔽₁-Programm.*

### Im Text erwähnt

- [[05 Die Hilbert–Pólya-Vermutung (spektraler Ansatz)]]
- [[10 Alain Connes – Spurformel & nichtkommutative Geometrie]]
