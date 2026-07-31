# Lean 4 project — formal verification (RH)

This layer is the **only one without hallucination risk**: Lean checks every proof step
by machine against the axioms.

## Build locally (where network access is allowed)
```bash
# Install Lean 4 + elan:
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y
source ~/.elan/env

# Check the self-contained part (NO mathlib needed, builds immediately):
cd kb/lean
lean RH/SelfContained.lean        # verifies 1+1=2, the reflection lemma, etc.

# Full project with mathlib (large download/cache on the first run):
lake exe cache get                # fetch the mathlib cache
lake build                        # builds RH.lean including Statement.lean
```

> Note: in some sandboxes the toolchain/mathlib download is blocked (HTTP 403).
> In that case build locally on your machine / the professor's machine.

## Files
- `RH/SelfContained.lean` — real, machine-checked proofs WITHOUT mathlib (pipeline test).
- `RH/Statement.lean` — formal RH statement with `sorry` (requires mathlib, `riemannZeta`).
- `RH.lean` — aggregate file.
- `lakefile.toml`, `lean-toolchain` — project configuration.

## Realistic contribution (with a professor)
1. Formalize a **criterion equivalent to the RH** (Λ≤0 docs/23, Li positivity docs/14)
   and prove the equivalence.
2. Formally reproduce **proven partial results** (Hardy docs/03, Rodgers–Tao Λ≥0 docs/23).
3. Every such step is **verified, publishable** progress — unlike
   informal "proofs" (see docs/27, docs/35).

Connection to the MCP server: `formal_statement` (statement + setup) and `lean_check` (checks
Lean code if a toolchain is present).
