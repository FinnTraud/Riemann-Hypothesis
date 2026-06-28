# Deningers Kohomologie-Programm & dynamische Systeme auf gefolierten Räumen

**Kategorie:** Aktives Lösungsprogramm (arithmetische Geometrie / Dynamik)
**Autor / Jahre:** Christopher Deninger (ab frühen 1990ern); verwandt Flach–Morin, Leichtnam
**Typ:** Konjekturales kohomologisches/dynamisches Programm zur RH
**Status:** Offen; konjekturaler Rahmen, Schlüsselobjekte noch nicht konstruiert

## Zusammenfassung
Christopher Deninger schlug ein **kohomologisches Programm** vor, in dem Zetafunktionen als **regularisierte Determinanten** geometrischer/dynamischer Operatoren ausgedrückt werden. Ziel: die explizite Formel der Zahlentheorie (Dok. 02) als **Lefschetz-Spurformel** zu interpretieren und die RH als **spektrale Symmetriebedingung** — in direkter Analogie zum bewiesenen Weil/Deligne-Fall (Dok. 18).

## Die Leitidee
- Im Funktionenkörper-Fall ist ζ ein Quotient charakteristischer Polynome des Frobenius auf étaler Kohomologie; die RH ist eine Aussage über die Eigenwerte dieses Operators.
- **Deningers Wunsch:** Finde für Spec(ℤ) (bzw. arithmetische Schemata) eine **Kohomologietheorie** mit einem "Frobenius-artigen" Fluss/Operator, sodass:

```
ζ(s) "=" det_∞( (s − Θ) / 2π | H^•_{?} )^{±1}
```

  (regularisierte Determinante eines Operators Θ auf hypothetischen Kohomologiegruppen).
- Die **nicht-trivialen Nullstellen** wären dann Eigenwerte von Θ auf H¹; die **RH = Selbstadjungiertheit / spektrale Symmetrie** von Θ (eine Hilbert–Pólya-Realisierung, Dok. 05).

## Dynamische Systeme auf gefolierten Räumen
- Da die gesuchte Kohomologie für arithmetische Schemata (noch) nicht existiert, sucht Deninger nach **Modellen**: dynamische Systeme auf **gefolierten Mannigfaltigkeiten** (foliated spaces), deren **blattweise (leafwise) Kohomologie** mehrere der erwarteten Struktureigenschaften besitzt.
- In diesen Modellen entsprechen:
  - geschlossene Orbits ↔ Primzahlen,
  - Längen der Orbits ↔ log p,
  - die Lefschetz-Spurformel des Flusses ↔ Weils explizite Formel.
- **Flach–Morin** und andere haben Deningers Vermutungen über **Weil-Arakelov-Kohomologie** präzisiert und teilweise formalisiert.

## Bedeutung / Einordnung
- Liefert eine **konzeptuelle Brücke** zwischen dem bewiesenen geometrischen Fall und der analytischen RH — und eine geometrische Erklärung, *warum* die RH wahr sein sollte (spektrale Symmetrie eines natürlichen Operators).
- Eng verwandt und teils komplementär zu Connes' Adèle/𝔽₁-Programm (Dok. 10, 30): beide suchen die "fehlende Geometrie über ℤ", aber mit unterschiedlichen Werkzeugen (Dynamik/Foliation vs. nichtkommutative Geometrie/Topos).
- **Status:** Programmatisch und konjektural — die zentrale Kohomologietheorie samt Operator ist nicht konstruiert. Kein Beweis, aber ein einflussreicher struktureller Kompass.

## Quellen
- [Arithmetic Geometry and Analysis on Foliated Spaces — C. Deninger (Arizona Winter School)](https://swc-math.github.io/dls/DLSDeninger.pdf)
- [Analogies between analysis on foliated spaces and arithmetic geometry (arXiv 0709.2801)](https://arxiv.org/pdf/0709.2801)
- [Deninger's conjectures and Weil-Arakelov cohomology — Flach & Morin](https://www.math.u-bordeaux.fr/~bmorin/Deninger-WA5.pdf)
- [Dynamical systems for arithmetic schemes — Deninger (ResearchGate)](https://www.researchgate.net/publication/381101198_Dynamical_systems_for_arithmetic_schemes)
- [The Riemann Hypothesis: Arithmetic and Geometry — J. Lagarias](https://websites.umich.edu/~lagarias//doc/mt-holyoke-rev.pdf)
