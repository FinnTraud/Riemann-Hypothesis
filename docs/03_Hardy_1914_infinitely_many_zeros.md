---
id: doc-03
number: 03
title: "Hardy (1914): Infinitely Many Zeros on the Critical Line"
category: partial-results
status: proven
tags: [hardy, critical-line, Z-function, theta-function]
source_file: 03_Hardy_1914_infinitely_many_zeros.md
lang: en
---

# Hardy (1914): Infinitely Many Zeros on the Critical Line

**Category:** Partial result
**Author / year:** G. H. Hardy, 1914 (extensions: Hardy–Littlewood 1921, Selberg 1942)
**Type:** Proven partial result on the RH
**Status:** Proven (a genuine theorem, not the full RH)

## Summary
In 1914 Godfrey Harold Hardy proved that **infinitely many** non-trivial zeros of the Riemann zeta function lie exactly on the critical line Re(s) = 1/2. This was the first rigorous result to single out the critical line as the location of (infinitely many) zeros — a first step toward the RH, but far from the full statement (*all* zeros).

## Core idea
- Hardy considers the real-valued **Hardy Z-function** Z(t), constructed so that |Z(t)| = |ζ(1/2 + it)| and Z(t) is real. Zeros of Z(t) on the real t-axis correspond exactly to zeros of ζ on the critical line.
- Using the **transformation formula of the Jacobi theta function**, Hardy shows that Z(t) changes sign infinitely often → infinitely many real zeros → infinitely many ζ zeros on Re(s) = 1/2.

## Later sharpenings
- **Hardy–Littlewood (1921):** at least K·T zeros on the critical line up to height T (K > 0 constant) — i.e. a *positive linear* fraction of the expected number.
- **Selberg (1942):** improvement to K·T·log T, i.e. a *positive fraction of all* N(T) ≈ (T/2π)log T zeros. Selberg's method (mollifier) was later developed further by Levinson and Conrey (see Doc. 04).

## Significance / context
- First hard indication of the correctness of the RH.
- Provides the Z-function, which became the central tool of numerical verification (sign changes of Z(t) localize zeros — the basis of the Turing method, Odlyzko, etc., Doc. 24).
- Important: "infinitely many on the line" does not rule out that *also* infinitely many might lie off it — exactly this gap is only partially closed by the proportion results (Doc. 04); the full RH remains open.

## Mathematical core (formulas, theorems, proof sketches)

### The Hardy Z-function
Define the Riemann–Siegel theta function and Z(t):
```
θ(t) = arg Γ(1/4 + it/2) − (t/2) log π,    Z(t) = e^{iθ(t)} ζ(1/2 + it)
```
**Properties:** Z(t) is real-valued for real t, and |Z(t)| = |ζ(1/2 + it)|. Therefore: Z(t₀) = 0 ⟺ ζ has a zero at 1/2 + it₀ on the critical line. A sign change of Z ⇒ a zero on the line.

### Hardy's theorem and proof idea (1914)
**Theorem (Hardy).** Z(t) has infinitely many real zeros; hence infinitely many zeros of ζ lie on Re(s) = 1/2.

**Proof sketch (moment method with theta transformation).** Hardy considers integrals of Z(t) against test kernels and uses the functional equation of the Jacobi theta function
```
ϑ(x) = Σ_{n=−∞}^∞ e^{−πn²x},    ϑ(1/x) = √x · ϑ(x).
```
From the Mellin representation of ξ he deduces that certain means of Z(t) cannot keep the same sign for all large T: if Z(t) were of fixed sign beyond some point, the asymptotic behavior of the integrals
```
∫_0^T Z(t) t^{2k} dt
```
(for suitable k, evaluated via the theta transformation at the point corresponding to the critical line) would contradict the assumption. More precisely, Hardy shows that the behavior of the theta function near x = 1 forces Z to change sign infinitely often.

### Quantitative sharpenings (with formulas)
Let N₀(T) be the number of zeros *on* the critical line up to height T, and N(T) the total number (Doc. 02).
- **Hardy–Littlewood (1921):** N₀(T) > c·T for some c > 0.
- **Selberg (1942):** N₀(T) > c·T log T, i.e. N₀(T) > c·N(T) (positive fraction), via the mollifier mean ∫ |ζ(1/2+it) M(1/2+it)|² dt with a Dirichlet polynomial M.
- **Proportion κ := liminf N₀(T)/N(T):** Levinson κ ≥ 1/3, Conrey κ ≥ 2/5, today κ > 0.41 (Doc. 04).

### Speiser equivalence (background of the mollifier method)
**Theorem (Speiser 1934).** RH ⟺ ζ'(s) ≠ 0 for 0 < Re(s) < 1/2. The Levinson method counts zeros of ζ'·(mollifier) and transfers them via this equivalence to ζ.

## Sources
- [Hardy's function Z(t) — results and problems (arXiv 1601.06512)](https://arxiv.org/pdf/1601.06512)
- [A note on Hardy's theorem (HAL)](https://hal.science/hal-01425570v1/document)
- [The Riemann zeta function and its zeros — Russian Math Surveys](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=2762&what=fullteng)
- [Almost all of the nontrivial zeros of the Riemann zeta-function (arXiv 2205.09042)](https://arxiv.org/pdf/2205.09042)
