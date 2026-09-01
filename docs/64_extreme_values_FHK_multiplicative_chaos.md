---
id: doc-64
number: 64
title: "Extremwerte von ζ: Fyodorov–Hiary–Keating & multiplikatives Chaos"
category: frontier
status: open
tags: [extreme-values, fyodorov-hiary-keating, multiplicative-chaos, branching-random-walk, lindelof, resonance-method, bondarenko-seip]
source_file: 64_extreme_values_FHK_multiplicative_chaos.md
lang: de
---

# Extremwerte von ζ — FHK-Vermutung, multiplikatives Chaos, Ω-Resultate

**Kategorie:** Aktive Front (Wahrscheinlichkeitstheorie ∩ analytische Zahlentheorie)
**Autoren / Jahre:** Fyodorov–Hiary–Keating (2012); Arguin–Belius–Bourgade–Radziwiłł–Soundararajan (2019); Arguin–Bourgade–Radziwiłł (2020er); Najnudel (2018); Saksman–Webb; Bondarenko–Seip (2017)
**Typ:** Präzise Vorhersagen für `max |ζ|` — kurzes Fenster (FHK) und globales Maximum (Ω-Resultate)
**Status:** Führende Ordnung bewiesen; volle FHK-Vermutung offen

## Zusammenfassung
Wie groß wird `|ζ(1/2+it)|`? Diese Frage verbindet die Lindelöf-Hypothese (Dok. 17), die Momentenvermutungen (Dok. 07, 63) und moderne Wahrscheinlichkeitstheorie (verzweigende Irrfahrten, multiplikatives Chaos). Fyodorov, Hiary und Keating sagten 2012 aus einer Analogie zu logarithmisch korrelierten Zufallsfeldern eine **erstaunlich präzise Formel** für das Maximum in einem kurzen Intervall voraus — inklusive des Terms dritter Ordnung. Große Teile davon sind inzwischen bewiesen. Für die RH ist das ein **Kalibrierungswerkzeug**: es sagt, wie groß ζ „darf", ohne dass die RH verletzt wird.

## Mathematischer Kern

### Die FHK-Vermutung (kurzes Fenster)
Für t gleichverteilt in [T, 2T]:
```
max_{|h| ≤ 1} log|ζ(1/2 + i(t+h))|
   =  log log T  −  (3/4)·log log log T  +  𝔐_T,
```
wobei `𝔐_T` gegen eine nicht-degenerierte Zufallsvariable konvergiert (Verteilung vom Typ der Ableitungs-Martingal-Randverteilung einer verzweigenden Irrfahrt).

**Herkunft der Analogie.** Über die Dirichlet-Reihe von `log ζ` ist
```
log|ζ(1/2+it)| ≈ Σ_{p ≤ T} cos(t log p)/√p,
```
und die Teilsummen über dyadische Bereiche `p ∈ [e^{e^k}, e^{e^{k+1}}]` verhalten sich wie die Generationen eines **verzweigenden Zufallsspaziergangs (BRW)**: Korrelation `≈ log(1/|h|)`, also **logarithmisch korreliertes Feld**. Für solche Felder ist das Maximum universell bekannt (Bramson, Aïdékon, Ding–Roy–Zeitouni): `Maximum = m_n − (3/2)·(1/2)·log n + O(1)` — daraus die `3/4`.

### Bewiesener Stand
- **Führende Ordnung (ABBRS 2019, unbedingt):** `max_{|h|≤1} log|ζ(1/2+i(t+h))| / log log T → 1` in Wahrscheinlichkeit.
- **Der `−(3/4) log log log T`-Term und Straffheit (Arguin–Bourgade–Radziwiłł):** bewiesen.
- **Najnudel (2018):** führende Ordnung unter RH, mit anderem Zugang.
- **Multiplikatives Chaos (Saksman–Webb):** `ζ(1/2 + it)` konvergiert nach geeigneter Normierung im Verteilungssinn gegen ein Gaußsches multiplikatives Chaos — eine tiefere Erklärung, warum das BRW-Bild stimmt.

### Globales Maximum: Ω-Resultate (untere Schranken)
Was ist mit dem Maximum über ein langes Intervall? Hier liefert die **Resonanzmethode**:
```
max_{t ∈ [0,T]} |ζ(1/2+it)|  ≥  exp( (1 + o(1)) · √( log T · log log log T / log log T ) )     (Bondarenko–Seip 2017),
```
verschärft von Soundararajan/de la Bretèche–Tenenbaum (Konstante `√2 + o(1)` im Exponenten). Unter RH gilt umgekehrt die obere Schranke
```
|ζ(1/2+it)|  ≪  exp( C · log t / log log t )      (Littlewood).
```
Die Lücke zwischen `exp(√(log T ···))` und `exp(log T/log log T)` ist riesig — die **Lindelöf-Hypothese** (Dok. 17) behauptet `|ζ(1/2+it)| ≪ t^ε` und folgt aus der RH, ist aber schwächer.

### Was das für die RH bedeutet
1. **Kein Implikationspfeil.** Auch dieses Gebiet **modelliert** (Fehlermodus `F14`); es beweist keine Nullstellenlage. Aber: die FHK-Statistik ist mit der RH *konsistent* und liefert einen scharfen Konsistenztest.
2. **Falsifizierbarkeit.** Würde man numerisch Maxima finden, die deutlich über der FHK-Vorhersage liegen, wäre das ein Hinweis auf zusätzliche Struktur — und mögliche Nullstellen abseits der Geraden (Dok. 67).
3. **Verbindung zu Lehmer-Paaren.** Sehr kleine Werte von `|ζ|`/enge Nullstellenpaare (Dok. 23) sind das Spiegelbild der Extremwerte; beide messen, wie „knapp" die RH gilt.
4. **Technik-Transfer.** Die Momenten-Obergrenzen von Harper und Soundararajan (unter RH) sind Bausteine für die Splitting-Vermutung (Dok. 63) und für Dichteabschätzungen (Dok. 49).

## Bedeutung / Einordnung
- Das ist derzeit eines der **aktivsten** Gebiete rund um ζ und im Netzwerk der natürliche Nachbar von 06, 07, 17, 63.
- **Für Numerik-Projekte hervorragend geeignet:** Maxima von `|ζ(1/2+it)|` in Fenstern der Länge 1 bei wachsendem T sind mit mpmath direkt messbar und gegen die FHK-Formel testbar — ein realistisches, publizierbares Experiment (Dok. 51).

## Quellen
- [Y. Fyodorov, G. Hiary, J. Keating, *Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta function*, PRL 108 (2012) (arXiv:1202.4713)](https://arxiv.org/abs/1202.4713)
- [Arguin–Belius–Bourgade–Radziwiłł–Soundararajan, *Maximum of the Riemann zeta function on a short interval of the critical line* (arXiv:1612.08575)](https://arxiv.org/abs/1612.08575)
- [L.-P. Arguin, P. Bourgade, M. Radziwiłł, *The Fyodorov–Hiary–Keating conjecture* (arXiv:2007.00988)](https://arxiv.org/abs/2007.00988)
- [A. Bondarenko, K. Seip, *Large greatest common divisor sums and extreme values of the Riemann zeta function* (arXiv:1507.05840)](https://arxiv.org/abs/1507.05840)
- [E. Saksman, C. Webb, *The Riemann zeta function and Gaussian multiplicative chaos* (arXiv:1609.00027)](https://arxiv.org/abs/1609.00027)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_probabilistic|Probabilistische Modelle & Statistik]]

| Achse | Wert |
|---|---|
| Familie | probabilistic |
| Implikation | `model` |
| Euler-Produkt | `essential` |
| Positivität | `n/a` |
| Strenge | `theorem` · Evidenz `strong` |
| Testbar / formalisierbar | `high` / `low` |

**Offener Kernschritt:** Volle FHK-Vermutung; Lücke zwischen Omega-Resultaten und Lindelöf.

**Hebel (was er liefern würde):** Scharfer, numerisch prüfbarer Konsistenztest für die RH.

**Typische Fehlermodi:** [[F14_model-without-implication|F14 Modell ohne Implikationspfeil]]

**Vergleichbar mit:** [[63_hybrid_Euler_Hadamard_product|Hybrides Euler–Hadamard-Produkt (Gonek–Hughes–Keating)]] · [[06_Montgomery_pair_correlation_RMT|Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]] · [[07_Keating_Snaith_moments|Keating–Snaith: Momente der Zetafunktion via charakteristische Polynome (CUE)]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-64 doc-63 doc-06 doc-07`

**Ausgehende Beziehungen**
- *ist Evidenz für* (`evidence_for`) → [[17_Lindelof_density_hypothesis|17 — Lindelöf-Hypothese & Dichte-Hypothese]] — Extremwert-Schranken kalibrieren Lindelöf.
- *benutzt* (`uses`) → [[63_hybrid_Euler_Hadamard_product|63 — Hybrides Euler–Hadamard-Produkt (Gonek–Hughes–Keating)]] — Zerlegung in Primzahl- und Nullstellenanteil ist der technische Kern.
- *ist Instanz von* (`instance_of`) → [[concept_moments|Momente & Zufallsmatrix-Modelle]] — Momente und Maxima sind zwei Seiten derselben Statistik.
- *ist Evidenz für* (`evidence_for`) → [[23_de_Bruijn_Newman_constant_Polymath15|23 — De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15]] — Extremwerte und Lehmer-Paare messen beide, wie 'knapp' die RH gilt.

**Thematisch benachbart (gemeinsame Tags):** [[17_Lindelof_density_hypothesis|Lindelöf-Hypothese & Dichte-Hypothese]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
