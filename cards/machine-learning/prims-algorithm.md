# Prim's Algorithm

**Topic:** Machine Learning
**Tags:** prim's algorithm, minimum spanning tree, graph theory, greedy algorithm, asset network, portfolio construction
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Prim's algorithm builds a minimum spanning tree by growing a tree one node at a time, always extending it by the cheapest edge that connects an unvisited node to the current tree.

## Key Formula

Given a distance matrix $D \in \mathbb{R}^{N \times N}$ (e.g. $d_{ij} = \sqrt{2(1-\rho_{ij})}$):

1. Initialise: tree $T = \{v_0\}$ (any starting node), $\text{key}[v_0] = 0$, $\text{key}[v] = \infty$ for $v \neq v_0$
2. While $T \neq V$: find $v^* = \arg\min_{v \notin T}\, \text{key}[v]$, add $v^*$ to $T$
3. For each neighbour $u$ of $v^*$ with $u \notin T$: update $\text{key}[u] = \min(\text{key}[u],\, d_{v^* u})$

Complexity: $O(N^2)$ with an adjacency matrix — lower than Kruskal's $O(E \log E)$ when $E = O(N^2)$ for dense graphs.

## Example

Four assets A–D with distances $d_{AB}=0.41$, $d_{AC}=0.72$, $d_{AD}=0.95$, $d_{BC}=0.48$, $d_{BD}=0.80$, $d_{CD}=0.55$. Start from A: key = [0, 0.41, 0.72, 0.95]. Add B (min). Update: key[C] = min(0.72, 0.48) = 0.48; key[D] = min(0.95, 0.80) = 0.80. Add C. Update: key[D] = min(0.80, 0.55) = 0.55. Add D. MST edges: A-B (0.41), B-C (0.48), C-D (0.55); total distance 1.44.

## Remember

Financial correlation matrices are dense — every asset has a non-zero correlation with every other — meaning $E = N(N-1)/2 = O(N^2)$. On dense graphs Prim's $O(N^2)$ adjacency-matrix implementation is more efficient than Kruskal's edge-sorting approach, which is why Prim's is preferred in production implementations of Hierarchical Risk Parity and asset correlation network analysis where $N$ can reach several hundred.
