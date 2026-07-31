---
id: doc-13
number: 13
title: "The Nyman–Beurling Criterion & the Báez-Duarte Sharpening"
category: criterion
status: open
tags: [nyman-beurling, baez-duarte, density, hilbert-space]
source_file: 13_Nyman_Beurling_Baez_Duarte.md
lang: en
---

# The Nyman–Beurling Criterion & the Báez-Duarte Sharpening

**Category:** Equivalent criterion (functional-analytic)
**Authors / years:** Arne Beurling & Bertil Nyman (1950–1955), Luis Báez-Duarte (2003)
**Type:** Reformulation equivalent to the RH
**Status:** Equivalence proven; the required density is unproven

## Summary
The Nyman–Beurling criterion formulates the RH as an **approximation/density problem in a Hilbert space**: the RH holds if and only if a certain function space is dense in L²(0,1). Báez-Duarte simplified this considerably in 2003 by showing that only **integer** dilations are needed.

## The criterion
- Consider the space of square-integrable functions on (0,∞) resp. L²(0,1).
- **Nyman–Beurling (1955):** the RH is equivalent to the characteristic function of the interval (0,1] being approximable in quadratic mean by linear combinations of the **dilations of the fractional-part function** {θ/x} (θ ∈ (0,1)) — i.e. this function space is dense.
- In other words: RH ⟺ a certain vector lies in the closure of the linear span of countably many other vectors ("cyclic vector").

## Báez-Duarte's sharpening (2003)
- It suffices to restrict the dilations to **positive integers** a = 1, 2, 3, … (instead of all real θ).
- This makes the RH equivalent to the approximability of χ_{(0,1]} by linear combinations of the {1/(a·x)} with a ∈ ℕ — a significant reduction in complexity.
- There exist **probabilistic generalizations** (random dilation factors) that yield new criteria and partly overlap with the strong Báez-Duarte criterion.

## Significance / context
- Translates the RH entirely into the language of **functional analysis / approximation theory / operator theory** (density, cyclic vectors).
- Numerically: the partial sums of the approximation converge, but **extremely slowly** — no practical proof route, and the required density is unproven to this day.
- Related to the Hilbert-space approach of de Branges (Doc. 20) and Weil positivity (Doc. 14).

## Mathematical core (formulas, theorems, proof sketches)

### The functions and the space
Let {x} = x − ⌊x⌋ be the fractional part, ρ(x) = {1/x} for x ∈ (0,1). For θ ∈ (0,1) define the dilation
```
f_θ(x) = { θ/x } = ρ_θ(x),   x ∈ (0,1).
```
Let 𝒩 = closed linear span (in L²(0,1)) of { f_θ : 0 < θ < 1 }.

### Nyman–Beurling theorem (1955)
```
RH  ⟺  𝟙_{(0,1)} ∈ 𝒩      (the constant function 1 lies in the closure of 𝒩)
⟺  inf_{c_k, θ_k, N}  ‖ 1 − Σ_{k=1}^N c_k f_{θ_k} ‖_{L²(0,1)} = 0.
```
**Proof idea:** Mellin transform. For g ∈ L²(0,1), Ĝ(s) = ∫_0^1 g(x) x^{s−1} dx. The dilations f_θ generate, via the identity ∫_0^1 {θ/x} x^{s−1} dx = −(θ^s/s)·ζ(s)/(s−1)-type factors, a space whose orthogonal complement is trivial exactly when ζ(s) has no zeros with Re(s) > 1/2 (Beurling's theorem on invariant subspaces / the location of the zeros of ζ as an "inner function").

### Báez-Duarte sharpening (2003)
Restrict θ to the reciprocals of integers, θ = 1/k. With
```
A_N(x) = Σ_{k=1}^N c_k {k x}   (suitable coefficients c_k)
```
one has:
```
RH  ⟺  d_N := inf_{c} ‖ 1 − Σ_{k=1}^N c_k ρ_{1/k} ‖²_{L²}  →  0   (N → ∞).
```
Báez-Duarte–Balazard–Landreau–Saias also showed the **quantitative** conjecture:
```
d_N  ~  (Σ_ρ 1/|ρ|²) / log N   ≈  C / log N,
```
i.e. the convergence rate is (under RH, with simple zeros) ∝ 1/log N — extremely slow.

### Distance formula via the zeros
The optimal approximation distance has a representation via the non-trivial zeros:
```
liminf_{N→∞} (log N) · d_N  ≥  Σ_ρ m_ρ²/|ρ|²    (m_ρ = multiplicity),
```
which establishes the direct link distance ↔ location of the zeros.

## Sources
- [A general strong Nyman-Beurling Criterion for the Riemann Hypothesis (arXiv math/0505453)](https://arxiv.org/pdf/math/0505453)
- [New versions of the Nyman-Beurling criterion for the Riemann hypothesis — Báez-Duarte (Wiley)](https://onlinelibrary.wiley.com/doi/pdf/10.1155/S0161171202013248)
- [A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis (arXiv math/0202141)](https://arxiv.org/pdf/math/0202141)
- [On probabilistic generalizations of the Nyman-Beurling criterion (arXiv 1805.06733)](https://arxiv.org/pdf/1805.06733)
