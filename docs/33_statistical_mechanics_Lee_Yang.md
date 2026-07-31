---
id: doc-33
number: 33
title: "Statistical Mechanics & the Lee–Yang Analogy (Newman)"
category: solution-program
status: open
tags: [statistical-mechanics, lee-yang, newman, polya, heat-flow]
source_file: 33_statistical_mechanics_Lee_Yang.md
lang: en
---

# Statistical Mechanics & the Lee–Yang Analogy (Newman)

**Category:** Solution-relevant analogy (mathematical physics)
**Authors / years:** Lee & Yang (1952); Pólya; Charles Newman (1976, 2016 mini-course); de Bruijn
**Type:** Physically motivated real-rootedness approach
**Status:** Structural analogy; contributes tools, not a proof

## Summary
There is a deep analogy between the RH (real-rootedness of the ξ-function) and the **Lee–Yang theorem** of statistical mechanics (zeros of partition functions lie on a circle/line). Charles Newman developed from this a statistical-mechanical view that led directly to the **de Bruijn–Newman constant** (Doc. 23) and provides tools for controlling real zeros.

## The analogy
- **Lee–Yang (1952):** for certain ferromagnetic spin models the zeros of the partition function (as a function of the fugacity/magnetic field) lie exactly on the unit circle resp. the imaginary axis — a *forced* location of the zeros due to positivity/correlation inequalities.
- **RH parallel:** the RH requires that the zeros of ξ all lie on the real axis (after rotation: the critical line). ξ is the Fourier transform of a **positive, even** function Φ.
- **Pólya's program:** Pólya studied sufficient conditions for Fourier transforms of positive even functions to have *only real* zeros — exactly the Lee–Yang-type question, applied to ξ.

## Newman's contribution & the deformation idea
- Newman (1976) introduced the **heat deformation** H_t of the ξ-function (convolution of Φ with a Gaussian kernel) and proved the existence of the **de Bruijn–Newman constant Λ**: H_t has only real zeros exactly when t ≥ Λ. RH ⟺ Λ ≤ 0 (Doc. 23).
- Tools from statistical mechanics (correlation inequalities, GHS inequality, monotonicity of the zeros under the heat flow) provide control over the movement of the zeros.
- **Lehmer pairs** (extremely close zeros) are the "critical configurations" that show how narrowly real-rootedness is preserved — they gave Rodgers–Tao (Doc. 23) the leverage for Λ ≥ 0.

## Significance / context
- Brings **positivity/correlation tools** of mathematical physics into RH research — methodologically fruitful (de Bruijn–Newman, Polymath15).
- Connects three strands: Pólya/Laguerre–Pólya (Doc. 29), de Bruijn–Newman (Doc. 23), and random matrices/quantum chaos (Doc. 06–08).
- **Limit:** provides a quantitative "how narrowly" and a strong heuristic, but no mechanism that forces Λ ≤ 0 — hence no proof.

## Mathematical core (formulas, theorems, proof sketches)

### Lee–Yang theorem (1952)
For a ferromagnetic Ising model with partition function as a polynomial in the fugacity z = e^{−2βh} (h = magnetic field):
```
Z_N(z) = Σ_{config} ... = c ∏_{k=1}^{N} (z − z_k).
```
**Theorem (Lee–Yang).** All zeros z_k lie on the unit circle |z_k| = 1 (equivalently: a purely imaginary field h). The proof uses positivity of the couplings (correlation inequalities) — the zeros are forced onto a curve by positivity.

### Analogy with the ξ-function
ξ is the Fourier (Laplace) transform of the **positive, even** density Φ (Doc. 23):
```
ξ(1/2 + iz) = ∫_{−∞}^∞ Φ(u) e^{izu} du,   Φ(u) > 0, Φ(−u) = Φ(u).
```
RH = "all zeros z real" is the **exact counterpart** of the Lee–Yang phenomenon (zeros on a line/curve, forced by the positivity of Φ).

### Pólya's criterion (sufficient condition)
**Theorem (Pólya).** If Φ(u) > 0 is even and satisfies certain convexity / log-concavity conditions (Φ in a suitable class), then ∫ Φ(u)e^{izu}du has only real zeros. The actual Φ for ξ is not demonstrably known to satisfy these sufficient conditions — this is exactly where the gap lies.

### Heat flow and Newman's Λ (connection to Doc. 23)
Convolve Φ with a Gaussian kernel (heat flow): Φ_t(u) = e^{t u²} weighting ⇒ H_t(z) = ∫ e^{tu²}Φ(u)e^{izu}du. The zeros z_k(t) satisfy a gradient-flow ODE
```
dz_k/dt = − Σ_{j≠k} 2/(z_k − z_j)   (Calogero-type dynamics / "Coulomb gas" on the line).
```
Real zeros are a fixed point of this dynamics for t ≥ Λ. The **GHS inequality** and monotonicity provide control ⇒ Newman's Λ exists, Λ ≤ 0 ⟺ RH.

### Lehmer pairs as critical configurations
Two zeros γ_n, γ_{n+1} with spacing ≪ the mean form a **Lehmer pair**; in the Coulomb-gas picture they are "nearly colliding" particles. Their existence (e.g. near γ ≈ 7005.06) shows that reality is held only narrowly — the leverage for Rodgers–Tao Λ ≥ 0 (Doc. 23).

## Sources
- [2016 Mini-Course by Chuck Newman — Statistical Mechanics and the Riemann Hypothesis (NYU Shanghai)](https://research.shanghai.nyu.edu/centers-and-institutes/math/2016-mini-course-chuck-newman-statistical-mechanics-and-riemann)
- [Constants of de Bruijn-Newman type in analytic number theory and statistical physics (arXiv 1901.06596)](https://arxiv.org/pdf/1901.06596)
- [Schoenberg's Theory of Totally Positive Functions and the Riemann Zeta Function (arXiv 2007.12889)](https://arxiv.org/pdf/2007.12889)
- [Lehmer pairs of zeros, the de Bruijn-Newman constant Λ, and the Riemann Hypothesis (ResearchGate)](https://www.researchgate.net/publication/226697760_Lehmer_pairs_of_zeros_the_de_Bruijn-Newman_constant_L_and_the_Riemann_Hypothesis)
- [The early historical roots of Lee-Yang theorem (arXiv 1410.6450)](https://arxiv.org/pdf/1410.6450)
