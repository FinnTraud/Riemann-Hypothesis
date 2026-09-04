---
id: doc-61
number: 61
title: "Negativraum: was gilt, wenn die RH falsch ist?"
category: meta
status: open
tags: [negative-space, counterfactual, falsity, lambda, robustness]
source_file: 61_negative_space_if_rh_is_false.md
lang: de
---

# Negativraum: was gilt, wenn die RH falsch ist?

**Kategorie:** Meta / Kontrafaktik
**Status:** Analytische Auswertung bestehender Resultate
**Verwandt:** `docs/35` (Ivićs Zweifelsgründe) · `docs/23` (Λ) · `docs/36` (Konsequenzen der RH) · `docs/59` (Invarianten)

## Warum diese Frage keine Spielerei ist

`docs/36` sammelt, was aus der RH **folgt**. Dieses Dokument fragt die
Gegenrichtung — und zwar aus drei praktischen Gründen:

1. **Robustheitsprüfung der Wissensbasis.** Welche Dokumente wären am Tag nach
   einem Gegenbeispiel wertlos, welche unverändert gültig? Ein Vault, der zu
   80 % aus Aussagen besteht, die nur unter RH gelten, ist fragil.
2. **Kalibrierung der eigenen Überzeugung.** Wer nicht sagen kann, wie die Welt
   aussähe, wenn die RH falsch ist, glaubt sie nicht, sondern setzt sie voraus.
3. **Diagnostik für Beweisversuche.** Ein Argument, das zeigt, warum die RH
   gelten *muss*, sollte erklären können, warum die bekannten „Beinahe-Verletzungen"
   (Λ = 0, Lehmer-Paare, unbeschränktes S(T)) so knapp ausfallen.

## Was ¬RH konkret bedeutet — eine einzige Zahl

Die schärfste Fassung folgt aus `docs/23`. Es gilt:

```
RH  ⟺  Λ ≤ 0          (de Bruijn, Newman)
Λ ≥ 0                  (Rodgers–Tao 2018, BEWIESEN)
Λ ≤ 0,22               (Polymath15 2019)
```

Daraus:

> **¬RH ist äquivalent zu Λ > 0. Und wegen der bewiesenen Schranken liegt Λ
> dann in einem Intervall der Länge 0,22.** Die gesamte Frage „gilt die
> Riemann-Vermutung?" ist die Frage, ob eine reelle Zahl, von der bewiesen ist,
> dass sie in [0; 0,22] liegt, gleich 0 ist oder nicht.

Das ist die präziseste Formulierung des offenen Problems, die die Wissensbasis
enthält — und sie hat eine unbequeme Konsequenz: **Λ ≥ 0 heißt, dass die RH,
falls wahr, keine Marge hat.** Sie ist der Randfall. Ein Gegenbeispiel wäre
kein grober Verstoß, sondern ein hauchdünner.

## Was zusammenbricht

| Betroffen | Was genau |
|---|---|
| `docs/02` | von Kochs Fehlerterm π(x) = Li(x) + O(√x log x) — die RH ist genau diese Schranke |
| `docs/13`, `docs/14`, `docs/15`, `docs/16`, `docs/45` | **alle** äquivalenten Kriterien werden zu falschen Aussagen: λ_n wird negativ, Robins Ungleichung versagt für ein n > 5040, d_N konvergiert nicht gegen 0, M(x) sprengt x^{1/2+ε} |
| `docs/36` | jede Konsequenz, die „unter RH" bewiesen wurde — u. a. deterministisches Miller–Rabin in polynomieller Zeit, explizite Klassenzahlschranken |
| `docs/23` | Λ > 0, das Programm bleibt aber sinnvoll: es würde Λ eingrenzen statt auf 0 drücken |
| `docs/05`–`docs/11` | ein selbstadjungierter Hilbert–Pólya-Operator kann nicht existieren — das gesamte Programm wäre widerlegt, nicht nur blockiert |

Bemerkenswert an dieser Liste: **fast alles, was zusammenbricht, sind
Äquivalenzen und Folgerungen — keine Methoden.** Die Werkzeuge überleben, die
Schlüsse nicht.

## Was unverändert gilt

| Unberührt | Warum |
|---|---|
| `docs/12`, Primzahlsatz | unbedingt bewiesen; ζ(1+it) ≠ 0 hängt nicht an der RH |
| `docs/18`, `docs/19` | RH über 𝔽_q und für Selberg-Zeta sind **bewiesene Sätze über andere Objekte**. Ein Gegenbeispiel für ζ berührt sie nicht — es würde nur zeigen, dass die Analogie nicht trägt |
| `docs/22` Guth–Maynard, `docs/32` Zhang, `docs/49` | unbedingte Resultate |
| `docs/03`, `docs/04` | Hardy und die Anteilsresultate bleiben wahr: unendlich viele und >41 % der Nullstellen liegen auf der Geraden — auch wenn nicht alle |
| `docs/29` GORZ (Teilresultate) | die Hyperbolizität für d ≤ 8 ist unbedingt |
| `docs/46` Voronin | unbedingt |
| `docs/24` | die Verifikation bis γ ≈ 3·10¹² bliebe korrekt — das Gegenbeispiel läge darüber |
| `docs/35`, `docs/55`, `docs/56`, `docs/59`, `docs/60` | die **gesamte Obstruktionsschicht** bliebe gültig und würde an Bedeutung gewinnen |

**Das ist der eigentliche Befund dieses Dokuments.** Der robuste Teil der
Wissensbasis ist genau der, der von Negativresultaten, Gegenbeispielen und
Methodengrenzen handelt. Der fragile Teil sind die Äquivalenzen. Das spiegelt
exakt die Bewertung in `docs/58`: Äquivalenzen tragen wenig — hier tragen sie
gar nichts.

## Wer hätte recht gehabt?

**Bestätigt worden wären:**
- **Ivić** (`docs/35`) mit den Zweifelsgründen — insbesondere dem Hinweis, dass
  S(T) unbeschränkt ist und sehr hohe Nullstellen unerwartetes Verhalten zeigen
  könnten.
- Die **Lehmer-Paar-Beobachtung** (`docs/23`): dass die RH nur knapp gilt, wäre
  im Rückblick das entscheidende Warnsignal gewesen.
- Die **Davenport–Heilbronn/Epstein-Linie** (`docs/35`, `docs/43`): dass
  ζ-artige Funktionen die RH systematisch verletzen können, wäre kein
  Sonderfall der Euler-Produkt-losen Welt mehr gewesen, sondern der Normalfall.
- Die **Alternative Hypothese** (`docs/53`) — ein Szenario, in dem die
  Nullstellenstatistik anders aussieht als das GUE-Bild erwarten lässt.

**Widerlegt worden wären:** das gesamte Hilbert–Pólya-Programm, jede
Positivitätsstrategie, und — am folgenreichsten — die Erwartung, dass die
𝔽_q-Blaupause (`docs/18`) über ℤ überhaupt trägt.

## Wo könnte ein Gegenbeispiel liegen?

Aus den bekannten Schranken lässt sich der Suchraum eingrenzen:

- **Höhe:** oberhalb γ ≈ 3 · 10¹² (`docs/24`, Platt rigoros).
- **Abstand von der Geraden:** winzig. Λ ≤ 0,22 und die nullstellenfreien
  Regionen (`docs/12`) drücken jede Ausnahme dicht an Re(s) = 1/2.
- **Dichte:** höchstens eine Menge der Dichte 0 — sonst widerspräche es den
  Anteilsresultaten (`docs/04`) und den Nullstellendichte-Schranken (`docs/22`).

Zusammen: **ein Gegenbeispiel wäre eine extrem hoch gelegene, extrem knapp
neben der Geraden liegende, extrem dünn gesäte Ausnahme.** Genau die Sorte
Objekt, die numerisch prinzipiell unauffindbar ist — und die ein Beweis
ausschließen müsste, ohne sie je zu sehen.

Das erklärt beiläufig, warum `docs/57` U1 so ausfällt, wie es ausfällt: ein
Kriterium mit γ²-Sensitivität hätte gegen ein Gegenbeispiel bei γ ~ 10¹²
schlicht keine Chance.

## Die ehrliche Gesamteinschätzung

Die Fachwelt hält die RH überwiegend für wahr. Die Gründe sind gut
(Verifikation bis 3·10¹², GUE-Übereinstimmung, bewiesene Analoga, >41 % auf der
Geraden). Sie sind aber **allesamt von der Sorte, die bei der
Mertens-Vermutung ebenfalls überzeugend aussah** — und die Mertens-Vermutung
ist falsch.

> Die redliche Position ist nicht „die RH ist wahr", sondern: **„die RH ist
> wahrscheinlich wahr, und alle unsere Gründe dafür sind genau der Typ Grund,
> der in diesem Gebiet schon einmal getäuscht hat."**

Genau deshalb ist die Obstruktionsschicht dieser Wissensbasis wichtiger als
ihre Evidenzschicht — und deshalb steht dieses Dokument hier.

## Quellen
Alle Sachaussagen stammen aus den zitierten Einzeldokumenten und sind dort
belegt. Zentrale Primärbelege:
- [Rodgers & Tao, *The de Bruijn–Newman constant is non-negative* (arXiv 1801.05914)](https://arxiv.org/abs/1801.05914)
- [On some reasons for doubting the Riemann hypothesis — A. Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- [Odlyzko & te Riele, *Disproof of the Mertens conjecture*](https://www.dtc.umn.edu/~odlyzko/doc/arch/mertens.disproof.pdf)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (2)
> - *benutzt* → [[36_consequences_of_RH|36 · Konsequenzen der Riemann-Vermutung]] — Kontrafaktik zu den Konsequenzen der RH.
> - *benutzt* → [[23_de_Bruijn_Newman_constant_Polymath15|23 · De-Bruijn–Newman-Konstante]] — Nicht-RH ist aequivalent zu Lambda > 0.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
