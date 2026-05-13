# t-SNE

**Topic:** Computational Finance
**Tags:** t-sne, dimensionality reduction, visualisation, non-linear, clustering, factor model
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**t-SNE (t-distributed Stochastic Neighbour Embedding)** is a non-linear dimensionality reduction technique that projects high-dimensional data onto 2-D or 3-D for visualisation, preserving local neighbourhood structure. Unlike PCA (which preserves global variance) or SOM (which preserves topology on a grid), t-SNE emphasises keeping similar points together in the low-dimensional map at the cost of global distance relationships.

## Key Formula

t-SNE defines pairwise similarities in high-D space as Gaussian probabilities $p_{ij}$ and in low-D space as Student-$t$ probabilities $q_{ij}$, then minimises the KL divergence between them:

$$p_{ij} = \frac{\exp\!\left(-\|\mathbf{x}_i - \mathbf{x}_j\|^2 / 2\sigma_i^2\right)}{\sum_{k \neq l} \exp\!\left(-\|\mathbf{x}_k - \mathbf{x}_l\|^2 / 2\sigma_k^2\right)}$$

$$q_{ij} = \frac{(1 + \|\mathbf{y}_i - \mathbf{y}_j\|^2)^{-1}}{\sum_{k \neq l}(1 + \|\mathbf{y}_k - \mathbf{y}_l\|^2)^{-1}}$$

$$\mathcal{L} = \text{KL}(P \| Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$

The heavy-tailed $t$-distribution in low-D space prevents the "crowding problem" — it gives more room for dissimilar points to spread apart.

## Example

Project 500 equities described by 50 factor loadings (value, momentum, quality, size, …) onto 2-D using t-SNE with perplexity 30. The scatter plot reveals distinct clusters matching sector classifications — without using sector labels. Points within each cluster represent stocks with similar multi-factor profiles, while the global arrangement (cluster distances) is not interpretable. Colour the points by sector: consumer staples and utilities cluster separately from technology and financials.

## Remember

t-SNE is the standard visualisation tool in quantitative finance for exploring high-dimensional factor spaces and clustering outputs because its non-linear structure reveals cluster shapes that PCA (constrained to linear projections) misses entirely. Its critical limitation is that **inter-cluster distances are not meaningful** — two clusters that appear far apart in a t-SNE plot are not necessarily more different than two that appear close. For portfolio construction and risk analysis, PCA or SOM are used; t-SNE is purely exploratory, helping analysts confirm that a K-Means or hierarchical clustering has found genuinely distinct groups before committing to a production model.
