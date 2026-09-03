---
id: doc-62
number: 62
title: "KI-Arbeitsteilung & Selbstaudit dieser Wissensbasis"
category: ai-context
status: meta
tags: [ai, division-of-labour, self-audit, limitations, failure-modes, honesty]
source_file: 62_ai_division_of_labour_self_audit.md
lang: de
---

# KI-Arbeitsteilung & Selbstaudit dieser Wissensbasis

**Kategorie:** KI-Kontext / Meta
**Verwandt:** `docs/28` (KI und RH) · `docs/50` (Denkprotokoll) · `docs/64` (Trust-Tiers) · `docs/55`, `docs/56`

## Teil 1 — Was eine KI hier tatsächlich anders kann

`docs/28` behandelt KI als *Werkzeug zur Mustererkennung an Nullstellendaten* —
und kommt zu Recht zum Ergebnis, dass das prinzipiell an eine Wand stößt.
Dieses Dokument behandelt eine andere Frage: **Was kann ein Sprachmodell an
diesem Problem leisten, das ein menschlicher Mathematiker nicht ohne Weiteres
leistet — nicht weil es klüger wäre, sondern weil es anders arbeitet?**

Fünf konkrete Punkte, alle in diesem Repo belegt:

### 1. Vollständige Kreuzauswertung statt selektiver Erinnerung
Die Blocker-Matrix (`docs/55`) verlangt, 55 Dokumente gleichzeitig gegen zwölf
Kategorien zu prüfen — 660 Einzelentscheidungen. Kein Mensch trifft die
konsistent, und niemand hat Anlass, es zu tun: der Ertrag pro Einzelzelle ist
zu klein. Erst die vollständige Matrix zeigt, dass **ein Blocker neun Ansätze
trägt**. Diese Aussage steckte immer schon in der Literatur; sichtbar wird sie
erst, wenn jemand die stumpfe Arbeit macht.

### 2. Negativkontrollen, die niemand durchführt
Die Frage aus `docs/60` — *würde mein Kriterium eine RH-verletzende Funktion
durchwinken?* — ist naheliegend und wird trotzdem praktisch nie gestellt. Der
Grund ist menschlich: Man rechnet an dem Objekt, das einen interessiert, nicht
an dem Gegenbeispiel. Ein System ohne inhaltliches Interesse hat diese
Voreingenommenheit nicht. Das Resultat (Sensitivität des Li-Kriteriums ~ γ²,
`docs/57` U1) ist elementar herleitbar und war trotzdem nicht dokumentiert.

### 3. Kein Sunk-Cost in einem eigenen Programm
Die instruktivste Autopsie der Sammlung ist de Branges (`docs/56` A1): Nach der
Widerlegung durch Conrey–Li folgten drei Jahrzehnte Umbau statt Rückzug. Das
ist keine Charakterschwäche, sondern der Normalfall bei jahrzehntelanger
Bindung an ein Programm. Ein System, das kein Programm besitzt, hat diesen
Fehlermodus nicht — **aber es hat einen spiegelbildlichen, siehe Teil 2.**

### 4. Ausdauer bei Buchhaltung
Trust-Tiers (`docs/64`), Gap-Registry (`docs/58`), Blocker-Zuordnungen: alles
Arbeit, die niemandes Publikationsliste verlängert und deren Wert erst ab
Vollständigkeit entsteht. Genau die Sorte Aufgabe, bei der ein
Kosten-Nutzen-Verhältnis für Menschen nie aufgeht.

### 5. Formalisierungsarbeit
Die Autopsien zeigen: die Bruchstellen liegen in *elementaren* Sätzen
(Liouville, bedingte Konvergenz, Definitionsbereiche), übersehen in Schritt 40
eines 60-Schritte-Arguments (`docs/56`, Beobachtung 2). Das ist exakt das
Profil, für das maschinelle Verifikation gebaut ist — und `docs/64` zeigt, dass
genau **ein** Claim von 43 diese Stufe erreicht.

### Was eine KI hier definitiv nicht kann
- **Das fehlende Objekt erfinden.** Die Kohomologie über Spec(ℤ) (`docs/30`)
  entsteht nicht durch Rekombination des Vorhandenen.
- **Beurteilen, ob eine Konstruktion „kanonisch" ist.** Das ist keine
  Eigenschaft des Objekts, sondern seiner Herkunft — nicht typisierbar
  (`kb/lean/RH/Gaps.lean`, `hilbert_polya_operator_exists`).
- **Ein Forschungsprogramm auswählen.** `docs/58` zeigt, dass die messbaren
  Ansätze die ausgereizten sind. Die Entscheidung, trotzdem am
  Unmessbaren zu arbeiten, ist mathematischer Geschmack — und der ist die
  eigentliche Leistung eines Forschers.

**Die ehrliche Arbeitsteilung lautet also nicht „KI löst Teilprobleme",
sondern: KI führt Buch, prüft gegen Gegenbeispiele und macht stumpfe Arbeit
vollständig — der Mensch entscheidet, woran gearbeitet wird.**

---

## Teil 2 — Selbstaudit: was an dieser Wissensbasis nicht stimmt

Ein Dokument über KI-Beiträge, das die KI-Fehlermodi nicht benennt, ist
Werbung. Die folgenden Punkte sind Befunde über **dieses Repo**.

### Befund 1 — 40 von 43 Claims sind Sekundärwissen
Die Primärquellen wurden für diese Wissensbasis **nicht gelesen**. Die
Quellenlinks belegen, *wo etwas nachzulesen wäre*, nicht dass es nachgelesen
wurde. Für Lehrbuchaussagen ist das unkritisch; für die neun T3-Claims aus
`docs/52`–`docs/54` (Arbeiten von 2025/2026) ist es die zentrale
Einschränkung. Vollständig aufgeschlüsselt in `docs/64`; Warnung automatisch
über `python3 kb/trust.py`.

### Befund 2 — der Vault war kein Obsidian-Vault
Bis zur Einführung der Obsidian-Schicht (`kb/obsidian.py`) enthielten die
55 Dokumente **null Wikilinks**. Es gab kein `.obsidian/`, kein Canvas, kein
Dataview. Die Verknüpfung, die das Projekt ausmacht, existierte
ausschließlich in `kb/graph/edges.json` — im Werkzeug sichtbar, im Vault
unsichtbar. Behoben, aber der Befund bleibt lehrreich: **Die Beschreibung des
Projekts und sein Zustand waren auseinandergelaufen, ohne dass es auffiel.**

### Befund 3 — das Anti-Crackpot-Gate ist schwächer, als es aussieht
`evaluate_proof_idea` arbeitet mit Stichwortsuche. Ein Beweisversuch, der das
Wort „Euler-Produkt" enthält, besteht den Test — auch wenn er das
Euler-Produkt nie benutzt. Das ist genau der Fall, den `docs/59` Ⓖ als eigene
Prüfung führen muss. **Das Gate filtert Vokabular, nicht Argumente.** Es sollte
als erste, nicht als letzte Instanz verstanden werden.

### Befund 4 — die Lean-Schicht ist Formulierung, kein Beweis
`kb/lean/RH/Gaps.lean` enthält ausschließlich `sorry`. Das ist beabsichtigt und
so dokumentiert (`docs/58`), aber es besteht Verwechslungsgefahr: Eine Datei
voller Lean-Signaturen sieht nach Fortschritt aus. Sie ist eine Adressliste.
Zusätzlich ist die Werkzeugkette in dieser Umgebung nicht gebaut worden — der
Code ist **nicht typgeprüft**. `kb/lean/README.md` sagt das; hier steht es
noch einmal.

### Befund 5 — die neuen Dokumente sind Ableitungen, keine Forschung
`docs/55`–`docs/64` enthalten **keine neue Mathematik über ζ**. Sie ordnen
Vorhandenes und rechnen Elementares (die γ²-Skalierung ist eine
Taylor-Entwicklung). Die einzige Aussage, die für dieses Repo neu ist — die
vierte DH-Nullstelle bei 0,724258 + 176,702461 i — ist mit hoher
Wahrscheinlichkeit längst publiziert; sie wurde hier nur nicht gefunden.
`docs/57` sagt das in seiner Ehrlichkeitsklausel ausdrücklich.

### Befund 6 — der Vault ist gegen wohlwollende Bestätigung nicht immun
Die gefährlichste Nutzung dieser Wissensbasis: jemand legt eine Beweisidee vor,
und das System bestätigt sie höflich. Sprachmodelle sind auf Zustimmung
trainiert; die RH zieht überzeugte Autoren an. Die Gegenmaßnahmen sind
absichtlich unhöflich gebaut — `docs/59` (beweist das zu viel?), `docs/60`
(gegen ein Gegenbeispiel rechnen), `docs/56` (Prüfprotokoll). Sie funktionieren
nur, wenn sie **vor** der inhaltlichen Würdigung laufen.

### Befund 7 — Datumsangaben, die hier nicht überprüfbar sind
Die Dokumente 52–54 tragen Zeitangaben („Stand August 2026") und verweisen auf
arXiv-Nummern aus 2025/2026. Diese Angaben konnten in dieser Umgebung nicht
gegen die Quellen geprüft werden. Sie sind als T3 (`docs/64`) eingestuft — mit
der ausdrücklichen Konsequenz, dass sie für Argumentation ohne Primärlektüre
nicht taugen.

### Befund 8 — ein Datenfehler stand unbemerkt im Graphen
`edges.json` enthielt die Kante `doc-20 --refuted_by--> doc-20` — eine
Selbstschleife. Aufgefallen ist sie erst, als der Obsidian-Compiler daraus
einen Wikilink erzeugte, der auf das eigene Dokument zeigt. Der Sachverhalt
(Conrey–Li widerlegten de Branges' Positivitätsbedingung) steht korrekt in
`claims.json`; die Kante war redundant und fehlerhaft. Sie ist entfernt, und
`kb/validate.py` prüft seitdem auf Selbstschleifen, ins Leere zeigende Kanten,
unbekannte Relationstypen und fehlende Pflichtfelder.

**Die verallgemeinerbare Lehre:** Kuratierte JSON-Daten ohne Validator
verrotten unbemerkt — genau wie Code ohne Tests. Der Fehler saß seit dem
Anlegen des Graphen darin und hätte durch bloßes Lesen nie auffallen können.

---

## Was daraus folgt

Für die Nutzung dieser Wissensbasis mit einem KI-System:

1. **Reihenfolge einhalten:** Obstruktionsprüfung (`docs/35`), dann
   Überschuss-Test (`docs/59`), dann Orakel (`docs/60`), **dann** erst
   inhaltliche Diskussion. Umgekehrt entsteht wohlwollende Bestätigung.
2. **Trust-Stufe mitzitieren:** `[BEWIESEN, T3-preprint]` statt `[BEWIESEN]`
   (`docs/64`).
3. **Primärquellen selbst lesen**, sobald etwas in eine Arbeit einfließt. Die
   Wissensbasis ist eine Landkarte, keine Quelle.
4. **Zahlen aus den Werkzeugen**, nicht aus dem Modellgedächtnis — das ist die
   Tool-Forcing-Regel aus `docs/50`, und Befund 1 ist der Grund dafür.

## Quellen
Dieses Dokument enthält keine mathematischen Behauptungen. Die Befunde in
Teil 2 sind am Repo selbst überprüfbar:
`python3 kb/validate.py` · `python3 kb/trust.py` · `python3 kb/matrix.py --stdout` ·
`cat kb/lean/RH/Gaps.lean`. Einordnung von KI in der Mathematik: `docs/28`.

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!abstract]- Graph-Nachbarn (2)
> - *benutzt* → [[28_AI_and_RH|28 · KI / Machine Learning und die Riemann-Vermutung]] — Vertieft die KI-Einordnung um Arbeitsteilung und Selbstaudit.
> - *benutzt* → [[64_trust_tiers_verification_levels|64 · Trust-Tiers]] — Befund 1 beruht auf der Trust-Tier-Auswertung.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
