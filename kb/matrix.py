#!/usr/bin/env python3
"""Erzeugt die Obstruktions x Ansatz-Matrix aus kb/graph/blockers.json.

Die Matrix wird in docs/55_failure_taxonomy.md zwischen die Marker
<!-- MATRIX:BEGIN --> und <!-- MATRIX:END --> geschrieben (idempotent).

    python3 kb/matrix.py            # schreibt in docs/55, gibt Statistik aus
    python3 kb/matrix.py --stdout   # nur ausgeben, nichts schreiben
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCKERS = ROOT / "kb" / "graph" / "blockers.json"
MANIFEST = ROOT / "manifest.json"
TARGET = ROOT / "docs" / "55_failure_taxonomy.md"
BEGIN = "<!-- MATRIX:BEGIN (generiert von kb/matrix.py -- nicht von Hand editieren) -->"
END = "<!-- MATRIX:END -->"

#: kompakte Spaltenkuerzel in Tier-Reihenfolge
SHORT = {
    "blk-euler-blindness": "EUL",
    "blk-parity": "PAR",
    "blk-softness": "SOFT",
    "blk-positivity-circular": "POS",
    "blk-noncanonical-operator": "OP",
    "blk-missing-base-geometry": "GEO",
    "blk-limit-interchange": "LIM",
    "blk-proportion-ceiling": "PROP",
    "blk-finite-evidence": "NUM",
    "blk-model-circularity": "MOD",
    "blk-equivalence-trap": "AEQ",
    "blk-unverifiable": "VER",
}


def load():
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))["blockers"]
    docs = json.loads(MANIFEST.read_text(encoding="utf-8"))["documents"]
    titles = {}
    for d in docs:
        did = d.get("id") or f"doc-{d.get('number'):02d}"
        titles[did] = d.get("title", did)
    return blockers, titles


def build_rows(blockers, titles):
    """doc-id -> Menge der Blocker-IDs, die es treffen."""
    hit = {}
    for b in blockers:
        for doc in b["betrifft"]:
            hit.setdefault(doc, set()).add(b["id"])
    return dict(sorted(hit.items(), key=lambda kv: kv[0]))


def short_title(t, n=44):
    t = t.split("(")[0].split(":")[0].split("—")[0].strip().strip('"')
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def render(blockers, titles):
    order = [b["id"] for b in sorted(blockers, key=lambda b: (b["tier"], b["id"]))]
    cols = [SHORT.get(b, b[4:8].upper()) for b in order]
    tiers = {b["id"]: b["tier"] for b in blockers}
    rows = build_rows(blockers, titles)

    out = []
    out.append("**Lesart:** ● = dieser Blocker trifft den Ansatz. Spalten nach Tier "
               "sortiert (Tier 1 links). Zeilen nur für Dokumente, die mindestens "
               "einen Blocker tragen — reine Referenz-, Glossar- und Meta-Dokumente "
               "fehlen daher bewusst.\n")
    out.append("| Dok | Ansatz | " + " | ".join(
        f"{c}<br><sub>T{tiers[b]}</sub>" for b, c in zip(order, cols)) + " | Σ |")
    out.append("|---|---|" + "---|" * (len(order) + 1))
    for doc, hits in rows.items():
        num = doc.replace("doc-", "")
        cells = ["●" if b in hits else "" for b in order]
        out.append(f"| `{num}` | {short_title(titles.get(doc, doc))} | "
                   + " | ".join(cells) + f" | **{len(hits)}** |")
    counts = Counter()
    for hits in rows.values():
        counts.update(hits)
    out.append("| | **Σ Ansätze je Blocker** | "
               + " | ".join(f"**{counts.get(b, 0)}**" for b in order)
               + f" | **{sum(counts.values())}** |")

    out.append("")
    out.append("**Spaltenlegende:** "
               + " · ".join(f"`{c}` = {next(x['name'] for x in blockers if x['id'] == b)}"
                            for b, c in zip(order, cols)))
    out.append("")
    top = counts.most_common(3)
    multi = sorted(((len(h), d) for d, h in rows.items()), reverse=True)[:4]
    out.append(f"**Kennzahlen (automatisch):** {len(rows)} Ansätze tragen zusammen "
               f"{sum(counts.values())} Blocker-Zuordnungen bei {len(order)} Blockern "
               f"— im Mittel {sum(counts.values())/len(rows):.1f} Blocker pro Ansatz. "
               f"Häufigster Blocker: **{next(x['name'] for x in blockers if x['id']==top[0][0])}** "
               f"({top[0][1]} Ansätze). "
               "Am stärksten blockierte Ansätze: "
               + ", ".join(f"`{d.replace('doc-','')}` ({n})" for n, d in multi) + ".")
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(description="Obstruktions x Ansatz-Matrix erzeugen")
    p.add_argument("--stdout", action="store_true", help="nur ausgeben, Datei nicht ändern")
    args = p.parse_args(argv)

    blockers, titles = load()
    table = render(blockers, titles)
    if args.stdout:
        print(table)
        return

    text = TARGET.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        raise SystemExit(f"Marker fehlen in {TARGET}")
    pre, rest = text.split(BEGIN, 1)
    _, post = rest.split(END, 1)
    TARGET.write_text(pre + BEGIN + "\n\n" + table + "\n\n" + END + post, encoding="utf-8")
    print(f"Matrix geschrieben nach {TARGET.relative_to(ROOT)} "
          f"({len(build_rows(blockers, titles))} Zeilen, {len(blockers)} Spalten).")


if __name__ == "__main__":
    main()
