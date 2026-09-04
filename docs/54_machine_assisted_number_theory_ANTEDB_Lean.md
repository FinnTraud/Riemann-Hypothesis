---
id: doc-54
number: 54
title: "Maschinengestützte Zahlentheorie: ANTEDB, systematische Exponenten-Optimierung und formalisierter Primzahlsatz (2025–2026)"
category: meta
status: reference
tags: [antedb, tao, trudgian, yang, exponent-pairs, zero-density, additive-energy, lean, mathlib, autoformalization, gauss, kontorovich, reproducibility, 2025, 2026]
source_file: 54_machine_assisted_number_theory_ANTEDB_Lean.md
lang: de
---

# Maschinengestützte Zahlentheorie: Datenbanken, Optimierung, Formalisierung (2025–2026)

**Kategorie:** Meta / Methodik & Verifikation
**Autoren / Jahre:** Tao–Trudgian–Yang (2025); Kontorovich–Tao & Mitwirkende (2024–2025);
Math Inc. / „Gauss" (2025); Bellotti u. a. (2024–2025)
**Typ:** Infrastruktur- und Methodenfortschritt (kein RH-Beweis)
**Status:** **[BEWIESEN]** für die einzelnen Resultate; als RH-Beitrag: methodisch, nicht inhaltlich

## Zusammenfassung
Zwischen 2024 und 2026 hat sich weniger die RH bewegt als die **Art, wie im RH-Umfeld gearbeitet
wird**. Drei Entwicklungen sind für dieses Repo direkt relevant, weil sie genau das Arbeitsmodell
beschreiben, das der MCP-Server hier erzwingt (Dok. 50): Ergebnisse als *Daten*, Beziehungen als
*Graph*, Beweise als *maschinell prüfbare* Objekte.

1. **ANTEDB** — analytische Zahlentheorie als optimierbare Datenbank statt als Aufsatzsammlung.
2. **Formalisierter starker Primzahlsatz** — Lean erreicht erstmals analytische Zahlentheorie
   auf PNT-Niveau, zuletzt agentengestützt.
3. **Reproduzierbarkeitspakete** als neue Norm bei Preprints im RH-Umfeld.

## Mathematischer Kern

### 1) ANTEDB: die Analytic Number Theory Exponent Database (arXiv:2501.16779)
Tao, Trudgian und Yang (28.01.2025) erzielen neue Schranken für gleich mehrere Klassen von
Exponenten:

- **vier neue Exponentenpaare** `(k, ℓ)` im van-der-Corput-Kalkül,
- **neue Nullstellendichte-Abschätzungen** für ζ,
- **neue Schranken für die additive Energie der Nullstellen** von ζ.

Der methodische Kern ist nicht ein einzelner Trick, sondern die Infrastruktur: Die Autoren legen
die **ANTEDB** an — eine Datenbank der bekannten Exponenten *und ihrer Implikationsbeziehungen* —
und optimieren diese Relationen dann **systematisch** (numerisch/algorithmisch) statt von Hand.

Zur Erinnerung die betroffene Größe (vgl. Dok. 49):
```
N(σ, T) = #{ ρ = β + iγ : ζ(ρ) = 0, β ≥ σ, |γ| ≤ T } ,
N(σ, T) ≪ T^{A(σ)(1−σ)} (log T)^C ,
```
und die additive Energie
```
E(T) = #{ (γ₁, γ₂, γ₃, γ₄) : |γ₁ + γ₂ − γ₃ − γ₄| ≤ 1/log T } ,
```
die Guth–Maynard (Dok. 22) als Zwischengröße benutzen. ANTEDB macht diese Landschaft
maschinenlesbar — dieselbe Idee wie der Wissensgraph in `kb/graph/`, nur für Exponenten statt
für Konzepte.

### 2) Explizite und log-freie Dichteabschätzungen (Fortschreibung von Dok. 49)
Parallel dazu die explizite Linie:
```
N(σ, T) ≤ A · T^{B(1−σ)} (log T)^C ,   log-frei: C = 0 ,
```
mit konkreten Konstanten — Bellottis explizite log-freie Abschätzung (arXiv:2405.12545,
J. Number Theory 2025) und die explizite Form von Inghams Abschätzung (arXiv:2507.15184).
Anwendung: explizite Primzahlschranken, Primzahlen in kurzen Intervallen — **unbedingt**.

### 3) Lean: der starke Primzahlsatz ist formalisiert
Das Projekt **PrimeNumberTheoremAnd** (Kontorovich, Tao, ab Januar 2024) hatte das Ziel, den PNT
*mit Fehlerterm* in Lean 4 zu formalisieren — über Wiener–Ikehara und weiter. Nach 18+ Monaten
war der Fortschritt an komplexanalytischen Kernstücken ins Stocken geraten (Zwischenstand
Juli 2025).

Im September 2025 meldete **Math, Inc.**, dass ihr Autoformalisierungs-Agent **„Gauss"** das
Projekt in **drei Wochen** abgeschlossen habe: ca. **25 000 Zeilen Lean**, über **1 000 Sätze und
Definitionen**. Ergänzend formalisieren Arbeiten aus dem PrimeNumberTheoremAnd-Umfeld das
asymptotische Verhalten der Primzahlzählfunktion mit einem stärkeren Fehlerterm als zuvor
formalisiert, inklusive Anteilen zur ζ-Funktion selbst.

**Was das für die RH bedeutet:** nichts inhaltlich — aber die **Verifikationsschwelle** ist
gestiegen. Dok. 37 argumentiert, dass Lean/mathlib das natürliche „Gateway" für jeden künftigen
RH-Beweis ist. Bis 2024 war das eine Hoffnung; jetzt ist demonstriert, dass Formalisierung
analytische Zahlentheorie auf PNT-Stärke tatsächlich trägt. Der Lean-Scaffold in `kb/lean/`
(`RH/Statement.lean`) zielt genau auf diese Schnittstelle.

### 4) Reproduzierbarkeitspakete als Norm
Im Umfeld der Weil-Form-Numerik (Dok. 52) liefern Preprints inzwischen vollständige Pakete mit:
Verifikationsskripten, Rohdaten, **Intervall-Zertifikaten** (verifizierte Fehlerschranken statt
Fließkomma-Behauptungen) und Figurengeneratoren als Ancillary Files — etwa arXiv:2607.02828,
dessen Aussagen über die ersten 512 Nullstellen auf drei unabhängigen Rechenwegen geprüft sind.
Das ist der Standard, an dem sich auch die Experimente in `kb/research/` messen lassen sollten.

## Bedeutung / Einordnung
- **Kein RH-Fortschritt im engeren Sinn.** Alles hier ist Methodik. Wer diese Punkte als
  „Fortschritt bei der RH" verkauft, verwechselt Werkzeug und Ergebnis.
- **Aber:** Genau diese Infrastruktur macht die Arbeit eines KI-Assistenten in diesem Feld
  überhaupt seriös. Statusgetrennte Claims (`kb/graph/claims.json`), typisierte Relationen
  und maschinell prüfbare Rechnungen sind die Repo-Entsprechung von ANTEDB + Lean + Zertifikaten.
- **Konkrete Anschlussaufgaben** (im Sinne von Dok. 51): ANTEDB-Exponenten in den Wissensgraph
  spiegeln; Intervall-Zertifikate statt roher `mpmath`-Ausgaben in `kb/compute.py`;
  `kb/lean/RH/Statement.lean` an die mathlib-Entwicklung der ζ-Bausteine anschließen.

## Anschlüsse in dieser Wissensbasis
- Dok. 22 (Guth–Maynard), 49 (Live-Front) — die Resultate, die ANTEDB systematisiert
- Dok. 24 (numerische Verifikation) — Rigorosität von Rechnungen (Platt-Standard)
- Dok. 28 (KI und RH), 37 (Formalisierung), 50 (Denkprotokoll) — der Methodenrahmen
- Dok. 51 (Kollaborations-Leitfaden), Dok. 52 (Weil-Form-Numerik) — wo man andocken kann
- `kb/lean/`, `kb/research/`, `kb/experiment.py` — die Repo-Gegenstücke

## Quellen
- [Tao, Trudgian, Yang — *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach* (arXiv:2501.16779)](https://arxiv.org/abs/2501.16779)
- [Tao — Blogbeitrag zum ANTEDB-Paper (28.01.2025)](https://terrytao.wordpress.com/2025/01/28/new-exponent-pairs-zero-density-estimates-and-zero-additive-energy-estimates-a-systematic-approach/)
- [Bellotti — *An explicit log-free zero density estimate for the Riemann zeta-function* (arXiv:2405.12545)](https://arxiv.org/abs/2405.12545)
- [*An explicit form of Ingham's zero density estimate* (arXiv:2507.15184)](https://arxiv.org/abs/2507.15184)
- [Math, Inc. — *Introducing Gauss, an agent for autoformalization*](https://www.math.inc/gauss)
- [Kontorovich, Tao — PrimeNumberTheoremAnd (Lean-Projekt)](https://leanprover-community.github.io/papers.html)
- [Groskin — Reproduzierbarkeitspaket zur abgeschnittenen Weil-Form (arXiv:2607.02828)](https://arxiv.org/abs/2607.02828)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (6)
> - *ist Evidenz für* → [[37_formalization_lean_proof_assistants|37 · Formalisierung]] — Der formalisierte starke Primzahlsatz zeigt, dass Lean analytische Zahlentheorie traegt.
> - *ist Evidenz für* → [[28_AI_and_RH|28 · KI / Machine Learning und die Riemann-Vermutung]] — Autoformalisierung als konkreter KI-Beitrag im RH-Umfeld.
> - *benutzt* → [[49_live_analytic_frontier|49 · Live-Front der analytischen Zahlentheorie]] — Systematisiert und verschaerft die Resultate der Live-Front.
> - *benutzt* → [[22_Guth_Maynard_2024|22 · Guth–Maynard]] — Additive Energie der Nullstellen ist die Guth-Maynard-Zwischengroesse.
> - *benutzt* → [[24_computational_verification|24 · Numerische Verifikation der Riemann-Vermutung]] — Rigorose Verifikationsstandards (Platt, Intervall-Zertifikate).
> - ← *hat Instanz* **Formale Verifikation / maschinengestuetzte Mathematik** — Dok. 54 beschreibt ANTEDB, Lean-PNT und Zertifikate.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
