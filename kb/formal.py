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

_ELAN_BIN = os.path.expanduser("~/.elan/bin")

def _lean_path():
    """lean-Binary finden (PATH oder ~/.elan/bin)."""
    p = shutil.which("lean")
    if p:
        return p
    cand = os.path.join(_ELAN_BIN, "lean")
    return cand if os.path.exists(cand) else None

def formal_statement():
    """Gibt die formale RH-Aussage in Lean + Erläuterung + Projekt-Gerüst zurück."""
    scaffold = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lean")
    return {
        "lean": RH_STATEMENT_LEAN,
        "explanation": ("Jede Nullstelle ist entweder kritisch (Re=1/2) oder trivial (-2,-4,…). "
                        "'sorry' markiert die offene Stelle. In mathlib ist die RH als Statement "
                        "vorhanden; der Beweis ist offen (siehe docs/37)."),
        "project_scaffold": scaffold,
        "scaffold_files": ["RH/SelfContained.lean (ohne mathlib, baut sofort)",
                           "RH/Statement.lean (RH-Aussage, braucht mathlib)",
                           "lakefile.toml", "lean-toolchain", "README.md"],
        "setup": ["curl .../elan-init.sh | sh -s -- -y   (Lean 4 + elan)",
                  "cd kb/lean && lean RH/SelfContained.lean   (sofortiger Test, kein mathlib)",
                  "lake exe cache get && lake build   (volles Projekt mit mathlib)"],
        "see": "docs/37_formalization_lean_proof_assistants.md, kb/lean/README.md",
    }

def lean_status():
    """Ehrlicher Toolchain-Status."""
    lean = _lean_path()
    elan = shutil.which("elan") or (os.path.join(_ELAN_BIN, "elan")
                                    if os.path.exists(os.path.join(_ELAN_BIN, "elan")) else None)
    toolchain = False
    if lean:
        try:
            r = subprocess.run([lean, "--version"], capture_output=True, text=True, timeout=20)
            toolchain = (r.returncode == 0)
        except Exception:
            toolchain = False
    return {"elan_installed": bool(elan), "lean_binary": lean,
            "toolchain_usable": toolchain}

def lean_available():
    st = lean_status()
    return st["toolchain_usable"]

def lean_check(code):
    """Prüft Lean-Code, falls Toolchain vorhanden. Sonst ehrliche Statusmeldung."""
    lean = _lean_path()
    if not lean_available():
        st = lean_status()
        return {"lean_available": False, "status": "skipped", "lean_status": st,
                "message": ("Lean-Toolchain nicht nutzbar (Code NICHT geprüft). "
                            + ("elan ist installiert, aber der Toolchain-Download ist blockiert. "
                               if st["elan_installed"] else "Lean 4 ist nicht installiert. ")
                            + "Lokal bauen: siehe kb/lean/README.md."),
                "code_received_chars": len(code)}
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".lean", delete=False, encoding="utf-8") as f:
            f.write(code); path = f.name
        proc = subprocess.run([lean, path], capture_output=True, text=True, timeout=120)
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
