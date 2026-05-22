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

    adj: dict[str, list[str]] = {}
    for edge in edges:
        s, t = edge["source"], edge["target"]
        adj.setdefault(s, []).append(t)

    cycles: list[str] = []

    def find_cycle(u: str, visited: set, stack: set, stack_path: list) -> None:
        """Iterative-safe DFS that tracks the exact stack path for cycle reporting."""
        visited.add(u)
        stack.add(u)
        stack_path.append(u)
        for v in adj.get(u, []):
            if v in stack:
                # v is on the current DFS stack — find it there, not in visited set
                start = stack_path.index(v)
                cycles.append(" -> ".join(stack_path[start:] + [v]))
            elif v not in visited:
                find_cycle(v, visited, stack, stack_path)
        stack.discard(u)
        stack_path.pop()

    visited: set[str] = set()
    for node in list(adj.keys()):
        if node not in visited:
            find_cycle(node, visited, set(), [])

    if cycles:
        print(f"\n[INFO] {len(cycles)} cycles detected in knowledge graph:")
        for c in cycles:
            print(f"  {c}")

    # Cycles are permitted by the current design — this test reports but does not fail.
