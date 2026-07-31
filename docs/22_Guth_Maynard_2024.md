---
id: doc-22
number: 22
title: "Guth–Maynard (2024): Breakthrough in Zero-Density Estimates"
category: breakthrough
status: proven
tags: [guth-maynard, zero-density, decoupling, dirichlet-polynomials, 2024]
source_file: 22_Guth_Maynard_2024.md
lang: en
---

# Guth–Maynard (2024): Breakthrough in Zero-Density Estimates

**Category:** Recent breakthrough (unconditional, not an RH proof)
**Authors / year:** Larry Guth & James Maynard, 2024
**Type:** Improved zero-density estimate
**Status:** ✅ Proven; the most important unconditional advance in decades — but NOT the RH

## Summary
In 2024 Larry Guth and James Maynard achieved the **first substantial improvement in over 80 years** of a classical zero-density estimate of Ingham (1940). Terence Tao publicly called this a "remarkable breakthrough". It is the most significant *unconditional* (RH-independent) advance in the RH area in decades — but it does **not** prove the RH.

## The result
- With N(σ, T) = number of ζ zeros with real part ≥ σ and imaginary part ≤ T (a measure of how many zeros *off* the critical line could lie in a height range).
- **Ingham (1940):** N(3/4, T) ≪ T^{3/5 + o(1)}. For over 80 years only the o(1) term improved, not the exponent.
- **Guth–Maynard (2024):** improvement of the **exponent itself** — in the range around σ = 3/4, bounds of order N(σ,T) ≪ T^{13/25 + o(1)} (13/25 = 0.52 < 3/5 = 0.6).

## Core idea / method
- New **Dirichlet-polynomial estimates** via **decoupling techniques** from harmonic analysis (related to the methods behind the resolution of the Vinogradov mean-value conjecture by Bourgain–Demeter–Guth).
- Import of tools from harmonic analysis / geometric measure theory into analytic number theory — described as a "paradigm shift".

## Significance / context
- **Why important:** zero-density estimates limit how many zeros could exist *at all* off the line, and feed directly into prime results (e.g. primes in short intervals) — **without** assuming the RH. Guth–Maynard thus improve unconditional statements about the distribution of the primes.
- **What it is NOT:** not a proof of the RH and no claim to be one. It only sharpens the density bounds in part of the critical strip.
- Revives hope that modern harmonic-analysis methods can improve further exponents (cf. density hypothesis, Doc. 17).

## Mathematical core (formulas, theorems, proof sketches)

### Counting/density function
N(σ, T) = #{ ρ = β + iγ : ζ(ρ) = 0, β ≥ σ, 0 ≤ γ ≤ T }. Under RH, N(σ,T) = 0 for σ > 1/2; unconditionally one seeks small upper bounds.

### Ingham's bound (1940) and the result
```
Ingham:        N(σ, T) ≪ T^{ 3(1−σ)/(2−σ) + o(1) }    ⇒  N(3/4, T) ≪ T^{3/5 + o(1)}.
Guth–Maynard:  N(σ, T) ≪ T^{ 30(1−σ)/13 + o(1) }       for  3/4 ≤ σ ≤ 1,
               ⇒  N(3/4, T) ≪ T^{30/13·1/4 + o(1)} = T^{15/26+o(1)} ≈ T^{0.577};
               in the key region they reach the exponent 13/25 = 0.52 at σ = 3/4.
```
(The central gain is the improvement 3/5 = 0.6 → 13/25 = 0.52 at σ = 3/4 — the first break in the exponent since Ingham 1940.)

### Reduction to large values of Dirichlet polynomials
As usual, the zero density translates (via zero-detecting polynomials, mean-value + large values) into a question about **large values of Dirichlet polynomials**
```
D(t) = Σ_{n ~ N} b_n n^{−it},   b_n bounded.
```
One must estimate how often (for well-separated t_r) |D(t_r)| can be large — a "large values" problem.

### New ingredient: decoupling
Guth–Maynard apply **ℓ² decoupling** (Bourgain–Demeter) to the frequencies log n: they split the frequency range into blocks and use quasi-orthogonality to control the ℓ^p norm of the large values by the sum of the blocks:
```
‖ Σ_θ D_θ ‖_{L^p}  ≲_ε  N^ε ( Σ_θ ‖D_θ‖_{L^p}² )^{1/2}    (decoupling inequality),
```
combined with a new geometric analysis of the set of "resonant" t_r. This beats the classical Montgomery/Halász large-values bound in this regime.

### Consequence for primes
Better N(σ,T) bounds ⇒ asymptotic prime counting in shorter intervals: Guth–Maynard unconditionally improve the length θ in "primes in [x, x + x^θ]" — concretely, results on primes in intervals of length x^{0.55+ε} (instead of previously larger exponents), independent of RH.

## Sources
- [Terence Tao on the Guth–Maynard breakthrough (Mathstodon)](https://mathstodon.xyz/@tao/112557248794707738)
- [The Riemann Hypothesis ... Is a Step Closer to Being Solved — Scientific American](https://www.scientificamerican.com/article/the-riemann-hypothesis-the-biggest-problem-in-mathematics-is-a-step-closer/)
- [New Horizons in Riemann Zeta Function Analysis: From Guth-Maynard Estimates ... (ResearchGate)](https://www.researchgate.net/publication/398421128_NEW_HORIZONS_IN_RIEMANN_ZETA_FUNCTION_ANALYSIS_FROM_GUTH-MAYNARD_ESTIMATES_TO_THE_GADU-IOMM_OPERATORIAL_PARADIGM)
- [The Riemann Hypothesis: Past, Present and a Letter Through Time (arXiv 2602.04022)](https://arxiv.org/abs/2602.04022)
