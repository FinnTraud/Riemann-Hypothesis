# RH Knowledge-Graph-RAG — MCP-Server

Hybrider **Wissensgraph + Retrieval**-Server über die 71 RH-Dokumente in `../docs/`.
Vier Schichten machen ihn „bulletproof":

1. **Wissensgraph** — Dokumente + Konzepte + atomare *Claims* als Knoten, typisierte
   Relationen als Kanten (`equivalent_to`, `implies`, `reduces_to`, `refuted_by`,
   `obstruction_for`, `models`, `blueprint_for`, …). Erlaubt *Traversieren* statt nur
   Ähnlichkeitssuche.
2. **Claims mit Status** — jede Schlüsselaussage trägt `status: proven|open|refuted`.
   So kann der Assistent eine widerlegte Aussage (z. B. Mertens-Vermutung) nie als
   wahr behandeln.
3. **Hybrid-Retrieval** — BM25 (lexikalisch, trifft Mathe-Symbole/Namen) + Graph-Expansion
   (Treffer wird um äquivalente/widerlegende Nachbarn ergänzt). Embeddings optional nachrüstbar.
4. **Vergleichs- & Diagnose-Schicht** (`compare.py`) — 45 Ansatzprofile entlang 8 Achsen und
   15 **Fehlermodi** (F1–F15). Beantwortet: *Wer hat überhaupt einen Implikationspfeil zur RH?
   Wer scheitert am selben Punkt? Woran scheitern Ansätze am häufigsten?*

## Dateien
```
kb/
  build_kb.py          # baut kb/index/kb.json aus docs/ + manifest.json + graph/
  core.py              # gemeinsame Abfragelogik (Stdlib)
  compare.py           # Ansatz-Vergleich + Fehlermodus-Analyse (Stdlib)
  build_obsidian.py    # erzeugt die Obsidian-Netzwerkschicht in docs/
  query.py             # CLI zum Testen (Stdlib, keine Installation)
  server.py            # MCP-Server (FastMCP) — exponiert die Tools
  requirements.txt
  graph/
    nodes.json         # kuratierte Konzept-Knoten
    edges.json         # kuratierte typisierte Relationen (das intellektuelle Herzstück)
    claims.json        # atomare Aussagen mit Status
    approaches.json    # 45 Ansatzprofile (Achsen, offener Schritt, Hebel, Fehlermodi)
    failure_modes.json # Taxonomie F1–F15 mit Prüffragen und historischen Fällen
  index/
    kb.json            # GENERIERT von build_kb.py
```

## Schnellstart (ohne Installation, nur Stdlib)
```bash
python3 kb/build_kb.py                 # Index bauen (einmalig / nach Doc-Änderungen)
python3 kb/query.py stats
python3 kb/query.py search "spektraler Operator Nullstellen" -k 5
python3 kb/query.py neighbors concept-hilbert-polya
python3 kb/query.py path doc-19 concept-RH
python3 kb/query.py status refuted
python3 kb/query.py claim "Mertens"
python3 kb/query.py evaluate "Beweis nur mit Funktionalgleichung und Wachstum"
```

## Als MCP-Server betreiben
```bash
pip install "mcp[cli]"
python3 kb/build_kb.py
python3 kb/server.py            # stdio
```
Registrierung in einem MCP-Client (Beispiel `claude_desktop_config.json` / `.mcp.json`):
```json
{
  "mcpServers": {
    "riemann-kb": {
      "command": "python3",
      "args": ["/home/user/Riemann-Hypothesis/kb/server.py"]
    }
  }
}
```

## Tools (MCP)
| Tool | Zweck |
|---|---|
| `search(query,k,status,category)` | Hybride BM25-Suche + Graph-Nachbarn |
| `get_document(node_id)` | Volles Markdown + Metadaten + Nachbarn |
| `graph_neighbors(node_id,relation)` | Typisierte Nachbarn (Relation filterbar) |
| `find_path(a,b,max_depth)` | Kürzester Beziehungspfad zweier Knoten |
| `list_by_status(status)` | Dokumente + Claims nach proven/open/refuted/… |
| `get_claim(query)` | Atomare Aussagen **mit Status** (Anti-Halluzination) |
| `evaluate_proof_idea(idea)` | Prüft Beweisidee gegen Obstruktionen (Doc 35/41/43/46) |
| `reasoning_scaffold(task)` | 7-Schritte-Denkprotokoll (Doc 50) |
| `kb_stats()` | Kennzahlen |

### Vergleich & Fehleranalyse (docs/68, docs/69)
| Tool | Zweck |
|---|---|
| `list_approaches(...)` | Ansätze über die Achsen filtern (z. B. `equivalence=conditional`) |
| `approach_profile(key)` | Profil: Achsen, offener Kernschritt, Hebel, Fehlermodi |
| `compare_approaches([keys])` | Achsenweise Gegenüberstellung, Gemeinsames vs. Trennendes |
| `bridge_approaches(a,b)` | Verknüpfung: gemeinsame Fehlermodi + Graphpfad + gemeinsame Nachbarn |
| `failure_statistics()` | **Woran scheitern Ansätze am häufigsten?** (aggregiert) |
| `failure_mode(id)` / `list_failure_modes()` | Ein Fehlermodus im Detail / ganze Taxonomie |
| `diagnose_idea(idea)` | Beweisidee gegen alle 15 Fehlermodi prüfen (Prüffragen) |

### Rechnen & Visualisieren (mpmath / matplotlib)
| Tool | Zweck |
|---|---|
| `compute_zeta`, `compute_nth_zero`, `compute_first_zeros` | ζ-Werte & Nullstellen |
| `compute_verify_rh_range`, `compute_count_zeros` | RH-Check (Evidenz), N(T) |
| `compute_li_coefficient`, `compute_psi_explicit` | λ_n, explizite Formel |
| `plot_hardy_Z`, `plot_zeros_on_line`, `plot_zeta_strip`, `plot_counting_N` | Grundplots |
| `plot_pair_correlation`, `plot_li_coefficients`, `plot_psi_convergence` | Forschungsplots |

### Experiment & formale Verifikation
| Tool | Zweck |
|---|---|
| `log_experiment`, `list_experiments`, `get_experiment` | reproduzierbares Logbuch |
| `formal_statement` | RH-Aussage in Lean + Projekt-Gerüst (kb/lean/) |
| `lean_check`, `lean_status` | Lean-Verifikation (falls Toolchain vorhanden) |

### Semantische Suche
`search` ist hybrid: **BM25 + Semantik** (neuronale Embeddings, falls `sentence-transformers`
installiert; sonst TF-IDF-Cosinus ohne Download) + Graph-Expansion. Parameter `semantic`/`alpha`.

### Flaggschiff-Experiment
`python3 kb/research/spacing_vs_gue.py 500` — Montgomery–Odlyzko-Gesetz (Nullstellenabstände
vs. GUE), schreibt Ergebnis ins Logbuch.

## Empfohlener System-Prompt für den RH-Assistenten
> Für jede Behauptung über die RH zuerst `get_claim` aufrufen und den `status` respektieren
> (refuted ⇒ nie als wahr ausgeben). Bei „ist das ein Beweis?"-Fragen IMMER
> `evaluate_proof_idea` + `get_document('doc-35')` + `get_document('doc-43')` nutzen.
> Antworten mit `search` belegen und Graph-Nachbarn (Äquivalenzen/Widerlegungen) erwähnen.
> Bei Vergleichsfragen („welcher Ansatz ist vielversprechender?") NICHT ranken, sondern
> `compare_approaches` bzw. `bridge_approaches` aufrufen und achsenweise antworten —
> insbesondere die Achse `equivalence` (hat der Ansatz überhaupt einen Implikationspfeil?).
> Bei „warum ist das noch nicht gelöst?" `failure_statistics()` + `docs/68` heranziehen.

## Relationstypen im Graphen
`equivalent_to, implies, reduces_to, special_case_of, generalizes, partial_result_for,
weaker_than, refuted_by, obstruction_for, evidence_for, models, blueprint_for,
attempts_transfer_of, uses, instance_of`.

## Erweiterung (optionale Aufwertungen)
- **Embeddings**: `core.search` um dichte Vektoren ergänzen (sentence-transformers), Score
  als `α·BM25 + (1−α)·cosine`. Schnittstelle ist vorbereitet (ein Scorer pro Chunk).
- **Tools für echte Mathematik**: mpmath/PARI (Nullstellen/ζ rechnen) und ein Lean-Checker
  (Doc 37) als zusätzliche MCP-Tools — macht aus dem Nachschlage- einen Rechen-/Prüf-Server.
- **Auto-Update**: `build_kb.py` per CI/cron nach Änderungen an `docs/` neu laufen lassen.

## Reproduzierbarkeit
`kb/index/kb.json` ist generiert. Quelle der Wahrheit sind `docs/*.md` (Inhalt) und
`kb/graph/*.json` (kuratierter Graph). Nach Änderungen `build_kb.py` erneut ausführen.
