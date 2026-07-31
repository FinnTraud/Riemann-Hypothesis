"""
formal.py — Bridge to formal verification (Lean 4 / mathlib).

Lean is the only layer in which a proof step is checked BY MACHINE
(no hallucination risk). This module:
  - provides the formal RH statement (mathlib) + setup instructions,
  - checks Lean code IF a Lean toolchain (lean/lake) is installed,
  - otherwise degrades honestly to instructions instead of a fake result.
"""
import os, shutil, subprocess, tempfile

RH_STATEMENT_LEAN = r"""
-- Formal statement of the Riemann Hypothesis (mathlib-style, schematic)
-- mathlib contains `riemannZeta` and a `RiemannHypothesis` formulation.
import Mathlib.NumberTheory.LSeries.RiemannZeta

theorem riemann_hypothesis_statement :
    ∀ s : ℂ, riemannZeta s = 0 → s.re = 1 / 2 ∨ ∃ n : ℕ, s = -2 * (n + 1) := by
  sorry  -- open: full proof (Millennium Problem)
""".strip()

_ELAN_BIN = os.path.expanduser("~/.elan/bin")

def _lean_path():
    """Find the lean binary (PATH or ~/.elan/bin)."""
    p = shutil.which("lean")
    if p:
        return p
    cand = os.path.join(_ELAN_BIN, "lean")
    return cand if os.path.exists(cand) else None

def formal_statement():
    """Returns the formal RH statement in Lean + explanation + project scaffold."""
    scaffold = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lean")
    return {
        "lean": RH_STATEMENT_LEAN,
        "explanation": ("Every zero is either critical (Re=1/2) or trivial (-2,-4,…). "
                        "'sorry' marks the open spot. mathlib contains the RH as a statement; "
                        "the proof is open (see docs/37)."),
        "project_scaffold": scaffold,
        "scaffold_files": ["RH/SelfContained.lean (without mathlib, builds immediately)",
                           "RH/Statement.lean (RH statement, needs mathlib)",
                           "lakefile.toml", "lean-toolchain", "README.md"],
        "setup": ["curl .../elan-init.sh | sh -s -- -y   (Lean 4 + elan)",
                  "cd kb/lean && lean RH/SelfContained.lean   (instant test, no mathlib)",
                  "lake exe cache get && lake build   (full project with mathlib)"],
        "see": "docs/37_formalization_lean_proof_assistants.md, kb/lean/README.md",
    }

def lean_status():
    """Honest toolchain status."""
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
    """Checks Lean code if a toolchain is present. Otherwise an honest status message."""
    lean = _lean_path()
    if not lean_available():
        st = lean_status()
        return {"lean_available": False, "status": "skipped", "lean_status": st,
                "message": ("Lean toolchain not usable (code NOT checked). "
                            + ("elan is installed, but the toolchain download is blocked. "
                               if st["elan_installed"] else "Lean 4 is not installed. ")
                            + "Build locally: see kb/lean/README.md."),
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
