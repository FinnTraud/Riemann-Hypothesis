---
id: doc-22
number: 22
title: "Guth–Maynard (2024): Durchbruch bei Nullstellendichte-Abschätzungen"
category: breakthrough
status: proven
tags: [guth-maynard, zero-density, decoupling, dirichlet-polynomials, 2024]
source_file: 22_Guth_Maynard_2024.md
lang: de
---

# Guth–Maynard (2024): Durchbruch bei Nullstellendichte-Abschätzungen

**Kategorie:** Aktueller Durchbruch (unbedingt, kein RH-Beweis)
**Autoren / Jahr:** Larry Guth & James Maynard, 2024
**Typ:** Verbesserte Nullstellendichte-Abschätzung
**Status:** ✅ Bewiesen; wichtigster unbedingter Fortschritt seit Jahrzehnten — aber NICHT die RH

## Zusammenfassung
Larry Guth und James Maynard erzielten 2024 die **erste substanzielle Verbesserung seit über 80 Jahren** einer klassischen Nullstellendichte-Abschätzung von Ingham (1940). Terence Tao bezeichnete dies öffentlich als "bemerkenswerten Durchbruch". Es ist der bedeutendste *unbedingte* (RH-unabhängige) Fortschritt im RH-Umfeld seit Jahrzehnten — beweist aber **nicht** die RH.

## Das Resultat
- Mit N(σ, T) = Anzahl der ζ-Nullstellen mit Realteil ≥ σ und Imaginärteil ≤ T (Maß dafür, wie viele Nullstellen *abseits* der kritischen Geraden in einem Höhenbereich liegen könnten).
- **Ingham (1940):** N(3/4, T) ≪ T^{3/5 + o(1)}. Über 80 Jahre verbesserte sich nur der o(1)-Term, nicht der Exponent.
- **Guth–Maynard (2024):** Verbesserung des **Exponenten selbst** — im Bereich um σ = 3/4 Schranken der Größenordnung N(σ,T) ≪ T^{13/25 + o(1)} (13/25 = 0,52 < 3/5 = 0,6).

## Kernidee / Methode
- Neue **Dirichlet-Polynom-Abschätzungen** mittels **Decoupling-Techniken** aus der harmonischen Analysis (verwandt mit den Methoden hinter der Lösung der Vinogradov-Mittelwertvermutung durch Bourgain–Demeter–Guth).
- Import von Werkzeugen aus der harmonischen Analysis / geometrischen Maßtheorie in die analytische Zahlentheorie — als "Paradigmenwechsel" beschrieben.

## Bedeutung / Einordnung
- **Warum wichtig:** Nullstellendichte-Abschätzungen begrenzen, wie viele Nullstellen *überhaupt* abseits der Geraden existieren könnten, und fließen direkt in Primzahl-Resultate ein (z. B. Primzahlen in kurzen Intervallen) — **ohne** die RH vorauszusetzen. Guth–Maynard verbessern damit unbedingte Aussagen über die Primzahlverteilung.
- **Was es NICHT ist:** Kein Beweis der RH und kein Anspruch darauf. Es verschärft nur die Dichteschranken in einem Teil des kritischen Streifens.
- Belebt die Hoffnung, dass moderne Harmonische-Analysis-Methoden weitere Exponenten verbessern (vgl. Dichte-Hypothese, Dok. 17).

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Zähl-/Dichtefunktion
N(σ, T) = #{ ρ = β + iγ : ζ(ρ) = 0, β ≥ σ, 0 ≤ γ ≤ T }. Unter RH ist N(σ,T) = 0 für σ > 1/2; unbedingt sucht man kleine obere Schranken.

### Inghams Schranke (1940) und das Resultat
```
Ingham:        N(σ, T) ≪ T^{ 3(1−σ)/(2−σ) + o(1) }    ⇒  N(3/4, T) ≪ T^{3/5 + o(1)}.
Guth–Maynard:  N(σ, T) ≪ T^{ 30(1−σ)/13 + o(1) }       für  3/4 ≤ σ ≤ 1,
               ⇒  N(3/4, T) ≪ T^{30/13·1/4 + o(1)} = T^{15/26+o(1)} ≈ T^{0,577};
               in der Schlüsselregion erreichen sie den Exponenten 13/25 = 0,52 bei σ = 3/4.
```
(Der zentrale Gewinn ist die Verbesserung 3/5 = 0,6 → 13/25 = 0,52 bei σ = 3/4 — der erste Bruch des Exponenten seit Ingham 1940.)

### Reduktion auf Dirichlet-Polynom-Großwerte
Wie üblich übersetzt sich die Nullstellendichte (via Zero-Detecting-Polynome, mean-value + large values) in eine Frage über **Großwerte von Dirichlet-Polynomen**
```
D(t) = Σ_{n ~ N} b_n n^{−it},   b_n beschränkt.
```
Man muss abschätzen, wie oft (für gut separierte t_r) |D(t_r)| groß sein kann — ein „large values" Problem.

### Neue Zutat: Decoupling
Guth–Maynard wenden **ℓ²-Decoupling** (Bourgain–Demeter) auf die Frequenzen log n an: Sie zerlegen den Frequenzbereich in Blöcke und nutzen die quasi-Orthogonalität, um die ℓ^p-Norm der Großwerte durch die Summe der Blöcke zu kontrollieren:
```
‖ Σ_θ D_θ ‖_{L^p}  ≲_ε  N^ε ( Σ_θ ‖D_θ‖_{L^p}² )^{1/2}    (Decoupling-Ungleichung),
```
kombiniert mit einer neuen geometrischen Analyse der Menge der „resonanten" t_r. Das schlägt die klassische Montgomery/Halász-Large-Values-Schranke in diesem Regime.

### Konsequenz für Primzahlen
Bessere N(σ,T)-Schranken ⇒ asymptotische Primzahlzählung in kürzeren Intervallen: Guth–Maynard verbessern unbedingt die Länge θ in „Primzahlen in [x, x + x^θ]" — konkret Resultate über Primzahlen in Intervallen der Länge x^{0,55+ε} (statt vormals größerer Exponenten), unabhängig von RH.

## Quellen
- [Terence Tao on the Guth–Maynard breakthrough (Mathstodon)](https://mathstodon.xyz/@tao/112557248794707738)
- [The Riemann Hypothesis ... Is a Step Closer to Being Solved — Scientific American](https://www.scientificamerican.com/article/the-riemann-hypothesis-the-biggest-problem-in-mathematics-is-a-step-closer/)
- [New Horizons in Riemann Zeta Function Analysis: From Guth-Maynard Estimates ... (ResearchGate)](https://www.researchgate.net/publication/398421128_NEW_HORIZONS_IN_RIEMANN_ZETA_FUNCTION_ANALYSIS_FROM_GUTH-MAYNARD_ESTIMATES_TO_THE_GADU-IOMM_OPERATORIAL_PARADIGM)
- [The Riemann Hypothesis: Past, Present and a Letter Through Time (arXiv 2602.04022)](https://arxiv.org/abs/2602.04022)
