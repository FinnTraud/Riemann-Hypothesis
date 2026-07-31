---
id: doc-16
number: 16
title: "Mertens Function & Riesz Criterion (Möbius-based criteria)"
category: criterion
status: open
tags: [mertens, mobius, riesz, mertens-conjecture-refuted]
source_file: 16_Mertens_function_Riesz_criterion.md
lang: en
---

# Mertens Function & Riesz Criterion (Möbius-based criteria)

**Category:** Equivalent criterion (Möbius / summatory)
**Authors / years:** Riesz (1916); Mertens connection classical; Mertens conjecture refuted by Odlyzko & te Riele (1985)
**Type:** Statements equivalent to the RH + an instructive counterexample
**Status:** Equivalences proven; the stronger Mertens conjecture REFUTED

## Summary
Several criteria express the RH via the **Möbius function** μ(n) and its summatory function. Especially instructive is the **refuted Mertens conjecture**: it would have implied the RH, but it is false — a warning against overly strong sufficient conditions.

## Mertens-function criterion
- Let M(x) = Σ_{n≤x} μ(n) be the summatory Möbius (Mertens) function.
- **RH-equivalent:** for every ε > 0, M(x) / x^{1/2 + ε} → 0 as x → ∞. (I.e. M(x) = O(x^{1/2+ε}).)
- This reflects 1/ζ(s) = Σ μ(n)/n^s: the growth order of M(x) is directly tied to the location of the zeros.

## The refuted Mertens conjecture (an important lesson)
- **Mertens conjecture:** |M(n)| < √n for all n. If it were true, the RH would follow (it is *stronger* than RH).
- **Refutation:** Andrew Odlyzko and Herman te Riele proved in 1985 that the Mertens conjecture is **false** (limsup M(x)/√x > 1, liminf < −1) — without giving an explicit counterexample n (the smallest known counterexample is extremely high, beyond 10^16, presumably around 10^{30}+).
- **Lesson:** a plausible "strengthening" of the RH, long supported numerically, can be false. Numerical evidence up to large bounds proves nothing — also relevant to the critical assessment of AI/data-driven RH "confirmations" (cf. Doc. 28).

## Riesz criterion (1916)
- Marcel Riesz gave a criterion equivalent to the RH via the growth of an infinite series formed with the Möbius function (the Riesz function). Related are the **Hardy–Littlewood criterion** and newer **Riesz-type criteria for the Selberg class** (Doc. 21).

## Significance / context
- Links the RH with the "randomness" of the signs of μ(n) (the multiplicative structure of the integers).
- The refuted Mertens conjecture is one of the most important **cautionary counterexamples** in the history of the RH.

## Mathematical core (formulas, theorems, proof sketches)

### Möbius function and 1/ζ
```
1/ζ(s) = Σ_{n=1}^∞ μ(n)/n^s   (Re s > 1),   μ(n) = (−1)^{#prime factors} if squarefree, else 0.
```
With Perron/Mellin, for M(x) = Σ_{n≤x} μ(n) one obtains the representation via the zeros of ζ:
```
M(x) ≈ Σ_ρ x^ρ/(ρ ζ'(ρ)) − 2 + Σ ...
```

### Mertens criterion
```
RH  ⟺  M(x) = O(x^{1/2 + ε})  for every ε > 0.
```
**Proof:** from M(x) = O(x^{Θ+ε}), Abel summation shows that 1/ζ(s) is analytic (zero-free) for Re(s) > Θ, so Θ ≥ sup_ρ Re(ρ). Conversely, RH (sup Re ρ = 1/2) gives, by contour shifting, M(x) ≪ x^{1/2+ε}.

### Mertens conjecture and its refutation
**Conjecture (stronger than RH):** |M(x)| < √x ∀x ≥ 1, i.e. m(x) := M(x)/√x ∈ (−1, 1).
**Theorem (Odlyzko–te Riele 1985):**
```
limsup_{x→∞} M(x)/√x  >  1.06     and     liminf_{x→∞} M(x)/√x  <  −1.009.
```
**Proof idea:** numerical evaluation of the first ~2000 zeros γ_n and of the sum Σ 2 Re( x^{iγ}/(½+iγ)ζ'(ρ) )·x^{−... } using a Diophantine-approximation argument (LLL lattice reduction) to force a resonance of many terms that drives m(x) above 1. No explicit counterexample x, but an existence proof. **Lesson:** the RH remains conjectured true, but the *stronger* bound |M|<√x is false — numerical evidence up to 10^{14} would have deceived.

### Riesz criterion (1916)
The Riesz function
```
P(x) = Σ_{k=1}^∞ (−1)^{k+1} x^k / ((k−1)! ζ(2k))
```
satisfies:
```
RH  ⟺  P(x) = O(x^{1/4 + ε})   for every ε > 0   (x → ∞).
```
(The Mellin transform of P involves Γ(s)/ζ(2s); the location of the zeros of ζ(2s) at Re = 1/4 yields the exponent.)

### Hardy–Littlewood criterion (related)
```
RH  ⟺  Σ_{n=1}^∞ (−x)^n/(n! ζ(2n+1)) = O(x^{−1/4})   (x → ∞).
```

## Sources
- [Criteria equivalent to the Riemann Hypothesis (arXiv 0808.0640)](https://arxiv.org/pdf/0808.0640)
- [Riemann's Hypothesis and the Mertens Function (Galetto)](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/galetto_RH_Mertens.pdf)
- [Riemann hypothesis — Wikipedia (Mertens function)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
- [Riesz type criteria for L-functions in the Selberg class (arXiv 2211.02954)](https://arxiv.org/pdf/2211.02954)
