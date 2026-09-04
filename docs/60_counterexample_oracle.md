---
id: doc-60
number: 60
title: "Das Gegenbeispiel-Orakel: Kriterien gegen eine RH-verletzende Funktion testen"
category: verification
status: reference
tags: [davenport-heilbronn, counterexample, oracle, turing-method, numerical, calibration]
source_file: 60_counterexample_oracle.md
lang: de
---

# Das Gegenbeispiel-Orakel: Kriterien gegen eine RH-verletzende Funktion testen

**Kategorie:** Verifikation / Werkzeug
**Implementierung:** `kb/counterexample.py` · Protokolle: `kb/research/results/oracle_*.json`
**Verwandt:** `docs/35` (Obstruktion) · `docs/43` (Epstein/Rigidität) · `docs/57` (abgeleitete Richtungen) · `docs/59` (Invarianten)

## Die Umkehrung der üblichen Frage

Jedes numerische Experiment dieser Wissensbasis lief bisher auf ζ — einer
Funktion, bei der die RH vermutlich gilt. Solche Rechnungen bestätigen, was
man ohnehin glaubt, und sagen **nichts über ihre eigene Trennschärfe**.

Das Orakel stellt die Frage um:

> **Würde mein Kriterium eine Funktion, für die die RH nachweislich FALSCH
> ist, als RH-konform durchwinken?**

Ein Test, der nie an einem Positivfall kalibriert wurde, hat unbekannte
Sensitivität. Ein Test, der ζ und die Davenport–Heilbronn-Funktion **nicht
trennt**, kann prinzipiell kein Bestandteil eines RH-Beweises sein.

## Der Testfall

Die Davenport–Heilbronn-Funktion, in der Hurwitz-Form:

```
τ    = (√(10 − 2√5) − 2)/(√5 − 1)                          = 0,2840790438…
f(s) = 5^{−s} [ ζ(s,1/5) + τ·ζ(s,2/5) − τ·ζ(s,3/5) − ζ(s,4/5) ]
```

Äquivalent: die Dirichlet-Reihe mit mod-5-periodischen Koeffizienten
a(n) = [0, 1, τ, −τ, −1] an der Stelle n mod 5. Vervollständigt mit dem
Gamma-Faktor eines ungeraden Charakters mod 5:

```
ξ_f(s) = (5/π)^{(s+1)/2} · Γ((s+1)/2) · f(s),        ξ_f(s) = ξ_f(1 − s)
```

Sie besitzt: Funktionalgleichung, analytische Fortsetzung, reelle
Dirichlet-Koeffizienten, ζ-artiges Wachstum. Sie besitzt **nicht**: ein
Euler-Produkt. Und sie verletzt die RH.

## Die Testbatterie und was sie misst

**Nur trennende Tests sind informativ.** Ergebnisse aus
`kb/research/results/oracle_report_T120.json`, reproduzierbar mit
`python3 kb/counterexample.py all -T 120`:

| Test | ζ | Davenport–Heilbronn | trennend? |
|---|---|---|:-:|
| **T1** Funktionalgleichung ξ(s) = ξ(1−s) | bestanden (Abw. < 2·10⁻²¹) | bestanden (Abw. < 4·10⁻²¹) | **nein** |
| **T2** Multiplikativität a(mn) = a(m)a(n) | bestanden | **durchgefallen** | **ja** |
| **T3** Nullstellen abseits der Geraden | keine gefunden | **4 gefunden** | **ja** |
| **T4** Vorzeichenwechsel-Defizit (Turing) | Defizit **0** | Defizit **4** | **ja** |
| **T5** Nullstellen mit Re(s) > 1 | keine im Raster | keine im Raster | **nein** |
| **T6** Nachweisgrenze des Li-Kriteriums | — | n ≈ 3,4 · 10⁵ nötig | Sensitivität |

### T1 — die Funktionalgleichung trennt nicht (und das ist der Punkt)

Beide Funktionen erfüllen ξ(s) = ξ(1−s) auf über 20 Dezimalstellen. Die
Funktionalgleichung ist **kein RH-Indikator**. Genau deshalb ist jeder Beweis,
der nur Funktionalgleichung, Fortsetzung und Wachstum benutzt, widerlegt,
bevor man ihn liest (`docs/35`, `docs/56` A6).

Dieser Test ist der pädagogisch wichtigste der Batterie, obwohl — nein: *weil*
— er nichts trennt.

### T2 — Multiplikativität trennt

```
a(6) = a(1) = 1     aber     a(2)·a(3) = τ·(−τ) = −0,0807…
```

Eine einzige Zeile Arithmetik. Das ist die **gesamte** strukturelle Differenz
zwischen ζ und einer Funktion, für die die RH falsch ist. Jeder Beweisschritt,
der diese Differenz nicht benutzt, ist wirkungslos.

### T3 — vier Nullstellen abseits der Geraden

Verifiziert auf 15 Stellen, Residuum |f(ρ)| < 10⁻²⁹
(`kb/research/results/oracle_offline_zeros.json`):

| Nullstelle | Abstand zur kritischen Geraden |
|---|---|
| 0,808517182456637 + 85,6993484853776 i | 0,3085 |
| 0,650830080609737 + 114,163342730757 i | 0,1508 |
| 0,724257694626810 + 176,702461242856 i | 0,2243 |
| 0,574356050450806 + 166,479305913168 i | 0,0744 |

Die ersten drei sind mit den Literaturwerten (Balanzario–Sánchez-Ortiz 2007)
verträglich; die vierte wurde über das Defizit aus T4 gezielt gesucht und
gefunden (siehe unten). **Die Verletzung ist nicht knapp:** Re bis 0,81 statt
0,5.

### T4 — der einzige Test, der die Verletzung selbst findet

Alle anderen Tests bekommen gesagt, wo sie suchen sollen. T4 nicht.

Für **beide** Funktionen ist Z(t) := ξ(1/2 + it) reellwertig (reelle
Koeffizienten + Funktionalgleichung). Jede Nullstelle **auf** der Geraden
erzeugt generisch einen Vorzeichenwechsel von Z. Das Argumentprinzip zählt
dagegen **alle** Nullstellen im Streifen:

```
N(T) = (1/π) · Δ arg ξ  entlang  2 → 2+iT → 1/2+iT        (+1 bei Pol)

Defizit := N(T) − #{Vorzeichenwechsel von Z auf (0, T]}
```

Ein positives Defizit ist ein **Existenznachweis** für Nullstellen abseits der
Geraden — ohne sie zu lokalisieren. Das ist Turings Idee, und sie ist
zugleich das Verfahren, das numerische RH-Verifikation überhaupt erst zu einem
Beweis für endliche Höhen macht (`docs/24`).

Gemessen:

| | T = 120 | T = 200 |
|---|---|---|
| ζ: N(T) / Vorzeichenwechsel / **Defizit** | 38 / 38 / **0** | 79 / 79 / **0** |
| DH: N(T) / Vorzeichenwechsel / **Defizit** | 68 / 64 / **4** | 130 / 122 / **8** |

**Die Selbstkonsistenz-Probe.** Nullstellen abseits der Geraden treten bei
reellen Koeffizienten in Paaren ρ, 1−ρ̄ auf — beide in der oberen Halbebene.
Ein Defizit von 4 bedeutet also **zwei** Paare unterhalb T = 120: bei
t ≈ 85,70 und t ≈ 114,16. Genau die zwei aus T3. Bei T = 200 steigt das
Defizit auf 8, also vier Paare. Drei waren bekannt (85,70 · 114,16 · 166,48);
das vierte wurde **auf Grund des Defizits** gesucht und bei t ≈ 176,70
gefunden. Zähler und Sucher bestätigen einander unabhängig.

**Vorbehalt, ausdrücklich.** Die Vorzeichenwechsel werden mit Schrittweite
h = 0,1 abgetastet. Ein sehr enges Nullstellenpaar (Lehmer-Paar, `docs/23`)
kann zwei Vorzeichenwechsel verschlucken und ein Defizit **vortäuschen**. Das
korrekte Vorgehen ist, h zu halbieren und nachzuprüfen — bei einem echten
Defizit ändert sich nichts. Für ζ, wo Lehmer-Paare tatsächlich vorkommen, ist
das der praktisch relevante Fall.

### T5 — ein negatives Ergebnis, das nichts beweist

Im gerasterten Bereich 1 < Re(s) ≤ 1,2, 0 < Im(s) ≤ 120 findet der Test bei
**beiden** Funktionen nichts. Für ζ ist das ein **Satz**: das Euler-Produkt
konvergiert dort und kein Faktor verschwindet. Für DH ist es nur eine
Reichweitengrenze des Rasters — die Theorie garantiert unendlich viele
Nullstellen mit Re(s) > 1, sie liegen aber weit oberhalb des abgesuchten
Bereichs.

**Identisches Messergebnis, völlig verschiedener Status.** Das ist
`blk-finite-evidence` in Reinform (`docs/35`, `docs/55`) — und der Grund,
warum T5 in der Batterie bleibt, obwohl er nichts trennt.

### T6 — wie stumpf ein äquivalentes Kriterium sein kann

Der Beitrag einer Nullstelle ρ = β + iγ zum Li-Koeffizienten λ_n enthält
−(1 − 1/ρ)ⁿ mit

```
|1 − 1/ρ| = 1 + (1 − 2β)/(2γ²) + O(γ⁻⁴)      >  1   ⟺   β < 1/2
```

Eine Nullstelle links der Geraden treibt λ_n also exponentiell nach −∞ — mit
einer Rate, die **quadratisch mit der Höhe abfällt**. Ergebnis
(`python3 kb/counterexample.py lisens --func dh`): um die DH-Verletzung bei
Höhe 85,7 zu sehen, bräuchte man λ_n bis **n ≈ 3,4 · 10⁵**. Umgekehrt schließt
ein Budget von n ≤ 1000 Nullstellen abseits nur bis γ ≈ 3,6 aus — **nicht
einmal bis zur ersten ζ-Nullstelle bei 14,13**.

Vollständige Tabellen und Einordnung: `docs/57`, Eintrag U1.

## Was das Orakel leistet — und was nicht

**Es leistet:**
- Eine harte, maschinelle Prüfung gegen `blk-euler-blindness` — den einzigen
  Blocker mit explizitem Gegenbeispiel (`docs/55`, Beob. 7).
- Kalibrierung: es misst die Trennschärfe eines Kriteriums, statt es zu
  bestätigen.
- Einen selbstständigen Verletzungsdetektor (T4), der Nullstellen abseits der
  Geraden findet, ohne dass man ihm sagt, wo.

**Es leistet nicht:**
- Es prüft keine Beweistexte, sondern Kriterien und Verfahren. Ein Argument in
  Prosa muss ein Mensch (oder ein Modell, das es gelesen hat) auf die Frage
  „gilt das auch für DH?" abbilden.
- Es sagt nichts über die anderen elf Blocker. Zirkuläre Positivität, fehlende
  Geometrie und nicht-kanonische Operatoren erfordern Urteil, nicht Rechnung.
- Es beweist nichts über ζ. Ein bestandener DH-Test ist eine **notwendige**,
  keine hinreichende Bedingung.

## Reproduktion

```bash
pip install -r kb/requirements.txt

python3 kb/counterexample.py all -T 120      # ganze Batterie (~2 min)
python3 kb/counterexample.py fe              # Funktionalgleichung (schnell)
python3 kb/counterexample.py euler           # Multiplikativität (sofort)
python3 kb/counterexample.py offline         # Nullstellen abseits (schnell)
python3 kb/counterexample.py deficit -T 200  # Turing-Defizit (~4 min)
python3 kb/counterexample.py lisens --func dh
```

MCP-Tool: `counterexample_oracle(test="euler")`. Gespeicherte Protokolle in
`kb/research/results/`:
`oracle_report_T120.json`, `oracle_offline_zeros.json`, `oracle_li_sensitivity.json`.

## Offene Erweiterungen

1. **Epstein-Zeta als zweiter Testvektor** (`docs/43`, `docs/59`). Wichtig,
   weil gegen DH der Einwand „künstliche Linearkombination" erhoben wird — die
   Epstein-Zeta einer quadratischen Form mit Klassenzahl > 1 ist ein
   natürliches arithmetisches Objekt und verletzt die RH trotzdem. Die
   Implementierung erfordert die Chowla–Selberg-Entwicklung
   (Bessel-K-Funktionen); noch nicht umgesetzt.
2. **d_N, Robin, Λ als Negativkontrollen** (`docs/57` U1). Für d_N ist wegen
   der 1/log N-Konvergenz eine noch schlechtere Sensitivität zu erwarten als
   beim Li-Kriterium.
3. **Die abgeschnittene Weil-Form gegen DH** (`docs/57` U2) — der
   folgenreichste offene Punkt: hält die Positivität bei jedem erreichbaren
   Cutoff auch für DH, liegt die gesamte arithmetische Last im Grenzübergang.

## Quellen
- [Zeros of the Davenport–Heilbronn Counterexample — Balanzario & Sánchez-Ortiz, Math. Comp. 76 (2007)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)
- [On Davenport and Heilbronn-Type of Functions (arXiv 1602.06328)](https://arxiv.org/abs/1602.06328)
- [On some reasons for doubting the Riemann hypothesis — A. Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- Turings Methode zur Nullstellenzählung: dargestellt in `docs/24`; Numerik in diesem Dokument selbst gerechnet (mpmath, 20 Stellen).

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (4)
> - *ist Evidenz für* → [[59_invariants_test_vectors|59 · Invarianten & Testvektoren]] — Liefert die maschinelle Haelfte der Invariantenpruefung.
> - *ist Instanz von* → **Euler-Produkt (Multiplikativität)** — Operationalisiert das Euler-Produkt als maschinellen Test.
> - *benutzt* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Macht die Davenport-Heilbronn-Obstruktion maschinell pruefbar.
> - *benutzt* → [[24_computational_verification|24 · Numerische Verifikation der Riemann-Vermutung]] — Benutzt Turings Nullstellenzaehlung als Verletzungsdetektor.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
