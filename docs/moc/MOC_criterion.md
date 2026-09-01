---
id: moc-criterion
title: "MOC — Äquivalente Kriterien"
type: moc
tags: [moc, netzwerk]
lang: de
---

# MOC — Äquivalente Kriterien

*7 Ansätze. Automatisch erzeugt aus `kb/graph/approaches.json`.*

| Ansatz | Status | Implikation | offener Kernschritt |
|---|---|---|---|
| [[13_Nyman_Beurling_Baez_Duarte|Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]] | `open` | `equivalent` | Approximationsgrad d_N -> 0 beweisen; bekannte untere Schranken sind vom richtigen Typ, obere fehlen. |
| [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]] | `open` | `equivalent` | λ_n >= 0 für alle n zeigen, ohne die Nullstellenlage zu benutzen. |
| [[15_Robin_inequality|Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)]] | `open` | `equivalent` | Kein Zugang zu σ(n) jenseits von Extremalzahlen; Kriterium ist so hart wie RH. |
| [[16_Mertens_function_Riesz_criterion|Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]] | `open` | `equivalent` | M(x) << x^(1/2+eps) - blockiert durch die Paritätsbarriere; Mertens-Vermutung ist widerlegt. |
| [[20_de_Branges_Hilbert_spaces|Louis de Branges: Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)]] | `refuted` | `conditional` | Die benutzte Positivitätsbedingung ist für ζ nachweislich verletzt (Conrey-Li-Gegenbeispiel). |
| [[55_Speiser_zeros_of_zeta_prime|Speisers Satz & die Nullstellen von ζ′ (die Maschine hinter Levinson)]] | `open` | `equivalent` | Ueber ζ′ links der Geraden weiß man nichts, was man nicht über ζ wüsste. |
| [[66_Bagchi_strong_recurrence|Bagchis Satz: RH als starke Rekurrenz (Universalität als Kriterium)]] | `open` | `equivalent` | Selbstbezüglich: Voronin verlangt Nullstellenfreiheit auf K - also genau die RH. |

## Typische Fehlermodi dieser Familie

- [[F11_criterion-restates|F11 Äquivalenz ohne neuen Zugriff]] — 6×
- [[F2_positivity-assumed|F2 Positivität angenommen statt bewiesen]] — 2×
- [[F6_numerics-as-proof|F6 Endliche Numerik als Beweis behandelt]] — 2×
- [[F8_parity-barrier|F8 Paritätsbarriere (Sieb-/Multiplikativitätsmethoden)]] — 1×
- [[F1_no-euler-product|F1 Euler-Produkt nicht wesentlich benutzt]] — 1×
- [[F15_verification-collapse|F15 Zusammenbruch in der Verifikation]] — 1×
- [[F13_error-term-ceiling|F13 Strukturelle Decke des Fehlerterms]] — 1×
- [[F7_soft-function-theory|F7 Weiche Funktionentheorie (zu allgemein)]] — 1×

**Navigation:** [[MOC_00_Hub|Netzwerk-Hub]] · [[69_comparison_matrix|Vergleichsmatrix]] · [[00_INDEX|Index]]
