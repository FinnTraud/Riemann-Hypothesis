---
id: doc-51
number: 51
title: "Kollaborations-Leitfaden: sinnvoll mit einer Fachperson an der RH arbeiten"
category: meta
status: meta
tags: [collaboration, open-problems, research-program, professor, experiments, formalization]
source_file: 51_collaboration_brief.md
lang: de
---

# Kollaborations-Leitfaden: sinnvoll mit einer Fachperson/Professor an der RH arbeiten

**Kategorie:** Meta / Forschungsorganisation
**Zweck:** Konkrete, realistische Teilprojekte, die mit den Tools dieses Repos einen *echten,
prüfbaren* Beitrag liefern — ohne den unrealistischen Anspruch eines vollständigen RH-Beweises.

## Grundhaltung (ehrlich)
Ein vollständiger RH-Beweis ist nicht das realistische Ziel einer Studien-/Seminararbeit oder
eines KI-Tools (siehe docs/35, 41, 46). **Wertvoll und erreichbar** sind: reproduzierbare
numerische Experimente, formale Verifikation von Teilresultaten, und die rechnerische
Ausreizung *zur RH äquivalenter* Kriterien. Genau dafür sind die Tools gebaut.

## Drei realistische Projektklassen

### Klasse A — Numerisch-experimentelle Mathematik (sofort machbar)
Werkzeuge: `compute_*`, `plot_*`, `research/spacing_vs_gue.py`, Experiment-Logbuch.
Beispiele:
1. **Montgomery–Odlyzko-Gesetz** quantifizieren (docs/06): Abstandsstatistik vs. GUE — bereits
   als Flaggschiff-Experiment vorhanden (`kb/research/spacing_vs_gue.py`). Erweiterbar auf
   höhere Korrelationen, größere Höhen, andere L-Funktionen.
2. **Li-Koeffizienten** (docs/14): λ_n-Positivität + Wachstum λ_n ~ ½ n log n testen; Abweichungen
   analysieren. Frage: ab welchem n bricht die Näherung (Nullstellenzahl) zusammen?
3. **Explizite Formel** (docs/02): Konvergenz von ψ(x) gegen die echte Primzahlsummation als
   Funktion der Nullstellenzahl — Fehlerterm-Skalierung empirisch bestimmen.
4. **S(T)-Statistik** (docs/02): Verteilung des Argumentterms S(T) bei wachsendem T (Selberg-CLT:
   S(T)/√(½ log log T) → Normalverteilung) numerisch prüfen.

### Klasse B — Formale Verifikation in Lean (mit Professor, hoher Wert)
Werkzeuge: `kb/lean/`, `formal_statement`, `lean_check` (docs/37).
Beispiele:
1. Ein **zur RH äquivalentes Kriterium** formal aufschreiben (Λ≤0 docs/23; Li-Positivität docs/14;
   Robin docs/15) und die Äquivalenz zur Standardaussage beweisen.
2. **Bewiesene Teilresultate** formalisieren: Hardy (∞ viele Nullstellen, docs/03), Rodgers–Tao
   Λ≥0 (docs/23). Jeder lückenlos geprüfte Beweis ist publizierbarer Fortschritt.
3. Schon die **Definitionen** sauber in mathlib-Stil (ξ-Funktion, N(T), Li-Koeffizienten) sind
   ein Beitrag, auf dem andere aufbauen.

### Klasse C — Ein äquivalentes Kriterium rechnerisch ausreizen
Beispiele:
1. **Báez-Duarte-Distanz** d_N (docs/13/45): numerisch berechnen und die vermutete Rate
   d_N² ~ (2+γ−log 4π)/log N prüfen — sehr „greifbares" Ziel mit konkreter Konstante.
2. **Weil-Positivität endlichdimensional** (docs/14): die quadratische Form auf einem
   endlichen Funktionenraum aufstellen und ihre kleinste Eigenwert-Schranke verfolgen.
3. **Lapidus-Spektraloperator** (docs/44): die Quasi-Invertierbarkeit in Modellfällen numerisch.

## Vorgehen (mit dem 7-Schritte-Protokoll, docs/50)
1. Frage präzise + falsifizierbar formulieren (`reasoning_scaffold`).
2. In ein Leitmotiv einordnen (A/B/C, docs/41) und verwandte Doks ziehen (`graph_neighbors`).
3. Annahmen + Status klären (`get_claim`).
4. **Obstruktions-Check** (`evaluate_proof_idea`) — bei jedem „Beweis"-Anspruch Pflicht.
5. Experiment rechnen (`compute_*`/`plot_*`) und **ins Logbuch** (`log_experiment`).
6. Ergebnis ehrlich einordnen: Evidenz vs. Beweis; nächster prüfbarer Schritt.

## Was man dem Professor vorlegen kann
- Reproduzierbare Experiment-Notizen (`kb/experiments/*.md`) mit Hypothese/Methode/Ergebnis.
- Figuren (`kb/figures/*.png`).
- Ein Lean-Projekt-Gerüst (`kb/lean/`), das lokal baut.
- Diese Wissensbasis als Landkarte des Forschungsstands (docs/00_INDEX.md, docs/42 Leseliste).

## Klare Grenzen (Anti-Crackpot)
- Kein „Beweis" ohne bestandenen Obstruktions-Check (docs/35) und ohne Euler-Produkt-Nutzung
  (docs/43). Numerik ist nie ein Beweis (docs/35: Mertens/Skewes).
- Vor Einreichung/Veröffentlichung: Peer-Standards beachten (docs/27).

## Quellen / Bezug
docs/41 (Synthese), docs/35/43/46 (Obstruktionen), docs/37 (Lean), docs/06/14/23 (Experimentfelder),
docs/50 (Denkprotokoll).

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Eingehende Beziehungen**
- *ist Blaupause für* (`blueprint_for`) → [[69_comparison_matrix|69 — Vergleichsmatrix der Ansätze: Achsen, Lesarten, Auswahlhilfe]] — Liefert die realistische Projektliste (testable=high).

**Thematisch benachbart (gemeinsame Tags):** [[37_formalization_lean_proof_assistants|Formalisierung: Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
