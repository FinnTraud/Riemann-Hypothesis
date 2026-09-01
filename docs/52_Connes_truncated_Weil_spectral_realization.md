---
id: doc-52
number: 52
title: "Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)"
category: spectral
status: open
tags: [connes, van-suijlekom, consani, moscovici, weil-positivity, spectral-triple, toeplitz, caratheodory-fejer, galerkin, truncation, hilbert-polya, 2025, 2026, active]
source_file: 52_Connes_truncated_Weil_spectral_realization.md
lang: de
---

# Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (2025–2026)

**Kategorie:** Spektraler Ansatz / Hilbert–Pólya-Programm (aktive Front)
**Autoren / Jahre:** Connes–van Suijlekom (2025); Connes–Consani–Moscovici (2025); Connes (2026);
Suzuki (2026); Folge-Numerik: Groskin u. a. (2026)
**Typ:** Neues, konkret rechenbares Programm zur *spektralen Realisierung* der Nullstellen
**Status:** **[OFFEN]** — kein RH-Beweis. Ein Teilschritt ist bewiesen, der entscheidende
Konvergenzschritt ist offen (siehe „Die Lücke").

## Zusammenfassung
Seit Ende 2025 gibt es die konkreteste Version des Hilbert–Pólya-Traums (Dok. 05, 10, 11) seit
Jahrzehnten. Statt *einen* Operator zu suchen, dessen Spektrum die Nullstellen sind, wird die
**Weilsche Quadratform** (Dok. 14) auf einen *endlichen* Ausschnitt eingeschränkt — abgeschnitten
sowohl im Ort (Intervall `[-L/2, L/2]` bzw. Skalierungsintervall `[λ⁻¹, λ]`) als auch in der
Arithmetik (nur Euler-Faktoren über Primzahlen `p ≤ x`). Das ergibt eine **endliche
Galerkin-Matrix**, deren Grundzustand man numerisch ausrechnen kann.

Zwei Befunde machen das bemerkenswert:

1. **Bewiesen:** Die Nullstellen der Fourier-Transformierten des Grundzustands liegen *exakt*
   auf der kritischen Geraden — für jeden endlichen Abschnitt, ohne RH anzunehmen.
2. **Numerisch:** Diese Nullstellen approximieren die echten ζ-Nullstellen mit teils
   *absurder* Genauigkeit — mit Primzahlen `p < 13` bereits Fehler um `2.6 × 10⁻⁵⁵`.

## Mathematischer Kern

### 1) Connes–van Suijlekom: Reelle Nullstellen aus Grundzuständen (arXiv:2511.23257)
Sei `Q` eine Quadratform mit Schwartz-Kern, die auf `L²([-L/2, L/2])` einen nach unten
beschränkten selbstadjungierten Operator definiert. **Satz.** Ist der kleinste Spektralwert `λ`
ein *einfacher, isolierter* Eigenwert mit *gerader* Eigenfunktion `ξ`, so liegen **alle**
Nullstellen der ganzen Funktion
```
ξ̂(z) = ∫ ξ(u) e^{i z u} du        (Fourier-Transformierte des Grundzustands)
```
auf der **reellen Achse**. Über die Mellin-/Fourier-Normierung entspricht „reell in `z`" genau
„`Re(s) = 1/2`" in der `s`-Ebene.

Beweiswerkzeug ist eine C\*-algebraische Fassung eines Korollars zum Struktursatz von
**Carathéodory–Fejér (1911)** für Toeplitz-Matrizen:

> Ist `T ∈ M_n(ℂ)` hermitesch, positiv semidefinit, Toeplitz und vom Rang `n − 1`, und ist
> `ξ ∈ ker T`, so hat das Polynom `P(z) = Σ_j ξ_j z^j` **alle** Nullstellen auf dem Einheitskreis.

Der Einheitskreis ist hier das diskrete Gegenstück zur kritischen Geraden. Positivität
(Dok. 14, `concept-positivity`) erzwingt also die Lage der Nullstellen — genau das Muster, das
ein RH-Beweis braucht.

### 2) Connes–Consani–Moscovici: Zeta-Spektraltripel (arXiv:2511.22755)
Konstruiert werden selbstadjungierte Operatoren als **Rang-1-Störungen** des Spektraltripels
zum Skalierungsoperator auf `[λ⁻¹, λ]`. Die Konstruktion benutzt *ausschließlich* Euler-Produkte
über die Primzahlen
```
p ≤ x = λ² .
```
Ergebnis: Die Spektren stimmen mit **verblüffender numerischer Genauigkeit** mit den untersten
nicht-trivialen Nullstellen von `ζ(1/2 + i s)` überein — schon für *kleine* `x`. Theoretische
Grundlage sind „Spectral triples and zeta cycles" (Connes 2021) plus die obige Erweiterung von
Carathéodory–Fejér, die die Selbstadjungiertheit garantiert.

### 3) Connes 2026: „Brief an Riemann" (arXiv:2602.04022)
Ein als Übersichtsartikel bestellter Text über 165 Jahre RH — mit einem **originalen Beitrag**
im Anhang: einem „Brief an Riemann", der *nur* Mathematik benutzt, die 1859 verfügbar war.
Die Methode ist Riemanns eigenem Zugang zum Riemannschen Abbildungssatz nachempfunden: man
**extremiert eine Quadratform** (in moderner Sprache: die Einschränkung der Weilschen
Quadratform) und erhält daraus Näherungen an die Nullstellen von ζ.

- Mit Primzahlen `p < 13` werden die **ersten 50 Nullstellen** approximiert.
- Genauigkeiten reichen von `~10⁻³` bis hinunter zu `2.6 × 10⁻⁵⁵`.
- **Bewiesen** wird zusätzlich generell, dass die Näherungswerte *exakt* auf der kritischen
  Geraden liegen.

Connes' eigene Wertung: Eine Übereinstimmung dieser Größenordnung „lässt sich nicht als Zufall
abtun". Sie ist trotzdem **kein Beweis** (siehe unten).

### 4) Folgearbeiten: Numerik, Zertifikate, Vereinheitlichung
- **arXiv:2605.20224** — „High-Precision Approximation of Riemann Zeros via the Truncated Weil
  Form". Erste öffentliche Implementierung der CvS-Galerkin-Matrix bei 16 Cutoffs (`c = 13 … 67`
  plus `c = 100`). Bei `N = 100` fällt der Fehler der ersten Nullstelle **monoton** von
  `≈ 2×10⁻⁵⁵` auf `≈ 1.5×10⁻¹⁶⁸` — 113 Größenordnungen über fünfzehn Cutoffs.
- **arXiv:2607.02828** (Groskin) — „A finite Guinand–Weil dictionary and archimedean tail order".
  (a) Jeder reelle gerade Galerkin-Koeffizientenvektor bestimmt eine **bandbeschränkte
  Guinand–Weil-Testfunktion**, für die die abgeschnittene Form *exakte* Summen über die
  nicht-trivialen Nullstellen liefert. (b) Jenseits des Galerkin-Bandes ist der weggelassene
  **archimedische Rest** ein total positives Cauchy–Stieltjes-Inkrement — daraus folgt eine
  zweiseitige Zertifizierungsregel mit explizitem Fehlerbudget, die *endliche* Positivität an
  *cutoff-freie* Positivität koppelt. Verifiziert über die ersten 512 Nullstellen auf drei
  unabhängigen Rechenwegen, mit vollständigem Reproduzierbarkeitspaket.
- **arXiv:2606.09096** (Suzuki) — „Weil's quadratic form via the screw function". Vereinheitlicht
  Yoshida (1992), Bombieri (2001, 2003), Connes–Consani (2023) und CCM (2025+) über die
  *Schraubenfunktion* (Suzuki 2023); Vorteil: die distributionell definierte Weil-Form wird durch
  *stetige* Funktionen behandelbar. Formuliert die Vermutung, ein selbstadjungierter Operator mit
  den `γ` als Eigenwerten entstehe als Limes `a → ∞` nichtlokaler Realisierungen des Operators
  erster Ordnung auf `[-a, a]` — alles **ohne** RH-Annahme.
- **arXiv:2607.24830** — numerische Realisierung des Suzuki-Operators, archimedisches Spektralgesetz,
  Operatorform des Weilschen Positivitätskriteriums.

## Die Lücke (warum das kein RH-Beweis ist)
Sauber getrennt:

| | Aussage | Status |
|---|---|---|
| (A) | Für jeden endlichen Cutoff `c` liegen die Nullstellen des Grundzustands auf der kritischen Geraden | **[BEWIESEN]** (CvS 2025) |
| (B) | Diese Nullstellen konvergieren für `c → ∞` gegen die Nullstellen von ζ | **[OFFEN]** |
| (C) | ⇒ RH | folgt aus (A) + (B), aber (B) fehlt |

Die numerische Evidenz für (B) ist außergewöhnlich stark (113 Größenordnungen monotoner
Fehlerabnahme), aber Evidenz ist kein Beweis — und die Wissensbasis kennt genug Fälle, in denen
überwältigende Numerik in die Irre führte (Mertens-Vermutung, Skewes-Zahl; Dok. 16, 35, 39).
**Der offene Punkt ist genau die Vertauschung von Limes und Nullstellenlage.**

## Einordnung / Warum das den bekannten Obstruktionen standhält
Ein Ansatz, der die RH beweisen *könnte*, muss die Obstruktionen aus Dok. 35, 43, 46 überleben:

- **Euler-Produkt wird wirklich benutzt** (Primzahlen `p ≤ x` gehen explizit in die Konstruktion
  ein). Damit greift die Davenport–Heilbronn-/Epstein-Warnung (Dok. 35, 43) *nicht*: die Methode
  ist nicht „weich genug", um auch für Dirichlet-Reihen ohne Euler-Produkt zu funktionieren.
- **Positivität statt Gleichungslösung** — der Mechanismus ist Weil-Positivität (Dok. 14),
  nicht eine explizite Formel für die Nullstellen; das ist mit Voronin-Universalität (Dok. 46)
  verträglich.
- **Endlich-dimensional und reproduzierbar** — jeder Schritt ist als Galerkin-Matrix nachrechenbar;
  vgl. das Experiment-Logbuch in `kb/experiment.py` und Dok. 51.

Das macht es zum derzeit *ernsthaftesten* spektralen Programm — und zugleich zu dem, an dem sich
die Anti-Crackpot-Prüfung (`evaluate_proof_idea`) gut kalibrieren lässt: Es scheitert an keiner
Tier-1-Obstruktion, hat aber eine klar benennbare offene Stelle.

## Anschlüsse in dieser Wissensbasis
- Dok. 05 (Hilbert–Pólya), 10 (Connes NCG), 11 (Connes–Moscovici, prolate spheroidal)
- Dok. 14 (Li-Kriterium & Weil-Positivität) — die Quadratform selbst
- Dok. 02 (explizite Formel) — Guinand–Weil-Testfunktionen
- Dok. 30 (𝔽₁, arithmetic site), 34 (Bost–Connes) — Connes' weiterer Programmrahmen
- Dok. 35, 43, 46 (Obstruktionen) — was der Ansatz überleben muss
- Dok. 24 (numerische Verifikation) — Vergleichsmaßstab für die Genauigkeitsangaben

## Quellen
- [Connes, van Suijlekom — *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* (arXiv:2511.23257)](https://arxiv.org/abs/2511.23257)
- [Connes, Consani, Moscovici — *Zeta Spectral Triples* (arXiv:2511.22755)](https://arxiv.org/abs/2511.22755)
- [Connes — *The Riemann Hypothesis: Past, Present and a Letter Through Time* (arXiv:2602.04022)](https://arxiv.org/abs/2602.04022)
- [*High-Precision Approximation of Riemann Zeros via the Truncated Weil Form* (arXiv:2605.20224)](https://arxiv.org/abs/2605.20224)
- [Groskin — *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form* (arXiv:2607.02828)](https://arxiv.org/abs/2607.02828)
- [Suzuki — *Weil's quadratic form via the screw function* (arXiv:2606.09096)](https://arxiv.org/abs/2606.09096)
- [*A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator* (arXiv:2607.24830)](https://arxiv.org/abs/2607.24830)
- [Connes — Publikationsseite](https://alainconnes.org/publications/)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_spectral|Spektrale Ansätze]]

| Achse | Wert |
|---|---|
| Familie | spectral |
| Implikation | `conditional` |
| Euler-Produkt | `essential` |
| Positivität | `must-prove` |
| Strenge | `theorem` · Evidenz `strong` |
| Testbar / formalisierbar | `high` / `medium` |

**Offener Kernschritt:** Gleichmäßiger Grenzübergang Cutoff -> unendlich (Turáns Partialsummen sind die Warnung).

**Hebel (was er liefern würde):** Pro Cutoff beweisbare Nullstellenlage + endliche Matrizen = numerisch angreifbar.

**Typische Fehlermodi:** [[F9_truncation-limit-gap|F9 Abgeschnittenes Modell bewiesen, Limes offen]] · [[F2_positivity-assumed|F2 Positivität angenommen statt bewiesen]]

**Vergleichbar mit:** [[23_de_Bruijn_Newman_constant_Polymath15|De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15]] · [[10_Connes_noncommutative_geometry|Alain Connes: Spurformel & nichtkommutative Geometrie]] · [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-52 doc-23 doc-10 doc-14`

**Ausgehende Beziehungen**
- *modelliert* (`models`) → [[concept_hilbert-polya|Hilbert–Pólya / spektrale Interpretation]] — Endlich-dimensionale, rechenbare Realisierung des Hilbert-Polya-Programms.
- *benutzt* (`uses`) → [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|14 — Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]] — Baut direkt auf Weil-Positivitaet / der Weilschen Quadratform auf.
- *benutzt* (`uses`) → [[02_Riemann_von_Mangoldt_formula_explicit_formula|02 — Riemann–von-Mangoldt-Formel und die explizite Formel]] — Guinand-Weil-Testfunktionen kommen aus der expliziten Formel.
- *benutzt* (`uses`) → [[11_Connes_Moscovici_prolate_spheroidal|11 — Connes–Moscovici: Prolate-Spheroidal-Operator und Zeta (2021–2022)]] — Setzt die Connes-Moscovici-Linie (prolate spheroidal, Skalierungsoperator) fort.
- *benutzt* (`uses`) → [[10_Connes_noncommutative_geometry|10 — Alain Connes: Spurformel & nichtkommutative Geometrie]] — Rahmen der nichtkommutativen Geometrie von Connes.
- *benutzt* (`uses`) → [[concept_positivity|Positivität / Reellwurzeligkeit]] — Positivitaet (Caratheodory-Fejer / PSD-Toeplitz) erzwingt die Nullstellenlage.
- *benutzt* (`uses`) → [[concept_euler-product|Euler-Produkt (Multiplikativität)]] — Nur Euler-Faktoren p <= x gehen in die Konstruktion ein - der arithmetische Input.
- *ist Evidenz für* (`evidence_for`) → [[concept_critical-line|Kritische Gerade Re(s)=1/2]] — Nullstellen des Grundzustands liegen fuer jeden endlichen Cutoff auf Re(s)=1/2.
- *ist Blaupause für* (`blueprint_for`) → [[concept_RH|Riemann-Vermutung (RH)]] — Programm fuer einen RH-Beweis; es fehlt der Konvergenzschritt Cutoff -> unendlich.

**Eingehende Beziehungen**
- *ist Instanz von* (`instance_of`) → [[concept_truncated-weil|Abgeschnittene Weil-Quadratform (Galerkin-Truncation)]] — Dok. 52 stellt die abgeschnittene Weil-Quadratform dar.
- *ist Obstruktion für* (`obstruction_for`) → [[43_Epstein_zeta_Selberg_class_rigidity|43 — Epstein-Zetafunktionen & Selberg-Klassen-Rigidität: Welche Eigenschaft erzwingt die kritische Gerade?]] — Epstein/Selberg-Rigiditaet verlangt echten Euler-Produkt-Input - Dok. 52 liefert ihn, besteht die Pruefung also.
- *ist Obstruktion für* (`obstruction_for`) → [[46_Voronin_universality|46 — Voronin-Universalität (Meta-Obstruktion gegen „weiche' Beweise)]] — Voronin-Universalitaet schliesst 'weiche' Argumente aus; Dok. 52 arbeitet ueber Positivitaet, nicht ueber Nullstellenformeln.
- *ist Evidenz für* (`evidence_for`) → [[24_computational_verification|24 — Numerische Verifikation der Riemann-Vermutung]] — Hochpraezise Nullstellendaten sind der Massstab fuer die Genauigkeitsangaben.
- *benutzt* (`uses`) → [[concept_formal-verification|Formale Verifikation / maschinengestuetzte Mathematik]] — Die Weil-Form-Numerik wird mit Reproduzierbarkeitspaketen und Intervall-Zertifikaten geliefert.
- *ist Obstruktion für* (`obstruction_for`) → [[56_Turan_power_sums_partial_sums|56 — Turáns Potenzsummen-Programm & die Partialsummen von ζ (widerlegter Ansatz)]] — Warnung für alle Galerkin-/Cutoff-Programme: der Limes kann scheitern.

**Thematisch benachbart (gemeinsame Tags):** [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)]] · [[54_machine_assisted_number_theory_ANTEDB_Lean|Maschinengestützte Zahlentheorie: ANTEDB, systematische Exponenten-Optimierung und formalisierter Primzahlsatz (2025–2026)]] · [[10_Connes_noncommutative_geometry|Alain Connes: Spurformel & nichtkommutative Geometrie]] · [[60_standard_conjectures_motives_positivity|Grothendiecks Standardvermutungen & Motive: die Herkunft der Positivität]] · [[49_live_analytic_frontier|Live-Front der analytischen Zahlentheorie (2019–2026)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
