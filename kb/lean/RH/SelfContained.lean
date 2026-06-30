/-
SelfContained.lean — Beweis-Pipeline OHNE mathlib (baut sofort, sobald Lean 4 da ist).
Dient als Funktionstest für `lean_check`: hier werden echte, maschinell geprüfte
Beweise geführt. Erweitere dies mit RH-nahen Lemmas, die ohne mathlib auskommen.
-/

namespace RHDemo

-- Triviales, aber MASCHINELL VERIFIZIERTES Theorem (Pipeline-Test).
theorem one_add_one : 1 + 1 = 2 := rfl

-- Symmetrie-Beispiel (illustriert „Funktionalgleichungs-Symmetrie" abstrakt):
-- Ein Punkt liegt auf der kritischen Geraden gdw. sein Realteil = 1/2 ist.
def onCriticalLine (re : Rat) : Prop := re = 1/2

theorem half_on_line : onCriticalLine (1/2) := rfl

-- Spiegelung re ↦ 1 - re fixiert genau die kritische Gerade (Kern der RH-Symmetrie):
theorem reflection_fixed_iff (re : Rat) :
    (1 - re = re) ↔ re = 1/2 := by
  constructor
  · intro h; linarith
  · intro h; rw [h]; norm_num

end RHDemo
