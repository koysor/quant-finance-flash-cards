# UMAP

**Topic:** Computational Finance
**Tags:** umap, dimensionality reduction, manifold learning, visualisation, clustering, factor model
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**UMAP (Uniform Manifold Approximation and Projection)** is a non-linear dimensionality reduction technique that projects high-dimensional data onto a low-dimensional space while preserving both local neighbourhood structure and — unlike t-SNE — meaningful global topology. It is faster than t-SNE, scales to large datasets, and crucially supports **out-of-sample projection**: new data points can be embedded into a previously trained map without retraining.

## Key Formula

UMAP constructs a weighted $k$-nearest-neighbour graph in high-D space and optimises a low-D embedding to match it, using a fuzzy set membership function:

$$w_{ij} = \exp\!\left(-\frac{d(\mathbf{x}_i, \mathbf{x}_j) - \rho_i}{\sigma_i}\right)$$

where $\rho_i$ is the distance to the nearest neighbour (ensures local connectivity) and $\sigma_i$ is calibrated so each point has a fixed effective number of neighbours (perplexity analogue).

The embedding minimises the cross-entropy between the high-D fuzzy graph and the low-D fuzzy graph:

$$\mathcal{L} = \sum_{(i,j)} \left[w_{ij} \log \frac{w_{ij}}{v_{ij}} + (1-w_{ij})\log\frac{1-w_{ij}}{1-v_{ij}}\right]$$

**Key hyperparameters:**
- `n_neighbors` — controls local vs global structure trade-off (typical: 5–50)
- `min_dist` — minimum spacing between points in low-D (typical: 0.0–0.5)

## Example

A fund maintains a live regime detection pipeline. Each day's market state is described by 40 features (yield curve shape, credit spreads, equity factor returns, VIX term structure). UMAP is trained once on 10 years of history, producing a 2-D map where regimes cluster visibly — pre-GFC expansion, GFC crisis, QE era, COVID shock. Each new trading day's 40-feature vector is projected into the same 2-D space in milliseconds via the trained UMAP transform, without retraining. The resulting $(y_1, y_2)$ coordinates feed a nearest-neighbour lookup to identify which historical regime today most resembles.

## Remember

UMAP's out-of-sample projection is the property that makes it operationally superior to t-SNE for live financial applications: t-SNE must retrain on the full dataset each time new observations arrive (breaking the temporal ordering and making it unsuitable for streaming data), whilst UMAP's trained transform applies to new points directly. In quantitative finance, UMAP is used for real-time regime identification, anomaly detection in trading data (unusual market conditions project to sparse regions of the map), and visualising high-dimensional factor exposures across a stock universe without the inter-cluster distance distortions that make t-SNE outputs non-transferable between training runs.
