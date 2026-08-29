---
id: doc-48
title: "Weitere algebraische/spektrale Programme: Meyer (Distributionen) & Kurokawa (absolute Zeta)"
nummer: "48"
kategorie: Lösungsprogramme
status: OFFEN
typ: dokument
aliases:
  - "doc-48"
  - "Dok. 48"
tags:
  - "dokument"
  - "kategorie/solution-program"
  - "status/open"
  - "thema/absolute-zeta"
  - "thema/distributions"
  - "thema/f1"
  - "thema/kurokawa"
  - "thema/meyer"
  - "thema/tensor-product"
quelle: docs/48_Meyer_Kurokawa_algebraic_programs.md
---

> [!info] Navigation
> **Karte:** [[MOC M – Meta ∕ 'Bulletproof'-Schicht (Obstruktionen, Synthese, Verifikation)]] · **Kategorie:** Lösungsprogramme · **Status:** `OFFEN`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/48_Meyer_Kurokawa_algebraic_programs.md`

# Weitere algebraische/spektrale Programme: Meyer (Distributionen) & Kurokawa (absolute Zeta)

**Kategorie:** Algebraisch/spektraler Ansatz (Ergänzung zu Dok. [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]], [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site|30]], [[31 Deningers Kohomologie-Programm & dynamische Systeme auf gefolierten Räumen|31]])
**Autoren / Jahre:** Ralf Meyer (2005); Nobushige Kurokawa (absolute Mathematik, 1990er–2000er)
**Typ:** Alternative spektrale bzw. F₁-nahe Programme
**Status:** Offen; teils rigorose Spektralrealisierung (Meyer), teils programmatisch (Kurokawa)

## Zusammenfassung
Zwei weitere ernstzunehmende Programme neben Connes (Dok. [[10 Alain Connes – Spurformel & nichtkommutative Geometrie|10]]), 𝔽₁ (Dok. [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site|30]]) und Deninger (Dok. [[31 Deningers Kohomologie-Programm & dynamische Systeme auf gefolierten Räumen|31]]): **Meyers** funktionalanalytische, distributionelle Spektralrealisierung der Nullstellen und **Kurokawas** „absolute" Zetafunktionen mit multiplikativer (Tensor-)Struktur über 𝔽₁.

## Mathematischer Kern (Konstruktionen, Formeln)

### Meyer: Spektralinterpretation via Distributionen (2005)
Meyer realisiert die nicht-trivialen Nullstellen als **Spektrum eines Operators auf einem Raum von Distributionen** auf der Adèleklassengruppe — eine rigorose, rein funktionalanalytische Variante von Connes' Programm, die **ohne** die Hypothese der RH auskommt und Weils explizite Formel als Spurformel reproduziert.
```
Idee:  betrachte den Quotienten  𝔸_ℚ^× / ℚ^×  und die Wirkung der Skalierung;
Nullstellen ρ  ↔  verallgemeinerte Eigenwerte (Distributionen) des Erzeugers;
explizite Formel  =  Spurformel auf diesem Distributionenraum.
```
Unterschied zu Connes: Meyer arbeitet mit **bornologischen / nuklearen** Räumen und vermeidet die Sobolev-Cutoff-Konstruktion; die RH bleibt äquivalent zu einer Positivität, ist aber sauberer eingebettet.

### Kurokawa: absolute Zeta & Tensorprodukte über 𝔽₁
Kurokawas „absolute Mathematik" definiert **absolute Tensorprodukte** ζ_1 ⊗ ζ_2 von Zetafunktionen, sodass Nullstellen/Pole sich additiv kombinieren:
```
(ζ_1 ⊗ ζ_2)  hat „Nullstellen"  ρ_1 + ρ_2 − (Verschiebung),
```
motiviert vom Wunsch, „Spec(ℤ) ×_{𝔽₁} Spec(ℤ)" zetafunktional zu realisieren (vgl. Weil-Beweis-Übertragung, Dok. [[18 Weil-Vermutungen – RH über endlichen Körpern (Deligne) – BEWIESEN|18]]/[[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site|30]]). Die **absolute Zetafunktion** ζ_{X/𝔽₁}(s) wird über ein „Limes q→1"-Verfahren aus den Punktzahlen #X(𝔽_q) gewonnen. In diesem Rahmen erscheint die gesuchte Positivität als Eigenschaft des Tensorprodukts ζ ⊗ ζ.

## Bedeutung / Einordnung
- **Meyer:** technisch sauberste Variante der Connes-Spektralrealisierung; nützlich, weil sie die Konstruktion von der RH entkoppelt und die verbleibende Hürde (Positivität) isoliert.
- **Kurokawa:** liefert die multiplikative/Tensor-Struktur, die ein 𝔽₁-Beweis (Dok. [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site|30]]) bräuchte, um Weils C×C-Argument nachzubilden.
- Beide teilen die Kern-Obstruktion: die entscheidende Positivität/Geometrie über ℤ ist nicht etabliert (Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]], [[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss|41]]).

## Quellen
- [R. Meyer — On a representation of the idele class group related to primes and zeros of L-functions (Duke Math. J. 2005 / arXiv math/0311468)](https://arxiv.org/abs/math/0311468)
- [A spectral interpretation for the zeros of the Riemann zeta function (arXiv math/0412277)](https://arxiv.org/pdf/math/0412277)
- [N. Kurokawa — Absolute tensor products / absolute zeta functions (Übersicht in: Deninger-Programm-Literatur)](https://arxiv.org/pdf/math/0505354)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **modelliert** → [[Hilbert–Pólya ∕ spektrale Interpretation]] — *Meyer: distributionelle Spektralrealisierung.*
- **versucht Transfer von** → [[Geometrie-Transfer (Funktionenkörper→ℤ)]] — *Kurokawa absolute Zeta/Tensorprodukte.*

### Im Text erwähnt

- [[10 Alain Connes – Spurformel & nichtkommutative Geometrie]]
- [[18 Weil-Vermutungen – RH über endlichen Körpern (Deligne) – BEWIESEN]]
- [[30 Der Körper mit einem Element (𝔽₁) & Connes–Consani arithmetic site]]
- [[31 Deningers Kohomologie-Programm & dynamische Systeme auf gefolierten Räumen]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
- [[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]]
