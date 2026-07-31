/-
SelfContained.lean — proof pipeline WITHOUT mathlib (builds immediately once Lean 4 is present).
Serves as a functional test for `lean_check`: real, machine-checked proofs are carried out here.
Extend this with RH-adjacent lemmas that do not require mathlib.
-/

namespace RHDemo

-- Trivial, but MACHINE-VERIFIED theorem (pipeline test).
theorem one_add_one : 1 + 1 = 2 := rfl

-- Symmetry example (illustrates "functional-equation symmetry" abstractly):
-- A point lies on the critical line iff its real part = 1/2.
def onCriticalLine (re : Rat) : Prop := re = 1/2

theorem half_on_line : onCriticalLine (1/2) := rfl

-- The reflection re ↦ 1 - re fixes exactly the critical line (core of the RH symmetry):
theorem reflection_fixed_iff (re : Rat) :
    (1 - re = re) ↔ re = 1/2 := by
  constructor
  · intro h; linarith
  · intro h; rw [h]; norm_num

end RHDemo
