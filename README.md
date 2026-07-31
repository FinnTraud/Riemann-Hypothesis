# Riemann-Hypothesis — Research & Knowledge Server

A complete toolkit to understand, visualize, try out approaches to, and investigate the
**Riemann Hypothesis (RH)** with an AI in a structured, analytical way. Three parts:

1. **Knowledge base** (`docs/`, 51 documents) — every approach, every criterion, every
   failed proof and every obstruction, each with its **mathematical core**
   (formulas, theorems, proof sketches) and sources.
2. **Knowledge graph + RAG** (`kb/`) — documents + concepts + atomic *claims* with status,
   connected by typed relations; hybrid search; as an **MCP server** with tools.
3. **Compute & visualize** (`kb/compute.py`, `kb/visualize.py`) — real ζ/zero
   computations (mpmath) and figures (matplotlib).

> **Honest disclaimer:** this repo *does not prove the RH* and cannot — nobody
> can so far. It is a **research, learning, and verification instrument** that
> enforces structured work and warns against known dead ends (see `docs/35`,
> `docs/43`, `docs/46`).

## What is the Riemann Hypothesis? (in one sentence)
The zeros of the Riemann ζ-function, which govern the distribution of the primes,
all lie — so the conjecture goes — exactly on the "critical line" Re(s) = 1/2.
Details: `docs/01`, `docs/02`, `docs/38`; terms: `docs/40_glossary_notation.md`.

## Quick start (for beginners)
```bash
# 1) Compute/plot libraries (once)
pip install -r kb/requirements.txt        # mpmath, numpy, matplotlib (+ optional mcp)

# 2) Build the index
python3 kb/build_kb.py

# 3) Guided tour (generates figures + an example experiment)
python3 kb/demo.py

# 4) Try it yourself (no installation, stdlib only for these)
python3 kb/query.py search "spectral operator" -k 5
python3 kb/query.py status refuted
python3 kb/query.py claim "Mertens"
python3 kb/query.py zero 1            # 1st zero: γ = 14.1347…
python3 kb/query.py scaffold "I want to prove the RH"
```

## As an AI tool (MCP server)
```bash
pip install "mcp[cli]"
python3 kb/server.py
```
The server provides **~26 tools**: search/graph/claims, reasoning protocol,
obstruction check, ζ/zero computation, plots, experiment logbook, and a
Lean verification tool. Registration & system prompt: `kb/README.md`.

## How the AI reasons in a structured, analytical way
Enforced by design (details: `docs/50_reasoning_protocol.md`):
- **Tool forcing** — numbers from `compute_*`, truth values from `get_claim` (status),
  relations from the graph. Nothing "from memory".
- **7-step protocol** (`reasoning_scaffold`) — make precise → classify →
  assumptions → separate status → **obstruction check** → experiment → honest conclusion.
- **Status separation** — every answer marks `[PROVEN] / [OPEN] / [EVIDENCE] / [HEURISTIC]`.
- **Anti-crackpot gate** — `evaluate_proof_idea` checks each proof idea against the known
  obstructions (Euler product required, don't assume positivity, no "soft" proof …).

## Directory
```
docs/                 51 knowledge documents (00_INDEX.md = entry point)
manifest.json         machine-readable index
README_RAG.md         ingestion/chunking notes for vector/MCP servers
kb/
  build_kb.py         builds the index
  core.py             search/graph/claims/scaffold (stdlib)
  query.py            CLI for testing
  server.py           MCP server (all tools)
  compute.py          ζ, Z(t), zeros, λ_n, ψ(x)  (mpmath)
  visualize.py        plots (matplotlib) -> kb/figures/
  experiment.py       reproducible experiment logbook -> kb/experiments/
  formal.py           Lean/mathlib bridge (formal verification)
  demo.py             guided tour
  graph/              curated nodes/edges/claims
  README.md           architecture & tool reference
Riemann_Hypothesis_Proof_Approaches.md   overall survey (one file, EN)
```

## Roadmap (together with a specialist/professor)
Realistic & valuable:
- **Numerical experiments** (λ_n positivity, BBLS distance, GUE statistics) — reproducible
  via the experiment logbook.
- **Formalizing partial results in Lean** (`docs/37`) — verified, publishable
  progress (e.g. Hardy, de-Bruijn–Newman Λ≥0).
- **Pushing an equivalent criterion computationally** (e.g. the Lapidus spectral operator `docs/44`).

Not achievable: a complete machine RH proof (the obstructions in `docs/35`,
`43`, `46` explain why this remains structurally hard).

## License / sources
Content from public sources (arXiv, AMS, Clay/AIM, Wikipedia, university pages),
cited at the end of each document. Numerics are **evidence, not proof**.
