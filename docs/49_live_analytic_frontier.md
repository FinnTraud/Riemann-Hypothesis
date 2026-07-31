---
id: doc-49
number: 49
title: "Live Frontier of Analytic Number Theory (2019–2026)"
category: frontier
status: open
tags: [zero-density, tao-program, nelson-subconvexity, harper-moments, 2024, active]
source_file: 49_live_analytic_frontier.md
lang: en
---

# Live Frontier of Analytic Number Theory (2019–2026)

**Category:** Current research frontier (unconditional advances)
**Authors / years:** Guth–Maynard (2024); Tao (zero-density program, 2024); Nelson (subconvexity, 2021); Harper, Radziwiłł–Soundararajan (moments, 2018–2022)
**Type:** Active, incremental advances (not an RH proof)
**Status:** Ongoing; unconditional results in the RH area

## Summary
Documents the *living* frontier at which unconditional progress is actually being made — beyond the Guth–Maynard breakthrough (Doc. 22). For an RH assistant this is the "newsfeed": where something is measurably moving.

## Mathematical core (results, formulas)

### Explicit & log-free zero-density estimates (2023–2025)
A wave of explicit sharpenings of the Ingham form:
```
N(σ, T) ≤ A · T^{B(1−σ)} (log T)^C   (log-free: C = 0),
```
with concrete constants A, B (e.g. arXiv 2405.12545, 2507.15184, 2311.05136). Application: explicit prime bounds, primes in short intervals — all **unconditional**.

### Tao's "outsourced" zero-density program (2024)
Tao systematized the reduction of zero-density bounds to **large-value estimates of Dirichlet polynomials** and outsourced parts to computer algebra / distributed verification. Connects Guth–Maynard decoupling (Doc. 22) with a reproducible estimation framework.

### Nelson: GL(n) subconvexity (2021)
Paul Nelson proved general **subconvex bounds** for GL(n) L-functions (with Venkatesh's methods / orbit integrals):
```
L(1/2, π) ≪ C(π)^{1/4 − δ}   (δ > 0),
```
where C(π) is the analytic conductor. Subconvexity is the unconditional approach to the Lindelöf hypothesis (Doc. 17) in high generality.

### Harper & sharp moment bounds (2018–2022)
- **Harper (2019):** "better than squareroot cancellation" for random multiplicative functions; a precise understanding of small moments (k < 1).
- **Radziwiłł–Soundararajan / Heap–Radziwiłł–Soundararajan:** sharp (conditional and partly unconditional) upper/lower bounds
```
M_k(T) = (1/T)∫_0^T |ζ(1/2+it)|^{2k} dt  ≍  T (log T)^{k²},
```
in agreement with Keating–Snaith (Doc. 07). Supports the random-matrix picture quantitatively.

### Transfer subconvexity ↔ moments (2022)
Functional-analytic implications between subconvexity bounds and moments in the right part of the critical strip (arXiv 2212.04421) — connects Doc. 07 and Doc. 17.

## Significance / context
- Here the **real, checkable progress** happens — mostly unconditional and thus permanent.
- None of these steps proves the RH; but together they narrow the "gap" (density, subconvexity, moments) and yield unconditional number-theoretic applications.
- Ideal as a regularly updated part of the MCP server (arXiv feeds on "zero-density estimate", "subconvexity", "moments of zeta").

## Sources
- [Terence Tao — zero-density program (Blog, 2024)](https://terrytao.wordpress.com/2024/07/07/)
- [An explicit log-free zero density estimate for the Riemann zeta-function (arXiv 2405.12545)](https://arxiv.org/pdf/2405.12545)
- [Implications between subconvexity and moments (arXiv 2212.04421)](https://arxiv.org/pdf/2212.04421)
- [P. Nelson — Bounds for standard L-functions (subconvexity for GL(n), arXiv 2109.15230)](https://arxiv.org/abs/2109.15230)
