---
id: doc-13
number: 13
title: "Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung"
category: criterion
status: open
tags: [nyman-beurling, baez-duarte, density, hilbert-space]
source_file: 13_Nyman_Beurling_Baez_Duarte.md
lang: de
---

# Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung

**Kategorie:** Äquivalentes Kriterium (funktionalanalytisch)
**Autoren / Jahre:** Arne Beurling & Bertil Nyman (1950–1955), Luis Báez-Duarte (2003)
**Typ:** Zur RH äquivalente Umformulierung
**Status:** Äquivalenz bewiesen; die geforderte Dichte ist unbewiesen

## Zusammenfassung
Das Nyman–Beurling-Kriterium formuliert die RH als ein **Approximations-/Dichteproblem in einem Hilbertraum**: Die RH gilt genau dann, wenn ein bestimmter Funktionenraum dicht in L²(0,1) liegt. Báez-Duarte vereinfachte dies 2003 erheblich, indem er zeigte, dass nur **ganzzahlige** Dilatationen benötigt werden.

## Das Kriterium
- Betrachte den Raum der quadratintegrierbaren Funktionen auf (0,∞) bzw. L²(0,1).
- **Nyman–Beurling (1955):** Die RH ist äquivalent dazu, dass sich die charakteristische Funktion des Intervalls (0,1] im quadratischen Mittel durch Linearkombinationen der **Dilatationen der Bruchteilfunktion** {θ/x} (θ ∈ (0,1)) approximieren lässt — d. h. dieser Funktionenraum ist dicht.
- Anders gesagt: RH ⟺ ein bestimmter Vektor liegt im Abschluss der linearen Hülle abzählbar vieler anderer Vektoren ("zyklischer Vektor").

## Báez-Duartes Verschärfung (2003)
- Es genügt, die Dilatationen auf **positive ganze Zahlen** a = 1, 2, 3, … zu beschränken (statt aller reellen θ).
- Damit wird die RH äquivalent zur Approximierbarkeit von χ_{(0,1]} durch Linearkombinationen der {1/(a·x)} mit a ∈ ℕ — eine deutliche Reduktion der Komplexität.
- Es existieren **probabilistische Verallgemeinerungen** (zufällige Dilatationsfaktoren), die neue Kriterien liefern und teils mit dem starken Báez-Duarte-Kriterium überlappen.

## Bedeutung / Einordnung
- Übersetzt die RH vollständig in die Sprache der **Funktionalanalysis / Approximationstheorie / Operatortheorie** (Dichte, zyklische Vektoren).
- Numerisch: Partialsummen der Approximation konvergieren, aber **extrem langsam** — kein praktischer Beweisweg, und die nötige Dichte ist bis heute unbewiesen.
- Verwandt mit dem Hilbertraum-Zugang von de Branges (Dok. 20) und der Weil-Positivität (Dok. 14).

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Die Funktionen und der Raum
Sei {x} = x − ⌊x⌋ der Bruchteil, ρ(x) = {1/x} für x ∈ (0,1). Für θ ∈ (0,1) definiere die Dilatation
```
f_θ(x) = { θ/x } = ρ_θ(x),   x ∈ (0,1).
```
Sei 𝒩 = abgeschlossene lineare Hülle (in L²(0,1)) der { f_θ : 0 < θ < 1 }.

### Nyman–Beurling-Satz (1955)
```
RH  ⟺  𝟙_{(0,1)} ∈ 𝒩      (die konstante Funktion 1 liegt im Abschluss von 𝒩)
⟺  inf_{c_k, θ_k, N}  ‖ 1 − Σ_{k=1}^N c_k f_{θ_k} ‖_{L²(0,1)} = 0.
```
**Beweisidee:** Mellin-Transformation. Für g ∈ L²(0,1) ist Ĝ(s) = ∫_0^1 g(x) x^{s−1} dx. Die Dilatationen f_θ erzeugen via der Identität ∫_0^1 {θ/x} x^{s−1} dx = −(θ^s/s)·ζ(s)/(s−1)-artiger Faktoren einen Raum, dessen Orthogonalkomplement genau dann trivial ist, wenn ζ(s) keine Nullstellen mit Re(s) > 1/2 hat (Beurlings Theorem über invariante Teilräume / die Lage der Nullstellen von ζ als „innere Funktion").

### Báez-Duarte-Verschärfung (2003)
Beschränke θ auf die Kehrwerte ganzer Zahlen, θ = 1/k. Mit
```
A_N(x) = Σ_{k=1}^N c_k {k x}   (geeignete Koeffizienten c_k)
```
gilt:
```
RH  ⟺  d_N := inf_{c} ‖ 1 − Σ_{k=1}^N c_k ρ_{1/k} ‖²_{L²}  →  0   (N → ∞).
```
Báez-Duarte–Balazard–Landreau–Saias zeigten zudem die **quantitative** Vermutung:
```
d_N  ~  (Σ_ρ 1/|ρ|²) / log N   ≈  C / log N,
```
d. h. die Konvergenzrate ist (unter RH, mit einfachen Nullstellen) ∝ 1/log N — extrem langsam.

### Distanz-Formel über die Nullstellen
Die optimale Approximationsdistanz hat eine Darstellung über die nicht-trivialen Nullstellen:
```
liminf_{N→∞} (log N) · d_N  ≥  Σ_ρ m_ρ²/|ρ|²    (m_ρ = Vielfachheit),
```
was den direkten Bezug Distanz ↔ Nullstellenlage herstellt.

## Quellen
- [A general strong Nyman-Beurling Criterion for the Riemann Hypothesis (arXiv math/0505453)](https://arxiv.org/pdf/math/0505453)
- [New versions of the Nyman-Beurling criterion for the Riemann hypothesis — Báez-Duarte (Wiley)](https://onlinelibrary.wiley.com/doi/pdf/10.1155/S0161171202013248)
- [A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis (arXiv math/0202141)](https://arxiv.org/pdf/math/0202141)
- [On probabilistic generalizations of the Nyman-Beurling criterion (arXiv 1805.06733)](https://arxiv.org/pdf/1805.06733)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (3)
> - **Zirkuläre Positivität** *(Tier 2)* — Die RH wird auf eine Positivitätsaussage reduziert, die selbst nur als äquivalent, nie unabhängig bewiesen ist.
>   *Fluchtbedingung:* Die Positivität muss aus einer Struktur folgen, die unabhängig von der Nullstellenlage definiert ist. Im bewiesenen Fall 𝔽_q (doc-18) leistet das die Schnittform auf der Fläche C×C — dort ist Positivität ein Satz der Geometrie, nicht eine Umformulierung des Ziels.
> - **Konvergenz- / Grenzübergangslücke** *(Tier 2)* — Für jede endliche Abschneidung bewiesen — der Grenzübergang ist offen.
>   *Fluchtbedingung:* Eine von Λ (bzw. N, d) UNABHÄNGIGE Schranke — Kompaktheit, gleichgradige Stetigkeit oder eine explizite Fehlerabschätzung, die den Grenzübergang erlaubt.
> - **Äquivalenz-Falle** *(Tier 2)* — Ein Kriterium ist zur RH äquivalent und damit exakt gleich schwer — die Umformulierung erzeugt den Anschein von Fortschritt, ohne die Beweislast zu senken.
>   *Fluchtbedingung:* Eine der beiden Richtungen muss in STRIKT SCHWÄCHERER Form unbedingt bewiesen werden, oder es muss eine quantitative Größe geben, die sich unabhängig von der RH bewegen lässt (Λ ≤ 0.22, Anteil > 41 %, d_N-Raten). Nur solche Bewegungen zählen als Fortschritt — siehe docs/58.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!missing]- Die fehlende Aussage
> **Bewiesen:** Unter RH (mit einfachen Nullstellen) gilt d_N ~ C / log N. Unbedingte untere Schranken (Burnol-Typ): liminf (log N) d_N ≥ Σ_ρ m_ρ²/|ρ|².
> **Es fehlt:** Eine UNBEDINGTE obere Schranke, die d_N → 0 erzwingt. Alle bekannten unbedingten Resultate zeigen nach unten, nicht nach oben.
> **Typ:** aequivalenz · Bewertung: [[58_gap_registry_near_miss]]

> [!abstract]- Graph-Nachbarn (2)
> - *äquivalent zu* → **Riemann-Vermutung (RH)** — Nyman-Beurling/Báez-Duarte: Dichte ⟺ RH.
> - ← *wird benutzt von* [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|14 · Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]] — Beide Positivitäts-/Dichtekriterien, gemeinsames Leitmotiv.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
