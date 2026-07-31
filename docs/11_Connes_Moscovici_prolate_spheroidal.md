---
id: doc-11
number: 11
title: "Connes–Moscovici: Prolate Spheroidal Operator and Zeta (2021–2022)"
category: spectral
status: open
tags: [connes-moscovici, prolate-spheroidal, operator]
source_file: 11_Connes_Moscovici_prolate_spheroidal.md
lang: en
---

# Connes–Moscovici: Prolate Spheroidal Operator and Zeta (2021–2022)

**Category:** Spectral approach / noncommutative geometry (most recent development)
**Authors / year:** Alain Connes & Henri Moscovici (2021–2022); related: Connes–Consani "Spectral triples and ζ-cycles" (2021)
**Type:** Concrete (approximate) Hilbert–Pólya operator realization
**Status:** Active research; an "approximate" operator solution, not a complete RH proof

## Summary
From 2021 Connes and Moscovici studied the spectrum of the **prolate spheroidal wave operator** (a classical differential operator from signal processing / band limiting, originally studied by Slepian, Landau, Pollak at Bell Labs) and showed that its spectrum is closely related to the **squares of the Riemann zeros**. They describe this as a **concrete, approximate realization of the Hilbert–Pólya conjecture**.

## Core idea
- The **prolate operator** is an explicit, well-studied self-adjoint second-order differential operator.
- Restricted to the complement of a finite interval, it has **negative eigenvalues** whose ultraviolet behavior (asymptotic growth) exactly matches that of the **squares of the ζ zeros**.
- Uniquely extended to be self-adjoint on a larger domain, the eigenvalues are asymptotically similar to the squares of the zeros; a suitable "square root" of this operator thus yields an operator that solves the Hilbert–Pólya conjecture **approximately**.
- Embedded in Connes' **semilocal trace-formula framework** (Doc. 10): a semilocal analogue of the prolate wave operator integrates two recent discoveries on the spectral realization of the zeros.

## Significance / context
- For the first time a **classical, explicitly known** operator (not an ad-hoc construction) whose spectrum structurally reflects the zeros — methodologically remarkable.
- Connects signal processing / spectral theory / noncommutative geometry / number theory.
- **Caveat:** the agreement is asymptotic/approximate ("ultraviolet behavior", "approximate solution"). An *exact* spectral realization of *all* zeros together with a proof of the RH is thus **not** achieved.

## Mathematical core (formulas, theorems, proof sketches)

### The prolate wave operator
Classical Slepian–Landau–Pollak operator on L²(−1,1), commuting with the band-limited Fourier projection:
```
(W_λ f)(x) = d/dx [ (1 − x²) df/dx ] + λ² x² f
```
W_λ is self-adjoint with a discrete spectrum; its eigenfunctions are the **prolate spheroidal wave functions** (PSWF). Connes–Moscovici study the restriction to the **complement** of an interval.

### Key result (asymptotic spectrum)
For the self-adjoint extension of the operator restricted to the outer interval, the negative eigenvalues −E_n satisfy asymptotically (ultraviolet behavior)
```
E_n  ~  (γ_n / 2)²   resp.   the counting function of the E_n  ≈  counting function of the  γ_n²
```
where γ_n are the imaginary parts of the non-trivial zeros. That is: the spectrum reproduces the **squares of the Riemann zeros**.

### Square root ⇒ approximate Hilbert–Pólya solution
If one defines (heuristically) the operator √(prolate) on the appropriate subspace, it has eigenvalues ≈ γ_n/2 — a concrete self-adjoint operator whose spectrum *approximates* the γ_n. By self-adjointness these are real (which was always the goal, Doc. 05). Hence "concrete approximate realization of the Hilbert–Pólya conjecture".

### Embedding in the semilocal trace formula
Connes places this in the **semilocal** framework (finitely many places S = {∞, p_1, …, p_k}): a semilocal prolate operator W_S whose trace formula realizes the explicit formula over S (cf. Doc. 10). The statement to be reached remains global positivity.

### Why only approximate
The agreement E_n ~ (γ_n/2)² is **asymptotic** (leading order in the UV); the exact identity of the spectrum with all γ_n — and thus RH — is not established. Correction terms and the low-energy region are not controlled.

## Sources
- [Prolate spheroidal operator and Zeta — Connes & Moscovici (arXiv 2112.05500)](https://arxiv.org/pdf/2112.05500)
- [Prolate operator and Riemann Zeta — Connes (PNAS)](https://alainconnes.org/wp-content/uploads/PNAS_030322.pdf)
- [Prolate spheroidal functions and zeta — Alain Connes (Blog)](https://alainconnes.org/2021/12/prolate-spheroidal-functions-and-zeta/)
- [Zeta cycles — Connes–Consani (arXiv 2106.01715)](https://alainconnes.org/wp-content/uploads/zeta-cycles-3.pdf)
- [The Hilbert-Pólya Conjecture and the Prolate Spheroidal Operator (TU Delft thesis)](https://repository.tudelft.nl/file/File_a03b023e-2ba7-45fb-bde9-6fcc7a53d306)
