# Kruskal's Algorithm

**Topic:** Machine Learning
**Tags:** kruskal's algorithm, minimum spanning tree, graph theory, union-find, greedy algorithm, asset network
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Kruskal's algorithm builds a minimum spanning tree by sorting all pairwise edges in ascending order of weight and greedily adding each edge that connects two previously disconnected components, using a union-find data structure to detect cycles in $O(\alpha(N))$ time.

## Key Formula

For $N$ assets with $E = N(N-1)/2$ pairwise distances:

1. Sort all edges: $d_{(1)} \leq d_{(2)} \leq \cdots \leq d_{(E)}$
2. Initialise $N$ singleton components $\{C_i\} = \{\{i\}\}$
3. For each edge $(i,j)$ in sorted order: if $\text{Find}(i) \neq \text{Find}(j)$, add $(i,j)$ to MST and call $\text{Union}(i,j)$
4. Stop when $N-1$ edges are in the MST

Complexity: $O(E \log E) = O(N^2 \log N)$ for a fully connected asset graph, versus Prim's $O(N^2)$ adjacency-matrix implementation — so Kruskal's is slower on the dense graphs typical of financial portfolios.

## Example

Five assets A–E with all 10 pairwise distances sorted ascending: A-B (0.41), B-C (0.48), C-D (0.55), D-E (0.71), B-E (0.73), A-C (0.72), … Kruskal's adds A-B, B-C, C-D, D-E (four edges connecting all five assets). When B-E (0.73) is considered, Find(B) = Find(E) — they are already connected — so it is skipped. MST complete.

## Remember

Kruskal's and Prim's always produce the same MST for a graph with unique edge weights; the choice between them is purely computational. For financial portfolios of $N \leq 500$ assets, where the correlation matrix is dense, Prim's $O(N^2)$ is the standard choice. Kruskal's $O(N^2 \log N)$ is preferred on sparse graphs (e.g. sector-filtered or minimum-correlation networks) where only a subset of $E \ll N^2$ edges are retained before tree construction.
