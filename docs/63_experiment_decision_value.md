---
id: doc-63
number: 63
title: "Entscheidungswert von Experimenten: welches Ergebnis tötet welchen Cluster?"
category: meta
status: meta
tags: [experiment-design, information-gain, decision-value, prioritization]
source_file: 63_experiment_decision_value.md
lang: de
---

# Entscheidungswert von Experimenten: welches Ergebnis tötet welchen Cluster?

**Kategorie:** Meta / Forschungsökonomie
**Verwandt:** `docs/55` (Blocker-Matrix) · `docs/57` (offene Richtungen) · `docs/58` (Near-Miss) · `docs/60` (Orakel) · `kb/experiment.py`

## Das Auswahlkriterium

Das Experiment-Logbuch (`kb/experiment.py`) macht Experimente reproduzierbar.
Es sagt nicht, **welches** man laufen lassen sollte. Dafür braucht es ein
Kriterium, und es ist nicht „wie interessant ist die Frage", sondern:

> **Wie viele Ansätze würde das Ergebnis neu einordnen — und zwar bei *jedem*
> möglichen Ausgang?**

Daraus folgt sofort die härteste Regel dieses Dokuments:

> **Ein Experiment, dessen Ergebnis man vorhersagen kann, hat
> Informationswert null.** Egal wie aufwendig es ist.

Das trifft den Großteil numerischer RH-Arbeit. „Wir haben λ_n bis n = 1000
berechnet und alle waren positiv" — das Ergebnis stand vorher fest, und
`docs/57` U1 zeigt quantitativ, dass es selbst dann nichts ausschließt, wenn
man es glaubt (Reichweite γ ≈ 3,6, unterhalb der ersten ζ-Nullstelle).

## Bewertungsraster

| Achse | Frage |
|---|---|
| **Vorhersagbarkeit** | Kenne ich das Ergebnis schon? Wenn ja → Wert 0, unabhängig vom Rest |
| **Beidseitigkeit** | Sind *beide* Ausgänge informativ, oder nur einer? |
| **Reichweite** | Wie viele Blocker/Ansätze (`docs/55`) würde das Ergebnis umsortieren? |
| **Kosten** | Rechenzeit, Implementierungsaufwand, benötigtes Vorwissen |

## Die Rangliste

### ① Abgeschnittene Weil-Form gegen Davenport–Heilbronn
*(`docs/57` U2 · Kosten: hoch · Reichweite: `blk-limit-interchange`, `blk-euler-blindness`, `doc-52`)*

| Ausgang | Was er bedeutet |
|---|---|
| **Positivität scheitert bei endlichem Λ** | Die endliche Konstruktion enthält bereits die arithmetische Information, die DH von ζ trennt. Man kann angeben, *welcher* Term das leistet — der Euler-Eintrittspunkt wäre lokalisiert. |
| **Positivität hält für DH bei jedem erreichbaren Λ** | Die endliche Konstruktion ist Euler-blind; die **gesamte** arithmetische Last liegt im Grenzübergang. Das erklärt, warum genau dieser Schritt so hart ist. |
| **Konstruktion für DH gar nicht definierbar** | Die Trennung ist bereits in die Definition eingebaut — dann sollte gesagt werden, wo. |

**Alle drei Ausgänge sind informativ, und keiner ist vorhersagbar.** Das ist
das Optimum. Es ist zugleich das einzige Experiment der Liste, das den
höchstplatzierten Ansatz des Near-Miss-Rankings (`docs/58`) direkt betrifft.

### ② Negativkontrollen für d_N, Robin und Λ
*(`docs/57` U1 · Kosten: klein–mittel · Reichweite: `blk-finite-evidence`, `blk-equivalence-trap`, fünf Dokumente)*

Für das Li-Kriterium ist die Analyse gerechnet: Sensitivität ~ γ².
Offen sind dieselbe Analyse für d_N (Báez-Duarte), Robin und die
Λ-Schranken.

- **Ausgang A — ähnlich schlechte Skalierung.** Dann gilt der Befund aus U1
  für die ganze Kriterienfamilie: **numerische Kriterienprüfung ist als
  RH-Evidenz systematisch wertlos.** Das würde die Evidenzbewertung in
  mindestens fünf Dokumenten korrigieren.
- **Ausgang B — ein Kriterium skaliert deutlich besser.** Dann hat man ein
  numerisch überlegenes Kriterium identifiziert, und das ist unmittelbar
  praktisch nutzbar.

Beidseitig informativ, niedrige Kosten, breite Reichweite. **Bestes
Aufwand-Nutzen-Verhältnis der Liste.**

### ③ Epstein-Zeta als zweiter Testvektor
*(`docs/59`, `docs/60` · Kosten: mittel · Reichweite: `blk-euler-blindness`, Einwandsresistenz)*

Nicht neue Mathematik, sondern die Beseitigung eines wiederkehrenden Einwands:
Davenport–Heilbronn sei „künstlich". Die Epstein-Zeta einer quadratischen Form
mit Klassenzahl > 1 ist ein natürliches arithmetisches Objekt und verletzt die
RH trotzdem. Ergebnis vorhersagbar (**Wert nach eigener Regel: niedrig**) —
der Nutzen liegt nicht im Erkenntnisgewinn, sondern in der Belastbarkeit des
Orakels gegenüber Kritik. Ehrlich als das ausweisen, was es ist:
Werkzeugbau, nicht Experiment.

### ④ Spektralstatistik des endlichen Modells vs. Alternative Hypothese
*(`docs/57` U3 · Kosten: mittel, nach ① · Reichweite: `blk-model-circularity`, `doc-52`, `doc-53`)*

Beim endlichen Modell ist die Nullstellenlage ein Satz, kein Postulat — die
Statistik ist also **unbedingt** berechenbar und umgeht die Zirkularität, die
GUE-Vergleiche bei ζ belastet. Übereinstimmung mit ζ wäre ein Treuenachweis
des Modells; Abweichung sagt, welche Struktur die Abschneidung zerstört.
Beidseitig informativ, aber abhängig von ①.

### ⑤ Formalisierung der Obstruktionen
*(`docs/57` U6 · Kosten: hoch, aber planbar · Reichweite: `blk-unverifiable`)*

Kein Experiment im engeren Sinn — es gibt keinen unbekannten Ausgang. Steht
hier, weil es die **einzige** Position der Liste ohne Forschungsrisiko ist:
Sie erfordert nur Arbeit und adressiert den einzigen Blocker mit heute
erreichbarer Fluchtbedingung (`docs/55`, Beobachtung 6).

### ⑥ Höher rechnen — mehr Nullstellen verifizieren
*(Kosten: sehr hoch · Reichweite: **null**)*

Steht hier, um explizit **abgeraten** zu werden. Ergebnis vollständig
vorhersagbar; `blk-finite-evidence` erklärt, warum es auch bei Erfolg nichts
belegt; `docs/61` zeigt, dass ein Gegenbeispiel oberhalb γ ≈ 3·10¹² liegen
müsste und dort numerisch prinzipiell unauffindbar ist. **Wert 0 bei
höchsten Kosten** — die schlechteste Kombination im Feld, und zugleich die
verbreitetste Form numerischer RH-Arbeit.

## Zusammenfassung

| Rang | Experiment | Beidseitig? | Vorhersagbar? | Kosten | Reichweite |
|---|---|:-:|:-:|---|---|
| ① | Weil-Truncation vs. DH | ✅ | nein | hoch | breit |
| ② | Negativkontrollen d_N/Robin/Λ | ✅ | nein | **klein** | breit |
| ③ | Epstein als Testvektor | ❌ | **ja** | mittel | eng (Werkzeugbau) |
| ④ | Spektralstatistik endliches Modell | ✅ | nein | mittel | mittel |
| ⑤ | Obstruktionen formalisieren | — | ja | hoch | eng, aber sicher |
| ⑥ | Höher rechnen | ❌ | **ja** | sehr hoch | **null** |

**Empfehlung:** ② zuerst — kleinste Kosten, breiteste Wirkung, beide Ausgänge
informativ. Dann ①.

## Bezug zu docs/58

`docs/58` zeigt, dass Near-Miss-Score und Erfolgsaussicht antikorreliert sind:
Was messbar ist, ist ausgereizt; was folgenreich wäre, erzeugt keine Messwerte.
Dieses Dokument ist die praktische Kehrseite davon.

> Ein Experiment kann nur dort ansetzen, wo etwas messbar ist. Deshalb kann
> **kein** Experiment die drei Score-0-Lücken (Weil-Positivität, kanonischer
> Operator, Geometrie über Spec(ℤ)) direkt angreifen.

Was Experimente leisten können, ist **Wegräumen**: Sie zeigen, welche der
messbaren Ansätze ausscheiden, und schärfen dadurch die Frage, die dann mit
anderen Mitteln beantwortet werden muss. Experiment ① ist genau deshalb das
wertvollste — es würde sagen, ob die Arbeit am aussichtsreichsten Programm an
der endlichen Konstruktion oder am Grenzübergang zu leisten ist.

## Quellen
Dieses Dokument enthält keine mathematischen Behauptungen. Die
Sensitivitätsergebnisse, auf die es sich stützt, sind in `docs/57` und
`docs/60` dokumentiert und über `kb/counterexample.py` reproduzierbar.

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (3)
> - *benutzt* → [[55_failure_taxonomy|55 · Muster im Scheitern]] — Bemisst Experimente an der Reichweite in der Blocker-Matrix.
> - *benutzt* → [[57_untried_directions|57 · Noch nicht Versuchtes]] — Priorisiert die dort abgeleiteten Richtungen.
> - *benutzt* → [[58_gap_registry_near_miss|58 · GAP-Registry & Near-Miss-Bewertung]] — Kehrseite des Near-Miss-Befunds: messbar heisst ausgereizt.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
