#!/usr/bin/env python3
"""
server.py — MCP server that exposes the RH knowledge graph as tools.

Requires the official MCP Python SDK:  pip install "mcp[cli]"
Start (stdio):  python3 kb/server.py
Register as a server in Claude/MCP clients (see kb/README.md for an example).

If the SDK is missing, use kb/query.py instead (same logic, CLI).
Run once before the first start:  python3 kb/build_kb.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core

try:
    from mcp.server.fastmcp import FastMCP
except Exception:
    sys.stderr.write(
        "ERROR: MCP SDK not installed. Use 'pip install \"mcp[cli]\"' or kb/query.py.\n")
    raise

mcp = FastMCP("riemann-hypothesis-kb")

@mcp.tool()
def search(query: str, k: int = 6, status: str = "", category: str = "") -> dict:
    """Hybrid BM25 search over the RH knowledge base, enriched with graph neighbors
    (equivalent/refuting/related nodes). status/category optional filters
    (status: proven|open|refuted|reference|meta)."""
    return core.search(query, k=k, status=status or None, category=category or None)

@mcp.tool()
def get_document(node_id: str) -> dict:
    """Full markdown of a document (e.g. 'doc-10') including metadata and graph neighbors."""
    return core.get_document(node_id)

@mcp.tool()
def graph_neighbors(node_id: str, relation: str = "") -> dict:
    """Typed neighbors of a node. relation optional, e.g. equivalent_to,
    implies, reduces_to, refuted_by, obstruction_for, models, blueprint_for."""
    return core.graph_neighbors(node_id, relation or None)

@mcp.tool()
def find_path(node_a: str, node_b: str, max_depth: int = 5) -> dict:
    """Shortest relation path between two nodes (e.g. doc-19 -> concept-RH)."""
    return core.find_path(node_a, node_b, max_depth)

@mcp.tool()
def list_by_status(status: str) -> dict:
    """Documents + atomic claims by status: proven | open | refuted | reference | meta."""
    return core.list_by_status(status)

@mcp.tool()
def get_claim(query: str) -> dict:
    """Atomic mathematical statements with STATUS (proven/open/refuted) for a keyword.
    Prevents refuted statements (e.g. the Mertens conjecture) from being treated as true."""
    return core.get_claim(query)

@mcp.tool()
def evaluate_proof_idea(idea: str) -> dict:
    """Checks a proposed RH proof idea against the known obstructions
    (Euler product, positivity, canonical operator, numerics, Voronin) and returns
    a checklist + warnings (Doc 35/41/43/46/37)."""
    return core.evaluate_proof_idea(idea)

@mcp.tool()
def kb_stats() -> dict:
    """Knowledge-base metrics (chunks, nodes, edges, claims, status distribution)."""
    return core.stats()

@mcp.tool()
def reasoning_scaffold(task: str = "") -> dict:
    """Returns the mandatory 7-step reasoning protocol (docs/50), tailored to the task.
    ALWAYS call it first, before working on an RH problem —
    enforces classification, assumptions, status separation, obstruction check, experiment."""
    return core.reasoning_scaffold(task)

# ---------------- Numerical & graphical tools (mpmath / matplotlib) ----------------
try:
    import compute as _cp
    import visualize as _vz
    _NUM = True
except Exception as _e:
    _NUM = False

if _NUM:
    @mcp.tool()
    def compute_zeta(sigma: float, t: float = 0.0) -> dict:
        """ζ(σ+it) numerically (mpmath, 30 digits)."""
        return _cp.zeta(sigma, t)

    @mcp.tool()
    def compute_nth_zero(n: int) -> dict:
        """n-th non-trivial zero ρ=1/2+iγ (mpmath.zetazero)."""
        return _cp.nth_zero(n)

    @mcp.tool()
    def compute_first_zeros(count: int = 10) -> dict:
        """First `count` zeros (γ values) + check whether all lie on Re=1/2."""
        return _cp.first_zeros(count)

    @mcp.tool()
    def compute_verify_rh_range(n_start: int = 1, n_end: int = 50) -> dict:
        """Numerical evidence: do zeros n_start..n_end lie on Re=1/2? (NOT a proof, docs/35)."""
        return _cp.verify_rh_range(n_start, n_end)

    @mcp.tool()
    def compute_count_zeros(T: float) -> dict:
        """N(T): exact number of zeros with γ≤T vs. smooth Riemann–von Mangoldt approximation."""
        return _cp.count_zeros(T)

    @mcp.tool()
    def compute_li_coefficient(n: int, num_zeros: int = 2000) -> dict:
        """Li coefficient λ_n (RH ⟺ λ_n≥0 ∀n, docs/14). n=1 exact, n≥2 approximation."""
        return _cp.li_coefficient(n, num_zeros)

    @mcp.tool()
    def compute_psi_explicit(x: float, num_zeros: int = 200) -> dict:
        """Explicit formula ψ(x)≈x−Σ_ρ x^ρ/ρ−… (shows how zeros control the primes, docs/02)."""
        return _cp.psi_explicit(x, num_zeros)

    @mcp.tool()
    def plot_hardy_Z(t0: float = 0.0, t1: float = 50.0) -> dict:
        """Plot of the Hardy Z(t) with marked zeros. Returns the PNG path."""
        return {"path": _vz.plot_Z_and_zeros(t0, t1)}

    @mcp.tool()
    def plot_zeros_on_line(count: int = 30) -> dict:
        """Plot of the first `count` zeros on the critical line. PNG path."""
        return {"path": _vz.plot_zeros_on_line(count)}

    @mcp.tool()
    def plot_zeta_strip(t0: float = 0.5, t1: float = 40.0) -> dict:
        """Heatmap of log|ζ(σ+it)| in the critical strip. PNG path."""
        return {"path": _vz.plot_zeta_abs_strip(t0, t1)}

    @mcp.tool()
    def plot_counting_N(T: float = 100.0) -> dict:
        """Plot N(T) exact vs. smooth approximation. PNG path."""
        return {"path": _vz.plot_counting_N(T)}

    @mcp.tool()
    def plot_pair_correlation(num_zeros: int = 300) -> dict:
        """Zero spacings vs. GUE prediction (random-matrix evidence, docs/06). PNG path."""
        return {"path": _vz.plot_pair_correlation(num_zeros)}

    @mcp.tool()
    def plot_li_coefficients(n_max: int = 12) -> dict:
        """λ_n for n=1..n_max (RH ⟺ all ≥0, docs/14). PNG path."""
        return {"path": _vz.plot_li_coefficients(n_max)}

    @mcp.tool()
    def plot_psi_convergence(x: float = 30.0, max_zeros: int = 150) -> dict:
        """Convergence of the explicit ψ(x) formula with the number of zeros (docs/02). PNG path."""
        return {"path": _vz.plot_psi_convergence(x, max_zeros)}

# ---------------- Experiment logbook ----------------
try:
    import experiment as _ex
    _LOG = True
except Exception:
    _LOG = False

if _LOG:
    @mcp.tool()
    def log_experiment(hypothesis: str, method: str, params: dict,
                       result: dict, conclusion: str = "", tags: list = None) -> dict:
        """Stores an experiment reproducibly (JSON+Markdown) for collaboration."""
        return _ex.log_experiment(hypothesis, method, params, result, conclusion, tags)

    @mcp.tool()
    def list_experiments() -> dict:
        """Lists all logged experiments."""
        return _ex.list_experiments()

    @mcp.tool()
    def get_experiment(experiment_id: str) -> dict:
        """Fetches an experiment by ID."""
        return _ex.get_experiment(experiment_id)

# ---------------- Formal verification (Lean) ----------------
try:
    import formal as _fm
    _FORMAL = True
except Exception:
    _FORMAL = False

if _FORMAL:
    @mcp.tool()
    def formal_statement() -> dict:
        """Formal RH statement in Lean 4/mathlib + setup instructions (docs/37)."""
        return _fm.formal_statement()

    @mcp.tool()
    def lean_check(code: str) -> dict:
        """Machine-checks Lean code IF a Lean toolchain is installed (otherwise an honest
        status message). The only layer without hallucination risk."""
        return _fm.lean_check(code)

    @mcp.tool()
    def lean_status() -> dict:
        """Honest status of the Lean toolchain (elan installed? lean usable?)."""
        return _fm.lean_status()

if __name__ == "__main__":
    mcp.run()
