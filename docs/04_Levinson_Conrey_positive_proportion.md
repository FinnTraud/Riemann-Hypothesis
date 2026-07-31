---
id: doc-04
number: 04
title: "Levinson, Conrey & Co.: Positive Proportion of Zeros on the Critical Line"
category: partial-results
status: proven
tags: [levinson, conrey, mollifier, positive-proportion, speiser]
source_file: 04_Levinson_Conrey_positive_proportion.md
lang: en
---

# Levinson, Conrey & Co.: Positive Proportion of Zeros on the Critical Line

**Category:** Partial result
**Authors / years:** Norman Levinson (1974), J. Brian Conrey (1989), Conrey–Iwaniec–Soundararajan and others (>2010)
**Type:** Proven quantitative partial results on the RH
**Status:** Proven; currently >41% established, full RH (100%) open

## Summary
A series of papers proves that a *positive fraction* of all non-trivial zeros lie on the critical line — quantitatively much more than Hardy's "infinitely many". The evolution of the proven lower bound:
- **Selberg (1942):** a positive (small) proportion.
- **Levinson (1974):** at least **1/3** (≈ 33.3%).
- **Conrey (1989):** at least **2/5** (= 40%).
- **Later work (Bui–Conrey–Young, Feng, Pratt–Robles and others, from ~2011):** **over 41%**.

## Core idea: the Levinson–Conrey mollifier method
- One does not count the zeros of ζ on the line directly, but exploits a relationship between the zeros of ζ and the zeros of its derivative ζ′ (resp. a modified function).
- A **mollifier** (a cleverly chosen Dirichlet polynomial) "smooths" the zeta function near the critical line, so that one can control the relevant sign changes / the argument principle and bound the number of zeros on the line from below.
- Refinements consist mainly of more sophisticated mollifiers (longer Dirichlet polynomials, two-piece mollifiers) and sharper asymptotic analysis of the resulting moment integrals.

## Related: the Speiser theorem
- Speiser (1934) showed: the RH is equivalent to ζ′(s) having no zeros in the strip 0 < Re(s) < 1/2. The Levinson method exploits this connection between the zeros of ζ and ζ′.

## Significance / context
- The strongest result *toward* the RH with classical methods: over 41% of all zeros are provably on the line.
- Limit of the method: mollifier techniques seem unable to exceed a proportion well below 100% — in principle they provide **no** route to the full RH (one would need exactly 100% *and* the exclusion of any exception).
- Closely connected to random matrix theory (moments of ζ, Doc. 07) and density estimates (Doc. 17).

## Mathematical core (formulas, theorems, proof sketches)

### Levinson's method (1974) — formulas
Central quantity: count zeros via the argument principle for a modified function. Levinson considers
```
G(s) = ξ(s) + (correction),   or the function  B(s) = ½ + (1/log T)·ζ'(s)/ζ(s)
```
and uses **Speiser's equivalence** (RH ⟺ ζ'(s) ≠ 0 for Re(s) < 1/2). The key is a **mollifier** — a Dirichlet polynomial
```
M(s) = Σ_{n ≤ y} μ(n) P(log(y/n)/log y) · n^{−(s−1/2)}/ ...,   y = T^θ
```
that "smooths" |ζ| near the line. One shows that the number of sign changes (resp. real zeros) of an associated real function is at least
```
N₀(T) ≥ κ · N(T),   κ = 1 − (1/R) log( (1/(2πi)) ∮ ... )
```
where R = log(y)/log(T) (mollifier length) and a mean-value integral
```
I = (1/T) ∫_0^T |V·M (1/2 + it)|² dt
```
is evaluated asymptotically (V a linear combination of ζ and ζ'). Levinson obtains κ = 1/3 with θ = 1/2 − ε.

### Conrey (1989) and beyond
- Conrey lengthened the mollifier to θ = 4/7 − ε (via Kloosterman-sum estimates) ⇒ **κ ≥ 2/5 = 0.40**.
- Two-piece mollifiers M = M₁ + M₂ (Feng; Bui–Conrey–Young; Pratt–Robles–Zaharescu) ⇒ **κ > 0.41** (current record range ~0.4172).
- General form of the main term to be evaluated (mollified second moment):
```
(1/T)∫_0^T |ζ(1/2+it)|² |M(1/2+it)|² dt ~ c(P) · log T
```
with a functional c(P) in the mollifier polynomial P, which one optimizes variationally (Euler–Lagrange equation for P).

### Why the method stalls below 100%
The mollifier length θ is limited by the available mean-value theorems (second/fourth moments, large sieve); even θ → 1 (under strong conjectures) yields κ well below 1. So there is no known way to reach κ = 1 *and* the exclusion of all exceptions via mollifiers.

## Sources
- [More than 41% of the zeros of the zeta function are on the critical line (ResearchGate)](https://www.researchgate.net/publication/45902466_More_than_41_of_the_zeros_of_the_zeta_function_are_on_the_critical_line)
- [Zeros on the Critical Line — E. Naslund (UBC)](https://personal.math.ubc.ca/~gerg/teaching/613-Winter2011/ZerosCriticalLine.pdf)
- [On a choice of the mollified function in the Levinson-Conrey method (arXiv 1403.5786)](https://arxiv.org/pdf/1403.5786)
- [Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Riemann_hypothesis)
