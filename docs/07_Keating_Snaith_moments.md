# Keating–Snaith: Momente der Zetafunktion via charakteristische Polynome (CUE)

**Kategorie:** Spektraler Ansatz / Random-Matrix-Theorie
**Autoren / Jahr:** Jonathan Keating, Nina Snaith (2000)
**Typ:** Vermutung (Modellierung), durch RMT gestützt
**Status:** Vermutung; in Spezialfällen bewiesen, allgemein offen

## Zusammenfassung
Keating und Snaith schlugen 2000 vor, die Riemannsche Zetafunktion auf der kritischen Geraden durch das **charakteristische Polynom einer zufälligen unitären Matrix** (Circular Unitary Ensemble, CUE) zu modellieren. Dieses Modell liefert präzise Vorhersagen für die **Momente** von ζ(1/2 + it) — ein langjähriges offenes Problem der analytischen Zahlentheorie, bei dem das Random-Matrix-Modell die richtigen Konstanten "errät".

## Kernidee
- Auf der kritischen Geraden verhält sich ζ(1/2 + it) statistisch wie das charakteristische Polynom Z(U, θ) einer Haar-zufälligen unitären N×N-Matrix U, wobei die Matrixgröße N ≈ log(T/2π) der lokalen Nullstellendichte entspricht.
- Für das CUE lassen sich Momente exakt berechnen (Produktformeln mit Gamma-/Barnes-G-Funktionen). Übertragen auf ζ ergibt sich die **Keating–Snaith-Vermutung** für die 2k-ten Momente:

```
(1/T) ∫₀ᵀ |ζ(1/2 + it)|^{2k} dt  ~  a_k · g_k · (log T)^{k²}
```

- Dabei ist (log T)^{k²} der von der RMT vorhergesagte Wachstumsexponent, g_k eine aus dem Barnes-G-Funktions-Limit stammende "Random-Matrix-Konstante", und a_k ein rein zahlentheoretischer arithmetischer Faktor (Eulerprodukt).

## Status der Beweise
- k = 1 (Hardy–Littlewood) und k = 2 (Ingham) klassisch bewiesen.
- Die volle Momentvermutung für allgemeine k ist **offen**; Random-Matrix-Theorie liefert aber die mutmaßlich korrekten Konstanten, die mit unabhängigen zahlentheoretischen Heuristiken (Conrey–Ghosh, Conrey–Gonek) übereinstimmen.
- Erweiterungen: Momente von Ableitungen ζ′, gemeinsame Momente, "moments of moments", log-korrelierte Felder, Fyodorov–Hiary–Keating-Vermutung über das Maximum von ζ in kurzen Intervallen.

## Bedeutung / Einordnung
- Macht die Zeta–GUE-Korrespondenz *quantitativ* und *vorhersagekräftig* (nicht nur Paarkorrelation wie bei Montgomery, Dok. 06).
- Liefert tiefe strukturelle Evidenz für einen spektralen/Random-Matrix-Ursprung der Nullstellen.
- Trägt indirekt zur RH bei (Momentschranken ↔ Anteil der Nullstellen auf der Geraden, Dok. 04), ist aber selbst kein Beweisweg zur vollen RH.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### CUE-Seite: charakteristisches Polynom
Für U ∈ U(N) Haar-verteilt sei Λ_U(θ) = det(I − U e^{−iθ}) = ∏_{n=1}^N (1 − e^{i(θ_n − θ)}). Keating–Snaith berechnen die Momente exakt:
```
E_{U(N)} |Λ_U(θ)|^{2k} = ∏_{j=1}^N  Γ(j) Γ(j + 2k) / Γ(j + k)²
```
Großes N (Barnes-G-Funktion G):
```
E |Λ|^{2k} ~ (G(1+k)² / G(1+2k)) · N^{k²}   (N → ∞)
```

### Übersetzung in die Zeta-Momente (Vermutung)
Identifiziere N ↔ log(T/2π) (gleiche lokale Dichte). Keating–Snaith-Vermutung für die 2k-ten Momente auf der kritischen Geraden:
```
(1/T) ∫_0^T |ζ(1/2 + it)|^{2k} dt  ~  a_k · g_k · (log T)^{k²}
```
mit
```
g_k = G(1+k)² / G(1+2k)         (Random-Matrix-Faktor, aus CUE)
a_k = ∏_p [ (1 − 1/p)^{k²} Σ_{m≥0} (Γ(m+k)/(m! Γ(k)))² p^{−m} ]   (arithmetischer Faktor, Eulerprodukt)
```

### Bekannte Spezialfälle (bewiesen)
```
k = 1:  (1/T)∫|ζ(1/2+it)|² dt ~ log T           (g_1 = 1, a_1 = 1; Hardy–Littlewood)
k = 2:  (1/T)∫|ζ(1/2+it)|⁴ dt ~ (1/2π²)(log T)⁴  (g_2 = 1/12, a_2 = 6/π²; Ingham)
```
Die Werte g_1 = 1, g_2 = 1/12 reproduzieren exakt G(2)²/G(3) bzw. G(3)²/G(5) — Bestätigung des RMT-Modells.

### Erweiterungen
- Ableitungsmomente: E|Λ'_U|² etc. ↔ Momente von ζ' (Hughes, Conrey–Ghosh–Gonek).
- **Fyodorov–Hiary–Keating-Vermutung** für das Maximum in kurzen Intervallen:
```
max_{|h| ≤ 1} log|ζ(1/2 + i(t+h))| = log log T − (3/4) log log log T + O(1)
```
(log-korreliertes Feld, Branching-Random-Walk-Analogie).

### Bezug zur RH
Momentschranken ⇒ untere Schranken für N₀(T)/N(T) (Anteil auf der Geraden, Dok. 04); k = 0-Verhalten ↔ Wertverteilung. Selbst die volle Momentvermutung impliziert die RH nicht, ist aber Teil desselben spektralen Bildes.

## Quellen
- [Derivative Moments for Characteristic Polynomials from the CUE (Springer, Comm. Math. Phys.)](https://link.springer.com/article/10.1007/s00220-012-1512-1)
- [Moments of the Riemann Zeta Function and Log-Correlated Random Variables (Oxford)](https://ora.ox.ac.uk/objects/uuid:9bbc320c-9738-43ef-b0f0-f18bf4b7c0d6/files/dh415pb096)
- [On moments of the derivative of CUE characteristic polynomials and the Riemann zeta function (arXiv 2409.03687)](https://arxiv.org/html/2409.03687)
- [Freezing transition and moments of moments of the Riemann zeta function (Oxford QJM)](https://academic.oup.com/qjmath/article/75/4/1481/7925234)
