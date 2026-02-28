"""Test suite for knowledge graph integrity and connectivity."""
import json
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def test_edges_integrity():
    """Verify all IDs in edges.json point to existing card files."""
    edges_path = ROOT / "edges.json"
    if not edges_path.exists():
        pytest.skip("edges.json not found")
        
    with open(edges_path) as f:
        edges = json.load(f)
        
    cards_dir = ROOT / "cards"
    for edge in edges:
        source = cards_dir / f"{edge['source']}.md"
        target = cards_dir / f"{edge['target']}.md"
        
        assert source.exists(), f"Source card not found: {edge['source']}"
        assert target.exists(), f"Target card not found: {edge['target']}"

def test_circular_dependencies_report():
    """Report cycles in edges.json. 
    Note: These are currently allowed in the app but reported here for awareness."""
    edges_path = ROOT / "edges.json"
    if not edges_path.exists():
        pytest.skip("edges.json not found")
        
    with open(edges_path) as f:
        edges = json.load(f)
        
    adj = {}
    for edge in edges:
        s, t = edge["source"], edge["target"]
        if s not in adj: adj[s] = []
        adj[s].append(t)
        
    cycles = []
    def find_cycle(u, visited, stack, path):
        visited.add(u)
        stack.add(u)
        path.append(u)
        for v in adj.get(u, []):
            if v in stack:
                cycles.append(" -> ".join(path[path.index(v):] + [v]))
            elif v not in visited:
                find_cycle(v, visited, stack, path)
        stack.remove(u)
        path.pop()

    visited = set()
    for node in list(adj.keys()):
        if node not in visited:
            find_cycle(node, visited, set(), [])
            
    if cycles:
        print(f"\n[INFO] {len(cycles)} cycles detected in knowledge graph:")
        for c in cycles:
            print(f"  {c}")
    
    # We don't assert False here because cycles are permitted by the current design
    # but we could if we wanted a strictly acyclic graph.
