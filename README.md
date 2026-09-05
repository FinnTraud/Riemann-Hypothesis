# Riemann-Hypothesis — Forschungs- & Wissens-Server

Ein vollständiges Werkzeug, um die **Riemann-Vermutung (RH)** zu verstehen, zu
visualisieren, Ansätze auszuprobieren und mit einer KI strukturiert-analytisch zu
untersuchen. Drei Teile:

1. **Wissensbasis** (`docs/`, 79 Dokumente) — jeder Ansatz, jedes Kriterium, jeder
   gescheiterte Beweis und jede Obstruktion, jeweils mit **mathematischem Kern**
   (Formeln, Sätze, Beweisskizzen) und Quellen. Dokumente 55–64 bilden eine
   **Meta-Analyse-Schicht**: Muster im Scheitern, Autopsien, Lücken-Register,
   Prüfwerkzeuge (siehe unten).
2. **Wissensgraph + RAG** (`kb/`) — Dokumente + Konzepte + atomare *Claims* mit Status,
   verbunden durch typisierte Relationen; hybride Suche; als **MCP-Server** mit Tools.
3. **Rechnen & Visualisieren** (`kb/compute.py`, `kb/visualize.py`) — echte ζ-/Nullstellen-
   Berechnungen (mpmath) und Grafiken (matplotlib).
4. **Obsidian-Vault** — der kuratierte Graph ist als Wikilinks, Canvas und
   Statusboard im Vault sichtbar (`kb/obsidian.py`, idempotent generiert).

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

## Die Meta-Analyse-Schicht (docs/55–64)

Diese Schicht enthält **keine neue Mathematik über ζ**. Sie wertet die Dokumente
01–54 quer aus — und genau daraus entstehen die Aussagen, die man an keinem
Einzeldokument sieht:

| Dok | Was es leistet | Kernbefund |
|---|---|---|
| **55** | Blocker-Taxonomie + Obstruktions×Ansatz-Matrix | 56 Ansätze scheitern an 15 Blockern; *zirkuläre Positivität* allein trägt 11. Zwei unabhängige Klassifikationen stimmen bei 12 von 15 Modi überein, beim **Tier** nur bei 7 von 12 |
| **56** | Fehler-Autopsien | Die Bruchstelle liegt nie in der Zahlentheorie — sie liegt bei Liouville, bedingter Konvergenz, Definitionsbereichen |
| **57** | Noch nicht Versuchtes, mit Abbruchkriterien | Die Nachweisgrenze des Li-Kriteriums skaliert wie γ² — n ≤ 1000 reicht nicht bis zur ersten ζ-Nullstelle |
| **58** | GAP-Registry mit Near-Miss-Score | Near-Miss und Aussicht sind **antikorreliert**: die drei folgenreichsten Lücken haben Score 0 |
| **59** | Invarianten: „beweist Ihr Argument zu viel?" | Λ ≥ 0 heißt: die RH hat **keine Marge** — jedes Argument mit Spielraum ist falsch |
| **60** | Gegenbeispiel-Orakel | Turing-Defizit findet die RH-Verletzung selbstständig: ζ 38/38 → 0, Davenport–Heilbronn 68/64 → **4** |
| **61** | Negativraum ¬RH | Robust ist genau die Obstruktionsschicht; fragil sind die Äquivalenzen |
| **62** | KI-Arbeitsteilung + Selbstaudit | 8 offengelegte Schwächen dieses Repos |
| **63** | Entscheidungswert von Experimenten | Ein Experiment mit vorhersagbarem Ergebnis hat Wert 0 |
| **64** | Trust-Tiers je Claim | **1 von 68** Claims ist maschinell verifiziert; 63 sind Sekundärwissen |
| **65** | Sensitivität der Kriterien | d_N < 0,01 verlangt Dimension **10²⁰¹**; Robins Marge fällt nur wie 1/√(log n) — numerische Kriterienprüfung ist als RH-Evidenz wertlos |
| **78** | Vergleichsmatrix (45 Ansätze × 8 Achsen) | Bestätigt den Positivitäts-Engpass **unabhängig** über einen zweiten Datensatz und eine andere Methode |

```bash
python3 kb/counterexample.py all -T 120   # Gegenbeispiel-Orakel (Kern von docs/60)
python3 kb/sensitivity.py all             # Reichweite der Kriterien (docs/65)
python3 kb/compare.py stats               # woran Ansätze am häufigsten scheitern
python3 kb/compare.py bridge doc-10 doc-31   # was zwei Ansätze verbindet
python3 kb/compare.py diagnose "<Beweisidee>"  # gegen alle 15 Fehlermodi prüfen
python3 kb/invariants.py                  # Prüfliste: beweist es zu viel? (docs/59)
python3 kb/trust.py                       # Verifikationsstufen (docs/64)
python3 kb/validate.py                    # Konsistenz des Wissensgraphen
python3 kb/matrix.py && python3 kb/gaps.py && python3 kb/obsidian.py   # alles neu generieren
```

## Als Obsidian-Vault
Repo in Obsidian als Vault öffnen. Die Konfiguration liegt bei (`.obsidian/`,
Graph-Farbgruppen nach Kategorie). Danach:
- **Graph View** zeigt die 209 kuratierten Kanten statt isolierter Punkte
- **`docs/_Statusboard.md`** ist das Dashboard (Dataview optional — statische
  Tabelle als Fallback ist eingebaut)
- **`Canvas/Zeitachse_Motive.canvas`** — 165 Jahre in vier Leitmotiv-Spalten
- **`Canvas/Obstruktionskarte.canvas`** — Blocker mit den Ansätzen, die daran hängen
- Jedes Dokument endet mit **„Verknüpfungen (auto)"**: Blocker, fehlende
  Aussage, Graph-Nachbarn — generiert aus `kb/graph/*.json`, nie von Hand

Neu generieren nach Änderungen an den Graph-Daten: `python3 kb/obsidian.py`.

## Wie die KI strukturiert-analytisch denkt
Erzwungen durch Design (Details: `docs/50_reasoning_protocol.md`):
- **Tool-Forcing** — Zahlen aus `compute_*`, Wahrheitswerte aus `get_claim` (Status),
  Beziehungen aus dem Graphen. Kein „aus dem Kopf".
- **7-Schritte-Protokoll** (`reasoning_scaffold`) — Präzisieren → Klassifizieren →
  Annahmen → Status trennen → **Obstruktions-Check** → Experiment → ehrliches Fazit.
- **Status-Trennung** — jede Antwort kennzeichnet `[BEWIESEN] / [OFFEN] / [EVIDENZ] / [HEURISTIK]`.
- **Anti-Crackpot-Gate** — `evaluate_proof_idea` prüft jede Beweisidee gegen die bekannten
  Obstruktionen (Euler-Produkt nötig, Positivität nicht annehmen, kein „weicher" Beweis …).
  Danach: `invariant_checklist` (beweist es zu viel? `docs/59`) und
  `counterexample_oracle` (was sagt die Maschine? `docs/60`). Zur Schwäche des
  Stichwort-Gates siehe `docs/62`, Befund 3.

## Verzeichnis
```
docs/                 79 Wissensdokumente (00_INDEX.md = Einstieg)
                      55-65 Meta-Analyse · 66-78 vertiefende Mathematik + Vergleichsmatrix
docs/fehlermodi/      generiert: je Blocker eine Atomnotiz (F1-F15)
docs/concepts/        generiert: je Konzept eine Hub-Notiz
docs/moc/             generiert: Maps of Content je Ansatz-Familie
docs/_Statusboard.md  generiertes Dashboard
Canvas/               2 generierte Obsidian-Canvas
.obsidian/            Vault-Konfiguration (Graph-Farbgruppen)
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
  counterexample.py   Gegenbeispiel-Orakel (Davenport-Heilbronn)  -> docs/60
  sensitivity.py      Reichweite der Kriterien (Robin/d_N/Li/Lambda) -> docs/65
  compare.py          Achsenvergleich, Bruecken, Diagnose            -> docs/78
  invariants.py       Testvektoren & Ueberschuss-Tests            -> docs/59
  matrix.py           Obstruktions x Ansatz-Matrix                -> docs/55
  gaps.py             Near-Miss-Ranking                           -> docs/58
  trust.py            Verifikationsstufen je Claim                -> docs/64
  obsidian.py         Wikilinks + Canvas + Statusboard + Config
  validate.py         Konsistenzpruefung des Graphen
  graph/              kuratierte Knoten/Kanten/Claims/Blocker/Luecken/Invarianten
                      + approaches.json (45 Ansaetze x 8 Achsen)
  lean/RH/Gaps.lean   Lean-Gap-Ledger (sorry-Adressliste)         -> docs/58
  README.md           Architektur & Tool-Referenz
Riemann_Hypothesis_Proof_Approaches.md   Gesamtüberblick (eine Datei, EN)
```

## Roadmap (gemeinsam mit Fachperson/Professor)
Priorisiert nach Entscheidungswert (`docs/63`) statt nach Aufwand:
- **Numerische Experimente** — reproduzierbar über das Experiment-Logbuch. Aber:
  `docs/65` zeigt, dass λ_n-Positivität und BBLS-Distanz als *Evidenz* nichts
  taugen (Reichweite γ ≈ 3,6 bzw. Dimension 10²⁰¹). Ihr Wert liegt in der
  Validierung von Implementierungen, nicht in der Bestätigung der RH.
- **Formalisierung von Teilresultaten in Lean** (`docs/37`) — verifizierter, publizierbarer
  Fortschritt (z. B. Hardy, de-Bruijn–Newman Λ≥0).
- **Ein äquivalentes Kriterium rechnerisch ausreizen** (z. B. Lapidus-Spektraloperator `docs/44`).

**Ausdrücklich abgeraten** wird von „höher rechnen" (mehr Nullstellen verifizieren):
Ergebnis vollständig vorhersagbar, Reichweite null, Kosten maximal — die
schlechteste Kombination im Feld (`docs/63`, Position ⑥).

Nicht erreichbar: ein vollständiger maschineller RH-Beweis (die Obstruktionen in `docs/35`,
`43`, `46`, `55` erklären, warum das strukturell hart bleibt).

## Lizenz / Quellen — und eine wichtige Einschränkung
Inhalte aus öffentlichen Quellen (arXiv, AMS, Clay/AIM, Wikipedia, Universitätsseiten),
je Dokument am Ende belegt. Numerik ist **Evidenz, kein Beweis**.

> **63 von 68 Claims tragen `zugang: sekundaer`: die Primärquellen wurden für
> diese Wissensbasis nicht gelesen.** Die Links belegen, *wo* etwas nachzulesen
> wäre — nicht, dass es nachgelesen wurde. Für Lehrbuchaussagen ist das
> unkritisch, für die neun Preprint-Claims aus `docs/52`–`54` ist es die
> entscheidende Einschränkung. Vollständig aufgeschlüsselt in `docs/64`,
> jederzeit prüfbar mit `python3 kb/trust.py`.
>
> **Wer aus dieser Wissensbasis zitiert, zitiert die Primärquelle — nach
> eigener Lektüre. Der Vault ist eine Landkarte, keine Quelle.**
