---
id: doc-28
number: 28
title: "AI / Machine Learning and the Riemann Hypothesis"
category: ai-context
status: meta
tags: [AI, machine-learning, LLM, formal-verification, hallucination]
source_file: 28_AI_and_RH.md
lang: en
---

# AI / Machine Learning and the Riemann Hypothesis

**Category:** AI context / methodological critique
**Period:** focus 2024–2026
**Type:** Empirical, data-driven (non-proof) approaches + critical assessment
**Status:** Explicitly NO formal proofs; exploratory/heuristic

## Summary
Modern AI and machine-learning methods (classifiers, neural networks, LLM-assisted pattern recognition, automated/formal proof systems) are increasingly applied to the numerical study of the ζ-zero distribution. They provide **empirical, falsifiability-oriented** evidence — but **no formal proof**. Guiding question (after Terence Tao): *"Will AI Prove the Riemann Hypothesis Without Understanding It?"*

## Types of AI approaches to the RH
1. **Data-driven classification / explainability (2025):** ML models are trained on computed zeros; one looks for discriminative statistical signals that distinguish on-line from hypothetical off-line behavior. Finding: stable explanatory signals exclusively along the critical line (consistent with RH). Explicitly framed as a *non-proof*.
2. **Generative / contradiction tests:** models check whether counterexample-like patterns can be generated (falsification attempt).
3. **Formal/verified proof systems:** projects for machine verification (Lean, Coq) and AI-assisted proof search — goal: correct, mechanically checked proofs *without* hallucination.

## Where AI has already succeeded in mathematics (for context)
- **Erdős unit-distance problem (1946):** significantly advanced with AI/LLM assistance — celebrated as an important proof via language AI.
- **AI corrected mathematicians:** cases where AI showed that established assumptions were wrong.
- These successes concern *specific, well-delineated* problems — **not** open Millennium Problems like the RH.

## Where it went wrong (cautionary cases)
- **Navier-Stokes false claim:** OpenAI researchers announced a "math breakthrough" (a Millennium Problem) that turned out to be **false** — publicly criticized. Shows: AI "breakthroughs" on Millennium Problems without rigorous peer review lead to false claims.
- **AI fails at top-researcher problems:** studies document systematic failure of current AI on hard mathematical problems.
- **Goldbach analogy:** the argument ("AI Cannot Prove Goldbach's Conjecture ... the Wrong Kind of Smart") — for open number-theoretic conjectures, AI lacks not compute power but the *kind of structural understanding* that a valid proof requires. This transfers directly to the RH.

## Critical appraisal (key points)
- **Numerics ≠ proof:** finite/statistical evidence never proves the RH (infinitely many zeros). The **refuted Mertens conjecture** (Doc. 16) shows that seemingly robust numerical patterns can fail at ~10^30.
- **Hallucination risk with LLMs:** generative models can produce plausible-sounding but false "proofs" — hence the trend toward formally verified systems.
- **Human–machine collaboration works** where machines exhaust search spaces and humans/verifiers guarantee correctness (cf. Polymath15, Doc. 23).
- **Self-regulation of the community:** guidelines for the responsible use of AI in mathematics are already emerging.

## Significance / context
- AI is (as of 2026) a **tool for exploration, pattern recognition, and verification** — not an independent producer of accepted RH proofs.
- Sensible roles: generating conjectures, locating promising structures, formally verifying human proofs, large-scale numerical computation.
- Open question (Tao): whether AI could ever deliver an RH proof "without understanding" — and whether such a proof would be accepted by the community as insight.

## Mathematical/methodological core (what AI works on, formally)

### What the ML models concretely use as data
- **Normalized zero spacings** δ_n = (γ_{n+1} − γ_n)·(1/2π)log(γ_n/2π) (cf. Doc. 06): input for classifiers that distinguish GUE vs. non-GUE statistics.
- **Values of Z(t)** / ζ(1/2+it) (Doc. 03/24) as a time series: pattern recognition for sign changes.
- **Li coefficients λ_n** / Turán expressions (Doc. 14/29): positivity checks as features.

### Formal learning problem (classification example)
Train f_θ: (feature vector from {γ_n}) → {"on-line", "off-line"}. Finding (MDPI 2025): discriminative signals appear stably **only** along Re=1/2; contradiction tests find no off-line pattern. **But:** this is induction over finite samples — not a universally-quantified proof ∀ρ.

### Why AI hits a wall here in principle
- **Finiteness:** every ML model sees finitely many zeros; the RH is a statement about ∞ many. The refuted Mertens conjecture (Doc. 16) shows formally: M(x)/√x < 1 holds up to ~10^{14} but is false (Odlyzko–te Riele: limsup > 1.06). A classifier would have learned "Mertens true".
- **Hallucination with LLMs:** a generative "proof" is a sample from p_θ(text); correctness is *not* part of the objective. Hence the trend toward **formal verification** (Lean/mathlib, Coq): there every step is checked against axioms, p(proof correct) = 1 by construction.

### Sensible, formally sound AI roles
1. **Conjecture generation** (e.g. patterns in λ_n, moment constants g_k, Doc. 07/14).
2. **Proof search + formal verification** (human/machine hybrid, like Polymath15, Doc. 23, where computers rigorously checked Lehmer-pair bounds).
3. **Large-scale numerical computation** (Doc. 24) — but verification via interval arithmetic, not via a neural network.

### Success vs. failure examples (formally categorized)
- **Erdős unit-distance problem:** a combinatorial-finite problem ⇒ AI-assisted construction is verifiable. The RH is *not* of this type.
- **Navier-Stokes false claim:** shows that an AI "proof" of a Millennium Problem fails without peer review / formal checking — exactly the risk with an AI "RH proof".

## Sources
- [Will AI Prove the Riemann Hypothesis Without Understanding It? — Terence Tao (YouTube)](https://youtu.be/PU1LMVGcyXA?si=RcL7JrKpHE5izoso)
- [Empirical Investigation of the Riemann Hypothesis Using Machine Learning (MDPI Mathematics 2025)](https://www.mdpi.com/2227-7390/13/17/2824)
- [No room for hallucinations: AI startup wants to guarantee correct math proofs — The Decoder](https://the-decoder.de/kein-platz-fuer-halluzinationen-ki-start-up-will-korrekte-mathebeweise-garantieren/)
- [A creative solution: AI solves a 60-year-old Erdős problem — Heise](https://www.heise.de/news/Kreativer-Loesungsweg-KI-loest-60-Jahre-altes-Erd-s-Problem-11275796.html)
- [OpenAI researchers announce a false math breakthrough — MSN/Der Standard](https://www.msn.com/de-ch/nachrichten/other/open-ai-forscher-verk%C3%BCnden-falschen-mathedurchbruch-und-ernten-spott/ar-AA1OSsBR)
- [AI Cannot Prove Goldbach's Conjecture — Towards AI](https://pub.towardsai.net/ai-cannot-prove-goldbachs-conjecture-115bca355678)
- [Guidelines: mathematicians want to curb the use of AI — Spektrum](https://www.spektrum.de/news/leitlinien-mathematiker-wollen-einsatz-von-ki-in-ihrem-fach-eindaemmen/2327655)
- [Terence Tao: "Proofs are no longer the most important thing in mathematics" — Der Standard](https://www.derstandard.de/story/3000000320851/terence-tao-beweise-sind-nicht-mehr-das-wichtigste-in-der-mathematik)
