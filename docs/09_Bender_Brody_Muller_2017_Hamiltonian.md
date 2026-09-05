---
id: doc-09
number: 09
title: "Bender–Brody–Müller (2017): PT-symmetrischer Hamiltonian für die Riemann-Nullstellen"
category: spectral
status: open
tags: [bender-brody-muller, PT-symmetry, hamiltonian]
source_file: 09_Bender_Brody_Muller_2017_Hamiltonian.md
lang: de
---

# Bender–Brody–Müller (2017): PT-symmetrischer Hamiltonian für die Riemann-Nullstellen

**Kategorie:** Spektraler Ansatz / Quantenphysik
**Autoren / Jahr:** Carl M. Bender, Dorje C. Brody, Markus P. Müller; *Physical Review Letters* 118, 130201 (30. März 2017)
**Typ:** Operator-Konstruktion (Hilbert–Pólya-Kandidat)
**Status:** Unvollständig; Selbstadjungiertheit nicht bewiesen, von Kritikern angezweifelt

## Zusammenfassung
Bender, Brody und Müller konstruierten 2017 einen konkreten Hamiltonian-Operator H mit der Eigenschaft: Erfüllen seine Eigenfunktionen eine geeignete Randbedingung, so entsprechen die Eigenwerte exakt den nicht-trivialen Nullstellen der Zetafunktion. Die Arbeit erregte mediale Aufmerksamkeit ("Physiker greifen die Riemann-Vermutung an"), blieb aber lückenhaft.

## Kernidee
- Der Operator ist eine **Verallgemeinerung des Berry–Keating xp-Operators** (Dok. 08).
- Konstruktion so, dass die Eigenwerte E_n mit den Nullstellen z_n via **z_n = ½(1 − i·E_n)** zusammenhängen. Sind alle E_n reell, so haben alle z_n Realteil 1/2 → RH.
- **PT-Symmetrie statt klassischer Hermitezität:** H selbst ist nicht hermitesch im üblichen Sinn, aber **iH ist PT-symmetrisch**. Wäre diese PT-Symmetrie *maximal gebrochen*, so wären alle Eigenwerte reell.

## Die entscheidende Lücke
- Die Autoren formulierten selbst die Bedingung: **Lässt sich rigoros zeigen, dass H (in einem geeigneten Sinn) selbstadjungiert ist bzw. die PT-Symmetrie maximal gebrochen ist, so folgt die RH.**
- Genau dieser Schritt wurde **nicht** bewiesen. Die Reduktion verlagert die RH lediglich in eine ebenso schwierige spektraltheoretische Aussage.
- **Kritik:** Mehrere Kommentare (u. a. arXiv 1704.02644) wiesen auf Probleme bei der Wohldefiniertheit / Selbstadjungiertheit und der Behandlung der Randbedingungen hin. Der Zusammenhang reproduziert zudem im Wesentlichen die bekannte explizite Formel / funktionalanalytische Struktur, ohne neue Kontrolle über die Nullstellen zu liefern.

## Bedeutung / Einordnung
- Sauberster moderner *expliziter* Hilbert–Pólya-Operatorkandidat — aber mit derselben fundamentalen Lücke wie alle Vorgänger: Die *Realität des Spektrums* ist die eigentliche Frage und bleibt unbewiesen.
- Belebte die Diskussion über PT-symmetrische (nicht-hermitesche) Quantenmechanik im RH-Kontext neu.
- **Kein Beweis der RH.**

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Der konstruierte Operator
Bender–Brody–Müller definieren auf einem geeigneten Hilbertraum (Eigenfunktionen mit Randbedingung) den Operator
```
Ĥ = (1/(1 − e^{−i p̂})) ( x̂ p̂ + p̂ x̂ ) (1 − e^{−i p̂})
```
mit x̂ = i d/dx (bzw. kanonisch [x̂, p̂] = i). Das ist eine Konjugation des symmetrisierten Berry–Keating-Operators (x̂p̂ + p̂x̂)/2 mit dem nicht-unitären Operator (1 − e^{−ip̂}).

### Behauptete Eigenwert-Beziehung
Erfüllen die Eigenfunktionen ψ die Randbedingung ψ(0) = 0, so behaupten die Autoren: die Eigenwerte E_n liefern die nicht-trivialen Nullstellen via
```
z_n = 1/2 + i·(... )   ⇔   die Sekulärgleichung wird zu  ζ(1/2 + i E_n …) = 0,
```
genauer in der Formulierung E_n ↔ z_n durch z_n = ½(1 − i E_n). Sind alle E_n reell ⇒ Re(z_n) = 1/2 ⇒ RH.

### PT-Symmetrie statt Hermitezität
Ĥ ist nicht hermitesch, aber es gilt
```
(PT) (i Ĥ) (PT)^{−1} = i Ĥ
```
mit Parität P: x ↦ −x und Zeitumkehr T: i ↦ −i. **Schlüsselsatz der PT-Theorie:** Ist die PT-Symmetrie ungebrochen (alle Eigenzustände PT-invariant), so ist das Spektrum reell. Die Autoren benötigen, dass die PT-Symmetrie **maximal gebrochen** auf dem relevanten Teilraum so wirkt, dass dennoch Realität folgt.

### Die Lücke (präzise)
Es fehlt der Beweis, dass Ĥ (bzw. die zugehörige Bilinearform) auf dem konstruierten Definitionsbereich tatsächlich **selbstadjungiert** (bzw. die PT-Symmetrie im nötigen Sinn ungebrochen) ist. Ohne diesen Schritt ist die Realität der E_n nicht gesichert. Zudem zeigt die Konjugation mit (1 − e^{−ip̂}) formal nur, dass die *Sekulärfunktion* mit ζ verwandt ist — die eigentliche Schwierigkeit (Lage der Nullstellen) wird reproduziert, nicht gelöst. Kommentar arXiv 1704.02644 weist auf Wohldefiniertheits-/Domänenprobleme hin.

## Quellen
- [Hamiltonian for the Zeros of the Riemann Zeta Function — Phys. Rev. Lett. 118, 130201](https://link.aps.org/doi/10.1103/PhysRevLett.118.130201)
- [Hamiltonian for the zeros of the Riemann zeta function (arXiv 1608.03679)](https://arxiv.org/abs/1608.03679)
- [Comment on "Hamiltonian for the Zeros of the Riemann Zeta Function" (arXiv 1704.02644)](https://arxiv.org/pdf/1704.02644)
- [Physicists Attack Math's $1,000,000 Question — Quanta Magazine](https://www.quantamagazine.org/quantum-physicists-attack-the-riemann-hypothesis-20170404/)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `physical` |
> | Implikation | `conditional` |
> | Euler-Produkt | `none` |
> | Positivität | `assumes` |
> | Strenge | `refuted` |
> | Evidenz | `weak` |
> | Testbar | `low` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Der behauptete Similaritätstransformations-Schritt setzt die Realität des Spektrums voraus - zirkulär.
> 
> **Hebel:** Zeigt anschaulich, wie ein Operator-Ansatz genau scheitert.
> 
> **Fehlermodi:** [[F3_non-canonical-operator|F3 Nicht-kanonischer Operator]] · [[F4_no-selfadjoint-realization|F4 Fehlende selbstadjungierte Realisierung]] · [[F1_no-euler-product|F1 Euler-Blindheit]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-09`

> [!warning]- Blocker — woran dieser Ansatz hängt (2)
> - **Fehlende selbstadjungierte Realisierung** *(Tier 2)* — Der Operator ist formal hingeschrieben, aber ohne Definitionsbereich, Randbedingungen und Nachweis eines diskreten Spektrums.
>   *Fluchtbedingung:* Hilbertraum, Definitionsbereich und Randbedingungen explizit angeben und wesentliche Selbstadjungiertheit sowie Diskretheit des Spektrums beweisen -- nicht behaupten.
> - **Nicht-kanonischer Operator** *(Tier 2)* — Ein Hilbert–Pólya-Operator wird konstruiert, um das richtige Spektrum zu haben, statt aus der Arithmetik zu entstehen.
>   *Fluchtbedingung:* Der Operator muss auf einem arithmetisch definierten Raum leben (Adele, arithmetic site, gefolierter Raum) UND eine Spurformel erfüllen, deren geometrische Seite die Primzahlterme der expliziten Formel liefert. Selbstadjungiertheit muss auf einem konkret angegebenen Definitionsbereich bewiesen sein, nicht behauptet.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (2)
> - *modelliert* → **Hilbert–Pólya / spektrale Interpretation** — Bender–Brody–Müller PT-Hamiltonian (Selbstadjungiertheit unbewiesen).
> - ← *wird benutzt von* [[56_failure_autopsies|56 · Fehler-Autopsien]] — Autopsie A4: zirkulaere Operatorkonstruktion.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
