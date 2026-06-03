# Minimum Spanning Tree

**Topic:** Computational Finance
**Tags:** minimum spanning tree, graph theory, correlation, asset network, kruskal, portfolio construction
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A Minimum Spanning Tree (MST) of an asset universe is the unique tree connecting all assets with minimum total edge weight, where edge weights are correlation-based distances; it extracts the most significant pairwise relationships from a correlation matrix as a sparse, interpretable network.

## Key Formula

Asset pairs are first converted from correlations $\rho_{ij}$ to distances using:

$$d_{ij} = \sqrt{2(1 - \rho_{ij})} \in [0,\, 2]$$

The MST is then built by Kruskal's algorithm: sort all $\binom{N}{2}$ edges by $d_{ij}$ ascending and greedily add each edge that does not form a cycle, stopping when $N-1$ edges have been selected. The result is a spanning tree with minimum total distance:

$$\text{MST} = \arg\min_{T \in \mathcal{T}} \sum_{(i,j)\in T} d_{ij}$$

## Example

A universe of 5 assets (A–E) has pairwise correlations converted to distances. After sorting, the MST selects the edges A-C (0.41), B-C (0.48), C-D (0.55), D-E (0.71) — a path of 4 edges connecting all 5 assets with total distance 2.15. The edge A-B (0.89) is skipped because adding it would create a cycle. The resulting tree shows C as the central "hub" asset most connected to the others.

## Remember

In quantitative finance, the MST reveals the backbone of the asset correlation network: central hub assets that co-move with many others (often a broad market index or a dominant sector) appear as high-degree nodes. This network structure informs hierarchical clustering and Hierarchical Risk Parity — the correlation distance $d_{ij} = \sqrt{2(1 - \rho_{ij})}$ used in MST construction is the same metric that drives HRP's dendrogram, making the MST a useful visualisation tool for understanding portfolio structure.
