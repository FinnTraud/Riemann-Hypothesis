# Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)

**Kategorie:** Äquivalentes Kriterium (Möbius-/Summatorik)
**Autoren / Jahre:** Riesz (1916); Mertens-Zusammenhang klassisch; Mertens-Vermutung widerlegt von Odlyzko & te Riele (1985)
**Typ:** Zur RH äquivalente Aussagen + lehrreiches Gegenbeispiel
**Status:** Äquivalenzen bewiesen; stärkere Mertens-Vermutung WIDERLEGT

## Zusammenfassung
Mehrere Kriterien drücken die RH über die **Möbius-Funktion** μ(n) und ihre Summatorik aus. Besonders lehrreich ist die **widerlegte Mertens-Vermutung**: Sie hätte die RH impliziert, ist aber falsch — eine Warnung vor zu starken hinreichenden Bedingungen.

## Mertens-Funktion-Kriterium
- Sei M(x) = Σ_{n≤x} μ(n) die summatorische Möbius-(Mertens-)Funktion.
- **RH-äquivalent:** Für jedes ε > 0 gilt M(x) / x^{1/2 + ε} → 0 für x → ∞. (D. h. M(x) = O(x^{1/2+ε}).)
- Das spiegelt 1/ζ(s) = Σ μ(n)/n^s wider: Die Wachstumsordnung von M(x) ist direkt an die Lage der Nullstellen gekoppelt.

## Die widerlegte Mertens-Vermutung (wichtige Lehre)
- **Mertens-Vermutung:** |M(n)| < √n für alle n. Wäre sie wahr, würde daraus die RH folgen (sie ist *stärker* als RH).
- **Widerlegung:** Andrew Odlyzko und Herman te Riele bewiesen 1985, dass die Mertens-Vermutung **falsch** ist (limsup M(x)/√x > 1, liminf < −1) — ohne ein explizites Gegenbeispiel n anzugeben (das kleinste bekannte Gegenbeispiel liegt extrem hoch, jenseits 10^16, vermutlich um 10^{30}+).
- **Lehre:** Eine plausible, numerisch lange gestützte "Verstärkung" der RH kann falsch sein. Numerische Evidenz bis zu großen Schranken beweist nichts — relevant auch für die kritische Einordnung von KI-/Datengetriebenen RH-"Bestätigungen" (vgl. Dok. 28).

## Riesz-Kriterium (1916)
- Marcel Riesz gab ein zur RH äquivalentes Kriterium über das Wachstum einer mit der Möbius-Funktion gebildeten unendlichen Reihe (Riesz-Funktion). Verwandt sind das **Hardy–Littlewood-Kriterium** und neuere **Riesz-Typ-Kriterien für die Selberg-Klasse** (Dok. 21).

## Bedeutung / Einordnung
- Verknüpft die RH mit der "Zufälligkeit" der Vorzeichen von μ(n) (multiplikative Struktur der ganzen Zahlen).
- Die widerlegte Mertens-Vermutung ist eines der wichtigsten **mahnenden Gegenbeispiele** in der RH-Geschichte.

## Quellen
- [Criteria equivalent to the Riemann Hypothesis (arXiv 0808.0640)](https://arxiv.org/pdf/0808.0640)
- [Riemann's Hypothesis and the Mertens Function (Galetto)](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/galetto_RH_Mertens.pdf)
- [Riemann hypothesis — Wikipedia (Mertens function)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
- [Riesz type criteria for L-functions in the Selberg class (arXiv 2211.02954)](https://arxiv.org/pdf/2211.02954)
