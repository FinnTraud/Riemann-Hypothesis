---
id: doc-76
number: 76
title: "Höhere Korrelationen: Hejhal, Rudnick–Sarnak & die GUE-Hypothese"
category: partial-results
status: proven
tags: [n-level-correlation, rudnick-sarnak, hejhal, GUE, katz-sarnak, symmetry-types, restricted-support]
source_file: 76_higher_correlations_Rudnick_Sarnak.md
lang: de
---

# Höhere Korrelationen der Nullstellen — Hejhal, Rudnick–Sarnak, Katz–Sarnak

**Kategorie:** Bewiesene Teilresultate (Statistik der Nullstellen)
**Autoren / Jahre:** Montgomery (1973, Paarkorrelation); Hejhal (1994, Tripel); Rudnick–Sarnak (1996, n-Level, alle GL_m); Katz–Sarnak (1999, Symmetrietypen); Bogomolny–Keating (Heuristik über Primzahl-Korrelationen)
**Typ:** Beweisbare Statistik-Aussagen unter **eingeschränktem Testfunktionsträger**
**Status:** BEWIESEN (im Rahmen der Trägerbedingung); die volle GUE-Hypothese ist offen

## Zusammenfassung
Montgomerys Paarkorrelation (Dok. 06) ist der Anfang, nicht das Ende: Rudnick und Sarnak bewiesen 1996, dass **alle n-Level-Korrelationen** der Nullstellen jeder cuspidalen automorphen L-Funktion mit dem GUE-Ensemble übereinstimmen — allerdings nur für Testfunktionen, deren Fouriertransformierte einen **eingeschränkten Träger** hat. Dieses Dokument erklärt, was genau bewiesen ist, wo die Trägerschranke herkommt und warum sie die entscheidende Barriere ist.

## Mathematischer Kern

### n-Level-Korrelation
Seien `γ_1 ≤ γ_2 ≤ …` die Ordinaten der Nullstellen und `\tilde γ_j = γ_j · (log γ_j)/(2π)` die **normalisierten** Ordinaten (mittlerer Abstand 1). Für eine Testfunktion `f: ℝ^n → ℝ` (glatt, translationsinvariant, schnell fallend) definiere
```
R_n(f, T) = (1/N(T)) · Σ_{j_1,…,j_n  paarweise verschieden, γ_{j_i} ≤ T}  f( \tilde γ_{j_1}, …, \tilde γ_{j_n} ).
```

**GUE-Vermutung (Montgomery–Odlyzko-Gesetz):**
```
R_n(f,T)  →  ∫_{ℝ^n} f(x) · det( K(x_i − x_j) )_{n×n} · δ(x̄) dx,     K(x) = sin(πx)/(πx).
```

### Satz (Rudnick–Sarnak 1996)
Für `f` mit `\hat f` getragen in
```
{ u ∈ ℝ^n : Σ_{j=1}^{n} |u_j|  <  2 }        (bzw. < 2/m für L-Funktionen von GL_m),
```
gilt die GUE-Formel **unbedingt** (ohne RH) — für ζ und allgemeiner für jede cuspidale automorphe L-Funktion von GL_m/ℚ. Hejhal hatte 1994 den Fall n = 3 behandelt, Montgomery 1973 den Fall n = 2 (mit Träger in (−1,1)).

### Woher die Trägerschranke kommt (und warum sie hart ist)
Der Beweis läuft über die **explizite Formel** (Dok. 02): Korrelationen der Nullstellen werden in Summen über Primzahlpotenzen übersetzt,
```
Σ_ρ  \hat f(γ …)   ⟷   Σ_{n}  Λ(n) … n^{−1/2} …
```
Die Trägerbedingung `Σ|u_j| < 2` entspricht genau der Länge, bis zu der man diese Primzahlsummen mit dem **Primzahlsatz** kontrollieren kann. Träger jenseits davon erfordert Wissen über **Korrelationen von Primzahlen** (Hardy–Littlewood-Tupelvermutung) — Bogomolny–Keating zeigten heuristisch, dass genau die Hardy–Littlewood-Konstanten dort auftauchen und sich zur GUE-Formel zusammensetzen. Damit gilt:
```
volle GUE-Statistik  ⟸  Hardy–Littlewood-Tupelvermutung (heuristisch/bedingt)
```
— d. h. „Zufälligkeit der Nullstellen" ist im Kern **äquivalent zu Zufälligkeit der Primzahlen**. Beide sind offen, und keine der beiden impliziert die RH.

### Katz–Sarnak: Symmetrietypen (Familien statt einzelner L-Funktion)
Für **Familien** von L-Funktionen (z. B. Dirichlet-L-Funktionen mod q, Modulform-L-Funktionen mit wachsendem Level) sagen Katz–Sarnak voraus, dass die **niedrigsten Nullstellen** (nahe s = 1/2) den klassischen kompakten Gruppen folgen:
```
unitär (U)   —  ζ, Dirichlet-Familie
symplektisch (USp)  —  quadratische Dirichlet-L-Funktionen
orthogonal (O±)   —  Modulform-Familien nach Vorzeichen der Funktionalgleichung
```
Im **Funktionenkörperfall** ist das ein **Satz** (Katz–Sarnak, via Deligne-Äquidistribution der Monodromie) — noch ein Beispiel dafür, dass die geometrische Seite liefert, was die arithmetische nur vermutet (vgl. Dok. 18, 59, 60).

### Was das für die RH bedeutet
- **Kein Implikationspfeil.** GUE-Statistik ist mit „RH falsch" nicht sofort unverträglich: einzelne Nullstellen abseits der Geraden würden Korrelationen in führender Ordnung kaum stören. Statistik ⇏ Lage (Fehlermodus `F14`).
- **Aber Struktur-Evidenz:** Die Übereinstimmung über n Ebenen und über Familien hinweg ist der stärkste bekannte Hinweis auf eine **spektrale Herkunft** der Nullstellen (Hilbert–Pólya, Dok. 05) — sie ist der Grund, warum das spektrale Programm ernst genommen wird.
- **Alternative Hypothese (Dok. 53):** Die AH ist mit der bewiesenen Trägerschranke *verträglich* — genau deshalb kann man sie mit heutigen Mitteln nicht ausschließen. Das ist der schärfste Beleg dafür, wie einschränkend die Trägerbedingung ist.

## Bedeutung / Einordnung
- Präzisiert und erweitert Dok. 06 — im Netzwerk der zentrale Knoten zwischen Statistik, expliziter Formel und Primzahl-Korrelationen.
- Nützlicher Merksatz für Beweisbewertung: *Wer aus GUE-Statistik die RH ableiten will, muss zuerst erklären, warum eine Ausnahme-Nullstelle die Statistik zerstören würde — das tut sie nicht.*

## Quellen
- [Z. Rudnick, P. Sarnak, *Zeros of principal L-functions and random matrix theory*, Duke Math. J. 81 (1996)](https://web.math.princeton.edu/sarnak/RudnickSarnak96.pdf)
- D. Hejhal, *On the triple correlation of zeros of the zeta function*, IMRN 1994.
- N. Katz, P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*, AMS Colloq. Publ. 45 (1999).
- E. Bogomolny, J. Keating, *Random matrix theory and the Riemann zeros I/II*, Nonlinearity 8 (1995) / 9 (1996).
- A. Odlyzko, *The 10^20-th zero of the Riemann zeta function and 175 million of its neighbors* (Datensätze).

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `probabilistic` |
> | Implikation | `model` |
> | Euler-Produkt | `essential` |
> | Positivität | `n/a` |
> | Strenge | `theorem` |
> | Evidenz | `strong` |
> | Testbar | `high` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Trägerbedingung Σ|u_j|<2 - jenseits davon braucht man Primzahl-Korrelationen.
> 
> **Hebel:** GUE über alle Ebenen bewiesen (im Trägerbereich) - starke Strukturevidenz.
> 
> **Fehlermodi:** [[F14_model-without-implication|F14 Zirkularität der Modellannahme]] · [[F13_error-term-ceiling|F13 Anteils-Decke der Mollifier-Methoden]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-76`

> [!warning]- Blocker — woran dieser Ansatz hängt (1)
> - **Zirkularität der Modellannahme** *(Tier 3)* — Zufallsmatrix- und probabilistische Modelle setzen die RH voraus, um überhaupt formuliert werden zu können.
>   *Fluchtbedingung:* Unbedingte Formulierung: Aussagen über Nullstellen ohne die Annahme, dass sie auf der Geraden liegen (doc-53 ist der Prototyp).
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (5)
> - *verallgemeinert* → [[06_Montgomery_pair_correlation_RMT|06 · Montgomery-Paarkorrelation & Random-Matrix-Theorie]] — n-Level-Korrelationen verallgemeinern Montgomerys Paarkorrelation.
> - *ist Instanz von* → **Paarkorrelation der Nullstellen (Montgomery F(alpha,T))** — Bewiesene GUE-Übereinstimmung im eingeschränkten Trägerbereich.
> - *ist Obstruktion für* → [[53_pair_correlation_alternative_hypothesis|53 · Paarkorrelation ohne RH & die Alternative Hypothese]] — Trägerbedingung erklärt, warum die Alternative Hypothese nicht auszuschließen ist.
> - *benutzt* → **Explizite Formel (Primzahlen↔Nullstellen)** — Übersetzt Nullstellenkorrelationen in Primzahlsummen.
> - *benutzt* → [[18_Weil_conjectures_function_fields_Deligne|18 · Weil-Vermutungen]] — Katz–Sarnak: im Funktionenkörperfall ist die Symmetrie ein Satz.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
