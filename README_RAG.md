# RH Knowledge Base — Anleitung für MCP-Server / RAG-Ingestion

Diese Wissensbasis ist eine kuratierte, quellenbelegte Sammlung zu **allen ernstzunehmenden Ansätzen, Kriterien, gescheiterten Beweisen und Obstruktionen** rund um die Riemann-Vermutung (RH). Sie ist für die Einbettung in einen Vektor-/MCP-Server optimiert.

## Aufbau

```
Riemann_Hypothesis_Proof_Approaches.md   # Gesamtüberblick (eine Datei, EN)
docs/
  00_INDEX.md                            # Inhaltsverzeichnis + Kategorien
  01..49_*.md                            # je 1 Thema pro Datei (DE), mit YAML-Frontmatter
README_RAG.md                            # diese Datei
manifest.json                            # maschinenlesbares Verzeichnis (generiert)
```

- **50 Dokumente** (00–49). Jedes ist ein eigenständiger, abrufbarer Chunk.
- Jede Datei hat **YAML-Frontmatter** (id, number, title, category, status, tags, source_file, lang).
- Jedes Inhaltsdokument folgt demselben Schema: `Metadaten → Zusammenfassung → Mathematischer Kern (Formeln/Sätze/Beweisskizzen) → Bedeutung/Einordnung → Quellen`.

## Frontmatter-Felder

| Feld | Bedeutung | Werte |
|---|---|---|
| `status` | Reifegrad | `proven` (bewiesen), `open` (offen), `refuted` (widerlegt/gescheitert), `reference` (Faktenreferenz), `meta` (Methodik/Obstruktion) |
| `category` | Themengruppe | foundations, partial-results, spectral, analytic, criterion, proven-analogue, generalization, breakthrough, numerical, failed-proof, ai-context, solution-program, obstruction, synthesis, glossary, frontier, heuristic, verification, context, reference, index |
| `tags` | Stichworte | Liste (z. B. `euler-product`, `GUE`, `weil-positivity`) |
| `number` | Dateinummer | `00`–`49` |

## Empfohlene Chunking-Strategie

1. **Pro `##`-Sektion chunken** (nicht pro Datei) — die Dokumente sind mit klaren `##`-Überschriften strukturiert. Ideale Chunk-Größe ist eine Sektion (Zusammenfassung / Mathematischer Kern / Bedeutung / Quellen).
2. **Frontmatter als Metadaten-Filter** in den Vektorstore übernehmen (status, category, tags) — erlaubt gefilterte Retrieval-Queries, z. B. „nur `status:open` + `category:solution-program`".
3. **Kontext-Präfix:** Jedem Chunk den `title` + `number` voranstellen (z. B. „[Doc 10 — Connes NCG] …"), damit Embeddings den Kontext behalten.
4. **Formeln beibehalten:** Code-Blöcke (``` … ```) enthalten die Mathematik — nicht entfernen; sie sind wesentlicher Retrieval-Inhalt.

## Empfohlene Retrieval-Hinweise (System-Prompt für den RH-Assistenten)

> Beim Beantworten von RH-Fragen: (a) zuerst `40_glossary_notation.md` für Begriffe; (b) für „könnte das ein Beweis sein?"-Fragen IMMER `35_obstructions_barriers.md` + `43_Epstein_zeta_Selberg_class_rigidity.md` + `41_synthesis_what_a_proof_needs.md` heranziehen und die Anti-Crackpot-Checkliste anwenden; (c) `status:refuted`-Dokumente als Warnbeispiele nutzen; (d) niemals numerische Evidenz als Beweis akzeptieren (siehe Mertens/Skewes in Doc 35).

## „Bulletproof"-Kerndokumente (für Beweis-Bewertung)

- `35_obstructions_barriers.md` — warum naive Ansätze scheitern + Checkliste
- `43_Epstein_zeta_Selberg_class_rigidity.md` — welche Eigenschaft die kritische Gerade erzwingt (Euler-Produkt!)
- `46_Voronin_universality.md` — warum „weiche" funktionentheoretische Beweise nicht gehen
- `41_synthesis_what_a_proof_needs.md` — notwendige Bedingungen + Bewertungsraster
- `37_formalization_lean_proof_assistants.md` — formale Verifikation als finaler Filter

## Status-Legende für Nutzer

- ✅ `proven` — etablierter Satz (z. B. RH über endlichen Körpern, Hardy, Guth–Maynard-Dichte)
- ⏳ `open` — aktiver, unbewiesener Ansatz/Kriterium
- ❌ `refuted` — gescheitert/widerlegt (de Branges, Atiyah, Mertens-Vermutung)
- 📖 `reference` / 🧭 `meta` — Fakten- bzw. Methodik-/Obstruktionsdokumente

## Aktualisierung
Die „Live-Front" (`49_live_analytic_frontier.md`) und numerische Schranken (`24`) veralten am schnellsten. Empfehlung: arXiv-Feeds zu *zero-density estimate*, *subconvexity*, *moments of zeta*, *de Bruijn–Newman* periodisch nachziehen. Stand der Sammlung: Juni 2026.

## Lizenz / Herkunft
Inhalte zusammengetragen via agentischer Web-Recherche aus öffentlichen Quellen (arXiv, AMS, Wikipedia, Universitätsseiten, Clay/AIM). Jede Datei listet ihre Quellen am Ende. Bei den jüngsten Preprints (2024–2026) vor Zitation in formalen Arbeiten Quelle gegenprüfen.
