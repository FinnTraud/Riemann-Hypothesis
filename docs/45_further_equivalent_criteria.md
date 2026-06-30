---
id: doc-45
number: 45
title: "Weitere äquivalente Kriterien (Volchkov, Sekatskii, Redheffer, Salem, BBLS-quantitativ)"
category: criterion
status: open
tags: [volchkov, sekatskii, redheffer-matrix, salem, baez-duarte-quantitative]
source_file: 45_further_equivalent_criteria.md
lang: de
---

# Weitere äquivalente Kriterien (Volchkov, Sekatskii, Redheffer, Salem, BBLS-quantitativ)

**Kategorie:** Äquivalente Kriterien (Ergänzung zu Dok. 13–16)
**Autoren / Jahre:** Salem (1953), Redheffer (1977), Volchkov (1995), Báez-Duarte–Balazard–Landreau–Saias (2000), Sekatskii–Beltraminelli–Merlini (2009–2012)
**Typ:** Zur RH äquivalente Aussagen
**Status:** Äquivalenzen bewiesen; jeweils unbewiesen für ζ

## Zusammenfassung
Sammlung weiterer zur RH äquivalenter Kriterien, die nicht in den Hauptdokumenten 13–16 stehen. Sie liefern alternative analytische, integrale und matrixbasierte „Angriffsflächen".

## Mathematischer Kern (Formeln, Sätze)

### Volchkov-Kriterium (1995) — Integral über log ζ
```
RH  ⟺  ∫_0^∞ (1 − 12t²)/(1 + 4t²)³ · log|ζ(1/2 + it)| dt  =  π(3 − γ)/32,
```
γ = Euler–Mascheroni-Konstante. Äquivalent über das Argument:
```
RH  ⟺  ∫_0^∞ [ 2t · arg ζ(1/2 + it) / (1/4 + t²)² ] dt = π(γ − 3).
```
Eine *Gleichheit* (nicht nur Ungleichung), die exakt dann gilt, wenn keine Nullstelle den Streifen rechts von 1/2 hat. Beweis via Argumentprinzip / generalisierter Littlewood-Satz angewandt auf log ζ.

### Sekatskii–Beltraminelli–Merlini (2009–2012) — Familie von log-ζ-Gleichheiten
Verallgemeinern Volchkov: Mittels des **generalisierten Littlewood-Satzes** (Konturintegral von log ζ gegen eine analytische Funktion g) erhält man eine ganze **Familie** von Gleichheiten der Form
```
RH  ⟺  ∫ (Gewicht_g(t)) log|ζ(1/2+it)| dt = (explizite Konstante),
```
parametrisiert durch g. Jede ist einzeln RH-äquivalent; liefert unendlich viele integrale Tests.

### Redheffer-Matrix-Kriterium (1977)
Definiere die n×n-Matrix R_n mit
```
(R_n)_{ij} = 1  falls j = 1  oder  i | j,   sonst 0.
```
Dann gilt det(R_n) = M(n) (Mertens-Funktion, Dok. 16!). Daher:
```
RH  ⟺  det(R_n) = O(n^{1/2 + ε})   für jedes ε > 0.
```
R_n hat n−1 Eigenwerte nahe 1 plus wenige große; die Determinante als Mertens-Summe verbindet Lineare Algebra/Graphentheorie mit der RH.

### Salem-Kriterium (1953)
Über eine Integralgleichung vom Wiener–Tauberischen Typ: die Nicht-Verschwindung einer bestimmten Integraltransformierten (Faltungskern e^{σx}/(e^{e^x}+1)-artig) ist äquivalent zu ζ(σ+it) ≠ 0 auf einer vertikalen Geraden. Verbindet RH mit Vollständigkeit/Dichte (verwandt Nyman–Beurling, Dok. 13).

### BBLS — quantitative Nyman–Beurling-Distanz (2000)
Mit d_N² = inf_{Polynom-Koeff.} ‖1 − Σ_{k≤N} c_k ρ_{1/k}‖²_{L²(0,1)} (vgl. Dok. 13):
```
RH  ⟺  d_N → 0,   und unter RH (einfache Nullstellen):  d_N² ~ (2 + γ − log 4π)/log N.
```
Die explizite Konstante (2+γ−log 4π) macht dies zum **konkretesten numerischen Zielwert** für einen approximationstheoretischen Angriff; die Auswertung läuft über eine arithmetische Gram-Matrix (Vasyunin).

## Bedeutung / Einordnung
- Erweitern das Arsenal äquivalenter Formulierungen (Integral-, Matrix-, Approximationsform).
- Redheffer verbindet direkt zur Mertens-Funktion (Dok. 16); Volchkov/Sekatskii bieten *Gleichheiten* (sensible Tests); BBLS gibt eine berechenbare Zielkonstante.
- **Offen:** Jede ist genauso schwer wie die RH selbst — sie verschieben das Problem, lösen es nicht.

## Quellen
- [On an equality equivalent to the Riemann hypothesis — Volchkov (Semantic Scholar)](https://www.semanticscholar.org/paper/On-an-equality-equivalent-to-the-Riemann-hypothesis-Volchkov/280edbe8824496a1dfb254fdbd41a2f215a26887)
- [Equalities involving integrals of the logarithm of the Riemann ζ equivalent to RH — Sekatskii et al. (arXiv 0806.1596)](https://arxiv.org/pdf/0806.1596)
- [The Riemann Hypothesis — AIM (Redheffer, Salem, Volchkov criteria)](https://www.aimath.org/WWN/rh/rh.pdf)
- [A strengthening of the Nyman-Beurling criterion — Báez-Duarte et al. (arXiv math/0202141)](https://arxiv.org/pdf/math/0202141)
