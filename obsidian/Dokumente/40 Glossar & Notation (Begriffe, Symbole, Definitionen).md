---
id: doc-40
title: "Glossar & Notation (Begriffe, Symbole, Definitionen)"
nummer: "40"
kategorie: Glossar
status: REFERENZ
typ: dokument
aliases:
  - "doc-40"
  - "Dok. 40"
tags:
  - "dokument"
  - "kategorie/glossary"
  - "status/reference"
  - "thema/definitions"
  - "thema/glossary"
  - "thema/notation"
quelle: docs/40_glossary_notation.md
---

> [!info] Navigation
> **Karte:** [[MOC M – Meta ∕ 'Bulletproof'-Schicht (Obstruktionen, Synthese, Verifikation)]] · **Kategorie:** Glossar · **Status:** `REFERENZ`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/40_glossary_notation.md`

# Glossar & Notation (Begriffe, Symbole, Definitionen)

**Kategorie:** Referenz (verbessert RAG-Retrieval bei Begriffsfragen)
**Typ:** Definitionssammlung
**Status:** Stabil

## Zweck
Nutzerfragen enthalten oft *Begriffe* statt Namen („Was ist die kritische Gerade?", „Was bedeutet GUE?"). Dieses Glossar erhöht die Retrieval-Trefferquote und verlinkt zu den vertiefenden Dokumenten.

## Funktionen & ihre Definitionen
- **Riemann-ζ:** ζ(s) = Σ_{n≥1} n^{−s} (Re s > 1), analytisch fortgesetzt; Pol bei s = 1. → Dok. [[01 Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel|01]]
- **Euler-Produkt:** ζ(s) = ∏_p (1−p^{−s})^{−1}; kodiert eindeutige Primfaktorzerlegung; impliziert ζ ≠ 0 für Re s > 1. → Dok. [[01 Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel|01]], [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]]
- **Vollständige ζ / ξ-Funktion:** ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s); ganz; ξ(s) = ξ(1−s). → Dok. [[01 Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel|01]]
- **Ξ(t):** Ξ(t) = ξ(1/2 + it), reellwertig für reelles t. → Dok. [[38 Bombieris offizielle Clay-Problemstellung (Millennium-Problem)|38]]
- **Hardysche Z-Funktion:** Z(t) = e^{iθ(t)} ζ(1/2+it), reell; |Z| = |ζ(1/2+it)|. → Dok. [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden|03]]
- **Riemann-Siegel-θ:** θ(t) = arg Γ(1/4+it/2) − (t/2)log π. → Dok. [[01 Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel|01]], [[24 Numerische Verifikation der Riemann-Vermutung|24]]
- **von-Mangoldt-Λ:** Λ(n) = log p falls n = p^k, sonst 0; −ζ'/ζ = Σ Λ(n)n^{−s}. → Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]]
- **Möbius-μ:** μ(n) = (−1)^{#Primf.} falls quadratfrei, sonst 0; 1/ζ = Σ μ(n)n^{−s}. → Dok. [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)|16]]
- **Mertens-M:** M(x) = Σ_{n≤x} μ(n). → Dok. [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)|16]]
- **Chebyshev-ψ:** ψ(x) = Σ_{n≤x} Λ(n); ψ(x) ~ x. → Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]]
- **Primzählfunktion:** π(x) = #{p ≤ x}; π(x) ~ Li(x). → Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]]
- **Li(x):** ∫_0^x dt/log t (Integrallogarithmus).
- **Dirichlet-L:** L(s,χ) = Σ χ(n)n^{−s} = ∏_p(1−χ(p)p^{−s})^{−1}. → Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]
- **Dedekind-ζ_K:** Zetafunktion eines Zahlkörpers K. → Dok. [[34 Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)|34]]

## Begriffe
- **Kritischer Streifen:** 0 < Re(s) < 1 (Bereich der nicht-trivialen Nullstellen).
- **Kritische Gerade:** Re(s) = 1/2 (vermuteter Ort *aller* nicht-trivialen Nullstellen).
- **Triviale Nullstellen:** s = −2, −4, −6, … (aus Funktionalgleichung).
- **Nicht-triviale Nullstellen:** ρ = β + iγ im kritischen Streifen; γ = Imaginärteil/„Höhe".
- **Funktionalgleichung:** ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s); Symmetrie s ↔ 1−s.
- **Nullstellenfreie Region:** Bereich nahe Re = 1, in dem ζ ≠ 0 bewiesen ist. → Dok. [[12 Nullstellenfreie Regionen (klassischer analytischer Ansatz)|12]]
- **Zählfunktion N(T):** Anzahl Nullstellen mit 0 < γ ≤ T ≈ (T/2π)log(T/2π). → Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]]
- **N(σ,T):** Anzahl Nullstellen mit β ≥ σ, γ ≤ T (Dichte abseits der Geraden). → Dok. [[17 Lindelöf-Hypothese & Dichte-Hypothese|17]], [[22 Guth–Maynard (2024) – Durchbruch bei Nullstellendichte-Abschätzungen|22]]
- **S(T):** (1/π) arg ζ(1/2+iT), Fluktuationsterm in N(T). → Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]]

## Statistik / Physik
- **GUE (Gaussian Unitary Ensemble):** Ensemble zufälliger hermitescher Matrizen; Eigenwert-Paarkorrelation 1−(sin πu/πu)². → Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]]
- **CUE (Circular Unitary Ensemble):** Haar-zufällige unitäre Matrizen; Modell für ζ-Momente. → Dok. [[07 Keating–Snaith – Momente der Zetafunktion via charakteristische Polynome (CUE)|07]]
- **Paarkorrelation:** Verteilung der Abstände γ−γ'. → Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]]
- **Niveau-Abstoßung:** Nullstellen meiden enge Abstände (R₂(u) → 0 für u → 0).
- **Lehmer-Paar:** zwei extrem nahe Nullstellen. → Dok. [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15|23]], [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]]
- **KMS-Zustand:** quantenstatistischer Gleichgewichtszustand. → Dok. [[34 Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)|34]]

## Kriterien-Stichworte
- **Koch:** π(x) = Li(x) + O(√x log x) ⟺ RH. → Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]]
- **Robin:** σ(n) < e^γ n log log n (n > 5040) ⟺ RH. → Dok. [[15 Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)|15]]
- **Li-Koeffizienten λ_n:** λ_n ≥ 0 ∀n ⟺ RH. → Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]
- **Weil-Positivität:** W(g⋆ḡ) ≥ 0 ⟺ RH. → Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]
- **Nyman–Beurling:** Dichte eines Funktionenraums ⟺ RH. → Dok. [[13 Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung|13]]
- **de-Bruijn–Newman Λ:** Λ ≤ 0 ⟺ RH. → Dok. [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15|23]]
- **Laguerre–Pólya:** ξ ∈ LP ⟺ RH. → Dok. [[29 Jensen–Pólya-Programm – Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)|29]]

## Verallgemeinerungen
- **GRH:** RH für alle Dirichlet-L-Funktionen. → Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]
- **Große RH:** RH für alle automorphen L-Funktionen. → Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]
- **Selberg-Klasse:** axiomatische L-Funktionen-Klasse. → Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]
- **RH über 𝔽_q:** RH-Analogon für Kurven über endlichen Körpern (BEWIESEN). → Dok. [[18 Weil-Vermutungen – RH über endlichen Körpern (Deligne) – BEWIESEN|18]]

---

## 🔗 Wissensgraph

### Im Text erwähnt

- [[01 Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel]]
- [[02 Riemann–von-Mangoldt-Formel und die explizite Formel]]
- [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden]]
- [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]]
- [[07 Keating–Snaith – Momente der Zetafunktion via charakteristische Polynome (CUE)]]
- [[12 Nullstellenfreie Regionen (klassischer analytischer Ansatz)]]
- [[13 Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]]
- [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]]
- [[15 Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)]]
- [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]]
- [[17 Lindelöf-Hypothese & Dichte-Hypothese]]
- [[18 Weil-Vermutungen – RH über endlichen Körpern (Deligne) – BEWIESEN]]
- [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse]]
- [[22 Guth–Maynard (2024) – Durchbruch bei Nullstellendichte-Abschätzungen]]
- [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15]]
- [[24 Numerische Verifikation der Riemann-Vermutung]]
- [[29 Jensen–Pólya-Programm – Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)]]
- [[34 Bost–Connes-System (Quantenstatistik mit ζ als Zustandssumme)]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
- [[38 Bombieris offizielle Clay-Problemstellung (Millennium-Problem)]]
