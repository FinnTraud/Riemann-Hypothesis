---
id: doc-14
number: 14
title: "Li Criterion, Bombieri–Lagarias & Weil Positivity"
category: criterion
status: open
tags: [li-criterion, bombieri-lagarias, weil-positivity, positivity]
source_file: 14_Li_criterion_Bombieri_Lagarias_Weil_positivity.md
lang: en
---

# Li Criterion, Bombieri–Lagarias & Weil Positivity

**Category:** Equivalent criterion (positivity)
**Authors / years:** André Weil (1952), Xian-Jin Li (1997), Enrico Bombieri & Jeffrey Lagarias (1999)
**Type:** Positivity conditions equivalent to the RH
**Status:** Equivalences proven; positivity unproven in general

## Summary
A family of closely related criteria formulates the RH as a **positivity statement**. Weil's criterion uses the explicit formula as a quadratic form; Li's criterion translates the RH into the non-negativity of an explicit number sequence λ_n; Bombieri–Lagarias show that the two mean the same thing and give an arithmetic formula.

## Li criterion (1997)
- Define the **Li coefficients**:

```
λ_n = Σ_ρ [ 1 − (1 − 1/ρ)^n ]   (sum over all non-trivial zeros ρ)
```

- **Theorem (Li):** the RH is equivalent to **λ_n ≥ 0 for all n ≥ 1**.
- The λ_n can also be expressed via logarithmic derivatives of the ξ-function at its zeros and are numerically computable; all values computed so far are positive (consistent with RH), but a general proof of positivity is missing.

## Bombieri–Lagarias (1999)
- Generalized the Li criterion to arbitrary multisets of complex numbers with certain properties.
- Provided an **arithmetic formula** for the λ_n via the **Guinand–Weil explicit formula** and showed: the positivity of the λ_n has **the same meaning** as Weil's positivity criterion.

## Weil positivity (Weil's criterion, 1952)
- Weil's explicit formula connects a sum over zeros with a sum over primes plus archimedean terms.
- **Weil's criterion:** the RH holds if and only if a certain associated **quadratic form is positive (semidefinite)** — the "Weil positivity".
- This positivity is also the analytic core of **Connes' trace-formula program** (Doc. 10): Connes' reduction of the RH ultimately amounts to establishing exactly this positivity (cf. Connes–Consani "Weil positivity and trace formula", 2021).

## Significance / context
- Bundles several programs (explicit formula, Connes, de Branges) under a common **positivity leitmotiv**.
- Turns the RH into a concrete, checkable (strongly numerically supported) inequality statement.
- **Open:** establishing the positivity for *all* n, resp. for the full quadratic form, is just as hard as the RH itself.

## Mathematical core (formulas, theorems, proof sketches)

### Definition of the Li coefficients
With the complete ξ-function (ξ(s) = ½ s(s−1)π^{−s/2}Γ(s/2)ζ(s)) set
```
λ_n = (1/(n−1)!) d^n/ds^n [ s^{n−1} log ξ(s) ] |_{s=1}     (n ≥ 1).
```
Equivalent sum over the zeros (with ρ, 1−ρ paired):
```
λ_n = Σ_ρ [ 1 − (1 − 1/ρ)^n ].
```

### Li criterion (1997)
```
RH  ⟺  λ_n ≥ 0   for all n ≥ 1.
```
**Proof idea:** the map ρ ↦ 1/ρ sends the critical line Re(s)=1/2 to the circle |z − 1| = 1. Write z = 1/ρ. Then 1 − (1−1/ρ)^n = 1 − (1−z)^n. One shows: Re(λ_n) ≥ 0 ∀n ⟺ all ρ lie in |1 − 1/ρ| ≤ 1 ⟺ Re(ρ) ≤ 1/2 — and with the functional equation (symmetry ρ ↔ 1−ρ) ⟺ Re(ρ) = 1/2. So positivity for all n forces the critical line.

### Bombieri–Lagarias (1999): generalization
For an arbitrary multiset R = {ρ} of complex numbers with Σ (1+|ρ|)^{−2} < ∞ and symmetry ρ ↔ 1−ρ:
```
Re(ρ) ≤ 1/2  ∀ρ   ⟺   λ_n := Σ_ρ [1 − (1 − 1/ρ)^n] ≥ 0  ∀n ≥ 1.
```
Plus an arithmetic formula via Guinand–Weil:
```
λ_n = Σ_{j=1}^n binom(n,j) (−1)^{j+1} ... = n(γ + log(4π))/2 − ... − Σ_{k} (arithmetic contributions of Λ(m))
```
(explicitly: λ_n is expressed via von Mangoldt's Λ and archimedean Γ-terms).

### Weil's positivity criterion (1952)
For a test function g (even, smooth, compactly supported) with ĝ(t)=∫ g(x)e^{ixt}dx, define the **Weil functional**
```
W(g) = Σ_ρ ĝ(−i(ρ − 1/2))
     = ĝ-main term(poles)  −  Σ_{n≥1} Λ(n)/√n · g(log n)  −  (1/2π)∫ ĝ(t) [Γ'/Γ-term] dt.
```
**Weil criterion:** RH ⟺ W(g ⋆ ḡ*) ≥ 0 for all such g (positive-semidefinite quadratic form). Exactly this form is the spectral side in Connes' trace formula (Doc. 10).

### Numerics
λ_1 = 1 + γ/2 − log(4π)/2 ≈ 0.0230957 > 0; all λ_n computed so far are > 0 and grow ~ (n/2)(log n − 1 + γ − log 2π) under RH.

## Sources
- [Complements to Li's Criterion for the Riemann Hypothesis — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022314X99923922)
- [On the explicit formula in the theory of prime numbers (World Scientific)](https://www.worldscientific.com/doi/10.1142/S1793042112500327)
- [An arithmetic interpretation of generalized Li's criterion (arXiv 1305.1421)](https://arxiv.org/pdf/1305.1421)
- [Li coefficients as norms of functions in a model space (arXiv 2301.05779)](https://arxiv.org/pdf/2301.05779)
