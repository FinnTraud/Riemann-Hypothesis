---
id: doc-24
number: 24
title: "Numerical Verification of the Riemann Hypothesis"
category: numerical
status: reference
tags: [computation, odlyzko, platt, zetagrid, turing-method, verification]
source_file: 24_computational_verification.md
lang: en
---

# Numerical Verification of the Riemann Hypothesis

**Category:** Numerical evidence
**Authors / years:** Turing (1953), Lehmer (1956), van de Lune–te Riele–Winter (1986), Odlyzko (1980s–2001), Wedeniwski/ZetaGrid (2001–2005), Gourdon–Demichel (2004), Platt (rigorous, 2010s)
**Type:** Computer verification (evidence, not proof)
**Status:** RH confirmed for the first >10^13 zeros; no counterexample found

## Summary
Since the first hand computations (Riemann, Gram, Backlund, Hutchinson) the RH has been numerically verified for ever more zeros. All non-trivial zeros computed so far lie **exactly on** the critical line Re(s) = 1/2. This is strong evidence — but **not a proof** (there could be a counterexample beyond the computational limit, cf. the refuted Mertens conjecture, Doc. 16).

## Methodology (brief overview)
- **Hardy Z-function** (Doc. 03): real-valued, |Z(t)| = |ζ(1/2+it)|. A sign change of Z(t) ⇒ a zero on the line.
- **Riemann–Siegel formula** (Doc. 01): efficient evaluation of ζ on the line.
- **Gram points / Turing method:** count whether *all* expected zeros up to height T have been found (compared with the Riemann–von Mangoldt formula N(T), Doc. 02). If the number of zeros found on the line matches N(T), then *all* zeros up to T lie on the line.
- **Odlyzko–Schönhage algorithm:** fast multiple evaluation of ζ → computation of very many/very high zeros.

## Milestones
| Year | Who | Extent |
|---|---|---|
| 1903 | Gram | first ~15 zeros |
| 1953 | Turing | computer + Turing method |
| 1986 | van de Lune, te Riele, Winter | first 1.5 · 10^9 zeros |
| 1980s–2001 | Odlyzko | statistics near the 10^20-th / 10^22-nd zero (test of the GUE correlations, Doc. 06) |
| 2001–2005 | Wedeniwski, **ZetaGrid** | distributed computing (>10,000 machines, >70 countries), first ~9 · 10^11 zeros; >1 billion zeros/day |
| 2004 | Gourdon & Demichel | first **10^13** zeros (Odlyzko–Schönhage) |

## Rigorous verification (Platt)
- Many early verifications used non-rigorous floating-point arithmetic. **David Platt** developed procedures with **interval arithmetic** (rigorous error bounds) and verified the RH **rigorously** up to a height of about H = 3.06 · 10^10 — i.e. mathematically certified, not merely numerically plausible. These rigorous bounds are the basis for conditional/unconditional number-theoretic results (e.g. the ternary Goldbach conjecture, Helfgott).

## Significance / context
- Massive evidence *for* the RH: not a single counterexample among >10^13 zeros.
- **Fundamental limit:** numerics can never prove the RH (infinitely many zeros). The Mertens conjecture warns: at ~10^30, numerical evidence would have misled.
- Important for the critical assessment of data-driven / AI-assisted "confirmations" of the RH (Doc. 28).

## Mathematical core (formulas, procedures, computations)

### Riemann–Siegel formula (evaluation on the line)
```
Z(t) = 2 Σ_{n=1}^{N} n^{−1/2} cos(θ(t) − t log n) + R(t),   N = ⌊√(t/2π)⌋,
θ(t) = (t/2) log(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760 t³) + …
R(t) = (−1)^{N−1} (2π/t)^{1/4} [ Ψ(p) + corrections ],  p = √(t/2π) − N,  Ψ(p)=cos(2π(p²−p−1/16))/cos(2πp).
```
Cost O(√t) per evaluation (instead of O(t)). Sign changes of Z localize zeros.

### Turing method (completeness proof)
One counts the found sign changes of Z on [0,T] and compares with
```
N(T) = θ(T)/π + 1 + S(T),   S(T) = (1/π) arg ζ(1/2 + iT).
```
Turing showed that ∫_{T}^{T'} S(t) dt is small and bounded, so that from
```
| (found count) − θ(T)/π − 1 | < (Turing bound)
```
it follows that *all* zeros up to T have been found — and all lie on the line. If the counted line zeros = N(T), then RH is verified up to height T.

### Gram points
Gram points g_n: θ(g_n) = nπ. "Gram's law": usually exactly one zero lies between consecutive Gram points ((−1)^n Z(g_n) > 0). Exceptions (Gram-point failure) are handled with the Turing method.

### Odlyzko–Schönhage algorithm
Speeds up the *simultaneous* evaluation of ζ(1/2 + it) at many points t via fast multipoint evaluation of the Dirichlet sum (FFT-like band limiting / Taylor expansion of Σ n^{−it}). Amortized cost O(t^{1/2+o(1)}) for ~t^{1/2} closely spaced values ⇒ mass computation of very high zeros.

### Rigorous verification (interval arithmetic, Platt)
Instead of floating point, Platt uses **interval arithmetic** with guaranteed error bounds and a rigorous version of the Turing method. Verified: the RH holds rigorously for all zeros with 0 < Im < ~3.06·10^{10}. A basis, among other things, for Helfgott's proof of the ternary Goldbach conjecture.

### Status of the computations
| Bound | Method |
|---|---|
| 10^{13} zeros (Gourdon–Demichel 2004) | Odlyzko–Schönhage, floating point |
| ~9·10^{11} (ZetaGrid) | distributed, van de Lune software |
| rigorous up to height 3.06·10^{10} (Platt) | interval arithmetic |
All zeros found: simple and exactly on Re(s) = 1/2.

## Sources
- [Andrew Odlyzko: Papers & tables on Zeros of the Riemann Zeta Function](https://www-users.cse.umn.edu/~odlyzko/doc/zeta.html)
- [ZetaGrid — Wikipedia](https://en.wikipedia.org/wiki/ZetaGrid)
- [Wedeniwski/ZetaGrid — GitHub](https://github.com/Wedeniwski/ZetaGrid)
- [Computation of zeros of the Zeta function — X. Gourdon & P. Sebah](http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeroscompute.html)
- [Riemann Zeta Function Zeros — Wolfram MathWorld](https://mathworld.wolfram.com/RiemannZetaFunctionZeros.html)
