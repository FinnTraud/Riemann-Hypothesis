# Synthese: Querschnittsthemen & was ein erfolgreicher Beweis leisten muss

**Kategorie:** Meta / Synthese (Kern-Dokument für „bulletproof")
**Typ:** Querschnittsanalyse aller Ansätze
**Status:** Analytische Zusammenfassung

## Zweck
Dieses Dokument verdichtet die 40 Einzeldokumente zu **Mustern**: Was haben alle ernsthaften Ansätze gemeinsam? Welche notwendigen Bedingungen muss ein gültiger Beweis erfüllen? Es ist die strategische „Landkarte" für einen RH-Assistenten.

## 1. Drei wiederkehrende Leitmotive
Praktisch jeder ernsthafte Ansatz lässt sich einem (oder mehreren) dieser Motive zuordnen:

### (A) Positivität / Reellwurzeligkeit
RH als Aussage, dass eine **quadratische Form positiv** bzw. eine Funktion **nur reelle Nullstellen** hat.
- Weil-Positivität W(g⋆ḡ) ≥ 0 (Dok. 14) · Li-Koeffizienten λ_n ≥ 0 (Dok. 14) · de Branges (Dok. 20) · Laguerre–Pólya / Jensen (Dok. 29) · Lee–Yang/Newman (Dok. 33) · de-Bruijn–Newman Λ ≤ 0 (Dok. 23).
- **Gemeinsame Hürde:** Die Positivität wird auf RH *reduziert*, aber nicht *bewiesen* — und darf nicht zirkulär angenommen werden (Dok. 35, Punkt 3).

### (B) Spektrale Interpretation (Hilbert–Pólya)
Nullstellen = Eigenwerte eines selbstadjungierten / kanonischen Operators.
- Hilbert–Pólya (Dok. 05) · Berry–Keating (Dok. 08) · Bender–Brody–Müller (Dok. 09) · Connes-Spurformel (Dok. 10) · Prolate-Operator (Dok. 11) · Selberg (Dok. 19, bewiesenes Modell) · Deninger (Dok. 31) · Bost–Connes (Dok. 34).
- **Gemeinsame Hürde:** Der Operator muss *kanonisch aus der Arithmetik* stammen; ein erfundener Operator ist zirkulär (Dok. 35, Punkt 5).

### (C) Geometrie / Übertragung des Funktionenkörper-Falls
RH über 𝔽_q ist bewiesen (Weil/Deligne, Dok. 18) durch Geometrie + Positivität der Schnittform. Übertragung auf ℤ:
- 𝔽₁-Geometrie / arithmetic site (Dok. 30) · Deninger-Kohomologie (Dok. 31) · Connes-Adèle (Dok. 10).
- **Gemeinsame Hürde:** Die nötige Geometrie/Kohomologie über Spec(ℤ) existiert noch nicht.

## 2. Notwendige Bedingungen für JEDEN gültigen Beweis
Aus den Obstruktionen (Dok. 35) destilliert:

1. **Euler-Produkt wesentlich nutzen.** Davenport–Heilbronn (Dok. 35) zeigt: Funktionalgleichung + Fortsetzung + Wachstum reichen NICHT. Die Multiplikativität/Primzahlstruktur muss eingehen.
2. **Zwischen „mit/ohne Euler-Produkt" unterscheiden.** Das Argument darf nicht für die Davenport–Heilbronn-Funktion gelten.
3. **Positivität wirklich beweisen, nicht annehmen.** (Conrey–Li widerlegten de Branges' Annahme, Dok. 20.)
4. **Keine reine Numerik.** Mertens/Skewes (Dok. 35) zeigen: endliche Evidenz kann täuschen.
5. **Konvergenzfragen der Nullstellensumme respektieren.** Σ_ρ ist nur bedingt konvergent (Dok. 27).
6. **Paritätsbarriere umgehen.** Reine Siebmethoden reichen nicht (Dok. 35, Punkt 3).

## 3. Warum die drei Motive zusammenhängen
- Die **explizite Formel** (Dok. 02) ist der gemeinsame Kern: Sie verbindet Nullstellen (spektral) mit Primzahlen (Euler-Produkt) und wird in (B)/(C) als **Spurformel** gelesen, in (A) als **quadratische Form** (Weil-Positivität).
- Im bewiesenen Fall (Dok. 18, 19) fallen alle drei zusammen: Selberg-Spurformel (B) = explizite Formel, Schnitt-Positivität (A) = Weils Beweis, Geometrie (C) = die Kurve. **Das ist die Blaupause** — gesucht ist ihre Realisierung über ℤ.

## 4. Realistische Etappenziele (was Fortschritt wäre)
- Positiver Anteil → 50 %+ → 100 % auf der Geraden (Dok. 04) — aber Anteil-Methoden allein reichen nicht.
- Exponentenverbesserung in N(σ,T) (Guth–Maynard, Dok. 22) → Richtung Dichte-Hypothese (Dok. 17).
- Ausschluss von Landau–Siegel-Nullstellen (Dok. 32) für GRH.
- Λ ≤ 0 (de-Bruijn–Newman, Dok. 23) — aktuell 0 ≤ Λ ≤ 0,22.
- Kanonische Konstruktion des Hilbert–Pólya-Operators / der Weil-Positivität (Dok. 10, 31) — der „große" Weg.

## 5. Bewertungsraster für eine vorgeschlagene Beweisidee
| Frage | Falls problematisch → |
|---|---|
| Nutzt es das Euler-Produkt wesentlich? | Nein → wahrscheinlich falsch (Dok. 35) |
| Gilt es auch für Davenport–Heilbronn? | Ja → falsch |
| Positivität bewiesen oder angenommen? | Angenommen → zirkulär |
| Operator kanonisch aus Arithmetik? | Nein → zirkulär/leer |
| Nur endliche Numerik? | Ja → kein Beweis |
| In Lean verifizierbar? (Dok. 37) | Nein → mit Vorsicht behandeln |

## Quellen (Synthese aus)
- [The Riemann Hypothesis — E. Bombieri (Clay)](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
- [On some reasons for doubting the Riemann hypothesis — Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)
- [The Riemann Hypothesis over Finite Fields — J. Milne](https://www.jmilne.org/math/xnotes/pRH.html)
- [An essay on the Riemann Hypothesis — A. Connes (arXiv 1509.05576)](https://arxiv.org/pdf/1509.05576)
- (sowie die Dokumente 01–40 dieser Wissensbasis)
