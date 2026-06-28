# Michael Atiyah (2018): gescheiterter Beweisversuch (Todd-Funktion)

**Kategorie:** Gescheiterter / umstrittener Beweis
**Autor / Jahr:** Sir Michael Atiyah, September 2018 (Heidelberg Laureate Forum)
**Typ:** Öffentlich präsentierte Beweisbehauptung
**Status:** ❌ Von der Fachwelt nicht akzeptiert; als fehlerhaft/unvollständig betrachtet

## Zusammenfassung
Sir Michael Atiyah (Fields-Medaille 1966, Abel-Preis 2004 — einer der bedeutendsten Mathematiker des 20. Jahrhunderts) kündigte im September 2018 einen "einfachen Beweis" der Riemann-Vermutung an und präsentierte ihn in einem 45-minütigen Vortrag am Heidelberg Laureate Forum. Der Beweis stützte sich auf eine angebliche neue Beschreibung der **Feinstrukturkonstante α** (aus der Physik) mittels einer "Todd-Funktion". Die mathematische Gemeinschaft reagierte mit deutlicher **Skepsis**; der Beweis gilt als nicht akzeptiert.

## Die behauptete Idee
- Atiyah führte eine **"Todd-Funktion" T** ein (benannt nach seinem Lehrer J. A. Todd), die er als Limes bestimmter analytischer Funktionen konstruiert haben wollte.
- **Beweis durch Widerspruch:** Angenommen, es gäbe eine Nullstelle abseits der kritischen Geraden. Über die Eigenschaften der Todd-Funktion (die er als "schwach analytisch", polynomial auf bestimmten Bereichen beschrieb) sollte ein Widerspruch entstehen.
- Als "Korollar" sollte sich nebenbei auch ein geschlossener Ausdruck für die Feinstrukturkonstante α ≈ 1/137 ergeben.

## Warum der Beweis scheiterte
- **Unveröffentlichte Grundlage:** Die zentrale Arbeit über die Todd-Funktion war nicht publiziert/begutachtet; der RH-Beweis sollte "leicht" daraus folgen — diese Grundlage existierte aber nicht in nachprüfbarer Form.
- **Mathematische Probleme:** Eine schwach-analytische Funktion, die auf einem 2D-Bereich polynomial ist und sich so verhält wie verlangt, müsste konstant sein — der Kernschritt ist nicht haltbar. Die Verbindung zur Feinstrukturkonstante (einer *gemessenen, dimensionslosen physikalischen* Größe) galt als mathematisch unbegründet.
- **Kontext:** Atiyah war zu diesem Zeitpunkt 89 Jahre alt und hatte in den Jahren zuvor mehrere fehlerhafte Behauptungen aufgestellt; Kollegen äußerten Skepsis bereits vor dem Vortrag.

## Bedeutung / Einordnung
- Hochprofiliertes Beispiel dafür, dass **Reputation einen Beweis nicht ersetzt** — die Community prüft die Mathematik, nicht den Namen.
- Wurde respektvoll, aber klar zurückgewiesen; Atiyah verstarb im Januar 2019.
- Lehre für KI-Kontext: Auch menschliche Genies produzieren falsche "Durchbrüche"; strenge Verifikation ist unverzichtbar (vgl. Dok. 27, 28).

## Mathematischer Kern (behauptete Konstruktion & der Fehler)

### Die behauptete Todd-Funktion T
Atiyah definierte (in Anlehnung an die von-Neumann-Hyperfinite-Faktor-Theorie) eine Funktion T als Limes von Polynomen, die er „schwach analytisch" nannte:
```
T = lim_{n→∞} T_n,   wobei T_n iterierte Exponential-/Polynomkonstruktionen sind,
T(1) = 1,   T  „polynomial auf jedem konvexen Bereich".
```
T sollte additiv/„kompatibel" mit der Hirzebruch-Todd-Klasse sein.

### Der behauptete Beweis durch Widerspruch
Definiere die Funktion (Atiyahs Notation) für eine angebliche Nullstelle b = 1/2 + iβ_0 außerhalb der Geraden:
```
F(s) = T( 1 + ζ(s) )  − 1   (schematisch),
```
und betrachte F auf einem Kreis um die kritische Stelle. Atiyah behauptete: aus der „schwachen Analytizität" von T folge, dass F auf einem 2-dimensionalen Bereich polynomial sei, dort aber zugleich verschwinden müsse ⇒ F ≡ 0 ⇒ Widerspruch zur Annahme der Off-Line-Nullstelle.

### Warum es falsch ist (präzise)
- **Verletzung des Identitätssatzes/Liouville:** Eine Funktion, die auf einem 2-dimensionalen (offenen) Bereich „polynomial" *und* beschränkt ist und sich wie verlangt verhält, müsste **konstant** sein (Liouville). Atiyahs T kann daher nicht gleichzeitig nicht-konstant *und* die geforderten Limes-/Analytizitätseigenschaften haben — der Kernschritt kollabiert.
- **Feinstrukturkonstante α:** Atiyah behauptete als „Korollar" eine geschlossene Formel α^{−1} = π · (ein Ausdruck in T). α ≈ 137,035999 ist eine *empirisch gemessene, dimensionslose physikalische* Größe ohne bekannten Grund, eine geschlossene mathematische Form zu besitzen — die Behauptung gilt als unbegründet.
- **Unveröffentlichte Grundlage:** Der Satz über T (woraus RH „leicht" folgen sollte) war nie in nachprüfbarer, begutachteter Form vorhanden.

### Einordnung
Strukturell ein Positivitäts-/Reellwurzeligkeits-Ansatz wie viele (Dok. 14, 20), aber der entscheidende analytische Schritt ist nicht haltbar. Lehre: Auch ein Fields-Medaillen-Träger ersetzt keinen prüfbaren Beweis.

## Quellen
- [Skepticism surrounds renowned mathematician's attempted proof — Science/AAAS](https://www.science.org/content/article/skepticism-surrounds-renowned-mathematician-s-attempted-proof-160-year-old-hypothesis)
- [Riemann hypothesis, the fine structure constant, and the Todd function — John D. Cook](https://www.johndcook.com/blog/2018/09/24/riemann-hypothesis-the-fine-structure-constant-and-the-todd-function/)
- [Atiyah's RH lecture preprint (mirror, El País)](https://ep00.epimg.net/descargables/2018/09/25/b133e2bf9a3e7bb55f5fae26dcf9b8c0.pdf)
- [Riemann hypothesis, fine structure constant, Todd function — Hacker News discussion](https://news.ycombinator.com/item?id=18059880)
