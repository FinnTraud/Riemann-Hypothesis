---
id: doc-57
number: 57
title: "Noch nicht Versuchtes: aus den Blocker-Lücken abgeleitete Richtungen"
category: meta
status: open
tags: [open-directions, generative, falsification, research-agenda, li-sensitivity]
source_file: 57_untried_directions.md
lang: de
---

# Noch nicht Versuchtes: aus den Blocker-Lücken abgeleitete Richtungen

**Kategorie:** Meta / generativ
**Typ:** Ableitungen aus `docs/55` (Matrix) und `docs/56` (Autopsien)
**Status:** ⚠️ **Spekulativ** — siehe Ehrlichkeitsklausel
**Verwandt:** `docs/55`, `docs/56`, `docs/58`, `docs/60`, `docs/63`

## Ehrlichkeitsklausel — bitte zuerst lesen

Dieses Dokument leitet Richtungen ab, die in **dieser Wissensbasis** nicht
dokumentiert sind. Das ist **nicht** dasselbe wie „in der Mathematik noch nicht
versucht". Die RH ist seit 165 Jahren das meistbearbeitete offene Problem der
Zahlentheorie; die Grundannahme muss lauten, dass jede naheliegende Idee
bereits jemand hatte. Der wahrscheinlichste Zustand jedes Eintrags unten ist:

> *bekannt, publiziert, und hier schlicht nicht erfasst.*

Der Wert des Dokuments liegt deshalb nicht in Originalitätsansprüchen, sondern
in zwei anderen Dingen:

1. **Als Literatursuchplan.** Jeder Eintrag ist präzise genug formuliert, um
   gezielt danach zu suchen. Findet man ihn, gehört er als Dokument in die
   Wissensbasis — die Lücke war eine Lücke der Erfassung.
2. **Als Falsifikationsprogramm.** Jeder Eintrag hat ein **Abbruchkriterium**:
   eine Beobachtung, die ihn erledigt. Ohne Abbruchkriterium ist ein Vorschlag
   kein Vorschlag, sondern eine Hoffnung.

Einträge sind nach **Prüfbarkeit** sortiert, nicht nach Erfolgsaussicht. U1 und
U2 sind mit dem vorhandenen Code heute rechenbar; U5 und U6 sind
Forschungsprogramme.

---

## U1 · Gegenbeispiel-Kontrolle für jedes numerische Kriterium

**Herleitung aus der Matrix.** Fünf Dokumente tragen `blk-finite-evidence`.
Alle numerischen Experimente der Wissensbasis (λ_n-Positivität, d_N, GUE,
ψ(x)-Konvergenz) laufen ausschließlich auf ζ — also auf einer Funktion, bei
der die RH vermutlich gilt. **Damit misst kein einziges Experiment seine
eigene Trennschärfe.** Ein Test, der nie an einem Positivfall (= RH verletzt)
kalibriert wurde, hat unbekannte Sensitivität.

**Vorschlag.** Jedes numerische Kriterium bekommt einen **Negativkontroll-Lauf**
gegen die Davenport–Heilbronn-Funktion. Die Frage ist nicht „bestätigt das
Kriterium die RH für ζ?", sondern: **„ab welchem Rechenaufwand würde dieses
Kriterium eine bekannte Verletzung bemerken?"**

**Erstes Ergebnis — bereits gerechnet.** Für das Li-Kriterium ist die Antwort
ernüchternd und quantitativ. Der Beitrag einer Nullstelle ρ = β + iγ zu λ_n
enthält den Term −(1 − 1/ρ)ⁿ mit

```
|1 − 1/ρ| = 1 + (1 − 2β)/(2γ²) + O(γ⁻⁴)     >  1  ⟺  β < 1/2
```

Eine Nullstelle links der Geraden treibt λ_n also exponentiell nach −∞ — aber
mit einer Rate, die **quadratisch mit der Höhe abfällt**. Die nötige Ordnung n
wächst folglich wie γ². Angewandt auf die tatsächlichen DH-Nullstellen
(`kb/counterexample.py lisens`, Ergebnis in `kb/research/results/oracle_li_sensitivity.json`):

| DH-Nullstelle (Partner links der Geraden) | Wachstumsrate − 1 | nötiges n |
|---|---|---|
| 0,1915 + 85,699 i | 4,19 · 10⁻⁵ | **342 000** |
| 0,3492 + 114,163 i | 1,16 · 10⁻⁵ | **1 369 000** |
| 0,2757 + 176,702 i | 7,17 · 10⁻⁶ | **2 289 000** |
| 0,4256 + 166,479 i | 2,67 · 10⁻⁶ | **6 577 000** |

Und in der Umkehrung — bis zu welcher Höhe trägt ein gegebenes Rechenbudget?

| λ_n berechnet bis n ≤ | schließt Nullstellen abseits aus bis γ ≈ |
|---|---|
| 100 | **1,4** |
| 1 000 | **3,6** |
| 10 000 | **9,8** |
| 10⁶ | **80** |
| 10⁹ | **2 089** |

**Die Pointe.** Die erste ζ-Nullstelle liegt bei γ = 14,13. Direkte
Nullstellenberechnung hat die RH bis γ ≈ 3 · 10¹² verifiziert (`docs/24`).
Ein Li-Budget von n ≤ 1000 — mehr, als üblicherweise gerechnet wird — reicht
**nicht einmal bis zur ersten Nullstelle**. Selbst n ≤ 10⁹ bliebe neun
Größenordnungen hinter der direkten Rechnung zurück.

> **Numerische λ_n-Positivität ist als RH-Evidenz praktisch wertlos** — nicht
> weil zu wenig gerechnet wird, sondern weil das Kriterium bei großen Höhen
> strukturell blind ist. Wo λ_n-Rechnungen als „Bestätigung der RH" zitiert
> werden, ist das eine Fehlinterpretation um Größenordnungen.

Das ist keine Kritik am Li-Kriterium als *Kriterium* — als Äquivalenz ist es
korrekt und nützlich. Es ist eine Aussage über seine **numerische
Trennschärfe**, und diese Aussage fehlt in der Literatur zur Zetafunktion
weitgehend, weil niemand das Kriterium an einem Gegenbeispiel kalibriert hat.

**Fortsetzung: durchgeführt.** Die angekündigte Analyse für d_N, Robin und Λ
ist inzwischen gerechnet — Ergebnisse in **`docs/65`** (`kb/sensitivity.py`).
Die damals geäußerte Vermutung („d_N ähnlich schlecht, Robin noch schlechter")
war **in beide Richtungen falsch**:

- **d_N ist mit Abstand das schlechteste** Kriterium, nicht nur „ähnlich":
  d_N < 0,01 verlangt eine Least-Squares-Dimension von N ≈ 10²⁰¹.
- **Robin ist besser als erwartet**, weil seine Testobjekte *komprimierbar*
  sind — kolossal abundante Zahlen speichert man als Exponentenvektor. Eine
  Zahl mit 38 220 Stellen war in Sekunden gerechnet.
- **Λ passt gar nicht ins Schema**: dort gibt es kein Rechenbudget, dessen
  Erhöhung hilft. Die Wand ist methodisch, nicht rechnerisch.

Die **Kompressionsfrage** war vor dieser Rechnung nicht sichtbar und ist eine
eigene Bewertungsachse (`docs/65`, Punkt 4).

**Abbruchkriterium.** Findet sich eine Arbeit, die diese Sensitivitätsanalyse
bereits durchführt, wird U1 zu einem regulären Dokument.

**Aufwand.** Erledigt. Offen bleiben Volchkov/Sekatskii/Redheffer (`docs/45`).

---

## U2 · Ist die abgeschnittene Weil-Form Euler-blind?

**Herleitung.** `docs/52` beschreibt das derzeit aussichtsreichste Programm:
Connes–van Suijlekom zeigen für **jeden endlichen Cutoff Λ**, dass die
Nullstellen der abgeschnittenen Weil-Quadratform korrekt liegen; offen ist nur
der Grenzübergang Λ → ∞ (`blk-limit-interchange`). Die Matrix in `docs/55`
zeigt aber: **kein Ansatz kombiniert diesen Blocker mit dem Gegenbeispiel-Test.**

**Die Frage.** Die abgeschnittene Konstruktion ist auf endlichdimensionalen
Galerkin-Räumen definiert und daher explizit rechenbar. Führt man sie für die
**Davenport–Heilbronn-Funktion** durch:

- **Fall A — die Positivität scheitert bei endlichem Λ.** Dann enthält bereits
  die abgeschnittene Konstruktion arithmetische Information, die DH von ζ
  trennt. Man kann angeben, *welcher* Term das leistet, und das ist genau die
  Stelle, an der das Euler-Produkt eingeht. Sehr wertvoll.
- **Fall B — die Positivität hält für DH bei jedem erreichbaren Λ.** Dann ist
  die endliche Konstruktion Euler-blind, und **die gesamte arithmetische Last
  liegt im Grenzübergang**. Das würde erklären, warum genau dieser Schritt so
  hart ist — und es wäre eine ernüchternde, aber sehr informative Nachricht
  über das Programm.

Beide Ausgänge sind wertvoll. Das ist das Kennzeichen eines guten Experiments
(vgl. `docs/63`).

**Abbruchkriterium.** Wenn die Konstruktion aus `docs/52` für Funktionen ohne
Euler-Produkt formal gar nicht definiert ist (weil sie ein Adelklassenraum
oder ein Euler-Produkt strukturell voraussetzt), ist die Frage
gegenstandslos — **und diese Antwort wäre selbst das Ergebnis:** dann ist die
Trennung bereits in die Definition eingebaut, und man sollte sagen, wo.

**Aufwand.** Hoch. Erfordert die Galerkin-Matrizen aus `docs/52` in
implementierbarer Form. Der ehrlichste erste Schritt ist die
Literaturprüfung: liegt die abgeschnittene Form explizit genug vor?

---

## U3 · Spektralstatistik des endlichen Modells gegen die Alternative Hypothese

**Herleitung.** `docs/52` liefert endliche Matrizen mit *bewiesener*
Nullstellenlage. `docs/53` liefert eine Aussage über Nullstellenabstände ohne
RH-Annahme (Alternative Hypothese, AH). Diese beiden Dokumente sind im Graphen
nicht verbunden — die Matrix zeigt sie unter verschiedenen Blockern
(`blk-limit-interchange` vs. `blk-model-circularity`).

**Die Frage.** Zeigen die Eigenwerte der abgeschnittenen Weil-Form
GUE-Abstandsstatistik, oder zeigen sie AH-typische Struktur (Abstände
konzentriert auf halbzahligen Vielfachen des mittleren Abstands)?

**Warum das nicht kosmetisch ist.** `blk-model-circularity` besagt, dass
GUE-Statistik der ζ-Nullstellen die RH voraussetzt. Beim endlichen Modell ist
das **nicht** so: dort ist die Nullstellenlage ein Satz, kein Postulat. Die
Statistik ist also unbedingt berechenbar. Stimmt sie mit der ζ-Statistik
überein, ist das ein Treuenachweis des Modells, der die Zirkularität umgeht.
Weicht sie ab, weiß man, welche Struktur die Abschneidung zerstört.

**Abbruchkriterium.** Ist die Eigenwertdichte des endlichen Modells so anders
skaliert, dass eine Entfaltung nicht sinnvoll definiert ist, entfällt der
Vergleich.

**Aufwand.** Mittel — sobald U2 die Matrizen bereitstellt. Die Statistikseite
steht bereits (`kb/research/spacing_vs_gue.py`).

---

## U4 · Der leere Quadrant: Ansätze, die am Euler-Produkt ansetzen

**Herleitung.** Beobachtung 4 aus `docs/56`: **kein einziger dokumentierter
Fehlversuch scheitert daran, dass er das Euler-Produkt ernsthaft benutzt.**
Alle scheitern daran, dass sie es nicht benutzen, oder an einer analytischen
Vorstufe. In der Matrix ist das eine leere Spalte-Zeilen-Kombination: es gibt
keine Ansatzklasse „arbeitet an der Multiplikativität, kommt aber nicht durch".

Zwei Deutungen, und sie schließen sich aus:
- **(a)** Der Raum ist leer, weil das der richtige Weg ist und alle
  ernsthaften Programme (Connes, Deninger, Weil-Blaupause) genau dort
  arbeiten — nur nicht unter diesem Etikett. Dann ist die Lücke ein
  Etikettierungsproblem der Wissensbasis.
- **(b)** Der Raum ist leer, weil niemand einen Zugriff auf die
  Multiplikativität hat, der stark genug ist, um überhaupt zu scheitern.

**Vorschlag.** Zuerst (a) prüfen, indem man alle Programme danach neu
klassifiziert, **an welcher Stelle genau die Multiplikativität eingeht** —
nicht ob, sondern wo. Ergebnis wäre eine neue Spalte in der Matrix:
„Euler-Eintrittspunkt". Erst wenn diese Spalte weitgehend leer bleibt, ist (b)
plausibel und die Lücke echt.

**Abbruchkriterium.** Lässt sich für jedes größere Programm ein präziser
Euler-Eintrittspunkt angeben, ist U4 erledigt und die Wissensbasis um eine
nützliche Spalte reicher.

**Aufwand.** Mittel; reine Analysearbeit an vorhandenen Dokumenten.

---

## U5 · Drei Blocker gleichzeitig — systematischer Blaupausen-Abgleich

**Herleitung.** Beobachtung 2 aus `docs/55`: der bewiesene Fall über 𝔽_q löst
`blk-positivity-circular`, `blk-noncanonical-operator` und
`blk-missing-base-geometry` mit **einem** Objekt. Über ℤ zerfällt das in drei
Probleme. In der Matrix trägt aber **kein Dokument alle drei** — Connes
(`doc-10`) trägt zwei, alle anderen einen.

**Vorschlag.** Eine Tabelle, die für jedes Transferprogramm eintragsweise
angibt, was es für jede der drei Rollen liefert — und, härter, **was es für
die anderen beiden schuldig bleibt**. Nicht als Wertung, sondern als
Buchführung:

| Programm | Positivität | Operator/Spektrum | Basisgeometrie | Verbindendes Objekt? |
|---|---|---|---|---|
| Weil/Deligne (𝔽_q) | Schnittform | Frobenius | C ×_𝔽 C | ✅ *ein* Objekt |
| Connes | offen | Adelklassenraum | teilweise | ? |
| Deninger | — | Fluss auf gefoliertem Raum | gesucht | ? |
| 𝔽₁ / arithmetic site | — | — | im Aufbau | ? |

Die entscheidende Spalte ist die letzte. Im bewiesenen Fall sind die drei
Rollen **dasselbe Objekt in drei Sprachen**. Ein Programm, das drei getrennte
Objekte liefert, hat die Blaupause noch nicht rekonstruiert — auch wenn es
formal alle drei Spalten füllt.

**Abbruchkriterium.** Existiert eine solche Gegenüberstellung in der Literatur
(Connes' Übersichtsarbeiten kommen in Frage), ist U5 ein Dokument statt einer
Idee.

**Aufwand.** Mittel bis hoch.

---

## U6 · Formalisierung der Obstruktionen statt der Sätze

**Herleitung.** `docs/37` und `docs/54` behandeln Formalisierung als Weg,
*positive* Resultate zu verifizieren (Hardy, Primzahlsatz). Die Autopsien in
`docs/56` zeigen aber: die Bruchstellen liegen in **elementaren** Sätzen
(Liouville, bedingte Konvergenz, Definitionsbereiche), und der Blocker
`blk-unverifiable` ist der einzige mit heute erreichbarer Fluchtbedingung.

**Vorschlag.** Nicht die RH formalisieren, sondern die **Anti-Crackpot-Checkliste**:
maschinenprüfbare Fassungen von Aussagen wie
- „Diese Funktion hat Funktionalgleichung und Fortsetzung, aber Nullstellen abseits" (Davenport–Heilbronn als formalisiertes Gegenbeispiel),
- „Σ_ρ ist nur bedingt konvergent" (als Typ, der Umordnung verbietet),
- „Ein auf einem Gebiet polynomialer, beschränkter, nicht-konstanter Ganzfunktion existiert nicht" (Liouville).

Ein Beweisversuch könnte dann gegen diese formalisierten Obstruktionen
**typgeprüft** werden, statt gegen sie argumentiert zu werden.

**Warum das die realistischste Idee der Liste ist.** Sie erfordert keinen
Durchbruch, nur Arbeit. Und sie adressiert den einzigen Blocker, der heute
lösbar ist. Erste Skelette: `kb/lean/RH/Gaps.lean` (siehe `docs/58`).

**Abbruchkriterium.** Zeigt sich, dass die Davenport–Heilbronn-Funktion in
Lean/mathlib nicht mit vertretbarem Aufwand definierbar ist (Hurwitz-Zeta,
Funktionalgleichung), reduziert sich U6 auf die rein funktionentheoretischen
Punkte — immer noch nützlich, aber kleiner.

**Aufwand.** Hoch, aber vollständig planbar — und als einzige Idee dieser
Liste **ohne Forschungsrisiko**.

---

## Was NICHT auf dieser Liste steht — und warum

Aus den Blockern folgt genauso deutlich, was man **nicht** versuchen sollte.
Die folgenden Richtungen wirken naheliegend und sind es nicht:

| Naheliegende Idee | Warum sie ausscheidet |
|---|---|
| Noch ein äquivalentes Kriterium | `blk-equivalence-trap` — logisch gleich schwer, kein Fortschritt (`docs/55`, Beob. 5) |
| Höher rechnen (mehr Nullstellen verifizieren) | `blk-finite-evidence` — Mertens/Skewes; und U1 zeigt, wie wenig Numerik trägt |
| Den Anteil auf der Geraden von 41 % weiter treiben | `blk-proportion-ceiling` — selbst 100 % im Dichtesinn ist nicht die RH |
| Einen Operator mit Spektrum {γ_n} angeben | `blk-noncanonical-operator` — zirkulär (Autopsie A4) |
| Ein ML-Modell auf Nullstellen trainieren | `docs/28`, `docs/62` — sagt vorher, beweist nicht |

Diese Negativliste ist praktisch der nützlichste Teil des Dokuments: sie
verhindert Arbeit, die garantiert nicht trägt.

## Quellen
Dieses Dokument leitet ab und behauptet nichts Neues über ζ. Die Ableitungen
stützen sich auf `docs/13`, `docs/14`, `docs/24`, `docs/35`, `docs/37`,
`docs/52`, `docs/53`, `docs/55`, `docs/56`. Die Sensitivitätsrechnung in U1 ist
reproduzierbar über `python3 kb/counterexample.py lisens --func dh`; die
zugrunde liegenden DH-Nullstellen sind in `kb/research/results/oracle_offline_zeros.json`
auf 15 Stellen dokumentiert und gegen
[Balanzario–Sánchez-Ortiz, Math. Comp. 76 (2007)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)
abgeglichen.

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (5)
> - *ist Evidenz für* → [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|14 · Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]] — Sensitivitaetsanalyse: die Nachweisgrenze des Li-Kriteriums skaliert wie gamma^2.
> - *benutzt* → [[55_failure_taxonomy|55 · Muster im Scheitern]] — Leitet Richtungen aus den Luecken der Blocker-Matrix ab.
> - *benutzt* → [[56_failure_autopsies|56 · Fehler-Autopsien]] — Nimmt Beobachtung 4 der Autopsien als Ausgangspunkt (leerer Euler-Quadrant).
> - ← *wird benutzt von* [[63_experiment_decision_value|63 · Entscheidungswert von Experimenten]] — Priorisiert die dort abgeleiteten Richtungen.
> - ← *wird benutzt von* [[65_criterion_sensitivity|65 · Sensitivität der Kriterien]] — Fuehrt die in U1 angekuendigte Sensitivitaetsanalyse aus.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
