# Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)

**Kategorie:** Spektraler Ansatz / statistische Evidenz
**Autoren / Jahr:** Hugh Montgomery (1973), Freeman Dyson (1972/73), Andrew Odlyzko (1980er, numerisch)
**Typ:** Statistische Vermutung & numerische Evidenz
**Status:** Vermutung (teils bedingt bewiesen unter RH); starke numerische Bestätigung

## Zusammenfassung
1973 berechnete Hugh Montgomery die **Paarkorrelation** der Imaginärteile der nicht-trivialen ζ-Nullstellen. In einem berühmten Gespräch am Institute for Advanced Study erkannte der Physiker Freeman Dyson diese Formel sofort als die Paarkorrelationsfunktion der Eigenwerte großer zufälliger hermitescher Matrizen aus dem **Gaussian Unitary Ensemble (GUE)**. Diese unerwartete Brücke zwischen Zahlentheorie und Quantenphysik gilt als eine der wichtigsten Stützen des Hilbert–Pólya-Programms.

## Kernidee / die Formel
- Montgomery zeigte (unter Annahme der RH) für die normierten Nullstellenabstände eine Paarkorrelationsfunktion der Form:

```
R₂(u) = 1 − (sin(πu)/(πu))² + δ(u)
```

- Genau diese Funktion beschreibt die Eigenwert-Paarkorrelation im GUE der Zufallsmatrixtheorie.
- Interpretation: Die Nullstellen "stoßen sich ab" (level repulsion) wie Energieniveaus eines quantenchaotischen Systems — sie sind *nicht* wie zufällige unabhängige Punkte (Poisson) verteilt.

## Numerische Bestätigung (Odlyzko)
- Andrew Odlyzko berechnete in den 1980er Jahren Millionen von Nullstellen in extrem großen Höhen (z. B. nahe der 10²⁰-ten Nullstelle) und verglich Abstandsstatistiken mit den GUE-Vorhersagen.
- Die Übereinstimmung ist verblüffend präzise — bekannt als **Montgomery–Odlyzko-Gesetz**. Sie erstreckt sich auf höhere Korrelationen und ganze Familien von L-Funktionen (Katz–Sarnak-Philosophie).

## Bedeutung / Einordnung
- Stärkste *statistische* Evidenz für die Existenz eines selbstadjungierten "Hilbert–Pólya-Operators" mit chaotischer Dynamik (GUE-Universalitätsklasse).
- Inspirierte die quantenchaotischen Modelle (Berry–Keating, Dok. 08) und die Momentvermutungen (Keating–Snaith, Dok. 07).
- **Wichtige Einschränkung:** Statistische Mimikry ist *kein Beweis* der RH — sie zeigt nur, dass die Nullstellen sich *verhalten*, als kämen sie von einem solchen Operator; der Operator selbst fehlt.

## Quellen
- [Montgomery's pair correlation conjecture — Wikipedia](https://en.wikipedia.org/wiki/Montgomery's_pair_correlation_conjecture)
- [Montgomery's Pair Correlation Conjecture — Wolfram MathWorld](https://mathworld.wolfram.com/MontgomerysPairCorrelationConjecture.html)
- [Pair Correlation Conjecture for the Zeros of the Riemann Zeta-function I (arXiv 2503.15449)](https://arxiv.org/abs/2503.15449)
- [Correlations of eigenvalues and Riemann zeros (arXiv 0803.2795)](https://arxiv.org/pdf/0803.2795)
- [Andrew Odlyzko: Papers on Zeros of the Riemann Zeta Function](https://www-users.cse.umn.edu/~odlyzko/doc/zeta.html)
