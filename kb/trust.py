#!/usr/bin/env python3
"""Trust-Tiers: Verifikationsstufe je Claim auswerten (docs/64).

    T0-lean-verified   maschinell geprueft
    T1-kanonisch       Lehrbuchniveau, jahrzehntelang geprueft
    T2-peer-reviewed   referiert publiziert
    T3-preprint        arXiv / sehr jung, Begutachtungsstand offen
    T4-repo-numerik    in diesem Repo gerechnet, nicht extern verifiziert
    T5-konsens         Fachkonsens ohne referierte Arbeit

    python3 kb/trust.py            # Verteilung + Warnungen
    python3 kb/trust.py --tier T3  # nur eine Stufe
    python3 kb/trust.py --json
"""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "kb" / "graph" / "claims.json"
ORDER = ["T0-lean-verified", "T1-kanonisch", "T2-peer-reviewed",
         "T3-preprint", "T4-repo-numerik", "T5-konsens"]


def load():
    return json.loads(CLAIMS.read_text(encoding="utf-8"))["claims"]


def report():
    claims = load()
    dist = Counter(c.get("trust", "unbekannt") for c in claims)
    warn = []
    for c in claims:
        t = c.get("trust", "unbekannt")
        if c.get("status") == "proven" and t in ("T3-preprint", "T5-konsens"):
            warn.append({
                "claim": c["id"], "trust": t, "doc": c.get("doc"),
                "hinweis": ("Als 'proven' gefuehrt, aber die Quelle ist "
                            + ("ein Preprint" if t == "T3-preprint" else "blosser Konsens")
                            + " -- beim Zitieren kennzeichnen."),
            })
    return {
        "gesamt": len(claims),
        "verteilung": {t: dist.get(t, 0) for t in ORDER if dist.get(t)},
        "anteil_sekundaer": sum(1 for c in claims if c.get("zugang") == "sekundaer"),
        "eigene_rechnung": [c["id"] for c in claims if c.get("zugang") == "eigene_rechnung"],
        "warnungen": warn,
        "grundwarnung": ("Alle mit zugang='sekundaer' gefuehrten Claims wurden aus "
                         "Sekundaerdarstellungen erfasst -- die Primaerquelle wurde fuer "
                         "dieses Repo NICHT gelesen. Das ist die wichtigste Einschraenkung "
                         "der gesamten Wissensbasis (docs/64, docs/62)."),
        "siehe": "docs/64",
    }


def main(argv=None):
    p = argparse.ArgumentParser(description="Trust-Tiers auswerten")
    p.add_argument("--tier", default="", help="nur diese Stufe auflisten")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    if a.tier:
        rows = [c for c in load() if c.get("trust") == a.tier]
        if a.json:
            print(json.dumps(rows, indent=2, ensure_ascii=False)); return
        print(f"{len(rows)} Claims mit Stufe {a.tier}:\n")
        for c in rows:
            print(f"  {c['id']:38s} [{c['status']:8s}] {c.get('doc')}")
            print(f"     {c['statement'][:110]}")
            print(f"     Quelle: {c.get('source','-')[:100]}\n")
        return
    r = report()
    if a.json:
        print(json.dumps(r, indent=2, ensure_ascii=False)); return
    print(f"Claims gesamt: {r['gesamt']}\n")
    for t, n in r["verteilung"].items():
        print(f"  {t:20s} {n:3d}  {'█' * n}")
    print(f"\n  davon aus Sekundaerdarstellungen erfasst: {r['anteil_sekundaer']}")
    print(f"  davon in diesem Repo gerechnet:           {len(r['eigene_rechnung'])}")
    if r["warnungen"]:
        print(f"\n{len(r['warnungen'])} Warnung(en) — 'proven' auf schwacher Quellenstufe:")
        for w in r["warnungen"]:
            print(f"  - {w['claim']:40s} {w['trust']:18s} ({w['doc']})")
    print(f"\n! {r['grundwarnung']}")


if __name__ == "__main__":
    main()
