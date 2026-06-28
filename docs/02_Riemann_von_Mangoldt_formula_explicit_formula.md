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
- Grundlage für nullstellenfreie Regionen (Dok. 12), Dichte-Hypothese (Dok. 17) und alle Spurformel-Ansätze (Connes, Selberg, Dok. 10/19), die die explizite Formel als "Spur" reinterpretieren.

## Quellen
- [Riemann–von Mangoldt formula — Wikipedia](https://en.wikipedia.org/wiki/Riemann%E2%80%93von_Mangoldt_formula)
- [The Explicit Formula in simple terms (arXiv math/9810169)](https://arxiv.org/pdf/math/9810169)
- [Sketch of the Riemann-von Mangoldt explicit formula — Reed College](https://people.reed.edu/~jerry/361/lectures/rvm.pdf)
- [On the error term in the explicit formula of Riemann–von Mangoldt (arXiv 2111.10001)](https://arxiv.org/pdf/2111.10001)
