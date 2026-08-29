# Obsidian-Vault: Riemann-Wissensnetz

Dieser Ordner **ist** ein fertiger Obsidian-Vault.

## Öffnen
1. Obsidian starten → *Ordner als Vault öffnen* → diesen Ordner (`obsidian/`) wählen.
2. Notiz **[[Riemann-Wissensnetz]]** öffnen (Einstiegspunkt).
3. Graph-Ansicht: `Strg/Cmd + G` — Farben zeigen die Kategorien, Pfeile die Relationsrichtung.

## Struktur
| Ordner | Inhalt |
| --- | --- |
| `Riemann-Wissensnetz.md` | Zentrale Übersicht: alle Dokumente, Konzepte, Claims, Statistik, Mermaid-Karte |
| `Dokumente/` | Je eine Notiz pro Wissensdokument (voller Text + typisierte Verknüpfungen) |
| `Konzepte/` | Konzepte und Querschnittsmotive (RH, Euler-Produkt, Positivität, Hilbert–Pólya …) |
| `Claims/` | Atomare Aussagen mit Status (BEWIESEN / OFFEN / WIDERLEGT) |
| `Karten/` | Themen-Karten (MOC) nach der Gliederung A–O + Relations-Legende |

## Neu erzeugen
```bash
python3 kb/build_obsidian.py
```
Der Vault wird vollständig aus `docs/`, `manifest.json` und `kb/graph/` regeneriert
(eigene Notizen daher **nicht** in diesem Ordner ablegen, sondern im Quellmaterial pflegen).

## Tipps für die Graph-Ansicht
- **Filter** `path:Dokumente` blendet Claims/Karten aus (reines Ansatz-Netz).
- **Filter** `tag:#status/offen` zeigt nur die noch offenen Programme.
- **Lokaler Graph** (`Strg/Cmd + P` → *Open local graph*) mit Tiefe 2 zeigt die Nachbarschaft
  eines einzelnen Ansatzes.
