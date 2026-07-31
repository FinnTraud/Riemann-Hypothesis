---
id: doc-36
number: 36
title: "Consequences of the Riemann Hypothesis (what follows if it is true)"
category: context
status: reference
tags: [consequences, prime-gaps, miller-rabin, class-numbers, GRH-applications]
source_file: 36_consequences_of_RH.md
lang: en
---

# Consequences of the Riemann Hypothesis (what follows if it is true)

**Category:** Context / implications
**Type:** Overview of the corollaries
**Status:** Conditional theorems (hold under RH / GRH)

## Summary
Hundreds of theorems are proved "conditionally under RH" — they would immediately hold unconditionally as soon as the RH is proved. This list shows *why* the RH is so central, and gives an RH assistant the application/consequence context. Some corollaries need the **GRH** (Doc. 21), not just the classical RH — this is noted in each case.

## Mathematical core (formulas & theorems)

### Prime distribution (RH)
```
π(x) = Li(x) + O(√x log x)        (Koch 1901; best possible error term)
ψ(x) = x + O(√x log²x)
|π(x) − Li(x)| < (1/8π) √x log x   for x ≥ 2657 (Schoenfeld, explicit under RH)
```

### Prime gaps (RH)
```
p_{n+1} − p_n = O(√(p_n) log p_n).
```
(Cramér under RH; unconditionally one is far from this. Note: the *Cramér conjecture* p_{n+1}−p_n = O(log²p_n) is stronger and does NOT follow from RH, Doc. 39.)

### Mertens / Möbius sums (RH)
```
M(x) = Σ_{n≤x} μ(n) = O(x^{1/2+ε}),   Σ_{n≤x} μ(n)/n = O(x^{−1/2+ε}).
```

### Miller–Rabin / primality tests (GRH)
Under GRH the **deterministic** Miller test is correct in polynomial time: a composite number n has a witness a ≤ 2(log n)². (Unconditionally, only AKS 2002 gives deterministic polynomial time — but slower.)

### Least quadratic non-residues / class numbers (GRH)
```
Least quadratic non-residue mod p  ≪ (log p)²   (Ankeny, under GRH).
Effective lower bounds for class numbers h(−d) (no Siegel zero, Doc. 32).
```

### Goldbach & additive problems
- The **ternary** Goldbach conjecture (every odd number > 5 is a sum of three primes) was proved **unconditionally by Helfgott** in 2013 — supported by rigorous RH verification up to a finite height (Platt, Doc. 24). Early proofs (Hardy–Littlewood) were conditional on GRH.

### Lindelöf & moments (RH ⇒)
```
ζ(1/2 + it) = O(t^ε)   (Lindelöf, Doc. 17).
```

### Growth of ζ and 1/ζ on the 1-line (RH)
```
1/ζ(1+it) = O(log log t),   |ζ(1+it)| ≍ log log t   (sharp constants under RH; Littlewood).
```

## Significance / context
- The RH is a **"master key"**: a proof would make hundreds of conditional results unconditional at a stroke.
- Many practical/algorithmic consequences need the **GRH** (Dirichlet L), not just the classical RH.
- Conversely, the list shows *why* a proof is so valuable (and sought after).

## Sources
- [Riemann hypothesis — Wikipedia (Consequences)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
- [The Riemann Hypothesis — E. Bombieri (Clay)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
- [Generalized Riemann hypothesis — Wikipedia (Consequences)](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)
