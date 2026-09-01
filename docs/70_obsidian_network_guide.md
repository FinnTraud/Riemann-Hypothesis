---
id: doc-70
number: 70
title: "Obsidian-Netzwerk: Aufbau, Linktypen, Graph-Ansicht & Dataview"
category: context
status: meta
tags: [obsidian, network, wikilinks, graph-view, dataview, moc, workflow]
source_file: 70_obsidian_network_guide.md
lang: de
---

# Obsidian-Netzwerk — wie diese Wissensbasis vernetzt ist

**Kategorie:** Arbeitsweise / Werkzeug
**Typ:** Leitfaden für die Nutzung des Vaults in Obsidian
**Status:** Meta

## Die vier Knotentypen
Das Netzwerk besteht bewusst aus **vier** Sorten von Notizen — nicht nur aus Themendokumenten. Erst dadurch entstehen in der Graph-Ansicht sichtbare Cluster.

| Typ | Ort | Anzahl | Erzeugt von | Rolle im Graphen |
|---|---|---|---|---|
| **Dokument** | `docs/NN_*.md` | 71 | handgeschrieben | Inhalt: ein Thema, ein Ansatz, ein Kriterium |
| **Konzept-Hub** | `docs/concepts/` | 12 | generiert | Bündelt Dokumente um eine Idee (Euler-Produkt, Positivität, …) |
| **Fehlermodus** | `docs/fehlermodi/` | 15 | generiert | Bündelt Ansätze nach **Scheiterns-Ursache** (Dok. 68) |
| **MOC / Karte** | `docs/moc/` | 8 | generiert | Einstieg pro Ansatz-Familie + Hub |

Alle generierten Notizen entstehen aus `kb/graph/*.json` durch
```bash
python3 kb/build_obsidian.py
```
Der Befehl ist **idempotent**: Er ersetzt nur Blöcke zwischen `<!-- AUTO:… START -->` und `<!-- AUTO:… END -->`. Handgeschriebener Text bleibt unangetastet.

## Der Vernetzungsblock
Am Ende jedes Themendokuments steht ein generierter Abschnitt `## 🔗 Vernetzung` mit:
- **Karte** — Link zur MOC der Familie
- **Profil-Tabelle** — die Achsen aus `approaches.json` (Implikation, Euler-Produkt, Positivität, Strenge, Testbarkeit)
- **Offener Kernschritt** und **Hebel** — was genau fehlt, und was der Ansatz liefern würde
- **Typische Fehlermodi** — Links zu `F1…F15`
- **Vergleichbar mit** — die drei ähnlichsten Ansätze (Achsenübereinstimmung + gemeinsame Fehlermodi) inkl. fertigem `compare`-Befehl
- **Ausgehende / eingehende Beziehungen** — die typisierten Kanten aus `edges.json` mit Begründung
- **Thematisch benachbart** — Dokumente mit den meisten gemeinsamen Tags

## Die 15 Beziehungstypen
Kanten sind **typisiert** — das ist der Unterschied zu einem gewöhnlichen Zettelkasten. Ein Link sagt nicht nur „hängt zusammen", sondern **wie**:

| Typ | Bedeutung | Beispiel |
|---|---|---|
| `equivalent_to` | beweisbar RH-äquivalent | Nyman–Beurling ↔ RH |
| `implies` | echte Implikation | RH ⇒ Lindelöf |
| `reduces_to` | führt zurück auf | Li-Kriterium → Positivität |
| `partial_result_for` | Teilresultat | Hardy → RH |
| `evidence_for` | Evidenz, kein Beweis | GUE → Hilbert–Pólya |
| `models` | modelliert | Cramér → Primzahlen |
| `blueprint_for` | Blaupause | Weil/𝔽_q → RH über ℚ |
| `attempts_transfer_of` | versucht Transfer | 𝔽₁ → Weils Beweis |
| `obstruction_for` | schließt Ansatzklasse aus | Davenport–Heilbronn → weiche Beweise |
| `refuted_by` | widerlegt durch | de Branges ← Conrey–Li |
| `uses` | benutzt | Connes → Adele |
| `weaker_than`, `generalizes`, `special_case_of`, `instance_of` | Hierarchie | GRH ⊃ RH |

**Regel:** Neue Kanten gehören in `kb/graph/edges.json` (mit `note` = Begründung), nicht direkt in den Fließtext. So bleiben Prosa, Graph und MCP-Server konsistent.

## Empfohlene Obsidian-Einstellungen
1. **Graph-Ansicht → Gruppen (Groups)** anlegen, damit die Cluster farbig werden:
   - Suchbegriff `path:docs/fehlermodi` → Rot (Fehlermodi)
   - `path:docs/concepts` → Blau (Konzepte)
   - `path:docs/moc` → Grün (Karten)
   - `status: refuted` → Grau (gescheiterte Ansätze)
   - `status: proven` → Gelb (Bewiesenes)
2. **Filter:** „Existierende Dateien anzeigen" aktivieren, „Anhänge" aus.
3. **Lokaler Graph** (⌘/Ctrl + Klick auf ein Dokument) mit Tiefe 2 — zeigt das direkte Umfeld eines Ansatzes inklusive seiner Fehlermodi.
4. **Backlinks-Panel** immer offen: Die generierten Hubs erzeugen dichte Rückverweise.

## Dataview-Abfragen (Plugin „Dataview")
Wenn das Community-Plugin *Dataview* installiert ist, funktionieren diese Abfragen direkt:

````
```dataview
TABLE status, category, tags
FROM "docs"
WHERE status = "open" AND contains(category, "solution-program")
SORT number ASC
```
````

Alle gescheiterten Ansätze als Warntafel:
````
```dataview
LIST
FROM "docs"
WHERE status = "refuted"
```
````

Alle Fehlermodi nach Tier:
````
```dataview
TABLE tier
FROM "docs/fehlermodi"
SORT tier ASC, file.name ASC
```
````

## Zusammenspiel mit dem MCP-Server
Der Vault ist **eine** Datenbasis mit zwei Zugängen:
- **Mensch:** Obsidian (Graph, Backlinks, Dataview, Suche)
- **KI:** MCP-Server (`kb/server.py`) mit Suche, Graph, Claims, Vergleich, Fehlerdiagnose, Numerik, Lean

Beide lesen dieselben Dateien. Nach inhaltlichen Änderungen:
```bash
python3 kb/build_kb.py        # RAG-Index neu bauen (Suche/Graph für die KI)
python3 kb/build_obsidian.py  # Netzwerkschicht neu bauen (Links für den Menschen)
```

## Arbeitsablauf beim Hinzufügen eines Themas
1. `docs/NN_titel.md` mit Frontmatter (`id`, `number`, `title`, `category`, `status`, `tags`) anlegen — Schema siehe `README_RAG.md`.
2. Eintrag in `manifest.json` ergänzen.
3. Kanten in `kb/graph/edges.json` ergänzen (**mindestens eine** — sonst bleibt der Knoten im Graphen isoliert).
4. Falls es ein Ansatz ist: Profil in `kb/graph/approaches.json` (Achsen + Fehlermodi + offener Schritt + Hebel).
5. Atomare Aussagen mit Status in `kb/graph/claims.json`.
6. Beide Build-Skripte laufen lassen, in `docs/00_INDEX.md` verlinken.

## Verwandte Dokumente
Dok. 68 (Fehler-Anatomie) · Dok. 69 (Vergleichsmatrix) · Dok. 50 (Denkprotokoll) · Dok. 51 (Kollaboration) · `README_RAG.md`

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *benutzt* (`uses`) → [[50_reasoning_protocol|50 — Denkprotokoll: strukturiert-analytisches Arbeiten an der RH]] — Netzwerk ist die Datenbasis des Denkprotokolls.
- *benutzt* (`uses`) → [[69_comparison_matrix|69 — Vergleichsmatrix der Ansätze: Achsen, Lesarten, Auswahlhilfe]] — Erklärt, wie Vergleich und Matrix erzeugt werden.
- *benutzt* (`uses`) → [[68_failure_anatomy|68 — Anatomie des Scheiterns: Taxonomie der Fehlermodi F1–F15]] — Erklärt die Fehlermodus-Notizen im Graphen.

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
