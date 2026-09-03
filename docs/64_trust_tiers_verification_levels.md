---
id: doc-64
number: 64
title: "Trust-Tiers: wie gut ist jede Behauptung dieser Wissensbasis belegt?"
category: meta
status: reference
tags: [trust, verification-levels, epistemics, provenance, self-limits]
source_file: 64_trust_tiers_verification_levels.md
lang: de
---

# Trust-Tiers: wie gut ist jede Behauptung dieser Wissensbasis belegt?

**Kategorie:** Meta / Epistemik
**Datenquelle:** `kb/graph/claims.json` (Felder `trust`, `trust_note`, `zugang`) · CLI: `python3 kb/trust.py`
**Verwandt:** `docs/62` (Selbstaudit) · `docs/37`, `docs/54` (Formalisierung) · `docs/50` (Denkprotokoll)

## Das Problem mit `status: proven`

Die Wissensbasis führt 43 atomare Claims mit einem `status`-Feld
(`proven` / `open` / `refuted`). Das verhindert den schlimmsten Fehler — eine
widerlegte Aussage als wahr auszugeben. Es verschweigt aber einen zweiten:

> **`proven` sagt, dass etwas bewiesen ist. Es sagt nicht, wie gut geprüft
> dieser Beweis ist — und schon gar nicht, wie gut *diese Wissensbasis* ihn
> geprüft hat.**

Zwischen „Hardy 1914, seit 110 Jahren in jedem Lehrbuch" und „arXiv-Preprint
von 2025, Begutachtung unbekannt" liegen Welten. Beide standen bis jetzt als
`proven` da. Dieses Dokument führt die fehlende Achse ein.

## Die Stufen

| Stufe | Bedeutung | Anzahl |
|---|---|:-:|
| **T0-lean-verified** | Maschinell geprüft. Kein Halluzinationsrisiko, kein Flüchtigkeitsfehler. | 1 |
| **T1-kanonisch** | Lehrbuchbestand (Titchmarsh, Iwaniec–Kowalski, Edwards); jahrzehntelang unabhängig geprüft. | 23 |
| **T2-peer-reviewed** | In referierter Zeitschrift publiziert, aber noch nicht Lehrbuchbestand. | 6 |
| **T3-preprint** | arXiv bzw. sehr junge Arbeit; Begutachtungsstand hier nicht verifiziert. | 9 |
| **T4-repo-numerik** | In diesem Repo gerechnet, nicht extern verifiziert. | 3 |
| **T5-konsens** | Fachkonsens ohne referierte Arbeit. | 1 |

Auswertung jederzeit über `python3 kb/trust.py`.

## Die drei Stufen, die eine Erklärung brauchen

### T0 — genau ein Claim
Nur `claim-lean-pnt` (der starke Primzahlsatz, im Lean-Umfeld formalisiert)
steht auf der höchsten Stufe. **Ein Claim von 43.** Das ist die nüchternste
Zahl dieses Dokuments und zugleich die beste Begründung für `docs/37` und
`docs/54`: Formalisierung ist die einzige Technik, die diese Zahl erhöhen kann,
und sie ist heute schon verfügbar.

### T4 — was dieses Repo selbst gerechnet hat
Drei Claims stammen aus eigener Rechnung (`docs/57`, `docs/60`):
- die vier Nullstellen der Davenport–Heilbronn-Funktion abseits der Geraden,
- das Turing-Defizit (4 bei T=120, 8 bei T=200; für ζ jeweils 0),
- die γ²-Skalierung der Nachweisgrenze des Li-Kriteriums.

Diese Stufe steht **unter** T3, nicht darüber. Eigene Rechnung ist keine
Verifikation, auch wenn sie reproduzierbar ist. Was für sie spricht: bei den
DH-Nullstellen stimmen zwei unabhängige Verfahren im Repo überein
(Argumentprinzip-Defizit und Newton-Verfahren), und drei der vier Nullstellen
sind mit der Literatur verträglich. Das ist eine **Konsistenzprobe**, keine
Peer Review — und genau so ist es im `trust_note` protokolliert.

### T5 — der interessanteste Eintrag
`claim-atiyah` („Atiyahs Beweisversuch ist fehlerhaft") steht auf T5. Die
Zurückweisung ist Fachkonsens — Vortragskritik, Presse, Blogs, das
Liouville-Argument. Aber es existiert **keine referierte Widerlegungsarbeit**.

Das ist keine Spitzfindigkeit gegenüber dem Konsens: die Ablehnung ist
begründet und mit hoher Wahrscheinlichkeit richtig. Es ist eine Aussage über
die **Belegkette**. Ein System, das solche Fälle nicht kennzeichnet, behandelt
mathematische Beweise und soziale Übereinkünfte gleich — und genau diesen
Fehler soll die Wissensbasis nicht machen.

## Die wichtigste Einschränkung: `zugang: sekundaer`

Zusätzlich zur Stufe trägt jeder Claim ein Feld `zugang`. Der Befund ist
unbequem und steht deshalb hier deutlich:

> **40 von 43 Claims tragen `zugang: sekundaer`. Für diese Wissensbasis wurde
> die Primärquelle nicht gelesen.** Die Inhalte stammen aus
> Übersichtsdarstellungen, Zusammenfassungen und Enzyklopädieartikeln. Die
> Quellenlinks am Ende jedes Dokuments belegen, *wo etwas nachzulesen wäre* —
> nicht, dass es dort nachgelesen wurde.

Für T1-Aussagen ist das unkritisch: Hardys Satz wird in Sekundärliteratur nicht
falsch wiedergegeben. Für die neun T3-Claims aus `docs/52`–`docs/54` ist es
die entscheidende Einschränkung — dort geht es um Arbeiten aus 2025/2026, deren
genaue Aussagen, Voraussetzungen und Begutachtungsstand hier **nicht** geprüft
werden konnten.

**Praktische Konsequenz:** Wer aus dieser Wissensbasis zitiert, zitiert die
Primärquelle — nach eigener Lektüre. Die Wissensbasis ist eine Landkarte, keine
Quelle.

## Sieben Warnungen, die `kb/trust.py` von selbst ausgibt

Sieben Claims stehen als `proven` bei Quellenstufe T3 — alle aus `docs/52`
(Connes-Programm), `docs/53` (Paarkorrelation ohne RH) und `docs/54`
(ANTEDB/Lean). Das ist kein Fehler der Erfassung, sondern eine korrekte
Beschreibung der Lage: **das sind die aktuellsten und deshalb am wenigsten
abgesicherten Teile der Wissensbasis.** Genau sie sind aber auch die
interessantesten (`docs/58` platziert `doc-52` an der Spitze des
Near-Miss-Rankings).

Das ist kein Widerspruch, sondern der Normalzustand an einer Forschungsfront —
er muss nur sichtbar sein. Deshalb gibt `kb/trust.py` die Warnung automatisch
aus, statt sie in einer Fußnote zu vergraben.

## Wie die Stufe die Verwendung ändert

| Stufe | Verwendbar für | Nicht verwendbar für |
|---|---|---|
| T0 | alles | — |
| T1 | Argumentation, Zitat, Ableitung | — |
| T2 | Argumentation, Zitat | Ableitungen ohne Blick in die Arbeit |
| T3 | Orientierung, Hypothesenbildung | Argumentation ohne Primärlektüre |
| T4 | Illustration, Kalibrierung, Plausibilität | jede Beweisführung |
| T5 | Einordnung | Zitat als bewiesene Aussage |

Für einen KI-Assistenten auf dieser Wissensbasis heißt das konkret: Die
Statuskennzeichnung aus `docs/50` (`[BEWIESEN] / [OFFEN] / [EVIDENZ] /
[HEURISTIK]`) sollte um die Stufe ergänzt werden, sobald ein Claim T3 oder
schlechter ist — also `[BEWIESEN, T3-preprint]` statt nur `[BEWIESEN]`.

## Pflege

- **Neuer Claim:** `trust`, `trust_note` und `zugang` sind Pflichtfelder.
- **Preprint erscheint referiert:** T3 → T2, `trust_note` aktualisieren.
- **Primärquelle wird tatsächlich gelesen:** `zugang` auf `primaer` setzen —
  und zwar nur dann.
- **Verboten:** eine Stufe anheben, weil eine Aussage plausibel wirkt. Die
  Stufe beschreibt die Belegkette, nicht die Überzeugung.

## Quellen
Dieses Dokument macht keine mathematischen Aussagen. Die Einstufungen selbst
stehen mit Begründung in `kb/graph/claims.json`; die Verteilung ist über
`python3 kb/trust.py` jederzeit reproduzierbar.

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (3)
> - *benutzt* → [[37_formalization_lean_proof_assistants|37 · Formalisierung]] — Formalisierung ist die einzige Technik, die T0 erreichbar macht.
> - *benutzt* → [[50_reasoning_protocol|50 · Denkprotokoll]] — Ergaenzt die Statustrennung des Denkprotokolls um die Verifikationsstufe.
> - ← *wird benutzt von* [[62_ai_division_of_labour_self_audit|62 · KI-Arbeitsteilung & Selbstaudit dieser Wissensbasis]] — Befund 1 beruht auf der Trust-Tier-Auswertung.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
