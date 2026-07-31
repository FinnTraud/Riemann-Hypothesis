---
id: doc-08
number: 08
title: "The Berry–Keating H = xp Model (quantum-chaos approach)"
category: spectral
status: open
tags: [berry-keating, xp-model, quantum-chaos, semiclassical]
source_file: 08_Berry_Keating_xp_model.md
lang: en
---

# The Berry–Keating H = xp Model (quantum-chaos approach)

**Category:** Spectral approach / quantum physics
**Authors / year:** Michael Berry, Jonathan Keating (1999); precursors & variants Sierra, Townsend and others (from 2008/2011)
**Type:** Physical operator model (Hilbert–Pólya candidate)
**Status:** Heuristic; yields only the smoothed zero density, no rigorous operator

## Summary
Berry and Keating proposed that the Riemann zeros are the energy levels (eigenvalues) of a quantum-mechanical operator arising from the quantization of the classical Hamiltonian **H = xp** (position × momentum). This is motivated by **quantum chaos**: in chaotic quantum systems the energy levels follow GUE statistics — exactly like the ζ zeros (Doc. 06).

## Core idea
- The classical Hamiltonian H = xp has hyperbolic trajectories (unstable, "chaotic").
- A semiclassical quantization gives a mean level density that asymptotically matches the **mean density of the Riemann zeros** N(T) ~ (T/2π)log(T/2π).
- **Berry's quantum-chaos conjecture:** the zeros are the spectrum of a Hamiltonian whose classical periodic orbits are indexed by the **primes** (periodic orbits ↔ primes, orbit lengths ↔ log p) — a physical reading of the explicit formula (Doc. 02).

## Known problems
- Naive quantization of H = xp yields only the **smooth/mean** zero density, **not** the exact zero positions.
- The spectrum is **continuous** rather than discrete unless a suitable regularization / boundary condition is chosen.
- Various regularizations:
  - **Berry–Keating:** a discrete spectrum that approximates the *smoothed* zeros.
  - **Connes:** absorption spectrum — the zeros appear as *missing* spectral lines (Doc. 10).
  - **Sierra & Townsend (2011):** models H = x(p + 1/p) resp. H = (x + 1/x)(p + 1/p) that produce a discrete spectrum with the smooth zero-counting function.

## Significance / context
- The most concrete *physical* embodiment of the Hilbert–Pólya idea.
- Connects primes ↔ periodic orbits ↔ spectral lines.
- **As of 2026:** no construction yields the *exact* zeros as eigenvalues of a rigorously defined self-adjoint operator — only smoothed/statistical agreement. Hence no complete RH proof.

## Mathematical core (formulas, theorems, proof sketches)

### Classical H = xp and semiclassical level counting
The classical Hamiltonian H = x·p has hyperbolic trajectories x p = E (hyperbolas in phase space). The semiclassical number of states with energy ≤ E is the phase-space volume / (2πℏ):
```
N_{sc}(E) = (1/2πℏ) · Vol{ (x,p) : 0 < x p < E, with cutoffs x ≥ ℓ_x, p ≥ ℓ_p }
```
With cutoffs x ≥ l_x, p ≥ l_p (cutoffs l_x l_p = 2πℏ) one obtains
```
N_{sc}(E) = (E/2πℏ)( log(E/2πℏ) − 1 ) + 7/8 + …
```

### Agreement with the Riemann counting function
Compare with the smooth part of N(T) (Doc. 02):
```
⟨N(E)⟩ = (E/2π) log(E/2π) − E/2π + 7/8 + …
```
Setting ℏ = 1, the **smooth term including the constant 7/8** agrees! This is the central observation of Berry–Keating: H = xp reproduces the mean zero density exactly.

### Missing pieces (why only "smooth")
- The fluctuating correction N(E) − ⟨N(E)⟩ = S(E)/π (Doc. 02) would correspond in the Gutzwiller trace formula to a sum over periodic orbits:
```
N_{fl}(E) ≈ (1/π) Σ_p Σ_{r≥1} (1/r) (Λ(p^r)/p^{r/2}) sin(r E log p)
```
— formally identical to the explicit formula with primes p as "orbits" of period log p. But: the bare H = xp has **no** periodic orbits (trajectories run off to infinity) ⇒ continuous spectrum, the fluctuation term is missing.
- Remedy via modification (Sierra–Townsend 2011):
```
H = x(p + ℓ_p²/p)   resp.   H = (x + ℓ_x²/x)(p + ℓ_p²/p)
```
produces bound, discrete spectra that approximate the smoothed zeros; the *exact* γ_n remain out of reach.

### Connes regularization (contrast)
Connes' adelic version (Doc. 10) yields, instead of a discrete emission spectrum, an **absorption spectrum**: the γ_n appear as *gaps* (missing lines) in the continuum — formally a trace over the adele-class space with the explicit formula as a trace formula.

## Sources
- [H = xp and the Riemann Zeros — Berry & Keating (Springer)](https://link.springer.com/chapter/10.1007/978-1-4615-4875-1_19)
- [The Riemann zeros as spectrum and the Riemann hypothesis (arXiv 1601.01797)](https://arxiv.org/pdf/1601.01797)
- [General covariant xp models and the Riemann zeros (arXiv 1110.3203)](https://arxiv.org/pdf/1110.3203)
- [H = xp with interaction and the Riemann zeros (arXiv math-ph/0702034)](https://arxiv.org/pdf/math-ph/0702034)
- [Landau levels and Riemann zeros (arXiv 0805.4079)](https://arxiv.org/pdf/0805.4079)
