# Perplexity

**Topic:** Computational Finance
**Tags:** perplexity, t-sne, hyperparameter, nearest neighbours, dimensionality reduction, visualisation
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Perplexity** is the key hyperparameter in t-SNE that controls the effective number of nearest neighbours each point "sees" when constructing its high-dimensional similarity distribution. It determines the balance between local and global structure in the resulting 2-D map: low perplexity emphasises tight local clusters, high perplexity reveals broader global patterns.

## Key Formula

The bandwidth $\sigma_i$ for each point $i$ is chosen so that the conditional probability distribution over neighbours has the specified perplexity:

$$\text{Perp}(P_i) = 2^{H(P_i)}, \qquad H(P_i) = -\sum_j p_{j|i} \log_2 p_{j|i}$$

where $H(P_i)$ is the Shannon entropy of the conditional distribution. Perplexity $\approx$ effective number of neighbours; typical range: **5 to 50**.

**Effect of perplexity on the map:**

| Perplexity | Neighbourhood size | Map characteristic |
|---|---|---|
| 5–10 | Very local | Tight micro-clusters; fragmented |
| 20–30 | Moderate | Balanced; standard default |
| 40–50 | Broad | Global patterns; clusters may merge |
| $> N/2$ | Near-global | Equivalent to PCA-like behaviour |

## Example

Mapping 200 equity factor vectors with t-SNE. Perplexity 5: 15 small fragmented clusters, many singletons — over-segmented, unstable across runs. Perplexity 30: 4–5 coherent clusters matching sector groupings (tech, financials, consumer, industrials) — interpretable. Perplexity 80: two broad blobs (growth vs value) — only the coarsest structure remains. KNN preservation peaks at perplexity 30, confirming it as the optimal value.

## Remember

Perplexity in t-SNE is the analogue of `n_neighbors` in UMAP and bandwidth in kernel density estimation — it is the single most important hyperparameter to tune for financial visualisation tasks. A common mistake is using the default perplexity=30 for very small datasets (fewer than 100 observations) or very large ones (more than 10,000), where it is either too large (all points become neighbours) or too small (only micro-structure is preserved). In practice, run t-SNE at perplexity 5, 15, 30, and 50, compute KNN preservation for each, and select the value that maximises KNN on the held-out validation period — the same rigour applied to any other model hyperparameter.
