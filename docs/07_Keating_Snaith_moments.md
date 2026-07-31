---
id: doc-07
number: 07
title: "Keating–Snaith: Moments of the Zeta Function via Characteristic Polynomials (CUE)"
category: spectral
status: open
tags: [keating-snaith, moments, CUE, random-matrix, barnes-G]
source_file: 07_Keating_Snaith_moments.md
lang: en
---

# Keating–Snaith: Moments of the Zeta Function via Characteristic Polynomials (CUE)

**Category:** Spectral approach / random matrix theory
**Authors / year:** Jonathan Keating, Nina Snaith (2000)
**Type:** Conjecture (modeling), supported by RMT
**Status:** Conjecture; proven in special cases, open in general

## Summary
In 2000 Keating and Snaith proposed modeling the Riemann zeta function on the critical line by the **characteristic polynomial of a random unitary matrix** (Circular Unitary Ensemble, CUE). This model yields precise predictions for the **moments** of ζ(1/2 + it) — a long-standing open problem of analytic number theory in which the random matrix model "guesses" the correct constants.

## Core idea
- On the critical line, ζ(1/2 + it) behaves statistically like the characteristic polynomial Z(U, θ) of a Haar-random unitary N×N matrix U, where the matrix size N ≈ log(T/2π) corresponds to the local zero density.
- For the CUE, moments can be computed exactly (product formulas with Gamma/Barnes-G functions). Transferred to ζ, this gives the **Keating–Snaith conjecture** for the 2k-th moments:

```
(1/T) ∫₀ᵀ |ζ(1/2 + it)|^{2k} dt  ~  a_k · g_k · (log T)^{k²}
```

- Here (log T)^{k²} is the growth exponent predicted by RMT, g_k is a "random matrix constant" arising from the Barnes-G-function limit, and a_k is a purely number-theoretic arithmetic factor (Euler product).

## Status of the proofs
- k = 1 (Hardy–Littlewood) and k = 2 (Ingham) are classically proven.
- The full moment conjecture for general k is **open**; but random matrix theory provides the presumably correct constants, which agree with independent number-theoretic heuristics (Conrey–Ghosh, Conrey–Gonek).
- Extensions: moments of derivatives ζ′, joint moments, "moments of moments", log-correlated fields, the Fyodorov–Hiary–Keating conjecture on the maximum of ζ in short intervals.

## Significance / context
- Makes the zeta–GUE correspondence *quantitative* and *predictive* (not just pair correlation as with Montgomery, Doc. 06).
- Provides deep structural evidence for a spectral/random-matrix origin of the zeros.
- Contributes indirectly to the RH (moment bounds ↔ proportion of zeros on the line, Doc. 04), but is not itself a route to the full RH.

## Mathematical core (formulas, theorems, proof sketches)

### CUE side: characteristic polynomial
For U ∈ U(N) Haar-distributed, let Λ_U(θ) = det(I − U e^{−iθ}) = ∏_{n=1}^N (1 − e^{i(θ_n − θ)}). Keating–Snaith compute the moments exactly:
```
E_{U(N)} |Λ_U(θ)|^{2k} = ∏_{j=1}^N  Γ(j) Γ(j + 2k) / Γ(j + k)²
```
Large N (Barnes-G function G):
```
E |Λ|^{2k} ~ (G(1+k)² / G(1+2k)) · N^{k²}   (N → ∞)
```

### Translation into the zeta moments (conjecture)
Identify N ↔ log(T/2π) (same local density). Keating–Snaith conjecture for the 2k-th moments on the critical line:
```
(1/T) ∫_0^T |ζ(1/2 + it)|^{2k} dt  ~  a_k · g_k · (log T)^{k²}
```
with
```
g_k = G(1+k)² / G(1+2k)         (random matrix factor, from the CUE)
a_k = ∏_p [ (1 − 1/p)^{k²} Σ_{m≥0} (Γ(m+k)/(m! Γ(k)))² p^{−m} ]   (arithmetic factor, Euler product)
```

### Known special cases (proven)
```
k = 1:  (1/T)∫|ζ(1/2+it)|² dt ~ log T           (g_1 = 1, a_1 = 1; Hardy–Littlewood)
k = 2:  (1/T)∫|ζ(1/2+it)|⁴ dt ~ (1/2π²)(log T)⁴  (g_2 = 1/12, a_2 = 6/π²; Ingham)
```
The values g_1 = 1, g_2 = 1/12 reproduce exactly G(2)²/G(3) resp. G(3)²/G(5) — confirmation of the RMT model.

### Extensions
- Derivative moments: E|Λ'_U|² etc. ↔ moments of ζ' (Hughes, Conrey–Ghosh–Gonek).
- **Fyodorov–Hiary–Keating conjecture** for the maximum in short intervals:
```
max_{|h| ≤ 1} log|ζ(1/2 + i(t+h))| = log log T − (3/4) log log log T + O(1)
```
(log-correlated field, branching-random-walk analogy).

### Relation to the RH
Moment bounds ⇒ lower bounds for N₀(T)/N(T) (proportion on the line, Doc. 04); k = 0 behavior ↔ value distribution. Even the full moment conjecture does not imply the RH, but is part of the same spectral picture.

## Sources
- [Derivative Moments for Characteristic Polynomials from the CUE (Springer, Comm. Math. Phys.)](https://link.springer.com/article/10.1007/s00220-012-1512-1)
- [Moments of the Riemann Zeta Function and Log-Correlated Random Variables (Oxford)](https://ora.ox.ac.uk/objects/uuid:9bbc320c-9738-43ef-b0f0-f18bf4b7c0d6/files/dh415pb096)
- [On moments of the derivative of CUE characteristic polynomials and the Riemann zeta function (arXiv 2409.03687)](https://arxiv.org/html/2409.03687)
- [Freezing transition and moments of moments of the Riemann zeta function (Oxford QJM)](https://academic.oup.com/qjmath/article/75/4/1481/7925234)
