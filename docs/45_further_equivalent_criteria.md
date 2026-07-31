---
id: doc-45
number: 45
title: "Further Equivalent Criteria (Volchkov, Sekatskii, Redheffer, Salem, BBLS quantitative)"
category: criterion
status: open
tags: [volchkov, sekatskii, redheffer-matrix, salem, baez-duarte-quantitative]
source_file: 45_further_equivalent_criteria.md
lang: en
---

# Further Equivalent Criteria (Volchkov, Sekatskii, Redheffer, Salem, BBLS quantitative)

**Category:** Equivalent criteria (supplement to Doc. 13–16)
**Authors / years:** Salem (1953), Redheffer (1977), Volchkov (1995), Báez-Duarte–Balazard–Landreau–Saias (2000), Sekatskii–Beltraminelli–Merlini (2009–2012)
**Type:** Statements equivalent to the RH
**Status:** Equivalences proven; each unproven for ζ

## Summary
A collection of further criteria equivalent to the RH that are not in the main documents 13–16. They provide alternative analytic, integral, and matrix-based "attack surfaces".

## Mathematical core (formulas, theorems)

### Volchkov criterion (1995) — integral of log ζ
```
RH  ⟺  ∫_0^∞ (1 − 12t²)/(1 + 4t²)³ · log|ζ(1/2 + it)| dt  =  π(3 − γ)/32,
```
γ = Euler–Mascheroni constant. Equivalently, via the argument:
```
RH  ⟺  ∫_0^∞ [ 2t · arg ζ(1/2 + it) / (1/4 + t²)² ] dt = π(γ − 3).
```
An *equality* (not just an inequality) that holds exactly when no zero lies in the strip to the right of 1/2. Proof via the argument principle / generalized Littlewood theorem applied to log ζ.

### Sekatskii–Beltraminelli–Merlini (2009–2012) — a family of log-ζ equalities
Generalize Volchkov: by means of the **generalized Littlewood theorem** (contour integral of log ζ against an analytic function g) one obtains a whole **family** of equalities of the form
```
RH  ⟺  ∫ (weight_g(t)) log|ζ(1/2+it)| dt = (explicit constant),
```
parametrized by g. Each is individually RH-equivalent; provides infinitely many integral tests.

### Redheffer matrix criterion (1977)
Define the n×n matrix R_n with
```
(R_n)_{ij} = 1  if j = 1  or  i | j,   else 0.
```
Then det(R_n) = M(n) (the Mertens function, Doc. 16!). Therefore:
```
RH  ⟺  det(R_n) = O(n^{1/2 + ε})   for every ε > 0.
```
R_n has n−1 eigenvalues near 1 plus a few large ones; the determinant as a Mertens sum connects linear algebra/graph theory with the RH.

### Salem criterion (1953)
Via an integral equation of Wiener–Tauberian type: the non-vanishing of a certain integral transform (convolution kernel of the form e^{σx}/(e^{e^x}+1)) is equivalent to ζ(σ+it) ≠ 0 on a vertical line. Connects the RH with completeness/density (related to Nyman–Beurling, Doc. 13).

### BBLS — quantitative Nyman–Beurling distance (2000)
With d_N² = inf_{polynomial coeffs} ‖1 − Σ_{k≤N} c_k ρ_{1/k}‖²_{L²(0,1)} (cf. Doc. 13):
```
RH  ⟺  d_N → 0,   and under RH (simple zeros):  d_N² ~ (2 + γ − log 4π)/log N.
```
The explicit constant (2+γ−log 4π) makes this the **most concrete numerical target value** for an approximation-theoretic attack; the evaluation runs via an arithmetic Gram matrix (Vasyunin).

## Significance / context
- Extend the arsenal of equivalent formulations (integral, matrix, approximation form).
- Redheffer connects directly to the Mertens function (Doc. 16); Volchkov/Sekatskii offer *equalities* (sensitive tests); BBLS gives a computable target constant.
- **Open:** each is just as hard as the RH itself — they shift the problem, they do not solve it.

## Sources
- [On an equality equivalent to the Riemann hypothesis — Volchkov (Semantic Scholar)](https://www.semanticscholar.org/paper/On-an-equality-equivalent-to-the-Riemann-hypothesis-Volchkov/280edbe8824496a1dfb254fdbd41a2f215a26887)
- [Equalities involving integrals of the logarithm of the Riemann ζ equivalent to RH — Sekatskii et al. (arXiv 0806.1596)](https://arxiv.org/pdf/0806.1596)
- [The Riemann Hypothesis — AIM (Redheffer, Salem, Volchkov criteria)](https://www.aimath.org/WWN/rh/rh.pdf)
- [A strengthening of the Nyman-Beurling criterion — Báez-Duarte et al. (arXiv math/0202141)](https://arxiv.org/pdf/math/0202141)
