---
id: doc-12
number: 12
title: "Nullstellenfreie Regionen (klassischer analytischer Ansatz)"
category: analytic
status: open
tags: [zero-free-region, vinogradov-korobov, de-la-vallee-poussin, prime-number-theorem]
source_file: 12_zero_free_regions.md
lang: de
---

# Nullstellenfreie Regionen (klassischer analytischer Ansatz)

**Kategorie:** Analytischer Ansatz
**Autoren / Jahre:** Hadamard & de la Vallée Poussin (1896/1899), Littlewood (1922), Vinogradov–Korobov (1958), moderne explizite Verfeinerungen (2020er)
**Typ:** Schrittweise Annäherung (keine volle RH)
**Status:** Aktiv; bestes asymptotisches Resultat seit Jahrzehnten Vinogradov–Korobov

## Zusammenfassung
Statt die RH direkt zu beweisen, verfolgt ein Jahrhundert analytischer Arbeit das Ziel, die **Region des kritischen Streifens, die nachweislich frei von Nullstellen ist**, schrittweise zu vergrößern — den Streifen also "von rechts" Richtung kritische Gerade einzuengen. Jede Verbesserung liefert effektivere Versionen des Primzahlsatzes mit Fehlertermen.

## Historische Entwicklung der nullstellenfreien Region
(σ = Re(s), Schranke nahe σ = 1)

| Jahr | Autor(en) | Nullstellenfreie Region |
|---|---|---|
| 1896 | Hadamard, de la Vallée Poussin | ζ(1 + it) ≠ 0 ⇒ erster Beweis des Primzahlsatzes |
| 1899 | de la Vallée Poussin | 1 − σ ≤ c / log t |
| 1922 | Littlewood | 1 − σ ≤ c · log log t / log t |
| 1938 | Chudakov | 1 − σ ≤ c / (log t)^{3/4 + ε} |
| 1958 | Vinogradov, Korobov | 1 − σ ≤ c / (log t)^{2/3} (log log t)^{1/3} |
| 2020er | diverse (explizit) | z. B. ζ(σ + it) ≠ 0 für t ≥ 3, σ ≥ 1 − 1/(4,896 · log t) |

## Kernidee
- **Globale Methode (Hadamard):** Nutze Nicht-Negativität trigonometrischer Polynome (klassisch: 3 + 4cos θ + cos 2θ ≥ 0) zusammen mit der Eulerprodukt-/log-Ableitungsstruktur, um Nullstellen nahe σ = 1 auszuschließen.
- **Lokale Methode (Landau):** lokale Abschätzungen von ζ.
- **Vinogradov–Korobov:** schärfere Abschätzungen von Exponentialsummen ⇒ größerer nullstellenfreier Bereich. Der Beweis ist erheblich aufwändiger, das Resultat aber nur geringfügig stärker als de la Vallée Poussins.

## Bedeutung / Einordnung
- Liefert *effektive, explizite* (wenn auch schwache) Versionen des Primzahlsatzes mit Fehlertermen — praktisch wichtig (z. B. für Berechnungen, kryptographisch relevante Primzahldichten).
- **Fundamentale Schwäche:** Eine nullstellenfreie Region, so klein sie auch sein mag, hält Nullstellen nur von σ = 1 fern — sie *fixiert* sie nicht auf σ = 1/2. Damit prinzipiell schwächer als die RH.
- Der Vinogradov–Korobov-Exponent (2/3) blieb ~70 Jahre der beste; jüngste Decoupling-basierte Arbeiten (vgl. Guth–Maynard, Dok. 22) beginnen, an Exponenten in verwandten Dichteabschätzungen zu rütteln.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Das 3+4cos+cos2-Argument (de la Vallée Poussin)
Grundlage ist die nicht-negative trigonometrische Identität
```
3 + 4 cos θ + cos 2θ = 2(1 + cos θ)² ≥ 0.
```
Angewandt auf Re(log ζ) = Σ_{p,k} (1/k) p^{−kσ} cos(kt log p) liefert für σ > 1:
```
3 log ζ(σ) + 4 Re log ζ(σ+it) + Re log ζ(σ+2it) ≥ 0
⟺  ζ(σ)³ |ζ(σ+it)|⁴ |ζ(σ+2it)| ≥ 1.
```
Hätte ζ eine Nullstelle bei 1 + it₀, so würde die linke Seite beim Grenzübergang σ → 1⁺ gegen 0 gehen (Faktor |ζ(σ+it)|⁴ → 0 schneller als ζ(σ)³ → ∞ divergiert) — Widerspruch. ⇒ **ζ(1+it) ≠ 0** (Primzahlsatz). Quantifizierung des Arguments liefert die Region.

### de la Vallée Poussin (1899) — quantitativ
Mit Schranken |ζ'/ζ| ≪ log t in der Nähe von σ = 1 ergibt das obige Argument eine explizite Konstante c > 0 mit
```
ζ(σ + it) ≠ 0   für   σ > 1 − c/log|t|,   |t| ≥ 2.
```

### Vinogradov–Korobov (1958) — die Methode
Schärfere Abschätzungen von **Exponentialsummen** Σ_{n≤N} n^{−it} = Σ e^{−it log n} (Vinogradovs Mittelwertsatz / Weyl-van-der-Corput) liefern die subkonvexe Schranke
```
ζ(σ + it) ≪ |t|^{B(1−σ)^{3/2}} (log|t|)^{2/3}
```
und damit die bislang beste asymptotische nullstellenfreie Region
```
ζ(σ+it) ≠ 0   für   σ ≥ 1 − c/( (log|t|)^{2/3} (log log|t|)^{1/3} ).
```

### Konsequenz für den Primzahlsatz (Fehlerterm)
Eine Region σ > 1 − η(t) liefert via Konturverschiebung (Dok. 02)
```
ψ(x) − x ≪ x · exp( −c (log x)^{3/5} (log log x)^{−1/5} )   (Vinogradov–Korobov-Fehlerterm).
```
Unter RH wäre der Fehler O(√x log²x) — exponentiell besser. Das illustriert: nullstellenfreie Region ⇒ Fehlerterm, aber strikt schwächer als RH.

## Quellen
- [Zero-free regions for the Riemann zeta function (arXiv 1910.08205)](https://arxiv.org/pdf/1910.08205)
- [Explicit bounds on ζ(s) in the critical strip and a zero-free region (arXiv 2301.03165)](https://arxiv.org/pdf/2301.03165)
- [Zero-free regions inspired by work of Heath-Brown (arXiv 2603.21490)](https://arxiv.org/html/2603.21490)
- [Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function (arXiv 1410.3926)](https://arxiv.org/pdf/1410.3926)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_analytic|Analytische Ansätze]]

| Achse | Wert |
|---|---|
| Familie | analytic |
| Implikation | `partial` |
| Euler-Produkt | `essential` |
| Positivität | `n/a` |
| Strenge | `theorem` · Evidenz `n/a` |
| Testbar / formalisierbar | `high` / `medium` |

**Offener Kernschritt:** Vinogradov-Korobov-Region ist seit 1958 nicht substanziell verbessert; jede Verbesserung Richtung fester Streifen wäre ein Durchbruch.

**Hebel (was er liefern würde):** Einzige Methode, die Nullstellen wirklich ausschließt - nur eben nicht genug.

**Typische Fehlermodi:** [[F13_error-term-ceiling|F13 Strukturelle Decke des Fehlerterms]] · [[F12_ineffective-nonuniform|F12 Ineffektive oder nicht gleichmäßige Konstanten]]

**Vergleichbar mit:** [[04_Levinson_Conrey_positive_proportion|Levinson, Conrey & Co.: Positiver Anteil der Nullstellen auf der kritischen Geraden]] · [[22_Guth_Maynard_2024|Guth–Maynard (2024): Durchbruch bei Nullstellendichte-Abschätzungen]] · [[03_Hardy_1914_infinitely_many_zeros|Hardy (1914): Unendlich viele Nullstellen auf der kritischen Geraden]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-12 doc-04 doc-22 doc-03`

**Ausgehende Beziehungen**
- *ist schwächer als* (`weaker_than`) → [[concept_RH|Riemann-Vermutung (RH)]] — Nullstellenfreie Region ist weit schwächer als RH.

**Eingehende Beziehungen**
- *ist Obstruktion für* (`obstruction_for`) → [[57_Beurling_generalized_primes|57 — Beurlingsche verallgemeinerte Primzahlen: Euler-Produkt allein genügt nicht]] — Zeigt: die klassische nullstellenfreie Region ist im Beurling-Rahmen optimal.

**Thematisch benachbart (gemeinsame Tags):** [[37_formalization_lean_proof_assistants|Formalisierung: Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
