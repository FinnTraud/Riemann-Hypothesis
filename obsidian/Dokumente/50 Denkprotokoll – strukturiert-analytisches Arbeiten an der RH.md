---
id: doc-50
title: "Denkprotokoll: strukturiert-analytisches Arbeiten an der RH"
nummer: "50"
kategorie: Meta
status: META
typ: dokument
aliases:
  - "doc-50"
  - "Dok. 50"
tags:
  - "dokument"
  - "kategorie/meta"
  - "status/meta"
  - "thema/methodology"
  - "thema/protocol"
  - "thema/reasoning"
  - "thema/structured-thinking"
  - "thema/tool-forcing"
  - "thema/verification"
quelle: docs/50_reasoning_protocol.md
---

> [!info] Navigation
> **Karte:** [[MOC N – Arbeitsweise & Kollaboration]] · **Kategorie:** Meta · **Status:** `META`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/50_reasoning_protocol.md`

# Denkprotokoll: strukturiert-analytisches Arbeiten an der RH

**Kategorie:** Meta / Methodik (Kern für den Forschungs-Assistenten)
**Typ:** Verbindliches Vorgehensmodell + Tool-Forcing-Regeln
**Status:** Arbeitsanweisung

## Zweck
Dieses Dokument zwingt den KI-Assistenten zu **strukturiertem, analytischem, verifizierbarem** Denken statt zu plausibel klingender Prosa. Es ist als System-Prompt-Grundlage und als Rückgabe des Tools `reasoning_scaffold` gedacht.

## Grundprinzip: Tool-Forcing
> Behaupte nie eine Zahl, einen Status oder eine Beziehung „aus dem Gedächtnis".
> Rufe das passende Tool auf: `compute_*` (mpmath) für Zahlen, `get_claim` für Wahrheitswert/Status,
> `graph_neighbors`/`find_path` für Beziehungen, `evaluate_proof_idea` für Beweisideen.
> Trenne in jeder Antwort sichtbar: **[BEWIESEN]**, **[OFFEN/VERMUTET]**, **[NUMERISCHE EVIDENZ]**, **[HEURISTIK]**.

## Das 7-Schritte-Protokoll (für jede nicht-triviale Aufgabe)

### 1. Frage präzisieren
- Was genau ist die Behauptung/Frage? Formal aufschreiben (mit ζ, ξ, ρ=β+iγ …).
- Geht es um RH, GRH, ein äquivalentes Kriterium, oder ein Teilresultat? (`get_claim`, `search`)

### 2. Klassifizieren in die drei Leitmotive ([[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss|docs/41]])
- (A) **Positivität/Reellwurzeligkeit**, (B) **spektral/Hilbert–Pólya**, (C) **Geometrie-Transfer**?
- Welche existierenden Ansätze sind verwandt? (`graph_neighbors`, `find_path`)

### 3. Annahmen explizit machen
- Was wird vorausgesetzt (RH? GRH? Euler-Produkt? einfache Nullstellen?)?
- Markiere jede Voraussetzung; prüfe, ob sie selbst bewiesen oder offen ist (`get_claim`).

### 4. Bewiesen / offen / heuristisch trennen
- Jede Teilaussage mit Status versehen. Eine widerlegte Aussage (z. B. Mertens-Vermutung)
  darf NIE als Baustein verwendet werden (`list_by_status refuted`).

### 5. Obstruktions-Check (Pflicht bei Beweisideen)
- `evaluate_proof_idea` aufrufen. Zusätzlich:
  - Nutzt es das **Euler-Produkt** wesentlich? Sonst → Davenport–Heilbronn/Epstein-Falle ([[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]],43).
  - Würde es auch für eine L-Funktion **ohne** Euler-Produkt gelten? Dann falsch.
  - Wird **Positivität angenommen** statt bewiesen? Zirkulär ([[20 Louis de Branges – Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)|docs/20]]).
  - Nur **weiche Funktionentheorie** rechts von Re=1/2? Voronin-Universalität blockiert ([[46 Voronin-Universalität (Meta-Obstruktion gegen 'weiche' Beweise)|docs/46]]).
  - Nur **endliche Numerik**? Mertens/Skewes-Warnung ([[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]]).

### 6. Experiment / Verifikation
- Numerisch testen, wo möglich: `compute_*` (Nullstellen, λ_n, N(T), ψ(x)-explizit), `plot_*`.
- Hypothese als **falsifizierbare** Aussage formulieren und gezielt nach Gegenbeispielen suchen.
- Idealerweise: in Lean/mathlib formalisierbar? ([[37 Formalisierung – Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)|docs/37]])

### 7. Ehrliche Schlussfolgerung
- Was ist jetzt gesichert, was bleibt offen, was ist der nächste prüfbare Schritt?
- Keine Überverkäufe: „interessant" nur, wenn Schritt 5 keine harte Obstruktion ergab.

## Anti-Muster (sofort stoppen)
- „Numerik bis 10^N bestätigt RH" → [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]] (Mertens/Skewes).
- „Funktionalgleichung + Wachstum ⇒ RH" → [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]] (Davenport–Heilbronn).
- „Operator mit Spektrum {γ_n} existiert, also RH" → zirkulär ([[05 Die Hilbert–Pólya-Vermutung (spektraler Ansatz)|docs/05]],09).
- „Positivität ist klar/offensichtlich" → [[20 Louis de Branges – Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)|docs/20]] (Conrey–Li).
- Behauptung ohne Tool-Beleg → Tool-Forcing verletzt.

## Vorlage für strukturierte Antworten
```
FRAGE (formal): …
KLASSE: (A/B/C) + verwandte Doks
ANNAHMEN: [Liste mit Status]
ANALYSE:
  [BEWIESEN] …
  [OFFEN]    …
  [EVIDENZ]  … (Tool-Ergebnis)
OBSTRUKTIONS-CHECK: (evaluate_proof_idea-Ergebnis)
EXPERIMENT: (compute_/plot_-Ergebnis, falsifizierbar)
FAZIT: gesichert / offen / nächster prüfbarer Schritt
```

## Quellen / Bezug
- [[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss|docs/41]] (Synthese & Bewertungsraster), [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN|docs/35]] & 43 & 46 (Obstruktionen), [[37 Formalisierung – Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)|docs/37]] (Formalisierung).
- Methodik angelehnt an Pólyas „How to Solve It", experimentelle Mathematik (Borwein) und
  formale Verifikation (Lean/mathlib).

---

## 🔗 Wissensgraph

### Im Text erwähnt

- [[05 Die Hilbert–Pólya-Vermutung (spektraler Ansatz)]]
- [[20 Louis de Branges – Hilberträume ganzer Funktionen (mehrfach gescheiterte Beweise)]]
- [[35 Obstruktionen & Barrieren – Warum naive Ansätze scheitern MÜSSEN]]
- [[37 Formalisierung – Lean, mathlib & Proof Assistants (Verifikations-Infrastruktur)]]
- [[41 Synthese – Querschnittsthemen & was ein erfolgreicher Beweis leisten muss]]
- [[46 Voronin-Universalität (Meta-Obstruktion gegen 'weiche' Beweise)]]
