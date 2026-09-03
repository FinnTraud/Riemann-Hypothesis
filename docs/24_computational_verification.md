---
id: doc-24
number: 24
title: "Numerische Verifikation der Riemann-Vermutung"
category: numerical
status: reference
tags: [computation, odlyzko, platt, zetagrid, turing-method, verification]
source_file: 24_computational_verification.md
lang: de
---

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

## Mathematischer Kern (Formeln, Verfahren, Rechnungen)

### Riemann-Siegel-Formel (Auswertung auf der Geraden)
```
Z(t) = 2 Σ_{n=1}^{N} n^{−1/2} cos(θ(t) − t log n) + R(t),   N = ⌊√(t/2π)⌋,
θ(t) = (t/2) log(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760 t³) + …
R(t) = (−1)^{N−1} (2π/t)^{1/4} [ Ψ(p) + Korrekturen ],  p = √(t/2π) − N,  Ψ(p)=cos(2π(p²−p−1/16))/cos(2πp).
```
Aufwand O(√t) pro Auswertung (statt O(t)). Vorzeichenwechsel von Z lokalisieren Nullstellen.

### Turing-Methode (Vollständigkeitsnachweis)
Man zählt die gefundenen Vorzeichenwechsel von Z auf [0,T] und vergleicht mit
```
N(T) = θ(T)/π + 1 + S(T),   S(T) = (1/π) arg ζ(1/2 + iT).
```
Turing zeigte: ∫_{T}^{T'} S(t) dt ist klein und beschränkt, sodass aus
```
| (gefundene Anzahl) − θ(T)/π − 1 | < (Turing-Schranke)
```
folgt, dass *alle* Nullstellen bis T gefunden wurden — und alle auf der Geraden liegen. Wenn die gezählten Geraden-Nullstellen = N(T), ist RH bis Höhe T verifiziert.

### Gram-Punkte
Gram-Punkte g_n: θ(g_n) = nπ. „Gramsche Gesetzmäßigkeit": meist liegt genau eine Nullstelle zwischen aufeinanderfolgenden Gram-Punkten ((−1)^n Z(g_n) > 0). Ausnahmen (Gram-Punkt-Versagen) werden mit der Turing-Methode aufgefangen.

### Odlyzko–Schönhage-Algorithmus
Beschleunigt die *gleichzeitige* Auswertung von ζ(1/2 + it) an vielen Punkten t durch schnelle Mehrpunkt-Auswertung der Dirichlet-Summe (FFT-artige Bandbegrenzung / Taylor-Entwicklung von Σ n^{−it}). Amortisierte Kosten O(t^{1/2+o(1)}) für ~t^{1/2} nahe beieinanderliegende Werte ⇒ Massenberechnung sehr hoher Nullstellen.

### Rigorose Verifikation (Intervallarithmetik, Platt)
Statt Gleitkomma nutzt Platt **Intervallarithmetik** mit garantierten Fehlerschranken und eine rigorose Version der Turing-Methode. Verifiziert: RH gilt rigoros für alle Nullstellen mit 0 < Im < ~3,06·10^{10}. Grundlage u. a. für Helfgotts Beweis der ternären Goldbach-Vermutung.

### Status der Rechnungen
| Schranke | Methode |
|---|---|
| 10^{13} Nullstellen (Gourdon–Demichel 2004) | Odlyzko–Schönhage, Gleitkomma |
| ~9·10^{11} (ZetaGrid) | verteilt, van-de-Lune-Software |
| rigoros bis Höhe 3,06·10^{10} (Platt) | Intervallarithmetik |
Alle gefundenen Nullstellen: einfach und exakt auf Re(s) = 1/2.

## Quellen
- [Andrew Odlyzko: Papers & tables on Zeros of the Riemann Zeta Function](https://www-users.cse.umn.edu/~odlyzko/doc/zeta.html)
- [ZetaGrid — Wikipedia](https://en.wikipedia.org/wiki/ZetaGrid)
- [Wedeniwski/ZetaGrid — GitHub](https://github.com/Wedeniwski/ZetaGrid)
- [Computation of zeros of the Zeta function — X. Gourdon & P. Sebah](http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeroscompute.html)
- [Riemann Zeta Function Zeros — Wolfram MathWorld](https://mathworld.wolfram.com/RiemannZetaFunctionZeros.html)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Numerische Extrapolation** *(Tier 3)* — Aus endlicher Rechnung wird auf asymptotisches Verhalten geschlossen — die RH-Landschaft hat dafür berüchtigte Gegenbeispiele.
>   *Fluchtbedingung:* Nicht überwindbar, nur vermeidbar: Numerik darf Hypothesen erzeugen und widerlegen, aber nie stützen. Ein rigoroses Intervall-Zertifikat (doc-54) ist etwas anderes als eine Stichprobe.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (4)
> - *ist Evidenz für* → **Riemann-Vermutung (RH)** — Numerische Verifikation (>10^13 Nullstellen) — Evidenz, kein Beweis.
> - *ist Evidenz für* → [[52_Connes_truncated_Weil_spectral_realization|52 · Abgeschnittene Weil-Quadratform & Zeta-Spektraltrip…]] — Hochpraezise Nullstellendaten sind der Massstab fuer die Genauigkeitsangaben.
> - ← *wird benutzt von* [[54_machine_assisted_number_theory_ANTEDB_Lean|54 · Maschinengestützte Zahlentheorie]] — Rigorose Verifikationsstandards (Platt, Intervall-Zertifikate).
> - ← *wird benutzt von* [[60_counterexample_oracle|60 · Das Gegenbeispiel-Orakel]] — Benutzt Turings Nullstellenzaehlung als Verletzungsdetektor.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
