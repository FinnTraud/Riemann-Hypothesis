---
id: doc-01
title: "Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel"
nummer: "01"
kategorie: Fundamente
status: REFERENZ
typ: dokument
aliases:
  - "doc-01"
  - "Dok. 01"
tags:
  - "dokument"
  - "kategorie/foundations"
  - "status/reference"
  - "thema/euler-product"
  - "thema/functional-equation"
  - "thema/riemann-siegel"
  - "thema/xi-function"
  - "thema/zeta"
quelle: docs/01_Riemann_1859_original_paper.md
---

> [!info] Navigation
> **Karte:** [[MOC A – Fundamente]] · **Kategorie:** Fundamente · **Status:** `REFERENZ`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/01_Riemann_1859_original_paper.md`

# Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel

**Kategorie:** Fundament
**Autor / Jahr:** Bernhard Riemann, 1859 (Riemann-Siegel-Anteil: Siegel 1932 aus dem Nachlass)
**Typ:** Ursprungspaper, in dem die Vermutung formuliert wird
**Status:** Historisches Fundament; enthält die ungelöste Vermutung

## Zusammenfassung
"Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse" ist eine ca. 9-seitige Arbeit von Bernhard Riemann, veröffentlicht im November 1859 in den *Monatsberichten der Königlich Preußischen Akademie der Wissenschaften zu Berlin*. Es ist die einzige Arbeit Riemanns zur Zahlentheorie überhaupt — und sie revolutionierte die Mathematik. In ihr formuliert Riemann beiläufig die berühmte Vermutung, dass alle nicht-trivialen Nullstellen der Zetafunktion den Realteil 1/2 besitzen.

## Kernideen der Arbeit
- **Analytische Fortsetzung:** Riemann setzt die Reihe ζ(s) = Σ 1/n^s (zunächst nur für Re(s) > 1 konvergent) auf die gesamte komplexe Ebene fort (mit einfachem Pol bei s = 1).
- **Funktionalgleichung:** Er beweist die Symmetrie ζ(s) ↔ ζ(1−s), formuliert über die vervollständigte Funktion ξ(s), die unter s ↦ 1−s invariant ist. Daraus folgt die Symmetrie der nicht-trivialen Nullstellen um die kritische Gerade Re(s) = 1/2.
- **Produktdarstellung / Hadamard-Produkt** für ganze Funktionen (später von Hadamard streng begründet).
- **Verbindung Primzahlen ↔ Nullstellen:** Riemann gibt eine explizite Formel für die Primzahlfunktion an, in der die nicht-trivialen Nullstellen als oszillierende Korrekturterme auftreten.
- **Die Vermutung selbst:** Riemann schreibt, es sei "sehr wahrscheinlich", dass alle nicht-trivialen Nullstellen auf Re(s) = 1/2 liegen — er habe jedoch nach einigen flüchtigen Versuchen den Beweis beiseitegelegt, da er für sein unmittelbares Ziel entbehrlich war.

## Die Riemann-Siegel-Formel (aus dem Nachlass)
- Riemanns private Notizen enthielten eine hocheffiziente asymptotische Formel zur numerischen Berechnung von ζ(1/2 + it) — die **Riemann-Siegel-Formel** — sowie konkrete Berechnungen der ersten Nullstellen.
- Diese Ergebnisse blieben unveröffentlicht und wurden erst **Anfang der 1930er Jahre von Carl Ludwig Siegel** im Nachlass entdeckt und 1932 publiziert ("Über Riemanns Nachlaß zur analytischen Zahlentheorie").
- Die Formel ist bis heute Grundlage vieler numerischer Nullstellen-Verifikationen (siehe Dokument [[24 Numerische Verifikation der Riemann-Vermutung|24]]).

## Bedeutung
- Begründet die analytische Zahlentheorie als Disziplin.
- Liefert die strukturelle Grundlage (Funktionalgleichung, explizite Formel) für praktisch alle späteren Beweisansätze.
- Zeigt: Riemann selbst hatte bereits numerische Evidenz, hielt die Aussage aber für nebensächlich gegenüber dem Primzahlsatz.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Eulerprodukt (Ausgangspunkt)
Für Re(s) > 1 gilt die von Euler entdeckte Identität, die ζ mit den Primzahlen verknüpft:
```
ζ(s) = Σ_{n=1}^∞ 1/n^s = ∏_{p prim} (1 − p^{−s})^{−1}
```
Beweis (Skizze): Geometrische Reihe (1 − p^{−s})^{−1} = Σ_{k≥0} p^{−ks}; Ausmultiplizieren über alle p liefert wegen eindeutiger Primfaktorzerlegung jeden Term n^{−s} genau einmal. Aus dem Produkt folgt ζ(s) ≠ 0 für Re(s) > 1 (kein Faktor verschwindet, Konvergenz).

### Analytische Fortsetzung über die Theta-Funktion
Mit der Jacobischen Theta-Funktion ψ(x) = Σ_{n=1}^∞ e^{−n²πx} und der Integraldarstellung
```
π^{−s/2} Γ(s/2) ζ(s) = ∫_0^∞ x^{s/2 − 1} ψ(x) dx
```
nutzt Riemann die Funktionalgleichung der Theta-Funktion ψ(1/x) = −1/2 + (1/2)√x + √x·ψ(x) (aus der Poisson-Summenformel), um das Integral in eine für alle s ∈ ℂ konvergente Form zu spalten:
```
ξ-Integral:  π^{−s/2}Γ(s/2)ζ(s) = 1/(s(s−1)) + ∫_1^∞ (x^{s/2−1} + x^{−(s+1)/2}) ψ(x) dx
```
Die rechte Seite ist offensichtlich invariant unter s ↦ 1 − s ⇒ Funktionalgleichung.

### Funktionalgleichung
```
ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s)
```
oder symmetrisch über die vervollständigte Funktion (vollständige Zeta):
```
ξ(s) := (1/2) s(s−1) π^{−s/2} Γ(s/2) ζ(s),     ξ(s) = ξ(1 − s)
```
ξ ist eine ganze Funktion (Pol bei s=1 und trivialer Faktor herausgekürzt). Die Symmetrie ξ(s) = ξ(1−s) zwingt die nicht-trivialen Nullstellen in spiegelsymmetrische Lage zur Geraden Re(s) = 1/2. Zusammen mit ξ(s) = ξ(s̄) (reelle Koeffizienten) liegen Nullstellen in Quadrupeln ρ, 1−ρ, ρ̄, 1−ρ̄ (außer auf der Geraden, wo sie zu Paaren ρ, ρ̄ kollabieren).

### Triviale Nullstellen
Der Faktor sin(πs/2) in der Funktionalgleichung erzwingt ζ(−2n) = 0 für n = 1, 2, 3, … (triviale Nullstellen); diese werden in ξ durch Γ(s/2) kompensiert.

### Die explizite Formel (Riemanns Resultat)
Riemann gibt für die gewichtete Primzahlfunktion J(x) = Σ_{p^k ≤ x} 1/k eine Formel an:
```
J(x) = Li(x) − Σ_ρ Li(x^ρ) − log 2 + ∫_x^∞ dt/(t(t²−1) log t)
```
und kehrt via Möbius-Inversion zu π(x) = Σ_{n} μ(n)/n · J(x^{1/n}) zurück. Die Summe Σ_ρ über die Nullstellen ist der oszillierende Korrekturterm (vgl. Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]]).

### Riemann-Siegel-Formel (aus dem Nachlass)
Zur Berechnung auf der kritischen Geraden mit Z(t) = e^{iθ(t)} ζ(1/2 + it) (reell):
```
Z(t) = 2 Σ_{n=1}^{N} cos(θ(t) − t log n)/√n  +  R(t),   N = ⌊√(t/2π)⌋
```
mit Riemann-Siegel-Theta θ(t) = arg Γ(1/4 + it/2) − (t/2) log π und einem asymptotisch berechenbaren Restterm R(t) ~ (−1)^{N−1} (t/2π)^{−1/4} · [C_0 + C_1(t/2π)^{−1/2} + …].

## Quellen
- [On the Number of Primes Less Than a Given Magnitude — Wikipedia](https://en.wikipedia.org/wiki/On_the_Number_of_Primes_Less_Than_a_Given_Magnitude)
- [On Riemann's Paper "On the Number of Primes Less Than a Given Magnitude" (arXiv 1609.02301)](https://arxiv.org/abs/1609.02301)
- [On a Fair Copy of Riemann's 1859 Publication Created by Alfred Clebsch (arXiv 1512.02976)](https://arxiv.org/pdf/1512.02976)
- [On Riemann's Nachlass for Analytic Number Theory: A translation of Siegel's Über (arXiv 1810.05198)](https://arxiv.org/pdf/1810.05198)
- [A computational history of prime numbers and Riemann zeros (arXiv 1810.05244)](https://arxiv.org/pdf/1810.05244)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Instanz von** → [[Kritische Gerade Re(s)=1∕2]] — *Riemann 1859: Funktionalgleichung erzeugt Symmetrie um Re=1/2.*

### Eingehende Relationen

- **wird genutzt von** ← [[02 Riemann–von-Mangoldt-Formel und die explizite Formel]] — *Explizite Formel baut auf Funktionalgleichung/ξ auf.*

### Im Text erwähnt

- [[24 Numerische Verifikation der Riemann-Vermutung]]
