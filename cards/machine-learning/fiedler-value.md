# Fiedler Value

**Topic:** Machine Learning
**Tags:** fiedler value, algebraic connectivity, graph laplacian, spectral graph theory, clustering, portfolio structure
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Fiedler value $\lambda_2$ is the second-smallest eigenvalue of the graph Laplacian; it measures algebraic connectivity — how much it costs to split the graph into two parts — and in portfolio analysis quantifies how distinctly an asset universe separates into clusters.

## Key Formula

For a graph with Laplacian $L$, the Fiedler value is:

$$\lambda_2 = \min_{\mathbf{x} \perp \mathbf{1},\; \mathbf{x} \neq \mathbf{0}} \frac{\mathbf{x}^\top L\, \mathbf{x}}{\mathbf{x}^\top \mathbf{x}}$$

The minimising vector $\mathbf{u}_2$ — the **Fiedler vector** — assigns each asset a score; the sign of $u_{2,i}$ indicates which side of the optimal bisection asset $i$ belongs to. The Cheeger inequality bounds the minimum normalised cut cost $h(G)$:

$$\frac{\lambda_2}{2} \leq h(G) \leq \sqrt{2\lambda_2}$$

A small $\lambda_2$ guarantees a cheap cut exists; $\lambda_2 = 0$ means the graph is already disconnected.

## Example

Twenty equities: 10 technology and 10 energy stocks with strong intra-sector but weak inter-sector correlations. The graph Laplacian has $\lambda_1 = 0$ and $\lambda_2 = 0.03$ (near-disconnection). The Fiedler vector $\mathbf{u}_2$ has positive entries for all technology stocks and negative entries for all energy stocks — a perfect partition. One month later, during a risk-off episode, cross-sector correlations spike and $\lambda_2$ rises to 0.18, signalling that the two clusters have merged and diversification has fallen sharply.

## Remember

The Fiedler value gives a single number — the algebraic connectivity — that can be monitored daily as a leading indicator of diversification breakdown. When previously uncorrelated asset clusters (equities vs bonds, US vs EM) start moving together under stress, $\lambda_2$ rises because no cheap partition exists. Risk managers use rising $\lambda_2$ as a crowding signal: the portfolio's correlation graph is becoming more connected, meaning diversification benefits are shrinking even before standard pairwise correlations indicate it.
