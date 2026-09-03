---
id: doc-56
number: 56
title: "Fehler-Autopsien: die exakte Bruchstelle je gescheitertem Ansatz"
category: meta
status: meta
tags: [autopsy, failed-proofs, error-analysis, de-branges, atiyah, bbm, forensics]
source_file: 56_failure_autopsies.md
lang: de
---

# Fehler-Autopsien: die exakte Bruchstelle je gescheitertem Ansatz

**Kategorie:** Meta / Forensik
**Typ:** Schrittgenaue Fehleranalyse
**Status:** Auswertung bestehender Dokumente; keine neuen mathematischen Behauptungen
**Verwandt:** `docs/55` (Blocker-Taxonomie) · `docs/35` (Obstruktionen) · `docs/25`, `docs/26`, `docs/27`, `docs/20`, `docs/09`

## Zweck

„Der Beweis war fehlerhaft" ist keine Information. Nützlich wird ein
Fehlversuch erst, wenn man **die eine Zeile benennen kann, an der er bricht**,
und daraus ableitet, welche Klasse künftiger Versuche an derselben Zeile
brechen wird.

Dieses Dokument leistet das in einheitlichem Schema. Jede Autopsie hat fünf
Felder:

1. **Behauptung** — was sollte bewiesen werden
2. **Der Beweisgang bis zur Bruchstelle** — was tatsächlich funktioniert
3. **Die Bruchstelle** — der erste Schritt, der nicht trägt (so präzise wie möglich)
4. **Was wahr sein müsste** — die Aussage, die den Beweis reparieren würde
5. **Übertragbare Lehre** — welche künftigen Versuche derselbe Fehler trifft

## Drei Sorten von Misserfolg — nicht dieselbe Sache

Die Wissensbasis führt `status: refuted` als eine Kategorie. Forensisch sind
es drei grundverschiedene Zustände:

| Zustand | Bedeutung | Beispiele |
|---|---|---|
| **Widerlegt** | Es existiert ein Gegenbeispiel oder ein Beweis der Negation des Kernschritts | de Branges (Conrey–Li), Atiyah (Liouville) |
| **Nicht tragfähig** | Der Beweisgang enthält eine Lücke, die niemand schließen konnte; kein Gegenbeispiel | Bender–Brody–Müller, Berry–Keating |
| **Nicht prüfbar** | Es gibt kein Artefakt, das man widerlegen *könnte* | Nash 1959 |

Nur der erste Zustand ist endgültig. Der zweite ist offene Forschung mit
schlechter Presse. Der dritte ist gar keine mathematische Aussage. Diese
Unterscheidung wird in der Rezeption fast durchgehend eingeebnet — und sie ist
der Grund, warum `docs/58` Ansätze im Zustand „nicht tragfähig" ganz anders
bewertet als solche im Zustand „widerlegt".

---

## A1 · Louis de Branges — die vollständigste Autopsie

**Blocker:** `blk-positivity-circular`, `blk-unverifiable` · **Quelle:** `docs/20` · **Zustand:** widerlegt (in der vorgeschlagenen Form)

**Behauptung.** Die Theorie der Hilberträume ganzer Funktionen H(E) liefert
für den zur ζ-Funktion gehörigen Raum eine Positivitätsbedingung, aus der die
RH folgt.

**Der Beweisgang bis zur Bruchstelle.** Bis weit hinein korrekt und
eigenständig wertvoll: Hermite–Biehler-Funktionen E, der reproduzierende Kern
K(w,z), die Strukturtheorie geschachtelter Räume H(E_a), die Phasenfunktion φ
mit φ′ > 0. Das ist echte, akzeptierte Mathematik.

**Die Bruchstelle.** Der Schritt von der *allgemeinen* Strukturtheorie zur
*konkreten* Anwendung auf ζ. De Branges benötigt, dass eine bestimmte, dem
ζ-Raum zugeordnete Funktion positiv definit ist. **Conrey–Li (2000) zeigten,
dass sie es nicht ist** — sie nimmt negative Werte an. Damit ist die
hinreichende Bedingung in der vorgeschlagenen Form für ζ nicht erfüllbar; der
Beweis bricht nicht an einer Schlamperei, sondern an einer *falschen
Tatsachenbehauptung über ζ*.

**Was wahr sein müsste.** Eine Gewichtsfunktion W, die (a) in der größeren
Halbebene nullstellenfrei ist und (b) den ζ-Raum erzeugt. Conrey–Li zeigen:
beide Forderungen sind zusammen nicht erfüllbar in der vorgeschlagenen Form.

**Übertragbare Lehre — die wichtigste des ganzen Dokuments.**
De Branges hat den Fehler nach 2000 nicht korrigiert, sondern die Konstruktion
wiederholt umgebaut (2004, 2009, 2014, 2017). Damit wanderte der Fall vom
Zustand „widerlegt" in den Zustand „nicht prüfbar": die Community stellte die
Nachprüfung ein. **Ein widerlegter Beweis, der revidiert statt zurückgezogen
wird, verliert seinen Status als mathematisches Objekt.** Genau dieser
Mechanismus — nicht der ursprüngliche Fehler — ist es, was den Fall
aussichtslos macht.

---

## A2 · Michael Atiyah 2018 — Widerspruch zu einem Standardsatz

**Blocker:** `blk-euler-blindness`, `blk-unverifiable` · **Quelle:** `docs/25` · **Zustand:** widerlegt

**Behauptung.** Eine „Todd-Funktion" T, konstruiert als Limes von Polynomen,
erlaubt einen Widerspruchsbeweis: eine Nullstelle abseits der Geraden führt
über T auf F ≡ 0 und damit auf einen Widerspruch.

**Die Bruchstelle — mit Namen.** T soll gleichzeitig (i) auf jedem konvexen
Bereich polynomial, (ii) nicht-konstant und (iii) als Limes beschränkt sein.
Eine solche Funktion existiert nicht: **Liouville/Identitätssatz** erzwingt
Konstanz. Der Widerspruch entsteht also nicht aus der angenommenen Nullstelle,
sondern aus den Eigenschaften, die T zugeschrieben werden. Der Beweis
widerlegt seine eigene Hilfskonstruktion.

**Warum das forensisch lehrreich ist.** Der Fehler sitzt **nicht** in der
Zetafunktion. Er sitzt in einem Standardsatz der Funktionentheorie ersten
Semesters. Das ist typisch: Fehlerhafte RH-Beweise scheitern fast nie an der
Arithmetik, sondern an einem Schritt, der so elementar ist, dass ihn niemand
mehr prüft.

**Übertragbare Lehre.** Zwei Prüfregeln, die diesen Fall in Sekunden erledigt
hätten:
1. **Jedes neu eingeführte Objekt braucht einen Existenzbeweis**, bevor es
   Eigenschaften bekommt. T wurde beschrieben, nicht konstruiert.
2. **Elementare Sätze zuerst prüfen, nicht zuletzt.** Wenn ein Objekt
   „polynomial und beschränkt und nicht-konstant" sein soll, ist die Prüfung
   trivial und tödlich.

Beide Regeln sind maschinell durchsetzbar — dies ist der Fall, der am
deutlichsten für Formalisierung spricht (`docs/37`).

---

## A3 · John Nash 1959 — der Fall ohne Objekt

**Blocker:** `blk-unverifiable` · **Quelle:** `docs/26` · **Zustand:** nicht prüfbar

**Behauptung.** Angekündigt, nie ausgeführt.

**Die Bruchstelle.** Es gibt keine. Es existiert kein Manuskript, keine
Methode, kein prüfbarer Schritt — der Columbia-Vortrag war inkohärent, und
Nashs erhaltenes Werk (Einbettungssatz, Nash–Moser, Nash-Gleichgewicht) hat
keinen etablierten Bezug zur ζ-Funktion.

**Warum der Fall trotzdem in dieser Sammlung steht.** Als **Kalibrierungspunkt
für den Umgang mit Autorität**. Der Fall wird regelmäßig als „Nashs
RH-Ansatz" zitiert, obwohl es keinen gibt. Eine Wissensbasis, die Prominenz
mit Inhalt verwechselt, produziert genau solche Phantomeinträge. Die
`status`-Felder dieser Wissensbasis und die Trust-Tiers in `docs/64` sind
unter anderem dafür da, diesen Fehler strukturell auszuschließen.

**Übertragbare Lehre.** *Kein Artefakt ist kein Ansatz.* Wo kein prüfbarer
Text vorliegt, ist die korrekte Statusangabe nicht „gescheitert", sondern
„keine Aussage vorhanden".

---

## A4 · Bender–Brody–Müller 2017 — nicht widerlegt, aber nicht tragfähig

**Blocker:** `blk-noncanonical-operator` · **Quelle:** `docs/09` · **Zustand:** nicht tragfähig

**Behauptung.** Ein PT-symmetrischer Hamiltonian, dessen Eigenwerte formal
den Imaginärteilen der ζ-Nullstellen entsprechen.

**Die Bruchstelle.** Der Operator wird so konstruiert, dass seine formale
Eigenwertbedingung genau die Nullstellenbedingung reproduziert. Damit ist die
Konstruktion **zirkulär in der entscheidenden Richtung**: Selbstadjungiertheit
(bzw. die Realität des Spektrums über PT-Symmetrie) auf einem konkret
angegebenen Definitionsbereich wird nicht bewiesen — sie ist äquivalent zu
dem, was gezeigt werden soll. Hinzu kommt: zu jeder reellen Folge existiert
ein selbstadjungierter Operator mit dieser Folge als Spektrum. Die bloße
Existenz eines solchen Operators hat daher Informationsgehalt null.

**Was wahr sein müsste.** Eine unabhängig definierte Spurformel, deren
geometrische Seite die Primzahlterme der expliziten Formel liefert — also
genau das, was Selberg im bewiesenen Fall (`docs/19`) hat und was über ℤ fehlt.

**Übertragbare Lehre — der Zirkularitätstest für Spektralansätze.**
> Streiche in der Konstruktion des Operators jeden Schritt, der auf die
> Nullstellen von ζ Bezug nimmt. Ist der Operator danach noch definiert?
> Wenn nein, ist die Konstruktion zirkulär.

Dieser Test ist mechanisch anwendbar und erledigt einen Großteil der
eingereichten Hilbert–Pólya-Vorschläge.

---

## A5 · Berry–Keating xp — das Modell, das zu viel und zu wenig erklärt

**Blocker:** `blk-noncanonical-operator` · **Quelle:** `docs/08` · **Zustand:** nicht tragfähig (als Beweis), erfolgreich (als Modell)

**Die Bruchstelle.** H = xp ist klassisch elegant und reproduziert das
Zählverhalten der Nullstellen erstaunlich gut. Was fehlt, ist eine
Quantisierung: eine selbstadjungierte Realisierung auf einem konkreten
Hilbertraum mit Randbedingungen, deren Spektrum diskret ist und die richtige
Zählfunktion liefert. Der Operator xp ist auf natürlichen Definitionsbereichen
**nicht** wesentlich selbstadjungiert mit diskretem Spektrum.

**Warum dieser Fall die Kategorie „gescheitert" sprengt.** Berry–Keating ist
als *Beweisansatz* blockiert, als *Modell* aber außerordentlich erfolgreich:
es sagt Nullstellenstatistik, Formfaktoren und Momente korrekt vorher. Die
Wissensbasis sollte diese beiden Rollen nie zusammenwerfen.

**Übertragbare Lehre.** **Vorhersagekraft ist kein Beweisfortschritt.** Ein
Modell, das die richtigen Zahlen liefert, kann trotzdem null Beweislast
tragen. Das ist derselbe Punkt wie `blk-model-circularity` — nur hier von der
Modellseite aus gesehen.

---

## A6 · Die arXiv-Klasse — der Standardfehler

**Blocker:** `blk-euler-blindness`, `blk-softness`, `blk-unverifiable` · **Quelle:** `docs/27` · **Zustand:** widerlegt (als Klasse)

Diese Autopsie gilt keinem Einzelfall, sondern dem statistischen Modalfall.
Der typische eingereichte „elementare Beweis" hat folgende Struktur:

1. Er benutzt die Funktionalgleichung.
2. Er benutzt analytische Fortsetzung und Wachstumsabschätzungen.
3. Er benutzt eine Vertauschung von Limes und Nullstellensumme Σ_ρ.
4. Er benutzt **nirgends** das Euler-Produkt.

**Die Bruchstelle liegt bei Punkt 4 und ist unabhängig von den Details
erkennbar.** Ein Argument aus 1.–3. gilt wortgleich für die
Davenport–Heilbronn-Funktion, für die die RH nachweislich falsch ist. Der
Beweis ist damit widerlegt, ohne dass man ihn lesen muss.

Punkt 3 liefert den zweithäufigsten Fehler eigenständig: Σ_ρ konvergiert nur
bedingt, gepaart nach ρ ↔ 1−ρ̄. Jede Umordnung ist ein Fehler.

**Übertragbare Lehre.** Das ist der einzige Fehlermodus dieser Sammlung, der
sich **automatisieren** lässt: `kb/counterexample.py` (siehe `docs/60`) führt
genau diesen Test aus. Wer eine Beweisidee hat, sollte sie zuerst gegen die
Davenport–Heilbronn-Funktion laufen lassen und erst danach aufschreiben.

---

## Querauswertung: was alle Autopsien gemeinsam haben

**Beobachtung 1 — die Bruchstelle liegt nie in der Zahlentheorie.**
Conrey–Li: Positivität einer konkreten Funktion. Atiyah: Liouville.
Bender–Brody–Müller: Definitionsbereich eines Operators. arXiv-Klasse:
bedingte Konvergenz. In keinem einzigen Fall liegt der Fehler dort, wo das
Problem schwer ist. Die RH ist an ihrer arithmetischen Front so gut
verteidigt, dass Angriffe an der *analytischen Flanke* zusammenbrechen, lange
bevor sie die Arithmetik erreichen.

**Beobachtung 2 — der Fehler ist fast immer elementar, aber tief versteckt.**
Alle vier genannten Bruchstellen wären in einem Grundstudium prüfbar. Sie
werden übersehen, weil sie in Schritt 40 eines 60-Schritte-Arguments stehen
und niemand mehr auf Semester-1-Sätze prüft. Das ist exakt das Profil, für
das maschinelle Verifikation gebaut ist.

**Beobachtung 3 — Reputation korreliert negativ mit Prüfintensität.**
Atiyah (Fields-Medaille), de Branges (Bieberbach-Beweis), Nash (Nobel/Abel):
in allen drei Fällen wurde der Ansatz *ernster genommen als sein Inhalt* und
zugleich *weniger gründlich geprüft als nötig*. Die Community hat
korrigiert — aber langsam.

**Beobachtung 4 — was in keiner Autopsie vorkommt.** Kein einziger der
dokumentierten Fehlversuche scheitert daran, dass er das Euler-Produkt
*benutzt* und damit nicht durchkommt. Alle scheitern daran, dass sie es
**nicht** benutzen oder an einer analytischen Vorstufe hängenbleiben.
**Der Raum der Beweise, die ernsthaft am Euler-Produkt ansetzen und dann
scheitern, ist praktisch leer.** Das ist entweder ein Hinweis, dass dort noch
etwas zu holen ist, oder darauf, dass niemand so weit kommt. `docs/57` nimmt
diese Beobachtung als Ausgangspunkt.

## Prüfprotokoll aus den Autopsien

Auf jede neue Beweisidee anzuwenden, in dieser Reihenfolge:

| # | Frage | Woher |
|---|---|---|
| 1 | Existiert jedes eingeführte Objekt (Existenzbeweis, nicht Beschreibung)? | A2 |
| 2 | Gilt das Argument wortgleich für Davenport–Heilbronn? | A6, `docs/60` |
| 3 | Bleibt der Operator definiert, wenn man alle Bezüge auf ζ-Nullstellen streicht? | A4 |
| 4 | Wird eine Positivität angenommen statt bewiesen? | A1 |
| 5 | Wird Σ_ρ umgeordnet oder mit einem Limes vertauscht? | A6 |
| 6 | Sind die elementaren Sätze (Liouville, Identitätssatz, Konvergenz) an jedem Schritt geprüft? | A2 |
| 7 | Liegt ein vollständiger, öffentlicher Text vor? | A3 |

## Quellen
Alle Sachaussagen stammen aus den Einzeldokumenten und sind dort belegt:
`docs/08`, `docs/09`, `docs/20`, `docs/25`, `docs/26`, `docs/27`, `docs/35`.
Zentrale Primärbelege:
- [A note on some positivity conditions related to zeta and L-functions — Conrey & Li (arXiv math/9812166)](https://arxiv.org/abs/math/9812166)
- [Skepticism surrounds renowned mathematician's attempted proof — Science/AAAS](https://www.science.org/content/article/skepticism-surrounds-renowned-mathematician-s-attempted-proof-160-year-old-hypothesis)
- [Hamiltonian for the zeros of the Riemann zeta function — Bender, Brody, Müller (Phys. Rev. Lett. 118, 130201)](https://arxiv.org/abs/1608.03679)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (7)
> - *benutzt* → [[20_de_Branges_Hilbert_spaces|20 · Louis de Branges]] — Autopsie A1: Bruchstelle bei der Positivitaetsbedingung (Conrey-Li).
> - *benutzt* → [[25_Atiyah_2018_failed_proof|25 · Michael Atiyah]] — Autopsie A2: Bruchstelle bei Liouville/Identitaetssatz.
> - *benutzt* → [[26_Nash_failed_attempt|26 · John Nash]] — Autopsie A3: kein pruefbares Artefakt.
> - *benutzt* → [[27_other_disputed_claimed_proofs|27 · Weitere umstrittene, zurückgezogene & fehlerhafte B…]] — Autopsie A6: der Standardfehler der arXiv-Klasse.
> - *benutzt* → [[09_Bender_Brody_Muller_2017_Hamiltonian|09 · Bender–Brody–Müller]] — Autopsie A4: zirkulaere Operatorkonstruktion.
> - *benutzt* → [[08_Berry_Keating_xp_model|08 · Berry–Keating H = xp Modell]] — Autopsie A5: Modell ohne selbstadjungierte Realisierung.
> - ← *wird benutzt von* [[57_untried_directions|57 · Noch nicht Versuchtes]] — Nimmt Beobachtung 4 der Autopsien als Ausgangspunkt (leerer Euler-Quadrant).

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
