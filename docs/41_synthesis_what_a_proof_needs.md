---
id: doc-41
number: 41
title: "Synthesis: Cross-Cutting Themes & What a Successful Proof Must Achieve"
category: synthesis
status: meta
tags: [synthesis, positivity, spectral, geometry, necessary-conditions, evaluation]
source_file: 41_synthesis_what_a_proof_needs.md
lang: en
---

# Synthesis: Cross-Cutting Themes & What a Successful Proof Must Achieve

**Category:** Meta / synthesis (core document for "bulletproof")
**Type:** Cross-cutting analysis of all approaches
**Status:** Analytical summary

## Purpose
This document condenses the 40 individual documents into **patterns**: what do all serious approaches have in common? Which necessary conditions must a valid proof satisfy? It is the strategic "map" for an RH assistant.

## 1. Three recurring leitmotivs
Practically every serious approach can be assigned to one (or more) of these motifs:

### (A) Positivity / real-rootedness
RH as the statement that a **quadratic form is positive** resp. a function has **only real zeros**.
- Weil positivity W(g⋆ḡ) ≥ 0 (Doc. 14) · Li coefficients λ_n ≥ 0 (Doc. 14) · de Branges (Doc. 20) · Laguerre–Pólya / Jensen (Doc. 29) · Lee–Yang/Newman (Doc. 33) · de Bruijn–Newman Λ ≤ 0 (Doc. 23).
- **Common hurdle:** positivity is *reduced* to RH but not *proven* — and must not be assumed circularly (Doc. 35, point 3).

### (B) Spectral interpretation (Hilbert–Pólya)
Zeros = eigenvalues of a self-adjoint / canonical operator.
- Hilbert–Pólya (Doc. 05) · Berry–Keating (Doc. 08) · Bender–Brody–Müller (Doc. 09) · Connes trace formula (Doc. 10) · prolate operator (Doc. 11) · Selberg (Doc. 19, proven model) · Deninger (Doc. 31) · Bost–Connes (Doc. 34).
- **Common hurdle:** the operator must arise *canonically from arithmetic*; an invented operator is circular (Doc. 35, point 5).

### (C) Geometry / transferring the function-field case
RH over 𝔽_q is proven (Weil/Deligne, Doc. 18) via geometry + positivity of the intersection form. Transfer to ℤ:
- 𝔽₁ geometry / arithmetic site (Doc. 30) · Deninger cohomology (Doc. 31) · Connes adeles (Doc. 10).
- **Common hurdle:** the required geometry/cohomology over Spec(ℤ) does not yet exist.

## 2. Necessary conditions for EVERY valid proof
Distilled from the obstructions (Doc. 35):

1. **Use the Euler product essentially.** Davenport–Heilbronn (Doc. 35) shows: functional equation + continuation + growth do NOT suffice. The multiplicativity/prime structure must enter.
2. **Distinguish "with/without Euler product".** The argument must not apply to the Davenport–Heilbronn function.
3. **Actually prove positivity, do not assume it.** (Conrey–Li refuted de Branges' assumption, Doc. 20.)
4. **No pure numerics.** Mertens/Skewes (Doc. 35) show: finite evidence can deceive.
5. **Respect the convergence questions of the zero sum.** Σ_ρ is only conditionally convergent (Doc. 27).
6. **Circumvent the parity barrier.** Pure sieve methods do not suffice (Doc. 35, point 3).

## 3. Why the three motifs are connected
- The **explicit formula** (Doc. 02) is the common core: it links zeros (spectral) with primes (Euler product) and is read in (B)/(C) as a **trace formula**, in (A) as a **quadratic form** (Weil positivity).
- In the proven case (Doc. 18, 19) all three coincide: Selberg trace formula (B) = explicit formula, intersection positivity (A) = Weil's proof, geometry (C) = the curve. **This is the blueprint** — what is sought is its realization over ℤ.

## 4. Realistic milestones (what would be progress)
- Positive proportion → 50%+ → 100% on the line (Doc. 04) — but proportion methods alone do not suffice.
- Exponent improvement in N(σ,T) (Guth–Maynard, Doc. 22) → toward the density hypothesis (Doc. 17).
- Exclusion of Landau–Siegel zeros (Doc. 32) for the GRH.
- Λ ≤ 0 (de Bruijn–Newman, Doc. 23) — currently 0 ≤ Λ ≤ 0.22.
- Canonical construction of the Hilbert–Pólya operator / Weil positivity (Doc. 10, 31) — the "grand" route.

## 5. Evaluation grid for a proposed proof idea
| Question | If problematic → |
|---|---|
| Does it use the Euler product essentially? | No → probably wrong (Doc. 35) |
| Does it also apply to Davenport–Heilbronn? | Yes → wrong |
| Positivity proven or assumed? | Assumed → circular |
| Operator canonical from arithmetic? | No → circular/empty |
| Only finite numerics? | Yes → not a proof |
| Verifiable in Lean? (Doc. 37) | No → treat with caution |

## Sources (synthesized from)
- [The Riemann Hypothesis — E. Bombieri (Clay)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
- [On some reasons for doubting the Riemann hypothesis — Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- [The Riemann Hypothesis over Finite Fields — J. Milne](https://www.jmilne.org/math/xnotes/pRH.html)
- [An essay on the Riemann Hypothesis — A. Connes (arXiv 1509.05576)](https://arxiv.org/pdf/1509.05576)
- (as well as documents 01–40 of this knowledge base)
