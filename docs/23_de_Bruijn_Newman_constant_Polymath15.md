---
id: doc-23
number: 23
title: "De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15"
category: breakthrough
status: open
tags: [de-bruijn-newman, rodgers-tao, polymath15, lehmer-pairs]
source_file: 23_de_Bruijn_Newman_constant_Polymath15.md
lang: de
---

# De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15

**Kategorie:** Aktueller Fortschritt (RH "auf der Kippe")
**Autoren / Jahre:** de Bruijn (1950), Newman (1976), Brad Rodgers & Terence Tao (2018), Polymath15 (2018–2019)
**Typ:** Quantitatives "Wie knapp gilt die RH?"-Resultat
**Status:** ✅ Λ ≥ 0 bewiesen (Rodgers–Tao); Λ ≤ 0,22 (Polymath15); RH ⟺ Λ ≤ 0

## Zusammenfassung
Die **De-Bruijn–Newman-Konstante Λ** quantifiziert, "wie knapp" die RH gilt. Es ist bekannt, dass die **RH äquivalent zu Λ ≤ 0** ist. Rodgers und Tao bewiesen 2018 die umgekehrte Schranke **Λ ≥ 0**. Zusammen heißt das: **Wenn die RH wahr ist, ist sie nur ganz knapp wahr** (Λ = 0 exakt). Das anschließende Polymath15-Projekt drückte die obere Schranke auf Λ ≤ 0,22.

## Kernidee
- Man deformiert die Riemann-ξ-Funktion durch einen Wärmeleitungs-/Diffusionsparameter t: Für jeden reellen Parameter t entsteht eine ganze Funktion H_t, deren Nullstellen man verfolgt.
- de Bruijn und Newman zeigten: Es gibt eine Konstante Λ, sodass H_t **genau dann nur reelle Nullstellen** hat (= RH-Analogon), wenn t ≥ Λ.
- Bei t = 0 ist H_0 im Wesentlichen die ξ-Funktion ⇒ **RH ⟺ Λ ≤ 0**.
- Newman vermutete 1976 die komplementäre Ungleichung **Λ ≥ 0** ("die RH, falls wahr, ist nur knapp wahr").

## Die Resultate
- **Rodgers–Tao (2018, "The de Bruijn–Newman constant is non-negative"):** Beweis von **Λ ≥ 0** (Newmans Vermutung). Veröffentlicht in *Forum of Mathematics, Pi* (2020). Idee: Wäre Λ < 0, hätten die Nullstellen eine "zu geordnete" Dynamik, die der bekannten GUE-artigen Statistik (Dok. 06) widerspricht.
- **Polymath15 (2018–2019, von Tao initiiertes offenes Online-Kollaborationsprojekt):** Verbesserte die **obere** Schranke (klassisch de Bruijn: Λ ≤ 1/2) auf **Λ ≤ 0,22**, durch Kombination analytischer Abschätzungen mit umfangreicher Computerrechnung.

## Bedeutung / Einordnung
- Liefert eine **quantitative Sicht** auf die RH: Sie ist (falls wahr) "auf Messers Schneide" wahr — Λ = 0 genau.
- Λ ≥ 0 gibt der RH eine konzeptionelle Erklärung: Die Nullstellen sind genau so weit "verschmiert", wie es noch mit Realität verträglich ist.
- Vorbild für **Polymath-Kollaboration** (massiv parallele, offene Mathematik) und Mensch-Computer-Zusammenarbeit.
- **Kein** Beweis der RH (das wäre Λ ≤ 0); die Lücke 0 ≤ Λ ≤ 0,22 müsste auf Λ ≤ 0 geschlossen werden.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Die deformierte Familie H_t
Schreibe die ξ-Funktion als Fourier-Transformierte einer positiven geraden Funktion:
```
ξ(1/2 + iz) = (1/2) ∫_{−∞}^∞ Φ(u) e^{izu} du,   Φ(u) = Σ_{n=1}^∞ (2π²n⁴ e^{9u} − 3πn² e^{5u}) exp(−πn² e^{4u}) > 0.
```
Deformiere mit einem Wärmeleitungsparameter t:
```
H_t(z) = ∫_{−∞}^∞ e^{t u²} Φ(u) e^{izu} du.
```
H_0 ist (bis auf Normierung) ξ. H_t erfüllt die Rückwärts-Wärmeleitungsgleichung ∂_t H = −∂_{zz} H; die Nullstellen z_k(t) bewegen sich gemäß einem Gradientenfluss.

### Definition der Konstante Λ
**Satz (de Bruijn 1950 / Newman 1976).** Es gibt Λ ∈ ℝ mit:
```
H_t hat nur reelle Nullstellen   ⟺   t ≥ Λ.
```
Da H_0 = ξ, folgt:
```
RH  ⟺  Λ ≤ 0.
```
de Bruijn zeigte Λ ≤ 1/2; Newman vermutete Λ ≥ 0.

### Rodgers–Tao (2018): Λ ≥ 0
**Beweisidee (Widerspruch).** Wäre Λ < 0, so wären die Nullstellen für ein t < 0 schon reell und würden unter dem Fluss zu t = 0 eine *zu reguläre* Verteilung annehmen: Man zeigt, dass dann die Nullstellen asymptotisch in nahezu arithmetischer Progression lägen (Abstände gleichmäßiger als erlaubt). Das widerspricht der bekannten **Paarkorrelations-/Montgomery-Statistik** (Dok. 06), die Niveau-Abstoßung *und* Fluktuationen verlangt. Formal: eine Größe (gemittelte Nullstellendynamik) müsste zugleich → 0 und ≥ c > 0 sein. ⇒ Λ ≥ 0.

### Polymath15 (2019): obere Schranke Λ ≤ 0,22
Strategie: Zeige H_t(x+iy) ≠ 0 für y > 0 und alle x, sobald t ≥ 0,2 und die Höhe groß genug ist; für niedrige Höhen numerische Verifikation, dass keine **Lehmer-Paare** (extrem nahe Nullstellen) die Reellheit gefährden. Werkzeuge:
```
- Newtonsche Ungleichungen / Approximation von H_t durch ein effektiv berechenbares A+B−C-Modell,
- explizite Schranken an den Quotienten H_t'/H_t,
- mollifizierte Barrieren-Argumente + großräumige Computerrechnung.
```
Ergebnis: **0 ≤ Λ ≤ 0,22**.

### Interpretation
Λ = 0 (RH) bedeutet: die ξ-Nullstellen sind „auf der Kippe" reell — jede infinitesimale Rückwärts-Wärmeleitung (t < 0) würde sofort komplexe Nullstellen erzeugen. Lehmer-Paare (z. B. nahe γ ≈ 7005) sind die empirischen Zeugen dieser Knappheit.

## Quellen
- [The De Bruijn-Newman constant is non-negative — Terence Tao (Blog)](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/)
- [The de Bruijn–Newman constant is non-negative — Forum of Mathematics, Pi (Cambridge)](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/de-bruijnnewman-constant-is-nonnegative/D4B85BA067E2D5A71D87E4FFB0D21E46)
- [De Bruijn-Newman constant — Polymath Wiki](https://michaelnielsen.org/polymath/index.php?title=De_Bruijn-Newman_constant)
- [de Bruijn–Newman constant — Wikipedia](https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_analytic|Analytische Ansätze]]

| Achse | Wert |
|---|---|
| Familie | analytic |
| Implikation | `conditional` |
| Euler-Produkt | `essential` |
| Positivität | `must-prove` |
| Strenge | `theorem` · Evidenz `strong` |
| Testbar / formalisierbar | `high` / `medium` |

**Offener Kernschritt:** Lambda <= 0 zeigen (Lambda >= 0 ist bewiesen); Lambda = 0 wäre äquivalent zur RH.

**Hebel (was er liefern würde):** Ein einziger reeller Parameter kodiert die RH - ideal für Numerik.

**Typische Fehlermodi:** [[F9_truncation-limit-gap|F9 Abgeschnittenes Modell bewiesen, Limes offen]]

**Vergleichbar mit:** [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)]] · [[12_zero_free_regions|Nullstellenfreie Regionen (klassischer analytischer Ansatz)]] · [[56_Turan_power_sums_partial_sums|Turáns Potenzsummen-Programm & die Partialsummen von ζ (widerlegter Ansatz)]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-23 doc-52 doc-12 doc-56`

**Ausgehende Beziehungen**
- *ist äquivalent zu* (`equivalent_to`) → [[concept_RH|Riemann-Vermutung (RH)]] — de-Bruijn–Newman: Λ≤0 ⟺ RH.
- *ist Instanz von* (`instance_of`) → [[concept_positivity|Positivität / Reellwurzeligkeit]] — de-Bruijn–Newman Λ≤0.

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[33_statistical_mechanics_Lee_Yang|33 — Statistische Mechanik & Lee–Yang-Analogie (Newman)]] — Statistische Mechanik liefert Werkzeuge für die dBN-Konstante.
- *benutzt* (`uses`) → [[29_Jensen_Polya_Laguerre_Polya_GORZ|29 — Jensen–Pólya-Programm: Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)]] — Laguerre-Pólya ⟺ Λ≤0; gemeinsame Pólya-Wurzel.
- *benutzt* (`uses`) → [[55_Speiser_zeros_of_zeta_prime|55 — Speisers Satz & die Nullstellen von ζ′ (die Maschine hinter Levinson)]] — Lehmer-Paare erzwingen ζ′-Nullstellen sehr nahe an der Geraden.
- *ist Evidenz für* (`evidence_for`) → [[64_extreme_values_FHK_multiplicative_chaos|64 — Extremwerte von ζ: Fyodorov–Hiary–Keating & multiplikatives Chaos]] — Extremwerte und Lehmer-Paare messen beide, wie 'knapp' die RH gilt.
- *benutzt* (`uses`) → [[67_what_if_RH_is_false|67 — Was wäre, wenn die RH falsch ist? Θ, Oszillationen & numerische Signaturen]] — Λ>0 wäre äquivalent zu 'RH falsch'.

**Thematisch benachbart (gemeinsame Tags):** [[67_what_if_RH_is_false|Was wäre, wenn die RH falsch ist? Θ, Oszillationen & numerische Signaturen]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
