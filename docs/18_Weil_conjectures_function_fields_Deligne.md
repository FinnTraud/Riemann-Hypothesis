---
id: doc-18
number: 18
title: "Weil Conjectures: RH over Finite Fields (Deligne) — PROVEN"
category: proven-analogue
status: proven
tags: [weil-conjectures, deligne, function-fields, finite-fields, etale-cohomology]
source_file: 18_Weil_conjectures_function_fields_Deligne.md
lang: en
---

# Weil Conjectures: RH over Finite Fields (Deligne) — PROVEN

**Category:** Proven analogue (algebraic/geometric)
**Authors / years:** Emil Artin (1920s), Helmut Hasse (1930s), André Weil (1940s), Bernard Dwork (1960), Alexander Grothendieck (1965), Pierre Deligne (1974)
**Type:** Fully PROVEN analogue of the RH
**Status:** ✅ Proven — the most important "success story" and model

## Summary
For **curves (and more generally varieties) over finite fields** there exists an exact analogue of the Riemann Hypothesis — and it is **completely proven**. This is the greatest triumph of the "RH family" and the most important model/guiding light for attacks on the classical RH (in particular Connes' program, Doc. 10).

## Core idea
- To a smooth projective curve C over the finite field 𝔽_q one associates a **congruence zeta function** Z(C, t) that replaces primes by closed points / prime divisors of the curve.
- This zeta function is a **rational function**, satisfies a **functional equation**, and its zeros satisfy an **RH analogue**: the "zeros" have absolute value q^{1/2} — the exact counterpart of "real part 1/2".

## The Weil conjectures and their proof
Weil formulated (modeled on Riemann) three conjectures that were proven one after another:
1. **Rationality** of the zeta function — Dwork (1960).
2. **Functional equation** — Grothendieck (1965, via étale cohomology).
3. **Riemann-hypothesis analogue** (location/absolute value of the zeros) — **Deligne (1974)**.

- **Weil's own proof (1940s)** for curves used classical **intersection theory** on the surface C × C (correspondences, positive-definiteness of the intersection form — a positivity / Hodge-index idea).
- **Deligne's proof (1974)** for general varieties uses **étale cohomology**, monodromy of Lefschetz pencils, and cleverly circumvents the (then unproven) standard conjectures. (Deligne received, among other honors, the Fields Medal; Weil II 1980 generalized the result further.)

## Significance / context for the classical RH
- **Proof of feasibility:** an RH-type statement *can* be proven — if one has the right geometry/cohomology.
- **Strategic model:** one would like the classical RH (over ℚ / ℤ) as "geometry over the hypothetical field with one element 𝔽₁" or over Spec(ℤ) — exactly what motivates Connes–Consani (Doc. 10/11) and arithmetic-geometry programs.
- **Key ingredient positivity:** both Weil's and Deligne's approaches rest on positivity/intersection arguments — reflected in the Weil positivity of the classical RH (Doc. 14).
- **Important caveat:** over ℤ the analogous geometric/cohomological structure is still missing — the transfer is *the* open task.

## Mathematical core (formulas, theorems, proof sketches)

### Congruence zeta function of a curve over 𝔽_q
For a smooth projective curve C/𝔽_q of genus g, let N_m = #C(𝔽_{q^m}). Define
```
Z(C, t) = exp( Σ_{m=1}^∞ N_m t^m / m )   =   ∏_{x closed point} (1 − t^{deg x})^{−1}.
```
The product over points is the exact analogue of the Euler product (points ↔ primes). With t = q^{−s} one obtains ζ_C(s) = Z(C, q^{−s}).

### Rationality & functional equation (Dwork, Weil)
```
Z(C, t) = P(t) / ((1 − t)(1 − q t)),   P(t) = ∏_{i=1}^{2g} (1 − α_i t) ∈ ℤ[t], deg P = 2g.
```
Functional equation: Z(C, 1/(qt)) = q^{1−g} t^{2−2g} Z(C, t), equivalently α_i ↦ q/α_i as a permutation of the roots.

### The RH analogue (Weil 1948 for curves, Deligne 1974 general)
```
|α_i| = q^{1/2}   for all i = 1, …, 2g.
```
Translated via t = q^{−s}: the zeros of ζ_C(s) (zeros of P(q^{−s})) satisfy q^{−s} = 1/α_i, so q^{s} = α_i, |α_i| = q^{1/2} ⟺ **Re(s) = 1/2**. An exact analogue of the RH. From this the sharp point estimate:
```
| N_m − (q^m + 1) | ≤ 2g · q^{m/2}    (Hasse–Weil bound).
```

### Weil's proof (positivity / intersection theory)
On the surface C × C one considers the Frobenius graph Γ_F and the diagonal Δ. The **Hodge-index inequality** (positivity of the intersection form on divisors) yields, for the Frobenius correspondence, the Cauchy–Schwarz-type estimate that forces |α_i| = √q. Core: positive-definiteness of ⟨D, D⟩ on the primitive cohomology / Néron–Severi group.

### Deligne's proof (étale cohomology)
The α_i are the eigenvalues of the **geometric Frobenius** F* on H¹_{ét}(C̄, ℚ_ℓ):
```
P(t) = det( 1 − t F* | H¹_{ét} ),   Z(C,t) = ∏_{i=0}^{2} det(1 − tF*|H^i)^{(−1)^{i+1}}.
```
Deligne (Weil I, 1974) proves |α_i| = q^{w/2} (w = weight) for general varieties via monodromy of Lefschetz pencils, Rankin–Selberg-type powering tricks, and L-functions of symmetric products — without the standard conjectures.

### Why no transfer to ℤ
For Spec(ℤ) the "×_{𝔽₁}" product, the Frobenius action, and the appropriate cohomology are missing (cf. 𝔽₁ Doc. 30, Deninger Doc. 31). Positivity (Weil) resp. purity (Deligne) has no known analogue over ℤ.

## Sources
- [The Riemann Hypothesis over Finite Fields: From Weil to the Present Day (arXiv 1509.00797)](https://arxiv.org/abs/1509.00797)
- [The Riemann Hypothesis over Finite Fields — J. Milne](https://www.jmilne.org/math/xnotes/pRH.html)
- [Weil conjectures — Wikipedia](https://en.wikipedia.org/wiki/Weil_conjectures)
- [Deligne's proof of the Weil conjectures — E. Kowalski's blog](https://blogs.ethz.ch/kowalski/2008/03/15/delignes-proof-of-the-weil-conjectures/)
