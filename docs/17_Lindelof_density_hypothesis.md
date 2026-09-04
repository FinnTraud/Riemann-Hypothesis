---
id: doc-17
number: 17
title: "Lindelöf-Hypothese & Dichte-Hypothese"
category: analytic
status: open
tags: [lindelof, density-hypothesis, subconvexity, mu-exponent]
source_file: 17_Lindelof_density_hypothesis.md
lang: de
---

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

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Der μ-Exponent
Definiere μ(σ) = inf{ a ≥ 0 : ζ(σ + it) = O(|t|^a) }. Bekannt:
- μ(σ) = 0 für σ > 1; μ(σ) = 1/2 − σ für σ < 0 (aus Funktionalgleichung + Stirling).
- μ ist konvex und nicht-wachsend. Konvexitätsschranke (Phragmén–Lindelöf): μ(1/2) ≤ 1/4.

### Lindelöf-Hypothese
```
LH:  μ(1/2) = 0,   d. h.  ζ(1/2 + it) = O(|t|^ε)  ∀ε > 0.
```
**Subkonvexitäts-Fortschritte (jeweils μ(1/2) ≤ …):** Weyl/Hardy–Littlewood 1/6 ≈ 0,1667; van der Corput; Titchmarsh; Huxley 32/205 ≈ 0,15610; **Bourgain (2017) 13/84 ≈ 0,15476**. Ziel 0.

### Äquivalenz LH ⟺ Momentenwachstum
```
LH  ⟺  (1/T)∫_0^T |ζ(1/2+it)|^{2k} dt = O(T^ε)  für jedes feste k ≥ 1.
```
(vgl. Keating–Snaith (log T)^{k²}, Dok. 07 — verträglich, da T^ε jedes log-Potenzwachstum dominiert.)

### Hierarchie und Implikationen
```
RH  ⟹  LH  ⟹  Dichte-Hypothese (DH).   (Rückrichtungen unbekannt.)
```
Beweis RH ⇒ LH: Unter RH gilt log|ζ(1/2+it)| ≤ (c log t)/log log t, also ζ(1/2+it) = O(exp(c log t/log log t)) = O(t^ε).

### Dichte-Hypothese
Mit N(σ,T) = #{ρ = β+iγ : β ≥ σ, 0 < γ ≤ T}:
```
DH:  N(σ, T) ≪_ε T^{2(1−σ) + ε}   für  1/2 ≤ σ ≤ 1.
```
Klassisch (Ingham 1940): N(σ,T) ≪ T^{3(1−σ)/(2−σ)+ε}. **Log-freie** Form: N(σ,T) ≪ A·T^{B(1−σ)}. Guth–Maynard (2024, Dok. 22) verbessern den Exponenten nahe σ = 3/4 (N(3/4,T) ≪ T^{13/25+o(1)} statt T^{3/5+o(1)}).

### Warum DH praktisch reicht
Für Primzahlen in kurzen Intervallen [x, x+x^θ] genügt eine hinreichend starke Dichteabschätzung (statt RH), um asymptotische Primzahlzählung zu sichern — Grund, warum Dichteresultate *unbedingte* zahlentheoretische Anwendungen haben.

## Quellen
- [Lindelöf hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis)
- [An explicit log-free zero density estimate for the Riemann zeta-function (arXiv 2405.12545)](https://arxiv.org/pdf/2405.12545)
- [Explicit zero density for the Riemann zeta function (arXiv 2101.12263)](https://arxiv.org/pdf/2101.12263)
- [An explicit form of Ingham's zero density estimate (arXiv 2507.15184)](https://arxiv.org/pdf/2507.15184)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `analytic` |
> | Implikation | `partial` |
> | Euler-Produkt | `essential` |
> | Positivität | `n/a` |
> | Strenge | `theorem` |
> | Evidenz | `medium` |
> | Testbar | `medium` |
> | Formalisierbar | `medium` |
> 
> **Offener Kernschritt:** Lindelöf folgt aus RH, impliziert sie aber nicht; selbst Lindelöf ist offen.
> 
> **Hebel:** Realistisches Zwischenziel mit messbarem Fortschritt (Exponenten).
> 
> **Fehlermodi:** [[F13_error-term-ceiling|F13 Anteils-Decke der Mollifier-Methoden]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-17`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Anteils-Decke der Mollifier-Methoden** *(Tier 2)* — Levinson/Conrey-Technik liefert einen positiven Anteil, ist aber strukturell weit unter 100 % gedeckelt.
>   *Fluchtbedingung:* Ein Mechanismus, der ALLE Nullstellen erfasst statt einen Anteil — Anteilsmethoden können die RH prinzipiell nicht abschließen, auch nicht im Limes.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (5)
> - *schwächer als* → **Riemann-Vermutung (RH)** — Lindelöf ist schwächer; Rückrichtung unbekannt.
> - ← *gestützt durch* [[49_live_analytic_frontier|49 · Live-Front der analytischen Zahlentheorie]] — Subkonvexität nähert Lindelöf an.
> - ← *gestützt durch* [[75_extreme_values_FHK_multiplicative_chaos|75 · Extremwerte von ζ]] — Extremwert-Schranken kalibrieren Lindelöf.
> - ← *wird impliziert von* **Riemann-Vermutung (RH)** — RH ⇒ Lindelöf-Hypothese.
> - ← *wird benutzt von* [[22_Guth_Maynard_2024|22 · Guth–Maynard]] — Guth–Maynard verbessert Dichte-Abschätzungen Richtung Dichte-Hypothese.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
