# RH Knowledge Base — guide for MCP server / RAG ingestion

This knowledge base is a curated, source-cited collection covering **all serious approaches, criteria, failed proofs, and obstructions** around the Riemann Hypothesis (RH). It is optimized for embedding into a vector/MCP server.

## Structure

```
Riemann_Hypothesis_Proof_Approaches.md   # overall survey (one file, EN)
docs/
  00_INDEX.md                            # table of contents + categories
  01..49_*.md                            # 1 topic per file (EN), with YAML frontmatter
README_RAG.md                            # this file
manifest.json                            # machine-readable index (generated)
```

- **50 documents** (00–49). Each is a self-contained, retrievable chunk.
- Every file has **YAML frontmatter** (id, number, title, category, status, tags, source_file, lang).
- Every content document follows the same schema: `metadata → summary → mathematical core (formulas/theorems/proof sketches) → significance/context → sources`.

## Frontmatter fields

| Field | Meaning | Values |
|---|---|---|
| `status` | Maturity | `proven`, `open`, `refuted` (refuted/failed), `reference` (factual reference), `meta` (methodology/obstruction) |
| `category` | Topic group | foundations, partial-results, spectral, analytic, criterion, proven-analogue, generalization, breakthrough, numerical, failed-proof, ai-context, solution-program, obstruction, synthesis, glossary, frontier, heuristic, verification, context, reference, index |
| `tags` | Keywords | list (e.g. `euler-product`, `GUE`, `weil-positivity`) |
| `number` | File number | `00`–`49` |

## Recommended chunking strategy

1. **Chunk per `##` section** (not per file) — the documents are structured with clear `##` headings. The ideal chunk size is one section (summary / mathematical core / significance / sources).
2. **Use the frontmatter as metadata filters** in the vector store (status, category, tags) — this allows filtered retrieval queries, e.g. "only `status:open` + `category:solution-program`".
3. **Context prefix:** prepend the `title` + `number` to each chunk (e.g. "[Doc 10 — Connes NCG] …") so the embeddings retain context.
4. **Keep the formulas:** code blocks (``` … ```) contain the mathematics — do not remove them; they are essential retrieval content.

## Recommended retrieval guidance (system prompt for the RH assistant)

> When answering RH questions: (a) first consult `40_glossary_notation.md` for terms; (b) for "could this be a proof?" questions, ALWAYS pull in `35_obstructions_barriers.md` + `43_Epstein_zeta_Selberg_class_rigidity.md` + `41_synthesis_what_a_proof_needs.md` and apply the anti-crackpot checklist; (c) use `status:refuted` documents as cautionary examples; (d) never accept numerical evidence as proof (see Mertens/Skewes in Doc 35).

## "Bulletproof" core documents (for proof evaluation)

- `35_obstructions_barriers.md` — why naive approaches fail + checklist
- `43_Epstein_zeta_Selberg_class_rigidity.md` — which property forces the critical line (the Euler product!)
- `46_Voronin_universality.md` — why "soft" function-theoretic proofs don't work
- `41_synthesis_what_a_proof_needs.md` — necessary conditions + evaluation grid
- `37_formalization_lean_proof_assistants.md` — formal verification as a final filter

## Status legend for users

- ✅ `proven` — established theorem (e.g. RH over finite fields, Hardy, Guth–Maynard density)
- ⏳ `open` — active, unproven approach/criterion
- ❌ `refuted` — failed/refuted (de Branges, Atiyah, Mertens conjecture)
- 📖 `reference` / 🧭 `meta` — factual resp. methodology/obstruction documents

## Updating
The "live frontier" (`49_live_analytic_frontier.md`) and numerical bounds (`24`) become outdated fastest. Recommendation: periodically follow arXiv feeds on *zero-density estimate*, *subconvexity*, *moments of zeta*, *de Bruijn–Newman*. State of the collection: June 2026.

## License / provenance
Content gathered via agentic web research from public sources (arXiv, AMS, Wikipedia, university pages, Clay/AIM). Each file lists its sources at the end. For the most recent preprints (2024–2026), cross-check the source before citing in formal work.
