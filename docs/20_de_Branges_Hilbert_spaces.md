---
id: doc-20
number: 20
title: "Louis de Branges: Hilbert Spaces of Entire Functions (repeatedly failed proofs)"
category: analytic
status: refuted
tags: [de-branges, hilbert-spaces-entire-functions, conrey-li, failed]
source_file: 20_de_Branges_Hilbert_spaces.md
lang: en
---

# Louis de Branges: Hilbert Spaces of Entire Functions (repeatedly failed proofs)

**Category:** Analytic approach / prominent failed proof
**Author / years:** Louis de Branges (theory from ~1959; RH approach from 1986; proof claims including 2004, 2009, 2014, 2017)
**Type:** Functional-analytic approach + repeatedly erroneous proof claims
**Status:** ❌ All proof claims with gaps/errors; the approach as such open

## Summary
Louis de Branges (famous for his *correct* proof of the Bieberbach conjecture in 1984) developed an extensive theory of **Hilbert spaces of entire functions** and, from 1986, proposed an approach to the (generalized) RH based on it. Over decades he published several **proof claims**, all of which were found to be **incomplete or erroneous**. It is the most prominent case of a technically serious, repeatedly revised — but not accepted — RH proof attempt.

## Core idea of the approach
- De Branges' theory (late 1950s/1960s) generalizes the part of Fourier analysis around the Fourier transform and Plancherel formula to **Hilbert spaces whose elements are entire functions**.
- Roots in **Stieltjes'** approach to proving the RH; passage to infinitely many dimensions via the **Hermite class** of entire functions (limits of polynomials with a zero-free half-plane).
- **RH strategy (1986):** a **positivity condition** on certain **weighted Hardy spaces** / Stieltjes spaces of entire functions ("Riemann Hypothesis for Hilbert spaces of entire functions") would — applied to the space associated with the Euler zeta function — imply the (generalized) RH. The analytic weight function must have no zeros in a larger half-plane.

## Why the proofs failed
- Several published versions ("A Proof of the Riemann Hypothesis", Purdue preprints, including 2004, 2009, 2014, 2017) were examined by the community.
- **Typical problems:** the required positivity condition was not really established; the concretely constructed space does not satisfy the needed axioms; counterexamples (Conrey–Li, 2000) showed that the sufficient conditions in the proposed form do **not** hold for ζ, so the approach in this form cannot yield the RH.
- **Conrey & Li (2000)** published an influential critique ("A note on some positivity conditions related to zeta and L-functions") showing that de Branges' positivity criteria are not applicable to the zeta function.

## Significance / context
- A cautionary example: even a high-ranking mathematician with a genuine earlier major success can repeatedly fail on the RH — the mathematics community verifies rigorously.
- The underlying **theory of Hilbert spaces of entire functions** is valuable and correct in its own right; only its *application* to the RH did not succeed.
- Related to other positivity/Hilbert-space criteria (Nyman–Beurling Doc. 13, Weil positivity Doc. 14).

## Mathematical core (formulas, theorems, proof sketches)

### de Branges spaces H(E)
The starting point is a **Hermite–Biehler function** E(z): entire, with |E(z̄)| < |E(z)| for Im(z) > 0 (all zeros in the lower half-plane). The associated space:
```
H(E) = { f entire : ‖f‖² = ∫_{−∞}^∞ |f(x)/E(x)|² dx < ∞,  and f/E, f*/E ∈ H²(upper half-plane) }
```
H(E) is a **reproducing-kernel Hilbert space** with kernel
```
K(w, z) = ( E(z) E*(w̄) − E*(z) E(w̄) ) / ( 2πi (w̄ − z) ).
```

### Structure theorem & shrinking condition
De Branges' structure theory associates to a chain of nested spaces H(E_a) a **phase function** φ(x) (E(x) = |E(x)| e^{−iφ(x)}), with φ'(x) > 0. Membership of functions in such chains is governed by monotonicity/positivity conditions.

### Application to ζ: the ξ-function as E
One wants to choose E so that the structure associated with the ξ-function arises. Write ξ(1/2 + iz) as a function with real zeros (which holds exactly when RH holds). De Branges' **positivity criterion** (simplified): if for the associated weight function W(z) (analytic, zero-free in a half-plane)
```
(de Branges condition)   ∫ |f(x)|² / W(x) dx ≥ 0  resp. the phase monotonicity  φ'(x) ≥ 0
```
holds for all f of the space, then the zeros of ξ lie on the real axis ⇒ RH.

### Why it fails for ζ — Conrey–Li (2000)
Conrey and Li showed **concretely** that the positivity/structure condition required by de Branges is **violated** for the Euler ζ-function: they constructed explicit counterexamples to the sufficient conditions by showing that a certain function assumed by de Branges to be positive-definite (in connection with the E associated to ζ) takes **negative** values under numerical/analytic examination. Thus the approach in the proposed form is not applicable to ζ — the repeated proof attempts (2004–2017) do not circumvent this obstruction.

### Relation to other positivity criteria
The de Branges condition is closely related to Weil positivity (Doc. 14) and Nyman–Beurling (Doc. 13) — all require the positivity of a quadratic form / real-rootedness; all run into the same unsolved core hurdle.

## Sources
- [The Riemann hypothesis for Hilbert spaces of entire functions — de Branges (Purdue)](https://www.math.purdue.edu/~branges/riemann-hilbert.pdf)
- [A Proof of the Riemann Hypothesis — de Branges (2017 draft, Purdue)](https://www.math.purdue.edu/~branges/proof-riemann-2017-04.pdf)
- [The Strange Case of Louis de Branges — Karl Sabbagh, London Review of Books](https://www.lrb.co.uk/the-paper/v26/n14/karl-sabbagh/the-strange-case-of-louis-de-branges)
- [The early historical roots of Lee-Yang theorem (arXiv 1410.6450, context Hermite class)](https://arxiv.org/pdf/1410.6450)
