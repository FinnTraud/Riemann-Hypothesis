---
id: doc-11
number: 11
title: "Connes–Moscovici: Prolate-Spheroidal-Operator und Zeta (2021–2022)"
category: spectral
status: open
tags: [connes-moscovici, prolate-spheroidal, operator]
source_file: 11_Connes_Moscovici_prolate_spheroidal.md
lang: de
---

# Connes–Moscovici: Prolate-Spheroidal-Operator und Zeta (2021–2022)

**Kategorie:** Spektraler Ansatz / nichtkommutative Geometrie (jüngste Entwicklung)
**Autoren / Jahr:** Alain Connes & Henri Moscovici (2021–2022); verwandt: Connes–Consani "Spectral triples and ζ-cycles" (2021)
**Typ:** Konkrete (approximative) Hilbert–Pólya-Operator-Realisierung
**Status:** Aktive Forschung; "annähernde" Operator-Lösung, kein vollständiger RH-Beweis

## Zusammenfassung
Connes und Moscovici untersuchten ab 2021 das Spektrum des **Prolate-Spheroidal-Wellenoperators** (ein klassischer Differentialoperator aus der Signalverarbeitung / Bandbegrenzung, ursprünglich von Slepian, Landau, Pollak an den Bell Labs studiert) und zeigten, dass dessen Spektrum eng mit den **Quadraten der Riemann-Nullstellen** zusammenhängt. Sie beschreiben dies als eine **konkrete, annähernde Realisierung der Hilbert–Pólya-Vermutung**.

## Kernidee
- Der **Prolate-Operator** ist ein expliziter, gut studierter selbstadjungierter Differentialoperator zweiter Ordnung.
- Schränkt man ihn auf das Komplement eines endlichen Intervalls ein, so besitzt er **negative Eigenwerte**, deren Ultraviolett-Verhalten (asymptotisches Wachstum) genau dem der **Quadrate der ζ-Nullstellen** entspricht.
- Auf einem größeren Definitionsbereich eindeutig selbstadjungiert fortgesetzt, sind die Eigenwerte asymptotisch ähnlich zu den Quadraten der Nullstellen; eine geeignete "Quadratwurzel" dieses Operators liefert damit einen Operator, der die Hilbert–Pólya-Vermutung **näherungsweise** löst.
- Eingebettet in das **semilokale Spurformel-Framework** von Connes (Dok. 10): ein semilokales Analogon des Prolate-Wellenoperators integriert zwei jüngere Entdeckungen zur spektralen Realisierung der Nullstellen.

## Bedeutung / Einordnung
- Erstmals ein **klassischer, explizit bekannter** Operator (kein ad-hoc konstruierter), dessen Spektrum strukturell die Nullstellen widerspiegelt — methodisch bemerkenswert.
- Verbindet Signalverarbeitung / Spektraltheorie / nichtkommutative Geometrie / Zahlentheorie.
- **Einschränkung:** Die Übereinstimmung ist asymptotisch/approximativ ("ultraviolettes Verhalten", "annähernde Lösung"). Eine *exakte* spektrale Realisierung *aller* Nullstellen samt Beweis der RH ist damit **nicht** erreicht.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Der Prolate-Wellenoperator
Klassischer Slepian–Landau–Pollak-Operator auf L²(−1,1), kommutierend mit der bandbegrenzten Fourier-Projektion:
```
(W_λ f)(x) = d/dx [ (1 − x²) df/dx ] + λ² x² f
```
W_λ ist selbstadjungiert mit diskretem Spektrum; seine Eigenfunktionen sind die **prolaten Sphäroidwellenfunktionen** (PSWF). Connes–Moscovici untersuchen die Einschränkung auf das **Komplement** eines Intervalls.

### Schlüsselresultat (asymptotisches Spektrum)
Für die selbstadjungierte Fortsetzung des auf das Außenintervall eingeschränkten Operators gilt: die negativen Eigenwerte −E_n erfüllen asymptotisch (Ultraviolett-Verhalten)
```
E_n  ~  (γ_n / 2)²   bzw.   die Zählfunktion der E_n  ≈  Zählfunktion der  γ_n²
```
wobei γ_n die Imaginärteile der nicht-trivialen Nullstellen sind. D. h.: das Spektrum reproduziert die **Quadrate der Riemann-Nullstellen**.

### Quadratwurzel ⇒ approximative Hilbert–Pólya-Lösung
Definiert man (heuristisch) den Operator √(Prolate) auf dem passenden Teilraum, so hat dieser Eigenwerte ≈ γ_n/2 — ein konkreter selbstadjungierter Operator, dessen Spektrum die γ_n *approximiert*. Wegen Selbstadjungiertheit sind diese reell (das war stets das Ziel, Dok. 05). Daher: „konkrete annähernde Realisierung der Hilbert–Pólya-Vermutung".

### Einbettung in die semilokale Spurformel
Connes setzt dies in das **semilokale** Framework (endlich viele Stellen S = {∞, p_1, …, p_k}): ein semilokaler Prolate-Operator W_S, dessen Spurformel die explizite Formel über S realisiert (vgl. Dok. 10). Die zu erreichende Aussage bleibt die globale Positivität.

### Warum nur approximativ
Die Übereinstimmung E_n ~ (γ_n/2)² ist **asymptotisch** (führende Ordnung im UV); die exakte Identität des Spektrums mit allen γ_n — und damit RH — ist nicht etabliert. Korrekturterme und die Niederenergie-Region sind nicht kontrolliert.

## Quellen
- [Prolate spheroidal operator and Zeta — Connes & Moscovici (arXiv 2112.05500)](https://arxiv.org/pdf/2112.05500)
- [Prolate operator and Riemann Zeta — Connes (PNAS)](https://alainconnes.org/wp-content/uploads/PNAS_030322.pdf)
- [Prolate spheroidal functions and zeta — Alain Connes (Blog)](https://alainconnes.org/2021/12/prolate-spheroidal-functions-and-zeta/)
- [Zeta cycles — Connes–Consani (arXiv 2106.01715)](https://alainconnes.org/wp-content/uploads/zeta-cycles-3.pdf)
- [The Hilbert-Pólya Conjecture and the Prolate Spheroidal Operator (TU Delft thesis)](https://repository.tudelft.nl/file/File_a03b023e-2ba7-45fb-bde9-6fcc7a53d306)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `spectral` |
> | Implikation | `partial` |
> | Euler-Produkt | `essential` |
> | Positivität | `must-prove` |
> | Strenge | `program` |
> | Evidenz | `medium` |
> | Testbar | `medium` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Vom abgeschnittenen (skalierungsinvarianten) Modell zum unbeschränkten Limes.
> 
> **Hebel:** Konkreter, numerisch zugänglicher Operator mit Bezug zu ζ.
> 
> **Fehlermodi:** [[F9_truncation-limit-gap|F9 Konvergenz- / Grenzübergangslücke]] · [[F2_positivity-assumed|F2 Zirkuläre Positivität]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-11`

> [!warning]- Blocker — woran dieser Ansatz hängt (3)
> - **Konvergenz- / Grenzübergangslücke** *(Tier 2)* — Für jede endliche Abschneidung bewiesen — der Grenzübergang ist offen.
>   *Fluchtbedingung:* Eine von Λ (bzw. N, d) UNABHÄNGIGE Schranke — Kompaktheit, gleichgradige Stetigkeit oder eine explizite Fehlerabschätzung, die den Grenzübergang erlaubt.
> - **Fehlende selbstadjungierte Realisierung** *(Tier 2)* — Der Operator ist formal hingeschrieben, aber ohne Definitionsbereich, Randbedingungen und Nachweis eines diskreten Spektrums.
>   *Fluchtbedingung:* Hilbertraum, Definitionsbereich und Randbedingungen explizit angeben und wesentliche Selbstadjungiertheit sowie Diskretheit des Spektrums beweisen -- nicht behaupten.
> - **Nicht-kanonischer Operator** *(Tier 2)* — Ein Hilbert–Pólya-Operator wird konstruiert, um das richtige Spektrum zu haben, statt aus der Arithmetik zu entstehen.
>   *Fluchtbedingung:* Der Operator muss auf einem arithmetisch definierten Raum leben (Adele, arithmetic site, gefolierter Raum) UND eine Spurformel erfüllen, deren geometrische Seite die Primzahlterme der expliziten Formel liefert. Selbstadjungiertheit muss auf einem konkret angegebenen Definitionsbereich bewiesen sein, nicht behauptet.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (2)
> - *modelliert* → **Hilbert–Pólya / spektrale Interpretation** — Prolate-Operator: approximative HP-Realisierung.
> - ← *wird benutzt von* [[52_Connes_truncated_Weil_spectral_realization|52 · Abgeschnittene Weil-Quadratform & Zeta-Spektraltrip…]] — Setzt die Connes-Moscovici-Linie (prolate spheroidal, Skalierungsoperator) fort.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
