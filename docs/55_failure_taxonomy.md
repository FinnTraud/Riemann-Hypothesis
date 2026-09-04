---
id: doc-55
number: 55
title: "Muster im Scheitern: Blocker-Taxonomie & Obstruktions×Ansatz-Matrix"
category: meta
status: meta
tags: [failure-patterns, taxonomy, blockers, meta-analysis, matrix]
source_file: 55_failure_taxonomy.md
lang: de
---

# Muster im Scheitern: Blocker-Taxonomie & Obstruktions×Ansatz-Matrix

**Kategorie:** Meta / Querschnittsanalyse
**Typ:** Aggregation über alle Ansatz-Dokumente
**Status:** Analytische Auswertung (keine neuen mathematischen Behauptungen)
**Datenquelle:** `kb/graph/blockers.json` · Matrix generiert von `kb/matrix.py`
**Herkunft:** Zusammenführung zweier unabhängig entstandener Klassifikationen (PR #5: `F1`–`F15`; PR #6: `blk-*`). Jeder Blocker trägt seine F-ID im Feld `f_mode` weiter.

## Zweck

`docs/35` listet Obstruktionen. `docs/41` listet Leitmotive. Was beide nicht
leisten: die **Umkehrung der Blickrichtung**.

Die Wissensbasis ordnet bisher jedem Ansatz seinen Scheiterngrund zu — eine
Abbildung *Ansatz → Grund*. Dieses Dokument invertiert sie zu *Grund → Ansätze*
und wertet die Fasern aus. Das Ergebnis ist die eigentliche Aussage:

> **56 dokumentierte Ansätze scheitern an 15 wiederkehrenden Blockern —
> im Mittel 1,7 pro Ansatz. Ein einziger Blocker, zirkuläre Positivität,
> trägt 11 davon.**

Diese Zahl ist der Grund, warum die RH nicht „schwer wie 40 offene Probleme"
ist, sondern „schwer wie eine Handvoll Probleme, die immer wieder in neuem
Gewand auftauchen". Wer das sieht, bewertet einen neuen Ansatz anders: die
erste Frage ist nicht „ist die Idee originell?", sondern **„welchen der fünfzehn
Blocker adressiert sie, und wie?"**

## Was ein Blocker ist — und was nicht

Ein **Blocker** ist ein *struktureller* Grund, der bei mehreren Ansätzen in
identischer Form auftritt. Er ist zu unterscheiden von:

| Nicht ein Blocker | Beispiel | Warum nicht |
|---|---|---|
| ein Rechenfehler | Atiyahs Todd-Funktion (doc-25) | einmalig, nicht übertragbar |
| eine unbewiesene Zwischenbehauptung | de Branges' Positivitätsannahme (doc-20) | das ist die *Instanz* eines Blockers, nicht der Blocker |
| Schwierigkeit an sich | „die RH ist schwer" | nicht operationalisierbar |

Ein Blocker hat immer eine **Fluchtbedingung**: eine präzise Angabe, was ein
Ansatz zeigen müsste, um ihn zu überwinden. Ohne Fluchtbedingung ist es eine
Ausrede, kein Blocker.

## Tier-System

- **Tier 1 — harte Obstruktion mit Gegenbeispiel.** Es existiert ein
  konkretes mathematisches Objekt, das den Ansatz widerlegt. Nicht
  verhandelbar. (Euler-Blindheit, Parität, Weichheit)
- **Tier 2 — strukturelle Lücke ohne bekannten Ausweg.** Kein Gegenbeispiel,
  aber auch kein bekannter Weg. Hier sitzen die interessanten Ansätze.
  (Zirkuläre Positivität, nicht-kanonischer Operator, fehlende Geometrie,
  Grenzübergang, Anteils-Decke)
- **Tier 3 — Methodengrenze / Warnung.** Kein Hindernis für einen Beweis,
  sondern eine Fehlerquelle bei der *Bewertung* oder bei der *Prüfbarkeit*.
  (Numerische Extrapolation, Modellzirkularität, Nicht-Verifizierbarkeit)

Die Unterscheidung ist praktisch relevant: **Tier 1 disqualifiziert sofort,
Tier 2 markiert Forschungsfront, Tier 3 markiert Interpretationsfehler.**

## Die fünfzehn Blocker

| ID | `F` | Name | Tier | Fluchtbedingung (Kurzform) |
|---|:-:|---|:-:|---|
| `blk-euler-blindness` | `F1` | Euler-Blindheit | 1 | Ein Schritt muss für Davenport–Heilbronn falsch sein |
| `blk-limit-exchange` **⁺** | `F5` | Unerlaubte Vertauschung | 1 | Jede Vertauschung einzeln rechtfertigen, Paarung ρ↔1−ρ̄ beibehalten |
| `blk-parity` | `F8` | Paritätsbarriere | 1 | Bilinearer oder spektraler Input von außerhalb des Siebs |
| `blk-softness` | `F7` | Weichheitsbarriere (Voronin) | 1 | Globale Rigidität statt lokaler Funktionentheorie |
| `blk-equivalence-trap` | `F11` | Äquivalenz-Falle | 2 | Eine Richtung strikt schwächer und unbedingt, oder eine bewegliche Kennzahl |
| `blk-ineffective-constants` **⁺** | `F12` | Ineffektive oder nicht gleichmaessige Konstanten | 2 | Alle Konstanten explizit und gleichmäßig in T und q |
| `blk-limit-interchange` | `F9` | Konvergenz- / Grenzübergangslücke | 2 | Von der Abschneidung unabhängige Schranke |
| `blk-missing-base-geometry` | `F10` | Fehlende Geometrie über Spec(ℤ) | 2 | Kohomologie + Lefschetz + Index-Positivität |
| `blk-no-selfadjoint-realization` **⁺** | `F4` | Fehlende selbstadjungierte Realisierung | 2 | Definitionsbereich und diskretes Spektrum beweisen, nicht behaupten |
| `blk-noncanonical-operator` | `F3` | Nicht-kanonischer Operator | 2 | Arithmetischer Raum + Spurformel mit Primzahltermen |
| `blk-positivity-circular` | `F2` | Zirkuläre Positivität | 2 | Positivität aus nullstellen-unabhängiger Struktur |
| `blk-proportion-ceiling` | `F13` | Anteils-Decke der Mollifier-Methoden | 2 | Mechanismus für *alle* statt für *einen Anteil* der Nullstellen |
| `blk-finite-evidence` | `F6` | Numerische Extrapolation | 3 | nicht überwindbar, nur vermeidbar |
| `blk-model-circularity` | `F14` | Zirkularität der Modellannahme | 3 | Unbedingte Formulierung ohne RH-Annahme |
| `blk-unverifiable` | `F15` | Nicht-Verifizierbarkeit | 3 | Vollständiger, öffentlicher, idealerweise maschinengeprüfter Beweistext |

**⁺** = erst durch die Zusammenführung sichtbar geworden; in der ursprünglichen Zwölfer-Taxonomie fehlten sie oder waren in einem gröberen Blocker subsumiert.

Vollständige Beschreibungen inkl. Fluchtbedingungen: `kb/graph/blockers.json`.

## Wie robust ist die Tier-Einstufung?

Diese Taxonomie entstand durch **Zusammenführung zweier unabhängig erstellter
Klassifikationen** — zwei Sitzungen, die dasselbe Material ohne Kenntnis
voneinander geordnet haben. Das erlaubt eine Messung, die man sonst nie
bekommt: **wie stabil ist so eine Einteilung eigentlich?**

**Bei der Identifikation der Modi: sehr stabil.** Zwölf der fünfzehn Blocker
wurden beidseitig gefunden, oft bis in die Formulierung hinein. Drei Modi hatte
nur eine Seite (`blk-no-selfadjoint-realization`, `blk-limit-exchange`,
`blk-ineffective-constants`) — alle drei sind Verfeinerungen, keine
Widersprüche.

**Bei der Tier-Zuordnung: deutlich weniger stabil.** Von zwölf gemeinsamen
Modi wurden **fünf verschieden eingestuft**:

| `F` | Blocker | PR #5 | hier | Worum der Dissens geht |
|---|---|:-:|:-:|---|
| `F6` | Numerische Extrapolation | 1 | 3 | Ist „Numerik als Beweis" ein **fataler Fehler** oder ein **Bewertungsfehler**? |
| `F8` | Paritätsbarriere | 3 | 1 | Ist die Paritätsschranke eine **Methodengrenze** oder eine **bewiesene Obstruktion**? |
| `F11` | Äquivalenz-Falle | 3 | 2 | Ist eine Äquivalenz ohne neuen Zugriff ein **struktureller Deckel** oder eine **offene Front**? |
| `F13` | Anteils-Decke | 3 | 2 | dieselbe Frage für Mollifier-Methoden |
| `F15` | Nicht-Verifizierbarkeit | 1 | 3 | Ist ein ungeprüfter Beweis **falsch** oder **statuslos**? |

Der Dissens ist nicht zufällig, sondern **systematisch**: Die eine Seite stuft
*Prozessfehler* (Numerik als Beweis, gescheiterte Verifikation) als Tier 1
fatal ein, die andere als Tier 3 — weil es keine mathematischen Obstruktionen
sind, sondern Fehler im Umgang mit ihnen. Umgekehrt bei der Parität: Tier 1
(es gibt ein bewiesenes Negativresultat) gegen Tier 3 (es ist eine
Methodenreichweite).

**Was daraus folgt.** Die Tier-Zahl ist eine **Konvention, keine Messung**. Sie
ordnet Prioritäten und taugt nicht als Argument. Die abweichenden Einstufungen
sind in `kb/graph/blockers.json` im Feld `tier_abweichung` bei jedem
betroffenen Blocker dokumentiert, statt stillschweigend aufgelöst zu werden.

Ein Nebenertrag: **die drei nur einseitig gefundenen Blocker sind ein Maß für
die Vollständigkeit.** Zwei unabhängige Durchgänge finden zusammen 15 Modi,
einzeln 12 bzw. 15 — ein dritter fände vermutlich weitere. Die Taxonomie ist
nützlich, aber nicht abgeschlossen.

## Obstruktions × Ansatz-Matrix

<!-- MATRIX:BEGIN (generiert von kb/matrix.py -- nicht von Hand editieren) -->

**Lesart:** ● = dieser Blocker trifft den Ansatz. Spalten nach Tier sortiert (Tier 1 links). Zeilen nur für Dokumente, die mindestens einen Blocker tragen — reine Referenz-, Glossar- und Meta-Dokumente fehlen daher bewusst.

| Dok | Ansatz | EUL<br><sub>T1</sub> | SWAP<br><sub>T1</sub> | PAR<br><sub>T1</sub> | SOFT<br><sub>T1</sub> | AEQ<br><sub>T2</sub> | EFF<br><sub>T2</sub> | LIM<br><sub>T2</sub> | GEO<br><sub>T2</sub> | SA<br><sub>T2</sub> | OP<br><sub>T2</sub> | POS<br><sub>T2</sub> | PROP<br><sub>T2</sub> | NUM<br><sub>T3</sub> | MOD<br><sub>T3</sub> | VER<br><sub>T3</sub> | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `02` | Riemann–von-Mangoldt-Formel und die explizi… |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| `03` | Hardy |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | **1** |
| `04` | Levinson, Conrey & Co. |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | **1** |
| `05` | Die Hilbert–Pólya-Vermutung |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  | **2** |
| `06` | Montgomery-Paarkorrelation & Random-Matrix-… |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  | **2** |
| `07` | Keating–Snaith |  |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  | **2** |
| `08` | Berry–Keating H = xp Modell |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  | **2** |
| `09` | Bender–Brody–Müller |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  | **2** |
| `10` | Alain Connes |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  | **2** |
| `11` | Connes–Moscovici |  |  |  |  |  |  | ● |  | ● | ● |  |  |  |  |  | **3** |
| `12` | Nullstellenfreie Regionen |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| `13` | Nyman–Beurling-Kriterium & Báez-Duarte-Vers… |  |  |  |  | ● |  | ● |  |  |  | ● |  |  |  |  | **3** |
| `14` | Li-Kriterium, Bombieri–Lagarias & Weil-Posi… |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  | **2** |
| `15` | Robins Ungleichung & Lagarias' elementares… |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  | **1** |
| `16` | Mertens-Funktion & Riesz-Kriterium |  |  | ● |  | ● |  |  |  |  |  |  |  | ● |  |  | **3** |
| `17` | Lindelöf-Hypothese & Dichte-Hypothese |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | **1** |
| `18` | Weil-Vermutungen |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | **1** |
| `20` | Louis de Branges |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● | **2** |
| `22` | Guth–Maynard |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | **1** |
| `23` | De-Bruijn–Newman-Konstante |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  |  | **2** |
| `24` | Numerische Verifikation der Riemann-Vermutu… |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | **1** |
| `25` | Michael Atiyah | ● |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● | **3** |
| `26` | John Nash |  | ● |  |  |  |  |  |  |  |  |  |  |  |  | ● | **2** |
| `27` | Weitere umstrittene, zurückgezogene & fehle… | ● | ● |  | ● |  |  |  |  |  |  |  |  |  |  | ● | **4** |
| `29` | Jensen–Pólya-Programm |  |  |  |  | ● |  | ● |  |  |  | ● |  |  |  |  | **3** |
| `30` | Der Körper mit einem Element |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | **1** |
| `31` | Deningers Kohomologie-Programm & dynamische… |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | **1** |
| `32` | Landau–Siegel-Nullstellen |  |  | ● |  |  | ● |  |  |  |  |  |  |  |  |  | **2** |
| `33` | Statistische Mechanik & Lee–Yang-Analogie |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |  | **2** |
| `34` | Bost–Connes-System |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | **1** |
| `35` | Obstruktionen & Barrieren | ● |  | ● |  |  |  |  |  |  | ● |  |  | ● |  |  | **4** |
| `37` | Formalisierung |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | **1** |
| `39` | Cramér-Modell & probabilistische Heuristike… |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  | **2** |
| `41` | Synthese |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  | **1** |
| `43` | Epstein-Zetafunktionen & Selberg-Klassen-Ri… | ● |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | **2** |
| `44` | Lapidus |  |  |  |  | ● |  | ● |  |  |  |  |  |  |  |  | **2** |
| `45` | Weitere äquivalente Kriterien |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  | **2** |
| `46` | Voronin-Universalität | ● |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | **2** |
| `47` | Physik-Schicht |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  | **2** |
| `48` | Weitere algebraische/spektrale Programme |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | **1** |
| `49` | Live-Front der analytischen Zahlentheorie |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | **1** |
| `52` | Abgeschnittene Weil-Quadratform & Zeta-Spek… |  |  |  |  |  |  | ● |  |  |  | ● |  |  |  |  | **2** |
| `53` | Paarkorrelation ohne RH & die Alternative H… |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | **1** |
| `54` | Maschinengestützte Zahlentheorie |  |  |  |  |  | ● |  |  |  |  |  |  |  |  | ● | **2** |
| `61` | Negativraum |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | **1** |
| `65` | Sensitivität der Kriterien |  |  |  |  | ● |  |  |  |  |  |  |  | ● |  |  | **2** |
| `66` | Speisers Satz & die Nullstellen von ζ′ |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | **1** |
| `67` | Turáns Potenzsummen-Programm & die Partials… | ● |  |  |  |  |  | ● |  |  |  |  |  |  |  |  | **2** |
| `69` | Möbius-Zufälligkeit |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| `71` | Grothendiecks Standardvermutungen & Motive |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  | **2** |
| `72` | Arakelov-Geometrie & die Kompaktifizierung… |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | **1** |
| `73` | Tates These & adelische Analysis | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| `74` | Hybrides Euler–Hadamard-Produkt |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | **1** |
| `75` | Extremwerte von ζ |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | **1** |
| `76` | Höhere Korrelationen |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | **1** |
| `77` | Bagchis Satz |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | **1** |
| | **Σ Ansätze je Blocker** | **7** | **3** | **5** | **4** | **9** | **3** | **6** | **8** | **5** | **6** | **11** | **6** | **8** | **8** | **6** | **95** |

**Spaltenlegende** (in Klammern die ID der zusammengeführten Parallel-Taxonomie, siehe `kb/graph/blockers.json`): `EUL` = Euler-Blindheit (F1) · `SWAP` = Unerlaubte Vertauschung (F5) · `PAR` = Paritätsbarriere (F8) · `SOFT` = Weichheitsbarriere (Voronin) (F7) · `AEQ` = Äquivalenz-Falle (F11) · `EFF` = Ineffektive oder nicht gleichmaessige Konstanten (F12) · `LIM` = Konvergenz- / Grenzübergangslücke (F9) · `GEO` = Fehlende Geometrie über Spec(ℤ) (F10) · `SA` = Fehlende selbstadjungierte Realisierung (F4) · `OP` = Nicht-kanonischer Operator (F3) · `POS` = Zirkuläre Positivität (F2) · `PROP` = Anteils-Decke der Mollifier-Methoden (F13) · `NUM` = Numerische Extrapolation (F6) · `MOD` = Zirkularität der Modellannahme (F14) · `VER` = Nicht-Verifizierbarkeit (F15)

**Kennzahlen (automatisch):** 56 Ansätze tragen zusammen 95 Blocker-Zuordnungen bei 15 Blockern — im Mittel 1.7 Blocker pro Ansatz. Häufigster Blocker: **Zirkuläre Positivität** (11 Ansätze). Am stärksten blockierte Ansätze: `35` (4), `27` (4), `29` (3), `25` (3).

<!-- MATRIX:END -->

## Auswertung: fünf Beobachtungen, die erst aus der Matrix sichtbar werden

### 1. Positivität ist der Flaschenhals, nicht ein Ansatz unter vielen
Neun Ansätze — Nyman–Beurling, Li/Weil, de Branges, de-Bruijn–Newman,
Jensen–Pólya, Lee–Yang, Connes, abgeschnittene Weil-Form, weitere Kriterien —
hängen an derselben Hürde. Sie sind keine neun unabhängigen Versuche, sondern
**neun Beschreibungen desselben Problems**. Der Erkenntnisgewinn eines
weiteren Positivitätskriteriums ist entsprechend gering; der Gewinn eines
Positivitätsbeweises wäre total.

### 2. Der bewiesene Fall überwindet drei Blocker gleichzeitig
Über 𝔽_q (doc-18) sind `blk-positivity-circular`, `blk-noncanonical-operator`
und `blk-missing-base-geometry` **alle drei zugleich** gelöst — und zwar durch
ein einziges Objekt, die Fläche C×C mit ihrer Schnittform. Das ist kein Zufall:
Positivität, Spektrum und Geometrie sind dort **dieselbe Aussage in drei
Sprachen**. Über ℤ zerfallen sie in drei getrennte offene Probleme.

**Folgerung für die Bewertung von Ansätzen:** Ein Ansatz, der nur *einen* der
drei Blocker adressiert, rekonstruiert die Blaupause nur zu einem Drittel. Die
aussichtsreichen Programme (Connes, Deninger) sind genau die, die alle drei
gleichzeitig angreifen — und genau deshalb sind sie so schwer.

### 3. Tier-1-Blocker treffen fast ausschließlich gescheiterte Beweise
Die drei harten Obstruktionen betreffen `doc-25`, `doc-26`, `doc-27`,
`doc-46` — also Fehlversuche und Meta-Warnungen. Kein einziges der aktiven
Forschungsprogramme steht unter Tier 1. Das ist ein **Gütesiegel für die
Auswahl der dokumentierten Programme**: die Fachwelt hat die Tier-1-Fälle
bereits ausgesiebt. Umgekehrt: Wer einen neuen Ansatz vorschlägt, landet mit
sehr hoher Wahrscheinlichkeit bei Tier 1 — deshalb steht der Test darauf am
Anfang jeder Prüfung (`evaluate_proof_idea`, `kb/counterexample.py`).

### 4. Die Grenzübergangslücke ist der jüngste Blocker — und der einzige, der schrumpft
`blk-limit-interchange` betrifft die *neuesten* Arbeiten (Connes–van Suijlekom
2022+, GORZ 2019, Baez-Duarte-Raten). Er unterscheidet sich qualitativ von
allen anderen Tier-2-Blockern: es gibt eine **Folge bewiesener Aussagen**, die
auf das Ziel zuläuft. Bei `blk-positivity-circular` gibt es das nicht — dort
gibt es nur Umformulierungen. Das ist der Grund, warum die Near-Miss-Bewertung
in `docs/58` diesen Blocker gesondert behandelt.

### 5. Die Äquivalenz-Falle erklärt, warum die Kriterienliste wächst, aber nicht näher kommt
Sieben Ansätze — Nyman–Beurling, Li/Weil, Robin, Riesz/Mertens, Volchkov &
Co., Lapidus, Jensen–Pólya — sind *Äquivalente* der RH. Logisch heißt das:
sie sind exakt gleich schwer. Eine wachsende Sammlung äquivalenter Kriterien
sieht nach Fortschritt aus und ist keiner. Ihr echter Wert ist ein anderer und
sollte auch so benannt werden: sie übersetzen die RH in Sprachen (Arithmetik,
Kombinatorik, Funktionalanalysis, Fraktalgeometrie), von denen eine
möglicherweise eine unabhängige Struktur mitbringt. Die Wette ist die
Übersetzung, nicht das Kriterium.

**Konsequenz für die Near-Miss-Frage:** Ein äquivalentes Kriterium kann
definitionsgemäß kein Near-Miss sein. Genau darauf baut die Bewertung in
`docs/58` auf.

### 6. Der einzige Blocker, den man heute schon beseitigen kann, ist kein mathematischer
`blk-unverifiable` trifft vier Dokumente — Nash (kein Beweistext), Atiyah
(unpublizierte Grundlage), de Branges (Prüfungsermüdung nach drei Jahrzehnten
revidierter Fassungen), plus die arXiv-Behauptungen. In keinem dieser Fälle
lautet der Status „widerlegt", sondern „nicht mit vertretbarem Aufwand
entscheidbar". Das ist der einzige Blocker der Sammlung mit einer *heute
technisch erreichbaren* Fluchtbedingung: maschinelle Verifikation
(`docs/37`, `docs/54`) macht Prüfaufwand unabhängig von Reputation und Geduld.

### 7. Ein Blocker ist maschinell prüfbar — genau einer
Nur `blk-euler-blindness` besitzt ein explizites Gegenbeispiel und ist damit
als *Test* implementierbar (`kb/counterexample.py`, Test T2/T4, siehe
`docs/60`). Alle anderen erfordern menschliches Urteil. Das begrenzt, was
Automatisierung hier leisten kann — und sagt zugleich, wo sie ansetzen sollte
(vgl. `docs/62`).

## Wie man das benutzt

**Für einen neuen Ansatz:**
1. Welchen Blocker adressiert er? (Wenn keinen: er adressiert nichts.)
2. Erfüllt er dessen Fluchtbedingung — beweisbar, nicht behauptet?
3. Steht er unter irgendeinem Tier-1-Blocker? Dann ist er widerlegt.

**Für die Bewertung eines Programms:** Zähle die gleichzeitig adressierten
Blocker. Drei ist die Zahl, die der bewiesene Fall braucht.

## Verwandte Dokumente
- `docs/35` — die Obstruktionen im Detail (Datenquelle)
- `docs/41` — die drei Leitmotive (orthogonale Zerlegung derselben Landschaft)
- `docs/56` — Autopsien: die Bruchstelle je gescheitertem Beweis
- `docs/57` — was aus den Lücken der Matrix folgt
- `docs/58` — Near-Miss-Bewertung auf Basis der Blocker
- `docs/60` — das Gegenbeispiel-Orakel, das `blk-euler-blindness` operationalisiert

## Quellen
Dieses Dokument enthält **keine neuen mathematischen Behauptungen**. Es
aggregiert ausschließlich die in `docs/03`–`docs/54` belegten Aussagen; die
Belege stehen jeweils dort. Die primären Grundlagen der Blocker:
- [On some reasons for doubting the Riemann hypothesis — A. Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- [The Riemann Hypothesis — E. Bombieri (Clay)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
- [Zeros of the Davenport–Heilbronn Counterexample (AMS Math. Comp. 76, 2007)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (10)
> - *verallgemeinert* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Diagnose-Ebene über den Obstruktionen.
> - *ist Instanz von* → **Fehlermodi (Scheiterns-Taxonomie)** — Prosa-Ebene der Taxonomie F1–F15.
> - *benutzt* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Aggregiert die Obstruktionen zu einer Blocker-Taxonomie (Grund -> Ansaetze).
> - *benutzt* → [[41_synthesis_what_a_proof_needs|41 · Synthese]] — Invertiert die Leitmotiv-Zerlegung zur Obstruktions-x-Ansatz-Matrix.
> - *benutzt* → [[78_approach_comparison_matrix|78 · Vergleichsmatrix der Ansätze]] — Die Matrix ordnet Ansaetze nach Achsen, die Blocker nach Huerden -- komplementaere Sichten.
> - ← *wird benutzt von* [[57_untried_directions|57 · Noch nicht Versuchtes]] — Leitet Richtungen aus den Luecken der Blocker-Matrix ab.
> - ← *wird benutzt von* [[58_gap_registry_near_miss|58 · GAP-Registry & Near-Miss-Bewertung]] — Bewertet die Luecken entlang der Blocker-Zuordnung.
> - ← *wird benutzt von* [[63_experiment_decision_value|63 · Entscheidungswert von Experimenten]] — Bemisst Experimente an der Reichweite in der Blocker-Matrix.
> - ← *wird benutzt von* [[60_counterexample_oracle|60 · Das Gegenbeispiel-Orakel]] — Erklärt die Fehlermodus-Notizen im Graphen.
> - ← *wird benutzt von* [[78_approach_comparison_matrix|78 · Vergleichsmatrix der Ansätze]] — Die Fehlermodus-Spalte verweist auf die zusammengefuehrte Blocker-Taxonomie.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
