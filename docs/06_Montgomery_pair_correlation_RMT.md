---
id: doc-06
number: 06
title: "Montgomery Pair Correlation & Random Matrix Theory (GUE)"
category: spectral
status: open
tags: [montgomery, pair-correlation, GUE, random-matrix, odlyzko]
source_file: 06_Montgomery_pair_correlation_RMT.md
lang: en
---

# Montgomery Pair Correlation & Random Matrix Theory (GUE)

**Category:** Spectral approach / statistical evidence
**Authors / year:** Hugh Montgomery (1973), Freeman Dyson (1972/73), Andrew Odlyzko (1980s, numerical)
**Type:** Statistical conjecture & numerical evidence
**Status:** Conjecture (partly conditionally proven under RH); strong numerical confirmation

## Summary
In 1973 Hugh Montgomery computed the **pair correlation** of the imaginary parts of the non-trivial ζ zeros. In a famous conversation at the Institute for Advanced Study, the physicist Freeman Dyson immediately recognized this formula as the pair-correlation function of the eigenvalues of large random Hermitian matrices from the **Gaussian Unitary Ensemble (GUE)**. This unexpected bridge between number theory and quantum physics is regarded as one of the most important supports of the Hilbert–Pólya program.

## Core idea / the formula
- Montgomery showed (assuming the RH) that the normalized zero spacings have a pair-correlation function of the form:

```
R₂(u) = 1 − (sin(πu)/(πu))² + δ(u)
```

- This is exactly the function that describes the eigenvalue pair correlation in the GUE of random matrix theory.
- Interpretation: the zeros "repel each other" (level repulsion) like the energy levels of a quantum-chaotic system — they are *not* distributed like random independent points (Poisson).

## Numerical confirmation (Odlyzko)
- In the 1980s Andrew Odlyzko computed millions of zeros at extremely large heights (e.g. near the 10²⁰-th zero) and compared spacing statistics with the GUE predictions.
- The agreement is astonishingly precise — known as the **Montgomery–Odlyzko law**. It extends to higher correlations and whole families of L-functions (Katz–Sarnak philosophy).

## Significance / context
- The strongest *statistical* evidence for the existence of a self-adjoint "Hilbert–Pólya operator" with chaotic dynamics (GUE universality class).
- Inspired the quantum-chaotic models (Berry–Keating, Doc. 08) and the moment conjectures (Keating–Snaith, Doc. 07).
- **Important caveat:** statistical mimicry is *not a proof* of the RH — it only shows that the zeros *behave* as if they came from such an operator; the operator itself is missing.

## Mathematical core (formulas, theorems, proof sketches)

### Normalization of the zeros
Because of the density (1/2π)log(T/2π) (Doc. 02), one rescales the imaginary parts γ to mean spacing 1:
```
γ̃ = γ · (1/2π) log(γ/2π)
```

### Montgomery's function and result (1973)
Define for α ∈ ℝ the pair-correlation sum (up to height T, under RH):
```
F(α, T) = (Σ_{0<γ,γ'≤T} T^{iα(γ−γ')} w(γ−γ')) / (Σ_{0<γ≤T} 1),   w(u) = 4/(4+u²)
```
**Montgomery's theorem (conditional on RH).** For |α| ≤ 1,
```
F(α, T) ~ |α| + T^{−2|α|} log T   (T → ∞), uniformly on compact subsets of (0,1).
```
**Montgomery's conjecture:** For |α| ≥ 1, F(α, T) ~ 1. By Fourier inversion it follows for every suitable test function r:
```
Σ_{γ≠γ'} r((γ̃ − γ̃')) ~ ∫ r(u) [ 1 − (sin(πu)/(πu))² ] du
```

### The pair-correlation function (GUE kernel)
```
R₂(u) = 1 − ( sin(πu)/(πu) )² + δ(u)
```
This is **exactly** the two-point correlation kernel of the Gaussian Unitary Ensemble (GUE): for Hermitian random matrices the n-point correlation is det[ K(x_i,x_j) ] with the **sine kernel** K(x,y) = sin(π(x−y))/(π(x−y)). Hence "level repulsion": R₂(u) → 0 like (πu)²/3 as u → 0 (cf. Poisson: R₂ ≡ 1, no repulsion).

### Dyson recognition & numerical confirmation
In 1972/73 Dyson immediately identified 1 − (sin πu/πu)² as the GUE kernel. Odlyzko numerically verified the **nearest-neighbor spacing distribution** p(s) (Wigner-surmise-like, p(s) ≈ (32/π²)s² e^{−4s²/π}) and higher correlations for millions of zeros near the 10²⁰-th — agreement to several decimal places.

### Limit as a proof
F(α,T) is only known *unconditionally under RH* for |α| ≤ 1; the range |α| ≥ 1 (Montgomery's conjecture) is open. Even if fully proven, it would be statistics, not an operator ⇒ no RH proof.

## Sources
- [Montgomery's pair correlation conjecture — Wikipedia](https://en.wikipedia.org/wiki/Montgomery's_pair_correlation_conjecture)
- [Montgomery's Pair Correlation Conjecture — Wolfram MathWorld](https://mathworld.wolfram.com/MontgomerysPairCorrelationConjecture.html)
- [Pair Correlation Conjecture for the Zeros of the Riemann Zeta-function I (arXiv 2503.15449)](https://arxiv.org/abs/2503.15449)
- [Correlations of eigenvalues and Riemann zeros (arXiv 0803.2795)](https://arxiv.org/pdf/0803.2795)
- [Andrew Odlyzko: Papers on Zeros of the Riemann Zeta Function](https://www-users.cse.umn.edu/~odlyzko/doc/zeta.html)
