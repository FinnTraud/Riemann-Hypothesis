---
id: doc-43
number: 43
title: "Epstein-Zetafunktionen & Selberg-Klassen-Rigidität: Welche Eigenschaft erzwingt die kritische Gerade?"
category: obstruction
status: meta
tags: [epstein-zeta, selberg-class-rigidity, davenport-heilbronn, euler-product, kaczorowski-perelli]
source_file: 43_Epstein_zeta_Selberg_class_rigidity.md
lang: de
---

# Epstein-Zetafunktionen & Selberg-Klassen-Rigidität: Welche Eigenschaft erzwingt die kritische Gerade?

**Kategorie:** Meta / Obstruktion (Tier-1 für „bulletproof")
**Autoren / Jahre:** Davenport–Heilbronn (1936); Epstein; Voronin; Kaczorowski–Perelli (Selberg-Klassen-Klassifikation, 1999–2011)
**Typ:** Diskriminierende Gegenbeispiele + Strukturtheorie
**Status:** Etablierte Negativ-/Rigiditätsresultate

## Zusammenfassung
Dies ist das **wichtigste „bulletproof"-Dokument** zusammen mit Dok. 35: Es beantwortet die Frage, **welche** Eigenschaften die Nullstellen tatsächlich auf die kritische Gerade zwingen — durch Funktionen, die *fast* wie ζ aussehen, aber die RH verletzen. Ergänzt Dok. 35 (Davenport–Heilbronn) um die **Epstein-Zetafunktionen** und die **Rigidität der Selberg-Klasse vom Grad 1**.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Epstein-Zetafunktion
Für eine positiv-definite quadratische Form Q(m,n) = am² + bmn + cn² (Diskriminante d = b²−4ac < 0):
```
ζ_Q(s) = Σ_{(m,n) ≠ (0,0)} Q(m,n)^{−s}   (Re s > 1).
```
ζ_Q besitzt eine **analytische Fortsetzung** und eine **Funktionalegleichung** vom Riemann-Typ (Re s ↔ 1−s, via Theta-Transformation) — also dieselben „weichen" Eigenschaften wie ζ.

### Das Gegenbeispiel
**Satz (Davenport–Heilbronn 1936 für die zugehörige Dirichlet-Reihe; Epstein-Fall).** Wenn die **Klassenzahl h(d) > 1** ist (die quadratische Form nicht allein in ihrer Geschlechterklasse liegt), dann hat ζ_Q **unendlich viele Nullstellen mit Re(s) > 1/2** — die RH-Analogie ist FALSCH. Dennoch hat ζ_Q auch einen positiven Anteil (sogar unendlich viele) Nullstellen *auf* der Geraden.

### Warum: das fehlende Euler-Produkt
ζ_Q ist eine **Linearkombination** von Hecke-L-Funktionen zu Idealklassencharakteren:
```
ζ_Q(s) = (1/w) Σ_{χ} χ̄(class(Q)) L(s, χ),
```
und diese Summe besitzt **kein Euler-Produkt** (die einzelnen L(s,χ) schon, ihre Linearkombination nicht). Genau das fehlende Euler-Produkt erlaubt Nullstellen abseits der Geraden (vgl. Dok. 35).

### Selberg-Klassen-Rigidität (was RH erzwingt)
Die **Selberg-Klasse 𝒮** (Dok. 21) verlangt zusätzlich zu Funktionalgleichung + Fortsetzung ein **Euler-Produkt** und die **Ramanujan-Bedingung**. Klassifikationssätze (Conrey–Ghosh; Kaczorowski–Perelli):
```
- Es gibt keine Funktionen in 𝒮 vom Grad 0 < d < 1.
- Grad d = 1 in 𝒮  ⟹  F(s) = ζ(s)  oder  F(s) = L(s + iθ, χ)  (verschobene Dirichlet-L-Funktion).
```
**Konsequenz (Rigidität):** Funktionen vom Grad 1 *mit* Euler-Produkt und Ramanujan-Bedingung sind im Wesentlichen ζ und Dirichlet-L — und für genau diese wird die RH erwartet. Davenport–Heilbronn (Grad 1, **ohne** Euler-Produkt) und Epstein (h>1, **ohne** Euler-Produkt) fallen heraus.

### Die präzise Lehre für einen Beweis
> Off-Line-Nullstellen werden möglich, sobald das Euler-Produkt fehlt. **Ein gültiger RH-Beweis muss die Multiplikativität (Euler-Produkt) + Ramanujan-Schranke an einer Stelle nutzen, an der Davenport–Heilbronn/Epstein sie verletzen.** Jeder Beweis, der diese Eigenschaften nicht unterscheidet, ist falsch.

## Verbindung
- Verschärft Dok. 35 (Obstruktionen) und Dok. 21 (Selberg-Klasse).
- Erklärt, warum Connes (Dok. 10) das Euler-Produkt adelisch (Stelle für Stelle) einbaut und warum Scattering-/Spektral­modelle für Davenport–Heilbronn gar nicht erst definierbar sind.

## Quellen
- [Zeros of the Davenport-Heilbronn Counterexample (AMS Math. Comp.)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)
- [Positive proportion of zeros of Epstein zeta on the critical line (arXiv 2411.18492)](https://arxiv.org/pdf/2411.18492)
- [On the Selberg class / converse theorems (arXiv 1605.02354)](https://arxiv.org/pdf/1605.02354)
- [On some reasons for doubting the Riemann hypothesis — Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (2)
> - **Euler-Blindheit** *(Tier 1)* — Das Argument benutzt nur Funktionalgleichung, Fortsetzung und Wachstum — es würde für Davenport–Heilbronn genauso gelten und ist damit falsch.
>   *Fluchtbedingung:* Mindestens ein Beweisschritt muss eine Eigenschaft benutzen, die für Davenport–Heilbronn NACHWEISLICH FALSCH ist — praktisch immer: Multiplikativität der Koeffizienten / Euler-Produkt.
> - **Weichheitsbarriere (Voronin)** *(Tier 1)* — ζ approximiert im kritischen Streifen JEDE nullstellenfreie analytische Funktion — 'weiche' Argumente können deshalb nicht greifen.
>   *Fluchtbedingung:* Das Argument muss eine globale Rigiditätseigenschaft benutzen (Euler-Produkt, Grad in der Selberg-Klasse, Spurformel), die durch lokale Approximation nicht sichtbar ist.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (5)
> - *ist Evidenz für* → **Euler-Produkt (Multiplikativität)** — Epstein-Zeta + Selberg-Klassen-Rigidität: Euler-Produkt+Ramanujan erzwingen die Gerade.
> - *ist Obstruktion für* → **Riemann-Vermutung (RH)** — Welche Eigenschaft die Gerade erzwingt; schließt 'weiche' Beweise aus.
> - *ist Obstruktion für* → [[52_Connes_truncated_Weil_spectral_realization|52 · Abgeschnittene Weil-Quadratform & Zeta-Spektraltrip…]] — Epstein/Selberg-Rigiditaet verlangt echten Euler-Produkt-Input - Dok. 52 liefert ihn, besteht die Pruefung also.
> - *benutzt* → [[21_GRH_Selberg_class_grand_RH|21 · Verallgemeinerte, Große Riemann-Vermutung & Selberg…]] — Selberg-Klassen-Klassifikation (Kaczorowski–Perelli).
> - ← *wird benutzt von* [[59_invariants_test_vectors|59 · Invarianten & Testvektoren]] — Epstein-Zeta als zweiter, natuerlicher Testvektor.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
