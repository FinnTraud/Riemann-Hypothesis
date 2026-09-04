#!/usr/bin/env python3
"""Near-Miss-Ranking aus kb/graph/gaps.json berechnen und in docs/58 schreiben.

Der Score wird IMMER hier berechnet, nie in der JSON gepflegt -- so bleibt die
Regel auditierbar und die Daten bleiben Rohdaten.

    score = 3A + 2B + 2C + D - 2E,   gedeckelt auf 3 falls erreichbar=false,
    untere Grenze 0.

    python3 kb/gaps.py            # schreibt die Tabelle nach docs/58
    python3 kb/gaps.py --stdout   # nur ausgeben
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAPS = ROOT / "kb" / "graph" / "gaps.json"
TARGET = ROOT / "docs" / "58_gap_registry_near_miss.md"
BEGIN = "<!-- GAPS:BEGIN (generiert von kb/gaps.py -- nicht von Hand editieren) -->"
END = "<!-- GAPS:END -->"

WEIGHTS = {"A": 3, "B": 2, "C": 2, "D": 1, "E": -2}
CAP = 3


def score(gap):
    raw = sum(WEIGHTS[k] * int(gap.get(k, 0)) for k in WEIGHTS)
    capped = min(raw, CAP) if not gap.get("erreichbar", True) else raw
    return max(0, capped), raw


def load():
    return json.loads(GAPS.read_text(encoding="utf-8"))


def render(data):
    gaps = data["gaps"]
    scored = []
    for g in gaps:
        s, raw = score(g)
        scored.append((s, raw, g))
    scored.sort(key=lambda t: (-t[0], t[2]["doc"]))

    out = []
    out.append("**Rechenregel (auditierbar):** `score = 3A + 2B + 2C + D − 2E`, "
               "gedeckelt auf 3, falls die Methode das Ziel prinzipiell nicht "
               "erreichen kann. Die Achsenwerte stehen mit Begründung in "
               "`kb/graph/gaps.json`; berechnet wird der Score von `kb/gaps.py`. "
               "**Ein hoher Score bedeutet „viel unbedingt bewiesene Struktur "
               "vorhanden“, nicht „aussichtsreich“ — siehe die "
               "Auswertung darunter.**\n")
    out.append("| Rang | Lücke | Dok | Typ | A | B | C | D | E | Score | roh |")
    out.append("|---|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|")
    for i, (s, raw, g) in enumerate(scored, 1):
        if s == raw:
            cap = ""
        elif raw < 0:
            cap = f" ⟨Untergrenze, roh {raw}⟩"
        else:
            cap = f" ⟨gedeckelt von {raw}⟩"
        out.append(
            f"| {i} | **{g['titel']}** | `{g['doc'].replace('doc-','')}` | "
            f"{g['luecken_typ'].replace('_',' ')} | "
            + " | ".join(str(int(g.get(k, 0))) for k in ("A", "B", "C", "D", "E"))
            + f" | **{s}**{cap} | {raw} |")
    out.append("")

    by_type = {}
    for s, _r, g in scored:
        by_type.setdefault(g["luecken_typ"], []).append(s)
    out.append("**Verteilung nach Lückentyp:** "
               + " · ".join(f"{t.replace('_',' ')}: n={len(v)}, Ø {sum(v)/len(v):.1f}"
                            for t, v in sorted(by_type.items(),
                                               key=lambda kv: -sum(kv[1]) / len(kv[1]))))
    top = [g["doc"].replace("doc-", "") for s, _r, g in scored if s == scored[0][0]]
    zeros = [g["doc"].replace("doc-", "") for s, _r, g in scored if s == 0]
    out.append("")
    out.append(f"**Kennzahlen:** {len(scored)} erfasste Lücken · Höchstwert {scored[0][0]} "
               f"(Dok. {', '.join(top)}) · Score 0 bei Dok. {', '.join(zeros)}.")
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(description="Near-Miss-Ranking erzeugen")
    p.add_argument("--stdout", action="store_true")
    args = p.parse_args(argv)

    table = render(load())
    if args.stdout:
        print(table)
        return
    text = TARGET.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        raise SystemExit(f"Marker fehlen in {TARGET}")
    pre, rest = text.split(BEGIN, 1)
    _, post = rest.split(END, 1)
    TARGET.write_text(pre + BEGIN + "\n\n" + table + "\n\n" + END + post, encoding="utf-8")
    print(f"Near-Miss-Tabelle geschrieben nach {TARGET.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
