---
id: doc-69
number: 69
title: "Möbius-Zufälligkeit: Chowla-Vermutung, Sarnak-Disjunktheit & die Paritätsbarriere"
category: solution-program
status: open
tags: [mobius, chowla, sarnak, parity, liouville, tao, entropy, randomness]
source_file: 69_Mobius_randomness_Chowla_Sarnak.md
lang: de
---

# Möbius-Zufälligkeit: Chowla, Sarnak & die Paritätsbarriere

**Kategorie:** Aktives Programm (analytisch/ergodisch) — RH-benachbart, nicht RH-äquivalent
**Autoren / Jahre:** Chowla (1965); Sarnak (2009/2011); Tao (2016, logarithmische 2-Punkt-Chowla); Tao–Teräväinen (2018/2019, ungerade Ordnungen); Matomäki–Radziwiłł (2016, kurze Intervalle)
**Typ:** Präzisierung der „Zufälligkeit" von μ(n) — und die Diagnose, warum sie die RH *nicht* liefert
**Status:** offen (Chowla, Sarnak); wichtige Teilresultate bewiesen

## Zusammenfassung
Die RH ist äquivalent zu einer Abschätzung der Mertens-Funktion: `M(x) = Σ_{n≤x} μ(n) = O(x^{1/2+ε})` (Dok. 16). Das legt nahe, μ(n) als „Zufallsvorzeichen" zu behandeln. Die **Chowla-Vermutung** und die **Sarnak-Vermutung** machen diese Zufälligkeit präzise — und die letzten zehn Jahre haben dort echte Durchbrüche gebracht. Dieses Dokument erklärt, *warum diese Fortschritte die RH trotzdem nicht näher bringen*: sie kontrollieren **Korrelationen**, die RH verlangt aber die **Größe einer einzigen Summe** — und dazwischen steht die Paritätsbarriere.

## Mathematischer Kern

### Chowla-Vermutung (1965)
Für die Liouville-Funktion λ(n) = (−1)^{Ω(n)} und paarweise verschiedene h_1,…,h_k ≥ 0:
```
Σ_{n≤x} λ(n+h_1)·λ(n+h_2)···λ(n+h_k)  =  o(x)     (x → ∞).
```
Der Fall k = 1 ist genau der Primzahlsatz. Bereits **k = 2 ist offen**. Bewiesen ist die *logarithmisch gemittelte* Version für k = 2 (Tao 2016):
```
Σ_{n≤x} λ(n)λ(n+h)/n  =  o(log x)   für jedes feste h ≥ 1,
```
sowie logarithmische Chowla für alle **ungeraden** k (Tao–Teräväinen).

### Sarnak-Vermutung (2009)
Für **jedes** topologische dynamische System (X, T) mit topologischer Entropie 0 und jede stetige f sowie jedes x ∈ X:
```
(1/N) Σ_{n≤N} μ(n) · f(T^n x)  →  0.
```
„μ ist disjunkt von allem, was nicht chaotisch ist."
- **Sarnak:** Chowla ⇒ Sarnak. (Die Umkehrung ist im logarithmischen Mittel ebenfalls bekannt, Tao 2017.)
- Bewiesen für viele Klassen: Nilsysteme (Green–Tao), horozyklische Flüsse (Bourgain–Sarnak–Ziegler), Interval-Exchange-Klassen, endliche Automaten (Müllner) u. v. m.

### Matomäki–Radziwiłł (2016) — Multiplikativität in kurzen Intervallen
```
(1/x) ∫ | (1/H) Σ_{y<n≤y+H} λ(n) | dy  =  o(1)   für H → ∞ beliebig langsam.
```
Das ist der technische Motor hinter Taos Chowla-Fortschritt und ein Resultat, das vor 2015 als unerreichbar galt.

### Warum das die RH nicht liefert — drei präzise Gründe
1. **Falsche Norm.** RH ⟺ `M(x) ≪ x^{1/2+ε}`, eine **Größenaussage über die Einzelsumme** mit Exponentengenauigkeit. Chowla/Sarnak liefern `o(x)`-Aussagen über **Korrelationen**; jede bekannte Ableitung von M(x)-Schranken aus Korrelationsschranken verliert genau den Exponentengewinn, auf den es ankommt. Aus Chowla folgt (bekanntermaßen) **nicht** die RH; umgekehrt folgt aus der RH auch nicht Chowla.
2. **Paritätsbarriere (Selberg).** Siebmethoden können Zahlen mit gerader/ungerader Primfaktoranzahl prinzipiell nicht trennen (Dok. 35, §3). μ und λ *messen* genau diese Parität. Alle bisherigen Erfolge (Matomäki–Radziwiłł, Tao) umgehen die Barriere durch **Mittelung** (über y, oder logarithmisch) — sie durchbrechen sie nicht. Eine Einzelsummen-Schranke der Stärke x^{1/2+ε} ist genau das, was die Mittelung nicht mehr hergibt.
3. **Mertens-Warnung.** `M(x) ≪ √x` (Mertens-Vermutung) ist **widerlegt** (Odlyzko–te Riele 1985, Dok. 16). Die RH-Version braucht das ε und ist damit knapp jenseits der widerlegten Aussage — jedes Argument, das „μ ist im Wesentlichen ein fairer Münzwurf" wörtlich nimmt, beweist zu viel und ist deshalb falsch (das Gesetz vom iterierten Logarithmus gäbe `√(x log log x)`, was die widerlegte Grenze mit einbezieht — ein guter Lackmustest).

### Was das Programm doch für die RH tut
- Es liefert das **richtige Zufälligkeitsmodell** und dessen Grenzen — komplementär zu Cramér (Dok. 39) und zur Maier-Warnung.
- Techniken (Entropie-Zerlegung, Multiplikativität in kurzen Intervallen) fließen in die **Momenten-** und **Dichte**-Literatur ein (Dok. 49, Harper).
- Es macht präzise, was „μ verhält sich zufällig" *nicht* heißen darf — und ist damit selbst eine Obstruktion (Fehlermodus `F8 parity-barrier`, Dok. 55).

## Bedeutung / Einordnung
- **Status ehrlich:** RH-benachbart, aber ohne Implikationspfeil in beide Richtungen. Wer „Chowla ⇒ RH" behauptet, irrt.
- Für das Netzwerk wichtig als **Gegengewicht** zu den μ-basierten Kriterien (Dok. 16, 45): sie sind äquivalent, aber der Weg über „Zufälligkeit" ist blockiert.

## Quellen
- S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*, Gordon & Breach 1965.
- [P. Sarnak, *Three lectures on the Möbius function, randomness and dynamics* (IAS)](https://publications.ias.edu/sites/default/files/MobiusFunctionsLectures%282%29.pdf)
- [T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations* (arXiv:1509.05422)](https://arxiv.org/abs/1509.05422)
- [K. Matomäki, M. Radziwiłł, *Multiplicative functions in short intervals* (arXiv:1501.04585)](https://arxiv.org/abs/1501.04585)
- [T. Tao, J. Teräväinen, *The structure of logarithmically averaged correlations of multiplicative functions* (arXiv:1708.02610)](https://arxiv.org/abs/1708.02610)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `probabilistic` |
> | Implikation | `none` |
> | Euler-Produkt | `essential` |
> | Positivität | `n/a` |
> | Strenge | `theorem` |
> | Evidenz | `medium` |
> | Testbar | `high` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Korrelationsschranken liefern keine Einzelsummen-Schranke; Paritätsbarriere.
> 
> **Hebel:** Präzisiert, was 'mu ist zufällig' heißen darf - und was nicht.
> 
> **Fehlermodi:** [[F8_parity-barrier|F8 Paritätsbarriere]] · [[F14_model-without-implication|F14 Zirkularität der Modellannahme]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-69`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Paritätsbarriere** *(Tier 1)* — Siebmethoden können gerade und ungerade Primfaktorzahl prinzipiell nicht trennen — genau das misst μ(n).
>   *Fluchtbedingung:* Ein bilinearer Input (Typ-II-Summen), ein Spektralinput (automorphe Formen) oder eine andere Quelle von Kancellation, die nicht aus dem Sieb selbst kommt.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (4)
> - *ist Evidenz für* → [[16_Mertens_function_Riesz_criterion|16 · Mertens-Funktion & Riesz-Kriterium]] — Stützt die Heuristik hinter M(x)=O(x^{1/2+ε}), liefert sie aber nicht.
> - *ist Instanz von* → **Paritätsbarriere (Möbius/Sieb)** — Chowla/Sarnak präzisieren die Zufälligkeit von μ — und stoßen an die Paritätsbarriere.
> - *modelliert* → [[39_Cramer_probabilistic_model|39 · Cramér-Modell & probabilistische Heuristiken der Pr…]] — Alternatives, präziseres Zufälligkeitsmodell gegenüber Cramér.
> - *benutzt* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Paritätsproblem (Selberg) als strukturelle Grenze.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
