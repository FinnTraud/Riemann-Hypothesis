---
id: doc-09
number: 09
title: "Bender–Brody–Müller (2017): PT-Symmetric Hamiltonian for the Riemann Zeros"
category: spectral
status: open
tags: [bender-brody-muller, PT-symmetry, hamiltonian]
source_file: 09_Bender_Brody_Muller_2017_Hamiltonian.md
lang: en
---

# Bender–Brody–Müller (2017): PT-Symmetric Hamiltonian for the Riemann Zeros

**Category:** Spectral approach / quantum physics
**Authors / year:** Carl M. Bender, Dorje C. Brody, Markus P. Müller; *Physical Review Letters* 118, 130201 (30 March 2017)
**Type:** Operator construction (Hilbert–Pólya candidate)
**Status:** Incomplete; self-adjointness not proven, doubted by critics

## Summary
In 2017 Bender, Brody and Müller constructed a concrete Hamiltonian operator H with the property: if its eigenfunctions satisfy a suitable boundary condition, then the eigenvalues correspond exactly to the non-trivial zeros of the zeta function. The work drew media attention ("Physicists attack the Riemann Hypothesis"), but remained incomplete.

## Core idea
- The operator is a **generalization of the Berry–Keating xp operator** (Doc. 08).
- Constructed so that the eigenvalues E_n are related to the zeros z_n via **z_n = ½(1 − i·E_n)**. If all E_n are real, then all z_n have real part 1/2 → RH.
- **PT symmetry instead of classical Hermiticity:** H itself is not Hermitian in the usual sense, but **iH is PT-symmetric**. If this PT symmetry were *maximally broken*, then all eigenvalues would be real.

## The decisive gap
- The authors themselves stated the condition: **if one can rigorously show that H is (in a suitable sense) self-adjoint, resp. that the PT symmetry is maximally broken, then the RH follows.**
- Exactly this step was **not** proven. The reduction merely shifts the RH into an equally difficult spectral-theoretic statement.
- **Criticism:** several comments (including arXiv 1704.02644) pointed to problems with well-definedness / self-adjointness and the treatment of the boundary conditions. Moreover, the relation essentially reproduces the known explicit formula / functional-analytic structure without providing new control over the zeros.

## Significance / context
- The cleanest modern *explicit* Hilbert–Pólya operator candidate — but with the same fundamental gap as all its predecessors: the *reality of the spectrum* is the actual question and remains unproven.
- Revived the discussion of PT-symmetric (non-Hermitian) quantum mechanics in the RH context.
- **Not a proof of the RH.**

## Mathematical core (formulas, theorems, proof sketches)

### The constructed operator
On a suitable Hilbert space (eigenfunctions with a boundary condition), Bender–Brody–Müller define the operator
```
Ĥ = (1/(1 − e^{−i p̂})) ( x̂ p̂ + p̂ x̂ ) (1 − e^{−i p̂})
```
with x̂ = i d/dx (resp. canonically [x̂, p̂] = i). This is a conjugation of the symmetrized Berry–Keating operator (x̂p̂ + p̂x̂)/2 by the non-unitary operator (1 − e^{−ip̂}).

### Claimed eigenvalue relation
If the eigenfunctions ψ satisfy the boundary condition ψ(0) = 0, the authors claim: the eigenvalues E_n yield the non-trivial zeros via
```
z_n = 1/2 + i·(... )   ⇔   the secular equation becomes  ζ(1/2 + i E_n …) = 0,
```
more precisely in the formulation E_n ↔ z_n via z_n = ½(1 − i E_n). If all E_n are real ⇒ Re(z_n) = 1/2 ⇒ RH.

### PT symmetry instead of Hermiticity
Ĥ is not Hermitian, but
```
(PT) (i Ĥ) (PT)^{−1} = i Ĥ
```
holds with parity P: x ↦ −x and time reversal T: i ↦ −i. **Key theorem of PT theory:** if the PT symmetry is unbroken (all eigenstates PT-invariant), then the spectrum is real. The authors need the PT symmetry to act, when **maximally broken** on the relevant subspace, in such a way that reality still follows.

### The gap (precisely)
What is missing is the proof that Ĥ (resp. the associated bilinear form) is actually **self-adjoint** on the constructed domain (resp. that the PT symmetry is unbroken in the required sense). Without this step the reality of the E_n is not secured. Moreover, the conjugation by (1 − e^{−ip̂}) formally only shows that the *secular function* is related to ζ — the actual difficulty (location of the zeros) is reproduced, not solved. Comment arXiv 1704.02644 points to well-definedness/domain problems.

## Sources
- [Hamiltonian for the Zeros of the Riemann Zeta Function — Phys. Rev. Lett. 118, 130201](https://link.aps.org/doi/10.1103/PhysRevLett.118.130201)
- [Hamiltonian for the zeros of the Riemann zeta function (arXiv 1608.03679)](https://arxiv.org/abs/1608.03679)
- [Comment on "Hamiltonian for the Zeros of the Riemann Zeta Function" (arXiv 1704.02644)](https://arxiv.org/pdf/1704.02644)
- [Physicists Attack Math's $1,000,000 Question — Quanta Magazine](https://www.quantamagazine.org/quantum-physicists-attack-the-riemann-hypothesis-20170404/)
