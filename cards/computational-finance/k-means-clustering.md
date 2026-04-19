# K-Means Clustering

**Topic:** Computational Finance
**Tags:** clustering, unsupervised learning, centroids, elbow method, regime detection, portfolio
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**K-Means Clustering** is an unsupervised algorithm that partitions $N$ observations into $K$ clusters by iteratively assigning each point to its nearest centroid and updating centroids to the cluster mean, until convergence.

## Key Formula

Minimise the within-cluster sum of squared distances (inertia):

$$J = \sum_{k=1}^{K} \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \boldsymbol{\mu}_k\|^2$$

where $\boldsymbol{\mu}_k$ is the centroid of cluster $C_k$.

## Example

Apply K-Means with $K=3$ to daily returns of 500 stocks using 5 factor loadings as features. The algorithm groups stocks into three clusters that correspond roughly to defensive, cyclical, and growth exposures — without any labels being provided.

## Remember

In quantitative finance, K-Means is used for market-regime detection (cluster historical return periods into "bull", "bear", "crisis"), sector classification of unlabelled securities, and correlation-based grouping for diversification analysis. The Elbow Method — plotting inertia against $K$ and finding the bend — guides the choice of the number of clusters.
