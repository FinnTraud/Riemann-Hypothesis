---
id: doc-32
number: 32
title: "Landau–Siegel Zeros (Exceptional Zeros) & Yitang Zhang (2022)"
category: solution-program
status: open
tags: [landau-siegel, exceptional-zeros, yitang-zhang, GRH, 2022]
source_file: 32_Landau_Siegel_zeros_Zhang.md
lang: en
---

# Landau–Siegel Zeros (Exceptional Zeros) & Yitang Zhang (2022)

**Category:** RH-adjacent solution field (exceptional zeros / GRH)
**Authors / years:** Landau, Siegel (1930s); Yitang Zhang (2022)
**Type:** Attack on potential counterexamples to the (G)RH
**Status:** Existence of Landau–Siegel zeros open; Zhang provides a strong (effective) bound

## Summary
A **Landau–Siegel zero** (exceptional zero) is a hypothetical real zero of a Dirichlet L-function *very close* to s = 1 — a potential counterexample to the Generalized Riemann Hypothesis (GRH, Doc. 21). Proving their **non-existence** is a central sub-goal on the way to the GRH/RH. Yitang Zhang (famous for the bounded prime gaps of 2013) presented a much-noticed preprint in 2022 that substantially advances the question.

## What is a Landau–Siegel zero?
- For a real primitive character χ mod D, L(s, χ) could have a real zero β very close to 1 (β = 1 − ε with tiny ε).
- Such a zero would contradict the GRH (which requires β = 1/2) and would "break through" the classical zero-free region (Doc. 12).
- Siegel's theorem excludes them, but **ineffectively** (the constant is not computable) — a notorious annoyance of analytic number theory.
- Equivalently: a Landau–Siegel zero exists exactly when (asymptotically) L(1, χ) is "too small".

## Yitang Zhang (2022): "Discrete mean estimates and the Landau–Siegel zero"
- **Result:** for real primitive χ mod D, L(1, χ) ≫ (log D)^{−2022}, with an **absolute, effectively computable** implied constant.
- **Method:** the lower bound for L(1, χ) is linked to the distribution of the zeros of a **family** of Dirichlet L-functions in a certain region (spacings of consecutive zeros). Evaluating certain **discrete mean values of large-sieve type** produces a contradiction if L(1, χ) were too small.
- The ~150-page preprint (arXiv 2211.02515) was intensively examined; it does not provide a complete exclusion of the exceptional zero, but a substantially stronger effective control than before.

## Significance / context
- Landau–Siegel zeros are the **most concrete potential counterexamples** in the (G)RH area; their exclusion is a realistic milestone with enormous consequences (class numbers, primes in progressions, twin-prime heuristics).
- Paradoxically, even the *existence* of a Siegel zero would have strong (partly GRH-like) consequences ("illusory world") — a much-studied phenomenon.
- Connects with density/zero-free estimates (Doc. 12, 17) and the GRH (Doc. 21).

## Mathematical core (formulas, theorems, proof sketches)

### Definition of the exceptional zero
For χ a real primitive character mod D, the classical zero-free region (Page/Landau) states: L(s,χ) ≠ 0 in
```
σ > 1 − c/log(D(|t|+2)),
```
**except** possibly for a single real, simple **Siegel zero** β with
```
β > 1 − c/log D.
```

### Equivalence Siegel zero ⟺ small L(1,χ)
Via the class number formula / mean-value relationship:
```
β near 1   ⟺   L(1, χ) small,   more precisely  1 − β  ≍  L(1,χ)/log D.
```
A lower bound for L(1,χ) keeps β away from 1.

### Siegel's (ineffective) theorem vs. effective bounds
```
Siegel (1935):  L(1,χ) ≫_ε D^{−ε}   — but the constant is NOT computable.
Classically effective (Goldfeld–Gross–Zagier area):  L(1,χ) ≫ (log D)^{−1}·(...)  only under additional assumptions.
```

### Yitang Zhang (2022) — the result
```
L(1, χ) ≫ (log D)^{−2022},   with an absolute, EFFECTIVELY computable constant.
```
Equivalently: every Siegel zero satisfies 1 − β ≫ (log D)^{−2023} (effectively).

### Proof strategy (sketch)
1. Link the lower bound for L(1,χ) with the **distribution of the zeros** of a family of Dirichlet L-functions L(s, ψ) in a region near s = 1; a Siegel zero forces anomalous zero clusters (Deuring–Heilbronn phenomenon: an exceptional zero repels other zeros).
2. Evaluate **discrete mean values of large-sieve type**:
```
Σ_{ψ mod Q}^* | Σ_{n ~ N} a_n ψ(n) |²  ≪  (Q + N) Σ |a_n|²,
```
over suitable families and weights (Zhang constructs special mollifiers/weights a_n).
3. If L(1,χ) were too small, then 1.+2. would give two incompatible estimates of the same discrete mean ⇒ **contradiction**.

### Meaning of the formulas
The effective bound is weaker than "no Siegel zero" (which would be 1−β ≫ 1/log D), but stronger and effective compared with Siegel. Excluding the Siegel zero would imply, among other things: GRH-like bounds for the least prime in progressions, class-number-1 problems, twin-prime constants.

## Sources
- [Discrete mean estimates and the Landau-Siegel zero — Y. Zhang (arXiv 2211.02515)](https://arxiv.org/abs/2211.02515)
- [Discrete mean estimates and the Landau-Siegel zero (PDF)](https://arxiv.org/pdf/2211.02515)
- [Landau–Siegel zero — Wikipedia](https://en.wikipedia.org/wiki/Landau%E2%80%93Siegel_zero)
- [Generalized Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)
