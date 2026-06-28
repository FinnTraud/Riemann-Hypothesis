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

## Quellen
- [Jensen polynomials for the Riemann zeta function and other sequences — PNAS (Griffin, Ono, Rolen, Zagier)](https://www.pnas.org/doi/10.1073/pnas.1902572116)
- [Jensen polynomials for the Riemann zeta function and other sequences (arXiv 1902.07321)](https://arxiv.org/pdf/1902.07321)
- [The Jensen-Pólya program for various L-functions (arXiv 1905.11269)](https://arxiv.org/abs/1905.11269)
- [Jensen polynomials are not a plausible route to proving the Riemann Hypothesis (arXiv 2008.07206)](https://arxiv.org/pdf/2008.07206)
- [On a new class of Laguerre-Pólya type functions with applications in number theory (arXiv 2108.01827)](https://ar5iv.labs.arxiv.org/html/2108.01827)
