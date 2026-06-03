# Union-Find

**Topic:** Computational Finance
**Tags:** union-find, disjoint set, cycle detection, kruskal, data structure, graph algorithm
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Union-Find (Disjoint Set Union) is a data structure that tracks which elements belong to the same connected component, supporting near-constant-time `Find` (which component?) and `Union` (merge two components) operations used in Kruskal's algorithm to detect cycles during MST construction.

## Key Formula

Two optimisations bring the per-operation cost to $O(\alpha(N))$ — effectively $O(1)$ for all practical $N$, where $\alpha$ is the inverse Ackermann function:

- **Path compression** (`Find`): on each call, re-attach all nodes along the path directly to the root, flattening the tree for future queries.
- **Union by rank** (`Union`): always attach the root of the smaller tree under the root of the larger tree, bounding tree height at $O(\log N)$.

Without both optimisations, `Find` degenerates to $O(N)$ per call in the worst case, turning Kruskal's total complexity from $O(N^2 \log N)$ to $O(N^3)$.

## Example

Five assets A–E, initially separate: $\{A\}, \{B\}, \{C\}, \{D\}, \{E\}$. Kruskal's adds edge A-B: `Union(A,B)` → $\{A,B\}$. Adds B-C: `Union(B,C)` → $\{A,B,C\}$. Candidate edge A-C: `Find(A)` and `Find(C)` both return the same root → cycle detected, skip. Adds C-D and D-E. Final MST uses 4 edges; the cycle check on A-C took one comparison.

## Remember

For a 500-asset portfolio with 124,750 pairwise distances, Union-Find makes Kruskal's cycle detection cost negligible — all 124,750 `Find` calls complete in effectively constant time, so the bottleneck is the initial $O(N^2 \log N)$ sort of edges. Without Union-Find, a naïve cycle check via depth-first search on the growing tree would cost $O(N)$ per edge, adding $O(N^3)$ total and making MST construction impractical on portfolios of more than a few hundred assets.
