---
id: doc-53
number: 53
title: "Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)"
category: partial-results
status: open
tags: [pair-correlation, montgomery, alternative-hypothesis, simple-zeros, critical-line, gallagher-mueller, essential-simplicity, goldston, suriajaya, 2025, 2026, active]
source_file: 53_pair_correlation_alternative_hypothesis.md
lang: de
---

# Paarkorrelation ohne RH & die Alternative Hypothese (2025–2026)

**Kategorie:** Partielle Resultate / vertikale & horizontale Nullstellenverteilung
**Autoren / Jahre:** Goldston–Lee–Schettler–Suriajaya (2025, zwei Teile);
Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (2025); Goldston–Suriajaya (2025/26)
**Typ:** Bedingte Struktursätze (Hebelwirkung), Verschärfung der Alternativen Hypothese
**Status:** **[OFFEN]** als RH-Aussage; die *Implikationen* sind **[BEWIESEN]**

## Zusammenfassung
Montgomerys Paarkorrelationsmethode (Dok. 06) war seit 1973 immer an die RH gekoppelt: Man
*nahm* die RH an und bekam Aussagen über die *vertikale* Verteilung der Nullstellen. Die
Arbeiten 2025/26 drehen das um. Zwei Ergebnisse sind für die Wissensbasis zentral:

1. **Die RH lässt sich aus Gallagher–Mueller herausnehmen.** Die Paarkorrelationsvermutung (PCC)
   allein — *ohne* RH — impliziert bereits, dass asymptotisch 100 % der Nullstellen **einfach**
   *und* **auf der kritischen Geraden** liegen.
2. **Auch die Alternative Hypothese hilft nicht dagegen.** Formuliert man die Alternative
   Hypothese (AH) passend, liefert sie eine *andere* PCC — und dieselbe Methode ergibt wieder
   100 % einfache Nullstellen auf der kritischen Geraden.

Damit wird Paarkorrelation von einem Werkzeug *unter* RH zu einem Werkzeug, das *auf* die
kritische Gerade zielt.

## Mathematischer Kern

### Montgomerys Form und die PCC
Mit `γ, γ'` über den Imaginärteilen der nicht-trivialen Nullstellen und `w(u) = 4/(4+u²)`:
```
F(α, T) = ( T/(2π) · log T )⁻¹ · Σ_{0<γ,γ'≤T} T^{iα(γ−γ')} · w(γ − γ') ,   α ∈ ℝ .
```
Montgomery bewies (unter RH) `F(α) ~ |α| + T^{−2α} log T` für `0 ≤ α ≤ 1` und vermutete
```
F(α, T) → 1     für α ≥ 1   (Paarkorrelationsvermutung, PCC),
```
äquivalent zur GUE-Paarkorrelation
```
1 − ( sin(πu)/(πu) )²  .
```
Klassische Folgerung (Montgomery 1973): **mindestens 2/3** der Nullstellen sind einfach.
Gallagher–Mueller (1978): PCC **unter RH** ⇒ asymptotisch **100 %** einfach.

### Teil I — die RH-Annahme fällt weg (arXiv:2503.15449)
Goldston, Lee, Schettler, Suriajaya zeigen, dass die Methode von Gallagher–Mueller die RH
**nicht wirklich benutzt**. Daraus:

- Montgomerys zweite Vermutung (100 % einfache Nullstellen) folgt aus der PCC **allein**.
- Wendet man zusätzlich die neueren Ideen an, mit denen Paarkorrelation auch die *horizontale*
  Verteilung (Realteile!) kontrolliert, so gilt:
```
PCC  ⇒  asymptotisch 100 % der Nullstellen sind einfach UND liegen auf Re(s) = 1/2 .
```
Das ist eine echte Hebelwirkung: eine rein *statistische* Vermutung über Abstände liefert eine
*geometrische* Aussage über die Lage.

### Die Alternative Hypothese (AH)
Die AH ist das hartnäckigste Gegenszenario zum GUE-Bild (Dok. 06). Sie behauptet, dass die
normierten Nullstellenabstände im Wesentlichen in `(1/2)·ℤ` konzentriert sind:
```
(γ' − γ) · (log T)/(2π)  ∈  { k/2 : k ∈ ℤ }   (asymptotisch),
```
also Vielfache des *halben* mittleren Abstands. Die AH ist mit GUE unvereinbar, aber bis heute
**nicht ausgeschlossen** — und sie hängt eng mit Landau–Siegel-Ausnahmenullstellen zusammen
(Dok. 32): Ein Szenario mit Siegel-Nullstellen erzwingt AH-artige Starrheit im Abstandsspektrum.

### Teil II — AH führt zum selben Ergebnis (arXiv:2507.06823)
Dieselben Autoren formulieren eine passende Form der AH, leiten die daraus folgende (andere) PCC
ab und zeigen mit der Gallagher–Mueller-Methode erneut:
```
AH-PCC  ⇒  asymptotisch 100 % der Nullstellen sind einfach UND auf der kritischen Geraden .
```
Interpretation: Das AH-Szenario ist **kein Schlupfloch** gegen diese Art von Argument.

### Die AH ohne Einfachheitsannahme (arXiv:2508.10857)
Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh knüpfen an Baluyots Formulierung von 2016 an,
die aufeinanderfolgende Nullstellen bei Vielfachen des halben mittleren Abstands ansetzt, **ohne**
Einfachheit vorauszusetzen. Unter RH + AH erhalten sie:

- Schranken an die Dichte der Nullstellenpaare mit normierter Differenz `k/2`;
- daraus **Einschränkungen an die Dichte möglicher mehrfacher Nullstellen**;
- eine verschärfte AH-Variante, die die **Essential Simplicity Hypothesis** impliziert.

### Expositorische Zuspitzung (arXiv:2511.20059)
Goldston–Suriajaya, „Zeta Zeros on the Critical Line" (9 Seiten): Könnte man die RH auch aus
Montgomerys *ursprünglichem* 2/3-Beweis herausnehmen, so bekäme man unmittelbar
```
≥ 2/3 der Nullstellen sind einfach UND liegen auf der kritischen Geraden — unbedingt.
```
Zum Vergleich: der beste *unbedingte* Anteil auf der Geraden ist derzeit ~41 % (Conrey und
Nachfolger, Dok. 04). Ein solcher Schritt wäre also eine deutliche Verbesserung — und er ist
präzise als offene Aufgabe formuliert.

## Bedeutung / Einordnung
- **Statusfalle vermeiden:** Alle diese 100-%-Aussagen sind **bedingt** (an PCC bzw. AH-PCC).
  Sie sind *keine* unbedingten Fortschritte und dürfen nie als solche zitiert werden.
- **Warum es trotzdem wichtig ist:** Die Ergebnisse verschieben die Beweislast. Bisher galt
  Paarkorrelation als „nur unter RH sinnvoll". Jetzt ist die PCC ein eigenständiges Ziel, dessen
  Nachweis direkt die kritische Gerade träfe.
- **AH als Prüfstein:** Wer ein RH-Programm vorschlägt, sollte sagen können, wie es sich zum
  AH-Szenario verhält (vgl. Dok. 32, 35). Teil II zeigt: Für Gallagher–Mueller-artige Argumente
  ist die AH kein Ausweg.
- **Verbindung zur Numerik:** Die GUE-Abstandsstatistik in `kb/research/spacing_vs_gue.py` testet
  genau das Bild, gegen das die AH antritt — ein AH-artiges Spektrum würde sich dort als
  Häufung bei halbzahligen normierten Abständen zeigen.

## Anschlüsse in dieser Wissensbasis
- Dok. 06 (Montgomery, GUE), 07 (Keating–Snaith) — der statistische Rahmen
- Dok. 03, 04 (Hardy; Levinson/Conrey ~41 %) — der unbedingte Vergleichsmaßstab
- Dok. 32 (Landau–Siegel-Nullstellen) — die arithmetische Quelle AH-artiger Szenarien
- Dok. 35 (Obstruktionen) — warum „100 % unter einer Vermutung" nicht „bewiesen" heißt
- `kb/research/spacing_vs_gue.py` — das zugehörige Experiment im Repo

## Quellen
- [Goldston, Lee, Schettler, Suriajaya — *Pair Correlation Conjecture … I: Simple and Critical Zeros* (arXiv:2503.15449)](https://arxiv.org/abs/2503.15449)
- [Goldston, Lee, Schettler, Suriajaya — *Pair Correlation Conjecture … II: The Alternative Hypothesis* (arXiv:2507.06823)](https://arxiv.org/abs/2507.06823)
- [Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh — *The Alternative Hypothesis for Zeros of the Riemann Zeta-Function* (arXiv:2508.10857)](https://arxiv.org/abs/2508.10857)
- [Goldston, Suriajaya — *Zeta Zeros on the Critical Line* (arXiv:2511.20059)](https://arxiv.org/abs/2511.20059)
- [Montgomery — *The pair correlation of zeros of the zeta function* (1973)](https://public.websites.umich.edu/~hlm/paircor1.pdf)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Zirkularität der Modellannahme** *(Tier 3)* — Zufallsmatrix- und probabilistische Modelle setzen die RH voraus, um überhaupt formuliert werden zu können.
>   *Fluchtbedingung:* Unbedingte Formulierung: Aussagen über Nullstellen ohne die Annahme, dass sie auf der Geraden liegen (doc-53 ist der Prototyp).
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!missing]- Die fehlende Aussage
> **Bewiesen:** Paarkorrelationsresultate ohne RH-Annahme; aus der Paarkorrelationsvermutung folgt, dass 100 % der Nullstellen einfach sind und auf der kritischen Geraden liegen.
> **Es fehlt:** Die Paarkorrelationsvermutung selbst — bzw. der Ausschluss der Alternativen Hypothese (Abstände konzentriert auf halbzahligen Vielfachen).
> **Typ:** bedingt auf offene vermutung · Bewertung: [[58_gap_registry_near_miss]]

> [!abstract]- Graph-Nachbarn (6)
> - *verallgemeinert* → [[06_Montgomery_pair_correlation_RMT|06 · Montgomery-Paarkorrelation & Random-Matrix-Theorie]] — Nimmt die RH-Annahme aus der Gallagher-Mueller-Methode heraus.
> - *ist Teilresultat für* → **Kritische Gerade Re(s)=1/2** — PCC (ohne RH) impliziert 100 % einfache Nullstellen auf der kritischen Geraden.
> - *benutzt* → [[07_Keating_Snaith_moments|07 · Keating–Snaith]] — Teilt den Random-Matrix-Rahmen mit Keating-Snaith.
> - *schwächer als* → [[04_Levinson_Conrey_positive_proportion|04 · Levinson, Conrey & Co.]] — Die 100-%-Aussagen sind bedingt; unbedingt sind bislang nur ~41 % (Conrey).
> - ← *hat Instanz* **Paarkorrelation der Nullstellen (Montgomery F(alpha,T))** — Dok. 53 behandelt die Paarkorrelation ohne RH-Annahme.
> - ← *hat Instanz* **Alternative Hypothese (AH)** — Dok. 53 formuliert und verschaerft die Alternative Hypothese.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
