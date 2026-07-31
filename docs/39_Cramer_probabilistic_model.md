---
id: doc-39
number: 39
title: "The Cramér Model & Probabilistic Heuristics of the Primes"
category: heuristic
status: open
tags: [cramer-model, probabilistic, prime-gaps, maier-theorem]
source_file: 39_Cramer_probabilistic_model.md
lang: en
---

# The Cramér Model & Probabilistic Heuristics of the Primes

**Category:** Heuristic / probabilistic model
**Authors / years:** Harald Cramér (1936); refinements Granville, Maier
**Type:** Heuristic model (not a proof approach, but a source of intuition)
**Status:** Heuristic; partly corrected in detail (Maier)

## Summary
The Cramér model treats the primes as a **random sequence** and yields predictions about prime gaps that are compatible with the RH world but independent of it. It is the most important *probabilistic intuition* behind conjectures about the fine distribution of the primes and explains why the zero statistics (GUE, Doc. 06) appear as "randomness with repulsion".

## Mathematical core (formulas & conjectures)

### The model
Model "n is prime" as independent events with probability 1/log n (motivated by the prime number theorem). Expected number of primes up to x: ∫_2^x dt/log t = Li(x). ✓

### Cramér conjecture (prime gaps)
```
limsup_{n→∞} (p_{n+1} − p_n) / (log p_n)²  =  1.
```
I.e. maximal gaps grow like (log p)². **Important:** this prediction is *stronger* than anything that follows from RH — RH gives only O(√p log p) (Doc. 36). So the model goes beyond the RH.

### Granville correction
The naive model ignores multiplicativity (small prime divisors). Granville corrected the factor; today one conjectures
```
limsup (p_{n+1} − p_n)/(log p_n)²  ≥  2 e^{−γ} ≈ 1.1229.
```

### Maier's theorem (the model is not exact)
**Theorem (Maier 1985).** The Cramér model predicts an asymptotic equidistribution of primes in *very short* intervals [x, x + (log x)^λ] — this is **false**. The actual count fluctuates by a factor that does not tend to 1. ⇒ probabilistic models are heuristics, not a substitute for analytic proofs.

## Significance / context
- Provides the **intuition** for why the ζ zeros behave like a "random system with level repulsion" (GUE, Doc. 06) — primes ≈ random, zeros ≈ their Fourier dual.
- **Warning (for "bulletproof"):** Maier's theorem shows that plausible probabilistic heuristics can be *false* in detail — analogous to the Mertens warning (Doc. 16, 35). A proof may never rely on the model.
- Not a solution approach for the RH, but indispensable context for interpreting the statistics.

## Sources
- [Cramér's conjecture — Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture)
- [Harald Cramér and the distribution of prime numbers — A. Granville](https://dms.umontreal.ca/~andrew/PDF/cramer.pdf)
- [Beyond the Riemann hypothesis — primes and smooth numbers (Oxford)](https://www.maths.ox.ac.uk/node/65844)
