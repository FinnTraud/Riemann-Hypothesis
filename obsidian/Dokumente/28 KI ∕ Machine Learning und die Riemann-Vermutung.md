---
id: doc-28
title: "KI / Machine Learning und die Riemann-Vermutung"
nummer: "28"
kategorie: KI-Kontext
status: META
typ: dokument
aliases:
  - "doc-28"
  - "Dok. 28"
tags:
  - "dokument"
  - "kategorie/ai-context"
  - "status/meta"
  - "thema/ai"
  - "thema/formal-verification"
  - "thema/hallucination"
  - "thema/llm"
  - "thema/machine-learning"
quelle: docs/28_AI_and_RH.md
---

> [!info] Navigation
> **Karte:** [[MOC K – KI-Kontext]] · **Kategorie:** KI-Kontext · **Status:** `META`
> **Zentrale Notiz:** [[Riemann-Wissensnetz]] · **Original:** `docs/28_AI_and_RH.md`

# KI / Machine Learning und die Riemann-Vermutung

**Kategorie:** KI-Kontext / Methodenkritik
**Zeitraum:** Schwerpunkt 2024–2026
**Typ:** Empirische, datengetriebene (Nicht-Beweis-)Ansätze + kritische Einordnung
**Status:** Explizit KEINE formalen Beweise; exploratorisch/heuristisch

## Zusammenfassung
Moderne KI- und Machine-Learning-Methoden (Klassifikatoren, neuronale Netze, LLM-gestützte Mustererkennung, automatisierte/formale Beweissysteme) werden zunehmend auf die numerische Untersuchung der ζ-Nullstellenverteilung angewandt. Sie liefern **empirische, falsifizierbarkeitsorientierte** Evidenz — aber **keinen formalen Beweis**. Leitfrage (nach Terence Tao): *"Will AI Prove the Riemann Hypothesis Without Understanding It?"*

## Arten von KI-Ansätzen zur RH
1. **Datengetriebene Klassifikation / Explainability (2025):** ML-Modelle werden auf berechneten Nullstellen trainiert; man sucht diskriminative statistische Signale, die On-Line- von hypothetischem Off-Line-Verhalten unterscheiden. Befund: stabile erklärende Signale ausschließlich entlang der kritischen Geraden (konsistent mit RH). Ausdrücklich als *Nicht-Beweis* gerahmt.
2. **Generative / Kontradiktions-Tests:** Modelle prüfen, ob sich gegenbeispielartige Muster erzeugen lassen (Falsifikationsversuch).
3. **Formale/verifizierte Beweissysteme:** Projekte zur maschinellen Verifikation (Lean, Coq) und KI-gestützten Beweissuche — Ziel: korrekte, mechanisch geprüfte Beweise *ohne* Halluzination.

## Wo KI in der Mathematik bereits Erfolge hatte (zur Einordnung)
- **Erdős-Einheitsabstands-Problem (1946):** KI-/LLM-gestützt ein jahrzehntealtes Problem signifikant vorangebracht — gefeiert als bedeutender Beweis mittels Sprach-KI.
- **KI korrigierte Mathematiker:** Fälle, in denen KI zeigte, dass etablierte Annahmen falsch waren.
- Diese Erfolge betreffen *spezifische, gut abgegrenzte* Probleme — **nicht** offene Millennium-Probleme wie die RH.

## Wo es schiefging (Mahnungen)
- **Navier-Stokes-Fehlclaim:** OpenAI-Forscher verkündeten einen "Mathedurchbruch" (Millennium-Problem), der sich als **falsch** erwies — öffentlich kritisiert. Zeigt: KI-"Durchbrüche" bei Millennium-Problemen ohne strenge Peer Review führen zu Fehlbehauptungen.
- **KI scheitert an Spitzenforscher-Aufgaben:** Studien dokumentieren systematisches Versagen aktueller KI an schwierigen mathematischen Problemen.
- **Goldbach-Analogie:** Argument ("AI Cannot Prove Goldbach's Conjecture ... the Wrong Kind of Smart") — für offene zahlentheoretische Vermutungen fehlt KI nicht Rechenleistung, sondern die *Art strukturellen Verständnisses*, die ein gültiger Beweis verlangt. Überträgt sich direkt auf die RH.

## Kritische Würdigung (Kernpunkte)
- **Numerik ≠ Beweis:** Endliche/statistische Evidenz beweist die RH nie (unendlich viele Nullstellen). Die **widerlegte Mertens-Vermutung** (Dok. [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)|16]]) zeigt, dass scheinbar robuste numerische Muster bei ~10^30 versagen können.
- **Halluzinationsrisiko bei LLMs:** generative Modelle können plausibel klingende, aber falsche "Beweise" erzeugen — daher der Trend zu formal verifizierten Systemen.
- **Mensch-Maschine-Kollaboration funktioniert** dort, wo Maschinen Suchräume erschöpfen und Menschen/Verifizierer die Korrektheit garantieren (vgl. Polymath15, Dok. [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15|23]]).
- **Selbstregulierung der Community:** Mathematiker-Leitlinien zum verantwortungsvollen KI-Einsatz entstehen bereits.

## Bedeutung / Einordnung
- KI ist (Stand 2026) ein **Werkzeug zur Exploration, Mustererkennung und Verifikation** — kein eigenständiger Erzeuger akzeptierter RH-Beweise.
- Sinnvolle Rollen: Generierung von Vermutungen, Lokalisierung vielversprechender Strukturen, formale Verifikation menschlicher Beweise, numerische Großrechnungen.
- Offene Frage (Tao): Ob KI je einen RH-Beweis "ohne Verständnis" liefern könnte — und ob ein solcher von der Community als Erkenntnis akzeptiert würde.

## Mathematischer/Methodischer Kern (woran KI arbeitet, formal)

### Was die ML-Modelle konkret als Daten nutzen
- **Normierte Nullstellenabstände** δ_n = (γ_{n+1} − γ_n)·(1/2π)log(γ_n/2π) (vgl. Dok. [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)|06]]): Eingabe für Klassifikatoren, die GUE- vs. Nicht-GUE-Statistik unterscheiden.
- **Werte von Z(t)** / ζ(1/2+it) (Dok. [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden|03]]/[[24 Numerische Verifikation der Riemann-Vermutung|24]]) als Zeitreihe: Mustererkennung für Vorzeichenwechsel.
- **Li-Koeffizienten λ_n** / Turán-Ausdrücke (Dok. [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]/[[29 Jensen–Pólya-Programm – Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)|29]]): Positivitäts-Checks als Features.

### Formales Lernproblem (Beispiel Klassifikation)
Trainiere f_θ: (Feature-Vektor aus {γ_n}) → {„on-line", „off-line"}. Befund (MDPI 2025): diskriminative Signale treten **nur** entlang Re=1/2 stabil auf; Kontradiktions-Tests finden kein Off-Line-Muster. **Aber:** Das ist Induktion über endliche Stichproben — kein Allquantor-Beweis ∀ρ.

### Warum KI hier prinzipiell an eine Wand stößt
- **Endlichkeit:** Jedes ML-Modell sieht endlich viele Nullstellen; die RH ist eine Aussage über ∞ viele. Die widerlegte Mertens-Vermutung (Dok. [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)|16]]) zeigt formal: M(x)/√x < 1 gilt bis ~10^{14}, ist aber falsch (Odlyzko–te Riele: limsup > 1,06). Ein Klassifikator hätte „Mertens wahr" gelernt.
- **Halluzination bei LLM:** Ein generativer „Beweis" ist ein Sample aus p_θ(Text); Korrektheit ist *nicht* Teil der Zielfunktion. Daher Trend zu **formaler Verifikation** (Lean/mathlib, Coq): Dort wird jeder Schritt gegen Axiome geprüft, p(Beweis korrekt) = 1 per Konstruktion.

### Sinnvolle, formal saubere KI-Rollen
1. **Vermutungsgenerierung** (z. B. Muster in λ_n, Momentkonstanten g_k, Dok. [[07 Keating–Snaith – Momente der Zetafunktion via charakteristische Polynome (CUE)|07]]/[[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität|14]]).
2. **Beweissuche + formale Verifikation** (Mensch/Maschine-Hybrid, wie Polymath15, Dok. [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15|23]], wo Computer Lehmer-Paar-Schranken rigoros prüften).
3. **Numerische Großrechnung** (Dok. [[24 Numerische Verifikation der Riemann-Vermutung|24]]) — aber Verifikation per Intervallarithmetik, nicht per neuronalem Netz.

### Erfolgs- vs. Fehlbeispiele (formal eingeordnet)
- **Erdős-Einheitsabstandsproblem:** kombinatorisch-endliches Problem ⇒ KI-gestützte Konstruktion verifizierbar. RH ist *nicht* von diesem Typ.
- **Navier-Stokes-Fehlclaim:** zeigt, dass ein KI-„Beweis" eines Millennium-Problems ohne Peer Review/formale Prüfung scheitert — exakt das Risiko bei einem KI-„RH-Beweis".

## Quellen
- [Will AI Prove the Riemann Hypothesis Without Understanding It? — Terence Tao (YouTube)](https://youtu.be/PU1LMVGcyXA?si=RcL7JrKpHE5izoso)
- [Empirical Investigation of the Riemann Hypothesis Using Machine Learning (MDPI Mathematics 2025)](https://www.mdpi.com/2227-7390/13/17/2824)
- [Kein Platz für Halluzinationen: KI-Start-up will korrekte Mathebeweise garantieren — The Decoder](https://the-decoder.de/kein-platz-fuer-halluzinationen-ki-start-up-will-korrekte-mathebeweise-garantieren/)
- [Kreativer Lösungsweg: KI löst 60 Jahre altes Erdős-Problem — Heise](https://www.heise.de/news/Kreativer-Loesungsweg-KI-loest-60-Jahre-altes-Erd-s-Problem-11275796.html)
- [OpenAI-Forscher verkünden falschen Mathedurchbruch — MSN/Der Standard](https://www.msn.com/de-ch/nachrichten/other/open-ai-forscher-verk%C3%BCnden-falschen-mathedurchbruch-und-ernten-spott/ar-AA1OSsBR)
- [AI Cannot Prove Goldbach's Conjecture — Towards AI](https://pub.towardsai.net/ai-cannot-prove-goldbachs-conjecture-115bca355678)
- [Leitlinien: Mathematiker wollen Einsatz von KI eindämmen — Spektrum](https://www.spektrum.de/news/leitlinien-mathematiker-wollen-einsatz-von-ki-in-ihrem-fach-eindaemmen/2327655)
- [Terence Tao: "Beweise sind nicht mehr das Wichtigste in der Mathematik" — Der Standard](https://www.derstandard.de/story/3000000320851/terence-tao-beweise-sind-nicht-mehr-das-wichtigste-in-der-mathematik)

---

## 🔗 Wissensgraph

### Eingehende Relationen

- **wird gestützt durch** ← [[54 Maschinengestützte Zahlentheorie – ANTEDB, systematische Exponenten-Optimierung und formalisierter Primzahl]] — *Autoformalisierung als konkreter KI-Beitrag im RH-Umfeld.*

### Im Text erwähnt

- [[03 Hardy (1914) – Unendlich viele Nullstellen auf der kritischen Geraden]]
- [[06 Montgomery-Paarkorrelation & Random-Matrix-Theorie (GUE)]]
- [[07 Keating–Snaith – Momente der Zetafunktion via charakteristische Polynome (CUE)]]
- [[14 Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]]
- [[16 Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]]
- [[23 De-Bruijn–Newman-Konstante – Rodgers–Tao & Polymath15]]
- [[24 Numerische Verifikation der Riemann-Vermutung]]
- [[29 Jensen–Pólya-Programm – Laguerre–Pólya-Klasse & Jensen-Polynome (Griffin–Ono–Rolen–Zagier 2019)]]
