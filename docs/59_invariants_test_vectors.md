---
id: doc-59
number: 59
title: "Invarianten & Testvektoren: beweist Ihr Argument zu viel?"
category: obstruction
status: meta
tags: [invariants, test-vectors, overshoot, verification, anti-crackpot, checklist]
source_file: 59_invariants_test_vectors.md
lang: de
---

# Invarianten & Testvektoren: beweist Ihr Argument zu viel?

**Kategorie:** Meta / Prüfwerkzeug
**Datenquelle:** `kb/graph/invariants.json` · CLI: `python3 kb/invariants.py` · MCP-Tool: `invariant_checklist`
**Verwandt:** `docs/35` (Obstruktionen) · `docs/55` (Blocker) · `docs/56` (Autopsien) · `docs/60` (Orakel)

## Der Grundgedanke

Die Anti-Crackpot-Checkliste in `docs/35` prüft, ob ein Argument **etwas
Notwendiges vergisst**. Dieses Dokument prüft das Gegenteil:

> **Beweist das Argument zu viel?**

Der Unterschied ist entscheidend. Um einen Fehler der ersten Art zu finden,
muss man das Argument *lesen und verstehen*. Um einen Fehler der zweiten Art
zu finden, genügt es, **eine bekannte Unwahrheit unter den Folgerungen zu
finden** — die fehlerhafte Zeile muss man nie sehen.

Das ist die stärkste verfügbare Prüftechnik für eingereichte Beweise, und sie
ist in der RH-Literatur ungewöhnlich gut bestückt: die Umgebung der RH ist
voll von Aussagen, die *fast* wahr sind, aber nachweislich nicht — die
Mertens-Vermutung, π(x) < Li(x), Λ < 0, beschränktes S(T). Jede davon ist eine
scharfe Klinge.

## Teil 1 — Testvektoren

Konkrete Funktionen mit **bekanntem** Wahrheitswert des RH-Analogons. Ein
Argument muss jeden korrekt klassifizieren.

| Testvektor | RH-Analogon | Euler-Produkt | Rolle |
|---|---|:-:|---|
| ζ (`doc-01`) | offen, vermutet wahr | ja | das Ziel |
| **Davenport–Heilbronn** (`doc-35`) | **FALSCH (bewiesen)** | **nein** | schärfster Negativtest |
| **Epstein-Zeta, h > 1** (`doc-43`) | **FALSCH (bewiesen)** | **nein** | Negativtest, *natürlich* |
| Dirichlet-L (`doc-21`) | offen (GRH) | ja | Diagnose |
| ζ über 𝔽_q (`doc-18`) | **WAHR (bewiesen)** | ja | Blaupause |
| Selberg-Zeta (`doc-19`) | **WAHR (bewiesen)** | ja | spektrale Blaupause |

Drei Beobachtungen zu dieser Tabelle:

**1. Die Euler-Spalte trennt perfekt.** Beide Gegenbeispiele haben kein
Euler-Produkt; beide bewiesenen Analoga haben eins. Das ist die gesamte
Obstruktion `blk-euler-blindness` in einer Spalte.

**2. Epstein ist der wichtigere Negativtest.** Gegen Davenport–Heilbronn wird
regelmäßig eingewandt, sie sei „künstlich" — eine von Hand gebaute
Linearkombination. Die Epstein-Zetafunktion einer binären quadratischen Form
mit Klassenzahl > 1 ist das nicht: sie ist ein natürliches arithmetisches
Objekt (Gitter), hat eine Funktionalgleichung, kommt aus der Zahlentheorie —
und hat Nullstellen abseits der Geraden (Potter–Titchmarsh 1935). **Der
Einwand „künstlich" trägt nicht.**

**3. Die beiden bewiesenen Analoga sind Positiv-, nicht Negativtests.** Sie
prüfen nicht auf Widerlegung, sondern auf Erklärungskraft: Ist der
vorgeschlagene Mechanismus im bewiesenen Fall wiederzuerkennen? Wenn nicht,
erklärt das Argument nicht, warum es über ℤ funktionieren sollte — auch dann
nicht, wenn es keinen sichtbaren Fehler hat.

## Teil 2 — Die Überschuss-Tests

Bekannte Wahrheiten, die ein zu starkes Argument sofort widerlegen. Nach
Schärfe sortiert.

### Ⓐ Λ < 0 — die Marginlosigkeit der RH
**Bekannt:** Λ ≥ 0 (Rodgers–Tao 2018, bewiesen). Falls die RH gilt, ist
**Λ = 0 exakt**.
**Konsequenz:** Ein Argument, das Λ < 0 mitliefert, ist falsch.

Das ist der tiefste Eintrag der Liste, weil er eine *strukturelle* Aussage
über die Beweisbarkeit macht: **Die RH hat keine Marge.** Sie gilt — wenn sie
gilt — gerade eben. Jedes Argument, das Spielraum erzeugt, hat sich verrechnet.
Und da robuste, „weiche" Argumente typischerweise Spielraum erzeugen, erklärt
Λ = 0 auf einen Schlag, warum alle weichen Ansätze scheitern müssen.

### Ⓑ Argument gilt ohne Euler-Produkt
**Bekannt:** Davenport–Heilbronn und Epstein erfüllen alles außer
Multiplikativität und verletzen die RH.
**Konsequenz:** falsch. **Maschinell prüfbar** über `kb/counterexample.py`
(`docs/60`) — der einzige Eintrag der Liste, der ohne menschliches Urteil
entschieden werden kann.

### Ⓒ |M(x)| < √x
**Bekannt:** Die Mertens-Vermutung ist **widerlegt** (Odlyzko–te Riele 1985),
obwohl sie bis 10¹⁴ zu gelten schien.
**Konsequenz:** falsch. Die RH braucht nur M(x) = O(x^{1/2+ε}). Wer die
stärkere Schranke mitbeweist, hat eine bewiesenermaßen falsche Aussage
bewiesen.

### Ⓓ π(x) < Li(x) für alle x
**Bekannt:** Littlewood — unendlich viele Vorzeichenwechsel, erste Umkehr bei
~10³¹⁶.
**Konsequenz:** falsch, obwohl die Aussage für jedes je berechnete x gilt.

### Ⓔ Zirkuläre Positivität
**Bekannt:** Weil-, Li- und de-Branges-Positivität sind **äquivalent** zur RH;
Conrey–Li (2000) widerlegten de Branges' konkrete Annahme.
**Konsequenz:** zirkulär.

### Ⓕ Umordnung von Σ_ρ
**Bekannt:** Die Summe konvergiert nur bedingt, gepaart ρ ↔ 1−ρ̄.
**Konsequenz:** falsch. Zweithäufigster Fehler der arXiv-Klasse (`docs/56`, A6).

### Ⓖ Argument gilt für die ganze Selberg-Klasse
**Bekannt:** Dort wird die RH nur mit Euler-Produkt-Axiom erwartet.
**Konsequenz:** falsch, falls das Axiom nicht benutzt wird. Dies ist Ⓑ in
axiomatischer Fassung — und deckt Argumente auf, die das Euler-Produkt
*erwähnen*, aber nicht *benutzen*.

### Ⓗ Endliche Numerik als Stütze
**Bekannt:** Mertens und Skewes; und quantitativ die Sensitivitätsanalyse in
`docs/57` (das Li-Kriterium bis n = 1000 schließt Nullstellen abseits nur bis
Höhe γ ≈ 3,6 aus — nicht einmal bis zur ersten ζ-Nullstelle).
**Konsequenz:** kein Beweis.

### Ⓘ Mindestabstand zwischen Nullstellen
**Bekannt:** Lehmer-Paare — Nullstellen kommen einander beliebig nahe, es gibt
keine gleichmäßige untere Schranke für den normierten Abstand.
**Konsequenz:** falsch, falls das Argument implizit Trennung annimmt (häufig
versteckt in Vertauschungen und Kontur-Verschiebungen).

### Ⓙ S(T) beschränkt
**Bekannt:** Unter RH ist S(T) unbeschränkt (Selberg), obwohl im Mittel klein.
**Konsequenz:** falsch.

### Ⓚ Bessere nullstellenfreie Region als Vinogradov–Korobov
**Bekannt:** Seit 1958 im Wesentlichen unverbessert.
**Konsequenz:** nicht automatisch falsch — aber wer nebenbei ein 65 Jahre
offenes Problem löst, sollte das bemerken und gesondert begründen. Der einzige
Eintrag der Liste, der eine Warnung statt einer Widerlegung ist.

## Warum diese Liste ungewöhnlich stark ist

Bei den meisten offenen Problemen gibt es keine solchen Klingen: man weiß
schlicht nicht genug über die Umgebung der Vermutung. Bei der RH ist die
Umgebung außergewöhnlich gut vermessen — und zwar überwiegend durch
**Negativresultate**: eine widerlegte Vermutung (Mertens), eine bewiesene
Vorzeichenumkehr (Littlewood), eine bewiesene Unbeschränktheit (Selbergs
S(T)), eine bewiesene untere Schranke (Λ ≥ 0), zwei explizite Gegenbeispiele
(Davenport–Heilbronn, Epstein).

> **Der Ertrag von 165 Jahren RH-Forschung besteht zu einem großen Teil aus
> präzisen Aussagen darüber, was NICHT gilt. Genau das macht die
> Überschuss-Prüfung hier so scharf — und es ist der Grund, warum diese
> Wissensbasis die Negativresultate mindestens so sorgfältig führt wie die
> positiven.**

## Anwendung

```bash
python3 kb/invariants.py                 # ganze Prüfliste, nach Schärfe sortiert
python3 kb/invariants.py --testvektoren  # nur die Testvektoren
python3 kb/invariants.py --json          # maschinenlesbar
```

Im MCP-Server: `invariant_checklist`. **Reihenfolge in der Prüfung:**

1. `evaluate_proof_idea` — fehlt etwas Notwendiges? (`docs/35`)
2. `invariant_checklist` — wird zu viel bewiesen? (dieses Dokument)
3. `counterexample_oracle` — was sagt die Maschine? (`docs/60`)
4. Autopsie-Protokoll (`docs/56`) — sitzt der Fehler an einer der bekannten Stellen?

Schritt 2 ist derjenige, den man am ehesten überspringt und am wenigsten
überspringen sollte: Er ist der einzige, der ein *auf den ersten Blick
fehlerfreies* Argument widerlegen kann.

## Quellen
Alle Sachaussagen sind in den Einzeldokumenten belegt: `docs/02`, `docs/12`,
`docs/14`, `docs/16`, `docs/18`, `docs/19`, `docs/21`, `docs/23`, `docs/24`,
`docs/27`, `docs/35`, `docs/43`. Zentrale Primärbelege:
- [Rodgers & Tao, *The de Bruijn–Newman constant is non-negative* (arXiv 1801.05914)](https://arxiv.org/abs/1801.05914)
- [Odlyzko & te Riele, *Disproof of the Mertens conjecture* (J. reine angew. Math. 357, 1985)](https://www.dtc.umn.edu/~odlyzko/doc/arch/mertens.disproof.pdf)
- [On some reasons for doubting the Riemann hypothesis — A. Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- [Zeros of the Davenport–Heilbronn Counterexample (AMS Math. Comp. 76, 2007)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (5)
> - *benutzt* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Ergaenzt die Anti-Crackpot-Checkliste um die Ueberschuss-Pruefung.
> - *benutzt* → [[43_Epstein_zeta_Selberg_class_rigidity|43 · Epstein-Zetafunktionen & Selberg-Klassen-Rigidität]] — Epstein-Zeta als zweiter, natuerlicher Testvektor.
> - *benutzt* → [[23_de_Bruijn_Newman_constant_Polymath15|23 · De-Bruijn–Newman-Konstante]] — Lambda >= 0 als schaerfster Ueberschuss-Test (Marginlosigkeit).
> - *benutzt* → [[16_Mertens_function_Riesz_criterion|16 · Mertens-Funktion & Riesz-Kriterium]] — Widerlegte Mertens-Vermutung als Ueberschuss-Test.
> - ← *gestützt durch* [[60_counterexample_oracle|60 · Das Gegenbeispiel-Orakel]] — Liefert die maschinelle Haelfte der Invariantenpruefung.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
