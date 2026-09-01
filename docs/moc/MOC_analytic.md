---
id: moc-analytic
title: "MOC — Analytische Ansätze"
type: moc
tags: [moc, netzwerk]
lang: de
---

# MOC — Analytische Ansätze

*11 Ansätze. Automatisch erzeugt aus `kb/graph/approaches.json`.*

| Ansatz | Status | Implikation | offener Kernschritt |
|---|---|---|---|
| [[03_Hardy_1914_infinitely_many_zeros|Hardy (1914): Unendlich viele Nullstellen auf der kritischen Geraden]] | `proven` | `partial` | Von 'unendlich viele' zu 'alle' - der Sprung ist qualitativ, nicht quantitativ. |
| [[04_Levinson_Conrey_positive_proportion|Levinson, Conrey & Co.: Positiver Anteil der Nullstellen auf der kritischen Geraden]] | `proven` | `partial` | Mollifier-Länge θ < 4/7; Anteil 1 braucht Momente, die ohne RH unbekannt sind. |
| [[12_zero_free_regions|Nullstellenfreie Regionen (klassischer analytischer Ansatz)]] | `proven` | `partial` | Vinogradov-Korobov-Region ist seit 1958 nicht substanziell verbessert; jede Verbesserung Richtung fester Streifen wäre ein Durchbruch. |
| [[17_Lindelof_density_hypothesis|Lindelöf-Hypothese & Dichte-Hypothese]] | `open` | `partial` | Lindelöf folgt aus RH, impliziert sie aber nicht; selbst Lindelöf ist offen. |
| [[22_Guth_Maynard_2024|Guth–Maynard (2024): Durchbruch bei Nullstellendichte-Abschätzungen]] | `proven` | `partial` | Verbesserte Exponenten bleiben weit von der Dichtehypothese entfernt. |
| [[23_de_Bruijn_Newman_constant_Polymath15|De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15]] | `proven` | `conditional` | Lambda <= 0 zeigen (Lambda >= 0 ist bewiesen); Lambda = 0 wäre äquivalent zur RH. |
| [[29_Jensen_Polya_Laguerre_Polya_GORZ|Jensen–Pólya-Programm: Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)]] | `open` | `equivalent` | Hyperbolizität der Jensen-Polynome für ALLE Grade d bei festem n (bewiesen: jedes feste d für große n). |
| [[32_Landau_Siegel_zeros_Zhang|Landau–Siegel-Nullstellen (Ausnahme-Nullstellen) & Yitang Zhang (2022)]] | `open` | `partial` | Ausschluss reeller Ausnahmennullstellen; Siegels Satz bleibt ineffektiv. |
| [[46_Voronin_universality|Voronin-Universalität (Meta-Obstruktion gegen „weiche' Beweise)]] | `proven` | `none` | Keiner - der Satz ist eine Obstruktion, kein Ansatz. |
| [[56_Turan_power_sums_partial_sums|Turáns Potenzsummen-Programm & die Partialsummen von ζ (widerlegter Ansatz)]] | `refuted` | `conditional` | Prämisse widerlegt: Montgomery 1983 zeigt Nullstellen von zeta_N rechts von Re=1. |
| [[57_Beurling_generalized_primes|Beurlingsche verallgemeinerte Primzahlen: Euler-Produkt allein genügt nicht]] | `proven` | `none` | Keiner - Negativresultat: Euler-Produkt + Dichte reichen nicht. |

## Typische Fehlermodi dieser Familie

- [[F13_error-term-ceiling|F13 Strukturelle Decke des Fehlerterms]] — 6×
- [[F12_ineffective-nonuniform|F12 Ineffektive oder nicht gleichmäßige Konstanten]] — 2×
- [[F9_truncation-limit-gap|F9 Abgeschnittenes Modell bewiesen, Limes offen]] — 2×
- [[F1_no-euler-product|F1 Euler-Produkt nicht wesentlich benutzt]] — 2×
- [[F11_criterion-restates|F11 Äquivalenz ohne neuen Zugriff]] — 1×
- [[F7_soft-function-theory|F7 Weiche Funktionentheorie (zu allgemein)]] — 1×

**Navigation:** [[MOC_00_Hub|Netzwerk-Hub]] · [[69_comparison_matrix|Vergleichsmatrix]] · [[00_INDEX|Index]]
