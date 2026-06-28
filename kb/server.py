#!/usr/bin/env python3
"""
server.py — MCP-Server, der den RH-Wissensgraphen als Tools bereitstellt.

Benötigt das offizielle MCP-Python-SDK:  pip install "mcp[cli]"
Start (stdio):  python3 kb/server.py
In Claude/MCP-Clients als Server registrieren (Beispiel siehe kb/README.md).

Falls das SDK fehlt, nutze stattdessen kb/query.py (gleiche Logik, CLI).
Vor dem ersten Start einmal:  python3 kb/build_kb.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core

try:
    from mcp.server.fastmcp import FastMCP
except Exception:
    sys.stderr.write(
        "FEHLER: MCP-SDK nicht installiert. 'pip install \"mcp[cli]\"' oder kb/query.py nutzen.\n")
    raise

mcp = FastMCP("riemann-hypothesis-kb")

@mcp.tool()
def search(query: str, k: int = 6, status: str = "", category: str = "") -> dict:
    """Hybride BM25-Suche über die RH-Wissensbasis, angereichert um Graph-Nachbarn
    (äquivalente/widerlegende/verwandte Knoten). status/category optional filtern
    (status: proven|open|refuted|reference|meta)."""
    return core.search(query, k=k, status=status or None, category=category or None)

@mcp.tool()
def get_document(node_id: str) -> dict:
    """Volles Markdown eines Dokuments (z. B. 'doc-10') inkl. Metadaten und Graph-Nachbarn."""
    return core.get_document(node_id)

@mcp.tool()
def graph_neighbors(node_id: str, relation: str = "") -> dict:
    """Typisierte Nachbarn eines Knotens. relation optional, z. B. equivalent_to,
    implies, reduces_to, refuted_by, obstruction_for, models, blueprint_for."""
    return core.graph_neighbors(node_id, relation or None)

@mcp.tool()
def find_path(node_a: str, node_b: str, max_depth: int = 5) -> dict:
    """Kürzester Beziehungspfad zwischen zwei Knoten (z. B. doc-19 -> concept-RH)."""
    return core.find_path(node_a, node_b, max_depth)

@mcp.tool()
def list_by_status(status: str) -> dict:
    """Dokumente + atomare Claims nach Status: proven | open | refuted | reference | meta."""
    return core.list_by_status(status)

@mcp.tool()
def get_claim(query: str) -> dict:
    """Atomare mathematische Aussagen mit STATUS (proven/open/refuted) zu einem Stichwort.
    Verhindert, dass widerlegte Aussagen (z. B. Mertens-Vermutung) als wahr behandelt werden."""
    return core.get_claim(query)

@mcp.tool()
def evaluate_proof_idea(idea: str) -> dict:
    """Prüft eine vorgeschlagene RH-Beweisidee gegen die bekannten Obstruktionen
    (Euler-Produkt, Positivität, kanonischer Operator, Numerik, Voronin) und gibt
    eine Checkliste + Warnungen zurück (Doc 35/41/43/46/37)."""
    return core.evaluate_proof_idea(idea)

@mcp.tool()
def kb_stats() -> dict:
    """Kennzahlen der Wissensbasis (Chunks, Knoten, Kanten, Claims, Status-Verteilung)."""
    return core.stats()

@mcp.tool()
def reasoning_scaffold(task: str = "") -> dict:
    """Liefert das verbindliche 7-Schritte-Denkprotokoll (docs/50), auf die Aufgabe
    zugeschnitten. IMMER zuerst aufrufen, bevor an einem RH-Problem gearbeitet wird —
    erzwingt Klassifikation, Annahmen, Status-Trennung, Obstruktions-Check, Experiment."""
    return core.reasoning_scaffold(task)

# ---------------- Numerische & grafische Tools (mpmath / matplotlib) ----------------
try:
    import compute as _cp
    import visualize as _vz
    _NUM = True
except Exception as _e:
    _NUM = False

if _NUM:
    @mcp.tool()
    def compute_zeta(sigma: float, t: float = 0.0) -> dict:
        """ζ(σ+it) numerisch (mpmath, 30 Stellen)."""
        return _cp.zeta(sigma, t)

    @mcp.tool()
    def compute_nth_zero(n: int) -> dict:
        """n-te nicht-triviale Nullstelle ρ=1/2+iγ (mpmath.zetazero)."""
        return _cp.nth_zero(n)

    @mcp.tool()
    def compute_first_zeros(count: int = 10) -> dict:
        """Erste `count` Nullstellen (γ-Werte) + Check, ob alle auf Re=1/2."""
        return _cp.first_zeros(count)

    @mcp.tool()
    def compute_verify_rh_range(n_start: int = 1, n_end: int = 50) -> dict:
        """Numerische Evidenz: liegen Nullstellen n_start..n_end auf Re=1/2? (KEIN Beweis, docs/35)."""
        return _cp.verify_rh_range(n_start, n_end)

    @mcp.tool()
    def compute_count_zeros(T: float) -> dict:
        """N(T): exakte Anzahl Nullstellen mit γ≤T vs. glatte Riemann-von-Mangoldt-Näherung."""
        return _cp.count_zeros(T)

    @mcp.tool()
    def compute_li_coefficient(n: int, num_zeros: int = 2000) -> dict:
        """Li-Koeffizient λ_n (RH ⟺ λ_n≥0 ∀n, docs/14). n=1 exakt, n≥2 Näherung."""
        return _cp.li_coefficient(n, num_zeros)

    @mcp.tool()
    def compute_psi_explicit(x: float, num_zeros: int = 200) -> dict:
        """Explizite Formel ψ(x)≈x−Σ_ρ x^ρ/ρ−… (zeigt, wie Nullstellen Primzahlen steuern, docs/02)."""
        return _cp.psi_explicit(x, num_zeros)

    @mcp.tool()
    def plot_hardy_Z(t0: float = 0.0, t1: float = 50.0) -> dict:
        """Plot der Hardyschen Z(t) mit markierten Nullstellen. Gibt PNG-Pfad zurück."""
        return {"path": _vz.plot_Z_and_zeros(t0, t1)}

    @mcp.tool()
    def plot_zeros_on_line(count: int = 30) -> dict:
        """Plot der ersten `count` Nullstellen auf der kritischen Geraden. PNG-Pfad."""
        return {"path": _vz.plot_zeros_on_line(count)}

    @mcp.tool()
    def plot_zeta_strip(t0: float = 0.5, t1: float = 40.0) -> dict:
        """Heatmap log|ζ(σ+it)| im kritischen Streifen. PNG-Pfad."""
        return {"path": _vz.plot_zeta_abs_strip(t0, t1)}

    @mcp.tool()
    def plot_counting_N(T: float = 100.0) -> dict:
        """Plot N(T) exakt vs. glatte Näherung. PNG-Pfad."""
        return {"path": _vz.plot_counting_N(T)}

    @mcp.tool()
    def plot_pair_correlation(num_zeros: int = 300) -> dict:
        """Nullstellenabstände vs. GUE-Vorhersage (Random-Matrix-Evidenz, docs/06). PNG-Pfad."""
        return {"path": _vz.plot_pair_correlation(num_zeros)}

    @mcp.tool()
    def plot_li_coefficients(n_max: int = 12) -> dict:
        """λ_n für n=1..n_max (RH ⟺ alle ≥0, docs/14). PNG-Pfad."""
        return {"path": _vz.plot_li_coefficients(n_max)}

    @mcp.tool()
    def plot_psi_convergence(x: float = 30.0, max_zeros: int = 150) -> dict:
        """Konvergenz der expliziten ψ(x)-Formel mit Zahl der Nullstellen (docs/02). PNG-Pfad."""
        return {"path": _vz.plot_psi_convergence(x, max_zeros)}

# ---------------- Experiment-Logbuch ----------------
try:
    import experiment as _ex
    _LOG = True
except Exception:
    _LOG = False

if _LOG:
    @mcp.tool()
    def log_experiment(hypothesis: str, method: str, params: dict,
                       result: dict, conclusion: str = "", tags: list = None) -> dict:
        """Speichert ein Experiment reproduzierbar (JSON+Markdown) für die Zusammenarbeit."""
        return _ex.log_experiment(hypothesis, method, params, result, conclusion, tags)

    @mcp.tool()
    def list_experiments() -> dict:
        """Listet alle protokollierten Experimente."""
        return _ex.list_experiments()

    @mcp.tool()
    def get_experiment(experiment_id: str) -> dict:
        """Holt ein Experiment per ID."""
        return _ex.get_experiment(experiment_id)

# ---------------- Formale Verifikation (Lean) ----------------
try:
    import formal as _fm
    _FORMAL = True
except Exception:
    _FORMAL = False

if _FORMAL:
    @mcp.tool()
    def formal_statement() -> dict:
        """Formale RH-Aussage in Lean 4/mathlib + Setup-Anleitung (docs/37)."""
        return _fm.formal_statement()

    @mcp.tool()
    def lean_check(code: str) -> dict:
        """Prüft Lean-Code maschinell, FALLS eine Lean-Toolchain installiert ist (sonst ehrliche
        Statusmeldung). Die einzige Schicht ohne Halluzinationsrisiko."""
        return _fm.lean_check(code)

if __name__ == "__main__":
    mcp.run()
