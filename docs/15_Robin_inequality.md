---
id: doc-15
number: 15
title: "Robin's Inequality & Lagarias' Elementary Criterion (arithmetic criteria)"
category: criterion
status: open
tags: [robin, lagarias, divisor-function, elementary]
source_file: 15_Robin_inequality.md
lang: en
---

# Robin's Inequality & Lagarias' Elementary Criterion (arithmetic criteria)

**Category:** Equivalent criterion (arithmetic/elementary)
**Authors / years:** Guy Robin (1984), Jeffrey Lagarias (2002); basis Ramanujan / Gronwall
**Type:** Elementary inequalities equivalent to the RH
**Status:** Equivalences proven; inequalities unproven in general

## Summary
What is remarkable about these criteria is that they express the RH **entirely elementarily** — without complex analysis — as an inequality on the sum-of-divisors function σ(n). σ(n) = Σ_{d|n} d is the sum of all divisors of n.

## Robin's inequality (1984)
- **Theorem (Robin):** the RH is equivalent to the inequality

```
σ(n) < e^γ · n · log(log n)   for all n > 5040
```

  where γ ≈ 0.5772 is the Euler–Mascheroni constant.
- Robin showed: if the inequality holds for all n > 5040, then the RH follows; if it does *not* hold, then the RH is false (and there would be a concrete counterexample n).
- The inequality is proven for many classes of n (e.g. odd n, many "colossally abundant" numbers); only a potential failure would refute the RH.

## Lagarias' elementary criterion (2002)
- **Theorem (Lagarias):** with the harmonic number H_n = Σ_{k=1}^n 1/k, the RH is equivalent to

```
σ(n) ≤ H_n + e^{H_n} · log(H_n)   for all n ≥ 1,
```

  with equality only for n = 1.
- Regarded as one of the "most elementary" known statements equivalent to the RH — statable with school mathematics, but just as hard to prove.

## Background (Gronwall / Ramanujan)
- Gronwall's theorem: limsup σ(n)/(n log log n) = e^γ. Robin's inequality sharpens this to a bound valid for *all* large n — and exactly this sharpening is the RH.
- Ramanujan had related results on "highly composite" / "superior highly composite" numbers (partly published only posthumously) that anticipated Robin's work.

## Significance / context
- An impressive demonstration of how deeply the RH reaches into elementary arithmetic (sums of divisors).
- Didactically valuable (no apparatus of complex analysis needed).
- **Open:** proving the seemingly "simple" inequality in general is equivalent to the full RH — hence just as hard.

## Mathematical core (formulas, theorems, proof sketches)

### Robin's theorem (1984)
With σ(n) = Σ_{d|n} d and γ ≈ 0.5772156649 (Euler–Mascheroni):
```
RH  ⟺  σ(n) < e^γ · n · log log n   for all n > 5040.
```
**Proof direction "RH ⇒ inequality" (sketch):** Robin uses explicit estimates of the Chebyshev function θ(x)=Σ_{p≤x} log p, which under RH have the error term θ(x) = x + O(√x log²x) (Doc. 02). For "colossally abundant" numbers (which maximize σ(n)/(n log log n)) this error term translates into the sharp constant e^γ. **Reverse direction:** if RH were false (a zero with β>1/2), one constructs a sequence of n that violate the inequality.

### Gronwall's theorem (1913, background)
```
limsup_{n→∞} σ(n)/(n log log n) = e^γ.
```
Robin sharpens this from "limsup = e^γ" to "strictly < e^γ for all n > 5040" — and exactly this sharpening is equivalent to the RH. The largest known n with σ(n) ≥ e^γ n log log n is n = 5040 itself (along with the smaller exceptions 3,4,5,6,8,9,10,12,16,18,20,24,30,36,48,60,72,84,120,180,240,360,720,840,2520,5040).

### Lagarias' variant (2002)
With the harmonic number H_n = Σ_{k=1}^n 1/k:
```
RH  ⟺  σ(n) ≤ H_n + exp(H_n) · log(H_n)   for all n ≥ 1,
```
with equality only at n = 1. **Derivation:** since H_n = log n + γ + O(1/n) and exp(H_n) = e^γ n (1+o(1)), we have exp(H_n) log H_n = e^γ n (log log n + log(1 + γ/log n + …)). Lagarias shows that the Robin bound can be brought equivalently into this equality-sharp form valid for *all* n ≥ 1.

### Related arithmetic criteria
- **Nicolas (1983):** RH ⟺ ∏_{p≤x}(p/(p−1)) > e^γ log θ(x) for all primorial-like arguments (via the function n/φ(n), φ = Euler totient).

## Sources
- [Robin's Inequality & the Riemann Hypothesis — Emergent Mind](https://www.emergentmind.com/topics/robin-s-inequality)
- [Criteria equivalent to the Riemann Hypothesis (arXiv 0808.0640)](https://arxiv.org/pdf/0808.0640)
- [Riemann hypothesis — Wikipedia (section: Consequences and equivalents)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
