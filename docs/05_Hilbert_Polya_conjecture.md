---
id: doc-05
number: 05
title: "The Hilbert–Pólya Conjecture (spectral approach)"
category: spectral
status: open
tags: [hilbert-polya, self-adjoint-operator, spectral]
source_file: 05_Hilbert_Polya_conjecture.md
lang: en
---

# The Hilbert–Pólya Conjecture (spectral approach)

**Category:** Spectral approach (umbrella program)
**Authors / year:** David Hilbert, George Pólya (around 1912–1914, transmitted orally)
**Type:** Strategic guiding conjecture
**Status:** Open; no suitable operator constructed

## Summary
The Hilbert–Pólya conjecture states: the imaginary parts γ of the non-trivial zeros ρ = 1/2 + iγ of the zeta function are the **eigenvalues of a self-adjoint (Hermitian) operator**. Since self-adjoint operators always have *real* eigenvalues, the existence of such an operator (correctly coupled to ζ) would immediately mean that all γ are real — i.e. all zeros lie on Re(s) = 1/2. This would prove the RH.

## Core idea
- Write ρ = 1/2 + iγ. The RH is equivalent to the statement: **all γ are real**.
- Find a Hilbert space and a self-adjoint operator H whose spectrum is exactly the set {γ}. Self-adjointness ⇒ real spectrum ⇒ RH.
- Pólya (around 1913) conjectured that the zeros are eigenvalues of a naturally arising, unbounded self-adjoint operator; Hilbert coined the term "spectrum" for the eigenvalues of an equivalent Hermitian operator.

## Status & manifestations
- **No** such operator has been rigorously constructed for the actual ζ zeros — this is *the* central open strategic question of the field.
- Indirect evidence: the statistical distribution of the zeros matches exactly the eigenvalue statistics of large random matrices (GUE), which is consistent with the existence of a "chaotic" self-adjoint operator (see Doc. 06).
- Concrete operator candidates / partial realizations:
  - **Berry–Keating H = xp** model (Doc. 08).
  - **Bender–Brody–Müller** PT-symmetric Hamiltonian (Doc. 09).
  - **Connes'** spectral realization in noncommutative geometry (Doc. 10).
  - **Connes–Moscovici** prolate spheroidal operator as a "concrete approximate solution of the Hilbert–Pólya conjecture" (Doc. 11).

## Significance / context
- Provides perhaps the most pursued *strategic* framework for an RH proof.
- Connects number theory with functional analysis, quantum physics, and quantum chaos.
- Weakness: statistical agreement (GUE) is *evidence*, not a proof mechanism — an actual operator is missing.

## Mathematical core (formulas, theorems, proof sketches)

### Precise formulation
Write the non-trivial zeros as ρ_n = 1/2 + i γ_n. One seeks a Hilbert space H and a **self-adjoint operator** Ĥ (unbounded) with
```
Ĥ ψ_n = γ_n ψ_n
```
for a complete system of eigenfunctions ψ_n. Since Ĥ = Ĥ* is self-adjoint, spectrum(Ĥ) ⊂ ℝ, so γ_n ∈ ℝ for all n. Because ξ(ρ) = 0 and ξ(s) = ξ(1−s), ξ(s)=ξ(s̄), γ_n ∈ ℝ is **equivalent** to Re(ρ_n) = 1/2. Hence:
```
(∃ self-adj. Ĥ with spectrum {γ_n})  ⟹  RH
```

### Why "self-adjoint" is the key
For a symmetric operator, only **self-adjointness** (equal deficiency indices, real spectral theorem) guarantees a real spectrum. Hermitian form: ⟨Ĥψ, φ⟩ = ⟨ψ, Ĥφ⟩ ⇒ eigenvalues real, eigenfunctions for different eigenvalues orthogonal. Exactly this reality "forces" the critical line.

### Connection to the trace formula (heuristic)
If Ĥ existed, a trace formula would link the spectral sum with a geometric sum:
```
Σ_n h(γ_n) = (smooth term) + Σ_{periodic orbits p} (contribution with length log p)
```
Comparison with Weil's explicit formula (Doc. 02) ⇒ the "periodic orbits" correspond to the primes, lengths = log p. This is the structural bridge that Berry–Keating (Doc. 08), Connes (Doc. 10), and Deninger (Doc. 31) try to realize concretely.

### Pólya's analytic precursor (Laguerre–Pólya)
An equivalent, operator-free version (Doc. 29): RH ⟺ ξ lies in the **Laguerre–Pólya class** (entire functions with only real zeros, limits of polynomials ∏(1 − x/x_k) with x_k ∈ ℝ). "Real spectrum" and "real zeros of ξ" are the same statement in two languages.

## Sources
- [Hilbert–Pólya conjecture — Wikipedia](https://en.wikipedia.org/wiki/Hilbert%E2%80%93P%C3%B3lya_conjecture)
- [The Riemann zeros as spectrum and the Riemann hypothesis (arXiv 1601.01797)](https://arxiv.org/pdf/1601.01797)
- [On Hilbert-Polya conjecture: Hermitian operator naturally associated to L-functions (arXiv 1105.1500)](https://arxiv.org/pdf/1105.1500)
- [The Hilbert-Pólya Conjecture and the Prolate Spheroidal Operator (TU Delft)](https://repository.tudelft.nl/file/File_a03b023e-2ba7-45fb-bde9-6fcc7a53d306)
