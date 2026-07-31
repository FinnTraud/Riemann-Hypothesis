---
id: doc-31
number: 31
title: "Deninger's Cohomology Program & Dynamical Systems on Foliated Spaces"
category: solution-program
status: open
tags: [deninger, cohomology, foliated-spaces, dynamical-systems, regularized-determinant]
source_file: 31_Deninger_cohomology_foliated_dynamical.md
lang: en
---

# Deninger's Cohomology Program & Dynamical Systems on Foliated Spaces

**Category:** Active solution program (arithmetic geometry / dynamics)
**Author / years:** Christopher Deninger (from the early 1990s); related Flach–Morin, Leichtnam
**Type:** Conjectural cohomological/dynamical program for the RH
**Status:** Open; conjectural framework, key objects not yet constructed

## Summary
Christopher Deninger proposed a **cohomological program** in which zeta functions are expressed as **regularized determinants** of geometric/dynamical operators. Goal: to interpret the explicit formula of number theory (Doc. 02) as a **Lefschetz trace formula** and the RH as a **spectral symmetry condition** — in direct analogy with the proven Weil/Deligne case (Doc. 18).

## The guiding idea
- In the function-field case, ζ is a quotient of characteristic polynomials of the Frobenius on étale cohomology; the RH is a statement about the eigenvalues of this operator.
- **Deninger's wish:** find, for Spec(ℤ) (resp. arithmetic schemes), a **cohomology theory** with a "Frobenius-like" flow/operator such that:

```
ζ(s) "=" det_∞( (s − Θ) / 2π | H^•_{?} )^{±1}
```

  (a regularized determinant of an operator Θ on hypothetical cohomology groups).
- The **non-trivial zeros** would then be eigenvalues of Θ on H¹; the **RH = self-adjointness / spectral symmetry** of Θ (a Hilbert–Pólya realization, Doc. 05).

## Dynamical systems on foliated spaces
- Since the sought cohomology for arithmetic schemes does not (yet) exist, Deninger looks for **models**: dynamical systems on **foliated manifolds** (foliated spaces) whose **leafwise cohomology** has several of the expected structural properties.
- In these models the following correspond:
  - closed orbits ↔ primes,
  - orbit lengths ↔ log p,
  - the Lefschetz trace formula of the flow ↔ Weil's explicit formula.
- **Flach–Morin** and others have made Deninger's conjectures about **Weil–Arakelov cohomology** precise and partially formalized them.

## Significance / context
- Provides a **conceptual bridge** between the proven geometric case and the analytic RH — and a geometric explanation of *why* the RH should be true (spectral symmetry of a natural operator).
- Closely related and partly complementary to Connes' adele/𝔽₁ program (Doc. 10, 30): both seek the "missing geometry over ℤ", but with different tools (dynamics/foliation vs. noncommutative geometry/topos).
- **Status:** programmatic and conjectural — the central cohomology theory together with the operator is not constructed. Not a proof, but an influential structural compass.

## Mathematical core (formulas, constructions, analogies)

### Zeta as a regularized determinant
Deninger's guiding formula (conjectural) expresses the complete zeta function as zeta-regularized determinants of a flow generator Θ on hypothetical cohomology groups H^i:
```
ξ(s) "="  ∏_{i=0}^{2}  det_∞( (s·Id − Θ) / 2π | H^i(X̄, ·) )^{(−1)^{i+1}}.
```
The regularized determinant is defined via the spectral zeta:
```
det_∞(A) = exp(−ζ_A'(0)),   ζ_A(z) = Σ_λ λ^{−z}  (λ eigenvalues of A).
```
Consistency example (archimedean factor):
```
det_∞( (s − Θ)/2π | H ) yields  Γ_ℝ(s) = π^{−s/2}Γ(s/2)  for the ∞-factor.
```

### Zeros = eigenvalues (Hilbert–Pólya realization)
The non-trivial zeros ρ would be the eigenvalues of Θ on H¹:
```
spectrum(Θ | H¹) = { ρ : ξ(ρ) = 0 }.
```
RH ⟺ Θ has (after a suitable shift by 1/2) a **purely imaginary** spectrum, i.e. a spectral symmetry/self-adjointness — a geometric Hilbert–Pólya statement (Doc. 05).

### Lefschetz trace formula as the explicit formula
For the flow φ^t with generator Θ, a Lefschetz trace formula holds (conjecturally)
```
Σ_i (−1)^i Tr(φ^{t*} | H^i)  =  Σ_{γ closed orbit}  (length ℓ(γ)) Σ_k δ(t − k ℓ(γ)) / |det(1 − D φ)|,
```
whose evaluation reproduces **Weil's explicit formula** (Doc. 02): closed orbits ↔ primes, ℓ(γ) ↔ log p.

### Model: foliated spaces
Since X for Spec(ℤ) is missing, Deninger studies **3-dimensional foliated manifolds** (M, ℱ) with a flow transverse to the foliation. The **reduced leafwise cohomology** H̄^•_ℱ carries a Θ-action with the structural properties (Poincaré duality, Lefschetz) desired for the arithmetic case. Closed orbits of the flow ↔ primes; their lengths ↔ log p.

### Status
The cohomology theory H^i for arithmetic schemes **does not exist** (Flach–Morin formalize parts as Weil–Arakelov cohomology). The formulas are a conjectural compass, not a proof — but they explain *structurally* why RH = spectral symmetry should hold.

## Sources
- [Arithmetic Geometry and Analysis on Foliated Spaces — C. Deninger (Arizona Winter School)](https://swc-math.github.io/dls/DLSDeninger.pdf)
- [Analogies between analysis on foliated spaces and arithmetic geometry (arXiv 0709.2801)](https://arxiv.org/pdf/0709.2801)
- [Deninger's conjectures and Weil-Arakelov cohomology — Flach & Morin](https://www.math.u-bordeaux.fr/~bmorin/Deninger-WA5.pdf)
- [Dynamical systems for arithmetic schemes — Deninger (ResearchGate)](https://www.researchgate.net/publication/381101198_Dynamical_systems_for_arithmetic_schemes)
- [The Riemann Hypothesis: Arithmetic and Geometry — J. Lagarias](https://websites.umich.edu/~lagarias//doc/mt-holyoke-rev.pdf)
