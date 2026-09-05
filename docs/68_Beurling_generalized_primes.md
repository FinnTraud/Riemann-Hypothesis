---
id: doc-68
number: 68
title: "Beurlingsche verallgemeinerte Primzahlen: Euler-Produkt allein genügt nicht"
category: obstruction
status: proven
tags: [beurling, generalized-primes, diamond-montgomery-vorhauer, axioms, obstruction, euler-product]
source_file: 68_Beurling_generalized_primes.md
lang: de
---

# Beurlingsche verallgemeinerte Primzahlen — die zweite große Obstruktion

**Kategorie:** Obstruktion (Axiom-Ebene) / bewiesene Negativresultate
**Autoren / Jahre:** Arne Beurling (1937); Diamond (1970er); Diamond–Montgomery–Vorhauer (2006); Kahane, Hilberdink, Zhang (2000er–2010er)
**Typ:** Gegenbeispiel-Klasse: Systeme mit Euler-Produkt, aber ohne RH
**Status:** BEWIESEN (als Negativresultat)

## Zusammenfassung
Die Davenport–Heilbronn-Funktion (Dok. 35) zeigt: *Funktionalgleichung ohne Euler-Produkt genügt nicht.* Die Beurlingschen verallgemeinerten Primzahlsysteme zeigen die **komplementäre** Aussage: *Euler-Produkt ohne die additive Struktur der ganzen Zahlen genügt ebenfalls nicht.* Zusammen bilden die beiden Resultate die schärfste bekannte Einkreisung dessen, was ein RH-Beweis benutzen **muss**.

## Mathematischer Kern

### Definition (Beurling 1937)
Ein **Beurling-System** ist eine Folge reeller „Primzahlen"
```
1 < p_1 ≤ p_2 ≤ p_3 ≤ …  →  ∞,
```
aus der man die „ganzen Zahlen" als alle endlichen Produkte `n = p_{i_1}^{a_1}···p_{i_k}^{a_k}` bildet (mit Vielfachheit). Zähfunktionen:
```
π(x) = #{ p_i ≤ x },      N(x) = #{ n ≤ x }.
```
Die zugehörige Zetafunktion ist **per Konstruktion multiplikativ**:
```
ζ_B(s) = Σ_n n^{−s} = Π_i (1 − p_i^{−s})^{−1}.
```
Das Euler-Produkt ist also **axiomatisch vorhanden** — genau das, was Davenport–Heilbronn fehlt.

### Beurlings Satz (1937)
```
Falls  N(x) = ρ·x + O( x · (log x)^{−γ} )  mit  γ > 3/2,
dann gilt der Primzahlsatz:  π(x) ~ x/log x.
```
Die Schranke γ > 3/2 ist **scharf**: Diamond konstruierte ein System mit γ = 3/2, für das der Primzahlsatz **falsch** ist. Es gibt also eine echte, quantitative Grenze dafür, wie viel „Analysis" allein aus der Dichteinformation herausholen kann.

### Diamond–Montgomery–Vorhauer (2006): große Oszillation
**Satz.** Es existiert ein Beurling-System mit
```
N(x) = ρx + O(x·exp(−c √(log x)))
```
— also mit einer Dichte, die so gut ist wie das, was man klassisch über ℤ beweist — dessen Zetafunktion **eine Nullstelle in der Halbebene Re(s) > 1 − C/ log(|t|+2)** besitzt, d. h. **die klassische nullstellenfreie Region (Dok. 12) ist im Beurling-Rahmen optimal**, und ein „RH-Analogon" ist für solche Systeme schlicht falsch.

**Konsequenz.** Kein Beweis, der nur benutzt:
- Multiplikativität / Euler-Produkt,
- eine gute Asymptotik der Zählfunktion N(x),
- Standard-Tauber-/Kontur-Analysis,

kann die RH liefern — denn genau diese Zutaten hat das DMV-System, und dort ist die Aussage falsch. Was den Beurling-Systemen fehlt, ist die **additive** Struktur von ℤ: Es gibt keine Funktionalgleichung, keine Poisson-Summation, keine Modularität, kein θ-Funktions-Argument (Dok. 73).

### Die „Zwei-Säulen"-Einkreisung
| Gegenbeispiel-Klasse | hat | fehlt | Lehre |
|---|---|---|---|
| Davenport–Heilbronn (Dok. 35) | Funktionalgleichung, Fortsetzung, Wachstum | Euler-Produkt | Multiplikativität ist **notwendig** |
| Beurling / DMV (dieses Dok.) | Euler-Produkt, gute Dichte | Funktionalgleichung / additive Struktur | Die additive Seite ist **notwendig** |

**Notwendige Bedingung für jeden RH-Beweis:** Er muss an mindestens einer Stelle beide Strukturen **gleichzeitig** koppeln — multiplikativ (Primzahlen) und additiv/archimedisch (Funktionalgleichung, Poisson-Summation, Skalierung). Genau diese Kopplung ist der Inhalt der expliziten Formel (Dok. 02) und der Weil-Positivität (Dok. 14) — und genau dort sitzt die eigentliche Schwierigkeit.

### Weitere Ergebnisse dieser Linie
- **Kahane, Hilberdink–Lapidus:** Beurling-Systeme mit vorgegebenem Nullstellenverhalten; Verbindungen zur Fraktalgeometrie (Dok. 44).
- **Zhang, Debruyne–Vindas (2010er):** verfeinerte Äquivalenzen zwischen Dichte-Bedingungen an N(x) und der Gültigkeit des PNT bzw. Fehlerterm-Größen — eine „Landkarte", welche analytische Annahme welche Konsequenz kauft.

## Bedeutung / Einordnung
- **Tier-1-Obstruktion**, gleichrangig mit Davenport–Heilbronn — im Anti-Crackpot-Filter (Dok. 35, Dok. 41) als zusätzliche Prüffrage: *„Würde das Argument in einem Beurling-System durchgehen? Falls ja → falsch."*
- Erklärt, warum rein **siebtheoretische** oder rein **multiplikative** Zugänge (Dok. 69) an der RH scheitern müssen.
- Erklärt indirekt, warum die bewiesenen Analoga (Dok. 18, 19) funktionieren: dort *gibt* es beide Strukturen gleichzeitig (Frobenius + Geometrie bzw. Geodäten + Laplace).

## Quellen
- A. Beurling, *Analyse de la loi asymptotique de la distribution des nombres premiers généralisés I*, Acta Math. 68 (1937).
- H. G. Diamond, H. L. Montgomery, U. Vorhauer, *Beurling primes with large oscillation*, Math. Ann. 334 (2006), 1–36.
- H. G. Diamond, W.-B. Zhang, *Beurling Generalized Numbers*, AMS Math. Surveys and Monographs 213 (2016).
- [T. Hilberdink, M. Lapidus, *Beurling zeta functions, generalised primes, and fractal membranes* (arXiv:math/0410270)](https://arxiv.org/abs/math/0410270)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `analytic` |
> | Implikation | `none` |
> | Euler-Produkt | `essential` |
> | Positivität | `n/a` |
> | Strenge | `theorem` |
> | Evidenz | `n/a` |
> | Testbar | `medium` |
> | Formalisierbar | `medium` |
> 
> **Offener Kernschritt:** Keiner - Negativresultat: Euler-Produkt + Dichte reichen nicht.
> 
> **Hebel:** Zweite Säule der Einkreisung neben Davenport-Heilbronn.
> 
> **Fehlermodi:** [[F1_no-euler-product|F1 Euler-Blindheit]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-68`

> [!abstract]- Graph-Nachbarn (5)
> - *verallgemeinert* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Zweite Säule neben Davenport–Heilbronn: auch Multiplikativität allein genügt nicht.
> - *ist Instanz von* → **Euler-Produkt (Multiplikativität)** — Beurling-Systeme haben ein Euler-Produkt per Konstruktion.
> - *ist Obstruktion für* → **Riemann-Vermutung (RH)** — Euler-Produkt + gute Dichte reichen nicht: DMV-System verletzt das RH-Analogon.
> - *ist Obstruktion für* → [[12_zero_free_regions|12 · Nullstellenfreie Regionen]] — Zeigt: die klassische nullstellenfreie Region ist im Beurling-Rahmen optimal.
> - *schwächer als* → [[73_Tate_thesis_adelic_analysis|73 · Tates These & adelische Analysis]] — Beurling-Systemen fehlt die additive Struktur (Poisson-Summation).

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
