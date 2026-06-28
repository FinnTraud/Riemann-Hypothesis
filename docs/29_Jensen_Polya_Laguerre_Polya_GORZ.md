# Jensen–Pólya-Programm: Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)

**Kategorie:** Aktiver Lösungsansatz (äquivalente Reformulierung + Fortschritt)
**Autoren / Jahre:** Pólya (1927), Jensen, Newman; Griffin, Ono, Rolen, Zagier (2019)
**Typ:** Zur RH äquivalentes Kriterium + neuer Fortschritt
**Status:** Äquivalenz bewiesen; GORZ bewiesen Hyperbolizität für Grad ≤ 8 und Dichte-1-Teilmenge; volle RH offen

## Zusammenfassung
Die RH ist **äquivalent** dazu, dass die Riemann-ξ-Funktion zur **Laguerre–Pólya-Klasse** gehört (ganze Funktionen mit *nur reellen* Nullstellen). Dies ist wiederum äquivalent zur **Hyperbolizität (Reellwurzeligkeit) aller Jensen-Polynome**, die aus den Taylor-Koeffizienten von ξ gebildet werden. Griffin, Ono, Rolen und Zagier (2019) erzielten hier substanziellen Fortschritt — einer der greifbarsten modernen "Teil-Lösungswege".

## Die Kette der Äquivalenzen
```
RH  ⟺  ξ ∈ Laguerre–Pólya-Klasse (nur reelle Nullstellen)
    ⟺  alle Jensen-Polynome J_d^{(n)}(ξ) sind hyperbolisch (nur reelle Wurzeln)
    ⟺  alle höheren Turán-/Laguerre-Ungleichungen für die (verschobenen) Taylor-Koeffizienten gelten
```
- **Jensen-Polynome:** Aus den Maclaurin-Koeffizienten einer Funktion bildet man für jeden Grad d und Verschiebung n ein Polynom J_d^{(n)}. "Hyperbolisch" = alle Wurzeln reell.
- **Turán-Ungleichungen:** konkrete (unendlich viele) polynomiale Ungleichungen an die Koeffizienten — eine sehr "explizite" Form der RH.

## Das Resultat von Griffin–Ono–Rolen–Zagier (2019, PNAS / arXiv 1902.07321)
- **Modellierung durch Hermite-Polynome:** Sie bewiesen einen allgemeinen Satz, wonach die Jensen-Polynome (geeignet skaliert) im Limes gegen **Hermite-Polynome** konvergieren — und Hermite-Polynome sind bekanntlich hyperbolisch.
- **Konkrete Resultate für ξ:**
  - Hyperbolizität für **alle Grade d ≤ 8** (zuvor nur d ≤ 3 bekannt).
  - Hyperbolizität für eine **Dichte-1-Teilmenge** der Jensen-Polynome jedes Grades (asymptotisch fast alle).
  - Erweiterung auf das Jensen–Pólya-Programm für allgemeine L-Funktionen (arXiv 1905.11269).
- Nebenresultat: präzise asymptotische Formel für die zentralen Ableitungen von ζ; Bezug zum SYK-Modell der Physik.

## Kritische Einordnung (wichtig!)
- Das Resultat beweist die RH **nicht**: Hyperbolizität "für alle d bis 8" und "für Dichte 1" ist weit von "für *alle* d und *alle* n" entfernt.
- Es gibt explizite Skepsis: Das Paper **"Jensen polynomials are not a plausible route to proving the Riemann Hypothesis"** (arXiv 2008.07206) argumentiert, dass dieser Weg an einer fundamentalen Hürde scheitert — die Hermite-Approximation kontrolliert gerade *nicht* die für die volle RH entscheidenden Regime.
- Dennoch: konkrete, prüfbare, aktiv beforschte Reformulierung mit echtem Fortschritt — relevant für die Wissensbasis.

## Verbindung zu anderen Dokumenten
- Eng verwandt mit der **de-Bruijn–Newman-Konstante** (Dok. 23): Λ ≤ 0 ⟺ ξ ∈ Laguerre–Pólya. Pólyas Untersuchung von Fourier-Transformierten positiver Funktionen ist die gemeinsame Wurzel.
- Positivitäts-/Reellwurzeligkeits-Leitmotiv wie bei Weil-Positivität (Dok. 14) und de Branges (Dok. 20).

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Laguerre–Pólya-Klasse (LP)
Eine ganze Funktion gehört zu LP, wenn sie lokal gleichmäßiger Limes reeller Polynome mit nur reellen Nullstellen ist. Charakterisierung (Hadamard-Produkt):
```
f(x) = c x^m e^{−a x² + b x} ∏_k (1 − x/x_k) e^{x/x_k},   a ≥ 0, b,c,x_k ∈ ℝ,  Σ 1/x_k² < ∞.
```
**Satz (Pólya).** RH ⟺ ξ(1/2 + iz) ∈ LP (als Funktion von z, nur reelle Nullstellen z = γ_n).

### Jensen-Polynome
Für eine reelle Folge (a(k)) (hier: Taylor-Koeffizienten, ξ(1/2+iz) = Σ a(k) z^{2k}/k! o. ä.) definiere
```
J^{d,n}(X) = Σ_{j=0}^d binom(d,j) a(n+j) X^j.
```
„Hyperbolisch" := nur reelle Wurzeln. **Satz:** f ∈ LP ⟺ alle J^{d,n} (d,n ≥ 0) sind hyperbolisch. Also:
```
RH  ⟺  J^{d,n} hyperbolisch für alle d, n  (für die ξ-Koeffizienten).
```

### Höhere Turán-Ungleichungen (äquivalente konkrete Form)
Hyperbolizität für kleine d entspricht expliziten Ungleichungen an die Koeffizienten:
```
d = 2 (Turán):     a(n)² − a(n−1) a(n+1) ≥ 0,
d = 3 (höhere T.):  4(a_n² − a_{n−1}a_{n+1})(a_{n+1}² − a_n a_{n+2}) − (a_n a_{n+1} − a_{n−1}a_{n+2})² ≥ 0,
```
und so weiter für jedes d — eine Folge immer komplexerer, aber elementarer Polynom-Ungleichungen, deren *Gesamtheit* die RH ist.

### GORZ-Hauptsatz (2019): Hermite-Limes
**Satz (Griffin–Ono–Rolen–Zagier).** Geeignet normiert (mit Verschiebung/Skalierung g(n), δ(n)) konvergieren die Jensen-Polynome gegen die **Hermite-Polynome** H_d:
```
lim_{n→∞}  ( δ(n)^{−d} J^{d,n}( δ(n) X − g(n) ) / a(n) )  =  H_d(X),
```
gleichmäßig auf Kompakta. Da die H_d nur reelle Wurzeln haben und diese „stabil" sind, folgt:
- **Hyperbolizität für jedes feste d und alle n ≥ N(d)** (also für eine Dichte-1-Teilmenge jeder Grades).
- Für ξ explizit verifiziert: **alle d ≤ 8** vollständig hyperbolisch.
Asymptotik der zentralen Ableitungen (Schlüssel-Lemma): a(n) bestimmt aus
```
a(n) ~ (Hauptterm via Sattelpunktmethode auf ∫ Φ(u) u^{2n} du), Φ wie in Dok. 23.
```

### Kritik (arXiv 2008.07206)
Die Hermite-Approximation kontrolliert nur das Regime n → ∞ bei **festem** d. Für die RH braucht man d und n *gemeinsam* groß (d ~ n). Genau dort versagt die Hermite-Kontrolle — daher „kein plausibler Weg zur vollen RH". Realistisch ist GORZ ein starkes Resultat über die *Verteilung* der Jensen-Wurzeln, nicht über alle simultan.

## Quellen
- [Jensen polynomials for the Riemann zeta function and other sequences — PNAS (Griffin, Ono, Rolen, Zagier)](https://www.pnas.org/doi/10.1073/pnas.1902572116)
- [Jensen polynomials for the Riemann zeta function and other sequences (arXiv 1902.07321)](https://arxiv.org/pdf/1902.07321)
- [The Jensen-Pólya program for various L-functions (arXiv 1905.11269)](https://arxiv.org/abs/1905.11269)
- [Jensen polynomials are not a plausible route to proving the Riemann Hypothesis (arXiv 2008.07206)](https://arxiv.org/pdf/2008.07206)
- [On a new class of Laguerre-Pólya type functions with applications in number theory (arXiv 2108.01827)](https://ar5iv.labs.arxiv.org/html/2108.01827)
