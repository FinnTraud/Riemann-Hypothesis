---
id: doc-55
number: 55
title: "Speisers Satz & die Nullstellen von ζ′ (die Maschine hinter Levinson)"
category: criterion
status: proven
tags: [speiser, derivative, levinson-montgomery, mollifier, critical-line, equivalent-criterion]
source_file: 55_Speiser_zeros_of_zeta_prime.md
lang: de
---

# Speisers Satz & die Nullstellen von ζ′

**Kategorie:** Äquivalentes Kriterium (funktionentheoretisch) + Werkzeug
**Autoren / Jahre:** Andreas Speiser (1934); Levinson–Montgomery (1974); Conrey, Soundararajan, Zhang (moderne Verschärfungen)
**Typ:** RH-Äquivalenz über die Ableitung; zugleich der technische Motor von Levinsons Methode (Dok. 04)
**Status:** Äquivalenz BEWIESEN; RH selbst offen

## Zusammenfassung
Speiser bewies 1934 eine überraschende Umformulierung: Die RH ist **äquivalent dazu, dass ζ′(s) im Streifen 0 < Re(s) < 1/2 keine Nullstellen hat**. Statt über die Nullstellen von ζ zu reden, redet man über die Nullstellen der Ableitung — und die liegen (unter RH) alle rechts der kritischen Geraden. Levinson und Montgomery machten das 1974 quantitativ; genau diese Version ist der Grund, warum Levinsons Mollifier-Methode (Dok. 04) überhaupt funktioniert.

## Mathematischer Kern

### Speisers Satz (1934)
```
RH  ⟺  ζ′(s) ≠ 0  für alle s mit 0 < Re(s) < 1/2.
```
**Beweisidee (eine Richtung, anschaulich).** Man betrachtet die logarithmische Ableitung ζ′/ζ und das Argumentprinzip auf einem Rechteck links der Geraden. Eine nicht-triviale Nullstelle ρ mit Re(ρ) < 1/2 erzwingt über die Funktionalgleichung eine Spiegelnullstelle 1−ρ mit Re > 1/2; zwischen beiden muss ζ′ (nach einem Rouché-/Argument-Zählargument in der ξ-Funktion, die reell auf der Geraden ist) eine Nullstelle links der Geraden haben. Umgekehrt: gilt RH, so ist ξ(1/2+it) reell mit nur reellen Nullstellen, und ξ′ hat zwischen je zwei ξ-Nullstellen genau eine reelle Nullstelle (Rolle) — links der Geraden bleibt nichts übrig.

### Levinson–Montgomery (1974) — quantitative Form
Sei N⁻(T) die Anzahl der ζ-Nullstellen mit 0 < γ ≤ T und σ < 1/2, und N₁⁻(T) dieselbe Zählung für ζ′. Dann
```
N⁻(T)  =  N₁⁻(T)  +  O(log T).
```
Also: **ζ und ζ′ haben links der kritischen Geraden bis auf O(log T) gleich viele Nullstellen.** Zusätzlich: ζ^{(k)} hat für jedes k höchstens endlich viele nicht-reelle Nullstellen mit σ < 1/2, sobald man weit genug rechts startet; und ζ′ hat keine Nullstellen in 0 < σ < 1/2 mit sehr kleinem |t|.

### Warum das Levinsons Methode ermöglicht (Brücke zu Dok. 04)
Levinson (1974) zeigt nicht direkt „viele ζ-Nullstellen auf der Geraden", sondern:
1. zähle mit einem **Mollifier** ψ(s) die Nullstellen von `V(s) = ζ(s) + (Konstante)·ζ′(s)` bzw. von ζ′ links der Geraden;
2. schätze das Integral `(1/2πi) ∮ (V′/V) ds` über ein schmales Rechteck ab (Littlewood-Lemma + Mittelwertsätze für |ζψ|²);
3. übersetze via Speiser/Levinson–Montgomery zurück in eine untere Schranke für den Anteil der Nullstellen **auf** der Geraden.
Ergebnis: ≥ 1/3 (Levinson), 2/5 (Conrey 1989), heute > 41 % (Bui–Conrey–Young, Feng, Pratt–Robles–Zaharescu–Zeindler).

### Wo die Methode an ihre Decke stößt (Fehlermodus)
Die Mollifier-Länge ist an die Länge der zugänglichen **Mittelwertsätze** (Momente von ζψ) gebunden: mit Mollifiern der Länge T^θ und dem heutigen θ < 4/7 gewinnt man nur einen festen Anteil < 1/2. Ein Anteil 1 (geschweige denn RH) erfordert θ → 1, also Momente von ζ, die man ohne RH nicht kennt — **die Methode ist strukturell gedeckelt**, nicht nur „noch nicht optimiert". Siehe Fehlermodus `F13 error-term-ceiling` in Dok. 68.

### Nullstellen von ζ′ nahe der Geraden
Unter RH liegen alle ζ′-Nullstellen rechts von Re = 1/2, können ihr aber beliebig nahe kommen: sehr nahe ζ-Nullstellenpaare (**Lehmer-Paare**, Dok. 23) erzwingen eine ζ′-Nullstelle extrem dicht an der Geraden. Soundararajan formulierte quantitative Vermutungen über `min Re(ρ′) − 1/2`; Zhang und andere zeigten Verbindungen zur de-Bruijn–Newman-Konstante: eine Folge von ζ′-Nullstellen, die die Gerade *berührt*, wäre mit Λ = 0 verträglich — das „RH gilt gerade eben"-Bild.

## Bedeutung / Einordnung
- **Echte Äquivalenz** — aber vom Typ „Reformulierung ohne neuen Zugriff" (Fehlermodus `F11`): über ζ′ links der Geraden weiß man nichts, was man nicht über ζ wüsste.
- **Aber** sie ist die einzige Äquivalenz, aus der ein *quantitativer* Fortschritt (der 41 %-Satz) tatsächlich geflossen ist — die Ausnahme, die den Fehlermodus `F11` relativiert.
- Für Formalisierung (Dok. 37/54) attraktiv: Speisers Satz ist rein funktionentheoretisch und ohne tiefe Arithmetik beweisbar — ein realistischer Lean-Kandidat.

## Quellen
- A. Speiser, *Geometrisches zur Riemannschen Zetafunktion*, Math. Ann. 110 (1934), 514–521.
- N. Levinson, H. L. Montgomery, *Zeros of the derivatives of the Riemann zeta-function*, Acta Math. 133 (1974).
- [J. B. Conrey, *More than two fifths of the zeros of the zeta function are on the critical line*](https://eudml.org/doc/153199)
- [Bui–Conrey–Young, *More than 41% of the zeros of the zeta function are on the critical line* (arXiv:1002.4127)](https://arxiv.org/abs/1002.4127)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Karte:** [[MOC_criterion|Äquivalente Kriterien]]

| Achse | Wert |
|---|---|
| Familie | criterion |
| Implikation | `equivalent` |
| Euler-Produkt | `partial` |
| Positivität | `n/a` |
| Strenge | `theorem` · Evidenz `medium` |
| Testbar / formalisierbar | `high` / `high` |

**Offener Kernschritt:** Ueber ζ′ links der Geraden weiß man nichts, was man nicht über ζ wüsste.

**Hebel (was er liefern würde):** Die einzige Äquivalenz, aus der quantitativer Fortschritt floss (Levinson).

**Typische Fehlermodi:** [[F11_criterion-restates|F11 Äquivalenz ohne neuen Zugriff]] · [[F13_error-term-ceiling|F13 Strukturelle Decke des Fehlerterms]]

**Vergleichbar mit:** [[15_Robin_inequality|Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)]] · [[13_Nyman_Beurling_Baez_Duarte|Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]] · [[29_Jensen_Polya_Laguerre_Polya_GORZ|Jensen–Pólya-Programm: Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)]]
> Vergleich abrufen: `python3 kb/compare.py compare doc-55 doc-15 doc-13 doc-29`

**Ausgehende Beziehungen**
- *ist äquivalent zu* (`equivalent_to`) → [[concept_RH|Riemann-Vermutung (RH)]] — Speiser: RH ⟺ ζ′ hat keine Nullstellen in 0<Re(s)<1/2.
- *ist Blaupause für* (`blueprint_for`) → [[04_Levinson_Conrey_positive_proportion|04 — Levinson, Conrey & Co.: Positiver Anteil der Nullstellen auf der kritischen Geraden]] — Speiser/Levinson–Montgomery ist die technische Grundlage von Levinsons Mollifier-Methode.
- *benutzt* (`uses`) → [[23_de_Bruijn_Newman_constant_Polymath15|23 — De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15]] — Lehmer-Paare erzwingen ζ′-Nullstellen sehr nahe an der Geraden.
- *ist Instanz von* (`instance_of`) → [[concept_critical-line|Kritische Gerade Re(s)=1/2]] — Charakterisierung der Geraden über die Ableitung.

**Thematisch benachbart (gemeinsame Tags):** [[04_Levinson_Conrey_positive_proportion|Levinson, Conrey & Co.: Positiver Anteil der Nullstellen auf der kritischen Geraden]] · [[66_Bagchi_strong_recurrence|Bagchis Satz: RH als starke Rekurrenz (Universalität als Kriterium)]] · [[53_pair_correlation_alternative_hypothesis|Paarkorrelation ohne RH & die Alternative Hypothese (Goldston, Lee, Schettler, Suriajaya, Baluyot, Turnage-Butterbaugh, 2025–2026)]] · [[03_Hardy_1914_infinitely_many_zeros|Hardy (1914): Unendlich viele Nullstellen auf der kritischen Geraden]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
