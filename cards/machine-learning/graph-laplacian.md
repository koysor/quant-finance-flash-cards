# Graph Laplacian

**Topic:** Machine Learning
**Tags:** graph laplacian, spectral graph theory, eigenvalues, asset network, fiedler vector, clustering
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The graph Laplacian $L = \text{Deg} - W$ is a matrix encoding the full connectivity structure of an asset network; its eigenvalues measure cluster separability and its eigenvectors reveal the natural partition boundaries of the graph.

## Key Formula

From a similarity matrix $W$ (where $W_{ij} \geq 0$ represents pairwise asset similarity and $W_{ii} = 0$), the degree matrix $\text{Deg}$ has diagonal entries $\text{Deg}_{ii} = \sum_j W_{ij}$. The two standard forms are:

$$L = \text{Deg} - W \qquad \text{(unnormalised)}$$

$$L_{\text{sym}} = I - \text{Deg}^{-1/2}\, W\, \text{Deg}^{-1/2} \qquad \text{(normalised)}$$

Both are symmetric positive semi-definite. The smallest eigenvalue is always $\lambda_1 = 0$ (eigenvector $\mathbf{1}$). The **algebraic connectivity** $\lambda_2 > 0$ (Fiedler value) equals zero only when the graph is disconnected; the corresponding **Fiedler vector** $\mathbf{u}_2$ identifies the optimal partition of the graph at its weakest connectivity point.

## Example

Twenty equities split into two sectors with strong intra-sector and weak inter-sector correlations. The normalised Laplacian has $\lambda_2 = 0.04$ (small, indicating near-disconnection between sectors) versus $\lambda_3 = 0.61$. The Fiedler vector $\mathbf{u}_2$ has positive entries for all technology stocks and negative entries for all energy stocks — a clean partition. Spectral clustering on $\mathbf{u}_2$ alone reproduces the known sector labels with 95% accuracy.

## Remember

In portfolio construction, the Fiedler value is a single number measuring how naturally the asset universe splits into two groups: a small Fiedler value means there is a clear cluster boundary (good for HRP and NCO); a large Fiedler value means assets are all strongly interconnected with no natural partition. Risk managers use the Laplacian spectrum to monitor whether a portfolio's diversification structure is breaking down — a rising Fiedler value indicates that previously distinct asset clusters are becoming correlated.
