---
id: doc-70
number: 70
title: "Langlands-Funktorialität & automorphe L-Funktionen: Weg zur GRH?"
category: solution-program
status: open
tags: [langlands, functoriality, automorphic, ramanujan-petersson, converse-theorem, GRH, selberg-class]
source_file: 70_Langlands_functoriality_automorphic.md
lang: de
---

# Langlands-Funktorialität & automorphe L-Funktionen

**Kategorie:** Aktives Großprogramm (algebraisch/automorph) — indirekt RH-relevant
**Autoren / Jahre:** Langlands (1967 ff.); Deligne (1974, Ramanujan für holomorphe Formen); Lafforgue (2002, Funktionenkörper GL_n); V. Lafforgue (2018); Arthur (2013, klassische Gruppen)
**Typ:** Struktur-Programm, das die *Familie* aller L-Funktionen organisiert
**Status:** offen; große bewiesene Teilstücke — liefert **keine** Nullstellenlage

## Zusammenfassung
Das Langlands-Programm ordnet jeder automorphen Darstellung π einer reduktiven Gruppe eine L-Funktion L(s, π) zu und postuliert **Funktorialität**: L-Funktionen von Galoisdarstellungen sind automorph. Die GRH (Dok. 21) ist die Aussage, dass **alle** diese L-Funktionen ihre nicht-trivialen Nullstellen auf Re(s) = 1/2 haben. Dieses Dokument klärt eine häufig verwechselte Frage: **Was genau würde Funktorialität für die RH leisten — und was nicht?**

## Mathematischer Kern

### Die Objekte
Für eine (unitäre, cuspidale) automorphe Darstellung π von GL_n(𝔸_ℚ):
```
L(s, π) = Π_p Π_{j=1}^{n} (1 − α_{j}(p) p^{−s})^{−1},
Λ(s, π) = L_∞(s, π) L(s, π) = ε(π) Λ(1−s, π̃).
```
Also: **Euler-Produkt** (Grad n) + **Funktionalgleichung** + analytische Fortsetzung. Das sind exakt die Axiome der Selberg-Klasse S (Dok. 21) — die Selberg-Klasse ist gewissermaßen die axiomatische Schattenversion der automorphen Welt (Vermutung: S = automorphe L-Funktionen).

### Was Funktorialität liefert
Funktorialität (z. B. `Sym^k`-Lifts, Basiswechsel, Transfer entlang eines L-Homomorphismus ᴸH → ᴸG) liefert für neue L-Funktionen:
- **analytische Fortsetzung + Funktionalgleichung** (via automorpher Realisierung, Converse-Theoreme von Cogdell–Piatetski-Shapiro),
- **Nichtverschwinden auf Re(s) = 1** (der Schlüsselschritt für PNT-Analoga),
- **Ramanujan–Petersson-Schranken** in bewiesenen Fällen (|α_j(p)| = 1),
- damit **Subkonvexität** und die gesamte moderne analytische Zahlentheorie (Dok. 49).

### Was Funktorialität NICHT liefert
```
Funktorialität  ⇏  GRH.
```
Denn Funktorialität ist eine Aussage über **Existenz und Herkunft** von L-Funktionen, nicht über die **Lage ihrer Nullstellen**. Der Beweis dafür, dass sie es nicht liefern kann, ist strukturell:
- Bereits die einfachste automorphe L-Funktion (ζ selbst, π = triviale Darstellung von GL_1) hat volle Funktorialität — und die RH ist offen.
- Der Selberg-Klassen-Rahmen (Dok. 43) zeigt: Euler-Produkt + Funktionalgleichung **allein** erzwingen die Gerade nicht (dazu braucht man Grad-Klassifikation *und* zusätzliche Rigidität).
- Umgekehrt sind **Landau–Siegel-Nullstellen** (Dok. 32) genau in der automorphen Welt am hartnäckigsten: eine reelle Ausnahmennullstelle nahe s = 1 ist mit allem Funktorialitäts-Wissen verträglich.

### Die eine Stelle, an der Geometrie doch Nullstellen erzwingt
Die **Ramanujan–Petersson-Vermutung** für holomorphe Modulformen (|τ(p)| ≤ 2p^{11/2}) ist ein *lokales* RH-Analogon und wurde von **Deligne** bewiesen — durch die Weil-Vermutungen (Dok. 18), also durch **Geometrie über 𝔽_p**. Muster:
```
lokal (Frobenius-Eigenwerte, |α| = p^{w/2})   ← Geometrie/Kohomologie liefert Beweis
global (Nullstellen von L(s,π) auf Re=1/2)   ← kein geometrisches Objekt bekannt
```
Diese Asymmetrie ist **der** Kern des Problems und verbindet dieses Dokument direkt mit Dok. 71 (Standardvermutungen), Dok. 72 (Arakelov) und Dok. 30 (𝔽₁): Es fehlt ein Raum, über dem die globalen Nullstellen Frobenius-Eigenwerte wären.

### Funktionenkörper: dort ist alles bewiesen
Über 𝔽_q(C) hat L. Lafforgue (GL_n, 2002) Funktorialität in Form der Langlands-Korrespondenz bewiesen — **und dort gilt die RH** (Deligne). Der Grund ist nicht die Korrespondenz, sondern die zugrundeliegende Geometrie (Weil II). Das ist das schärfste Argument dafür, dass Funktorialität allein über ℚ nicht reicht: über 𝔽_q ist sie bewiesen *und* die RH ist bewiesen — aber die RH kommt aus der anderen Zutat.

## Bedeutung / Einordnung
- Für den Assistenten wichtig als **Erwartungs-Korrektur**: „Wenn Langlands gelöst ist, folgt die RH" ist **falsch**.
- Konkret nützlich bleibt Langlands für die RH-Landschaft über: Nichtverschwinden bei Re = 1, Subkonvexität, Momente in Familien (Dok. 07), Rigiditätsaussagen (Dok. 43).
- Fehlermodus: `F10 analogy-transfer-gap` (Dok. 55) — das Programm baut die Familie, nicht den Grund für die Gerade.

## Quellen
- [R. P. Langlands, *Problems in the theory of automorphic forms* (1970)](https://publications.ias.edu/rpl/paper/28)
- P. Deligne, *La conjecture de Weil I*, Publ. Math. IHÉS 43 (1974).
- L. Lafforgue, *Chtoucas de Drinfeld et correspondance de Langlands*, Invent. Math. 147 (2002).
- J. Arthur, *The Endoscopic Classification of Representations*, AMS Colloq. Publ. 61 (2013).
- [Iwaniec–Kowalski, *Analytic Number Theory*, Kap. 5 (L-Funktionen-Axiome)](https://www.ams.org/books/coll/053/)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!info]- Achsenprofil — wie dieser Ansatz einzuordnen ist
> | Achse | Wert |
> |---|---|
> | Familie | `algebraic-geometric` |
> | Implikation | `none` |
> | Euler-Produkt | `essential` |
> | Positivität | `n/a` |
> | Strenge | `program` |
> | Evidenz | `medium` |
> | Testbar | `low` |
> | Formalisierbar | `low` |
> 
> **Offener Kernschritt:** Funktorialität organisiert die Familie, sagt aber nichts über Nullstellenlage.
> 
> **Hebel:** Liefert Nichtverschwinden bei Re=1, Subkonvexität, Familien-Statistik.
> 
> **Fehlermodi:** [[F10_analogy-transfer-gap|F10 Fehlende Geometrie über Spec(ℤ)]]
> 
> Vergleich: [[78_approach_comparison_matrix]] · `python3 kb/compare.py profile doc-70`

> [!abstract]- Graph-Nachbarn (4)
> - *ist Obstruktion für* → [[32_Landau_Siegel_zeros_Zhang|32 · Landau–Siegel-Nullstellen]] — Landau–Siegel-Nullstellen bleiben mit voller Funktorialität verträglich.
> - *ist Teilresultat für* → **Verallgemeinerte/Große RH** — Organisiert die Familie aller L-Funktionen, für die GRH behauptet wird.
> - *benutzt* → [[21_GRH_Selberg_class_grand_RH|21 · Verallgemeinerte, Große Riemann-Vermutung & Selberg…]] — Selberg-Klasse als axiomatische Schattenversion der automorphen Welt.
> - *benutzt* → [[18_Weil_conjectures_function_fields_Deligne|18 · Weil-Vermutungen]] — Ramanujan–Petersson (lokales RH-Analogon) folgt aus Deligne/Weil.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
