# Nullstellenfreie Regionen (klassischer analytischer Ansatz)

**Kategorie:** Analytischer Ansatz
**Autoren / Jahre:** Hadamard & de la Vallée Poussin (1896/1899), Littlewood (1922), Vinogradov–Korobov (1958), moderne explizite Verfeinerungen (2020er)
**Typ:** Schrittweise Annäherung (keine volle RH)
**Status:** Aktiv; bestes asymptotisches Resultat seit Jahrzehnten Vinogradov–Korobov

## Zusammenfassung
Statt die RH direkt zu beweisen, verfolgt ein Jahrhundert analytischer Arbeit das Ziel, die **Region des kritischen Streifens, die nachweislich frei von Nullstellen ist**, schrittweise zu vergrößern — den Streifen also "von rechts" Richtung kritische Gerade einzuengen. Jede Verbesserung liefert effektivere Versionen des Primzahlsatzes mit Fehlertermen.

## Historische Entwicklung der nullstellenfreien Region
(σ = Re(s), Schranke nahe σ = 1)

| Jahr | Autor(en) | Nullstellenfreie Region |
|---|---|---|
| 1896 | Hadamard, de la Vallée Poussin | ζ(1 + it) ≠ 0 ⇒ erster Beweis des Primzahlsatzes |
| 1899 | de la Vallée Poussin | 1 − σ ≤ c / log t |
| 1922 | Littlewood | 1 − σ ≤ c · log log t / log t |
| 1938 | Chudakov | 1 − σ ≤ c / (log t)^{3/4 + ε} |
| 1958 | Vinogradov, Korobov | 1 − σ ≤ c / (log t)^{2/3} (log log t)^{1/3} |
| 2020er | diverse (explizit) | z. B. ζ(σ + it) ≠ 0 für t ≥ 3, σ ≥ 1 − 1/(4,896 · log t) |

## Kernidee
- **Globale Methode (Hadamard):** Nutze Nicht-Negativität trigonometrischer Polynome (klassisch: 3 + 4cos θ + cos 2θ ≥ 0) zusammen mit der Eulerprodukt-/log-Ableitungsstruktur, um Nullstellen nahe σ = 1 auszuschließen.
- **Lokale Methode (Landau):** lokale Abschätzungen von ζ.
- **Vinogradov–Korobov:** schärfere Abschätzungen von Exponentialsummen ⇒ größerer nullstellenfreier Bereich. Der Beweis ist erheblich aufwändiger, das Resultat aber nur geringfügig stärker als de la Vallée Poussins.

## Bedeutung / Einordnung
- Liefert *effektive, explizite* (wenn auch schwache) Versionen des Primzahlsatzes mit Fehlertermen — praktisch wichtig (z. B. für Berechnungen, kryptographisch relevante Primzahldichten).
- **Fundamentale Schwäche:** Eine nullstellenfreie Region, so klein sie auch sein mag, hält Nullstellen nur von σ = 1 fern — sie *fixiert* sie nicht auf σ = 1/2. Damit prinzipiell schwächer als die RH.
- Der Vinogradov–Korobov-Exponent (2/3) blieb ~70 Jahre der beste; jüngste Decoupling-basierte Arbeiten (vgl. Guth–Maynard, Dok. 22) beginnen, an Exponenten in verwandten Dichteabschätzungen zu rütteln.

## Quellen
- [Zero-free regions for the Riemann zeta function (arXiv 1910.08205)](https://arxiv.org/pdf/1910.08205)
- [Explicit bounds on ζ(s) in the critical strip and a zero-free region (arXiv 2301.03165)](https://arxiv.org/pdf/2301.03165)
- [Zero-free regions inspired by work of Heath-Brown (arXiv 2603.21490)](https://arxiv.org/html/2603.21490)
- [Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function (arXiv 1410.3926)](https://arxiv.org/pdf/1410.3926)
