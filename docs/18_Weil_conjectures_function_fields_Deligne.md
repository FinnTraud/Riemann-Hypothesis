---
id: doc-18
number: 18
title: "Weil-Vermutungen: RH über endlichen Körpern (Deligne) — BEWIESEN"
category: proven-analogue
status: proven
tags: [weil-conjectures, deligne, function-fields, finite-fields, etale-cohomology]
source_file: 18_Weil_conjectures_function_fields_Deligne.md
lang: de
---

# Weil-Vermutungen: RH über endlichen Körpern (Deligne) — BEWIESEN

**Kategorie:** Bewiesenes Analogon (algebraisch/geometrisch)
**Autoren / Jahre:** Emil Artin (1920er), Helmut Hasse (1930er), André Weil (1940er), Bernard Dwork (1960), Alexander Grothendieck (1965), Pierre Deligne (1974)
**Typ:** Vollständig BEWIESENES Analogon der RH
**Status:** ✅ Bewiesen — wichtigste "Erfolgsgeschichte" und Vorbild

## Zusammenfassung
Für **Kurven (und allgemeiner Varietäten) über endlichen Körpern** existiert ein exaktes Analogon der Riemann-Vermutung — und dieses ist **vollständig bewiesen**. Das ist der größte Triumph der "RH-Familie" und das wichtigste Vorbild/Leitlicht für Angriffe auf die klassische RH (insbesondere Connes' Programm, Dok. 10).

## Kernidee
- Zu einer glatten projektiven Kurve C über dem endlichen Körper 𝔽_q definiert man eine **Kongruenz-Zetafunktion** Z(C, t), die Primzahlen durch abgeschlossene Punkte / Primdivisoren der Kurve ersetzt.
- Diese Zetafunktion ist eine **rationale Funktion**, erfüllt eine **Funktionalgleichung**, und ihre Nullstellen erfüllen ein **RH-Analogon**: Die "Nullstellen" haben Absolutbetrag q^{1/2} — die exakte Entsprechung von "Realteil 1/2".

## Die Weil-Vermutungen und ihr Beweis
Weil formulierte (modelliert nach Riemann) drei Vermutungen, die nacheinander bewiesen wurden:
1. **Rationalität** der Zetafunktion — Dwork (1960).
2. **Funktionalgleichung** — Grothendieck (1965, via étale Kohomologie).
3. **Riemann-Hypothese-Analogon** (Lage/Betrag der Nullstellen) — **Deligne (1974)**.

- **Weils eigener Beweis (1940er)** für Kurven nutzte klassische **Schnitttheorie** auf der Fläche C × C (Korrespondenzen, positive Definitheit der Schnittform — eine Positivitäts-/Hodge-Index-Idee).
- **Delignes Beweis (1974)** für allgemeine Varietäten nutzt **étale Kohomologie**, Monodromie von Lefschetz-Büscheln und umgeht geschickt die (damals unbewiesenen) Standardvermutungen. (Deligne erhielt u. a. die Fields-Medaille; Weil II 1980 verallgemeinerte das Resultat weiter.)

## Bedeutung / Einordnung für die klassische RH
- **Beweis der Machbarkeit:** Eine RH-artige Aussage *kann* bewiesen werden — wenn man die richtige Geometrie/Kohomologie hat.
- **Strategisches Vorbild:** Die klassische RH (über ℚ / ℤ) hätte man gern als "Geometrie über dem hypothetischen Körper mit einem Element 𝔽₁" oder über Spec(ℤ) — genau das motiviert Connes–Consani (Dok. 10/11) und arithmetische Geometrie-Programme.
- **Schlüsselzutat Positivität:** Sowohl Weils als auch Delignes Zugang beruhen auf Positivitäts-/Schnittargumenten — das spiegelt sich in der Weil-Positivität der klassischen RH (Dok. 14).
- **Wichtige Einschränkung:** Über ℤ fehlt bislang die analoge geometrische/kohomologische Struktur — der Transfer ist *die* offene Aufgabe.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Kongruenz-Zetafunktion einer Kurve über 𝔽_q
Für eine glatte projektive Kurve C/𝔽_q vom Geschlecht g sei N_m = #C(𝔽_{q^m}). Definiere
```
Z(C, t) = exp( Σ_{m=1}^∞ N_m t^m / m )   =   ∏_{x abgeschlossener Punkt} (1 − t^{deg x})^{−1}.
```
Das Produkt über Punkte ist das exakte Analogon des Eulerprodukts (Punkte ↔ Primzahlen). Mit t = q^{−s} entsteht ζ_C(s) = Z(C, q^{−s}).

### Rationalität & Funktionalgleichung (Dwork, Weil)
```
Z(C, t) = P(t) / ((1 − t)(1 − q t)),   P(t) = ∏_{i=1}^{2g} (1 − α_i t) ∈ ℤ[t], deg P = 2g.
```
Funktionalgleichung: Z(C, 1/(qt)) = q^{1−g} t^{2−2g} Z(C, t), äquivalent α_i ↦ q/α_i als Permutation der Wurzeln.

### Das RH-Analogon (Weil 1948 für Kurven, Deligne 1974 allgemein)
```
|α_i| = q^{1/2}   für alle i = 1, …, 2g.
```
Übersetzt via t = q^{−s}: die Nullstellen von ζ_C(s) (Nullstellen von P(q^{−s})) erfüllen q^{−s} = 1/α_i, also q^{s} = α_i, |α_i| = q^{1/2} ⟺ **Re(s) = 1/2**. Exaktes Analogon der RH. Daraus die scharfe Punktschätzung:
```
| N_m − (q^m + 1) | ≤ 2g · q^{m/2}    (Hasse–Weil-Schranke).
```

### Weils Beweis (Positivität / Schnitttheorie)
Auf der Fläche C × C betrachtet man den Frobenius-Graphen Γ_F und die Diagonale Δ. Die **Hodge-Index-Ungleichung** (Positivität der Schnittform auf Divisoren) liefert für die Frobenius-Korrespondenz die Cauchy–Schwarz-artige Abschätzung, die |α_i| = √q erzwingt. Kern: positive Definitheit von ⟨D, D⟩ auf der primitiven Kohomologie/Néron–Severi-Gruppe.

### Delignes Beweis (étale Kohomologie)
Die α_i sind die Eigenwerte des **geometrischen Frobenius** F* auf H¹_{ét}(C̄, ℚ_ℓ):
```
P(t) = det( 1 − t F* | H¹_{ét} ),   Z(C,t) = ∏_{i=0}^{2} det(1 − tF*|H^i)^{(−1)^{i+1}}.
```
Deligne (Weil I, 1974) beweist |α_i| = q^{w/2} (w = Gewicht) für allgemeine Varietäten via Monodromie von Lefschetz-Büscheln, Rankin–Selberg-artige Potenzierungstricks und L-Funktionen von Symmetrieprodukten — ohne die Standardvermutungen.

### Warum kein Transfer auf ℤ
Es fehlt für Spec(ℤ) das „×_{𝔽₁} "-Produkt, die Frobenius-Wirkung und die passende Kohomologie (vgl. 𝔽₁ Dok. 30, Deninger Dok. 31). Die Positivität (Weil) bzw. Reinheit (Deligne) hat über ℤ kein bekanntes Analogon.

## Quellen
- [The Riemann Hypothesis over Finite Fields: From Weil to the Present Day (arXiv 1509.00797)](https://arxiv.org/abs/1509.00797)
- [The Riemann Hypothesis over Finite Fields — J. Milne](https://www.jmilne.org/math/xnotes/pRH.html)
- [Weil conjectures — Wikipedia](https://en.wikipedia.org/wiki/Weil_conjectures)
- [Deligne's proof of the Weil conjectures — E. Kowalski's blog](https://blogs.ethz.ch/kowalski/2008/03/15/delignes-proof-of-the-weil-conjectures/)

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
> **Offener Kernschritt:** Transfer nach Z: es fehlen Fläche, Frobenius und Polarisierung.
> 
> **Hebel:** Der einzige vollständig bewiesene RH-Fall - Blaupause für alles Weitere.
> 
> **Fehlermodi:** [[F10_analogy-transfer-gap|F10 Fehlende Geometrie über Spec(ℤ)]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-18`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Fehlende Geometrie über Spec(ℤ)** *(Tier 2)* — Der bewiesene Funktionenkörperfall braucht eine Fläche C×_𝔽 C; das Analogon Spec(ℤ)×_{𝔽₁}Spec(ℤ) existiert nicht.
>   *Fluchtbedingung:* Konstruktion einer Kohomologietheorie über Spec(ℤ) mit (a) Lefschetz-Formel, die die explizite Formel reproduziert, (b) Poincaré-Dualität, (c) einem Positivitäts-/Index-Satz (Hodge-Index-Analogon). Alle drei, nicht nur (a).
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (4)
> - *ist Blaupause für* → **Geometrie-Transfer (Funktionenkörper→ℤ)** — Weil/Deligne: BEWIESENES RH-Analogon über 𝔽_q — die Blaupause.
> - ← *ist Reduktionsziel von* [[71_standard_conjectures_motives_positivity|71 · Grothendiecks Standardvermutungen & Motive]] — Isoliert den Schritt in Weils Beweis, der die kritische Gerade erzwingt.
> - ← *wird benutzt von* [[70_Langlands_functoriality_automorphic|70 · Langlands-Funktorialität & automorphe L-Funktionen]] — Ramanujan–Petersson (lokales RH-Analogon) folgt aus Deligne/Weil.
> - ← *wird benutzt von* [[76_higher_correlations_Rudnick_Sarnak|76 · Höhere Korrelationen]] — Katz–Sarnak: im Funktionenkörperfall ist die Symmetrie ein Satz.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
