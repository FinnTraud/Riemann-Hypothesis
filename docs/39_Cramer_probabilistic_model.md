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

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *ist Evidenz für* (`evidence_for`) → [[35_obstructions_barriers|35 — Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN]] — Maier-Satz: probabilistisches Modell im Detail falsch (Warnung).

**Eingehende Beziehungen**
- *modelliert* (`models`) → [[58_Mobius_randomness_Chowla_Sarnak|58 — Möbius-Zufälligkeit: Chowla-Vermutung, Sarnak-Disjunktheit & die Paritätsbarriere]] — Alternatives, präziseres Zufälligkeitsmodell gegenüber Cramér.

**Thematisch benachbart (gemeinsame Tags):** [[36_consequences_of_RH|Konsequenzen der Riemann-Vermutung (was folgt, wenn sie wahr ist)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
