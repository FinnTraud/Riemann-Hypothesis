---
id: doc-39
title: "Cramér-Modell & probabilistische Heuristiken der Primzahlen"
nummer: "39"
kategorie: Heuristik
status: OFFEN
typ: dokument
aliases:
  - "doc-39"
  - "Dok. 39"
tags:
  - "dokument"
  - "kategorie/heuristic"
  - "status/open"
  - "thema/cramer-model"
  - "thema/maier-theorem"
  - "thema/prime-gaps"
  - "thema/probabilistic"
quelle: docs/39_Cramer_probabilistic_model.md
---

> [!info] Navigation
> **Karte:** [[MOC M – Meta ∕ 'Bulletproof'-Schicht (Obstruktionen, Synthese, Verifikation)]] · **Kategorie:** Heuristik · **Status:** `OFFEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/39_Cramer_probabilistic_model.md`

# Cramér-Modell & probabilistische Heuristiken der Primzahlen

**Kategorie:** Heuristik / probabilistisches Modell
**Autoren / Jahre:** Harald Cramér (1936); Verfeinerungen Granville, Maier
**Typ:** Heuristisches Modell (kein Beweisansatz, aber Intuitionsquelle)
**Status:** Heuristik; teils im Detail korrigiert (Maier)

## Zusammenfassung
Das Cramér-Modell behandelt die Primzahlen als **Zufallsfolge** und liefert Vorhersagen über Primzahllücken, die mit der RH-Welt verträglich, aber unabhängig davon sind. Es ist die wichtigste *probabilistische Intuition* hinter Vermutungen über die Feinverteilung der Primzahlen und erklärt, warum die Nullstellenstatistik (GUE, Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]]) als „Zufälligkeit mit Abstoßung" erscheint.

## Mathematischer Kern (Formeln & Vermutungen)

### Das Modell
Modelliere „n ist prim" als unabhängige Ereignisse mit Wahrscheinlichkeit 1/log n (motiviert vom Primzahlsatz). Erwartete Anzahl Primzahlen bis x: ∫_2^x dt/log t = Li(x). ✓

### Cramér-Vermutung (Primzahllücken)
```
limsup_{n→∞} (p_{n+1} − p_n) / (log p_n)²  =  1.
```
D. h. maximale Lücken wachsen wie (log p)². **Wichtig:** Diese Vorhersage ist *stärker* als alles, was aus RH folgt — RH liefert nur O(√p log p) (Dok. [[36 Konsequenzen der Riemann-Vermutung (was folgt, wenn sie wahr ist)|36]]). Das Modell geht also über die RH hinaus.

### Granville-Korrektur
Das naive Modell ignoriert die Multiplikativität (kleine Primteiler). Granville korrigierte den Faktor; vermutet wird heute
```
limsup (p_{n+1} − p_n)/(log p_n)²  ≥  2 e^{−γ} ≈ 1,1229.
```

### Maiers Satz (das Modell ist nicht exakt)
**Satz (Maier 1985).** Das Cramér-Modell sagt für Primzahlen in *sehr kurzen* Intervallen [x, x + (log x)^λ] eine asymptotische Gleichverteilung voraus — dies ist **falsch**. Die tatsächliche Anzahl schwankt um einen Faktor, der nicht gegen 1 geht. ⇒ Probabilistische Modelle sind Heuristik, kein Ersatz für analytische Beweise.

## Bedeutung / Einordnung
- Liefert die **Intuition**, warum die ζ-Nullstellen sich wie ein „Zufallssystem mit Niveau-Abstoßung" (GUE, Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]]) verhalten — Primzahlen ≈ zufällig, Nullstellen ≈ Fourier-dual dazu.
- **Warnung (für „bulletproof"):** Maiers Satz zeigt, dass plausible probabilistische Heuristiken im Detail *falsch* sein können — analog zur Mertens-Warnung (Dok. [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)|16]], [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]]). Ein Beweis darf sich nie auf das Modell stützen.
- Kein Lösungsansatz für die RH, aber unverzichtbarer Kontext für die Interpretation der Statistik.

## Quellen
- [Cramér's conjecture — Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture)
- [Harald Cramér and the distribution of prime numbers — A. Granville](https://dms.umontreal.ca/~andrew/PDF/cramer.pdf)
- [Beyond the Riemann hypothesis — primes and smooth numbers (Oxford)](https://www.maths.ox.ac.uk/node/65844)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Evidenz für** → [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]] — *Maier-Satz: probabilistisches Modell im Detail falsch (Warnung).*

### Im Text erwähnt

- [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]]
- [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]]
- [[36 Konsequenzen der Riemann-Vermutung (was folgt, wenn sie wahr ist)]]
