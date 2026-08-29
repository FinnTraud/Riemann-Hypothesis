---
id: doc-52
title: "Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025–2026)"
nummer: "52"
kategorie: Spektrale Ansätze
status: OFFEN
typ: dokument
aliases:
  - "doc-52"
  - "Dok. 52"
tags:
  - "dokument"
  - "kategorie/spectral"
  - "status/open"
  - "thema/2025"
  - "thema/2026"
  - "thema/active"
  - "thema/caratheodory-fejer"
  - "thema/connes"
  - "thema/consani"
  - "thema/galerkin"
  - "thema/hilbert-polya"
  - "thema/moscovici"
  - "thema/spectral-triple"
  - "thema/toeplitz"
  - "thema/truncation"
  - "thema/van-suijlekom"
  - "thema/weil-positivity"
quelle: docs/52_Connes_truncated_Weil_spectral_realization.md
---

> [!info] Navigation
> **Karte:** [[MOC O – Aktuelle Front 2025–2026 (Recherche-Update August 2026)]] · **Kategorie:** Spektrale Ansätze · **Status:** `OFFEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/52_Connes_truncated_Weil_spectral_realization.md`

# Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (2025–2026)

**Kategorie:** Spektraler Ansatz / Hilbert–Pólya-Programm (aktive Front)
**Autoren / Jahre:** Connes–van Suijlekom (2025); Connes–Consani–Moscovici (2025); Connes (2026);
Suzuki (2026); Folge-Numerik: Groskin u. a. (2026)
**Typ:** Neues, konkret rechenbares Programm zur *spektralen Realisierung* der Nullstellen
**Status:** **[OFFEN]** — kein RH-Beweis. Ein Teilschritt ist bewiesen, der entscheidende
Konvergenzschritt ist offen (siehe „Die Lücke").

## Zusammenfassung
Seit Ende 2025 gibt es die konkreteste Version des Hilbert–Pólya-Traums (Dok. [[05 Die Hilbert–Pólya-Vermutung (spektraler Ansatz)|05]], [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]], [[11 Connes–Moscovici – Prolate-Spheroidal-Operator und Zeta (2021–2022)|11]]) seit
Jahrzehnten. Statt *einen* Operator zu suchen, dessen Spektrum die Nullstellen sind, wird die
**Weilsche Quadratform** (Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]) auf einen *endlichen* Ausschnitt eingeschränkt — abgeschnitten
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
(Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]], `concept-positivity`) erzwingt also die Lage der Nullstellen — genau das Muster, das
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
überwältigende Numerik in die Irre führte (Mertens-Vermutung, Skewes-Zahl; Dok. [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)|16]], [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]], [[39 Cramér-Modell & probabilistische Heuristiken der Primzahlen|39]]).
**Der offene Punkt ist genau die Vertauschung von Limes und Nullstellenlage.**

## Einordnung / Warum das den bekannten Obstruktionen standhält
Ein Ansatz, der die RH beweisen *könnte*, muss die Obstruktionen aus Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]], [[43 Epstein-Zetafunktionen & Selberg-Klassen-Rigidität – Welche Eigenschaft erzwingt die kritische Gerade|43]], [[46 Voronin-Universalität (Meta-Obstruktion gegen 'weiche' Beweise)|46]] überleben:

- **Euler-Produkt wird wirklich benutzt** (Primzahlen `p ≤ x` gehen explizit in die Konstruktion
  ein). Damit greift die Davenport–Heilbronn-/Epstein-Warnung (Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]], [[43 Epstein-Zetafunktionen & Selberg-Klassen-Rigidität – Welche Eigenschaft erzwingt die kritische Gerade|43]]) *nicht*: die Methode
  ist nicht „weich genug", um auch für Dirichlet-Reihen ohne Euler-Produkt zu funktionieren.
- **Positivität statt Gleichungslösung** — der Mechanismus ist Weil-Positivität (Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]),
  nicht eine explizite Formel für die Nullstellen; das ist mit Voronin-Universalität (Dok. [[46 Voronin-Universalität (Meta-Obstruktion gegen 'weiche' Beweise)|46]])
  verträglich.
- **Endlich-dimensional und reproduzierbar** — jeder Schritt ist als Galerkin-Matrix nachrechenbar;
  vgl. das Experiment-Logbuch in `kb/experiment.py` und Dok. [[51 Kollaborations-Leitfaden – sinnvoll mit einer Fachperson an der RH arbeiten|51]].

Das macht es zum derzeit *ernsthaftesten* spektralen Programm — und zugleich zu dem, an dem sich
die Anti-Crackpot-Prüfung (`evaluate_proof_idea`) gut kalibrieren lässt: Es scheitert an keiner
Tier-1-Obstruktion, hat aber eine klar benennbare offene Stelle.

## Anschlüsse in dieser Wissensbasis
- Dok. [[05 Die Hilbert–Pólya-Vermutung (spektraler Ansatz)|05]] (Hilbert–Pólya), 10 (Connes NCG), 11 (Connes–Moscovici, prolate spheroidal)
- Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]] (Li-Kriterium & Weil-Positivität) — die Quadratform selbst
- Dok. [[02 Riemann–von-Mangoldt-Formel und die explizite Formel|02]] (explizite Formel) — Guinand–Weil-Testfunktionen
- Dok. [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site|30]] (𝔽₁, arithmetic site), 34 (Bost–Connes) — Connes' weiterer Programmrahmen
- Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]], [[43 Epstein-Zetafunktionen & Selberg-Klassen-Rigidität – Welche Eigenschaft erzwingt die kritische Gerade|43]], [[46 Voronin-Universalität (Meta-Obstruktion gegen 'weiche' Beweise)|46]] (Obstruktionen) — was der Ansatz überleben muss
- Dok. [[24 Numerische Verifikation der Riemann-Vermutung|24]] (numerische Verifikation) — Vergleichsmaßstab für die Genauigkeitsangaben

## Quellen
- [Connes, van Suijlekom — *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* (arXiv:2511.23257)](https://arxiv.org/abs/2511.23257)
- [Connes, Consani, Moscovici — *Zeta Spectral Triples* (arXiv:2511.22755)](https://arxiv.org/abs/2511.22755)
- [Connes — *The Riemann Hypothesis: Past, Present and a Letter Through Time* (arXiv:2602.04022)](https://arxiv.org/abs/2602.04022)
- [*High-Precision Approximation of Riemann Zeros via the Truncated Weil Form* (arXiv:2605.20224)](https://arxiv.org/abs/2605.20224)
- [Groskin — *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form* (arXiv:2607.02828)](https://arxiv.org/abs/2607.02828)
- [Suzuki — *Weil's quadratic form via the screw function* (arXiv:2606.09096)](https://arxiv.org/abs/2606.09096)
- [*A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator* (arXiv:2607.24830)](https://arxiv.org/abs/2607.24830)
- [Connes — Publikationsseite](https://alainconnes.org/publications/)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Blaupause für** → [[Riemann-Vermutung (RH)]] — *Programm fuer einen RH-Beweis; es fehlt der Konvergenzschritt Cutoff -> unendlich.*
- **ist Evidenz für** → [[Kritische Gerade Re(s)=1∕2]] — *Nullstellen des Grundzustands liegen fuer jeden endlichen Cutoff auf Re(s)=1/2.*
- **modelliert** → [[Hilbert–Pólya ∕ spektrale Interpretation]] — *Endlich-dimensionale, rechenbare Realisierung des Hilbert-Polya-Programms.*
- **nutzt** → [[02 Riemann–von-Mangoldt-Formel und die explizite Formel]] — *Guinand-Weil-Testfunktionen kommen aus der expliziten Formel.*
- **nutzt** → [[10 Alain Connes – Spurformel & nichtkommutative Geometrie]] — *Rahmen der nichtkommutativen Geometrie von Connes.*
- **nutzt** → [[11 Connes–Moscovici – Prolate-Spheroidal-Operator und Zeta (2021–2022)]] — *Setzt die Connes-Moscovici-Linie (prolate spheroidal, Skalierungsoperator) fort.*
- **nutzt** → [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]] — *Baut direkt auf Weil-Positivitaet / der Weilschen Quadratform auf.*
- **nutzt** → [[Euler-Produkt (Multiplikativität)]] — *Nur Euler-Faktoren p <= x gehen in die Konstruktion ein - der arithmetische Input.*
- **nutzt** → [[Positivität ∕ Reellwurzeligkeit]] — *Positivitaet (Caratheodory-Fejer / PSD-Toeplitz) erzwingt die Nullstellenlage.*

### Eingehende Relationen

- **hat als Instanz** ← [[Abgeschnittene Weil-Quadratform (Galerkin-Truncation)]] — *Dok. 52 stellt die abgeschnittene Weil-Quadratform dar.*
- **hat als Obstruktion** ← [[43 Epstein-Zetafunktionen & Selberg-Klassen-Rigidität – Welche Eigenschaft erzwingt die kritische Gerade]] — *Epstein/Selberg-Rigiditaet verlangt echten Euler-Produkt-Input - Dok. 52 liefert ihn, besteht die Pruefung also.*
- **hat als Obstruktion** ← [[46 Voronin-Universalität (Meta-Obstruktion gegen 'weiche' Beweise)]] — *Voronin-Universalitaet schliesst 'weiche' Argumente aus; Dok. 52 arbeitet ueber Positivitaet, nicht ueber Nullstellenformeln.*
- **wird genutzt von** ← [[Formale Verifikation ∕ maschinengestuetzte Mathematik]] — *Die Weil-Form-Numerik wird mit Reproduzierbarkeitspaketen und Intervall-Zertifikaten geliefert.*
- **wird gestützt durch** ← [[24 Numerische Verifikation der Riemann-Vermutung]] — *Hochpraezise Nullstellendaten sind der Massstab fuer die Genauigkeitsangaben.*

### Belegte Aussagen (Claims)

- `[BEWIESEN]` [[claim-cvs-groundstate]] — Definiert eine Quadratform mit Schwartz-Kern auf L^2([-L/2,L/2]) einen nach unten beschraenkten selbstadjungierten Operator, dessen kleinster Spektralwert ein einfacher, isolierter Eigenwert mit gerader Eigenfunktion xi ist, so liegen alle Nullstellen der Fourier-Transformierten xi^ auf der reellen Achse (entspricht Re(s)=1/2).
- `[BEWIESEN]` [[claim-caratheodory-fejer]] — Ist T eine hermitesche, positiv semidefinite Toeplitz-Matrix in M_n(C) vom Rang n-1 und xi in ker T, so hat P(z) = sum_j xi_j z^j alle Nullstellen auf dem Einheitskreis.
- `[OFFEN]` [[claim-truncated-weil-convergence]] — Die Nullstellen der Grundzustaende der abgeschnittenen Weil-Quadratform konvergieren fuer Cutoff c -> unendlich gegen die nicht-trivialen Nullstellen von zeta. (Zusammen mit claim-cvs-groundstate wuerde dies die RH liefern.)
- `[BEWIESEN]` [[claim-ccm-numerics]] — Die Spektren der Zeta-Spektraltripel bzw. der abgeschnittenen Weil-Form approximieren die untersten Nullstellen von zeta(1/2+is); mit Primzahlen p<13 werden Fehler um 2.6e-55 erreicht, ueber 15 Cutoffs faellt der Fehler der ersten Nullstelle monoton auf ca. 1.5e-168.

### Im Text erwähnt

- [[05 Die Hilbert–Pólya-Vermutung (spektraler Ansatz)]]
- [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]]
- [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
- [[39 Cramér-Modell & probabilistische Heuristiken der Primzahlen]]
- [[51 Kollaborations-Leitfaden – sinnvoll mit einer Fachperson an der RH arbeiten]]
