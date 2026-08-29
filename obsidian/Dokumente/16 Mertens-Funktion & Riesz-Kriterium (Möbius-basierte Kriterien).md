---
id: doc-16
title: "Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)"
nummer: "16"
kategorie: Äquivalente Kriterien
status: OFFEN
typ: dokument
aliases:
  - "doc-16"
  - "Dok. 16"
tags:
  - "dokument"
  - "kategorie/criterion"
  - "status/open"
  - "thema/mertens"
  - "thema/mertens-conjecture-refuted"
  - "thema/mobius"
  - "thema/riesz"
quelle: docs/16_Mertens_function_Riesz_criterion.md
---

> [!info] Navigation
> **Karte:** [[MOC D – Analytische Ansätze & äquivalente Kriterien]] · **Kategorie:** Äquivalente Kriterien · **Status:** `OFFEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/16_Mertens_function_Riesz_criterion.md`

# Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)

**Kategorie:** Äquivalentes Kriterium (Möbius-/Summatorik)
**Autoren / Jahre:** Riesz (1916); Mertens-Zusammenhang klassisch; Mertens-Vermutung widerlegt von Odlyzko & te Riele (1985)
**Typ:** Zur RH äquivalente Aussagen + lehrreiches Gegenbeispiel
**Status:** Äquivalenzen bewiesen; stärkere Mertens-Vermutung WIDERLEGT

## Zusammenfassung
Mehrere Kriterien drücken die RH über die **Möbius-Funktion** μ(n) und ihre Summatorik aus. Besonders lehrreich ist die **widerlegte Mertens-Vermutung**: Sie hätte die RH impliziert, ist aber falsch — eine Warnung vor zu starken hinreichenden Bedingungen.

## Mertens-Funktion-Kriterium
- Sei M(x) = Σ_{n≤x} μ(n) die summatorische Möbius-(Mertens-)Funktion.
- **RH-äquivalent:** Für jedes ε > 0 gilt M(x) / x^{1/2 + ε} → 0 für x → ∞. (D. h. M(x) = O(x^{1/2+ε}).)
- Das spiegelt 1/ζ(s) = Σ μ(n)/n^s wider: Die Wachstumsordnung von M(x) ist direkt an die Lage der Nullstellen gekoppelt.

## Die widerlegte Mertens-Vermutung (wichtige Lehre)
- **Mertens-Vermutung:** |M(n)| < √n für alle n. Wäre sie wahr, würde daraus die RH folgen (sie ist *stärker* als RH).
- **Widerlegung:** Andrew Odlyzko und Herman te Riele bewiesen 1985, dass die Mertens-Vermutung **falsch** ist (limsup M(x)/√x > 1, liminf < −1) — ohne ein explizites Gegenbeispiel n anzugeben (das kleinste bekannte Gegenbeispiel liegt extrem hoch, jenseits 10^16, vermutlich um 10^{30}+).
- **Lehre:** Eine plausible, numerisch lange gestützte "Verstärkung" der RH kann falsch sein. Numerische Evidenz bis zu großen Schranken beweist nichts — relevant auch für die kritische Einordnung von KI-/Datengetriebenen RH-"Bestätigungen" (vgl. Dok. [[28 KI ∕ Machine Learning und die Riemann-Vermutung|28]]).

## Riesz-Kriterium (1916)
- Marcel Riesz gab ein zur RH äquivalentes Kriterium über das Wachstum einer mit der Möbius-Funktion gebildeten unendlichen Reihe (Riesz-Funktion). Verwandt sind das **Hardy–Littlewood-Kriterium** und neuere **Riesz-Typ-Kriterien für die Selberg-Klasse** (Dok. [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse|21]]).

## Bedeutung / Einordnung
- Verknüpft die RH mit der "Zufälligkeit" der Vorzeichen von μ(n) (multiplikative Struktur der ganzen Zahlen).
- Die widerlegte Mertens-Vermutung ist eines der wichtigsten **mahnenden Gegenbeispiele** in der RH-Geschichte.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Möbius-Funktion und 1/ζ
```
1/ζ(s) = Σ_{n=1}^∞ μ(n)/n^s   (Re s > 1),   μ(n) = (−1)^{#Primfaktoren} falls quadratfrei, sonst 0.
```
Mit Perron/Mellin folgt für M(x) = Σ_{n≤x} μ(n) die Darstellung über die Nullstellen von ζ:
```
M(x) ≈ Σ_ρ x^ρ/(ρ ζ'(ρ)) − 2 + Σ ...
```

### Mertens-Kriterium
```
RH  ⟺  M(x) = O(x^{1/2 + ε})  für jedes ε > 0.
```
**Beweis:** Aus M(x) = O(x^{Θ+ε}) folgt durch abelsche Summation, dass 1/ζ(s) für Re(s) > Θ analytisch (nullstellenfrei) ist, also Θ ≥ sup_ρ Re(ρ). Umgekehrt liefert RH (sup Re ρ = 1/2) per Konturverschiebung M(x) ≪ x^{1/2+ε}.

### Mertens-Vermutung und ihre Widerlegung
**Vermutung (stärker als RH):** |M(x)| < √x ∀x ≥ 1, d. h. m(x) := M(x)/√x ∈ (−1, 1).
**Satz (Odlyzko–te Riele 1985):**
```
limsup_{x→∞} M(x)/√x  >  1,06     und     liminf_{x→∞} M(x)/√x  <  −1,009.
```
**Beweisidee:** Numerische Auswertung der ersten ~2000 Nullstellen γ_n und der Summe Σ 2 Re( x^{iγ}/(½+iγ)ζ'(ρ) )·x^{−... } mittels eines Diophantischen Approximationsarguments (LLL-Gitterreduktion), um eine Resonanz vieler Terme zu erzwingen, die m(x) über 1 treibt. Kein explizites Gegenbeispiel x, aber Existenznachweis. **Lehre:** RH bleibt wahr-vermutet, aber die *stärkere* Schranke |M|<√x ist falsch — numerische Evidenz bis 10^{14} hätte getäuscht.

### Riesz-Kriterium (1916)
Die Riesz-Funktion
```
P(x) = Σ_{k=1}^∞ (−1)^{k+1} x^k / ((k−1)! ζ(2k))
```
erfüllt:
```
RH  ⟺  P(x) = O(x^{1/4 + ε})   für jedes ε > 0   (x → ∞).
```
(Mellin-Transformierte von P involviert Γ(s)/ζ(2s); die Lage der Nullstellen von ζ(2s) bei Re = 1/4 liefert den Exponenten.)

### Hardy–Littlewood-Kriterium (verwandt)
```
RH  ⟺  Σ_{n=1}^∞ (−x)^n/(n! ζ(2n+1)) = O(x^{−1/4})   (x → ∞).
```

## Quellen
- [Criteria equivalent to the Riemann Hypothesis (arXiv 0808.0640)](https://arxiv.org/pdf/0808.0640)
- [Riemann's Hypothesis and the Mertens Function (Galetto)](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/galetto_RH_Mertens.pdf)
- [Riemann hypothesis — Wikipedia (Mertens function)](https://en.wikipedia.org/wiki/Riemann_hypothesis)
- [Riesz type criteria for L-functions in the Selberg class (arXiv 2211.02954)](https://arxiv.org/pdf/2211.02954)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **ist Evidenz für** → [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]] — *Widerlegte Mertens-Vermutung: numerische Evidenz täuscht (Warnung).*
- **ist äquivalent zu** → [[45 Weitere äquivalente Kriterien (Volchkov, Sekatskii, Redheffer, Salem, BBLS-quantitativ)]] — *Redheffer-Matrix det(R_n)=M(n) verbindet Mertens und Matrix-Kriterium.*
- **ist äquivalent zu** → [[Riemann-Vermutung (RH)]] — *Mertens-Kriterium M(x)=O(x^{1/2+ε}) ⟺ RH (NICHT die widerlegte Mertens-Vermutung).*

### Belegte Aussagen (Claims)

- `[BEWIESEN]` [[claim-mertens-criterion]] — RH ⟺ M(x)=O(x^{1/2+ε}) für jedes ε>0.
- `[WIDERLEGT]` [[claim-mertens-conjecture]] — |M(x)| < √x für alle x (Mertens-Vermutung, STÄRKER als RH).

### Im Text erwähnt

- [[21 Verallgemeinerte, Große Riemann-Vermutung & Selberg-Klasse]]
- [[28 KI ∕ Machine Learning und die Riemann-Vermutung]]
