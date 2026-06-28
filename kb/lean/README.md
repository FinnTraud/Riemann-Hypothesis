# Lean 4 Projekt — formale Verifikation (RH)

Diese Schicht ist die **einzige ohne Halluzinationsrisiko**: Lean prüft jeden Beweisschritt
maschinell gegen die Axiome.

## Lokal bauen (dort, wo Netzwerkzugriff erlaubt ist)
```bash
# Lean 4 + elan installieren:
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y
source ~/.elan/env

# Selbst-enthaltenen Teil prüfen (KEIN mathlib nötig, baut sofort):
cd kb/lean
lean RH/SelfContained.lean        # verifiziert 1+1=2, Spiegelungs-Lemma etc.

# Volles Projekt mit mathlib (großer Download/Cache beim ersten Mal):
lake exe cache get                # mathlib-Cache holen
lake build                        # baut RH.lean inkl. Statement.lean
```

> Hinweis: In manchen Sandboxes ist der Toolchain-/mathlib-Download geblockt (HTTP 403).
> Dann lokal bei dir / beim Professor bauen.

## Dateien
- `RH/SelfContained.lean` — echte, maschinell geprüfte Beweise OHNE mathlib (Pipeline-Test).
- `RH/Statement.lean` — formale RH-Aussage mit `sorry` (benötigt mathlib, `riemannZeta`).
- `RH.lean` — Sammeldatei.
- `lakefile.toml`, `lean-toolchain` — Projektkonfiguration.

## Realistischer Beitrag (mit Professor)
1. Ein **zur RH äquivalentes Kriterium** formalisieren (Λ≤0 docs/23, Li-Positivität docs/14)
   und die Äquivalenz beweisen.
2. **Bewiesene Teilresultate** formal nachziehen (Hardy docs/03, Rodgers–Tao Λ≥0 docs/23).
3. Jeder solche Schritt ist **verifizierter, publizierbarer** Fortschritt — anders als
   informelle „Beweise" (siehe docs/27, docs/35).

Anbindung an den MCP-Server: `formal_statement` (Aussage + Setup) und `lean_check` (prüft
Lean-Code, falls Toolchain vorhanden).
