---
id: doc-27
number: 27
title: "Other Disputed, Retracted & Erroneous Proof Claims"
category: failed-proof
status: refuted
tags: [disputed-proofs, retracted, error-patterns, crackpot]
source_file: 27_other_disputed_claimed_proofs.md
lang: en
---

# Other Disputed, Retracted & Erroneous Proof Claims

**Category:** Failed / disputed proofs (collective document)
**Period:** ongoing (focus 2000s–2020s)
**Type:** Overview of non-accepted claims
**Status:** ❌ None of these claims is recognized by the community; the RH remains open

## Summary
The Riemann Hypothesis attracts an unusually large number of proof (and disproof) claims — from serious research programs to obviously flawed one-off papers. **As of June 2026 none is accepted as valid; the RH is formally open.** This document collects patterns and concrete examples; the prominent individual cases de Branges (Doc. 20), Atiyah (Doc. 25), and Nash (Doc. 26) have their own documents.

## Typical sources of error (recurring patterns)
- **Unjustified interchange step:** illegitimately interchanging limit/integral/sum.
- **Unestablished positivity:** a positivity condition (Li/Weil type, Doc. 14) is claimed but not proven.
- **Circular reasoning:** the statement to be proven is (covertly) assumed.
- **False generalization:** an argument valid for special cases is illegitimately extended to the general case.
- **Numerics instead of proof:** finite numerical evidence is presented as a proof (cf. the Mertens warning, Doc. 16).

## Concrete examples (2010s–2020s)
- **Frank Vega, "New Criterion for the Riemann Hypothesis" (Cambridge Open Engage):** **retracted** in 2023 after the author himself acknowledged an error in the proof (p. 7).
- **L. Agélas, claimed GRH proof:** **Richard P. Brent** showed in a 2021 note that the paper contains an error.
- **Various arXiv claims** (pro and con), including "The Riemann Hypothesis is false" (arXiv 2006.12546), "The Disproof of the Riemann Hypothesis" (arXiv 2102.08313), "Hypothesis of Riemann is rejected by definition" (arXiv 2110.03253) — none accepted by the community.
- **Jin Gyu Lee, claimed proof:** analyzed as erroneous in a separate note (arXiv 1305.4614).
- **"Pseudodifferential arithmetic and a failed attempt on the Riemann hypothesis" (arXiv 2202.11652):** notable because the author himself documents the **failed** attempt — instructive about exactly where such approaches break.

## AI/physics-adjacent claims
- Various preprints derive the RH from physical "coupling-constant spectra" or ML patterns (e.g. arXiv 2103.02223, 0803.1818). These are heuristic/speculative and provide no formal proof (cf. Doc. 28 on the critical assessment of AI approaches).

## Significance / context
- The sheer volume of failed attempts underscores that the RH is **resistant to "simple" ideas**; every proposed shortcut has been checked and rejected.
- **Peer review works:** claims are systematically examined; errors are found (often within days/weeks).
- Practical note: the Clay Mathematics Institute recognizes a Millennium Prize proof only after publication in a reputable journal and several years of standing in the community — not on a mere preprint announcement.

## Mathematical core (typical error mechanisms, shown on formulas)

### Error type 1 — illegitimate interchange of limit/sum/integral
Often the explicit formula (Doc. 02) is manipulated, e.g.
```
"ψ(x) − x = −Σ_ρ x^ρ/ρ"   →   (wrong) Σ_ρ x^ρ/ρ = O(x^{1/2}) "because each term ≤ x^{1/2}/|ρ|".
```
The error: the sum over ρ is only **conditionally** convergent, not absolutely; term-by-term estimation is invalid. Without control of Σ 1/|ρ| (divergent) the argument collapses.

### Error type 2 — positivity assumed instead of proven
In Li/Weil-type proofs (Doc. 14) one "shows" λ_n = Σ_ρ[1−(1−1/ρ)^n] ≥ 0 by already using the very location Re(ρ)=1/2 to be proven in an intermediate step:
```
"(1 − 1/ρ) has modulus ≤ 1, so λ_n ≥ 0" — holds only if Re(ρ) ≤ 1/2, hence circular.
```

### Error type 3 — false generalization
An argument valid for Re(s) > 1 (Euler-product region, ζ ≠ 0) is illegitimately continued into the critical strip 0 < Re(s) < 1, where the Euler product diverges.

### Concrete documented cases
- **Vega, "New Criterion for the RH"** (Cambridge Open Engage, 2023): retracted by the author himself — an erroneous step on p. 7 (a claimed inequality does not hold).
- **Agélas (GRH proof):** Brent (arXiv 2103.09418) locates the error in an illegitimate estimate of an L-function sum.
- **"The Riemann Hypothesis is false" (arXiv 2006.12546), "Disproof…" (2102.08313):** numerical/definitional misunderstandings; no valid construction of an off-line zero.
- **Jin Gyu Lee:** analyzed as erroneous in arXiv 1305.4614 (error in a contour shift).
- **arXiv 2202.11652 (self-documented failed attempt):** explicitly shows at which point a pseudodifferential-operator approach *fails* to yield the required self-adjointness — instructive.

### Meta-rule (Clay Institute)
A Millennium proof is recognized only after publication in a reputable journal **and** ~2 years of standing in the community — never on a mere preprint announcement.

## Sources
- [Retracted: New Criterion for the Riemann Hypothesis — Cambridge Open Engage](https://www.cambridge.org/engage/coe/article-details/647ff4fe4f8b1884b7f34706)
- [On some results of Agelas concerning the GRH ... (Brent, arXiv 2103.09418)](https://arxiv.org/pdf/2103.09418)
- [Note on a proposed proof of the Riemann Hypothesis by Jin Gyu Lee (arXiv 1305.4614)](https://arxiv.org/pdf/1305.4614)
- [Pseudodifferential arithmetic and a failed attempt on the Riemann hypothesis (arXiv 2202.11652)](https://arxiv.org/pdf/2202.11652)
- [Millennium Prize Problems — Wikipedia](https://en.wikipedia.org/wiki/Millennium_Prize_Problems)
