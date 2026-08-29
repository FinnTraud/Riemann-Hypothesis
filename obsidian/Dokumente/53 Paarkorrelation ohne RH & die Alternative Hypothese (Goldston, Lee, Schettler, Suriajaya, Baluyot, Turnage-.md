---
id: doc-53
title: "Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)"
nummer: "53"
kategorie: Partielle Resultate
status: OFFEN
typ: dokument
aliases:
  - "doc-53"
  - "Dok. 53"
tags:
  - "dokument"
  - "kategorie/partial-results"
  - "status/open"
  - "thema/2025"
  - "thema/2026"
  - "thema/active"
  - "thema/alternative-hypothesis"
  - "thema/critical-line"
  - "thema/essential-simplicity"
  - "thema/gallagher-mueller"
  - "thema/goldston"
  - "thema/montgomery"
  - "thema/pair-correlation"
  - "thema/simple-zeros"
  - "thema/suriajaya"
quelle: docs/53_pair_correlation_alternative_hypothesis.md
---

> [!info] Navigation
> **Karte:** [[MOC O – Aktuelle Front 2025–2026 (Recherche-Update August 2026)]] · **Kategorie:** Partielle Resultate · **Status:** `OFFEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/53_pair_correlation_alternative_hypothesis.md`

# Paarkorrelation ohne RH & die Alternative Hypothese (2025–2026)

**Kategorie:** Partielle Resultate / vertikale & horizontale Nullstellenverteilung
**Autoren / Jahre:** Goldston–Lee–Schettler–Suriajaya (2025, zwei Teile);
Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (2025); Goldston–Suriajaya (2025/26)
**Typ:** Bedingte Struktursätze (Hebelwirkung), Verschärfung der Alternativen Hypothese
**Status:** **[OFFEN]** als RH-Aussage; die *Implikationen* sind **[BEWIESEN]**

## Zusammenfassung
Montgomerys Paarkorrelationsmethode (Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]]) war seit 1973 immer an die RH gekoppelt: Man
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
Die AH ist das hartnäckigste Gegenszenario zum GUE-Bild (Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]]). Sie behauptet, dass die
normierten Nullstellenabstände im Wesentlichen in `(1/2)·ℤ` konzentriert sind:
```
(γ' − γ) · (log T)/(2π)  ∈  { k/2 : k ∈ ℤ }   (asymptotisch),
```
also Vielfache des *halben* mittleren Abstands. Die AH ist mit GUE unvereinbar, aber bis heute
**nicht ausgeschlossen** — und sie hängt eng mit Landau–Siegel-Ausnahmenullstellen zusammen
(Dok. [[32 Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)|32]]): Ein Szenario mit Siegel-Nullstellen erzwingt AH-artige Starrheit im Abstandsspektrum.

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
Nachfolger, Dok. [[04 Levinson, Conrey & Co. – Positiver Anteil der Nullstellen auf der kritischen Geraden|04]]). Ein solcher Schritt wäre also eine deutliche Verbesserung — und er ist
präzise als offene Aufgabe formuliert.

## Bedeutung / Einordnung
- **Statusfalle vermeiden:** Alle diese 100-%-Aussagen sind **bedingt** (an PCC bzw. AH-PCC).
  Sie sind *keine* unbedingten Fortschritte und dürfen nie als solche zitiert werden.
- **Warum es trotzdem wichtig ist:** Die Ergebnisse verschieben die Beweislast. Bisher galt
  Paarkorrelation als „nur unter RH sinnvoll". Jetzt ist die PCC ein eigenständiges Ziel, dessen
  Nachweis direkt die kritische Gerade träfe.
- **AH als Prüfstein:** Wer ein RH-Programm vorschlägt, sollte sagen können, wie es sich zum
  AH-Szenario verhält (vgl. Dok. [[32 Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)|32]], [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]]). Teil II zeigt: Für Gallagher–Mueller-artige Argumente
  ist die AH kein Ausweg.
- **Verbindung zur Numerik:** Die GUE-Abstandsstatistik in `kb/research/spacing_vs_gue.py` testet
  genau das Bild, gegen das die AH antritt — ein AH-artiges Spektrum würde sich dort als
  Häufung bei halbzahligen normierten Abständen zeigen.

## Anschlüsse in dieser Wissensbasis
- Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]] (Montgomery, GUE), 07 (Keating–Snaith) — der statistische Rahmen
- Dok. [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden|03]], [[04 Levinson, Conrey & Co. – Positiver Anteil der Nullstellen auf der kritischen Geraden|04]] (Hardy; Levinson/Conrey ~41 %) — der unbedingte Vergleichsmaßstab
- Dok. [[32 Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)|32]] (Landau–Siegel-Nullstellen) — die arithmetische Quelle AH-artiger Szenarien
- Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]] (Obstruktionen) — warum „100 % unter einer Vermutung" nicht „bewiesen" heißt
- `kb/research/spacing_vs_gue.py` — das zugehörige Experiment im Repo

## Quellen
- [Goldston, Lee, Schettler, Suriajaya — *Pair Correlation Conjecture … I: Simple and Critical Zeros* (arXiv:2503.15449)](https://arxiv.org/abs/2503.15449)
- [Goldston, Lee, Schettler, Suriajaya — *Pair Correlation Conjecture … II: The Alternative Hypothesis* (arXiv:2507.06823)](https://arxiv.org/abs/2507.06823)
- [Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh — *The Alternative Hypothesis for Zeros of the Riemann Zeta-Function* (arXiv:2508.10857)](https://arxiv.org/abs/2508.10857)
- [Goldston, Suriajaya — *Zeta Zeros on the Critical Line* (arXiv:2511.20059)](https://arxiv.org/abs/2511.20059)
- [Montgomery — *The pair correlation of zeros of the zeta function* (1973)](https://public.websites.umich.edu/~hlm/paircor1.pdf)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Teilresultat für** → [[Kritische Gerade Re(s)=1∕2]] — *PCC (ohne RH) impliziert 100 % einfache Nullstellen auf der kritischen Geraden.*
- **ist schwächer als** → [[04 Levinson, Conrey & Co. – Positiver Anteil der Nullstellen auf der kritischen Geraden]] — *Die 100-%-Aussagen sind bedingt; unbedingt sind bislang nur ~41 % (Conrey).*
- **nutzt** → [[07 Keating–Snaith – Momente der Zetafunktion via charakteristische Polynome (CUE)]] — *Teilt den Random-Matrix-Rahmen mit Keating-Snaith.*
- **verallgemeinert** → [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]] — *Nimmt die RH-Annahme aus der Gallagher-Mueller-Methode heraus.*

### Eingehende Relationen

- **hat als Instanz** ← [[Alternative Hypothese (AH)]] — *Dok. 53 formuliert und verschaerft die Alternative Hypothese.*
- **hat als Instanz** ← [[Paarkorrelation der Nullstellen (Montgomery F(alpha,T))]] — *Dok. 53 behandelt die Paarkorrelation ohne RH-Annahme.*

### Belegte Aussagen (Claims)

- `[BEWIESEN]` [[claim-pcc-simple-critical]] — Montgomerys Paarkorrelationsvermutung (PCC) impliziert - OHNE Annahme der RH -, dass asymptotisch 100 % der nicht-trivialen Nullstellen einfach sind und auf der kritischen Geraden liegen.
- `[BEWIESEN]` [[claim-ah-pcc-simple-critical]] — Auch die aus einer passend formulierten Alternativen Hypothese folgende Paarkorrelationsvermutung impliziert, dass asymptotisch 100 % der Nullstellen einfach und auf der kritischen Geraden liegen.
- `[BEWIESEN]` [[claim-ah-essential-simplicity]] — Eine verschaerfte Form der Alternativen Hypothese impliziert die Essential Simplicity Hypothesis; unter RH+AH ergeben sich Schranken an die Dichte moeglicher mehrfacher Nullstellen.
- `[OFFEN]` [[claim-alternative-hypothesis]] — Die normierten Abstaende aufeinanderfolgender Nullstellen konzentrieren sich asymptotisch auf Vielfache des halben mittleren Abstands (Alternative Hypothese). Unvereinbar mit GUE, bis heute nicht ausgeschlossen.

### Im Text erwähnt

- [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden]]
- [[32 Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
