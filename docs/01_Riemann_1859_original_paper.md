---
id: doc-01
number: 01
title: "Riemann's Original Paper (1859) and the Riemann–Siegel Formula"
category: foundations
status: reference
tags: [zeta, functional-equation, euler-product, riemann-siegel, xi-function]
source_file: 01_Riemann_1859_original_paper.md
lang: en
---

# Riemann's Original Paper (1859) and the Riemann–Siegel Formula

**Category:** Foundation
**Author / year:** Bernhard Riemann, 1859 (Riemann–Siegel part: Siegel 1932, from the Nachlass)
**Type:** Origin paper in which the conjecture is formulated
**Status:** Historical foundation; contains the unsolved conjecture

## Summary
"Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse" is an approximately 9-page paper by Bernhard Riemann, published in November 1859 in the *Monatsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin*. It is Riemann's only paper on number theory at all — and it revolutionized mathematics. In it Riemann casually formulates the famous conjecture that all non-trivial zeros of the zeta function have real part 1/2.

## Core ideas of the paper
- **Analytic continuation:** Riemann continues the series ζ(s) = Σ 1/n^s (initially convergent only for Re(s) > 1) to the entire complex plane (with a simple pole at s = 1).
- **Functional equation:** He proves the symmetry ζ(s) ↔ ζ(1−s), formulated via the completed function ξ(s), which is invariant under s ↦ 1−s. From this follows the symmetry of the non-trivial zeros about the critical line Re(s) = 1/2.
- **Product representation / Hadamard product** for entire functions (later rigorously justified by Hadamard).
- **Connection primes ↔ zeros:** Riemann gives an explicit formula for the prime-counting function in which the non-trivial zeros appear as oscillating correction terms.
- **The conjecture itself:** Riemann writes that it is "very probable" that all non-trivial zeros lie on Re(s) = 1/2 — but that after a few fleeting attempts he had set the proof aside, since it was dispensable for his immediate goal.

## The Riemann–Siegel formula (from the Nachlass)
- Riemann's private notes contained a highly efficient asymptotic formula for the numerical computation of ζ(1/2 + it) — the **Riemann–Siegel formula** — as well as concrete computations of the first zeros.
- These results remained unpublished and were only discovered in the Nachlass by **Carl Ludwig Siegel in the early 1930s** and published in 1932 ("Über Riemanns Nachlaß zur analytischen Zahlentheorie").
- The formula remains the basis of many numerical zero verifications to this day (see document 24).

## Significance
- Founds analytic number theory as a discipline.
- Provides the structural basis (functional equation, explicit formula) for practically all later proof approaches.
- Shows that Riemann himself already had numerical evidence but regarded the statement as secondary to the prime number theorem.

## Mathematical core (formulas, theorems, proof sketches)

### Euler product (starting point)
For Re(s) > 1 the identity discovered by Euler, which links ζ with the primes, holds:
```
ζ(s) = Σ_{n=1}^∞ 1/n^s = ∏_{p prime} (1 − p^{−s})^{−1}
```
Proof (sketch): geometric series (1 − p^{−s})^{−1} = Σ_{k≥0} p^{−ks}; expanding the product over all p yields, by unique prime factorization, each term n^{−s} exactly once. From the product it follows that ζ(s) ≠ 0 for Re(s) > 1 (no factor vanishes, convergence).

### Analytic continuation via the theta function
Using the Jacobi theta function ψ(x) = Σ_{n=1}^∞ e^{−n²πx} and the integral representation
```
π^{−s/2} Γ(s/2) ζ(s) = ∫_0^∞ x^{s/2 − 1} ψ(x) dx
```
Riemann uses the functional equation of the theta function ψ(1/x) = −1/2 + (1/2)√x + √x·ψ(x) (from the Poisson summation formula) to split the integral into a form convergent for all s ∈ ℂ:
```
ξ-integral:  π^{−s/2}Γ(s/2)ζ(s) = 1/(s(s−1)) + ∫_1^∞ (x^{s/2−1} + x^{−(s+1)/2}) ψ(x) dx
```
The right-hand side is manifestly invariant under s ↦ 1 − s ⇒ functional equation.

### Functional equation
```
ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s)
```
or symmetrically via the completed function (complete zeta):
```
ξ(s) := (1/2) s(s−1) π^{−s/2} Γ(s/2) ζ(s),     ξ(s) = ξ(1 − s)
```
ξ is an entire function (the pole at s=1 and the trivial factor cancelled out). The symmetry ξ(s) = ξ(1−s) forces the non-trivial zeros into positions mirror-symmetric about the line Re(s) = 1/2. Together with ξ(s) = ξ(s̄) (real coefficients), zeros come in quadruples ρ, 1−ρ, ρ̄, 1−ρ̄ (except on the line, where they collapse to pairs ρ, ρ̄).

### Trivial zeros
The factor sin(πs/2) in the functional equation forces ζ(−2n) = 0 for n = 1, 2, 3, … (trivial zeros); these are compensated in ξ by Γ(s/2).

### The explicit formula (Riemann's result)
For the weighted prime-counting function J(x) = Σ_{p^k ≤ x} 1/k Riemann gives a formula:
```
J(x) = Li(x) − Σ_ρ Li(x^ρ) − log 2 + ∫_x^∞ dt/(t(t²−1) log t)
```
and returns via Möbius inversion to π(x) = Σ_{n} μ(n)/n · J(x^{1/n}). The sum Σ_ρ over the zeros is the oscillating correction term (cf. Doc. 02).

### Riemann–Siegel formula (from the Nachlass)
For computation on the critical line with Z(t) = e^{iθ(t)} ζ(1/2 + it) (real):
```
Z(t) = 2 Σ_{n=1}^{N} cos(θ(t) − t log n)/√n  +  R(t),   N = ⌊√(t/2π)⌋
```
with the Riemann–Siegel theta θ(t) = arg Γ(1/4 + it/2) − (t/2) log π and an asymptotically computable remainder term R(t) ~ (−1)^{N−1} (t/2π)^{−1/4} · [C_0 + C_1(t/2π)^{−1/2} + …].

## Sources
- [On the Number of Primes Less Than a Given Magnitude — Wikipedia](https://en.wikipedia.org/wiki/On_the_Number_of_Primes_Less_Than_a_Given_Magnitude)
- [On Riemann's Paper "On the Number of Primes Less Than a Given Magnitude" (arXiv 1609.02301)](https://arxiv.org/abs/1609.02301)
- [On a Fair Copy of Riemann's 1859 Publication Created by Alfred Clebsch (arXiv 1512.02976)](https://arxiv.org/pdf/1512.02976)
- [On Riemann's Nachlass for Analytic Number Theory: A translation of Siegel's Über (arXiv 1810.05198)](https://arxiv.org/pdf/1810.05198)
- [A computational history of prime numbers and Riemann zeros (arXiv 1810.05244)](https://arxiv.org/pdf/1810.05244)
