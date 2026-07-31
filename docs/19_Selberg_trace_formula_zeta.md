---
id: doc-19
number: 19
title: "Selberg Trace Formula & Selberg Zeta Function (RH analogue PROVEN)"
category: proven-analogue
status: proven
tags: [selberg, trace-formula, selberg-zeta, laplacian, geodesics]
source_file: 19_Selberg_trace_formula_zeta.md
lang: en
---

# Selberg Trace Formula & Selberg Zeta Function (RH analogue PROVEN)

**Category:** Proven analogue (spectral/geometric)
**Author / year:** Atle Selberg (1956)
**Type:** Proven RH analogue + structural model for trace formulas
**Status:** ✅ RH analogue for the Selberg zeta function proven

## Summary
The **Selberg trace formula** (1956) links, on a hyperbolic Riemann surface, the **eigenvalues of the Laplace operator** (spectral side) with the **lengths of closed geodesics** (geometric side). The associated **Selberg zeta function** satisfies an exact analogue of the Riemann Hypothesis — and this is **proven**. It is the most important *spectral* model for the Hilbert–Pólya program.

## Core idea
- **Selberg zeta function:** an Euler-product-like product, but instead of over primes it runs over **primitive closed geodesics** of the hyperbolic surface (orbit lengths ↔ "log p").
- It has a **functional equation** and an Euler product analogous to ζ.
- **Proven RH analogue:** the non-trivial zeros of the Selberg zeta function lie on a critical line — their imaginary parts are related to the **eigenvalues of the Laplace operator**. Since the Laplace operator is **self-adjoint** (real eigenvalues!), the zeros lie in the right place *automatically*.

## Direct analogy with the classical RH
| Selberg world (proven) | Riemann world (open) |
|---|---|
| Closed geodesics | Primes |
| Orbit lengths | log p |
| Eigenvalues of the Laplace operator | Imaginary parts of the ζ zeros |
| Selberg trace formula | Weil's explicit formula (Doc. 02) |
| Self-adjoint Laplacian ⇒ RH analogue | sought Hilbert–Pólya operator (Doc. 05) |

- **This is exactly where the hope of the Hilbert–Pólya program lies:** in the Selberg world the self-adjoint operator (the Laplace operator) *exists* and delivers the RH analogue "for free". If one found the ζ analogue of this operator, the classical RH would be proven.
- Connes explicitly stated: a suitable analogue of the Selberg trace formula for the action of the idele-class group on the adele-class space would imply the RH (Doc. 10).

## Significance / context
- Provides a *working* model in which "zeros = eigenvalues of a self-adjoint operator" is a reality.
- Considerably strengthens the plausibility of the spectral approach.
- **Caveat:** the hyperbolic geometry is *given*; for ζ the corresponding geometric object is missing — the operator is not known.

## Mathematical core (formulas, theorems, proof sketches)

### Setting
Let Γ \ ℍ be a compact hyperbolic surface (Γ ⊂ PSL₂(ℝ) discrete, cocompact), Δ the Laplace–Beltrami operator. Eigenvalues 0 = λ_0 < λ_1 ≤ λ_2 ≤ …, write λ_n = 1/4 + r_n² (so r_n = √(λ_n − 1/4)).

### Selberg zeta function
Product over primitive closed geodesics γ₀ of length ℓ(γ₀):
```
Z(s) = ∏_{γ₀ primitive} ∏_{k=0}^∞ ( 1 − e^{−(s+k) ℓ(γ₀)} ),   Re(s) > 1.
```
(Lengths ℓ(γ₀) ↔ log p; the closed geodesics ↔ primes.)

### Functional equation & zeros
Z(s) satisfies a functional equation Z(s) = Z(1−s)·(explicit) and has:
- "trivial" zeros at s = −k (k ≥ 0) and
- **non-trivial zeros at s = 1/2 ± i r_n** (from the Laplace eigenvalues).

### The proven RH analogue
Since Δ is **self-adjoint positive**, the λ_n ≥ 0 are real. For λ_n ≥ 1/4, r_n ∈ ℝ, so the non-trivial zeros 1/2 ± i r_n lie **exactly on Re(s) = 1/2**. (Finitely many "small" eigenvalues 0 ≤ λ_n < 1/4 give exceptional zeros on the real segment — the exact analogue of possible Siegel zeros, Doc. 32.) ⇒ RH analogue proven, because the operator is self-adjoint.

### Selberg trace formula
For a suitable test function h (even, holomorphic in a strip) with Fourier transform g:
```
Σ_{n=0}^∞ h(r_n)  =  (Area/4π) ∫_{−∞}^∞ h(r) r tanh(π r) dr  +  Σ_{γ₀} Σ_{k=1}^∞  (ℓ(γ₀) g(k ℓ(γ₀))) / (2 sinh(k ℓ(γ₀)/2)).
```
- **Left (spectral) side:** sum over Laplace eigenvalues ↔ in the Riemann world the sum over zeros γ.
- **Right (geometric) side:** identity term (area) + sum over geodesic lengths ↔ in the Riemann world Σ Λ(n)/√n g(log n).

### Dictionary to the explicit formula (Doc. 02)
| Selberg trace formula | Weil's explicit formula |
|---|---|
| Σ_n h(r_n) | Σ_ρ h(γ) |
| (Area/4π)∫ h(r) r tanh(πr) dr | archimedean Γ'/Γ term |
| Σ_{γ₀,k} ℓ g(kℓ)/(2 sinh(kℓ/2)) | Σ_n Λ(n) n^{−1/2} g(log n) |

**Key message:** in the Selberg world the self-adjoint operator (Δ) *exists* and delivers the RH analogue for free. This is the blueprint that Connes (Doc. 10) and Deninger (Doc. 31) seek to realize for ζ.

## Sources
- [Selberg trace formula — Wikipedia](https://en.wikipedia.org/wiki/Selberg_trace_formula)
- [The Selberg trace formula and the Riemann zeta function — Hejhal (Experts@Minnesota)](https://experts.umn.edu/en/publications/the-selberg-trace-formula-and-the-riemann-zeta-function)
- [Selberg trace formula and zeta functions — M. Watkins](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/physics4.htm)
- [Riemann hypothesis — Wikipedia (Selberg zeta)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
