---
id: doc-43
title: "Epstein-Zetafunktionen & Selberg-Klassen-Rigidität: Welche Eigenschaft erzwingt die kritische Gerade?"
nummer: "43"
kategorie: Obstruktionen
status: META
typ: dokument
aliases:
  - "doc-43"
  - "Dok. 43"
tags:
  - "dokument"
  - "kategorie/obstruction"
  - "status/meta"
  - "thema/davenport-heilbronn"
  - "thema/epstein-zeta"
  - "thema/euler-product"
  - "thema/kaczorowski-perelli"
  - "thema/selberg-class-rigidity"
quelle: docs/43_Epstein_zeta_Selberg_class_rigidity.md
---

> [!info] Navigation
> **Karte:** [[MOC M – Meta ∕ 'Bulletproof'-Schicht (Obstruktionen, Synthese, Verifikation)]] · **Kategorie:** Obstruktionen · **Status:** `META`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/43_Epstein_zeta_Selberg_class_rigidity.md`

# Epstein-Zetafunktionen & Selberg-Klassen-Rigidität: Welche Eigenschaft erzwingt die kritische Gerade?

**Kategorie:** Meta / Obstruktion (Tier-1 für „bulletproof")
**Autoren / Jahre:** Davenport–Heilbronn (1936); Epstein; Voronin; Kaczorowski–Perelli (Selberg-Klassen-Klassifikation, 1999–2011)
**Typ:** Diskriminierende Gegenbeispiele + Strukturtheorie
**Status:** Etablierte Negativ-/Rigiditätsresultate

## Zusammenfassung
Dies ist das **wichtigste „bulletproof"-Dokument** zusammen mit Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]]: Es beantwortet die Frage, **welche** Eigenschaften die Nullstellen tatsächlich auf die kritische Gerade zwingen — durch Funktionen, die *fast* wie ζ aussehen, aber die RH verletzen. Ergänzt Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]] (Davenport–Heilbronn) um die **Epstein-Zetafunktionen** und die **Rigidität der Selberg-Klasse vom Grad 1**.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Epstein-Zetafunktion
Für eine positiv-definite quadratische Form Q(m,n) = am² + bmn + cn² (Diskriminante d = b²−4ac < 0):
```
ζ_Q(s) = Σ_{(m,n) ≠ (0,0)} Q(m,n)^{−s}   (Re s > 1).
```
ζ_Q besitzt eine **analytische Fortsetzung** und eine **Funktionalegleichung** vom Riemann-Typ (Re s ↔ 1−s, via Theta-Transformation) — also dieselben „weichen" Eigenschaften wie ζ.

### Das Gegenbeispiel
**Satz (Davenport–Heilbronn 1936 für die zugehörige Dirichlet-Reihe; Epstein-Fall).** Wenn die **Klassenzahl h(d) > 1** ist (die quadratische Form nicht allein in ihrer Geschlechterklasse liegt), dann hat ζ_Q **unendlich viele Nullstellen mit Re(s) > 1/2** — die RH-Analogie ist FALSCH. Dennoch hat ζ_Q auch einen positiven Anteil (sogar unendlich viele) Nullstellen *auf* der Geraden.

### Warum: das fehlende Euler-Produkt
ζ_Q ist eine **Linearkombination** von Hecke-L-Funktionen zu Idealklassencharakteren:
```
ζ_Q(s) = (1/w) Σ_{χ} χ̄(class(Q)) L(s, χ),
```
und diese Summe besitzt **kein Euler-Produkt** (die einzelnen L(s,χ) schon, ihre Linearkombination nicht). Genau das fehlende Euler-Produkt erlaubt Nullstellen abseits der Geraden (vgl. Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]]).

### Selberg-Klassen-Rigidität (was RH erzwingt)
Die **Selberg-Klasse 𝒮** (Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]) verlangt zusätzlich zu Funktionalgleichung + Fortsetzung ein **Euler-Produkt** und die **Ramanujan-Bedingung**. Klassifikationssätze (Conrey–Ghosh; Kaczorowski–Perelli):
```
- Es gibt keine Funktionen in 𝒮 vom Grad 0 < d < 1.
- Grad d = 1 in 𝒮  ⟹  F(s) = ζ(s)  oder  F(s) = L(s + iθ, χ)  (verschobene Dirichlet-L-Funktion).
```
**Konsequenz (Rigidität):** Funktionen vom Grad 1 *mit* Euler-Produkt und Ramanujan-Bedingung sind im Wesentlichen ζ und Dirichlet-L — und für genau diese wird die RH erwartet. Davenport–Heilbronn (Grad 1, **ohne** Euler-Produkt) und Epstein (h>1, **ohne** Euler-Produkt) fallen heraus.

### Die präzise Lehre für einen Beweis
> Off-Line-Nullstellen werden möglich, sobald das Euler-Produkt fehlt. **Ein gültiger RH-Beweis muss die Multiplikativität (Euler-Produkt) + Ramanujan-Schranke an einer Stelle nutzen, an der Davenport–Heilbronn/Epstein sie verletzen.** Jeder Beweis, der diese Eigenschaften nicht unterscheidet, ist falsch.

## Verbindung
- Verschärft Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]] (Obstruktionen) und Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]] (Selberg-Klasse).
- Erklärt, warum Connes (Dok. [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]]) das Euler-Produkt adelisch (Stelle für Stelle) einbaut und warum Scattering-/Spektral­modelle für Davenport–Heilbronn gar nicht erst definierbar sind.

## Quellen
- [Zeros of the Davenport-Heilbronn Counterexample (AMS Math. Comp.)](https://www.ams.org/journals/mcom/2007-76-260/S0025-5718-07-01999-0/S0025-5718-07-01999-0.pdf)
- [Positive proportion of zeros of Epstein zeta on the critical line (arXiv 2411.18492)](https://arxiv.org/pdf/2411.18492)
- [On the Selberg class / converse theorems (arXiv 1605.02354)](https://arxiv.org/pdf/1605.02354)
- [On some reasons for doubting the Riemann hypothesis — Ivić (arXiv math/0311162)](https://arxiv.org/pdf/math/0311162)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Evidenz für** → [[Euler-Produkt (Multiplikativität)]] — *Epstein-Zeta + Selberg-Klassen-Rigidität: Euler-Produkt+Ramanujan erzwingen die Gerade.*
- **ist Obstruktion für** → [[52 Abgeschnittene Weil-Quadratform & Zeta-Spektraltripel (Connes–van Suijlekom, Connes–Consani–Moscovici, 2025]] — *Epstein/Selberg-Rigiditaet verlangt echten Euler-Produkt-Input - Dok. 52 liefert ihn, besteht die Pruefung also.*
- **ist Obstruktion für** → [[Riemann-Vermutung (RH)]] — *Welche Eigenschaft die Gerade erzwingt; schließt 'weiche' Beweise aus.*
- **nutzt** → [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse]] — *Selberg-Klassen-Klassifikation (Kaczorowski–Perelli).*

### Belegte Aussagen (Claims)

- `[BEWIESEN]` [[claim-epstein]] — Epstein-Zeta mit Klassenzahl>1 hat unendlich viele Nullstellen mit Re>1/2.
- `[BEWIESEN]` [[claim-selberg-rigidity]] — Grad-1-Elemente der Selberg-Klasse (mit Euler-Produkt+Ramanujan) sind genau ζ und verschobene Dirichlet-L.

### Im Text erwähnt

- [[10 Alain Connes – Spurformel & nichtkommutative Geometrie]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
