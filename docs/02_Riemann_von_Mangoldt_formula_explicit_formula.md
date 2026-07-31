---
id: doc-02
number: 02
title: "The Riemann–von Mangoldt Formula and the Explicit Formula"
category: foundations
status: reference
tags: [explicit-formula, von-mangoldt, counting-function, prime-counting]
source_file: 02_Riemann_von_Mangoldt_formula_explicit_formula.md
lang: en
---

# The Riemann–von Mangoldt Formula and the Explicit Formula

**Category:** Foundation
**Authors / year:** B. Riemann (1859, formulated), Hans von Mangoldt (1895/1905, proved)
**Type:** Structural tool (zero counting & prime–zero bridge)
**Status:** Proven; central infrastructure for RH research

## Summary
The Riemann–von Mangoldt formula describes the distribution of the zeros of the zeta function quantitatively. The associated *explicit formula* makes the central idea of the RH tangible: the non-trivial zeros directly control the distribution of the primes. Von Mangoldt proved in 1895 (fully in 1905) the formula given by Riemann in 1859.

## The counting formula N(T)
The number N(T) of non-trivial zeros with imaginary part in (0, T] satisfies:

```
N(T) = (T/2π) · log(T/2π) − (T/2π) + 7/8 + S(T) + (1/π)·δ(T)
```

- The smooth main term grows like (T/2π)·log(T/2π) → the zeros become denser with increasing height.
- **S(T)** is a fluctuation term (the argument of ζ along the line); its behavior is closely tied to the RH.
- **Backlund** gave an explicit error bound: |N(T) − main term| < 0.137·log(T) + 0.443·log(log T) + 4.350 for T > 2.

## The explicit formula (primes ↔ zeros)
With the Chebyshev function ψ(x) = Σ_{n≤x} Λ(n) (von Mangoldt function Λ) one has:

```
ψ(x) = x − Σ_ρ (x^ρ / ρ) − log(2π) − (1/2)·log(1 − x^(−2))
```

- The sum runs over **all non-trivial zeros ρ**.
- Each zero ρ = β + iγ contributes an oscillating term of order x^β. **This is exactly where the RH becomes significant:** if every zero lies at β = 1/2, then all error terms are of order √x — the smallest possible, "most regular" prime distribution (cf. Koch criterion: π(x) = Li(x) + O(√x·log x)).
- A zero off Re=1/2 would force a larger error term (x^β with β > 1/2) — so the RH is exactly the statement of maximal regularity of the prime distribution.

## Significance
- Provides the precise link "location of zeros ⇒ prime error term" and thereby the real motivation of the RH.
- Basis for zero-free regions (Doc. 12), the density hypothesis (Doc. 17), and all trace-formula approaches (Connes, Selberg, Doc. 10/19) that reinterpret the explicit formula as a "trace".

## Mathematical core (formulas, theorems, proof sketches)

### Derivation of the counting formula N(T) (argument principle)
N(T) counts zeros in the rectangle 0 < Im(s) < T of the critical strip. By the argument principle:
```
N(T) = (1/2π) ∮_∂R d arg ξ(s)
```
Evaluating the contributions along the boundary rectangle (with ξ(s) = (1/2)s(s−1)π^{−s/2}Γ(s/2)ζ(s)). The smooth part comes from the Stirling asymptotics of Γ:
```
N(T) = (T/2π) log(T/2π) − T/2π + 7/8 + S(T) + O(1/T)
```
with the **argument term** S(T) = (1/π) arg ζ(1/2 + iT) (continuously extended along a horizontal line). It is known that S(T) = O(log T) unconditionally; under RH even S(T) = O(log T / log log T).

### Mean zero density
Differentiating the main term gives the local density of the imaginary parts:
```
dN/dT ≈ (1/2π) log(T/2π)
```
i.e. the mean spacing of neighboring zeros at height T is ≈ 2π/log(T/2π) → 0. (Basis for the normalization in the pair correlation, Doc. 06.)

### Derivation of the explicit formula (Perron + residues)
Starting point: the logarithmic derivative of the Euler product,
```
−ζ'(s)/ζ(s) = Σ_{n=1}^∞ Λ(n) n^{−s},   Λ(n) = log p if n = p^k, else 0.
```
Perron formula for ψ(x) = Σ_{n≤x} Λ(n):
```
ψ(x) = (1/2πi) ∫_{c−i∞}^{c+i∞} (−ζ'(s)/ζ(s)) x^s/s ds   (c > 1)
```
Shifting the contour to the left and collecting the **residues** contributes:
- pole of ζ at s = 1 (residue of −ζ'/ζ · x^s/s is x) → main term **x**;
- each non-trivial zero ρ (pole of ζ'/ζ) → term **−x^ρ/ρ**;
- pole at s = 0 → −log(2π);
- trivial zeros s = −2n → +(1/2) log(1 − x^{−2}).
Result (von Mangoldt):
```
ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − (1/2) log(1 − x^{−2})
```

### Why RH ⟺ optimal error term
Write ρ = β + iγ. Then |x^ρ/ρ| = x^β/|ρ|. The sum over zeros yields
```
ψ(x) − x = − Σ_ρ x^ρ/ρ = O(x^{Θ} (log x)²),   Θ = sup_ρ β.
```
Under RH, Θ = 1/2, so ψ(x) = x + O(√x (log x)²), equivalent to **π(x) = Li(x) + O(√x log x)** (Koch 1901). A zero with β > 1/2 would increase the exponent Θ and thus the error. Hence:
```
RH  ⟺  ψ(x) − x = O(x^{1/2+ε})  ⟺  π(x) − Li(x) = O(x^{1/2+ε})
```

### Weil's explicit formula (general form, prime ↔ zero duality)
For a suitable test function g with Fourier transform h:
```
Σ_ρ h(γ) = (1/2π)∫ h(r)[ψ-term] dr − Σ_{n} Λ(n)/√n · g(log n) + (archimedean term)
```
This identity is the pivot of the trace-formula approaches (Connes, Doc. 10) and the positivity criteria (Weil/Li, Doc. 14).

## Sources
- [Riemann–von Mangoldt formula — Wikipedia](https://en.wikipedia.org/wiki/Riemann%E2%80%93von_Mangoldt_formula)
- [The Explicit Formula in simple terms (arXiv math/9810169)](https://arxiv.org/pdf/math/9810169)
- [Sketch of the Riemann-von Mangoldt explicit formula — Reed College](https://people.reed.edu/~jerry/361/lectures/rvm.pdf)
- [On the error term in the explicit formula of Riemann–von Mangoldt (arXiv 2111.10001)](https://arxiv.org/pdf/2111.10001)
