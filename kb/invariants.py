#!/usr/bin/env python3
"""Invarianten & Testvektoren: die Pruefliste, die ein RH-Beweis bestehen muss.

Zwei Sorten von Pruefungen (Daten in kb/graph/invariants.json, docs/59):

  TESTVEKTOREN      konkrete Funktionen mit BEKANNTEM Wahrheitswert des
                    RH-Analogons. Ein Argument muss sie korrekt klassifizieren.

  UEBERSCHUSS-TESTS bekannte WAHRHEITEN, die ein zu starkes Argument sofort
                    widerlegen. Wer nebenbei eine dieser Aussagen mitbeweist,
                    hat einen Fehler -- unabhaengig davon, ob man die Luecke
                    findet. Das ist die schaerfere Pruefung.

Bewusst KEIN Automatismus: die Frage "beweist Ihr Argument zu viel?" laesst
sich nicht durch Stichwortsuche entscheiden. Das Modul liefert deshalb die
Pruefliste in der Reihenfolge abnehmender Schaerfe, mit der jeweils
widerlegenden Tatsache -- zu beantworten von einem Menschen oder von einem
Modell, das den Beweistext tatsaechlich gelesen hat.

    python3 kb/invariants.py                # ganze Pruefliste
    python3 kb/invariants.py --testvektoren
    python3 kb/invariants.py --json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "kb" / "graph" / "invariants.json"
_SHARP = {"hoch": 0, "mittel": 1, "niedrig": 2}


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))


def testvectors():
    """Konkrete Funktionen mit bekanntem Wahrheitswert des RH-Analogons."""
    return load()["testvektoren"]


def overshoot_checks():
    """Ueberschuss-Tests, nach Schaerfe sortiert (schaerfste zuerst)."""
    return sorted(load()["ueberschuss_tests"],
                  key=lambda c: _SHARP.get(c.get("schaerfe", "mittel"), 1))


def checklist():
    """Vollstaendige Pruefliste als strukturiertes Dict (fuer MCP/Tools)."""
    tv = testvectors()
    ov = overshoot_checks()
    return {
        "anleitung": (
            "Schritt 1: Klassifiziert das Argument jeden Testvektor korrekt? "
            "Ein Argument, das die Davenport-Heilbronn-Funktion oder die "
            "Epstein-Zeta als RH-konform durchwinkt, ist widerlegt. "
            "Schritt 2: Beweist das Argument zu viel? Jede mitbewiesene "
            "bekannte Unwahrheit ist ein Fehlerbeweis -- ohne dass man die "
            "fehlerhafte Zeile finden muss."),
        "testvektoren": tv,
        "ueberschuss_tests": ov,
        "gegenbeispiele_mit_falschem_rh_analogon": [
            t["name"] for t in tv if t["rh_analogon"].startswith("FALSCH")],
        "bewiesene_analoga": [
            t["name"] for t in tv if t["rh_analogon"].startswith("WAHR")],
        "maschinell_pruefbar": [c["id"] for c in ov if c.get("orakel_test")],
        "siehe": ["docs/59", "docs/35", "docs/60", "kb/counterexample.py"],
    }


def _print_human(data, only_tv=False):
    print("=" * 78)
    print("TESTVEKTOREN — Funktionen mit bekanntem Wahrheitswert des RH-Analogons")
    print("=" * 78)
    for t in data["testvektoren"]:
        mark = {"FALSCH": "✗", "WAHR": "✓"}.get(t["rh_analogon"].split()[0], "?")
        print(f"\n[{mark}] {t['name']}   ({t['doc']})")
        print(f"    RH-Analogon:     {t['rh_analogon']}")
        print(f"    Euler-Produkt:   {'ja' if t['hat_euler_produkt'] else 'NEIN'}"
              f"   Funktionalgleichung: {'ja' if t['hat_funktionalgleichung'] else 'nein'}")
        print(f"    Muss gelten:     {t['muss_klassifiziert_werden_als']}")
        if t.get("orakel"):
            print(f"    Prüfbar mit:     {t['orakel']}")
        if t.get("bemerkung"):
            print(f"    → {t['bemerkung']}")
    if only_tv:
        return
    print("\n" + "=" * 78)
    print("ÜBERSCHUSS-TESTS — beweist Ihr Argument zu viel?")
    print("=" * 78)
    print("Jede hier mitbewiesene Aussage widerlegt das Argument, ohne dass man")
    print("die fehlerhafte Zeile finden muss.\n")
    for i, c in enumerate(data["ueberschuss_tests"], 1):
        print(f"{i:2d}. [{c['schaerfe']:6s}] {c['frage']}   ({c['doc']})")
        print(f"    Bekannte Wahrheit: {c['bekannte_wahrheit']}")
        print(f"    Konsequenz:        {c['konsequenz']}")
        if c.get("orakel_test"):
            print(f"    Maschinell:        kb/counterexample.py → {c['orakel_test']}")
        print()


def main(argv=None):
    p = argparse.ArgumentParser(description="Invarianten & Testvektoren für RH-Beweisideen")
    p.add_argument("--testvektoren", action="store_true", help="nur die Testvektoren")
    p.add_argument("--json", action="store_true", help="maschinenlesbar ausgeben")
    args = p.parse_args(argv)
    data = checklist()
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        _print_human(data, only_tv=args.testvektoren)


if __name__ == "__main__":
    main()
