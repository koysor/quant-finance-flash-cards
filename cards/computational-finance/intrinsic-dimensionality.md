# Intrinsic Dimensionality

**Topic:** Computational Finance
**Tags:** intrinsic dimensionality, correlation dimension, manifold, dimensionality reduction, pca, factor model
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Intrinsic dimensionality** $k$ is the minimum number of parameters needed to describe the structure of a dataset, irrespective of the number of observed variables $d$. It is the true number of degrees of freedom — the dimension of the underlying manifold on which the data lies. Estimating $k$ before applying t-SNE, UMAP, or PCA tells the practitioner how much information the low-dimensional map can capture and whether compression to 2-D is justified.

## Key Formula

**Correlation dimension** (Grassberger–Procaccia estimator):

$$C(r) = \frac{2}{N(N-1)} \sum_{i < j} \mathbf{1}\!\left[\|\mathbf{x}_i - \mathbf{x}_j\| < r\right] \propto r^k$$

Taking logarithms, $k$ is the slope of $\log C(r)$ vs $\log r$ in the linear region:

$$\hat{k} = \frac{d \log C(r)}{d \log r}$$

**PCA-based estimator** — simpler linear estimate: $k_{\text{PCA}}$ = smallest number of principal components explaining $p\%$ of variance (typically $p = 90$ or $95$). The correlation dimension estimate $\hat{k}$ is typically lower because it exploits non-linear structure that PCA cannot capture.

## Example

Daily returns for 500 FTSE stocks over 10 years:

| Estimator | $\hat{k}$ | Interpretation |
|---|---|---|
| PCA (90% var) | 12 | 12 linear factors needed |
| PCA (95% var) | 22 | — |
| Correlation dimension | 5 | 5 true degrees of freedom |

The correlation dimension of 5 aligns with the Fama–French 5-factor model: market, size, value, profitability, investment. These 5 systematic sources of variation drive most of the cross-sectional return structure. The gap between PCA ($k = 12$) and the correlation dimension ($k = 5$) confirms that the factor manifold is non-linear — PCA requires extra components to approximate its curvature.

## Remember

Estimating intrinsic dimensionality before applying dimensionality reduction is a prerequisite that practitioners often skip. If $\hat{k} = 5$, projecting to 2-D loses 3 dimensions of genuine structure — the t-SNE or UMAP output is necessarily incomplete, and the practitioner should interpret clusters cautiously. If $\hat{k} = 2$, a 2-D embedding is near-lossless and cluster boundaries can be trusted. In quantitative finance, correlation dimension estimation on equity return matrices typically yields $\hat{k} \in [3, 8]$, consistent with multi-factor models; on macroeconomic state vectors it yields $\hat{k} \in [2, 4]$, consistent with a small number of global macro regimes. This prior on $k$ also informs the VAE bottleneck dimension and the number of clusters to test in $k$-means.
