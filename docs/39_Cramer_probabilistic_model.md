---
id: doc-39
number: 39
title: "Cramér-Modell & probabilistische Heuristiken der Primzahlen"
category: heuristic
status: open
tags: [cramer-model, probabilistic, prime-gaps, maier-theorem]
source_file: 39_Cramer_probabilistic_model.md
lang: de
---

# Cramér-Modell & probabilistische Heuristiken der Primzahlen

**Kategorie:** Heuristik / probabilistisches Modell
**Autoren / Jahre:** Harald Cramér (1936); Verfeinerungen Granville, Maier
**Typ:** Heuristisches Modell (kein Beweisansatz, aber Intuitionsquelle)
**Status:** Heuristik; teils im Detail korrigiert (Maier)

## Zusammenfassung
Das Cramér-Modell behandelt die Primzahlen als **Zufallsfolge** und liefert Vorhersagen über Primzahllücken, die mit der RH-Welt verträglich, aber unabhängig davon sind. Es ist die wichtigste *probabilistische Intuition* hinter Vermutungen über die Feinverteilung der Primzahlen und erklärt, warum die Nullstellenstatistik (GUE, Dok. 06) als „Zufälligkeit mit Abstoßung" erscheint.

## Mathematischer Kern (Formeln & Vermutungen)

### Das Modell
Modelliere „n ist prim" als unabhängige Ereignisse mit Wahrscheinlichkeit 1/log n (motiviert vom Primzahlsatz). Erwartete Anzahl Primzahlen bis x: ∫_2^x dt/log t = Li(x). ✓

### Cramér-Vermutung (Primzahllücken)
```
limsup_{n→∞} (p_{n+1} − p_n) / (log p_n)²  =  1.
```
D. h. maximale Lücken wachsen wie (log p)². **Wichtig:** Diese Vorhersage ist *stärker* als alles, was aus RH folgt — RH liefert nur O(√p log p) (Dok. 36). Das Modell geht also über die RH hinaus.

### Granville-Korrektur
Das naive Modell ignoriert die Multiplikativität (kleine Primteiler). Granville korrigierte den Faktor; vermutet wird heute
```
limsup (p_{n+1} − p_n)/(log p_n)²  ≥  2 e^{−γ} ≈ 1,1229.
```

### Maiers Satz (das Modell ist nicht exakt)
**Satz (Maier 1985).** Das Cramér-Modell sagt für Primzahlen in *sehr kurzen* Intervallen [x, x + (log x)^λ] eine asymptotische Gleichverteilung voraus — dies ist **falsch**. Die tatsächliche Anzahl schwankt um einen Faktor, der nicht gegen 1 geht. ⇒ Probabilistische Modelle sind Heuristik, kein Ersatz für analytische Beweise.

## Bedeutung / Einordnung
- Liefert die **Intuition**, warum die ζ-Nullstellen sich wie ein „Zufallssystem mit Niveau-Abstoßung" (GUE, Dok. 06) verhalten — Primzahlen ≈ zufällig, Nullstellen ≈ Fourier-dual dazu.
- **Warnung (für „bulletproof"):** Maiers Satz zeigt, dass plausible probabilistische Heuristiken im Detail *falsch* sein können — analog zur Mertens-Warnung (Dok. 16, 35). Ein Beweis darf sich nie auf das Modell stützen.
- Kein Lösungsansatz für die RH, aber unverzichtbarer Kontext für die Interpretation der Statistik.

## Quellen
- [Cramér's conjecture — Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture)
- [Harald Cramér and the distribution of prime numbers — A. Granville](https://dms.umontreal.ca/~andrew/PDF/cramer.pdf)
- [Beyond the Riemann hypothesis — primes and smooth numbers (Oxford)](https://www.maths.ox.ac.uk/node/65844)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (2)
> - **Numerische Extrapolation** *(Tier 3)* — Aus endlicher Rechnung wird auf asymptotisches Verhalten geschlossen — die RH-Landschaft hat dafür berüchtigte Gegenbeispiele.
>   *Fluchtbedingung:* Nicht überwindbar, nur vermeidbar: Numerik darf Hypothesen erzeugen und widerlegen, aber nie stützen. Ein rigoroses Intervall-Zertifikat (doc-54) ist etwas anderes als eine Stichprobe.
> - **Zirkularität der Modellannahme** *(Tier 3)* — Zufallsmatrix- und probabilistische Modelle setzen die RH voraus, um überhaupt formuliert werden zu können.
>   *Fluchtbedingung:* Unbedingte Formulierung: Aussagen über Nullstellen ohne die Annahme, dass sie auf der Geraden liegen (doc-53 ist der Prototyp).
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (2)
> - *ist Evidenz für* → [[35_obstructions_barriers|35 · Obstruktionen & Barrieren]] — Maier-Satz: probabilistisches Modell im Detail falsch (Warnung).
> - ← *modelliert von* [[69_Mobius_randomness_Chowla_Sarnak|69 · Möbius-Zufälligkeit]] — Alternatives, präziseres Zufälligkeitsmodell gegenüber Cramér.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
