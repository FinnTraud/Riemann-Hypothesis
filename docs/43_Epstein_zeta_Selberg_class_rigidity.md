---
id: doc-43
number: 43
title: "Epstein Zeta Functions & Selberg-Class Rigidity: Which Property Forces the Critical Line?"
category: obstruction
status: meta
tags: [epstein-zeta, selberg-class-rigidity, davenport-heilbronn, euler-product, kaczorowski-perelli]
source_file: 43_Epstein_zeta_Selberg_class_rigidity.md
lang: en
---

# Epstein Zeta Functions & Selberg-Class Rigidity: Which Property Forces the Critical Line?

**Category:** Meta / obstruction (Tier-1 for "bulletproof")
**Authors / years:** Davenport–Heilbronn (1936); Epstein; Voronin; Kaczorowski–Perelli (Selberg-class classification, 1999–2011)
**Type:** Discriminating counterexamples + structure theory
**Status:** Established negative/rigidity results

## Summary
This is the **most important "bulletproof" document** together with Doc. 35: it answers the question of **which** properties actually force the zeros onto the critical line — via functions that look *almost* like ζ but violate the RH. It complements Doc. 35 (Davenport–Heilbronn) with the **Epstein zeta functions** and the **rigidity of the degree-1 Selberg class**.

## Mathematical core (formulas, theorems, proof sketches)

### Epstein zeta function
For a positive-definite quadratic form Q(m,n) = am² + bmn + cn² (discriminant d = b²−4ac < 0):
```
ζ_Q(s) = Σ_{(m,n) ≠ (0,0)} Q(m,n)^{−s}   (Re s > 1).
```
ζ_Q has an **analytic continuation** and a **functional equation** of Riemann type (Re s ↔ 1−s, via theta transformation) — i.e. the same "soft" properties as ζ.

### The counterexample
**Theorem (Davenport–Heilbronn 1936 for the associated Dirichlet series; Epstein case).** If the **class number h(d) > 1** (the quadratic form does not lie alone in its genus class), then ζ_Q has **infinitely many zeros with Re(s) > 1/2** — the RH analogy is FALSE. Nonetheless ζ_Q also has a positive proportion (indeed infinitely many) of zeros *on* the line.

### Why: the missing Euler product
ζ_Q is a **linear combination** of Hecke L-functions for ideal-class characters:
```
ζ_Q(s) = (1/w) Σ_{χ} χ̄(class(Q)) L(s, χ),
```
and this sum has **no Euler product** (the individual L(s,χ) do, their linear combination does not). Exactly the missing Euler product allows zeros off the line (cf. Doc. 35).

### Selberg-class rigidity (what forces the RH)
The **Selberg class 𝒮** (Doc. 21) requires, in addition to functional equation + continuation, an **Euler product** and the **Ramanujan condition**. Classification theorems (Conrey–Ghosh; Kaczorowski–Perelli):
```
- There are no functions in 𝒮 of degree 0 < d < 1.
- Degree d = 1 in 𝒮  ⟹  F(s) = ζ(s)  or  F(s) = L(s + iθ, χ)  (shifted Dirichlet L-function).
```
**Consequence (rigidity):** functions of degree 1 *with* an Euler product and the Ramanujan condition are essentially ζ and Dirichlet L — and for exactly these the RH is expected. Davenport–Heilbronn (degree 1, **without** Euler product) and Epstein (h>1, **without** Euler product) drop out.

### The precise lesson for a proof
> Off-line zeros become possible as soon as the Euler product is missing. **A valid RH proof must use the multiplicativity (Euler product) + Ramanujan bound at a point where Davenport–Heilbronn/Epstein violate them.** Any proof that does not distinguish these properties is wrong.

## Connection
- Sharpens Doc. 35 (obstructions) and Doc. 21 (Selberg class).
- Explains why Connes (Doc. 10) builds the Euler product in adelically (place by place) and why scattering/spectral models are not even definable for Davenport–Heilbronn.

## Sources
- [Zeros of the Davenport-Heilbronn Counterexample (AMS Math. Comp.)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)
- [Positive proportion of zeros of Epstein zeta on the critical line (arXiv 2411.18492)](https://arxiv.org/pdf/2411.18492)
- [On the Selberg class / converse theorems (arXiv 1605.02354)](https://arxiv.org/pdf/1605.02354)
- [On some reasons for doubting the Riemann hypothesis — Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
