---
id: doc-51
title: "Kollaborations-Leitfaden: sinnvoll mit einer Fachperson an der RH arbeiten"
nummer: "51"
kategorie: Meta
status: META
typ: dokument
aliases:
  - "doc-51"
  - "Dok. 51"
tags:
  - "dokument"
  - "kategorie/meta"
  - "status/meta"
  - "thema/collaboration"
  - "thema/experiments"
  - "thema/formalization"
  - "thema/open-problems"
  - "thema/professor"
  - "thema/research-program"
quelle: docs/51_collaboration_brief.md
---

> [!info] Navigation
> **Karte:** [[MOC N – Arbeitsweise & Kollaboration]] · **Kategorie:** Meta · **Status:** `META`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/51_collaboration_brief.md`

# Kollaborations-Leitfaden: sinnvoll mit einer Fachperson/Professor an der RH arbeiten

**Kategorie:** Meta / Forschungsorganisation
**Zweck:** Konkrete, realistische Teilprojekte, die mit den Tools dieses Repos einen *echten,
prüfbaren* Beitrag liefern — ohne den unrealistischen Anspruch eines vollständigen RH-Beweises.

## Grundhaltung (ehrlich)
Ein vollständiger RH-Beweis ist nicht das realistische Ziel einer Studien-/Seminararbeit oder
eines KI-Tools (siehe [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]], 41, 46). **Wertvoll und erreichbar** sind: reproduzierbare
numerische Experimente, formale Verifikation von Teilresultaten, und die rechnerische
Ausreizung *zur RH äquivalenter* Kriterien. Genau dafür sind die Tools gebaut.

## Drei realistische Projektklassen

### Klasse A — Numerisch-experimentelle Mathematik (sofort machbar)
Werkzeuge: `compute_*`, `plot_*`, `research/spacing_vs_gue.py`, Experiment-Logbuch.
Beispiele:
1. **Montgomery–Odlyzko-Gesetz** quantifizieren ([[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|docs/06]]): Abstandsstatistik vs. GUE — bereits
   als Flaggschiff-Experiment vorhanden (`kb/research/spacing_vs_gue.py`). Erweiterbar auf
   höhere Korrelationen, größere Höhen, andere L-Funktionen.
2. **Li-Koeffizienten** ([[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|docs/14]]): λ_n-Positivität + Wachstum λ_n ~ ½ n log n testen; Abweichungen
   analysieren. Frage: ab welchem n bricht die Näherung (Nullstellenzahl) zusammen?
3. **Explizite Formel** ([[02 Riemann–von-Mangoldt-Formel und die explizite Formel|docs/02]]): Konvergenz von ψ(x) gegen die echte Primzahlsummation als
   Funktion der Nullstellenzahl — Fehlerterm-Skalierung empirisch bestimmen.
4. **S(T)-Statistik** ([[02 Riemann–von-Mangoldt-Formel und die explizite Formel|docs/02]]): Verteilung des Argumentterms S(T) bei wachsendem T (Selberg-CLT:
   S(T)/√(½ log log T) → Normalverteilung) numerisch prüfen.

### Klasse B — Formale Verifikation in Lean (mit Professor, hoher Wert)
Werkzeuge: `kb/lean/`, `formal_statement`, `lean_check` ([[37 Formalisierung – Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)|docs/37]]).
Beispiele:
1. Ein **zur RH äquivalentes Kriterium** formal aufschreiben (Λ≤0 [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15|docs/23]]; Li-Positivität [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|docs/14]];
   Robin [[15 Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)|docs/15]]) und die Äquivalenz zur Standardaussage beweisen.
2. **Bewiesene Teilresultate** formalisieren: Hardy (∞ viele Nullstellen, [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden|docs/03]]), Rodgers–Tao
   Λ≥0 ([[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15|docs/23]]). Jeder lückenlos geprüfte Beweis ist publizierbarer Fortschritt.
3. Schon die **Definitionen** sauber in mathlib-Stil (ξ-Funktion, N(T), Li-Koeffizienten) sind
   ein Beitrag, auf dem andere aufbauen.

### Klasse C — Ein äquivalentes Kriterium rechnerisch ausreizen
Beispiele:
1. **Báez-Duarte-Distanz** d_N ([[13 Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung|docs/13]]/45): numerisch berechnen und die vermutete Rate
   d_N² ~ (2+γ−log 4π)/log N prüfen — sehr „greifbares" Ziel mit konkreter Konstante.
2. **Weil-Positivität endlichdimensional** ([[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|docs/14]]): die quadratische Form auf einem
   endlichen Funktionenraum aufstellen und ihre kleinste Eigenwert-Schranke verfolgen.
3. **Lapidus-Spektraloperator** ([[44 Lapidus – Fraktale Saiten, inverses Spektralproblem & Spektraloperator|docs/44]]): die Quasi-Invertierbarkeit in Modellfällen numerisch.

## Vorgehen (mit dem 7-Schritte-Protokoll, [[50 Denkprotokoll – strukturiert-analytisches Arbeiten an der RH|docs/50]])
1. Frage präzise + falsifizierbar formulieren (`reasoning_scaffold`).
2. In ein Leitmotiv einordnen (A/B/C, [[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss|docs/41]]) und verwandte Doks ziehen (`graph_neighbors`).
3. Annahmen + Status klären (`get_claim`).
4. **Obstruktions-Check** (`evaluate_proof_idea`) — bei jedem „Beweis"-Anspruch Pflicht.
5. Experiment rechnen (`compute_*`/`plot_*`) und **ins Logbuch** (`log_experiment`).
6. Ergebnis ehrlich einordnen: Evidenz vs. Beweis; nächster prüfbarer Schritt.

## Was man dem Professor vorlegen kann
- Reproduzierbare Experiment-Notizen (`kb/experiments/*.md`) mit Hypothese/Methode/Ergebnis.
- Figuren (`kb/figures/*.png`).
- Ein Lean-Projekt-Gerüst (`kb/lean/`), das lokal baut.
- Diese Wissensbasis als Landkarte des Forschungsstands ([[00 Riemann Hypothesis – Dokumenten-Index (RAG Knowledge Base)|docs/00]], [[42 Zeittafel & kanonische Leseliste|docs/42]] Leseliste).

## Klare Grenzen (Anti-Crackpot)
- Kein „Beweis" ohne bestandenen Obstruktions-Check ([[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]]) und ohne Euler-Produkt-Nutzung
  ([[43 Epstein-Zetafunktionen & Selberg-Klassen-Rigidität – Welche Eigenschaft erzwingt die kritische Gerade|docs/43]]). Numerik ist nie ein Beweis ([[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]]: Mertens/Skewes).
- Vor Einreichung/Veröffentlichung: Peer-Standards beachten ([[27 Weitere umstrittene, zurückgezogene & fehlerhafte Beweisbehauptungen|docs/27]]).

## Quellen / Bezug
[[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss|docs/41]] (Synthese), [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]]/43/46 (Obstruktionen), [[37 Formalisierung – Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)|docs/37]] (Lean), [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|docs/06]]/14/23 (Experimentfelder),
[[50 Denkprotokoll – strukturiert-analytisches Arbeiten an der RH|docs/50]] (Denkprotokoll).

---

## 🔗 Wissensgraph

### Im Text erwähnt

- [[00 Riemann Hypothesis – Dokumenten-Index (RAG Knowledge Base)]]
- [[02 Riemann–von-Mangoldt-Formel und die explizite Formel]]
- [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden]]
- [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]]
- [[13 Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]]
- [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]]
- [[15 Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)]]
- [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15]]
- [[27 Weitere umstrittene, zurückgezogene & fehlerhafte Beweisbehauptungen]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
- [[37 Formalisierung – Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)]]
- [[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]]
- [[42 Zeittafel & kanonische Leseliste]]
- [[43 Epstein-Zetafunktionen & Selberg-Klassen-Rigidität – Welche Eigenschaft erzwingt die kritische Gerade]]
- [[44 Lapidus – Fraktale Saiten, inverses Spektralproblem & Spektraloperator]]
- [[50 Denkprotokoll – strukturiert-analytisches Arbeiten an der RH]]
