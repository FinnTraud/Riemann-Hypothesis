---
id: doc-21
number: 21
title: "Generalized, Grand Riemann Hypothesis & the Selberg Class"
category: generalization
status: open
tags: [GRH, selberg-class, grand-RH, automorphic-L-functions, langlands]
source_file: 21_GRH_Selberg_class_grand_RH.md
lang: en
---

# Generalized, Grand Riemann Hypothesis & the Selberg Class

**Category:** Generalizations
**Authors / years:** Dirichlet/Hecke (L-functions), Atle Selberg (Selberg class, 1989/1992), Langlands (automorphic L-functions)
**Type:** Generalized conjectures
**Status:** All open; the classical RH is a special case

## Summary
The Riemann Hypothesis is the special case of a whole hierarchy of conjectures about the zeros of more general "zeta/L-functions". These generalizations are in some respects even more important from an applications standpoint (e.g. the GRH in algorithmic number theory).

## Generalized Riemann Hypothesis (GRH)
- Extends the RH to **Dirichlet L-functions** L(s, χ) for Dirichlet characters χ.
- **Statement:** all non-trivial zeros of *every* Dirichlet L-function have real part 1/2.
- **Applications:** under GRH follow, among others, bounds for the least quadratic non-residue, deterministic primality tests (Miller test), results on primes in arithmetic progressions.

## Selberg class (1989/1992)
- Selberg's **axiomatic** approach: instead of individual functions one defines a **class** of Dirichlet series via characterizing properties (Euler product, analytic continuation, functional equation, Ramanujan condition).
- For all functions of this class an RH analogue is expected ("RH for the Selberg class").
- There exist Riesz-type and Li-type criteria specifically for the Selberg class (cf. Doc. 14, 16).

## Grand Riemann Hypothesis (Grand RH, GRH)
- **Most general version:** all non-trivial zeros of *all* **automorphic L-functions** (Mellin transforms of Hecke eigenforms, etc.) lie on the critical line.
- Generalizes both the classical RH and the GRH for Dirichlet L-functions.

## Connection / open structural problem
- It is conjectured that the **Selberg class = the class of automorphic L-functions** — in which case "RH for the Selberg class" and "Grand RH" would be equivalent. This equality is itself an important open problem and part of the **Langlands program**.

## Significance / context
- Shows that the RH is not an isolated phenomenon but part of a universal pattern across a whole world of L-functions.
- Random-matrix statistics (Katz–Sarnak) predict different symmetry types (unitary, symplectic, orthogonal) for *families* of L-functions — strong cross-structural evidence.
- Practically: many number-theoretic/algorithmic results depend on GRH, not just on the classical RH.

## Mathematical core (formulas, theorems, proof sketches)

### Dirichlet L-functions (GRH)
For a Dirichlet character χ mod q:
```
L(s, χ) = Σ_{n=1}^∞ χ(n)/n^s = ∏_p (1 − χ(p) p^{−s})^{−1}   (Re s > 1).
```
**GRH:** all non-trivial zeros of L(s,χ) (for every primitive χ) have Re(s) = 1/2.

### Axioms of the Selberg class 𝒮
A Dirichlet series F(s) = Σ a_n n^{−s} belongs to 𝒮 if:
1. **Ramanujan condition:** a_n ≪_ε n^ε.
2. **Analytic continuation:** (s−1)^m F(s) entire for some m ≥ 0.
3. **Functional equation:** Φ(s) = Q^s ∏_j Γ(λ_j s + μ_j) F(s) satisfies Φ(s) = ω Φ̄(1 − s̄), |ω| = 1.
4. **Euler product:** log F(s) = Σ_n b_n n^{−s} with b_n = 0 except for prime powers, b_n ≪ n^θ (θ < 1/2).
Defining invariants: **degree** d_F = 2 Σ_j λ_j (conjectured always ∈ ℤ_{≥0}); examples: ζ (degree 1), L(s,χ) (degree 1), automorphic L (degree n).

### RH for the Selberg class
```
For all F ∈ 𝒮, all non-trivial zeros lie on Re(s) = 1/2.
```

### Automorphic L-functions (Grand RH)
For an automorphic representation π of GL_n(𝔸_ℚ):
```
L(s, π) = ∏_p ∏_{i=1}^n (1 − α_{i,p} p^{−s})^{−1}.
```
**Grand RH:** all non-trivial zeros of L(s,π) on Re(s) = 1/2 (for all π).

### Structural hierarchy & open identity
```
{Dirichlet/Hecke-L} ⊂ {automorphic L-functions} ⊆? Selberg class 𝒮.
```
Conjecture (part of the Langlands program): 𝒮 = {automorphic L-functions}. Known: elements of 𝒮 of degree 0 are the constant 1; degree strictly between 0 and 1 does not exist (Conrey–Ghosh / Kaczorowski–Perelli classification of low degrees).

### Katz–Sarnak symmetry types (random matrix, Doc. 06/07)
Families of L-functions show different low-zero statistics according to their symmetry:
```
unitary (U)  →  ζ, Dirichlet-L;   symplectic (USp)  →  quadratic L;   orthogonal (O)  →  elliptic-curve L.
```
This cross-structural universality is strong evidence for the Grand RH.

## Sources
- [Generalized Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)
- [Grand Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Grand_Riemann_hypothesis)
- [On relations equivalent to the generalized Riemann hypothesis for the Selberg class (arXiv 1511.04603)](https://arxiv.org/pdf/1511.04603)
- [Equivalent criteria for the Riemann hypothesis for a general class of L-functions (arXiv 2409.17708)](https://arxiv.org/pdf/2409.17708)
