---
title: "Relationstypen (Legende)"
typ: legende
tags:
  - "legende"
---

# Relationstypen & Farben

> [!note] Wie das Netz zu lesen ist
> Jede Kante im Wissensgraph ist **typisiert**. Die Richtung steht in den Abschnitten
> *Ausgehende / Eingehende Relationen* jeder Notiz.

## Kantentypen

| Typ | Bedeutung | Umkehrung | Anzahl |
| --- | --- | --- | --- |
| `equivalent_to` | ist äquivalent zu | ist äquivalent zu | 10 |
| `implies` | impliziert | wird impliziert von | 1 |
| `reduces_to` | reduziert sich auf | ist Reduktionsziel von | 1 |
| `refuted_by` | wird widerlegt durch | widerlegt | 4 |
| `special_case_of` | ist Spezialfall von | hat als Spezialfall | 1 |
| `generalizes` | verallgemeinert | wird verallgemeinert von | 2 |
| `obstruction_for` | ist Obstruktion für | hat als Obstruktion | 5 |
| `evidence_for` | ist Evidenz für | wird gestützt durch | 14 |
| `models` | modelliert | wird modelliert von | 10 |
| `blueprint_for` | ist Blaupause für | hat als Blaupause | 4 |
| `uses` | nutzt | wird genutzt von | 26 |
| `partial_result_for` | ist Teilresultat für | hat als Teilresultat | 4 |
| `weaker_than` | ist schwächer als | ist stärker als | 3 |
| `attempts_transfer_of` | versucht Transfer von | wird zu übertragen versucht von | 4 |
| `instance_of` | ist Instanz von | hat als Instanz | 15 |

## Farbgruppen der Graph-Ansicht

| Farbe (Tag) | Kategorie |
| --- | --- |
| `#kategorie/foundations` — #4C8DFF | Fundamente |
| `#kategorie/partial-results` — #4CC9F0 | Partielle Resultate |
| `#kategorie/spectral` — #9B6BFF | Spektrale Ansätze |
| `#kategorie/analytic` — #2EC4B6 | Analytische Ansätze |
| `#kategorie/criterion` — #00B894 | Äquivalente Kriterien |
| `#kategorie/proven-analogue` — #3DDC84 | Bewiesene Analoga |
| `#kategorie/generalization` — #7BDFF2 | Verallgemeinerungen |
| `#kategorie/breakthrough` — #FFB703 | Durchbrüche |
| `#kategorie/numerical` — #B0BEC5 | Numerik |
| `#kategorie/failed-proof` — #E63946 | Gescheiterte Beweise |
| `#kategorie/obstruction` — #FF5C8A | Obstruktionen |
| `#kategorie/solution-program` — #F77F00 | Lösungsprogramme |
| `#kategorie/frontier` — #FFD166 | Aktuelle Front |
| `#kategorie/meta` — #8D99AE | Meta |
| `#kategorie/synthesis` — #EF476F | Synthese |

## Status-Tags

| Tag | Bedeutung |
| --- | --- |
| `#status/open` | OFFEN |
| `#status/proven` | BEWIESEN |
| `#status/refuted` | WIDERLEGT |
| `#status/reference` | REFERENZ |
| `#status/meta` | META |

Zurück zu [[Riemann-Wissensnetz]].
