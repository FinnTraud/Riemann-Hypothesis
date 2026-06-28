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

## Quellen
- [Derivative Moments for Characteristic Polynomials from the CUE (Springer, Comm. Math. Phys.)](https://link.springer.com/article/10.1007/s00220-012-1512-1)
- [Moments of the Riemann Zeta Function and Log-Correlated Random Variables (Oxford)](https://ora.ox.ac.uk/objects/uuid:9bbc320c-9738-43ef-b0f0-f18bf4b7c0d6/files/dh415pb096)
- [On moments of the derivative of CUE characteristic polynomials and the Riemann zeta function (arXiv 2409.03687)](https://arxiv.org/html/2409.03687)
- [Freezing transition and moments of moments of the Riemann zeta function (Oxford QJM)](https://academic.oup.com/qjmath/article/75/4/1481/7925234)
