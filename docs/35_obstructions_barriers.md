---
id: doc-35
number: 35
title: "Obstructions & Barriers: Why Naive Approaches MUST Fail"
category: obstruction
status: meta
tags: [obstructions, davenport-heilbronn, parity-problem, mertens-warning, skewes, checklist]
source_file: 35_obstructions_barriers.md
lang: en
---

# Obstructions & Barriers: Why Naive Approaches MUST Fail

**Category:** Meta / negative results (crucial for "bulletproof")
**Authors / years:** Davenport–Heilbronn (1936); Bombieri; Ivić ("Reasons for doubting", 2003); various
**Type:** Known obstacles that every proof attempt must overcome
**Status:** Established negative results / warning signs

## Summary
This document collects the **known reasons why entire classes of proof approaches cannot work**. For an RH assistant this is the most important "protective layer": it makes it possible to test proposed proof ideas immediately against known obstructions and to recognize dead ends.

## 1. The Davenport–Heilbronn function — the "almost-ζ" counterexample
**Fact (Davenport–Heilbronn 1936).** There is a Dirichlet series f(s) that
- satisfies a **functional equation** of ζ type (s ↔ 1−s),
- has an analytic continuation,
- has **infinitely many zeros on** the critical line,
- but **also has zeros OFF** the line (even in the region Re(s) > 1) — so the RH analogue is FALSE.

### Construction (formula)
With a non-principal character mod 5 and a phase ξ, one takes
```
f(s) = (1 − i τ)/2 · L(s, χ) + (1 + i τ)/2 · L(s, χ̄),   τ = (√(10 − 2√5) − 2)/(√5 − 1),
```
a linear combination of two Dirichlet L-functions with a common functional equation.

### The decisive lesson: the Euler product is indispensable
f(s) has **no Euler product** (the linear combination of two L-functions is no longer multiplicative). **Consequence:**
> Every RH proof that uses only functional equation + analytic continuation + growth behavior MUST fail — because f would have the same properties but violates the RH. A valid proof must use the **Euler product** (multiplicativity / prime structure) ESSENTIALLY.

This is the sharpest known obstruction. It immediately disqualifies many "elementary" and purely function-theoretic proof attempts (cf. Doc. 27).

## 2. The Selberg-class bound
In the Selberg class (Doc. 21), the RH is expected only for functions **with an Euler product**. Functions of degree 1 without an Euler product (like Davenport–Heilbronn) are counterexamples. ⇒ every proof must be able to distinguish "with" from "without" an Euler product.

## 3. The parity problem (sieve methods)
Classical sieve methods (Brun, Selberg) can **in principle** not distinguish between numbers with an even and an odd number of prime factors (the parity barrier, Selberg). Since the Möbius function μ(n) = (−1)^{Ω(n)} measures exactly this parity and 1/ζ = Σ μ(n)/n^s, pure sieve arguments cannot provide the control over M(x) (Doc. 16) needed for the RH.

## 4. Reasons for doubting (Ivić 2003) — beware of "too beautiful" evidence
- **Mertens conjecture refuted** (Doc. 16): |M(x)| < √x seems to hold up to 10^{14}, but is false. Numerics deceive.
- **Skewes number:** π(x) < Li(x) holds for all computable x, but reverses at ~10^{316} (Littlewood: both signs infinitely often). ⇒ "computer confirmation up to 10^{N}" proves nothing.
- **S(T) growth:** the argument term S(T) (Doc. 02) is small on average but (under RH) becomes unbounded — very high zeros could show unexpected behavior invisible at today's heights.
- Very close zero pairs (**Lehmer pairs**, Doc. 23) show that the RH (if true) holds only "narrowly" — no comfortable margin.

## 5. Why spectral approaches are not "free"
- A Hilbert–Pólya operator (Doc. 05) must arise **canonically from arithmetic**; to "invent" an ad-hoc operator with spectrum {γ_n} proves nothing (one can produce a self-adjoint operator for any real sequence — circular if one already assumes reality). This is exactly the gap in Bender–Brody–Müller (Doc. 09).
- Connes' program circumvents this by requiring the positivity to be shown *independently* — and exactly that is open (Doc. 10).

## Checklist for proposed proofs (anti-crackpot filter)
1. **Does the proof use the Euler product essentially?** If no → almost certainly wrong (Davenport–Heilbronn).
2. **Would the same argument apply to an L-function without an Euler product?** If yes → wrong.
3. **Is positivity (Li/Weil/de Branges) assumed or proven?** Assumed → circular (Doc. 14, 20).
4. **Does the evidence rest only on finite numerics?** → not a proof (Mertens, Skewes).
5. **Does the proof interchange limit/sum over the non-absolutely-convergent zero sum?** → error (Doc. 27).

## Sources
- [Zeros of the Davenport-Heilbronn Counterexample (AMS Math. Comp.)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)
- [On some reasons for doubting the Riemann hypothesis — A. Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- [On Davenport and Heilbronn-Type of Functions (arXiv 1602.06328)](https://arxiv.org/abs/1602.06328)
- [The Riemann Hypothesis — E. Bombieri (Clay official problem description)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
