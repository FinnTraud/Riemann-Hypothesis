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

## Quellen
- [H = xp and the Riemann Zeros — Berry & Keating (Springer)](https://link.springer.com/chapter/10.1007/978-1-4615-4875-1_19)
- [The Riemann zeros as spectrum and the Riemann hypothesis (arXiv 1601.01797)](https://arxiv.org/pdf/1601.01797)
- [General covariant xp models and the Riemann zeros (arXiv 1110.3203)](https://arxiv.org/pdf/1110.3203)
- [H = xp with interaction and the Riemann zeros (arXiv math-ph/0702034)](https://arxiv.org/pdf/math-ph/0702034)
- [Landau levels and Riemann zeros (arXiv 0805.4079)](https://arxiv.org/pdf/0805.4079)
