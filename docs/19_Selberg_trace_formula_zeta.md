# Selberg-Spurformel & Selberg-Zetafunktion (RH-Analogon BEWIESEN)

**Kategorie:** Bewiesenes Analogon (spektral/geometrisch)
**Autor / Jahr:** Atle Selberg (1956)
**Typ:** Bewiesenes RH-Analogon + strukturelles Vorbild für Spurformeln
**Status:** ✅ RH-Analogon für Selberg-Zetafunktion bewiesen

## Zusammenfassung
Die **Selberg-Spurformel** (1956) verknüpft auf einer hyperbolischen Riemannschen Fläche die **Eigenwerte des Laplace-Operators** (spektrale Seite) mit den **Längen geschlossener Geodäten** (geometrische Seite). Die zugehörige **Selberg-Zetafunktion** erfüllt ein exaktes Analogon der Riemann-Vermutung — und dieses ist **bewiesen**. Sie ist das wichtigste *spektrale* Vorbild für das Hilbert–Pólya-Programm.

## Kernidee
- **Selberg-Zetafunktion:** ein Eulerprodukt-artiges Produkt, aber statt über Primzahlen läuft es über **primitive geschlossene Geodäten** der hyperbolischen Fläche (Bahnlängen ↔ "log p").
- Sie besitzt eine **Funktionalgleichung** und ein Eulerprodukt analog zu ζ.
- **Bewiesenes RH-Analogon:** Die nicht-trivialen Nullstellen der Selberg-Zetafunktion liegen auf einer kritischen Geraden — ihre Imaginärteile hängen mit den **Eigenwerten des Laplace-Operators** zusammen. Da der Laplace-Operator **selbstadjungiert** ist (reelle Eigenwerte!), liegen die Nullstellen *automatisch* richtig.

## Direkte Analogie zur klassischen RH
| Selberg-Welt (bewiesen) | Riemann-Welt (offen) |
|---|---|
| Geschlossene Geodäten | Primzahlen |
| Bahnlängen | log p |
| Eigenwerte des Laplace-Operators | Imaginärteile der ζ-Nullstellen |
| Selberg-Spurformel | Weils explizite Formel (Dok. 02) |
| Selbstadjungierter Laplace ⇒ RH-Analogon | gesuchter Hilbert–Pólya-Operator (Dok. 05) |

- **Genau hier liegt die Hoffnung des Hilbert–Pólya-Programms:** In der Selberg-Welt *existiert* der selbstadjungierte Operator (der Laplace-Operator) und liefert das RH-Analogon "geschenkt". Fände man das ζ-Analogon dieses Operators, wäre die klassische RH bewiesen.
- Connes formulierte explizit: Ein passendes Analogon der Selberg-Spurformel für die Wirkung der Idèleklassengruppe auf den Adèleklassenraum würde die RH implizieren (Dok. 10).

## Bedeutung / Einordnung
- Liefert ein *funktionierendes* Modell, in dem "Nullstellen = Eigenwerte eines selbstadjungierten Operators" Realität ist.
- Stärkt die Plausibilität des spektralen Ansatzes erheblich.
- **Einschränkung:** Die hyperbolische Geometrie ist *gegeben*; für ζ fehlt das entsprechende geometrische Objekt — der Operator ist nicht bekannt.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Setting
Sei Γ \ ℍ eine kompakte hyperbolische Fläche (Γ ⊂ PSL₂(ℝ) diskret, kokompakt), Δ der Laplace–Beltrami-Operator. Eigenwerte 0 = λ_0 < λ_1 ≤ λ_2 ≤ …, schreibe λ_n = 1/4 + r_n² (also r_n = √(λ_n − 1/4)).

### Selberg-Zetafunktion
Produkt über primitive geschlossene Geodäten γ₀ mit Länge ℓ(γ₀):
```
Z(s) = ∏_{γ₀ primitiv} ∏_{k=0}^∞ ( 1 − e^{−(s+k) ℓ(γ₀)} ),   Re(s) > 1.
```
(Längen ℓ(γ₀) ↔ log p; die geschlossenen Geodäten ↔ Primzahlen.)

### Funktionalgleichung & Nullstellen
Z(s) erfüllt eine Funktionalgleichung Z(s) = Z(1−s)·(explizit) und hat:
- „triviale" Nullstellen bei s = −k (k ≥ 0) und
- **nicht-triviale Nullstellen bei s = 1/2 ± i r_n** (aus den Laplace-Eigenwerten).

### Das bewiesene RH-Analogon
Da Δ **selbstadjungiert positiv** ist, sind die λ_n ≥ 0 reell. Für λ_n ≥ 1/4 ist r_n ∈ ℝ, also liegen die nicht-trivialen Nullstellen 1/2 ± i r_n **exakt auf Re(s) = 1/2**. (Endlich viele „kleine" Eigenwerte 0 ≤ λ_n < 1/4 geben Ausnahme-Nullstellen auf dem reellen Segment — das exakte Analogon möglicher Siegel-Nullstellen, Dok. 32.) ⇒ RH-Analogon bewiesen, weil der Operator selbstadjungiert ist.

### Selberg-Spurformel
Für eine geeignete Testfunktion h (gerade, holomorph im Streifen) mit Fourier-Transformierter g:
```
Σ_{n=0}^∞ h(r_n)  =  (Area/4π) ∫_{−∞}^∞ h(r) r tanh(π r) dr  +  Σ_{γ₀} Σ_{k=1}^∞  (ℓ(γ₀) g(k ℓ(γ₀))) / (2 sinh(k ℓ(γ₀)/2)).
```
- **Linke (spektrale) Seite:** Summe über Laplace-Eigenwerte ↔ in der Riemann-Welt Summe über Nullstellen γ.
- **Rechte (geometrische) Seite:** Identitätsterm (Fläche) + Summe über Geodäten-Längen ↔ in der Riemann-Welt Σ Λ(n)/√n g(log n).

### Wörterbuch zur expliziten Formel (Dok. 02)
| Selberg-Spurformel | Weils explizite Formel |
|---|---|
| Σ_n h(r_n) | Σ_ρ h(γ) |
| (Area/4π)∫ h(r) r tanh(πr) dr | archimedischer Γ'/Γ-Term |
| Σ_{γ₀,k} ℓ g(kℓ)/(2 sinh(kℓ/2)) | Σ_n Λ(n) n^{−1/2} g(log n) |

**Kernbotschaft:** In der Selberg-Welt *existiert* der selbstadjungierte Operator (Δ) und liefert das RH-Analogon umsonst. Das ist die Blaupause, die Connes (Dok. 10) und Deninger (Dok. 31) für ζ zu realisieren suchen.

## Quellen
- [Selberg trace formula — Wikipedia](https://en.wikipedia.org/wiki/Selberg_trace_formula)
- [The Selberg trace formula and the Riemann zeta function — Hejhal (Experts@Minnesota)](https://experts.umn.edu/en/publications/the-selberg-trace-formula-and-the-riemann-zeta-function)
- [Selberg trace formula and zeta functions — M. Watkins](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/physics4.htm)
- [Riemann hypothesis — Wikipedia (Selberg zeta)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
