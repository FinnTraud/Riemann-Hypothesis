---
id: doc-17
number: 17
title: "Lindelöf Hypothesis & Density Hypothesis"
category: analytic
status: open
tags: [lindelof, density-hypothesis, subconvexity, mu-exponent]
source_file: 17_Lindelof_density_hypothesis.md
lang: en
---

# Lindelöf Hypothesis & Density Hypothesis

**Category:** Weaker consequences / related hypotheses
**Authors / years:** Ernst Lindelöf (1908); density estimates Ingham, Huxley, Bourgain, Guth–Maynard
**Type:** Hypotheses (weaker) that follow from the RH
**Status:** Both open; partial progress (subconvexity, density estimates)

## Summary
The Lindelöf and density hypotheses are **consequences** of the RH that are formally weaker but likewise unsolved. They form a hierarchy:

```
RH  ⟹  Lindelöf hypothesis  ⟹  density hypothesis
```

Whether, conversely, the Lindelöf hypothesis implies the RH is **unknown** (presumably not). Progress here yields unconditional (RH-independent) results.

## Lindelöf hypothesis (1908)
- A statement about the **growth** of ζ on the critical line:

```
ζ(1/2 + it) = O(t^ε)   for every ε > 0   (t → ∞)
```

- Equivalently, via the **Lindelöf μ-exponent**: μ(1/2) = 0, where μ(σ) is the infimum of the exponents with ζ(σ+it) = O(t^{μ(σ)+ε}).
- **State of subconvexity:** the convex bound gives μ(1/2) ≤ 1/4; **Bourgain (2017)** improved it to μ(1/2) ≤ **13/84** ≈ 0.1548 — far from the conjectured value 0. (Related: Weyl, Hardy–Littlewood, van der Corput, Huxley 32/205.)
- Note: a "Lindelöf hypothesis for primes" was shown (2019/2020) to be even *equivalent* to the RH — but the standard Lindelöf hypothesis remains weaker.

## Density hypothesis
- A statement about the **number of possible zeros off** the critical line. With N(σ,T) = number of zeros with Re ≥ σ and |Im| ≤ T:

```
N(σ, T) = O_ε( T^{2(1−σ) + ε} )   for 1/2 ≤ σ ≤ 1
```

- Under RH there would be no such zeros at all for σ > 1/2; the density hypothesis is a quantitative weakening.
- **Progress:** explicit log-free density estimates (e.g. arXiv 2405.12545), Ingham, Huxley, and in particular the **Guth–Maynard breakthrough (2024)** for σ near 3/4 (Doc. 22).

## Significance / context
- Density estimates replace the RH in many applications (primes in short intervals, primes in arithmetic progressions) — **unconditionally**, i.e. without assuming RH.
- The most important *practical* frontier: even without a proof of the RH, better density/subconvexity bounds yield concrete number-theoretic results.

## Mathematical core (formulas, theorems, proof sketches)

### The μ-exponent
Define μ(σ) = inf{ a ≥ 0 : ζ(σ + it) = O(|t|^a) }. Known:
- μ(σ) = 0 for σ > 1; μ(σ) = 1/2 − σ for σ < 0 (from the functional equation + Stirling).
- μ is convex and non-increasing. Convexity bound (Phragmén–Lindelöf): μ(1/2) ≤ 1/4.

### Lindelöf hypothesis
```
LH:  μ(1/2) = 0,   i.e.  ζ(1/2 + it) = O(|t|^ε)  ∀ε > 0.
```
**Subconvexity progress (each μ(1/2) ≤ …):** Weyl/Hardy–Littlewood 1/6 ≈ 0.1667; van der Corput; Titchmarsh; Huxley 32/205 ≈ 0.15610; **Bourgain (2017) 13/84 ≈ 0.15476**. Goal 0.

### Equivalence LH ⟺ moment growth
```
LH  ⟺  (1/T)∫_0^T |ζ(1/2+it)|^{2k} dt = O(T^ε)  for every fixed k ≥ 1.
```
(cf. Keating–Snaith (log T)^{k²}, Doc. 07 — compatible, since T^ε dominates any power-of-log growth.)

### Hierarchy and implications
```
RH  ⟹  LH  ⟹  density hypothesis (DH).   (Reverse directions unknown.)
```
Proof RH ⇒ LH: under RH, log|ζ(1/2+it)| ≤ (c log t)/log log t, so ζ(1/2+it) = O(exp(c log t/log log t)) = O(t^ε).

### Density hypothesis
With N(σ,T) = #{ρ = β+iγ : β ≥ σ, 0 < γ ≤ T}:
```
DH:  N(σ, T) ≪_ε T^{2(1−σ) + ε}   for  1/2 ≤ σ ≤ 1.
```
Classical (Ingham 1940): N(σ,T) ≪ T^{3(1−σ)/(2−σ)+ε}. **Log-free** form: N(σ,T) ≪ A·T^{B(1−σ)}. Guth–Maynard (2024, Doc. 22) improve the exponent near σ = 3/4 (N(3/4,T) ≪ T^{13/25+o(1)} instead of T^{3/5+o(1)}).

### Why the DH is enough in practice
For primes in short intervals [x, x+x^θ], a sufficiently strong density estimate (instead of RH) suffices to secure asymptotic prime counting — the reason density results have *unconditional* number-theoretic applications.

## Sources
- [Lindelöf hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis)
- [An explicit log-free zero density estimate for the Riemann zeta-function (arXiv 2405.12545)](https://arxiv.org/pdf/2405.12545)
- [Explicit zero density for the Riemann zeta function (arXiv 2101.12263)](https://arxiv.org/pdf/2101.12263)
- [An explicit form of Ingham's zero density estimate (arXiv 2507.15184)](https://arxiv.org/pdf/2507.15184)
