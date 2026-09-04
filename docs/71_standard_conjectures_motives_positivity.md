---
id: doc-71
number: 71
title: "Grothendiecks Standardvermutungen & Motive: die Herkunft der Positivität"
category: solution-program
status: open
tags: [grothendieck, standard-conjectures, motives, hodge-index, weil-positivity, castelnuovo-severi, intersection-theory]
source_file: 71_standard_conjectures_motives_positivity.md
lang: de
---

# Standardvermutungen & Motive — wo die Positivität im bewiesenen Fall herkommt

**Kategorie:** Struktur-Analyse eines bewiesenen Analogons (algebraische Geometrie)
**Autoren / Jahre:** Weil (1948, Kurven); Grothendieck (1968/69, Standardvermutungen); Deligne (1974, Weil I — Umgehung); Kleiman (Übersichten)
**Typ:** Diagnose: *welcher* Satz genau im Funktionenkörperfall die kritische Gerade erzwingt
**Status:** Standardvermutungen offen (in Char. p); die für die RH über 𝔽_q nötigen Fälle sind bewiesen bzw. umgangen

## Zusammenfassung
Im bewiesenen Fall — RH für Kurven über endlichen Körpern (Dok. 18) — kommt die Aussage `|α_i| = q^{1/2}` **nicht** aus Analysis, sondern aus einer **Positivitätsaussage der Schnitttheorie**: dem Hodge-Index-Satz bzw. der Castelnuovo–Severi-Ungleichung auf der Fläche C × C. Dieses Dokument isoliert genau diesen Schritt — weil er die Blaupause für Weil-Positivität (Dok. 14) und Connes' Programm (Dok. 10, 52) ist und weil man an ihm exakt ablesen kann, **was über ℤ fehlt**.

## Mathematischer Kern

### Weils Beweis für Kurven (die Positivitätsquelle)
Sei C/𝔽_q eine glatte projektive Kurve vom Geschlecht g, F der Frobenius auf C, und arbeite auf der **Fläche** S = C × C. Für Korrespondenzen (Divisorklassen) D auf S gilt der **Hodge-Index-Satz**: die Schnittform ist auf dem Orthogonalraum der Polarisierung **negativ definit**. Daraus folgt die *Castelnuovo–Severi-Ungleichung*
```
(D · D)  ≤  2 · d_1(D) · d_2(D)
```
für effektive Korrespondenzen mit Bi-Graden d_1, d_2. Angewandt auf `D = ΔF^n` (Graph des n-ten Frobenius) und die Lefschetz-Fixpunktformel
```
#C(𝔽_{q^n}) = (Δ · ΔF^n) = q^n + 1 − Σ_{i=1}^{2g} α_i^n
```
liefert die Ungleichung eine Schranke `|Σ α_i^n| ≤ 2g·q^{n/2}` für alle n, und daraus (Standardargument über Potenzreihen / Landau) `|α_i| = q^{1/2}` — **die RH über 𝔽_q**.

> **Merksatz:** Die kritische Gerade ist im bewiesenen Fall der Schatten einer **Definitheitsaussage einer Bilinearform** (Schnittform), nicht das Ergebnis einer Abschätzung.

### Grothendiecks Standardvermutungen
Grothendieck wollte die Weil-Vermutungen aus zwei Vermutungen über algebraische Zykel ableiten:
- **Lefschetz-Standardvermutung (B):** der inverse Lefschetz-Operator Λ ist algebraisch.
- **Hodge-Standardvermutung (Hdg):** die Paarung `x ↦ (−1)^i (x · L^{n−2i} x)` ist auf primitiven Zykeln **positiv definit**.
Zusammen ⇒ Weil-Vermutungen (inkl. RH) *und* die Kategorie der Motive wird semisimpel (Tannaka-Formalismus).

**Status:** In Charakteristik 0 folgt Hdg aus den Hodge–Riemann-Bilinearrelationen. In **Charakteristik p** ist die Hodge-Standardvermutung **offen** (außer in Dimension ≤ 2 / Spezialfällen). Deligne bewies Weil I **ohne** sie (Monodromie + Rankin-Trick + Hadamard–de la Vallée-Poussin-artiges Argument) — eine der ganz wenigen Situationen, in der die „falsche Reihenfolge" funktionierte.

### Übersetzungstabelle: was hätte man über ℤ?
| Funktionenkörper (bewiesen) | Zahlkörper (fehlt) |
|---|---|
| Fläche C × C über 𝔽_q | „Spec ℤ ×_{𝔽₁} Spec ℤ" — **existiert nicht** (Dok. 30) |
| Frobenius-Endomorphismus F | keine kanonische Selbstabbildung auf Spec ℤ |
| Schnittform + Hodge-Index (**positiv definit**) | Arakelov-Schnitttheorie liefert Hodge-Index für arithmetische **Flächen** (Faltings–Hriljac), aber Spec ℤ ist eine Kurve (Dok. 72) |
| Lefschetz-Fixpunktformel | Weilsche explizite Formel (Dok. 02, 14) — formal analog, aber **ohne Raum**, auf dem sie eine Spur wäre |
| ⇒ `|α_i| = q^{1/2}` | ⇒ Re(ρ) = 1/2 — **offen** |

### Warum das die Diagnose für Connes/Weil-Positivität ist
Weils explizite Formel lässt sich als „Spurformel" lesen; RH ⟺ die zugehörige quadratische Form W(f, f) ist ≥ 0 (Weil-Positivität, Dok. 14). Im geometrischen Fall **ist** diese Positivität der Hodge-Index-Satz. Connes' Programm (Dok. 10, 52) versucht, die Positivität analytisch zu erzwingen — aber jeder bisherige Versuch nutzt implizit dieselbe Information, die man beweisen will (`F2 positivity-assumed`, Dok. 55), oder gilt nur nach Abschneidung (`F9`). **Die Standardvermutungen zeigen, wo die Positivität herkommen müsste: aus einer Geometrie mit Polarisierung.**

## Bedeutung / Einordnung
- Dieses Dokument ist der **Knotenpunkt** zwischen dem bewiesenen Analogon (18), Connes (10/52), Deninger (31), 𝔽₁ (30) und Arakelov (61).
- Praktische Konsequenz für Beweisbewertung: Fragt jemand „warum sollte die quadratische Form positiv sein?", ist die einzige bekannte ehrliche Antwort „weil sie eine Schnittform auf einer polarisierten Varietät ist" — fehlt diese Varietät, ist die Positivität eine **Annahme**.

## Quellen
- A. Grothendieck, *Standard conjectures on algebraic cycles*, in: Algebraic Geometry (Bombay 1968), Oxford 1969, 193–199.
- [S. Kleiman, *The standard conjectures*, in: Motives, Proc. Sympos. Pure Math. 55 (1994)](https://www.ams.org/books/pspum/055.1/)
- A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*, Hermann 1948.
- P. Deligne, *La conjecture de Weil I / II*, Publ. Math. IHÉS 43 (1974) / 52 (1980).
- [J. S. Milne, *Motives — Grothendieck's Dream* (Notizen)](https://www.jmilne.org/math/xnotes/MOT.pdf)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `algebraic-geometric` |
> | Implikation | `partial` |
> | Euler-Produkt | `essential` |
> | Positivität | `proves` |
> | Strenge | `theorem` |
> | Evidenz | `n/a` |
> | Testbar | `low` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Analogon der Hodge-Standardvermutung über Z formulieren - dazu fehlt die Varietät.
> 
> **Hebel:** Zeigt exakt, woher Positivität im bewiesenen Fall kommt.
> 
> **Fehlermodi:** [[F10_analogy-transfer-gap|F10 Fehlende Geometrie über Spec(ℤ)]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-71`

> [!warning]- Blocker — woran dieser Ansatz hängt (2)
> - **Fehlende Geometrie über Spec(ℤ)** *(Tier 2)* — Der bewiesene Funktionenkörperfall braucht eine Fläche C×_𝔽 C; das Analogon Spec(ℤ)×_{𝔽₁}Spec(ℤ) existiert nicht.
>   *Fluchtbedingung:* Konstruktion einer Kohomologietheorie über Spec(ℤ) mit (a) Lefschetz-Formel, die die explizite Formel reproduziert, (b) Poincaré-Dualität, (c) einem Positivitäts-/Index-Satz (Hodge-Index-Analogon). Alle drei, nicht nur (a).
> - **Zirkuläre Positivität** *(Tier 2)* — Die RH wird auf eine Positivitätsaussage reduziert, die selbst nur als äquivalent, nie unabhängig bewiesen ist.
>   *Fluchtbedingung:* Die Positivität muss aus einer Struktur folgen, die unabhängig von der Nullstellenlage definiert ist. Im bewiesenen Fall 𝔽_q (doc-18) leistet das die Schnittform auf der Fläche C×C — dort ist Positivität ein Satz der Geometrie, nicht eine Umformulierung des Ziels.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (6)
> - *ist Blaupause für* → [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|14 · Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]] — Weil-Positivität ist im geometrischen Fall der Hodge-Index-Satz.
> - *ist Blaupause für* → [[10_Connes_noncommutative_geometry|10 · Alain Connes]] — Sagt, woher die von Connes benötigte Positivität kommen müsste.
> - *ist Instanz von* → **Schnittform-Positivität (Hodge-Index)** — Hodge-Standardvermutung = Positivität der Schnittform.
> - *ist Instanz von* → **Geometrie-Transfer (Funktionenkörper→ℤ)** — Diagnose des fehlenden Trägerobjekts über ℤ.
> - *reduziert sich auf* → [[18_Weil_conjectures_function_fields_Deligne|18 · Weil-Vermutungen]] — Isoliert den Schritt in Weils Beweis, der die kritische Gerade erzwingt.
> - ← *wird benutzt von* [[72_Arakelov_geometry_SpecZ_compactification|72 · Arakelov-Geometrie & die Kompaktifizierung von Spec…]] — Arithmetischer Hodge-Index-Satz (Faltings–Hriljac) als Gegenstück zur Standardvermutung.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
