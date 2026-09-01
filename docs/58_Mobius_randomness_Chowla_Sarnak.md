---
id: doc-58
number: 58
title: "Möbius-Zufälligkeit: Chowla-Vermutung, Sarnak-Disjunktheit & die Paritätsbarriere"
category: solution-program
status: open
tags: [mobius, chowla, sarnak, parity, liouville, tao, entropy, randomness]
source_file: 58_Mobius_randomness_Chowla_Sarnak.md
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
- Es macht präzise, was „μ verhält sich zufällig" *nicht* heißen darf — und ist damit selbst eine Obstruktion (Fehlermodus `F8 parity-barrier`, Dok. 68).

## Bedeutung / Einordnung
- **Status ehrlich:** RH-benachbart, aber ohne Implikationspfeil in beide Richtungen. Wer „Chowla ⇒ RH" behauptet, irrt.
- Für das Netzwerk wichtig als **Gegengewicht** zu den μ-basierten Kriterien (Dok. 16, 45): sie sind äquivalent, aber der Weg über „Zufälligkeit" ist blockiert.

## Quellen
- S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*, Gordon & Breach 1965.
- [P. Sarnak, *Three lectures on the Möbius function, randomness and dynamics* (IAS)](https://publications.ias.edu/sites/default/files/MobiusFunctionsLectures%282%29.pdf)
- [T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations* (arXiv:1509.05422)](https://arxiv.org/abs/1509.05422)
- [K. Matomäki, M. Radziwiłł, *Multiplicative functions in short intervals* (arXiv:1501.04585)](https://arxiv.org/abs/1501.04585)
- [T. Tao, J. Teräväinen, *The structure of logarithmically averaged correlations of multiplicative functions* (arXiv:1708.02610)](https://arxiv.org/abs/1708.02610)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_probabilistic|Probabilistische Modelle & Statistik]]

| Achse | Wert |
|---|---|
| Familie | probabilistic |
| Implikation | `none` |
| Euler-Produkt | `essential` |
| Positivität | `n/a` |
| Strenge | `theorem` · Evidenz `medium` |
| Testbar / formalisierbar | `high` / `low` |

**Offener Kernschritt:** Korrelationsschranken liefern keine Einzelsummen-Schranke; Paritätsbarriere.

**Hebel (was er liefern würde):** Präzisiert, was 'mu ist zufällig' heißen darf - und was nicht.

**Typische Fehlermodi:** [[F8_parity-barrier|F8 Paritätsbarriere (Sieb-/Multiplikativitätsmethoden)]] · [[F14_model-without-implication|F14 Modell ohne Implikationspfeil]]

**Vergleichbar mit:** [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)]] · [[63_hybrid_Euler_Hadamard_product|Hybrides Euler–Hadamard-Produkt (Gonek–Hughes–Keating)]] · [[64_extreme_values_FHK_multiplicative_chaos|Extremwerte von ζ: Fyodorov–Hiary–Keating & multiplikatives Chaos]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-58 doc-53 doc-63 doc-64`

**Ausgehende Beziehungen**
- *ist Instanz von* (`instance_of`) → [[concept_parity|Paritätsbarriere (Möbius/Sieb)]] — Chowla/Sarnak präzisieren die Zufälligkeit von μ — und stoßen an die Paritätsbarriere.
- *ist Evidenz für* (`evidence_for`) → [[16_Mertens_function_Riesz_criterion|16 — Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]] — Stützt die Heuristik hinter M(x)=O(x^{1/2+ε}), liefert sie aber nicht.
- *benutzt* (`uses`) → [[35_obstructions_barriers|35 — Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN]] — Paritätsproblem (Selberg) als strukturelle Grenze.
- *modelliert* (`models`) → [[39_Cramer_probabilistic_model|39 — Cramér-Modell & probabilistische Heuristiken der Primzahlen]] — Alternatives, präziseres Zufälligkeitsmodell gegenüber Cramér.

**Thematisch benachbart (gemeinsame Tags):** [[54_machine_assisted_number_theory_ANTEDB_Lean|Maschinengestützte Zahlentheorie: ANTEDB, systematische Exponenten-Optimierung und formalisierter Primzahlsatz (2025–2026)]] · [[16_Mertens_function_Riesz_criterion|Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
