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

if __name__ == "__main__":
    mcp.run()
