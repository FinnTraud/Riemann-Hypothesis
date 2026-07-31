# The Riemann Hypothesis: Proof Approaches — Research Compendium

> Compiled via agentic web retrieval (June 2026). This document surveys the major mathematical strategies that have been pursued toward proving the Riemann Hypothesis (RH), their current status, key equivalences, recent breakthroughs, and known failed/disputed attempts. It is structured for chunked ingestion into a vector database / RAG pipeline (each `##`/`###` section is a self-contained retrievable unit).
>
> **Going deeper with the mathematics:** This survey is the short version. The `docs/` folder contains 34 individual documents — one per approach / paper / failed proof — that additionally include a **"Mathematical core (formulas, theorems, proof sketches)"** section with the actual definitions, equations, theorems, and proof computations. Entry point: `docs/00_INDEX.md`.

## 1. The Statement of the Riemann Hypothesis

The Riemann zeta function, defined for Re(s) > 1 by

```
ζ(s) = Σ_{n=1}^∞ 1/n^s
```

and analytically continued to the whole complex plane (except a simple pole at s = 1), has so-called "trivial" zeros at the negative even integers (s = -2, -4, -6, ...). The Riemann Hypothesis, posed by Bernhard Riemann in his 1859 paper "Über die Anzahl der Primzahlen unter einer gegebenen Größe," asserts:

> All non-trivial zeros of ζ(s) have real part equal to 1/2.

Equivalently, every non-trivial zero lies on the "critical line" Re(s) = 1/2 within the "critical strip" 0 < Re(s) < 1. It is one of the seven Clay Mathematics Institute Millennium Prize Problems (unsolved as of 2026), and is widely regarded as the most important unsolved problem in pure mathematics due to its deep connections to the distribution of prime numbers.

---

## 2. Equivalent Formulations and Criteria

Over one hundred statements are known to be equivalent to RH. These reformulations matter because each opens a different toolkit for attack.

### 2.1 Koch's Criterion (1901)
RH is equivalent to the prime-counting error bound:
```
π(x) = Li(x) + O(√x · ln x)
```
This is the tightest possible error term of this form; RH is exactly the statement that primes are distributed "as regularly as possible."

### 2.2 Mertens Function Criterion
Let M(x) = Σ_{n≤x} μ(n) (summatory Möbius function). RH is equivalent to: for every ε > 0, M(x)/x^(1/2+ε) → 0 as x → ∞.
- The stronger **Mertens conjecture** (|M(n)| < √n for all n) would have implied RH, but it was **disproved** by Odlyzko and te Riele in 1984 — a cautionary tale about over-strong sufficient conditions.

### 2.3 Riesz's Criterion (1916)
RH is equivalent to a growth bound on a series built from the Möbius function μ(n), related to a generating function for 1/ζ(s).

### 2.4 Nyman–Beurling Criterion (1950s) and Báez-Duarte's Strengthening
Reformulates RH as a **functional-analytic density problem**: RH holds iff the characteristic function of (0,1] lies in the L²(0,∞)-closure of the linear span of the dilations {ρ(θ/x)} of the fractional-part function ρ(t) = {1/t}, for θ ranging over (0,1).
- **Báez-Duarte (2003)** strengthened this: it suffices to use only the integer dilations θ = 1, 2, 3, ... — a major simplification.
- This recasts RH as a question about whether a certain vector is a "cyclic vector" / whether a span is dense in a Hilbert space — connecting RH to operator theory and approximation theory.
- Numerically, partial sums of this approximation converge, but extremely slowly, and no one has proven the needed density.

### 2.5 Li's Criterion (1997)
Xian-Jin Li showed RH is equivalent to the positivity of an explicit sequence of real numbers λ_n (n ≥ 1) defined via logarithmic derivatives of the Riemann ξ-function evaluated at its zeros. Numerical computation of λ_n for many n is consistent with positivity, but a general proof is missing.

### 2.6 Robin's Inequality (1984)
For all n > 5040: σ(n) < e^γ · n · log(log n), where σ(n) is the sum-of-divisors function and γ is the Euler–Mascheroni constant. RH is equivalent to this inequality holding for **all** n > 5040 (it is known to hold for many classes of n, and known to fail only if RH is false).

### 2.7 Lindelöf Hypothesis Connections
The Lindelöf Hypothesis (a statement about the growth rate of ζ(1/2 + it)) is implied by RH but is formally weaker; recent work (2019–2020) shows a "Lindelöf hypothesis for primes" version is actually *equivalent* to RH, tightening the relationship between growth-rate statements and the zero location statement.

### 2.8 de Branges' Hilbert-Space Criterion
De Branges' theory of Hilbert spaces of entire functions provides another equivalent positivity-type condition (a "Riemann hypothesis for Hilbert spaces of entire functions") which, if it could be verified for the specific space attached to ζ, would imply RH. See Section 4.

---

## 3. Classical Analytic Approaches (Zero-Free Regions)

Rather than proving RH outright, a century of work has aimed at progressively **shrinking the region of the critical strip known to be free of zeros**, narrowing the strip toward the critical line.

| Year | Author(s) | Zero-free region (σ = Re(s), bound near σ = 1) |
|---|---|---|
| 1896 | Hadamard, de la Vallée Poussin | ζ(1+it) ≠ 0; first proof of Prime Number Theorem |
| 1899 | de la Vallée Poussin | 1 − σ ≤ c / log t |
| 1922 | Littlewood | 1 − σ ≤ c·log log t / log t |
| 1938 | Chudakov | 1 − σ ≤ c / (log t)^(3/4+ε) |
| 1950s | Vinogradov, Korobov | 1 − σ ≤ c / (log t)^(2/3) (log log t)^(1/3) — long-standing best asymptotic order |
| 2024 (explicit) | various | ζ(σ+it) ≠ 0 for t ≥ 3, σ ≥ 1 − 1/(4.896 log t) (explicit constant improvements) |

The **Vinogradov–Korobov bound** stood as the best known *asymptotic* exponent for ~70 years; subsequent work mostly improved explicit constants rather than the exponent, until very recent decoupling-based work (Section 6) began to push the exponent itself.

These results give effective, explicit (if weak) versions of the Prime Number Theorem with error terms, but a zero-free region, however small, is fundamentally weaker than RH itself — it bounds zeros away from the line σ=1, not pins them to σ=1/2.

---

## 4. Spectral / Operator-Theoretic Approaches (Hilbert–Pólya Program)

### 4.1 The Hilbert–Pólya Conjecture (c. 1912)
Conjectured independently by David Hilbert and George Pólya: the imaginary parts of the non-trivial zeros of ζ(s) correspond to the eigenvalues of some self-adjoint (Hermitian) operator. Since self-adjoint operators have real eigenvalues, if such an operator exists and is correctly tied to ζ, RH follows immediately. No such operator has been rigorously constructed for the actual zeta zeros — this remains the central open strategic question in the field.

### 4.2 Random Matrix Theory (RMT) Connection
- In 1972, **Hugh Montgomery** computed the pair-correlation statistics of zeta zeros and, in a conversation with **Freeman Dyson**, discovered they matched the pair-correlation of eigenvalues of random Hermitian matrices from the **Gaussian Unitary Ensemble (GUE)**.
- This **Montgomery–Odlyzko law** has been confirmed numerically to high precision (Odlyzko's massive zero computations) and extended to higher-order correlations and statistics (e.g., Katz–Sarnak philosophy across families of L-functions).
- This is strong heuristic/statistical evidence *consistent* with a Hilbert–Pólya operator existing and being "chaotic" in the GUE universality class, but it is not itself a proof — it establishes statistical mimicry, not an actual operator.

### 4.3 Quantum Chaos / Berry–Keating Program
- **Berry and Keating** (1999) proposed that the zeros are eigenvalues of the quantization of the classical Hamiltonian **H = xp** (position times momentum), motivated by semiclassical/quantum-chaos heuristics connecting periodic orbits to primes (a "physicist's Hilbert–Pólya operator").
- Known issue: naive quantization of H=xp gives only the *mean* (smoothed) density of zeros, not their exact locations; the spectrum is continuous, not discrete, without further regularization.
- Variants and refinements: Berry–Keating regularizations, Connes' regularization (different boundary conditions giving an "absorption spectrum" rather than discrete eigenvalues — missing spectral lines correspond to zeros), Sierra & Townsend's H = x(p + 1/p) and related models (2011) producing discrete spectra matching the smooth zero-counting function, polymer quantization approaches, and pseudo-Hermitian/PT-symmetric Hamiltonian models.
- As of 2026, no construction yields the *exact* nontrivial zeros as eigenvalues of a rigorously defined self-adjoint operator — only smoothed/statistical agreement.

### 4.4 Alain Connes' Noncommutative Geometry / Trace Formula Approach
- Connes (1996–1999, *Selecta Mathematica*) constructed a **trace formula on the noncommutative adèle class space** 𝔸/ℚ* that reproduces the Weil explicit formula relating primes and zeta zeros.
- In Connes' framework, the critical zeros appear as an **absorption spectrum** (missing spectral lines) of a natural operator, while *hypothetical* zeros off the critical line would appear as resonances breaking the formula's structure.
- **Key reduction:** Connes shows RH for ζ (and the generalized RH for the L-functions of Hecke characters) is implied by the validity of a specific trace formula identity (a Lefschetz-trace-formula-style statement) on this noncommutative space — turning RH into a precise, if still unproven, geometric/spectral statement.
- This program connects to the **Selberg trace formula** in spirit (which relates eigenvalues of the Laplacian on a hyperbolic surface to lengths of closed geodesics, analogous to zeros vs. primes) but works in an adelic, noncommutative setting rather than classical hyperbolic geometry.
- Connes published an accessible summary, "An Essay on the Riemann Hypothesis" (2015), updating the state of this program — still open as of 2026.

### 4.5 De Branges' Hilbert Spaces of Entire Functions
- Louis de Branges built an extensive theory of Hilbert spaces of entire functions (originating from Stieltjes' earlier attempts on RH) in the late 1950s–60s, generalizing Fourier/Plancherel theory.
- In 1986, de Branges proposed that proving a specific positivity ("Riemann hypothesis for Hilbert spaces of entire functions" — a condition on certain weighted Hardy spaces having no zeros in associated half-planes) for the Hilbert space naturally associated to the Euler zeta function would imply the (generalized) RH.
- De Branges released **several claimed proofs** of RH over the following decades (e.g., drafts in 2004, 2009, and as late as 2017 — "A Proof of the Riemann Hypothesis," Purdue preprint), but each was found by the mathematical community to contain **gaps or errors** (often issues with the positivity condition not actually being established, or with the specific space constructed not satisfying required axioms). None has been accepted as valid. De Branges' case is the most cited example of a serious, technically sophisticated, repeatedly-revised — but ultimately unsuccessful — proof attempt. (Documented in Karl Sabbagh's *London Review of Books* piece "The Strange Case of Louis de Branges.")

---

## 5. Functional / Variational and Other Analytic Programs

- **Conformal mapping methods** inspired by Riemann's own (geometric) original approach: extremizing a quadratic form yields close approximations to zero locations — explored in recent survey work as a "fresh perspective," but not a proof.
- **Laplace transform reformulations**: convert some analytic conditions on ζ into algebraic/integral-transform language; claimed to give more "intuitive" geometric pictures but not yet a complete proof.
- **Positivity / explicit formula approaches**: Weil's explicit formula relates a sum over zeros to a sum over primes plus archimedean terms; proving a suitable positivity condition on this formula (the "Weil positivity criterion") would imply RH (and is essentially the analytic heart of the Connes program too).

---

## 6. Recent Breakthroughs (2020s) — Progress Short of a Full Proof

### 6.1 Guth–Maynard Zero-Density Breakthrough (2024)
Larry Guth and James Maynard achieved the **first substantial improvement in over 80 years** to a classical zero-density estimate of Ingham (1940). Ingham's bound on N(σ,T) — the number of zeros with real part ≥ σ ∈ [3/4,1] and imaginary part ≤ T — had N(3/4,T) ≪ T^(3/5+o(1)); only the o(1) term had improved since 1940. Guth–Maynard improved the *exponent itself*, showing (for σ near 3/4) bounds like N(σ,T) ≪ T^(13/25+o(1)) at σ=3/4 region, via new **Dirichlet polynomial / decoupling estimates** imported from harmonic analysis (related to techniques behind the resolution of the Vinogradov mean value conjecture). Terence Tao publicly described this as "a remarkable breakthrough."
- **Significance:** Zero-density estimates bound how many zeros could exist *off* the critical line in a given height range; they feed directly into prime-counting error terms (e.g., improving results on primes in short intervals) even without full RH. This is widely viewed as the most important *unconditional* progress on the RH-adjacent landscape in decades.
- This does **not** prove RH and does not claim to; it tightens density bounds in part of the strip.

### 6.2 Explicit Zero-Free Regions (2023–2026)
Continued explicit (constant-improving) work has pushed known zero-free regions, e.g. ζ(σ+it) ≠ 0 for t ≥ 3 and σ ≥ 1 − 1/(4.896 log t), and further refinements citing Heath-Brown-style methods (2026) and explicit bounds in the critical strip — incremental but practically important for effective prime-counting bounds (e.g., explicit error terms used in computational number theory and cryptographically relevant prime-density estimates).

### 6.3 Machine-Learning / Data-Driven "Falsifiability" Studies (2025)
Several 2025 papers (e.g., in *Mathematics* (MDPI) and *JAMCS*) apply machine learning classification/explainability models to numerically computed zeta zeros, looking for discriminative statistical signals that distinguish on-line vs. off-line behavior, and testing whether ML models trained on partial data ever find counterexample-like patterns. These are explicitly framed as **empirical, falsifiability-oriented, non-proof** explorations — useful for generating heuristic confidence and possibly flagging numerical anomalies, not as a path to a rigorous proof.

### 6.4 Disputed / Unverified Claimed Proofs (ongoing)
Numerous arXiv preprints periodically claim full proofs of RH (e.g., "Proof of the Riemann Hypothesis," 2022; "Towards a proof of the Riemann Hypothesis," 2022, explicitly titled as a collaborator-seeking draft; assorted 2024–2026 claims). As of June 2026, **none have survived peer review or community scrutiny** to be accepted as valid; the consistent pattern is subtle gaps in positivity arguments, unjustified interchange of limits/integrals, or circular reasoning smuggling in the result. The Riemann Hypothesis remains formally **open**.

---

## 7. Summary Table of Major Programs

| Approach | Core Idea | Status (2026) |
|---|---|---|
| Zero-free regions (classical analytic) | Shrink region provably free of zeros near σ=1 | Active; recent explicit + Guth–Maynard density improvements |
| Hilbert–Pólya / spectral | Find self-adjoint operator whose eigenvalues = zero ordinates | Operator not found; only heuristic/statistical candidates |
| Random Matrix Theory | Zeros statistically match GUE eigenvalue correlations | Strong numerical/statistical match; not a proof mechanism |
| Berry–Keating quantum chaos (H=xp) | Quantize classical chaotic Hamiltonian tied to primes | Reproduces smoothed zero density only |
| Connes noncommutative trace formula | Reduce RH to validity of an adelic trace formula | Precise reduction achieved; trace formula validity still open |
| de Branges Hilbert spaces of entire functions | Positivity condition on associated function space implies RH | Multiple claimed proofs (2004–2017), all found flawed |
| Nyman–Beurling / Báez-Duarte | RH ⟺ density of a function span in L²(0,1) | Equivalent reformulation; density unproven |
| Li's criterion | RH ⟺ positivity of explicit λ_n sequence | Numerically consistent; general proof missing |
| Robin's inequality | RH ⟺ arithmetic inequality on σ(n) for n>5040 | Equivalent reformulation; unproven in general |
| ML / data-driven studies | Statistical/empirical evidence via classifiers on zero data | Explicitly non-proof, exploratory |

---

## 8. Key Sources

- [The Riemann Hypothesis: Past, Present and a Letter Through Time (arXiv 2602.04022)](https://arxiv.org/abs/2602.04022)
- [Criteria equivalent to the Riemann Hypothesis (arXiv 0808.0640)](https://arxiv.org/pdf/0808.0640)
- [Equivalent criteria for the Riemann hypothesis for a general class of L-functions (arXiv 2409.17708)](https://arxiv.org/pdf/2409.17708)
- [Robin's Inequality & the Riemann Hypothesis (Emergent Mind)](https://www.emergentmind.com/topics/robin-s-inequality)
- [The Riemann Hypothesis — AIM (American Institute of Mathematics)](https://www.aimath.org/WWN/rh/rh.pdf)
- [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function — Connes (arXiv math/9811068)](https://arxiv.org/abs/math/9811068)
- [An essay on the Riemann Hypothesis — Connes (arXiv 1509.05576)](https://arxiv.org/pdf/1509.05576)
- [A spectral interpretation for the zeros of the Riemann zeta function (arXiv math/0412277)](https://arxiv.org/pdf/math/0412277)
- [What is new with Connes' approach to the Riemann hypothesis? — Khalkhali](https://www.math.uwo.ca/faculty/khalkhali/files/TehProg.pdf)
- [The Riemann hypothesis for Hilbert spaces of entire functions — de Branges](https://www.math.purdue.edu/~branges/riemann-hilbert.pdf)
- [A Proof of the Riemann Hypothesis — de Branges (2017 draft)](https://www.math.purdue.edu/~branges/proof-riemann-2017-04.pdf)
- [The Strange Case of Louis de Branges — Karl Sabbagh, LRB](https://www.lrb.co.uk/the-paper/v26/n14/karl-sabbagh/the-strange-case-of-louis-de-branges)
- [General covariant xp models and the Riemann zeros (arXiv 1110.3203)](https://arxiv.org/pdf/1110.3203)
- [The Riemann zeros as spectrum and the Riemann hypothesis (arXiv 1601.01797)](https://arxiv.org/pdf/1601.01797)
- [A general strong Nyman-Beurling Criterion for the Riemann Hypothesis (arXiv math/0505453)](https://arxiv.org/pdf/math/0505453)
- [On probabilistic generalizations of the Nyman-Beurling criterion (arXiv 1805.06733)](https://arxiv.org/pdf/1805.06733)
- [Zero-free regions for the Riemann zeta function (arXiv 1910.08205)](https://arxiv.org/pdf/1910.08205)
- [Zero-free regions inspired by work of Heath-Brown (arXiv 2603.21490)](https://arxiv.org/html/2603.21490)
- [Explicit bounds on ζ(s) in the critical strip and a zero-free region (arXiv 2301.03165)](https://arxiv.org/pdf/2301.03165)
- [Terence Tao on the Guth–Maynard breakthrough (Mathstodon)](https://mathstodon.xyz/@tao/112557248794707738)
- [The Riemann Hypothesis, the Biggest Problem in Mathematics, Is a Step Closer to Being Solved — Scientific American](https://www.scientificamerican.com/article/the-riemann-hypothesis-the-biggest-problem-in-mathematics-is-a-step-closer/)
- [Empirical Investigation of the Riemann Hypothesis Using Machine Learning (MDPI Mathematics 2025)](https://www.mdpi.com/2227-7390/13/17/2824)
- [The Riemann Hypothesis: New Approaches Using Analytic Methods (Math Research Journal, 2025)](https://www.mathresearchjournal.com/uploads/archives/20250613104255_5.pdf)

---

## 9. AI and the Riemann Hypothesis: possibilities and limits of machine learning

> Addition based on the outline of a student research paper ("The Riemann Hypothesis and AI: possibilities and limits of machine learning in number theory", survey work). This section gathers the sources referenced there and organizes them thematically for the RAG knowledge base.

### 9.1 Motivation and starting thesis
Guiding question: *"Will AI Prove the Riemann Hypothesis Without Understanding It?"* — a question raised by Terence Tao (Fields Medalist) that marks the tension between statistical, pattern-recognizing AI methods and a formal, understood proof.

- [Will AI Prove the Riemann Hypothesis Without Understanding It? — Terence Tao (YouTube)](https://youtu.be/PU1LMVGcyXA?si=RcL7JrKpHE5izoso)
- [Terence Tao: "Proofs are no longer the most important thing in mathematics" — Der Standard](https://www.derstandard.de/story/3000000320851/terence-tao-beweise-sind-nicht-mehr-das-wichtigste-in-der-mathematik)
- [Encrypted mathematics: proofs challenge AI — Spektrum](https://www.spektrum.de/news/verschluesselte-mathematik-beweise-fordern-ki-heraus/2308813)

### 9.2 Foundations: what is the Riemann Hypothesis — introductory source
- [The Riemann Hypothesis — Christmas Lecture 2016 (YouTube)](https://youtu.be/sZhl6PyTflw?si=QBvUI15ADHSpIjh9)
  - Covers: what the RH states, its relevance, why it is unsolved, the consequences of a proof, its status as a Millennium Problem.

### 9.3 What is AI? Clarification of terms and suitability for mathematical problems
Relevant aspects for context: sorting out terminology (LLM vs. classical ML classifiers vs. symbolic AI), opportunities and risks (in particular hallucination), the question of which AI architecture is suited to formal mathematical problems, and what advantages AI could offer over human mathematicians (compute power, pattern recognition in large number spaces, exhaustion of search spaces).

- [No room for hallucinations: AI startup wants to guarantee correct math proofs — The Decoder](https://the-decoder.de/kein-platz-fuer-halluzinationen-ki-start-up-will-korrekte-mathebeweise-garantieren/)

### 9.4 Where has AI already proved/supported mathematical theorems? (case studies)

**Project First Proof (Harvard)** — an initiative for AI-assisted verification/generation of formal proofs.

**Erdős unit-distance problem (solved after ~60 years, posed in 1946):**
- [A creative solution: AI solves a 60-year-old Erdős problem — Heise](https://www.heise.de/news/Kreativer-Loesungsweg-KI-loest-60-Jahre-altes-Erd-s-Problem-11275796.html)
- [The most significant mathematical proof by language AI so far astonishes experts — Der Standard](https://www.derstandard.de/story/3000000321753/bisher-bedeutendster-mathematischer-beweis-mittels-sprach-ki-verbluefft-fachleute)

**Navier-Stokes equations (Millennium Problem) — counterexample of a *failed* AI breakthrough claim:**
- [AI just solved a 100-year-old million-dollar science puzzle (announcement) — YouTube](https://youtu.be/XohlBa8NkKw?si=ZExr5UfsNRt4QGQr)
- [OpenAI researchers announce a false math breakthrough and are met with ridicule — MSN/Der Standard](https://www.msn.com/de-ch/nachrichten/other/open-ai-forscher-verk%C3%BCnden-falschen-mathedurchbruch-und-ernten-spott/ar-AA1OSsBR)
- [Nature article on the incident](https://www.nature.com/articles/d41586-026-00969-z)
  - **Important for the critical appraisal:** this is a central counterexample to the success story — it shows that AI-generated "breakthroughs" on Millennium Problems can lead to publicly false claims without rigorous peer review. Directly relevant to the critical assessment of AI approaches to the Riemann Hypothesis.

**Limits and error sources of AI in mathematics generally:**
- [AI fails at math problems for top researchers — Forschung und Wissen](https://www.forschung-und-wissen.de/nachrichten/technik/ki-scheitert-an-matheaufgaben-fuer-spitzenforscher-133711288)
- [The simple task that every AI fails — YouTube](https://www.youtube.com/watch?v=x_ZhqjbgdAQ&t=58)

**Where AI has corrected mathematicians (counterexample: AI as a useful corrective):**
- [AI proves: mathematicians were wrong — Heise](https://www.heise.de/news/KI-beweist-Mathematiker-lagen-falsch-11302698.html)

**A fundamental limit — the Goldbach conjecture as an analogue to the Riemann Hypothesis:**
- [AI Cannot Prove Goldbach's Conjecture. Not Because It Isn't Smart Enough. Because It's the Wrong Kind of Smart — Towards AI](https://pub.towardsai.net/ai-cannot-prove-goldbachs-conjecture-115bca355678)
  - Core argument: for open number-theoretic conjectures like Goldbach (and analogously the Riemann Hypothesis), what is lacking is not compute power or pattern-recognition ability, but the kind of structural/conceptual understanding that a valid formal proof requires — a core argument for the "critical appraisal" in the context of AI and RH.

### 9.5 Current state: guidelines and self-regulation of the mathematics community
- [Guidelines: mathematicians want to curb the use of AI in their field — Spektrum](https://www.spektrum.de/news/leitlinien-mathematiker-wollen-einsatz-von-ki-in-ihrem-fach-eindaemmen/2327655)
  - Relevant for the "state of the art" / "outlook" section: shows that the professional community is already discussing/establishing rules for the responsible use of AI in mathematical research — important for contextualizing an AI proof of the RH.

### 9.6 Proposed outline of the student research paper (reference)
1. Introduction
2. What is the Riemann Hypothesis (RH)? — statement, relevance, why unsolved, consequences of a proof, Millennium Problem
3. What is AI? — sorting out terminology (LLM etc.), opportunities/risks (hallucination), suitable AI architectures for mathematical problems, advantages over human mathematicians
4. Connecting mathematics / RH – AI:
   - Where has AI already proved mathematical theorems? (Erdős unit-distance problem, Project First Proof)
   - Where did it go wrong? (Navier-Stokes false claim)
   - Where has AI corrected mathematicians?
   - Where are the limits? (Goldbach conjecture as an analogy)
5. The Riemann Hypothesis and AI: state of the art
6. Critical appraisal
7. Outlook
8. Sources
9. Glossary

---

*Document compiled for RAG ingestion. Each numbered section is intended to function as an independently retrievable chunk describing one proof strategy, criterion, or development in Riemann Hypothesis research as of June 2026.*
