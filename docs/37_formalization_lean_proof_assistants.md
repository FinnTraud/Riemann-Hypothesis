---
id: doc-37
number: 37
title: "Formalization: Lean, mathlib & Proof Assistants (verification infrastructure)"
category: verification
status: reference
tags: [lean, mathlib, formalization, proof-assistant, prime-number-theorem]
source_file: 37_formalization_lean_proof_assistants.md
lang: en
---

# Formalization: Lean, mathlib & Proof Assistants (verification infrastructure)

**Category:** Infrastructure / verification (not a solution approach, but "bulletproof"-relevant)
**Authors / years:** Loeffler & Stoll (zeta/L-functions in Lean, 2025); Kontorovich & Tao (PrimeNumberTheorem+); mathlib community
**Type:** Machine-verified mathematics
**Status:** RH is formalized in Lean as a *statement*; proof open. PNT formalized.

## Summary
Proof assistants (Lean 4 / mathlib, Coq, Isabelle) allow **machine-checked** proofs in which every step is verified against the axioms — no gaps, no hallucination. For a "bulletproof" RH server this is the bridge between AI-generated ideas (Doc. 28) and certified correctness: a future RH proof (by human or AI) should be verified in such a system.

## Mathematical/technical core

### What is already formalized (Lean 4 / mathlib, as of 2025)
- **Riemann ζ and Dirichlet L-functions** as objects (Loeffler–Stoll, "Formalizing zeta and L-functions in Lean", arXiv 2503.00959): analytic continuation, functional equation, special values.
- **Dirichlet's theorem** on primes in arithmetic progressions (formal).
- **Formal statement of the Riemann Hypothesis** in mathlib (`RiemannHypothesis`) — the *claim* is precisely recorded; the proof is present only as a `sorry`-free statement.
- **Prime number theorem (PNT)** via Wiener–Ikehara: project **PrimeNumberTheorem+** (Kontorovich, Tao and others) — formalized, merge into mathlib planned; goals: explicit error term, PNT in progressions.
- **Irrationality of ζ(3)** (Apéry) formalized in Lean 4 (arXiv 2503.07625).

### What the RH statement looks like in Lean (schematic)
```lean
-- roughly (mathlib notation simplified):
theorem RiemannHypothesis :
    ∀ s : ℂ, riemannZeta s = 0 → s.re = 1/2 ∨ (∃ n : ℕ, s = -2*(n+1))
```
(i.e.: every zero is either critical or trivial — the trivial ones are excepted.)

### Why this matters for "bulletproof"
- **Verifiability:** a proof that goes through in Lean is guaranteed gapless (modulo kernel correctness) — this addresses exactly the hallucination problem of LLMs (Doc. 28) and the error types of failed proofs (Doc. 27).
- **AI synergy:** autoformalization + proof search (AlphaProof-like, Lean-Copilot) can generate candidate proofs that the kernel checks. This is the serious role of AI for the RH.
- **Partial goals:** even the formalization of intermediate results (Hardy, Levinson, Guth–Maynard, de Bruijn–Newman Λ≥0) would be valuable and checkable.

## Significance / context
- Not a solution *approach*, but the **quality assurance**: the system in which a found proof would have to hold up.
- Recommendation for the MCP server: use this document as a "verification gateway" — every claimed proof should be checked against the Lean statement form and the obstruction checklist (Doc. 35).

## Sources
- [Formalizing zeta and L-functions in Lean — Loeffler & Stoll (arXiv 2503.00959)](https://arxiv.org/pdf/2503.00959)
- [A Formal Proof of the Irrationality of ζ(3) in Lean 4 (arXiv 2503.07625)](https://arxiv.org/pdf/2503.07625)
- [Lean4 — Terence Tao (Blog, PrimeNumberTheorem+)](https://terrytao.wordpress.com/tag/lean4/)
- [Formalizing zeta and L-functions in Lean — Annales (afm.episciences.org)](https://afm.episciences.org/15954)
