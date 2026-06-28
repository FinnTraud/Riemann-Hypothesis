# Lindelöf-Hypothese & Dichte-Hypothese

**Kategorie:** Schwächere Konsequenzen / verwandte Hypothesen
**Autoren / Jahre:** Ernst Lindelöf (1908); Dichteabschätzungen Ingham, Huxley, Bourgain, Guth–Maynard
**Typ:** Aus RH folgende (schwächere) Hypothesen
**Status:** Beide offen; Teilfortschritte (Subkonvexität, Dichteschätzungen)

## Zusammenfassung
Lindelöf- und Dichte-Hypothese sind **Konsequenzen** der RH, die formal schwächer, aber ebenfalls ungelöst sind. Sie bilden eine Hierarchie:

```
RH  ⟹  Lindelöf-Hypothese  ⟹  Dichte-Hypothese
```

Ob umgekehrt die Lindelöf-Hypothese die RH impliziert, ist **unbekannt** (vermutlich nicht). Fortschritte hier liefern unbedingte (RH-unabhängige) Resultate.

## Lindelöf-Hypothese (1908)
- Aussage über das **Wachstum** von ζ auf der kritischen Geraden:

```
ζ(1/2 + it) = O(t^ε)   für jedes ε > 0   (t → ∞)
```

- Äquivalent über den **Lindelöf-μ-Exponenten**: μ(1/2) = 0, wobei μ(σ) das Infimum der Exponenten mit ζ(σ+it) = O(t^{μ(σ)+ε}) ist.
- **Stand der Subkonvexität:** Die konvexe Schranke gibt μ(1/2) ≤ 1/4; **Bourgain (2017)** verbesserte auf μ(1/2) ≤ **13/84** ≈ 0,1548 — weit entfernt vom vermuteten Wert 0. (Verwandt: Weyl, Hardy–Littlewood, van der Corput, Huxley 32/205.)
- Hinweis: Eine "Lindelöf-Hypothese für Primzahlen" wurde (2019/2020) als sogar *äquivalent* zur RH gezeigt — die Standard-Lindelöf-Hypothese bleibt aber schwächer.

## Dichte-Hypothese
- Aussage über die **Anzahl möglicher Nullstellen abseits** der kritischen Geraden. Mit N(σ,T) = Anzahl der Nullstellen mit Re ≥ σ und |Im| ≤ T:

```
N(σ, T) = O_ε( T^{2(1−σ) + ε} )   für 1/2 ≤ σ ≤ 1
```

- Unter RH gäbe es für σ > 1/2 gar keine solchen Nullstellen; die Dichte-Hypothese ist eine quantitative Abschwächung.
- **Fortschritte:** explizite log-freie Dichteabschätzungen (z. B. arXiv 2405.12545), Ingham, Huxley, und insbesondere der **Guth–Maynard-Durchbruch (2024)** für σ nahe 3/4 (Dok. 22).

## Bedeutung / Einordnung
- Dichteabschätzungen ersetzen die RH in vielen Anwendungen (Primzahlen in kurzen Intervallen, Primzahlen in arithmetischen Progressionen) — **unbedingt**, d. h. ohne RH anzunehmen.
- Wichtigste *praktische* Front: Selbst ohne RH-Beweis liefern bessere Dichte-/Subkonvexitätsschranken konkrete zahlentheoretische Resultate.

## Quellen
- [Lindelöf hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis)
- [An explicit log-free zero density estimate for the Riemann zeta-function (arXiv 2405.12545)](https://arxiv.org/pdf/2405.12545)
- [Explicit zero density for the Riemann zeta function (arXiv 2101.12263)](https://arxiv.org/pdf/2101.12263)
- [An explicit form of Ingham's zero density estimate (arXiv 2507.15184)](https://arxiv.org/pdf/2507.15184)
