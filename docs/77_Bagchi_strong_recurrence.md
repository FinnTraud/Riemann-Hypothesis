---
id: doc-77
number: 77
title: "Bagchis Satz: RH als starke Rekurrenz (Universalität als Kriterium)"
category: criterion
status: proven
tags: [bagchi, strong-recurrence, universality, voronin, almost-periodicity, ergodic, equivalent-criterion]
source_file: 77_Bagchi_strong_recurrence.md
lang: de
---

# Bagchis Satz — RH als „starke Rekurrenz" von ζ

**Kategorie:** Äquivalentes Kriterium (funktionentheoretisch/ergodisch)
**Autoren / Jahre:** Bhaskar Bagchi (1981/1982, Diss. ISI Kalkutta; 1987); Anbauten: Steuding, Nakamura, Garunkštis–Laurinčikas
**Typ:** RH-Äquivalenz über Selbst-Approximation von ζ
**Status:** Äquivalenz BEWIESEN; RH offen — und das Kriterium ist beweisbar **schwer zugänglich** (siehe Dok. 46)

## Zusammenfassung
Voronins Universalitätssatz (Dok. 46) besagt: ζ approximiert im Streifen `1/2 < σ < 1` **jede** nullstellenfreie holomorphe Funktion beliebig gut. Bagchi bemerkte: Wendet man das auf **ζ selbst** an, entsteht ein RH-Kriterium. Die RH ist genau dann wahr, wenn ζ sich selbst „mit positiver Dichte an Zeitverschiebungen" reproduziert — **starke Rekurrenz**. Damit wird die RH zu einer Aussage über die Dynamik einer Translation, nicht über Nullstellen.

## Mathematischer Kern

### Satz (Bagchi 1981)
Sei `K ⊂ {s : 1/2 < Re s < 1}` kompakt mit zusammenhängendem Komplement. Dann:
```
RH   ⟺   ∀K, ∀ε>0:
         liminf_{T→∞} (1/T) · meas{ τ ∈ [0,T] : max_{s∈K} |ζ(s+iτ) − ζ(s)| < ε }  >  0.
```
In Worten: **ζ ist genau dann „stark rekurrent", wenn die RH gilt.** Man verlangt nicht nur *eine* gute Zeitverschiebung (das folgte schon aus fast-Periodizität), sondern eine Menge positiver **unterer Dichte**.

### Beweisskizze
**(⇐, die leichte Richtung als Kontraposition.)** Gäbe es eine Nullstelle `ρ₀` mit `Re ρ₀ = σ₀ > 1/2`, wähle K als kleine Kreisscheibe um `ρ₀`, ganz im Streifen. Nach der Nullstellenzähl-Theorie (Dichte-Sätze) besitzt ζ in einem solchen Streifen dann Nullstellen mit **positiver Dichte in t**; eine Verschiebung `ζ(s+iτ)`, die `ζ(s)` auf K gut approximiert, müsste nach Rouché ebenfalls eine Nullstelle in K haben. Zählt man die möglichen τ, widerspricht die geforderte positive Dichte der bekannten Nullstellendichte-Schranke `N(σ₀,T) = o(T)` (Dok. 17/22). Also keine starke Rekurrenz.

**(⇒.)** Unter RH ist ζ im Streifen nullstellenfrei; nach Voronin ist ζ auf K durch sich selbst approximierbar, und der Universalitätssatz liefert die positive Dichte (der Satz gibt sie sogar mit `liminf > 0` für *jede* zulässige Zielfunktion, insbesondere für ζ|_K selbst).

### Der eingebaute Haken (warum das Kriterium nicht „hilft")
Voronins Satz gilt **nur für nullstellenfreie** Zielfunktionen. Um ζ|_K als Ziel zuzulassen, muss man wissen, dass ζ auf K nullstellenfrei ist — also die RH. **Das Kriterium ist damit nicht zirkulär (der Beweis ist korrekt), aber es ist selbstbezüglich: die einzige bekannte Methode, seine Voraussetzung zu prüfen, ist die RH selbst.**

Das ist der genaue Grund, warum Voronin-Universalität in Dok. 46 als **Meta-Obstruktion** geführt wird: Universalität sagt, dass ζ im Streifen „alles tut, was erlaubt ist". Eine Eigenschaft, die man aus weicher Funktionentheorie ableitet, gilt deshalb automatisch für sehr viele Funktionen — und kann die Gerade nicht auszeichnen. Bagchis Kriterium ist die schärfste Formulierung dieses Zustands: **RH ⟺ ζ ist nicht ausgezeichnet genug, um sich selbst zu vermeiden.**

### Erweiterungen
- **Nakamura, Pańkowski:** „gemeinsame starke Rekurrenz" und Varianten für Dirichlet-L-Funktionen (GRH-Versionen).
- **Garunkštis–Laurinčikas:** effektive/quantitative Universalität — sehr schwache Schranken (Doppel-Exponential), ein bekannter offener Punkt.
- **Diskrete Version:** starke Rekurrenz entlang arithmetischer Folgen `τ = nh` (diskrete Universalität) — ebenfalls RH-äquivalent.

## Bedeutung / Einordnung
- **Wertvoll als Diagnose-Instrument:** Bagchi zeigt formal, was „weiche" Ansätze prinzipiell nicht leisten können. Für den Anti-Crackpot-Filter (Dok. 35/41) die Prüffrage: *„Würde das Argument auch für eine andere universelle Funktion (z. B. Hurwitz-ζ mit transzendentem Parameter) gelten? Dann ist es falsch."*
- **Testbar (schwach):** Die Rekurrenzmenge `{τ : max_K|ζ(s+iτ)−ζ(s)| < ε}` ist numerisch messbar (Dichte für kleine T abschätzen). Das ist kein RH-Test (die Dichte ist positiv, egal was man findet), aber ein anschauliches Experiment für die Universalität.
- Fehlermodus: `F7 soft-function-theory` + `F11 criterion-restates` (Dok. 55).

## Quellen
- B. Bagchi, *The statistical behaviour and universality properties of the Riemann zeta-function and other allied Dirichlet series*, PhD thesis, Indian Statistical Institute, Kalkutta 1981.
- B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math. Hungar. 50 (1987), 227–240.
- J. Steuding, *Value-Distribution of L-Functions*, Springer Lecture Notes in Math. 1877 (2007).
- [S. M. Voronin, *Theorem on the universality of the Riemann zeta function* (Izv. 1975)](https://www.mathnet.ru/eng/im2224)
- [T. Nakamura, *The joint universality and the generalized strong recurrence for Dirichlet L-functions* (arXiv:0908.1129)](https://arxiv.org/abs/0908.1129)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `criterion` |
> | Implikation | `equivalent` |
> | Euler-Produkt | `none` |
> | Positivität | `n/a` |
> | Strenge | `theorem` |
> | Evidenz | `weak` |
> | Testbar | `medium` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Selbstbezüglich: Voronin verlangt Nullstellenfreiheit auf K - also genau die RH.
> 
> **Hebel:** Formuliert präzise, warum weiche Funktionentheorie nicht reichen kann.
> 
> **Fehlermodi:** [[F7_soft-function-theory|F7 Weichheitsbarriere (Voronin)]] · [[F11_criterion-restates|F11 Äquivalenz-Falle]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-77`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Weichheitsbarriere (Voronin)** *(Tier 1)* — ζ approximiert im kritischen Streifen JEDE nullstellenfreie analytische Funktion — 'weiche' Argumente können deshalb nicht greifen.
>   *Fluchtbedingung:* Das Argument muss eine globale Rigiditätseigenschaft benutzen (Euler-Produkt, Grad in der Selberg-Klasse, Spurformel), die durch lokale Approximation nicht sichtbar ist.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (3)
> - *äquivalent zu* → **Riemann-Vermutung (RH)** — RH ⟺ starke Rekurrenz von ζ im Streifen 1/2<σ<1.
> - *ist Evidenz für* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Schärfste Formulierung, warum weiche Funktionentheorie nicht reicht.
> - *benutzt* → [[46_Voronin_universality|46 · Voronin-Universalität]] — Beruht direkt auf Voronin-Universalität.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
