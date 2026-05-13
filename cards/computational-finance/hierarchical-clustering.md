# Hierarchical Clustering

**Topic:** Computational Finance
**Tags:** hierarchical clustering, dendrogram, agglomerative, linkage, portfolio construction, correlation
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Hierarchical clustering** builds a nested sequence of clusters, visualised as a **dendrogram** — a tree diagram where the height of each merge represents the dissimilarity between the joined clusters. Unlike K-Means, it requires no pre-specified number of clusters; the user cuts the dendrogram at a chosen height to obtain any number of groups.

## Key Formula

**Agglomerative algorithm** (bottom-up, most common):

1. Start: each observation is its own cluster ($N$ clusters)
2. Merge the two closest clusters according to a linkage criterion
3. Repeat until a single cluster remains

The dendrogram height at a merge equals the inter-cluster distance under the chosen linkage:

$$d_{\text{merge}}(A, B) = \text{linkage}(A, B)$$

The number of clusters $K$ is chosen by cutting at a threshold $h$:

$$K = \text{number of branches below height } h$$

Unlike K-Means (which minimises a global objective), hierarchical clustering is **deterministic** — the same data always produces the same dendrogram, with no random initialisation.

## Example

Apply agglomerative clustering to 30 FTSE 100 stocks using correlation distance $d_{ij} = 1 - \rho_{ij}$. Ward's linkage merges the two groups that produce the smallest increase in total within-cluster variance. The dendrogram shows: energy and mining stocks fuse first (high correlation), then financials cluster, then defensives (utilities, consumer staples). Cutting at height $h = 0.6$ yields 5 clusters — a natural sector partition without using sector labels.

## Remember

Hierarchical clustering is used in quantitative finance for **correlation-based portfolio construction**: group securities by return correlation, then select one representative from each cluster to ensure diversification. Because the dendrogram captures the full hierarchical structure of correlations, a portfolio manager can choose the granularity of diversification by adjusting the cut height — a flexibility K-Means cannot provide. It also underpins Hierarchical Risk Parity (HRP), which uses the dendrogram to allocate portfolio weights in a way that respects the correlation structure.
