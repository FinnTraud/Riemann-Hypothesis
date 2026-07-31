---
id: doc-23
number: 23
title: "The De Bruijn–Newman Constant: Rodgers–Tao & Polymath15"
category: breakthrough
status: open
tags: [de-bruijn-newman, rodgers-tao, polymath15, lehmer-pairs]
source_file: 23_de_Bruijn_Newman_constant_Polymath15.md
lang: en
---

# The De Bruijn–Newman Constant: Rodgers–Tao & Polymath15

**Category:** Recent progress (RH "on a knife's edge")
**Authors / years:** de Bruijn (1950), Newman (1976), Brad Rodgers & Terence Tao (2018), Polymath15 (2018–2019)
**Type:** Quantitative "how narrowly does the RH hold?" result
**Status:** ✅ Λ ≥ 0 proven (Rodgers–Tao); Λ ≤ 0.22 (Polymath15); RH ⟺ Λ ≤ 0

## Summary
The **De Bruijn–Newman constant Λ** quantifies "how narrowly" the RH holds. It is known that the **RH is equivalent to Λ ≤ 0**. In 2018 Rodgers and Tao proved the reverse bound **Λ ≥ 0**. Together this means: **if the RH is true, it is only just barely true** (Λ = 0 exactly). The subsequent Polymath15 project pushed the upper bound down to Λ ≤ 0.22.

## Core idea
- One deforms the Riemann ξ-function by a heat/diffusion parameter t: for each real parameter t an entire function H_t arises, whose zeros one tracks.
- de Bruijn and Newman showed: there is a constant Λ such that H_t has **only real zeros** (= RH analogue) exactly when t ≥ Λ.
- At t = 0, H_0 is essentially the ξ-function ⇒ **RH ⟺ Λ ≤ 0**.
- Newman conjectured in 1976 the complementary inequality **Λ ≥ 0** ("the RH, if true, is only just barely true").

## The results
- **Rodgers–Tao (2018, "The de Bruijn–Newman constant is non-negative"):** proof of **Λ ≥ 0** (Newman's conjecture). Published in *Forum of Mathematics, Pi* (2020). Idea: if Λ < 0, the zeros would have a "too ordered" dynamics contradicting the known GUE-type statistics (Doc. 06).
- **Polymath15 (2018–2019, an open online collaboration project initiated by Tao):** improved the **upper** bound (classically de Bruijn: Λ ≤ 1/2) to **Λ ≤ 0.22**, by combining analytic estimates with extensive computation.

## Significance / context
- Provides a **quantitative view** of the RH: it is (if true) true "on a knife's edge" — Λ = 0 exactly.
- Λ ≥ 0 gives the RH a conceptual explanation: the zeros are "smeared out" exactly as far as is still compatible with reality.
- A model for **Polymath collaboration** (massively parallel, open mathematics) and human–computer cooperation.
- **Not** a proof of the RH (that would be Λ ≤ 0); the gap 0 ≤ Λ ≤ 0.22 would have to be closed to Λ ≤ 0.

## Mathematical core (formulas, theorems, proof sketches)

### The deformed family H_t
Write the ξ-function as the Fourier transform of a positive even function:
```
ξ(1/2 + iz) = (1/2) ∫_{−∞}^∞ Φ(u) e^{izu} du,   Φ(u) = Σ_{n=1}^∞ (2π²n⁴ e^{9u} − 3πn² e^{5u}) exp(−πn² e^{4u}) > 0.
```
Deform with a heat parameter t:
```
H_t(z) = ∫_{−∞}^∞ e^{t u²} Φ(u) e^{izu} du.
```
H_0 is (up to normalization) ξ. H_t satisfies the backward heat equation ∂_t H = −∂_{zz} H; the zeros z_k(t) move according to a gradient flow.

### Definition of the constant Λ
**Theorem (de Bruijn 1950 / Newman 1976).** There is Λ ∈ ℝ with:
```
H_t has only real zeros   ⟺   t ≥ Λ.
```
Since H_0 = ξ, it follows:
```
RH  ⟺  Λ ≤ 0.
```
de Bruijn showed Λ ≤ 1/2; Newman conjectured Λ ≥ 0.

### Rodgers–Tao (2018): Λ ≥ 0
**Proof idea (contradiction).** If Λ < 0, then the zeros would already be real for some t < 0 and would, under the flow to t = 0, take on a *too regular* distribution: one shows that the zeros would then lie asymptotically in nearly arithmetic progression (spacings more uniform than allowed). This contradicts the known **pair-correlation / Montgomery statistics** (Doc. 06), which require level repulsion *and* fluctuations. Formally: a quantity (averaged zero dynamics) would have to be simultaneously → 0 and ≥ c > 0. ⇒ Λ ≥ 0.

### Polymath15 (2019): upper bound Λ ≤ 0.22
Strategy: show H_t(x+iy) ≠ 0 for y > 0 and all x once t ≥ 0.2 and the height is large enough; for low heights, numerical verification that no **Lehmer pairs** (extremely close zeros) endanger reality. Tools:
```
- Newton's inequalities / approximation of H_t by an effectively computable A+B−C model,
- explicit bounds on the quotient H_t'/H_t,
- mollified barrier arguments + large-scale computation.
```
Result: **0 ≤ Λ ≤ 0.22**.

### Interpretation
Λ = 0 (RH) means: the ξ zeros are "on the edge" of being real — any infinitesimal backward heat flow (t < 0) would immediately produce complex zeros. Lehmer pairs (e.g. near γ ≈ 7005) are the empirical witnesses of this narrowness.

## Sources
- [The De Bruijn-Newman constant is non-negative — Terence Tao (Blog)](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/)
- [The de Bruijn–Newman constant is non-negative — Forum of Mathematics, Pi (Cambridge)](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/de-bruijnnewman-constant-is-nonnegative/D4B85BA067E2D5A71D87E4FFB0D21E46)
- [De Bruijn-Newman constant — Polymath Wiki](https://michaelnielsen.org/polymath/index.php?title=De_Bruijn-Newman_constant)
- [de Bruijn–Newman constant — Wikipedia](https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant)
