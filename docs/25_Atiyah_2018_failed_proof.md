---
id: doc-25
number: 25
title: "Michael Atiyah (2018): Failed Proof Attempt (Todd Function)"
category: failed-proof
status: refuted
tags: [atiyah, todd-function, fine-structure-constant, 2018, failed]
source_file: 25_Atiyah_2018_failed_proof.md
lang: en
---

# Michael Atiyah (2018): Failed Proof Attempt (Todd Function)

**Category:** Failed / disputed proof
**Author / year:** Sir Michael Atiyah, September 2018 (Heidelberg Laureate Forum)
**Type:** Publicly presented proof claim
**Status:** ❌ Not accepted by the community; regarded as erroneous/incomplete

## Summary
Sir Michael Atiyah (Fields Medal 1966, Abel Prize 2004 — one of the most important mathematicians of the 20th century) announced a "simple proof" of the Riemann Hypothesis in September 2018 and presented it in a 45-minute talk at the Heidelberg Laureate Forum. The proof relied on a supposed new description of the **fine-structure constant α** (from physics) by means of a "Todd function". The mathematical community responded with clear **skepticism**; the proof is regarded as not accepted.

## The claimed idea
- Atiyah introduced a **"Todd function" T** (named after his teacher J. A. Todd), which he claimed to have constructed as a limit of certain analytic functions.
- **Proof by contradiction:** suppose there were a zero off the critical line. Via the properties of the Todd function (which he described as "weakly analytic", polynomial on certain regions), a contradiction was supposed to arise.
- As a "corollary", a closed-form expression for the fine-structure constant α ≈ 1/137 was also supposed to fall out.

## Why the proof failed
- **Unpublished basis:** the central paper on the Todd function was not published/reviewed; the RH proof was supposed to follow "easily" from it — but this basis did not exist in verifiable form.
- **Mathematical problems:** a weakly-analytic function that is polynomial on a 2D region and behaves as required would have to be constant — the core step is untenable. The connection to the fine-structure constant (a *measured, dimensionless physical* quantity) was regarded as mathematically unfounded.
- **Context:** Atiyah was 89 at the time and had made several erroneous claims in the preceding years; colleagues expressed skepticism even before the talk.

## Significance / context
- A high-profile example that **reputation does not replace a proof** — the community checks the mathematics, not the name.
- It was respectfully but clearly rejected; Atiyah died in January 2019.
- A lesson for the AI context: even human geniuses produce false "breakthroughs"; rigorous verification is indispensable (cf. Doc. 27, 28).

## Mathematical core (claimed construction & the error)

### The claimed Todd function T
Atiyah defined (in analogy with the von Neumann hyperfinite factor theory) a function T as a limit of polynomials, which he called "weakly analytic":
```
T = lim_{n→∞} T_n,   where the T_n are iterated exponential/polynomial constructions,
T(1) = 1,   T  "polynomial on every convex region".
```
T was supposed to be additive/"compatible" with the Hirzebruch–Todd class.

### The claimed proof by contradiction
Define the function (Atiyah's notation) for a supposed zero b = 1/2 + iβ_0 off the line:
```
F(s) = T( 1 + ζ(s) )  − 1   (schematic),
```
and consider F on a circle around the critical point. Atiyah claimed: from the "weak analyticity" of T it follows that F is polynomial on a 2-dimensional region but must simultaneously vanish there ⇒ F ≡ 0 ⇒ contradiction to the assumption of the off-line zero.

### Why it is wrong (precisely)
- **Violation of the identity theorem/Liouville:** a function that is "polynomial" *and* bounded on a 2-dimensional (open) region and behaves as required would have to be **constant** (Liouville). Atiyah's T therefore cannot be simultaneously non-constant *and* have the required limit/analyticity properties — the core step collapses.
- **Fine-structure constant α:** Atiyah claimed as a "corollary" a closed formula α^{−1} = π · (an expression in T). α ≈ 137.035999 is an *empirically measured, dimensionless physical* quantity with no known reason to possess a closed mathematical form — the claim is regarded as unfounded.
- **Unpublished basis:** the theorem about T (from which the RH was supposed to follow "easily") was never available in verifiable, reviewed form.

### Assessment
Structurally a positivity/real-rootedness approach like many (Doc. 14, 20), but the decisive analytic step is untenable. Lesson: even a Fields Medalist does not replace a checkable proof.

## Sources
- [Skepticism surrounds renowned mathematician's attempted proof — Science/AAAS](https://www.science.org/content/article/skepticism-surrounds-renowned-mathematician-s-attempted-proof-160-year-old-hypothesis)
- [Riemann hypothesis, the fine structure constant, and the Todd function — John D. Cook](https://www.johndcook.com/blog/2018/09/24/riemann-hypothesis-the-fine-structure-constant-and-the-todd-function/)
- [Atiyah's RH lecture preprint (mirror, El País)](https://ep00.epimg.net/descargables/2018/09/25/b133e2bf9a3e7bb55f5fae26dcf9b8c0.pdf)
- [Riemann hypothesis, fine structure constant, Todd function — Hacker News discussion](https://news.ycombinator.com/item?id=18059880)
