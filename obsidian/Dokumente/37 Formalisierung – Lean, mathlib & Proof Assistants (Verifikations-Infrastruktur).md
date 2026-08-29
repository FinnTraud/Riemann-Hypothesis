---
id: doc-37
title: "Formalisierung: Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)"
nummer: "37"
kategorie: Verifikation
status: REFERENZ
typ: dokument
aliases:
  - "doc-37"
  - "Dok. 37"
tags:
  - "dokument"
  - "kategorie/verification"
  - "status/reference"
  - "thema/formalization"
  - "thema/lean"
  - "thema/mathlib"
  - "thema/prime-number-theorem"
  - "thema/proof-assistant"
quelle: docs/37_formalization_lean_proof_assistants.md
---

> [!info] Navigation
> **Karte:** [[MOC M – Meta ∕ 'Bulletproof'-Schicht (Obstruktionen, Synthese, Verifikation)]] · **Kategorie:** Verifikation · **Status:** `REFERENZ`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/37_formalization_lean_proof_assistants.md`

# Formalisierung: Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)

**Kategorie:** Infrastruktur / Verifikation (nicht Lösungsansatz, aber „bulletproof"-relevant)
**Autoren / Jahre:** Loeffler & Stoll (zeta/L-functions in Lean, 2025); Kontorovich & Tao (PrimeNumberTheorem+); mathlib-Community
**Typ:** Maschinell verifizierte Mathematik
**Status:** RH ist in Lean als *Aussage* formalisiert; Beweis offen. PNT formalisiert.

## Zusammenfassung
Proof Assistants (Lean 4 / mathlib, Coq, Isabelle) erlauben **maschinell geprüfte** Beweise, bei denen jeder Schritt gegen die Axiome verifiziert wird — keine Lücken, keine Halluzination. Für einen „bulletproof" RH-Server ist das die Brücke zwischen KI-generierten Ideen (Dok. [[28 KI ∕ Machine Learning und die Riemann-Vermutung|28]]) und zertifizierter Korrektheit: Ein künftiger RH-Beweis (von Mensch oder KI) sollte in einem solchen System verifiziert werden.

## Mathematischer/technischer Kern

### Was bereits formalisiert ist (Lean 4 / mathlib, Stand 2025)
- **Riemann-ζ und Dirichlet-L-Funktionen** als Objekte (Loeffler–Stoll, „Formalizing zeta and L-functions in Lean", arXiv 2503.00959): analytische Fortsetzung, Funktionalgleichung, Spezialwerte.
- **Dirichlets Satz** über Primzahlen in arithmetischen Progressionen (formal).
- **Formale Aussage der Riemann-Hypothese** in mathlib (`RiemannHypothesis`) — die *Behauptung* ist präzise hinterlegt, der Beweis ist `sorry`-frei nur als Statement.
- **Primzahlsatz (PNT)** via Wiener–Ikehara: Projekt **PrimeNumberTheorem+** (Kontorovich, Tao u. a.) — formalisiert, Merge in mathlib geplant; Ziele: expliziter Fehlerterm, PNT in Progressionen.
- **Irrationalität von ζ(3)** (Apéry) in Lean 4 formalisiert (arXiv 2503.07625).

### Wie die RH-Aussage in Lean aussieht (schematisch)
```lean
-- sinngemäß (mathlib-Notation vereinfacht):
theorem RiemannHypothesis :
    ∀ s : ℂ, riemannZeta s = 0 → s.re = 1/2 ∨ (∃ n : ℕ, s = -2*(n+1))
```
(d. h.: jede Nullstelle ist entweder kritisch oder trivial — die trivialen werden ausgenommen.)

### Warum das für „bulletproof" zählt
- **Verifizierbarkeit:** Ein Beweis, der in Lean durchläuft, ist garantiert lückenlos (modulo Kernel-Korrektheit) — das adressiert exakt das Halluzinationsproblem von LLMs (Dok. [[28 KI ∕ Machine Learning und die Riemann-Vermutung|28]]) und die Fehlertypen gescheiterter Beweise (Dok. [[27 Weitere umstrittene, zurückgezogene & fehlerhafte Beweisbehauptungen|27]]).
- **KI-Synergie:** Autoformalisierung + Beweissuche (AlphaProof-artig, Lean-Copilot) können Kandidatenbeweise generieren, die der Kernel prüft. Das ist die seriöse Rolle von KI bei der RH.
- **Teilziele:** Schon die Formalisierung von Zwischenresultaten (Hardy, Levinson, Guth–Maynard, de-Bruijn–Newman Λ≥0) wäre wertvoll und prüfbar.

## Bedeutung / Einordnung
- Kein Lösungs*ansatz*, sondern die **Qualitätssicherung**: das System, in dem ein gefundener Beweis bestehen müsste.
- Empfehlung für den MCP-Server: dieses Dokument als „Verifikations-Gateway" — jeder behauptete Beweis sollte gegen die Lean-Statement-Form und die Obstruktions-Checkliste (Dok. [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|35]]) geprüft werden.

## Quellen
- [Formalizing zeta and L-functions in Lean — Loeffler & Stoll (arXiv 2503.00959)](https://arxiv.org/pdf/2503.00959)
- [A Formal Proof of the Irrationality of ζ(3) in Lean 4 (arXiv 2503.07625)](https://arxiv.org/pdf/2503.07625)
- [Lean4 — Terence Tao (Blog, PrimeNumberTheorem+)](https://terrytao.wordpress.com/tag/lean4/)
- [Formalizing zeta and L-functions in Lean — Annales (afm.episciences.org)](https://afm.episciences.org/15954)

---

## 🔗 Wissensgraph

### Ausgehende Relationen

- **nutzt** → [[Riemann-Vermutung (RH)]] — *Lean/Formalisierung als Verifikations-Gateway.*

### Eingehende Relationen

- **wird gestützt durch** ← [[54 Maschinengestützte Zahlentheorie – ANTEDB, systematische Exponenten-Optimierung und formalisierter Primzahl]] — *Der formalisierte starke Primzahlsatz zeigt, dass Lean analytische Zahlentheorie traegt.*

### Im Text erwähnt

- [[27 Weitere umstrittene, zurückgezogene & fehlerhafte Beweisbehauptungen]]
- [[28 KI ∕ Machine Learning und die Riemann-Vermutung]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
