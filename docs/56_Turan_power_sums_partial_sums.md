---
id: doc-56
number: 56
title: "Turáns Potenzsummen-Programm & die Partialsummen von ζ (widerlegter Ansatz)"
category: failed-proof
status: refuted
tags: [turan, power-sums, partial-sums, montgomery-1983, dirichlet-polynomial, failed-approach]
source_file: 56_Turan_power_sums_partial_sums.md
lang: de
---

# Turáns Potenzsummen-Programm & die Partialsummen von ζ

**Kategorie:** Gescheiterter Ansatz mit erhaltenem Werkzeug
**Autoren / Jahre:** Paul Turán (1948, Potenzsummen-Methode); H. L. Montgomery (1983, Widerlegung der Turán-Bedingung)
**Typ:** Reduktion der RH auf Nullstellenfreiheit von Dirichlet-Partialsummen
**Status:** ❌ **Der RH-Weg ist widerlegt**; die Potenzsummen-Methode selbst bleibt ein produktives Werkzeug

## Zusammenfassung
Turán versuchte, die RH auf eine scheinbar viel einfachere Frage zurückzuführen: das Nullstellenverhalten der **endlichen Partialsummen**
```
ζ_N(s) = Σ_{n=1}^{N} n^{−s}.
```
Er bewies: Wären diese Partialsummen für alle großen N in der Halbebene Re(s) > 1 nullstellenfrei, so folgte die RH (bzw. eine quasi-RH-Nullstellenfreiheit). Montgomery zeigte 1983, dass genau das **falsch** ist: ζ_N hat für große N Nullstellen rechts von Re = 1. Der Ansatz ist damit endgültig tot — und ist eines der lehrreichsten Beispiele dafür, wie eine korrekte Implikation an einer falschen Prämisse scheitert.

## Mathematischer Kern

### Turáns Reduktion (1948)
Turán arbeitete mit **Potenzsummen**: für komplexe z_1,…,z_N und Koeffizienten b_j untersucht man
```
s_ν = Σ_{j=1}^{N} b_j z_j^ν  (ν = m+1, …, m+N),
```
und fragt, wie groß `max_ν |s_ν|` mindestens sein muss (Turáns erster und zweiter Hauptsatz). Angewandt auf `ζ_N(s) = Σ n^{−s}` mit z_j = j^{−1} liefert das untere Schranken für |ζ_N| und damit Nullstellenfreiheit — **falls** die Konfiguration günstig ist. Turáns Satz:
```
Wenn ζ_N(s) ≠ 0 für Re(s) > 1 und alle N ≥ N₀,
dann hat ζ(s) keine Nullstellen mit Re(s) > 1/2  (⇒ RH).
```
Die Brücke ist die klassische Approximation `ζ(s) = ζ_N(s) + N^{1−s}/(s−1) + O(N^{−σ})` im kritischen Streifen: die Partialsummen approximieren ζ, und ihre Nullstellen „wandern" beim Grenzübergang.

### Montgomerys Widerlegung (1983)
**Satz (Montgomery).** Für alle hinreichend großen N besitzt ζ_N(s) Nullstellen mit
```
Re(s)  >  1 + (4/π − 1 − o(1)) · (log log N)/(log N).
```
Insbesondere gibt es Nullstellen **rechts von Re = 1**, und die Turán-Bedingung ist für kein N₀ erfüllbar. Der Beweis benutzt, dass die Partialsumme sich in einem geeigneten Bereich wie ein zufälliges Dirichlet-Polynom verhält; das Maximum des reellen Anteils von Σ n^{−s} über einen langen t-Bereich erreicht (Resonanz-/Diophantische-Approximation-Argument) Werte, die eine Nullstelle in der genannten Halbebene erzwingen.

### Die eigentliche Lehre
Der Fehler liegt nicht in Turáns Implikation (die ist korrekt), sondern in der stillschweigenden Erwartung, ein **endliches Modell** (Dirichlet-Polynom) erbe die entscheidende Eigenschaft des unendlichen Objekts. Es erbt sie nicht:
- ζ_N hat **kein Euler-Produkt** (eine abgeschnittene Summe ist nicht multiplikativ) — dieselbe Wurzel wie bei Davenport–Heilbronn (Dok. 35).
- ζ_N erfüllt **keine Funktionalgleichung**.
- Die Nullstellen von ζ_N liegen asymptotisch auf einer ganz anderen Kurve als die von ζ (Verteilungssätze von Borwein–Fee–Ferguson–van der Waall; „zeros of partial sums" — sie füllen einen Streifen um Re = 1).

Das ist der Fehlermodus `F9 truncation-limit-gap` in Reinform (Dok. 68): *das abgeschnittene Objekt ist beweisbar, aber der Limes vererbt nichts.* Genau dieselbe Gefahr besteht heute beim abgeschnittenen Weil-Ansatz (Dok. 52) und bei Galerkin-Approximationen — dort ist die Konvergenz der ehrlich offene Schritt, und Turán ist die Warnung, dass diese Schritte scheitern können.

### Was vom Programm überlebt hat
Turáns **Potenzsummen-Methode** ist ein Standardwerkzeug geblieben:
- Nullstellendichte-Abschätzungen (Dok. 22/49) benutzen Turán-Typ-Ungleichungen für Dirichlet-Polynome;
- „Turán-Ungleichungen" in der Laguerre–Pólya-Theorie (Dok. 29) — **Achtung: gleicher Name, anderes Objekt** (dort: Ungleichungen für Jensen-Polynom-Koeffizienten, Griffin–Ono–Rolen–Zagier);
- die Methode liefert Ω-Resultate (Vorzeichenwechsel in Fehlertermen).

## Bedeutung / Einordnung
- **Kanonisches Beispiel** einer Reduktion, deren Prämisse widerlegt wurde — wichtiger Kalibrierungsfall für jeden Beweis-Bewerter: „Reduziert die Idee die RH auf eine Aussage, die man *unabhängig* prüfen kann? Dann prüfe sie zuerst numerisch/asymptotisch."
- **Testbar:** ζ_N-Nullstellen sind billig zu berechnen — ein reproduzierbares Experiment (Nullstellen von ζ_N für N = 10…2000 plotten) macht Montgomerys Satz sichtbar und ist ein guter Einstieg ins Experiment-Logbuch (Dok. 51).

## Quellen
- P. Turán, *On some approximative Dirichlet polynomials in the theory of the zeta-function*, Danske Vid. Selsk. Mat.-Fys. Medd. 24 (1948).
- H. L. Montgomery, *Zeros of approximations to the zeta function*, in: Studies in Pure Mathematics (To the Memory of Paul Turán), Birkhäuser 1983, 497–506.
- P. Turán, *On a New Method of Analysis and its Applications*, Wiley 1984.
- [Borwein–Fee–Ferguson–van der Waall, *Zeros of partial sums of the Riemann zeta function*](https://www.ams.org/journals/mcom/2007-76-259/S0025-5718-07-01950-3/)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_analytic|Analytische Ansätze]]

| Achse | Wert |
|---|---|
| Familie | analytic |
| Implikation | `conditional` |
| Euler-Produkt | `none` |
| Positivität | `n/a` |
| Strenge | `refuted` · Evidenz `n/a` |
| Testbar / formalisierbar | `high` / `medium` |

**Offener Kernschritt:** Prämisse widerlegt: Montgomery 1983 zeigt Nullstellen von zeta_N rechts von Re=1.

**Hebel (was er liefern würde):** Präzedenzfall dafür, dass Abschneide-Modelle NICHT vererben.

**Typische Fehlermodi:** [[F9_truncation-limit-gap|F9 Abgeschnittenes Modell bewiesen, Limes offen]] · [[F1_no-euler-product|F1 Euler-Produkt nicht wesentlich benutzt]]

**Vergleichbar mit:** [[09_Bender_Brody_Muller_2017_Hamiltonian|Bender–Brody–Müller (2017): PT-symmetrischer Hamiltonian für die Riemann-Nullstellen]] · [[20_de_Branges_Hilbert_spaces|Louis de Branges: Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)]] · [[23_de_Bruijn_Newman_constant_Polymath15|De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-56 doc-09 doc-20 doc-23`

**Ausgehende Beziehungen**
- *versucht Transfer von* (`attempts_transfer_of`) → [[concept_RH|Riemann-Vermutung (RH)]] — Reduktion der RH auf Nullstellenfreiheit der Partialsummen ζ_N.
- *widerlegt durch* (`refuted_by`) → [[35_obstructions_barriers|35 — Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN]] — Montgomery 1983: ζ_N hat Nullstellen rechts von Re=1 — Prämisse falsch.
- *ist Instanz von* (`instance_of`) → [[concept_truncation-limit|Abschneidung & Grenzübergang]] — Kanonischer Fall, in dem das abgeschnittene Modell NICHTS vererbt.
- *ist Obstruktion für* (`obstruction_for`) → [[52_Connes_truncated_Weil_spectral_realization|52 — Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)]] — Warnung für alle Galerkin-/Cutoff-Programme: der Limes kann scheitern.

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
