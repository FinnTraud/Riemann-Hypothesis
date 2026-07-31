---
id: doc-12
number: 12
title: "Zero-Free Regions (classical analytic approach)"
category: analytic
status: open
tags: [zero-free-region, vinogradov-korobov, de-la-vallee-poussin, prime-number-theorem]
source_file: 12_zero_free_regions.md
lang: en
---

# Zero-Free Regions (classical analytic approach)

**Category:** Analytic approach
**Authors / years:** Hadamard & de la Vallée Poussin (1896/1899), Littlewood (1922), Vinogradov–Korobov (1958), modern explicit refinements (2020s)
**Type:** Gradual approximation (not the full RH)
**Status:** Active; best asymptotic result for decades is Vinogradov–Korobov

## Summary
Instead of proving the RH directly, a century of analytic work pursues the goal of gradually enlarging the **region of the critical strip that is provably free of zeros** — squeezing the strip "from the right" toward the critical line. Every improvement yields more effective versions of the prime number theorem with error terms.

## Historical development of the zero-free region
(σ = Re(s), bound near σ = 1)

| Year | Author(s) | Zero-free region |
|---|---|---|
| 1896 | Hadamard, de la Vallée Poussin | ζ(1 + it) ≠ 0 ⇒ first proof of the prime number theorem |
| 1899 | de la Vallée Poussin | 1 − σ ≤ c / log t |
| 1922 | Littlewood | 1 − σ ≤ c · log log t / log t |
| 1938 | Chudakov | 1 − σ ≤ c / (log t)^{3/4 + ε} |
| 1958 | Vinogradov, Korobov | 1 − σ ≤ c / (log t)^{2/3} (log log t)^{1/3} |
| 2020s | various (explicit) | e.g. ζ(σ + it) ≠ 0 for t ≥ 3, σ ≥ 1 − 1/(4.896 · log t) |

## Core idea
- **Global method (Hadamard):** use the non-negativity of trigonometric polynomials (classically: 3 + 4cos θ + cos 2θ ≥ 0) together with the Euler-product / log-derivative structure to exclude zeros near σ = 1.
- **Local method (Landau):** local estimates of ζ.
- **Vinogradov–Korobov:** sharper estimates of exponential sums ⇒ larger zero-free region. The proof is considerably more involved, but the result only slightly stronger than de la Vallée Poussin's.

## Significance / context
- Provides *effective, explicit* (albeit weak) versions of the prime number theorem with error terms — practically important (e.g. for computations, cryptographically relevant prime densities).
- **Fundamental weakness:** a zero-free region, however small, only keeps zeros away from σ = 1 — it does not *fix* them at σ = 1/2. Hence it is in principle weaker than the RH.
- The Vinogradov–Korobov exponent (2/3) remained the best for ~70 years; recent decoupling-based work (cf. Guth–Maynard, Doc. 22) is beginning to shake exponents in related density estimates.

## Mathematical core (formulas, theorems, proof sketches)

### The 3+4cos+cos2 argument (de la Vallée Poussin)
The basis is the non-negative trigonometric identity
```
3 + 4 cos θ + cos 2θ = 2(1 + cos θ)² ≥ 0.
```
Applied to Re(log ζ) = Σ_{p,k} (1/k) p^{−kσ} cos(kt log p), for σ > 1 it gives:
```
3 log ζ(σ) + 4 Re log ζ(σ+it) + Re log ζ(σ+2it) ≥ 0
⟺  ζ(σ)³ |ζ(σ+it)|⁴ |ζ(σ+2it)| ≥ 1.
```
If ζ had a zero at 1 + it₀, then the left side would go to 0 as σ → 1⁺ (the factor |ζ(σ+it)|⁴ → 0 faster than ζ(σ)³ → ∞ diverges) — contradiction. ⇒ **ζ(1+it) ≠ 0** (prime number theorem). Quantifying the argument yields the region.

### de la Vallée Poussin (1899) — quantitative
With bounds |ζ'/ζ| ≪ log t near σ = 1, the argument above gives an explicit constant c > 0 with
```
ζ(σ + it) ≠ 0   for   σ > 1 − c/log|t|,   |t| ≥ 2.
```

### Vinogradov–Korobov (1958) — the method
Sharper estimates of **exponential sums** Σ_{n≤N} n^{−it} = Σ e^{−it log n} (Vinogradov's mean-value theorem / Weyl–van der Corput) give the subconvex bound
```
ζ(σ + it) ≪ |t|^{B(1−σ)^{3/2}} (log|t|)^{2/3}
```
and thus the best asymptotic zero-free region so far
```
ζ(σ+it) ≠ 0   for   σ ≥ 1 − c/( (log|t|)^{2/3} (log log|t|)^{1/3} ).
```

### Consequence for the prime number theorem (error term)
A region σ > 1 − η(t) yields, via contour shifting (Doc. 02),
```
ψ(x) − x ≪ x · exp( −c (log x)^{3/5} (log log x)^{−1/5} )   (Vinogradov–Korobov error term).
```
Under RH the error would be O(√x log²x) — exponentially better. This illustrates: zero-free region ⇒ error term, but strictly weaker than the RH.

## Sources
- [Zero-free regions for the Riemann zeta function (arXiv 1910.08205)](https://arxiv.org/pdf/1910.08205)
- [Explicit bounds on ζ(s) in the critical strip and a zero-free region (arXiv 2301.03165)](https://arxiv.org/pdf/2301.03165)
- [Zero-free regions inspired by work of Heath-Brown (arXiv 2603.21490)](https://arxiv.org/html/2603.21490)
- [Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function (arXiv 1410.3926)](https://arxiv.org/pdf/1410.3926)
