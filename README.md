# Riemann-Hypothesis — Forschungs- & Wissens-Server

Ein vollständiges Werkzeug, um die **Riemann-Vermutung (RH)** zu verstehen, zu
visualisieren, Ansätze auszuprobieren und mit einer KI strukturiert-analytisch zu
untersuchen. Vier Teile:

1. **Wissensbasis** (`docs/`, 55 Dokumente) — jeder Ansatz, jedes Kriterium, jeder
   gescheiterte Beweis und jede Obstruktion, jeweils mit **mathematischem Kern**
   (Formeln, Sätze, Beweisskizzen) und Quellen.
2. **Wissensgraph + RAG** (`kb/`) — Dokumente + Konzepte + atomare *Claims* mit Status,
   verbunden durch typisierte Relationen; hybride Suche; als **MCP-Server** mit Tools.
3. **Rechnen & Visualisieren** (`kb/compute.py`, `kb/visualize.py`) — echte ζ-/Nullstellen-
   Berechnungen (mpmath) und Grafiken (matplotlib).
4. **Obsidian-Wissensnetz** (`obsidian/`) — derselbe Graph als begehbarer Vault: jede
   Notiz ein Ansatz, jede Kante ein [[Wikilink]], sichtbar in Obsidians Graph-Ansicht.

> **Ehrlich vorab:** Dieses Repo *beweist die RH nicht* und kann das auch nicht — niemand
> kann das bisher. Es ist ein **Forschungs-, Lern- und Verifikationsinstrument**, das
> strukturiertes Arbeiten erzwingt und vor bekannten Sackgassen warnt (siehe `docs/35`,
> `docs/43`, `docs/46`).

## Was ist die Riemann-Vermutung? (in einem Satz)
Die Nullstellen der Riemannschen ζ-Funktion, die die Verteilung der Primzahlen steuern,
liegen — so die Vermutung — alle exakt auf der „kritischen Geraden" Re(s) = 1/2.
Details: `docs/01`, `docs/02`, `docs/38`; Begriffe: `docs/40_glossary_notation.md`.

## Schnellstart (für Einsteiger)
```bash
# 1) Rechen-/Plot-Bibliotheken (einmalig)
pip install -r kb/requirements.txt        # mpmath, numpy, matplotlib (+ optional mcp)

# 2) Index bauen
python3 kb/build_kb.py

# 3) Geführte Tour (erzeugt Figuren + ein Beispiel-Experiment)
python3 kb/demo.py

# 4) Selbst ausprobieren (ohne Installation, nur Stdlib für diese)
python3 kb/query.py search "spektraler Operator" -k 5
python3 kb/query.py status refuted
python3 kb/query.py claim "Mertens"
python3 kb/query.py zero 1            # 1. Nullstelle: γ = 14.1347…
python3 kb/query.py scaffold "Ich will die RH beweisen"
```

## Als KI-Werkzeug (MCP-Server)
```bash
pip install "mcp[cli]"
python3 kb/server.py
```
Der Server stellt **~26 Tools** bereit: Suche/Graph/Claims, Denkprotokoll,
Obstruktions-Prüfung, ζ-/Nullstellen-Rechnen, Plots, Experiment-Logbuch und ein
Lean-Verifikations-Tool. Registrierung & System-Prompt: `kb/README.md`.

## Wie die KI strukturiert-analytisch denkt
Erzwungen durch Design (Details: `docs/50_reasoning_protocol.md`):
- **Tool-Forcing** — Zahlen aus `compute_*`, Wahrheitswerte aus `get_claim` (Status),
  Beziehungen aus dem Graphen. Kein „aus dem Kopf".
- **7-Schritte-Protokoll** (`reasoning_scaffold`) — Präzisieren → Klassifizieren →
  Annahmen → Status trennen → **Obstruktions-Check** → Experiment → ehrliches Fazit.
- **Status-Trennung** — jede Antwort kennzeichnet `[BEWIESEN] / [OFFEN] / [EVIDENZ] / [HEURISTIK]`.
- **Anti-Crackpot-Gate** — `evaluate_proof_idea` prüft jede Beweisidee gegen die bekannten
  Obstruktionen (Euler-Produkt nötig, Positivität nicht annehmen, kein „weicher" Beweis …).

## Wissensnetz in Obsidian (visuell)
```bash
python3 kb/build_obsidian.py      # baut/aktualisiert obsidian/
```
Dann in Obsidian *Ordner als Vault öffnen* → `obsidian/` wählen, Notiz
**`Riemann-Wissensnetz`** öffnen und die Graph-Ansicht starten (`Strg/Cmd + G`).

Der Vault enthält **126 Notizen**: 55 Dokument-Notizen (voller Text), 12 Konzepte/Motive,
40 Claims mit Status, 15 Themen-Karten (MOC) und eine Relations-Legende — verbunden durch
~1300 Links. Die Verknüpfungen stammen aus zwei Quellen:
- **kuratierte Relationen** aus `kb/graph/edges.json`, typisiert und richtungsbehaftet
  (`equivalent_to`, `uses`, `obstruction_for`, `refuted_by`, `models`, …);
- **Querverweise im Fließtext** („Dok. 05", `docs/35`), die automatisch zu Wikilinks werden.
Kategorien sind in der Graph-Ansicht farbig gruppiert; Filter wie `tag:#status/open` oder
`path:Dokumente` blenden Teilnetze ein und aus. Details: `obsidian/README.md`.

## Verzeichnis
```
docs/                 55 Wissensdokumente (00_INDEX.md = Einstieg)
manifest.json         maschinenlesbares Verzeichnis
README_RAG.md         Ingestion-/Chunking-Hinweise für Vektor-/MCP-Server
kb/
  build_kb.py         baut den Index
  core.py             Suche/Graph/Claims/Scaffold (Stdlib)
  query.py            CLI zum Testen
  server.py           MCP-Server (alle Tools)
  compute.py          ζ, Z(t), Nullstellen, λ_n, ψ(x)  (mpmath)
  visualize.py        Plots (matplotlib) -> kb/figures/
  experiment.py       reproduzierbares Experiment-Logbuch -> kb/experiments/
  formal.py           Lean/mathlib-Brücke (formale Verifikation)
  demo.py             geführte Tour
  build_obsidian.py   erzeugt den Obsidian-Vault obsidian/
  graph/              kuratierte Knoten/Kanten/Claims
  README.md           Architektur & Tool-Referenz
obsidian/             Obsidian-Vault (Dokumente/, Konzepte/, Claims/, Karten/)
Riemann_Hypothesis_Proof_Approaches.md   Gesamtüberblick (eine Datei, EN)
```

## Roadmap (gemeinsam mit Fachperson/Professor)
Realistisch & wertvoll:
- **Numerische Experimente** (λ_n-Positivität, BBLS-Distanz, GUE-Statistik) — reproduzierbar
  über das Experiment-Logbuch.
- **Formalisierung von Teilresultaten in Lean** (`docs/37`) — verifizierter, publizierbarer
  Fortschritt (z. B. Hardy, de-Bruijn–Newman Λ≥0).
- **Ein äquivalentes Kriterium rechnerisch ausreizen** (z. B. Lapidus-Spektraloperator `docs/44`).

Nicht erreichbar: ein vollständiger maschineller RH-Beweis (die Obstruktionen in `docs/35`,
`43`, `46` erklären, warum das strukturell hart bleibt).

## Lizenz / Quellen
Inhalte aus öffentlichen Quellen (arXiv, AMS, Clay/AIM, Wikipedia, Universitätsseiten),
je Dokument am Ende belegt. Numerik ist **Evidenz, kein Beweis**.
