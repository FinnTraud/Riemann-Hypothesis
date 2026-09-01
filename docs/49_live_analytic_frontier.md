---
id: doc-49
number: 49
title: "Live-Front der analytischen Zahlentheorie (2019–2026)"
category: frontier
status: open
tags: [zero-density, tao-program, nelson-subconvexity, harper-moments, 2024, active]
source_file: 49_live_analytic_frontier.md
lang: de
---

# Live-Front der analytischen Zahlentheorie (2019–2026)

**Kategorie:** Aktuelle Forschungsfront (unbedingte Fortschritte)
**Autoren / Jahre:** Guth–Maynard (2024); Tao (zero-density program, 2024); Nelson (Subkonvexität, 2021); Harper, Radziwiłł–Soundararajan (Momente, 2018–2022)
**Typ:** Aktive, inkrementelle Fortschritte (kein RH-Beweis)
**Status:** Laufend; unbedingte Resultate im RH-Umfeld

## Zusammenfassung
Dokumentiert die *lebendige* Front, an der tatsächlich unbedingte Fortschritte erzielt werden — jenseits des Guth–Maynard-Durchbruchs (Dok. 22). Für einen RH-Assistenten ist dies der „Newsfeed": wo sich messbar etwas bewegt.

## Mathematischer Kern (Resultate, Formeln)

### Explizite & log-freie Nullstellendichte-Abschätzungen (2023–2025)
Eine Welle expliziter Verschärfungen der Ingham/Inghamschen Form:
```
N(σ, T) ≤ A · T^{B(1−σ)} (log T)^C   (log-frei: C = 0),
```
mit konkreten Konstanten A, B (z. B. arXiv 2405.12545, 2507.15184, 2311.05136). Anwendung: explizite Primzahlschranken, Primzahlen in kurzen Intervallen — alles **unbedingt**.

### Taos „outsourced" Zero-Density-Programm (2024)
Tao systematisierte die Reduktion von Nullstellendichte-Schranken auf **Großwert-Abschätzungen von Dirichlet-Polynomen** und lagerte Teile an Computeralgebra / verteilte Verifikation aus. Verbindet Guth–Maynard-Decoupling (Dok. 22) mit einem reproduzierbaren Schätz-Framework.

### Nelson: GL(n)-Subkonvexität (2021)
Paul Nelson bewies allgemeine **subkonvexe Schranken** für GL(n)-L-Funktionen (mit Venkatesh' Methoden / Orbit-Integralen):
```
L(1/2, π) ≪ C(π)^{1/4 − δ}   (δ > 0),
```
wo C(π) der analytische Leiter ist. Subkonvexität ist die unbedingte Annäherung an die Lindelöf-Hypothese (Dok. 17) in hoher Allgemeinheit.

### Harper & scharfe Momentschranken (2018–2022)
- **Harper (2019):** „better than squareroot cancellation" für zufällige multiplikative Funktionen; präzises Verständnis kleiner Momente (k < 1).
- **Radziwiłł–Soundararajan / Heap–Radziwiłł–Soundararajan:** scharfe (bedingte und teils unbedingte) obere/untere Schranken
```
M_k(T) = (1/T)∫_0^T |ζ(1/2+it)|^{2k} dt  ≍  T (log T)^{k²},
```
in Übereinstimmung mit Keating–Snaith (Dok. 07). Stützt das Random-Matrix-Bild quantitativ.

### Transfer Subkonvexität ↔ Momente (2022)
Funktionalanalytische Implikationen zwischen Subkonvexitätsschranken und Momenten im rechten Teil des kritischen Streifens (arXiv 2212.04421) — verbindet Dok. 07 und Dok. 17.

## Bedeutung / Einordnung
- Hier passiert der **reale, überprüfbare Fortschritt** — meist unbedingt und damit dauerhaft.
- Keiner dieser Schritte beweist die RH; zusammen verengen sie aber die „Lücke" (Dichte, Subkonvexität, Momente) und liefern unbedingte zahlentheoretische Anwendungen.
- Ideal als regelmäßig zu aktualisierender Teil des MCP-Servers (arXiv-Feeds zu „zero-density estimate", „subconvexity", „moments of zeta").

## Quellen
- [Terence Tao — zero-density program (Blog, 2024)](https://terrytao.wordpress.com/2024/07/07/)
- [An explicit log-free zero density estimate for the Riemann zeta-function (arXiv 2405.12545)](https://arxiv.org/pdf/2405.12545)
- [Implications between subconvexity and moments (arXiv 2212.04421)](https://arxiv.org/pdf/2212.04421)
- [P. Nelson — Bounds for standard L-functions (subconvexity for GL(n), arXiv 2109.15230)](https://arxiv.org/abs/2109.15230)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *ist Evidenz für* (`evidence_for`) → [[22_Guth_Maynard_2024|22 — Guth–Maynard (2024): Durchbruch bei Nullstellendichte-Abschätzungen]] — Live-Front: explizite Dichte, Subkonvexität, Momente.
- *ist Evidenz für* (`evidence_for`) → [[17_Lindelof_density_hypothesis|17 — Lindelöf-Hypothese & Dichte-Hypothese]] — Subkonvexität nähert Lindelöf an.
- *ist Evidenz für* (`evidence_for`) → [[07_Keating_Snaith_moments|07 — Keating–Snaith: Momente der Zetafunktion via charakteristische Polynome (CUE)]] — Harper/Radziwiłł–Soundararajan: scharfe Momentschranken stützen Keating-Snaith.

**Eingehende Beziehungen**
- *benutzt* (`uses`) → [[54_machine_assisted_number_theory_ANTEDB_Lean|54 — Maschinengestützte Zahlentheorie: ANTEDB, systematische Exponenten-Optimierung und formalisierter Primzahlsatz (2025–2026)]] — Systematisiert und verschaerft die Resultate der Live-Front.

**Thematisch benachbart (gemeinsame Tags):** [[22_Guth_Maynard_2024|Guth–Maynard (2024): Durchbruch bei Nullstellendichte-Abschätzungen]] · [[54_machine_assisted_number_theory_ANTEDB_Lean|Maschinengestützte Zahlentheorie: ANTEDB, systematische Exponenten-Optimierung und formalisierter Primzahlsatz (2025–2026)]] · [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)]] · [[52_Connes_truncated_Weil_spectral_realization|Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
