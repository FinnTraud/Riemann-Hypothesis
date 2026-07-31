---
id: doc-40
number: 40
title: "Glossary & Notation (terms, symbols, definitions)"
category: glossary
status: reference
tags: [glossary, notation, definitions]
source_file: 40_glossary_notation.md
lang: en
---

# Glossary & Notation (terms, symbols, definitions)

**Category:** Reference (improves RAG retrieval for terminology questions)
**Type:** Collection of definitions
**Status:** Stable

## Purpose
User questions often contain *terms* rather than names ("What is the critical line?", "What does GUE mean?"). This glossary increases the retrieval hit rate and links to the more detailed documents.

## Functions & their definitions
- **Riemann ζ:** ζ(s) = Σ_{n≥1} n^{−s} (Re s > 1), analytically continued; pole at s = 1. → Doc. 01
- **Euler product:** ζ(s) = ∏_p (1−p^{−s})^{−1}; encodes unique prime factorization; implies ζ ≠ 0 for Re s > 1. → Doc. 01, 35
- **Complete ζ / ξ-function:** ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s); entire; ξ(s) = ξ(1−s). → Doc. 01
- **Ξ(t):** Ξ(t) = ξ(1/2 + it), real-valued for real t. → Doc. 38
- **Hardy Z-function:** Z(t) = e^{iθ(t)} ζ(1/2+it), real; |Z| = |ζ(1/2+it)|. → Doc. 03
- **Riemann–Siegel θ:** θ(t) = arg Γ(1/4+it/2) − (t/2)log π. → Doc. 01, 24
- **von Mangoldt Λ:** Λ(n) = log p if n = p^k, else 0; −ζ'/ζ = Σ Λ(n)n^{−s}. → Doc. 02
- **Möbius μ:** μ(n) = (−1)^{#prime factors} if squarefree, else 0; 1/ζ = Σ μ(n)n^{−s}. → Doc. 16
- **Mertens M:** M(x) = Σ_{n≤x} μ(n). → Doc. 16
- **Chebyshev ψ:** ψ(x) = Σ_{n≤x} Λ(n); ψ(x) ~ x. → Doc. 02
- **Prime-counting function:** π(x) = #{p ≤ x}; π(x) ~ Li(x). → Doc. 02
- **Li(x):** ∫_0^x dt/log t (logarithmic integral).
- **Dirichlet L:** L(s,χ) = Σ χ(n)n^{−s} = ∏_p(1−χ(p)p^{−s})^{−1}. → Doc. 21
- **Dedekind ζ_K:** zeta function of a number field K. → Doc. 34

## Terms
- **Critical strip:** 0 < Re(s) < 1 (region of the non-trivial zeros).
- **Critical line:** Re(s) = 1/2 (conjectured location of *all* non-trivial zeros).
- **Trivial zeros:** s = −2, −4, −6, … (from the functional equation).
- **Non-trivial zeros:** ρ = β + iγ in the critical strip; γ = imaginary part / "height".
- **Functional equation:** ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s); symmetry s ↔ 1−s.
- **Zero-free region:** region near Re = 1 in which ζ ≠ 0 is proven. → Doc. 12
- **Counting function N(T):** number of zeros with 0 < γ ≤ T ≈ (T/2π)log(T/2π). → Doc. 02
- **N(σ,T):** number of zeros with β ≥ σ, γ ≤ T (density off the line). → Doc. 17, 22
- **S(T):** (1/π) arg ζ(1/2+iT), fluctuation term in N(T). → Doc. 02

## Statistics / physics
- **GUE (Gaussian Unitary Ensemble):** ensemble of random Hermitian matrices; eigenvalue pair correlation 1−(sin πu/πu)². → Doc. 06
- **CUE (Circular Unitary Ensemble):** Haar-random unitary matrices; model for ζ moments. → Doc. 07
- **Pair correlation:** distribution of the spacings γ−γ'. → Doc. 06
- **Level repulsion:** zeros avoid close spacings (R₂(u) → 0 as u → 0).
- **Lehmer pair:** two extremely close zeros. → Doc. 23, 35
- **KMS state:** quantum-statistical equilibrium state. → Doc. 34

## Criterion keywords
- **Koch:** π(x) = Li(x) + O(√x log x) ⟺ RH. → Doc. 02
- **Robin:** σ(n) < e^γ n log log n (n > 5040) ⟺ RH. → Doc. 15
- **Li coefficients λ_n:** λ_n ≥ 0 ∀n ⟺ RH. → Doc. 14
- **Weil positivity:** W(g⋆ḡ) ≥ 0 ⟺ RH. → Doc. 14
- **Nyman–Beurling:** density of a function space ⟺ RH. → Doc. 13
- **de Bruijn–Newman Λ:** Λ ≤ 0 ⟺ RH. → Doc. 23
- **Laguerre–Pólya:** ξ ∈ LP ⟺ RH. → Doc. 29

## Generalizations
- **GRH:** RH for all Dirichlet L-functions. → Doc. 21
- **Grand RH:** RH for all automorphic L-functions. → Doc. 21
- **Selberg class:** axiomatic class of L-functions. → Doc. 21
- **RH over 𝔽_q:** RH analogue for curves over finite fields (PROVEN). → Doc. 18
