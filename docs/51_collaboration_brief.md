---
id: doc-51
number: 51
title: "Collaboration Brief: working meaningfully with a specialist on the RH"
category: meta
status: meta
tags: [collaboration, open-problems, research-program, professor, experiments, formalization]
source_file: 51_collaboration_brief.md
lang: en
---

# Collaboration Brief: working meaningfully with a specialist/professor on the RH

**Category:** Meta / research organization
**Purpose:** Concrete, realistic sub-projects that make a *genuine, checkable* contribution with
the tools of this repo — without the unrealistic claim of a complete RH proof.

## Basic stance (honest)
A complete RH proof is not the realistic goal of a student/seminar project or an AI tool
(see docs/35, 41, 46). **Valuable and achievable** are: reproducible numerical experiments,
formal verification of partial results, and the computational exhaustion of criteria *equivalent
to the RH*. The tools are built for exactly this.

## Three realistic project classes

### Class A — numerical/experimental mathematics (doable immediately)
Tools: `compute_*`, `plot_*`, `research/spacing_vs_gue.py`, the experiment logbook.
Examples:
1. **Quantify the Montgomery–Odlyzko law** (docs/06): spacing statistics vs. GUE — already
   present as a flagship experiment (`kb/research/spacing_vs_gue.py`). Extendable to
   higher correlations, larger heights, other L-functions.
2. **Li coefficients** (docs/14): test λ_n positivity + the growth λ_n ~ ½ n log n; analyze
   deviations. Question: from which n does the approximation (number of zeros) break down?
3. **Explicit formula** (docs/02): the convergence of ψ(x) to the true prime summation as a
   function of the number of zeros — empirically determine the error-term scaling.
4. **S(T) statistics** (docs/02): numerically check the distribution of the argument term S(T)
   as T grows (Selberg CLT: S(T)/√(½ log log T) → normal distribution).

### Class B — formal verification in Lean (with a professor, high value)
Tools: `kb/lean/`, `formal_statement`, `lean_check` (docs/37).
Examples:
1. Formally write down a **criterion equivalent to the RH** (Λ≤0 docs/23; Li positivity docs/14;
   Robin docs/15) and prove the equivalence to the standard statement.
2. Formalize **proven partial results**: Hardy (∞ many zeros, docs/03), Rodgers–Tao
   Λ≥0 (docs/23). Every gaplessly checked proof is publishable progress.
3. Even the **definitions** cleanly in mathlib style (ξ-function, N(T), Li coefficients) are
   a contribution that others can build on.

### Class C — computationally exhaust an equivalent criterion
Examples:
1. **Báez-Duarte distance** d_N (docs/13/45): compute numerically and check the conjectured rate
   d_N² ~ (2+γ−log 4π)/log N — a very "tangible" goal with a concrete constant.
2. **Finite-dimensional Weil positivity** (docs/14): set up the quadratic form on a
   finite function space and track its smallest-eigenvalue bound.
3. **Lapidus spectral operator** (docs/44): the quasi-invertibility in model cases, numerically.

## Procedure (with the 7-step protocol, docs/50)
1. Formulate the question precisely + falsifiably (`reasoning_scaffold`).
2. Classify into a leitmotiv (A/B/C, docs/41) and pull related docs (`graph_neighbors`).
3. Clarify assumptions + status (`get_claim`).
4. **Obstruction check** (`evaluate_proof_idea`) — mandatory for any "proof" claim.
5. Run the experiment (`compute_*`/`plot_*`) and **log it** (`log_experiment`).
6. Assess the result honestly: evidence vs. proof; the next testable step.

## What you can present to the professor
- Reproducible experiment notes (`kb/experiments/*.md`) with hypothesis/method/result.
- Figures (`kb/figures/*.png`).
- A Lean project scaffold (`kb/lean/`) that builds locally.
- This knowledge base as a map of the state of research (docs/00_INDEX.md, docs/42 reading list).

## Clear limits (anti-crackpot)
- No "proof" without a passed obstruction check (docs/35) and without using the Euler product
  (docs/43). Numerics are never a proof (docs/35: Mertens/Skewes).
- Before submission/publication: observe peer standards (docs/27).

## Sources / references
docs/41 (synthesis), docs/35/43/46 (obstructions), docs/37 (Lean), docs/06/14/23 (experiment fields),
docs/50 (reasoning protocol).
