---
id: doc-08
number: 08
title: "Berry–Keating H = xp Modell (Quantenchaos-Ansatz)"
category: spectral
status: open
tags: [berry-keating, xp-model, quantum-chaos, semiclassical]
source_file: 08_Berry_Keating_xp_model.md
lang: de
---

# Berry–Keating H = xp Modell (Quantenchaos-Ansatz)

**Kategorie:** Spektraler Ansatz / Quantenphysik
**Autoren / Jahr:** Michael Berry, Jonathan Keating (1999); Vorläufer & Varianten Sierra, Townsend u. a. (ab 2008/2011)
**Typ:** Physikalisches Operator-Modell (Hilbert–Pólya-Kandidat)
**Status:** Heuristisch; liefert nur geglättete Nullstellendichte, kein rigoroser Operator

## Zusammenfassung
Berry und Keating schlugen vor, dass die Riemann-Nullstellen die Energieniveaus (Eigenwerte) eines quantenmechanischen Operators sind, der aus der Quantisierung des klassischen Hamiltonians **H = xp** (Ort × Impuls) entsteht. Motiviert ist dies durch das **Quantenchaos**: In chaotischen Quantensystemen folgen die Energieniveaus GUE-Statistik — genau wie die ζ-Nullstellen (Dok. 06).

## Kernidee
- Klassischer Hamiltonian H = xp besitzt hyperbolische Trajektorien (instabil, "chaotisch").
- Eine semiklassische Quantisierung liefert eine mittlere Niveaudichte, die asymptotisch mit der **mittleren Dichte der Riemann-Nullstellen** N(T) ~ (T/2π)log(T/2π) übereinstimmt.
- **Berrys Quantenchaos-Vermutung:** Die Nullstellen sind das Spektrum eines Hamiltonians, dessen klassische periodische Bahnen durch die **Primzahlen** indiziert sind (periodische Orbits ↔ Primzahlen, Bahnlängen ↔ log p) — eine physikalische Lesart der expliziten Formel (Dok. 02).

## Bekannte Probleme
- Naive Quantisierung von H = xp liefert nur die **glatte/mittlere** Nullstellendichte, **nicht** die exakten Nullstellenpositionen.
- Das Spektrum ist **kontinuierlich** statt diskret, solange keine geeignete Regularisierung / Randbedingung gewählt wird.
- Verschiedene Regularisierungen:
  - **Berry–Keating:** diskretes Spektrum, das die *geglätteten* Nullstellen approximiert.
  - **Connes:** Absorptionsspektrum — die Nullstellen erscheinen als *fehlende* Spektrallinien (Dok. 10).
  - **Sierra & Townsend (2011):** Modelle H = x(p + 1/p) bzw. H = (x + 1/x)(p + 1/p), die ein diskretes Spektrum mit der glatten Nullstellen-Zählfunktion erzeugen.

## Bedeutung / Einordnung
- Konkreteste *physikalische* Verkörperung des Hilbert–Pólya-Gedankens.
- Verbindet Primzahlen ↔ periodische Orbits ↔ Spektrallinien.
- **Stand 2026:** Keine Konstruktion liefert die *exakten* Nullstellen als Eigenwerte eines rigoros definierten selbstadjungierten Operators — nur geglättete/statistische Übereinstimmung. Damit kein vollständiger RH-Beweis.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Klassisches H = xp und semiklassische Niveauzählung
Klassischer Hamiltonian H = x·p hat hyperbolische Trajektorien x p = E (Hyperbeln im Phasenraum). Die semiklassische Anzahl der Zustände mit Energie ≤ E ist das Phasenraumvolumen / (2πℏ):
```
N_{sc}(E) = (1/2πℏ) · Vol{ (x,p) : 0 < x p < E, mit Cutoffs x ≥ ℓ_x, p ≥ ℓ_p }
```
Mit Abschneidungen x ≥ l_x, p ≥ l_p (Cutoffs l_x l_p = 2πℏ) ergibt sich
```
N_{sc}(E) = (E/2πℏ)( log(E/2πℏ) − 1 ) + 7/8 + …
```

### Übereinstimmung mit der Riemann-Zählfunktion
Vergleiche mit dem glatten Teil von N(T) (Dok. 02):
```
⟨N(E)⟩ = (E/2π) log(E/2π) − E/2π + 7/8 + …
```
Setzt man ℏ = 1, so stimmen **glatter Term inklusive der Konstante 7/8** überein! Das ist die zentrale Beobachtung von Berry–Keating: H = xp reproduziert die mittlere Nullstellendichte exakt.

### Fehlende Teile (warum nur „glatt")
- Die fluktuierende Korrektur N(E) − ⟨N(E)⟩ = S(E)/π (Dok. 02) entspräche in der Gutzwiller-Spurformel einer Summe über periodische Orbits:
```
N_{fl}(E) ≈ (1/π) Σ_p Σ_{r≥1} (1/r) (Λ(p^r)/p^{r/2}) sin(r E log p)
```
— formal identisch zur expliziten Formel mit Primzahlen p als „Orbits" der Periode log p. Aber: das nackte H = xp hat **keine** periodischen Orbits (Trajektorien laufen ins Unendliche) ⇒ Spektrum kontinuierlich, Fluktuationsterm fehlt.
- Abhilfe durch Modifikation (Sierra–Townsend 2011):
```
H = x(p + ℓ_p²/p)   bzw.   H = (x + ℓ_x²/x)(p + ℓ_p²/p)
```
erzeugt gebundene, diskrete Spektren, die die geglätteten Nullstellen approximieren; die *exakten* γ_n bleiben unerreicht.

### Connes-Regularisierung (Kontrast)
Connes' adelische Version (Dok. 10) liefert statt eines diskreten Emissionsspektrums ein **Absorptionsspektrum**: die γ_n erscheinen als *Lücken* (fehlende Linien) im Kontinuum — formal Spur über den Adèleklassenraum mit der expliziten Formel als Spurformel.

## Quellen
- [H = xp and the Riemann Zeros — Berry & Keating (Springer)](https://link.springer.com/chapter/10.1007/978-1-4615-4875-1_19)
- [The Riemann zeros as spectrum and the Riemann hypothesis (arXiv 1601.01797)](https://arxiv.org/pdf/1601.01797)
- [General covariant xp models and the Riemann zeros (arXiv 1110.3203)](https://arxiv.org/pdf/1110.3203)
- [H = xp with interaction and the Riemann zeros (arXiv math-ph/0702034)](https://arxiv.org/pdf/math-ph/0702034)
- [Landau levels and Riemann zeros (arXiv 0805.4079)](https://arxiv.org/pdf/0805.4079)
