---
id: doc-02
title: "Riemann–von-Mangoldt-Formel und die explizite Formel"
nummer: "02"
kategorie: Fundamente
status: REFERENZ
typ: dokument
aliases:
  - "doc-02"
  - "Dok. 02"
tags:
  - "dokument"
  - "kategorie/foundations"
  - "status/reference"
  - "thema/counting-function"
  - "thema/explicit-formula"
  - "thema/prime-counting"
  - "thema/von-mangoldt"
quelle: docs/02_Riemann_von_Mangoldt_formula_explicit_formula.md
---

> [!info] Navigation
> **Karte:** [[MOC A – Fundamente]] · **Kategorie:** Fundamente · **Status:** `REFERENZ`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/02_Riemann_von_Mangoldt_formula_explicit_formula.md`

# Riemann–von-Mangoldt-Formel und die explizite Formel

**Kategorie:** Fundament
**Autoren / Jahr:** B. Riemann (1859, formuliert), Hans von Mangoldt (1895/1905, bewiesen)
**Typ:** Strukturelles Werkzeug (Nullstellenzählung & Primzahl-Nullstellen-Brücke)
**Status:** Bewiesen; zentrale Infrastruktur für RH-Forschung

## Zusammenfassung
Die Riemann–von-Mangoldt-Formel beschreibt die Verteilung der Nullstellen der Zetafunktion quantitativ. Die zugehörige *explizite Formel* macht die zentrale Idee der RH greifbar: Die nicht-trivialen Nullstellen kontrollieren direkt die Verteilung der Primzahlen. Von Mangoldt bewies 1895 (vollständig 1905) die von Riemann 1859 angegebene Formel.

## Die Zählformel N(T)
Die Anzahl N(T) der nicht-trivialen Nullstellen mit Imaginärteil in (0, T] erfüllt:

```
N(T) = (T/2π) · log(T/2π) − (T/2π) + 7/8 + S(T) + (1/π)·δ(T)
```

- Der glatte Hauptterm wächst wie (T/2π)·log(T/2π) → die Nullstellen werden mit zunehmender Höhe dichter.
- **S(T)** ist ein Fluktuationsterm (Argument von ζ entlang der Geraden); sein Verhalten ist eng mit der RH verknüpft.
- **Backlund** gab eine explizite Fehlerschranke: |N(T) − Hauptterm| < 0,137·log(T) + 0,443·log(log T) + 4,350 für T > 2.

## Die explizite Formel (Primzahlen ↔ Nullstellen)
Mit der Chebyshev-Funktion ψ(x) = Σ_{n≤x} Λ(n) (von-Mangoldt-Funktion Λ) gilt:

```
ψ(x) = x − Σ_ρ (x^ρ / ρ) − log(2π) − (1/2)·log(1 − x^(−2))
```

- Die Summe läuft über **alle nicht-trivialen Nullstellen ρ**.
- Jede Nullstelle ρ = β + iγ liefert einen oszillierenden Term der Größenordnung x^β. **Genau hier wird die RH bedeutsam:** Liegt jede Nullstelle bei β = 1/2, sind alle Fehlerterme von der Ordnung √x — die kleinstmögliche, "regulärste" Primzahlverteilung (vgl. Koch-Kriterium: π(x) = Li(x) + O(√x·log x)).
- Eine Nullstelle abseits von Re=1/2 würde einen größeren Fehlerterm (x^β mit β > 1/2) erzwingen — die RH ist also exakt die Aussage maximaler Regularität der Primzahlverteilung.

## Bedeutung
- Liefert das präzise Bindeglied "Nullstellenlage ⇒ Primzahl-Fehlerterm" und damit die eigentliche Motivation der RH.
- Grundlage für nullstellenfreie Regionen (Dok. [[12 Nullstellenfreie Regionen (klassischer analytischer Ansatz)|12]]), Dichte-Hypothese (Dok. [[17 Lindelöf-Hypothese & Dichte-Hypothese|17]]) und alle Spurformel-Ansätze (Connes, Selberg, Dok. [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]]/[[19 Selberg-Spurformel & Selberg-Zetafunktion (RH-Analogon BEWIESEN)|19]]), die die explizite Formel als "Spur" reinterpretieren.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Herleitung der Zählformel N(T) (Argumentprinzip)
N(T) zählt Nullstellen im Rechteck 0 < Im(s) < T des kritischen Streifens. Per Argumentprinzip:
```
N(T) = (1/2π) ∮_∂R d arg ξ(s)
```
Auswertung der Beiträge entlang des Randrechtecks (mit ξ(s) = (1/2)s(s−1)π^{−s/2}Γ(s/2)ζ(s)). Der glatte Teil stammt aus der Stirling-Asymptotik von Γ:
```
N(T) = (T/2π) log(T/2π) − T/2π + 7/8 + S(T) + O(1/T)
```
mit dem **Argumentterm** S(T) = (1/π) arg ζ(1/2 + iT) (entlang horizontaler Linie stetig fortgesetzt). Bekannt ist S(T) = O(log T) unbedingt; unter RH sogar S(T) = O(log T / log log T).

### Mittlere Nullstellendichte
Differenzieren des Hauptterms ergibt die lokale Dichte der Imaginärteile:
```
dN/dT ≈ (1/2π) log(T/2π)
```
d. h. mittlerer Abstand benachbarter Nullstellen auf Höhe T ist ≈ 2π/log(T/2π) → 0. (Grundlage für die Normierung in der Paarkorrelation, Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]].)

### Herleitung der expliziten Formel (Perron + Residuen)
Ausgangspunkt: logarithmische Ableitung des Eulerprodukts,
```
−ζ'(s)/ζ(s) = Σ_{n=1}^∞ Λ(n) n^{−s},   Λ(n) = log p falls n = p^k, sonst 0.
```
Perron-Formel für ψ(x) = Σ_{n≤x} Λ(n):
```
ψ(x) = (1/2πi) ∫_{c−i∞}^{c+i∞} (−ζ'(s)/ζ(s)) x^s/s ds   (c > 1)
```
Verschiebt man die Kontur nach links und sammelt die **Residuen**, so trägt bei:
- Pol von ζ bei s = 1 (Residuum von −ζ'/ζ · x^s/s ist x) → Hauptterm **x**;
- jede nicht-triviale Nullstelle ρ (Pol von ζ'/ζ) → Term **−x^ρ/ρ**;
- Pol bei s = 0 → −log(2π);
- triviale Nullstellen s = −2n → +(1/2) log(1 − x^{−2}).
Ergebnis (von-Mangoldt):
```
ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − (1/2) log(1 − x^{−2})
```

### Warum RH ⟺ optimaler Fehlerterm
Schreibe ρ = β + iγ. Dann |x^ρ/ρ| = x^β/|ρ|. Die Summe über Nullstellen liefert
```
ψ(x) − x = − Σ_ρ x^ρ/ρ = O(x^{Θ} (log x)²),   Θ = sup_ρ β.
```
Unter RH ist Θ = 1/2, also ψ(x) = x + O(√x (log x)²), äquivalent zu **π(x) = Li(x) + O(√x log x)** (Koch 1901). Eine Nullstelle mit β > 1/2 würde den Exponenten Θ und damit den Fehler vergrößern. Somit:
```
RH  ⟺  ψ(x) − x = O(x^{1/2+ε})  ⟺  π(x) − Li(x) = O(x^{1/2+ε})
```

### Weils explizite Formel (allgemeine Form, Dualität Primzahlen ↔ Nullstellen)
Für eine geeignete Testfunktion g mit Fourier-Transformierter h:
```
Σ_ρ h(γ) = (1/2π)∫ h(r)[ψ-Term] dr − Σ_{n} Λ(n)/√n · g(log n) + (archimedischer Term)
```
Diese Identität ist der Angelpunkt der Spurformel-Ansätze (Connes, Dok. [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]]) und der Positivitätskriterien (Weil/Li, Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]).

## Quellen
- [Riemann–von Mangoldt formula — Wikipedia](https://en.wikipedia.org/wiki/Riemann%E2%80%93von_Mangoldt_formula)
- [The Explicit Formula in simple terms (arXiv math/9810169)](https://arxiv.org/pdf/math/9810169)
- [Sketch of the Riemann-von Mangoldt explicit formula — Reed College](https://people.reed.edu/~jerry/361/lectures/rvm.pdf)
- [On the error term in the explicit formula of Riemann–von Mangoldt (arXiv 2111.10001)](https://arxiv.org/pdf/2111.10001)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **nutzt** → [[01 Riemanns Originalarbeit (1859) und die Riemann-Siegel-Formel]] — *Explizite Formel baut auf Funktionalgleichung/ξ auf.*

### Eingehende Relationen

- **hat als Instanz** ← [[Explizite Formel (Primzahlen↔Nullstellen)]] — *Doc 02 stellt die explizite Formel dar.*
- **wird genutzt von** ← [[52 Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025]] — *Guinand-Weil-Testfunktionen kommen aus der expliziten Formel.*

### Belegte Aussagen (Claims)

- `[BEWIESEN]` [[claim-koch]] — RH ⟺ π(x)=Li(x)+O(√x·log x).

### Im Text erwähnt

- [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]]
- [[10 Alain Connes – Spurformel & nichtkommutative Geometrie]]
- [[12 Nullstellenfreie Regionen (klassischer analytischer Ansatz)]]
- [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]]
- [[17 Lindelöf-Hypothese & Dichte-Hypothese]]
- [[19 Selberg-Spurformel & Selberg-Zetafunktion (RH-Analogon BEWIESEN)]]
