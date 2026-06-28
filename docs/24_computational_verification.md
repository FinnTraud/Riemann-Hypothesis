# Numerische Verifikation der Riemann-Vermutung

**Kategorie:** Numerische Evidenz
**Autoren / Jahre:** Turing (1953), Lehmer (1956), van de Lune–te Riele–Winter (1986), Odlyzko (1980er–2001), Wedeniwski/ZetaGrid (2001–2005), Gourdon–Demichel (2004), Platt (rigoros, 2010er)
**Typ:** Computerverifikation (Evidenz, kein Beweis)
**Status:** RH für die ersten >10^13 Nullstellen bestätigt; kein Gegenbeispiel gefunden

## Zusammenfassung
Seit den ersten Handrechnungen (Riemann, Gram, Backlund, Hutchinson) wurde die RH numerisch für immer mehr Nullstellen verifiziert. Alle bislang berechneten nicht-trivialen Nullstellen liegen **exakt auf** der kritischen Geraden Re(s) = 1/2. Das ist starke Evidenz — aber **kein Beweis** (es könnte ein Gegenbeispiel jenseits der Rechengrenze geben, vgl. die widerlegte Mertens-Vermutung, Dok. 16).

## Methodik (Kurzüberblick)
- **Hardysche Z-Funktion** (Dok. 03): reellwertig, |Z(t)| = |ζ(1/2+it)|. Vorzeichenwechsel von Z(t) ⇒ Nullstelle auf der Geraden.
- **Riemann-Siegel-Formel** (Dok. 01): effiziente Auswertung von ζ auf der Geraden.
- **Gram-Punkte / Turing-Methode:** Zählen, ob *alle* erwarteten Nullstellen bis zur Höhe T gefunden wurden (Abgleich mit der Riemann–von-Mangoldt-Formel N(T), Dok. 02). Stimmt die Anzahl der auf der Geraden gefundenen Nullstellen mit N(T) überein, liegen *alle* Nullstellen bis T auf der Geraden.
- **Odlyzko–Schönhage-Algorithmus:** schnelle Mehrfachauswertung von ζ → Berechnung sehr vieler/sehr hoher Nullstellen.

## Meilensteine
| Jahr | Wer | Umfang |
|---|---|---|
| 1903 | Gram | erste ~15 Nullstellen |
| 1953 | Turing | Computer + Turing-Methode |
| 1986 | van de Lune, te Riele, Winter | erste 1,5 · 10^9 Nullstellen |
| 1980er–2001 | Odlyzko | Statistik nahe 10^20-ter / 10^22-ter Nullstelle (Test der GUE-Korrelationen, Dok. 06) |
| 2001–2005 | Wedeniwski, **ZetaGrid** | verteiltes Rechnen (>10.000 Rechner, >70 Länder), erste ~9 · 10^11 Nullstellen; >1 Mrd. Nullstellen/Tag |
| 2004 | Gourdon & Demichel | erste **10^13** Nullstellen (Odlyzko–Schönhage) |

## Rigorose Verifikation (Platt)
- Viele frühe Verifikationen verwendeten nicht-rigorose Gleitkomma-Arithmetik. **David Platt** entwickelte Verfahren mit **Intervallarithmetik** (rigorose Fehlerschranken) und verifizierte die RH **rigoros** bis zu einer Höhe von etwa H = 3,06 · 10^10 — d. h. mathematisch zertifiziert, nicht nur numerisch plausibel. Diese rigorosen Schranken sind Grundlage für bedingte/unbedingte zahlentheoretische Resultate (z. B. ternäre Goldbach-Vermutung, Helfgott).

## Bedeutung / Einordnung
- Massive Evidenz *für* die RH: kein einziges Gegenbeispiel unter >10^13 Nullstellen.
- **Prinzipielle Grenze:** Numerik kann die RH niemals beweisen (unendlich viele Nullstellen). Die Mertens-Vermutung mahnt: bei ~10^30 hätte numerische Evidenz in die Irre geführt.
- Wichtig für die kritische Einordnung datengetriebener / KI-gestützter "Bestätigungen" der RH (Dok. 28).

## Quellen
- [Andrew Odlyzko: Papers & tables on Zeros of the Riemann Zeta Function](https://www-users.cse.umn.edu/~odlyzko/doc/zeta.html)
- [ZetaGrid — Wikipedia](https://en.wikipedia.org/wiki/ZetaGrid)
- [Wedeniwski/ZetaGrid — GitHub](https://github.com/Wedeniwski/ZetaGrid)
- [Computation of zeros of the Zeta function — X. Gourdon & P. Sebah](http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeroscompute.html)
- [Riemann Zeta Function Zeros — Wolfram MathWorld](https://mathworld.wolfram.com/RiemannZetaFunctionZeros.html)
