---
id: doc-58
number: 58
title: "GAP-Registry & Near-Miss-Bewertung: das eine fehlende Lemma je Ansatz"
category: meta
status: meta
tags: [gaps, near-miss, missing-lemma, ranking, methodology]
source_file: 58_gap_registry_near_miss.md
lang: de
---

# GAP-Registry & Near-Miss-Bewertung: das eine fehlende Lemma je Ansatz

**Kategorie:** Meta / Bewertungsrahmen
**Datenquelle:** `kb/graph/gaps.json` · Ranking berechnet von `kb/gaps.py`
**Verwandt:** `docs/55` (Blocker) · `docs/56` (Autopsien) · `docs/59` (Invarianten) · `docs/63` (Experimentwert)

## Zweck und Warnung in einem Satz

Dieses Dokument beantwortet für jeden ernsthaften Ansatz die Frage **„was genau
fehlt?"** — und zeigt dabei, dass die naheliegende Anschlussfrage **„wer ist am
nächsten dran?"** in einer Form gestellt werden muss, die fast alle intuitiven
Antworten umkehrt.

## Warum „Near-Miss" bei der RH eine Falle ist

Logisch gibt es keine Nähe. Solange kein Beweis existiert, ist der Abstand zur
RH bei jedem offenen Ansatz **derselbe**: unendlich. Insbesondere:

> **Ein äquivalentes Kriterium kann definitionsgemäß kein Near-Miss sein.**
> „RH ⟺ X" heißt: X ist exakt so schwer wie die RH. Wer Robins Ungleichung
> beweist, hat die RH bewiesen — und wer sie nicht beweist, ist um keinen
> Millimeter näher als vorher.

Das ist keine Spitzfindigkeit, sondern der häufigste Bewertungsfehler im Feld.
Eine wachsende Liste äquivalenter Kriterien (`docs/13`, `docs/14`, `docs/15`,
`docs/16`, `docs/45`) sieht nach Annäherung aus und ist keine
(`blk-equivalence-trap`, `docs/55`).

**Was dann?** Sinnvoll messbar ist nicht Nähe, sondern:

> Wie viel **unbedingt bewiesene Struktur** bringt ein Ansatz bereits mit —
> und gibt es eine Größe, die sich nachweislich in die richtige Richtung
> bewegt hat?

Genau das misst der Score unten. Er misst **nicht** Erfolgsaussicht. Der
Unterschied ist das eigentliche Ergebnis dieses Dokuments (Auswertung 2).

## Die Achsen

| Achse | Frage | Gewicht |
|---|---|---|
| **A** | Existiert ein *unbedingt bewiesenes* Teilresultat in Richtung des Ziels — nicht bloß eine Äquivalenz? | 3 |
| **B** | Gibt es eine bewegliche Kennzahl mit dokumentiertem Fortschritt? | 2 |
| **C** | Läuft eine Folge bewiesener Aussagen auf das Ziel zu — in der *richtigen* Richtung? | 2 |
| **D** | Ist der fehlende Schritt rechnerisch oder maschinell prüfbar? | 1 |
| **E** | Steht der Ansatz unter einem Tier-1-Blocker? | −2 |

Zusätzlich: kann die Methode das Ziel **prinzipiell** erreichen? Falls nein,
wird der Score auf 3 gedeckelt — ein Ansatz mit strukturell unerreichbarem Ziel
darf nicht oben stehen, egal wie viel er bewiesen hat.

Alle Achsenwerte stehen **mit Begründung** in `kb/graph/gaps.json`. Der Score
wird nie von Hand eingetragen, sondern von `kb/gaps.py` berechnet — wer die
Gewichtung für falsch hält, ändert eine Zeile und bekommt sofort das
alternative Ranking.

## Das Ranking

<!-- GAPS:BEGIN (generiert von kb/gaps.py -- nicht von Hand editieren) -->

**Rechenregel (auditierbar):** `score = 3A + 2B + 2C + D − 2E`, gedeckelt auf 3, falls die Methode das Ziel prinzipiell nicht erreichen kann. Die Achsenwerte stehen mit Begründung in `kb/graph/gaps.json`; berechnet wird der Score von `kb/gaps.py`. **Ein hoher Score bedeutet „viel unbedingt bewiesene Struktur vorhanden“, nicht „aussichtsreich“ — siehe die Auswertung darunter.**

| Rang | Lücke | Dok | Typ | A | B | C | D | E | Score | roh |
|---|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | **Schließen der Lücke 0 ≤ Λ ≤ 0,22** | `23` | quantitativ | 1 | 1 | 0 | 1 | 0 | **6** | 6 |
| 2 | **Hyperbolizität der Jensen-Polynome im gemeinsamen Regime d ~ n** | `29` | grenzuebergang | 1 | 1 | 0 | 1 | 0 | **6** | 6 |
| 3 | **Grenzübergang der abgeschnittenen Weil-Quadratform** | `52` | grenzuebergang | 1 | 0 | 1 | 1 | 0 | **6** | 6 |
| 4 | **Von >41 % auf alle Nullstellen** | `04` | quantitativ | 1 | 1 | 0 | 0 | 0 | **3** ⟨gedeckelt von 5⟩ | 5 |
| 5 | **Unbedingte obere Schranke für d_N** | `13` | aequivalenz | 0 | 1 | 0 | 1 | 0 | **3** | 3 |
| 6 | **Von der Nullstellendichte zur Dichte-Hypothese** | `22` | quantitativ | 1 | 1 | 0 | 0 | 0 | **3** ⟨gedeckelt von 5⟩ | 5 |
| 7 | **Ausschluss von Landau–Siegel-Nullstellen** | `32` | quantitativ | 1 | 1 | 0 | 0 | 1 | **3** | 3 |
| 8 | **Ausschluss der Alternativen Hypothese** | `53` | bedingt auf offene vermutung | 1 | 0 | 0 | 0 | 0 | **3** | 3 |
| 9 | **Invertierbarkeit des Spektraloperators außerhalb Re(s)=1/2** | `44` | aequivalenz | 0 | 0 | 1 | 0 | 0 | **2** | 2 |
| 10 | **Kanonische Konstruktion des Hilbert–Pólya-Operators** | `05` | fehlendes objekt | 0 | 0 | 0 | 0 | 0 | **0** | 0 |
| 11 | **Weil-Positivität unabhängig beweisen** | `14` | aequivalenz | 0 | 0 | 0 | 0 | 0 | **0** | 0 |
| 12 | **Robins Ungleichung für alle n > 5040** | `15` | aequivalenz | 0 | 0 | 0 | 0 | 0 | **0** | 0 |
| 13 | **M(x) = O(x^{1/2+ε})** | `16` | aequivalenz | 0 | 0 | 0 | 0 | 1 | **0** ⟨Untergrenze, roh -2⟩ | -2 |
| 14 | **Geometrie über Spec(ℤ) mit Positivität** | `30` | fehlendes objekt | 0 | 0 | 0 | 0 | 0 | **0** | 0 |

**Verteilung nach Lückentyp:** grenzuebergang: n=2, Ø 6.0 · quantitativ: n=4, Ø 3.8 · bedingt auf offene vermutung: n=1, Ø 3.0 · aequivalenz: n=5, Ø 1.0 · fehlendes objekt: n=2, Ø 0.0

**Kennzahlen:** 14 erfasste Lücken · Höchstwert 6 (Dok. 23, 29, 52) · Score 0 bei Dok. 05, 14, 15, 16, 30.

<!-- GAPS:END -->

## Auswertung

### 1. Die Spitze wird von *Grenzübergangs*-Lücken gebildet, nicht von Äquivalenzen
Der Durchschnitt nach Lückentyp ist eindeutig: Grenzübergang 6,0 —
quantitativ 3,8 — Äquivalenz 1,0 — fehlendes Objekt 0,0. Das ist kein Artefakt
der Gewichtung, sondern spiegelt eine echte Unterscheidung: nur bei
Grenzübergangs- und Kennzahl-Lücken gibt es überhaupt etwas, das sich bewegen
*kann*.

### 2. Der zentrale Befund: Near-Miss und Aussicht sind antikorreliert

Man vergleiche die beiden Enden der Tabelle:

| | Score 6 (Spitze) | Score 0 (Ende) |
|---|---|---|
| **Lücken** | Λ ≤ 0 · Jensen-Polynome bei d ~ n · Grenzübergang der Weil-Truncation | Weil-Positivität · kanonischer Operator · Geometrie über Spec(ℤ) |
| **Charakter** | eine Zahl bzw. eine Gleichmäßigkeitsaussage fehlt | ein **Objekt** fehlt |
| **Falls gelöst** | RH bewiesen — aber ohne Erklärung, *warum* sie gilt | RH bewiesen **und verstanden**; ganze Gebiete entstehen |
| **Messbarer Fortschritt seit 1950** | ja (Λ: 1/2 → 0,22; Grad: 3 → 8) | nein — per Konstruktion nicht möglich |

Die drei Lücken mit Score 0 sind genau die, deren Lösung das Feld verändern
würde. Sie haben Score 0, **weil ein Objekt entweder existiert oder nicht** —
es gibt keinen Zwischenzustand, in dem man „halb" eine Kohomologietheorie über
Spec(ℤ) hätte. Fehlende Objekte erzeugen keine messbaren Zwischenschritte.

> **Die Bewertungsskala misst also nicht Erfolgsaussicht, sondern
> Messbarkeit — und Messbarkeit ist im Wesentlichen dasselbe wie
> „die Methode ist ausgereizt genug, um Zahlen zu produzieren".**

Wer ein Forschungsprogramm nach Near-Miss-Score auswählt, wählt systematisch
die ausgereizten Methoden und meidet die folgenreichen. Das ist der wichtigste
praktische Hinweis dieses Dokuments — und der Grund, warum es unmittelbar neben
`docs/63` (Entscheidungswert von Experimenten) gelesen werden sollte.

### 3. Score 6 heißt nicht „fast fertig"
Alle drei Spitzenlücken sind, soweit bekannt, **äquivalent zur RH**:
- Λ ≤ 0 ist äquivalent zur RH.
- Hyperbolizität aller Jensen-Polynome ist äquivalent zur RH.
- Der Grenzübergang der abgeschnittenen Weil-Form liefert vermutlich die volle
  Weil-Positivität und damit die RH.

Der Score sagt nur: hier ist bereits unbedingt bewiesene Substanz vorhanden,
und es gibt eine Größe, die sich bewegt hat. Er sagt **nicht**, dass der letzte
Schritt klein ist. Bei `doc-29` sagt die Wissensbasis das sogar ausdrücklich:
die Hermite-Approximation kontrolliert festes d bei n → ∞, gebraucht wird
d ~ n — **die bewiesene Folge läuft in die falsche Richtung.** Deshalb steht
dort C = 0 trotz eines gefeierten Resultats.

### 4. Ein Score-0-Eintrag ist der wichtigste der Liste
`gap-weil-positivity` (`doc-14`) hat Score 0 und ist zugleich die Lücke, auf
die neun Ansätze zulaufen (`docs/55`, Beobachtung 1). Über 𝔽_q ist genau diese
Positivität ein **Satz** — geliefert von der Schnittform auf C × C. Über ℤ ist
sie eine Umformulierung des Ziels. Der gesamte Unterschied zwischen bewiesenem
und offenem Fall lässt sich an dieser einen Zeile ablesen.

### 5. Zwei Lücken zielen gar nicht auf die RH
`gap-density-to-lindeloef` (Guth–Maynard) zielt auf Lindelöf,
`gap-landau-siegel-exclusion` (Zhang) auf die GRH. Beides sind bedeutende
unbedingte Fortschritte — und beide werden in der Rezeption regelmäßig als
„Fortschritt bei der Riemann-Vermutung" verkauft. Der Deckel `erreichbar=false`
ist im Datenmodell genau dafür da, diesen Kategorienfehler sichtbar zu machen.

## Lean-Gap-Ledger

Die Lücken sind in `kb/lean/RH/Gaps.lean` als Lean-4-Skelette mit `sorry`
hinterlegt: jede Lücke bekommt eine Signatur, einen Kommentar mit Doku-Bezug
und ein offenes Beweisziel. Das leistet dreierlei:

1. **Präzisionszwang.** Eine Lücke, die sich nicht als Lean-Signatur schreiben
   lässt, ist nicht präzise genug formuliert. Der Versuch ist der Test.
2. **Maschinelle Adressierbarkeit.** Ein `sorry` ist eine Adresse, auf die man
   Arbeit richten kann — für Menschen wie für Beweisassistenten.
3. **Ehrliche Buchführung.** Die Zahl der `sorry` ist die Zahl der offenen
   Stellen. Sie kann nur durch Beweisen sinken, nicht durch Umformulieren.

Wichtig und ausdrücklich: Diese Skelette sind **Formulierungen, keine
Beweisfortschritte**. Sie machen die Lücken adressierbar; sie machen sie nicht
kleiner. Der Status der Lean-Werkzeugkette im Repo steht ehrlich in
`kb/lean/README.md`.

## Wie man die Registry pflegt

- **Neue Lücke:** Eintrag in `kb/graph/gaps.json` mit Achsenwerten **und
  Begründungsfeldern**; `python3 kb/gaps.py` neu laufen lassen.
- **Ein Resultat erscheint:** die betroffene Achse ändern, Begründung
  aktualisieren, `bewiesen`/`fehlt` neu schreiben. Der Score folgt automatisch.
- **Verboten:** den Score von Hand setzen. Er ist eine Funktion der Daten.

## Quellen
Alle Sachaussagen über bewiesene Teilresultate stammen aus den Einzeldokumenten
und sind dort belegt: `docs/04`, `docs/05`, `docs/13`, `docs/14`, `docs/15`,
`docs/16`, `docs/22`, `docs/23`, `docs/29`, `docs/30`, `docs/32`, `docs/44`,
`docs/52`, `docs/53`. Zentrale Primärbelege für die Kennzahlen:
- [Rodgers & Tao, *The de Bruijn–Newman constant is non-negative* (arXiv 1801.05914)](https://arxiv.org/abs/1801.05914)
- [Polymath15, *Effective approximation of heat flow evolution of the Riemann ξ function* (arXiv 1904.12438)](https://arxiv.org/abs/1904.12438)
- [Griffin, Ono, Rolen & Zagier, *Jensen polynomials for the Riemann zeta function* (PNAS 116, 2019)](https://www.pnas.org/doi/10.1073/pnas.1902572116)
- [Guth & Maynard, *New large value estimates for Dirichlet polynomials* (arXiv 2405.20552)](https://arxiv.org/abs/2405.20552)
