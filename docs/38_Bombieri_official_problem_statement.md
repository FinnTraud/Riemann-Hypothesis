---
id: doc-38
number: 38
title: "Bombieri's Official Clay Problem Statement (Millennium Problem)"
category: reference
status: reference
tags: [bombieri, clay, millennium-problem, official-statement]
source_file: 38_Bombieri_official_problem_statement.md
lang: en
---

# Bombieri's Official Clay Problem Statement (Millennium Problem)

**Category:** Reference / authoritative problem statement
**Author / year:** Enrico Bombieri, 2000 (Clay Mathematics Institute)
**Type:** Official formulation of the Millennium Prize Problem
**Status:** Authoritative reference; prize ($1M) unawarded

## Summary
Enrico Bombieri wrote the **official problem description** of the Riemann Hypothesis for the Millennium Prize Problems of the Clay Mathematics Institute (2000). It is the authoritative reference for the exact formulation, the context, and the accepted equivalent versions.

## Mathematical core (formulas & theorems)

### Official statement
The ζ-function (Re s > 1: ζ(s) = Σ n^{−s} = ∏_p (1−p^{−s})^{−1}), continued to ℂ, satisfies, with the completed function
```
ξ(s) = (1/2) s(s−1) π^{−s/2} Γ(s/2) ζ(s),   ξ(s) = ξ(1−s),
```
**Riemann Hypothesis:** all zeros of ξ(s) have Re(s) = 1/2.

### Bombieri's equivalent formulation (ξ on the critical line)
Define the real function on the line:
```
Ξ(t) = ξ(1/2 + it)   (real-valued for real t).
```
**RH ⟺** all local maxima of Ξ(t) are positive and all local minima are negative (i.e. between every two consecutive extrema there is a sign change ⇒ all zeros real ⇒ on the line).

### Functional equation & Hadamard product (in the official presentation)
```
ξ(s) = ξ(0) ∏_ρ (1 − s/ρ)   (product over the non-trivial zeros, suitably paired),
ζ(s) = π^{s/2} / (Γ(s/2)) · ξ(s) / ((1/2)s(s−1)).
```

### Connection to primes (von Mangoldt, in the problem description)
```
ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − (1/2)log(1−x^{−2}),
RH ⟺ ψ(x) = x + O(√x log²x).
```

## Significance / context
- **Authoritative source** for the exact formulation and accepted equivalences — ideal as "ground truth" in the MCP server.
- Contains Bombieri's discussion of the function-field case (Weil/Deligne, Doc. 18) as motivation and of the spectral interpretation (Hilbert–Pólya, Doc. 05).
- Implicitly defines the Clay Institute's acceptance criteria (publication + 2 years of standing, cf. Doc. 27).

## Sources
- [Problems of the Millennium: the Riemann Hypothesis — E. Bombieri (Clay, PDF)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
- [Riemann Hypothesis — Clay Mathematics Institute](https://www.claymath.org/millennium/riemann-hypothesis/)
- [The Riemann Hypothesis — E. Bombieri (UC Davis Mirror)](https://www.math.ucdavis.edu/~tracy/courses/math205A/riemann.pdf)
