"""
formal.py — Brücke zur formalen Verifikation (Lean 4 / mathlib).

Lean ist die einzige Schicht, in der ein Beweisschritt MASCHINELL geprüft wird
(kein Halluzinationsrisiko). Dieses Modul:
  - liefert die formale RH-Aussage (mathlib) + Setup-Anleitung,
  - prüft Lean-Code, FALLS eine Lean-Toolchain (lean/lake) installiert ist,
  - degradiert sonst ehrlich zu Anleitung statt Fake-Ergebnis.
"""
import os, shutil, subprocess, tempfile

RH_STATEMENT_LEAN = r"""
-- Formale Aussage der Riemann-Vermutung (mathlib-nah, schematisch)
-- mathlib enthält `riemannZeta` und eine `RiemannHypothesis`-Formulierung.
import Mathlib.NumberTheory.LSeries.RiemannZeta

theorem riemann_hypothesis_statement :
    ∀ s : ℂ, riemannZeta s = 0 → s.re = 1 / 2 ∨ ∃ n : ℕ, s = -2 * (n + 1) := by
  sorry  -- offen: vollständiger Beweis (Millennium-Problem)
""".strip()

def formal_statement():
    """Gibt die formale RH-Aussage in Lean + Erläuterung zurück."""
    return {
        "lean": RH_STATEMENT_LEAN,
        "explanation": ("Jede Nullstelle ist entweder kritisch (Re=1/2) oder trivial (-2,-4,…). "
                        "'sorry' markiert die offene Stelle. In mathlib ist die RH als Statement "
                        "vorhanden; der Beweis ist offen (siehe docs/37)."),
        "setup": ["elan/Lean 4 installieren (https://leanprover-community.github.io)",
                  "lake new rh_project; mathlib als Abhängigkeit hinzufügen",
                  "obige Datei als RH.lean ablegen; 'lake build' prüft sie"],
        "see": "docs/37_formalization_lean_proof_assistants.md",
    }

def lean_available():
    return shutil.which("lean") is not None or shutil.which("lake") is not None

def lean_check(code):
    """Prüft Lean-Code, falls Toolchain vorhanden. Sonst ehrliche Statusmeldung."""
    if not lean_available():
        return {"lean_available": False,
                "status": "skipped",
                "message": ("Keine Lean-Toolchain gefunden. Code NICHT geprüft. "
                            "Zur echten Verifikation Lean 4 + mathlib installieren (siehe formal_statement.setup)."),
                "code_received_chars": len(code)}
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".lean", delete=False, encoding="utf-8") as f:
            f.write(code); path = f.name
        proc = subprocess.run(["lean", path], capture_output=True, text=True, timeout=120)
        ok = proc.returncode == 0
        return {"lean_available": True, "status": "ok" if ok else "error",
                "returncode": proc.returncode,
                "stdout": proc.stdout[-4000:], "stderr": proc.stderr[-4000:]}
    except subprocess.TimeoutExpired:
        return {"lean_available": True, "status": "timeout"}
    except Exception as e:
        return {"lean_available": True, "status": "exception", "error": str(e)}
    finally:
        try: os.unlink(path)
        except Exception: pass
