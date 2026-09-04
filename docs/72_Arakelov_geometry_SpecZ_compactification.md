---
id: doc-72
number: 72
title: "Arakelov-Geometrie & die Kompaktifizierung von Spec ℤ"
category: solution-program
status: open
tags: [arakelov, arithmetic-surface, hodge-index, faltings, hriljac, spec-z, archimedean-place, soule]
source_file: 72_Arakelov_geometry_SpecZ_compactification.md
lang: de
---

# Arakelov-Geometrie & die Kompaktifizierung von Spec ℤ

**Kategorie:** Aktives Programm (arithmetische Geometrie) — Infrastruktur für den Geometrie-Transfer
**Autoren / Jahre:** Arakelov (1974); Faltings (1984); Hriljac (1985); Gillet–Soulé (1990er); Soulé, Durov, Connes–Consani (𝔽₁-Anbindung)
**Typ:** „Geometrisierung" der ganzen Zahlen inkl. der unendlichen Stelle
**Status:** Theorie etabliert & mächtig (Faltings-Beweis der Mordell-Vermutung); **RH daraus nicht ableitbar** — der Grund ist strukturell benennbar

## Zusammenfassung
Arakelov-Geometrie behandelt `Spec ℤ` als „Kurve", die man durch Hinzunahme der **archimedischen Stelle** ∞ kompaktifiziert: Primzahlen sind die endlichen Punkte, die reelle Einbettung liefert den Punkt im Unendlichen, und hermitesche Metriken auf Vektorbündeln ersetzen dort die fehlende Faser. Damit existiert eine echte Schnitttheorie mit Riemann–Roch und **Hodge-Index-Satz**. Genau das ist die Zutat, die nach Dok. 71 die RH im geometrischen Fall erzeugt — und dennoch bekommt man die RH nicht. Dieses Dokument sagt präzise, warum.

## Mathematischer Kern

### Arakelov-Divisoren
Ein Arakelov-Divisor auf `\overline{Spec ℤ}` ist ein formales Paar
```
D = Σ_p n_p · [p]  +  x_∞ · [∞],     n_p ∈ ℤ,  x_∞ ∈ ℝ,
```
mit Grad
```
deg(D) = Σ_p n_p log p  +  x_∞.
```
Ein hermitesches Geradenbündel auf Spec ℤ ist ein Paar (L, ‖·‖) mit L ≅ ℤ als Modul und einer Norm auf L ⊗ ℝ; `deg` ist wohldefiniert und Hauptdivisoren haben Grad 0 (**Produktformel** `Σ_v log|x|_v = 0`) — die exakte Analogie zu „Grad eines Hauptdivisors auf einer projektiven Kurve ist 0".

### Arithmetische Flächen und der arithmetische Hodge-Index-Satz
Für ein arithmetisches Flächenmodell 𝒳 → Spec 𝒪_K einer Kurve X/K definierte Arakelov eine Schnittzahl `(\overline{D} · \overline{E})` (endliche Beiträge + Green-Funktionen an ∞). **Satz (Faltings, Hriljac).** Auf der Untergruppe der Divisoren vom Grad 0, modulo Fasern, gilt
```
(\overline{D} · \overline{D})  =  − 2 · h_{NT}(cl(D))   ≤ 0,
```
mit der **Néron–Tate-Höhe** h_{NT} ≥ 0 — also ein **arithmetischer Hodge-Index-Satz** (negative Definitheit auf dem primitiven Teil). Die Positivitätsaussage aus Dok. 71 **existiert** in der arithmetischen Welt. Faltings/Vojta nutzten diesen Apparat für die Mordell-Vermutung — die Theorie ist also beweiskräftig.

### Warum daraus nicht die RH folgt (die drei Lücken)
1. **Dimension.** `\overline{Spec ℤ}` ist ein arithmetisches **Kurven**-Analogon (Dimension 1). Weils Beweis lebt auf der **Fläche** C × C. Das Produkt `Spec ℤ ×_{Spec ℤ} Spec ℤ = Spec ℤ` ist trivial; man bräuchte ein Produkt über einer **absoluten Basis** — das ist genau die 𝔽₁-Frage (Dok. 30). Ohne zweite Dimension gibt es keine Korrespondenzen, keine Diagonale, keinen Graphen eines Frobenius.
2. **Kein Frobenius.** Es gibt keine kanonische Selbstabbildung von Spec ℤ, deren Fixpunkte die Primzahlen zählen. Deningers Programm (Dok. 31) postuliert stattdessen einen ℝ-**Fluss** auf einem gefolierten Raum; Connes' Skalierungswirkung (Dok. 10) ist die analytische Version derselben Idee.
3. **Die archimedische Faser ist keine Varietät.** Die Stelle ∞ wird durch Analysis (Green-Funktionen, hermitesche Metriken) *ersetzt*, nicht durch Geometrie *realisiert*. Genau an dieser Stelle sitzt in der expliziten Formel (Dok. 02) der Γ-Faktor-Term — und genau er ist es, der in Connes' Spurformel den Positivitätsdefekt trägt. Arakelov löst das archimedische Problem für Höhen, nicht für Spektren.

### Ansätze, die trotzdem hier ansetzen
- **Gillet–Soulé, arithmetisches Riemann–Roch**: vollständige Indexformel für arithmetische Schemata — Kandidat für eine „arithmetische Lefschetz-Formel", bisher ohne RH-Konsequenz.
- **Soulés Programm zu 𝔽₁**: Definition von Varietäten über 𝔽₁ mit dem Ziel, `Spec ℤ ×_{𝔽₁} Spec ℤ` überhaupt zu definieren (Dok. 30).
- **Durov, Toën–Vaquié, Connes–Consani (arithmetic site)**: konkrete Kandidaten für die absolute Basis; Connes–Consani zeigten, dass die **Weil-Positivität auf dem arithmetic site** die RH liefern würde — die Positivität bleibt der offene Punkt (Dok. 52).

## Bedeutung / Einordnung
- Arakelov-Geometrie ist die **beste bestehende Infrastruktur** für den Geometrie-Transfer und trotzdem beweisbar unzureichend, solange die Produktbasis fehlt. Sie ist damit ein Musterbeispiel für Fehlermodus `F10 analogy-transfer-gap` (Dok. 55) — und zugleich der Ort, an dem ein echter Durchbruch am plausibelsten wäre.
- Für die Beweisbewertung: Ein Vorschlag „RH via Arakelov" muss zuerst sagen, **welche Fläche** und **welcher Frobenius** benutzt werden. Fehlt eines von beiden, ist das Argument leer.

## Quellen
- S. Arakelov, *Intersection theory of divisors on an arithmetic surface*, Izv. Akad. Nauk SSSR 38 (1974).
- G. Faltings, *Calculus on arithmetic surfaces*, Ann. of Math. 119 (1984), 387–424.
- P. Hriljac, *Heights and Arakelov's intersection theory*, Amer. J. Math. 107 (1985).
- H. Gillet, C. Soulé, *An arithmetic Riemann–Roch theorem*, Invent. Math. 110 (1992).
- [C. Soulé, *Les variétés sur le corps à un élément*, Mosc. Math. J. 4 (2004)](http://www.mathjournals.org/mmj/2004-004-001/)
- [A. Connes, C. Consani, *The Arithmetic Site* (arXiv:1405.4527)](https://arxiv.org/abs/1405.4527)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `algebraic-geometric` |
> | Implikation | `conditional` |
> | Euler-Produkt | `essential` |
> | Positivität | `proves` |
> | Strenge | `theorem` |
> | Evidenz | `medium` |
> | Testbar | `low` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Spec ℤ ist eindimensional; das Produkt über einer absoluten Basis fehlt.
> 
> **Hebel:** Arithmetischer Hodge-Index-Satz existiert bereits (Faltings-Hriljac).
> 
> **Fehlermodi:** [[F10_analogy-transfer-gap|F10 Fehlende Geometrie über Spec(ℤ)]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-72`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Fehlende Geometrie über Spec(ℤ)** *(Tier 2)* — Der bewiesene Funktionenkörperfall braucht eine Fläche C×_𝔽 C; das Analogon Spec(ℤ)×_{𝔽₁}Spec(ℤ) existiert nicht.
>   *Fluchtbedingung:* Konstruktion einer Kohomologietheorie über Spec(ℤ) mit (a) Lefschetz-Formel, die die explizite Formel reproduziert, (b) Poincaré-Dualität, (c) einem Positivitäts-/Index-Satz (Hodge-Index-Analogon). Alle drei, nicht nur (a).
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (4)
> - *ist Instanz von* → **Geometrie-Transfer (Funktionenkörper→ℤ)** — Beste bestehende Infrastruktur für den Geometrie-Transfer.
> - *reduziert sich auf* → [[30_F1_field_one_element_arithmetic_site|30 · Der Körper mit einem Element]] — Für die fehlende zweite Dimension braucht man Spec ℤ ×_{𝔽₁} Spec ℤ.
> - *benutzt* → [[71_standard_conjectures_motives_positivity|71 · Grothendiecks Standardvermutungen & Motive]] — Arithmetischer Hodge-Index-Satz (Faltings–Hriljac) als Gegenstück zur Standardvermutung.
> - *benutzt* → [[31_Deninger_cohomology_foliated_dynamical|31 · Deningers Kohomologie-Programm & dynamische Systeme…]] — Deningers Fluss ersetzt den fehlenden Frobenius.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
