---
id: doc-47
number: 47
title: "Physics Layer: Primon Gas, Schumayer–Hutchinson, Sierra Models & Quantum Graphs"
category: spectral
status: open
tags: [primon-gas, riemann-gas, schumayer-hutchinson, sierra, quantum-graphs, physics]
source_file: 47_physics_layer_primon_gas_quantum_graphs.md
lang: en
---

# Physics Layer: Primon Gas, Schumayer–Hutchinson, Sierra Models & Quantum Graphs

**Category:** Spectral approach / mathematical physics (consolidation)
**Authors / years:** Julia (primon gas, 1990); Spector; Schumayer–Hutchinson (survey, RMP 2011); Sierra (Rindler–Dirac, 2008); various (quantum graphs, 2013)
**Type:** Physical models / realization attempts (Hilbert–Pólya area)
**Status:** Heuristic/model-based; not an RH proof

## Summary
Consolidates the physical modeling layer around the Riemann zeros that goes beyond Berry–Keating (Doc. 08) and Bender–Brody–Müller (Doc. 09): the **primon gas** (ζ as the partition function of free bosons), Sierra's explicit Hamiltonian models, and **quantum graphs** whose spectra reproduce the zeros. The main reference is the RMP survey by Schumayer–Hutchinson.

## Mathematical core (formulas, models)

### Primon gas / "Riemann gas" (Julia)
Free bosons whose single-particle energy levels are the **logarithms of the primes**: ε_p = log p. A state = a multiset of "primons"; an integer n = ∏ p^{k_p} has energy E_n = Σ k_p log p = log n. Partition function at inverse temperature β:
```
Z(β) = Σ_{states} e^{−βE} = Σ_{n=1}^∞ n^{−β} = ζ(β).
```
- **Hagedorn temperature:** the pole at β = 1 is a Hagedorn-like divergence (phase transition) — this is the elementary statistical mechanics behind the Bost–Connes system (Doc. 34).
- **Fermionic primon gas:** the Pauli principle (each prime at most once) ⇒ squarefree numbers, and the partition function involves ζ(β)/ζ(2β) resp. the Möbius function μ(n) (the sign = fermion parity). Connected to Mertens (Doc. 16).

### Schumayer–Hutchinson survey (RMP 2011)
"Physics of the Riemann Hypothesis" — the canonical overview of all physical approaches: quantum chaos, xp models, random matrices, primon gas, spectral statistics, quantum graphs. The recommended main reference on the physics side.

### Sierra: Rindler–Dirac model ("Riemann magneton of the primes", 2008)
A relativistic Dirac particle in **Rindler coordinates** (uniformly accelerated observer) with δ-potentials localized on **squarefree numbers**. The scattering phases reproduce — via a quantization condition — the smoothed zero density. A more concrete realization of the xp idea (Doc. 08) with a built-in prime structure.

### Quantum graphs
Metric graphs with edge lengths ∝ log p; the spectrum of the Laplace operator on the graph (with Kirchhoff boundary conditions) is tuned so that the eigenvalues approximate the γ_n. The graph's **orbit-sum (trace) formula** mimics the explicit formula (closed paths ↔ products of primes).

## Significance / context
- Provides physical **intuition** and concrete (albeit approximate) spectral realizations in the Hilbert–Pólya spirit (Doc. 05).
- **Common limit:** all reproduce the *smoothed* density or approximate the γ_n; none yields the exact zeros as the spectrum of a canonical self-adjoint operator (cf. obstruction Doc. 35, point 5).
- The primon gas grounds the Bost–Connes system (Doc. 34) physically.

## Sources
- [Physics of the Riemann Hypothesis — Schumayer & Hutchinson, Rev. Mod. Phys. 83, 307 (2011) (ar5iv)](https://ar5iv.labs.arxiv.org/html/1101.3116)
- [The Riemann Magneton of the Primes — Sierra (arXiv math-ph/0404031)](https://arxiv.org/pdf/math-ph/0404031)
- [Quantum graphs and the Riemann zeros (arXiv 1307.6055)](https://arxiv.org/pdf/1307.6055)
- [Riemann zeros as quantized energies of scattering with impurities (arXiv 2307.01254)](https://arxiv.org/pdf/2307.01254)
