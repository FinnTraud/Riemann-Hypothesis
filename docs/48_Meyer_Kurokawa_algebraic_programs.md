---
id: doc-48
number: 48
title: "Further Algebraic/Spectral Programs: Meyer (Distributions) & Kurokawa (Absolute Zeta)"
category: solution-program
status: open
tags: [meyer, distributions, kurokawa, absolute-zeta, tensor-product, F1]
source_file: 48_Meyer_Kurokawa_algebraic_programs.md
lang: en
---

# Further Algebraic/Spectral Programs: Meyer (Distributions) & Kurokawa (Absolute Zeta)

**Category:** Algebraic/spectral approach (supplement to Doc. 10, 30, 31)
**Authors / years:** Ralf Meyer (2005); Nobushige Kurokawa (absolute mathematics, 1990s–2000s)
**Type:** Alternative spectral resp. 𝔽₁-adjacent programs
**Status:** Open; partly rigorous spectral realization (Meyer), partly programmatic (Kurokawa)

## Summary
Two further serious programs alongside Connes (Doc. 10), 𝔽₁ (Doc. 30), and Deninger (Doc. 31): **Meyer's** functional-analytic, distributional spectral realization of the zeros and **Kurokawa's** "absolute" zeta functions with multiplicative (tensor) structure over 𝔽₁.

## Mathematical core (constructions, formulas)

### Meyer: spectral interpretation via distributions (2005)
Meyer realizes the non-trivial zeros as the **spectrum of an operator on a space of distributions** on the adele-class group — a rigorous, purely functional-analytic variant of Connes' program that manages **without** the RH hypothesis and reproduces Weil's explicit formula as a trace formula.
```
Idea:  consider the quotient  𝔸_ℚ^× / ℚ^×  and the scaling action;
zeros ρ  ↔  generalized eigenvalues (distributions) of the generator;
explicit formula  =  trace formula on this space of distributions.
```
Difference from Connes: Meyer works with **bornological / nuclear** spaces and avoids the Sobolev-cutoff construction; the RH remains equivalent to a positivity, but is embedded more cleanly.

### Kurokawa: absolute zeta & tensor products over 𝔽₁
Kurokawa's "absolute mathematics" defines **absolute tensor products** ζ_1 ⊗ ζ_2 of zeta functions such that zeros/poles combine additively:
```
(ζ_1 ⊗ ζ_2)  has "zeros"  ρ_1 + ρ_2 − (shift),
```
motivated by the wish to realize "Spec(ℤ) ×_{𝔽₁} Spec(ℤ)" zeta-functionally (cf. the transfer of Weil's proof, Doc. 18/30). The **absolute zeta function** ζ_{X/𝔽₁}(s) is obtained from the point counts #X(𝔽_q) via a "limit q→1" procedure. In this framework the sought positivity appears as a property of the tensor product ζ ⊗ ζ.

## Significance / context
- **Meyer:** technically the cleanest variant of the Connes spectral realization; useful because it decouples the construction from the RH and isolates the remaining hurdle (positivity).
- **Kurokawa:** provides the multiplicative/tensor structure that an 𝔽₁ proof (Doc. 30) would need to reproduce Weil's C×C argument.
- Both share the core obstruction: the decisive positivity/geometry over ℤ is not established (Doc. 35, 41).

## Sources
- [R. Meyer — On a representation of the idele class group related to primes and zeros of L-functions (Duke Math. J. 2005 / arXiv math/0311468)](https://arxiv.org/abs/math/0311468)
- [A spectral interpretation for the zeros of the Riemann zeta function (arXiv math/0412277)](https://arxiv.org/pdf/math/0412277)
- [N. Kurokawa — Absolute tensor products / absolute zeta functions (overview in: Deninger-program literature)](https://arxiv.org/pdf/math/0505354)
