---
id: doc-00
number: 00
title: "Riemann Hypothesis — Document Index (RAG Knowledge Base)"
category: index
status: reference
tags: [index, overview]
source_file: 00_INDEX.md
lang: en
---

# Riemann Hypothesis — Document Index (RAG Knowledge Base)

> This knowledge base contains one self-contained document per paper, proof approach, criterion, failed proof, or milestone around the Riemann Hypothesis (RH). Each file is designed as an independently retrievable chunk for a vector database / RAG: uniform structure (metadata → summary → core idea → status → significance → sources). As of: June 2026.

## Categories and documents

### A. Foundations
- `01_Riemann_1859_original_paper.md` — Riemann's original 1859 paper, functional equation, Riemann–Siegel formula
- `02_Riemann_von_Mangoldt_formula_explicit_formula.md` — zero-counting formula N(T) and explicit formula (primes ↔ zeros)

### B. Partial results (zeros on the critical line)
- `03_Hardy_1914_infinitely_many_zeros.md` — Hardy: infinitely many zeros on the critical line
- `04_Levinson_Conrey_positive_proportion.md` — Levinson (1/3), Conrey (2/5), >41% positive proportion

### C. Spectral approaches / Hilbert–Pólya program
- `05_Hilbert_Polya_conjecture.md` — Hilbert–Pólya conjecture (self-adjoint operator)
- `06_Montgomery_pair_correlation_RMT.md` — Montgomery pair correlation & random matrices (GUE)
- `07_Keating_Snaith_moments.md` — Keating–Snaith: moments via characteristic polynomials (CUE)
- `08_Berry_Keating_xp_model.md` — Berry–Keating H = xp quantum-chaos model
- `09_Bender_Brody_Muller_2017_Hamiltonian.md` — Bender–Brody–Müller PT-symmetric Hamiltonian (2017)
- `10_Connes_noncommutative_geometry.md` — Connes: trace formula & noncommutative geometry
- `11_Connes_Moscovici_prolate_spheroidal.md` — Connes–Moscovici: prolate spheroidal operator (2021–2022)

### D. Analytic approaches & equivalent criteria
- `12_zero_free_regions.md` — zero-free regions (de la Vallée Poussin → Vinogradov–Korobov)
- `13_Nyman_Beurling_Baez_Duarte.md` — Nyman–Beurling criterion & Báez-Duarte sharpening
- `14_Li_criterion_Bombieri_Lagarias_Weil_positivity.md` — Li criterion, Bombieri–Lagarias, Weil positivity
- `15_Robin_inequality.md` — Robin's inequality (arithmetic criterion)
- `16_Mertens_function_Riesz_criterion.md` — Mertens function & Riesz criterion (Möbius)
- `17_Lindelof_density_hypothesis.md` — Lindelöf hypothesis & density hypothesis

### E. Proven analogues (algebraic/geometric)
- `18_Weil_conjectures_function_fields_Deligne.md` — Weil conjectures, RH over finite fields (Deligne, PROVEN)
- `19_Selberg_trace_formula_zeta.md` — Selberg trace formula & Selberg zeta function (RH analogue PROVEN)

### F. de Branges
- `20_de_Branges_Hilbert_spaces.md` — de Branges: Hilbert spaces of entire functions (repeatedly failed proofs)

### G. Generalizations
- `21_GRH_Selberg_class_grand_RH.md` — Generalized / Grand Riemann Hypothesis, Selberg class

### H. Recent breakthroughs
- `22_Guth_Maynard_2024.md` — Guth–Maynard zero-density breakthrough (2024)
- `23_de_Bruijn_Newman_constant_Polymath15.md` — de Bruijn–Newman constant, Rodgers–Tao, Polymath15

### I. Numerical verification
- `24_computational_verification.md` — Odlyzko, Platt (rigorous), ZetaGrid, Gourdon–Demichel

### J. Failed / disputed proofs
- `25_Atiyah_2018_failed_proof.md` — Atiyah's 2018 proof attempt (Todd function)
- `26_Nash_failed_attempt.md` — John Nash's attempt (1959)
- `27_other_disputed_claimed_proofs.md` — Further retracted/erroneous claims

### K. AI context
- `28_AI_and_RH.md` — AI/machine learning and the Riemann Hypothesis (student-paper context)

### L. Further active solution programs (potentially proof-relevant)
- `29_Jensen_Polya_Laguerre_Polya_GORZ.md` — Jensen–Pólya program, Laguerre–Pólya class, Griffin–Ono–Rolen–Zagier (2019)
- `30_F1_field_one_element_arithmetic_site.md` — field with one element 𝔽₁, Connes–Consani arithmetic site
- `31_Deninger_cohomology_foliated_dynamical.md` — Deninger's cohomology program & dynamical systems on foliated spaces
- `32_Landau_Siegel_zeros_Zhang.md` — Landau–Siegel (exceptional) zeros & Yitang Zhang (2022)
- `33_statistical_mechanics_Lee_Yang.md` — statistical mechanics & the Lee–Yang analogy (Newman)
- `34_Bost_Connes_system.md` — Bost–Connes quantum statistics (ζ as the partition function)

### M. Meta / "bulletproof" layer (obstructions, synthesis, verification)
- `35_obstructions_barriers.md` — **Why naive approaches MUST fail** (Davenport–Heilbronn, parity, Mertens/Skewes warnings) + anti-crackpot checklist
- `36_consequences_of_RH.md` — What follows from the RH (primes, Miller–Rabin, class numbers …)
- `37_formalization_lean_proof_assistants.md` — Lean/mathlib formalization as a verification gateway
- `38_Bombieri_official_problem_statement.md` — Official Clay problem statement (authoritative reference)
- `39_Cramer_probabilistic_model.md` — Cramér model & probabilistic heuristics (incl. Maier warning)
- `40_glossary_notation.md` — Glossary & notation (improves retrieval)
- `41_synthesis_what_a_proof_needs.md` — **Synthesis: cross-cutting motifs & necessary conditions for a valid proof**
- `42_timeline_and_reading_list.md` — Timeline & canonical reading list (Titchmarsh, Iwaniec–Kowalski, Conrey, AIM, LMFDB)
- `43_Epstein_zeta_Selberg_class_rigidity.md` — **Epstein zeta & Selberg-class rigidity: which property forces the line** (Tier-1 obstruction)
- `44_Lapidus_fractal_strings_spectral_operator.md` — Lapidus: fractal strings, inverse spectral problem (D=1/2), spectral operator
- `45_further_equivalent_criteria.md` — Volchkov, Sekatskii, Redheffer matrix, Salem, BBLS quantitative
- `46_Voronin_universality.md` — Voronin universality (meta-obstruction against "soft" proofs)
- `47_physics_layer_primon_gas_quantum_graphs.md` — Primon gas, Schumayer–Hutchinson, Sierra Rindler–Dirac, quantum graphs
- `48_Meyer_Kurokawa_algebraic_programs.md` — Meyer (distributions), Kurokawa (absolute zeta)
- `49_live_analytic_frontier.md` — Live frontier 2019–2026: explicit/log-free density, Tao program, Nelson subconvexity, Harper moments

## Source verification / research
This knowledge base was checked for completeness by a 5-step research agent (as of June 2026); documents 43–49 close the gaps identified in the process. Notes on use in a vector/MCP server: see `README_RAG.md`.

## Overarching survey file
The file `../Riemann_Hypothesis_Proof_Approaches.md` (one level up) contains the summarizing overall survey of all approaches in a single document.
