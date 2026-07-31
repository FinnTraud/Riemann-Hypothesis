---
id: doc-29
number: 29
title: "The Jensen–Pólya Program: Laguerre–Pólya Class & Jensen Polynomials (Griffin–Ono–Rolen–Zagier 2019)"
category: solution-program
status: open
tags: [jensen-polya, laguerre-polya, griffin-ono-rolen-zagier, turan-inequalities, hyperbolicity]
source_file: 29_Jensen_Polya_Laguerre_Polya_GORZ.md
lang: en
---

# The Jensen–Pólya Program: Laguerre–Pólya Class & Jensen Polynomials (Griffin–Ono–Rolen–Zagier 2019)

**Category:** Active solution approach (equivalent reformulation + progress)
**Authors / years:** Pólya (1927), Jensen, Newman; Griffin, Ono, Rolen, Zagier (2019)
**Type:** Criterion equivalent to the RH + new progress
**Status:** Equivalence proven; GORZ proved hyperbolicity for degree ≤ 8 and a density-1 subset; full RH open

## Summary
The RH is **equivalent** to the Riemann ξ-function belonging to the **Laguerre–Pólya class** (entire functions with *only real* zeros). This in turn is equivalent to the **hyperbolicity (real-rootedness) of all Jensen polynomials** formed from the Taylor coefficients of ξ. Griffin, Ono, Rolen, and Zagier (2019) achieved substantial progress here — one of the most tangible modern "partial solution routes".

## The chain of equivalences
```
RH  ⟺  ξ ∈ Laguerre–Pólya class (only real zeros)
    ⟺  all Jensen polynomials J_d^{(n)}(ξ) are hyperbolic (only real roots)
    ⟺  all higher Turán/Laguerre inequalities for the (shifted) Taylor coefficients hold
```
- **Jensen polynomials:** from the Maclaurin coefficients of a function one forms, for each degree d and shift n, a polynomial J_d^{(n)}. "Hyperbolic" = all roots real.
- **Turán inequalities:** concrete (infinitely many) polynomial inequalities on the coefficients — a very "explicit" form of the RH.

## The result of Griffin–Ono–Rolen–Zagier (2019, PNAS / arXiv 1902.07321)
- **Modeling by Hermite polynomials:** they proved a general theorem that the Jensen polynomials (suitably scaled) converge in the limit to **Hermite polynomials** — and Hermite polynomials are known to be hyperbolic.
- **Concrete results for ξ:**
  - hyperbolicity for **all degrees d ≤ 8** (previously known only for d ≤ 3).
  - hyperbolicity for a **density-1 subset** of the Jensen polynomials of each degree (asymptotically almost all).
  - extension to the Jensen–Pólya program for general L-functions (arXiv 1905.11269).
- Side result: a precise asymptotic formula for the central derivatives of ζ; connection to the SYK model of physics.

## Critical assessment (important!)
- The result does **not** prove the RH: hyperbolicity "for all d up to 8" and "for density 1" is far from "for *all* d and *all* n".
- There is explicit skepticism: the paper **"Jensen polynomials are not a plausible route to proving the Riemann Hypothesis"** (arXiv 2008.07206) argues that this route fails at a fundamental hurdle — the Hermite approximation precisely does *not* control the regimes decisive for the full RH.
- Nonetheless: a concrete, checkable, actively researched reformulation with genuine progress — relevant for the knowledge base.

## Connection to other documents
- Closely related to the **de Bruijn–Newman constant** (Doc. 23): Λ ≤ 0 ⟺ ξ ∈ Laguerre–Pólya. Pólya's study of Fourier transforms of positive functions is the common root.
- Positivity/real-rootedness leitmotiv as in Weil positivity (Doc. 14) and de Branges (Doc. 20).

## Mathematical core (formulas, theorems, proof sketches)

### Laguerre–Pólya class (LP)
An entire function belongs to LP if it is a locally uniform limit of real polynomials with only real zeros. Characterization (Hadamard product):
```
f(x) = c x^m e^{−a x² + b x} ∏_k (1 − x/x_k) e^{x/x_k},   a ≥ 0, b,c,x_k ∈ ℝ,  Σ 1/x_k² < ∞.
```
**Theorem (Pólya).** RH ⟺ ξ(1/2 + iz) ∈ LP (as a function of z, only real zeros z = γ_n).

### Jensen polynomials
For a real sequence (a(k)) (here: Taylor coefficients, ξ(1/2+iz) = Σ a(k) z^{2k}/k! or similar) define
```
J^{d,n}(X) = Σ_{j=0}^d binom(d,j) a(n+j) X^j.
```
"Hyperbolic" := only real roots. **Theorem:** f ∈ LP ⟺ all J^{d,n} (d,n ≥ 0) are hyperbolic. Hence:
```
RH  ⟺  J^{d,n} hyperbolic for all d, n  (for the ξ coefficients).
```

### Higher Turán inequalities (equivalent concrete form)
Hyperbolicity for small d corresponds to explicit inequalities on the coefficients:
```
d = 2 (Turán):     a(n)² − a(n−1) a(n+1) ≥ 0,
d = 3 (higher T.):  4(a_n² − a_{n−1}a_{n+1})(a_{n+1}² − a_n a_{n+2}) − (a_n a_{n+1} − a_{n−1}a_{n+2})² ≥ 0,
```
and so on for each d — a sequence of increasingly complex but elementary polynomial inequalities whose *totality* is the RH.

### GORZ main theorem (2019): Hermite limit
**Theorem (Griffin–Ono–Rolen–Zagier).** Suitably normalized (with shift/scaling g(n), δ(n)), the Jensen polynomials converge to the **Hermite polynomials** H_d:
```
lim_{n→∞}  ( δ(n)^{−d} J^{d,n}( δ(n) X − g(n) ) / a(n) )  =  H_d(X),
```
uniformly on compact sets. Since the H_d have only real roots and these are "stable", it follows:
- **hyperbolicity for each fixed d and all n ≥ N(d)** (i.e. for a density-1 subset of each degree).
- Explicitly verified for ξ: **all d ≤ 8** fully hyperbolic.
Asymptotics of the central derivatives (key lemma): a(n) determined from
```
a(n) ~ (main term via saddle-point method on ∫ Φ(u) u^{2n} du), Φ as in Doc. 23.
```

### Criticism (arXiv 2008.07206)
The Hermite approximation only controls the regime n → ∞ at **fixed** d. For the RH one needs d and n *jointly* large (d ~ n). Exactly there the Hermite control fails — hence "not a plausible route to the full RH". Realistically GORZ is a strong result about the *distribution* of the Jensen roots, not about all of them simultaneously.

## Sources
- [Jensen polynomials for the Riemann zeta function and other sequences — PNAS (Griffin, Ono, Rolen, Zagier)](https://www.pnas.org/doi/10.1073/pnas.1902572116)
- [Jensen polynomials for the Riemann zeta function and other sequences (arXiv 1902.07321)](https://arxiv.org/pdf/1902.07321)
- [The Jensen-Pólya program for various L-functions (arXiv 1905.11269)](https://arxiv.org/abs/1905.11269)
- [Jensen polynomials are not a plausible route to proving the Riemann Hypothesis (arXiv 2008.07206)](https://arxiv.org/pdf/2008.07206)
- [On a new class of Laguerre-Pólya type functions with applications in number theory (arXiv 2108.01827)](https://ar5iv.labs.arxiv.org/html/2108.01827)
