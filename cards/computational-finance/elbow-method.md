# Elbow Method

**Topic:** Computational Finance
**Tags:** elbow method, silhouette score, selecting k, k-means, cluster validation, regime detection
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **elbow method** and **silhouette score** are the two standard techniques for choosing the optimal number of clusters $K$ in K-Means and related algorithms. The elbow method plots within-cluster inertia against $K$ and looks for the point of diminishing returns; the silhouette score measures how well each point fits its assigned cluster relative to neighbouring clusters.

## Key Formula

**Inertia** (within-cluster sum of squared distances):
$$J(K) = \sum_{k=1}^{K} \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \boldsymbol{\mu}_k\|^2$$

Choose $K$ where the marginal decrease in $J(K)$ flattens — the "elbow".

**Silhouette score** for observation $i$:
$$s_i = \frac{b_i - a_i}{\max(a_i, b_i)}, \qquad s_i \in [-1, 1]$$

where $a_i$ = mean distance to own-cluster members, $b_i$ = mean distance to nearest-cluster members. Choose $K$ that **maximises** $\bar{s} = \frac{1}{N}\sum_i s_i$. $s_i \approx 1$ means well-placed; $s_i \approx 0$ means on a boundary; $s_i < 0$ means likely in the wrong cluster.

## Example

Clustering 10 years of daily macro features (yields, spreads, VIX) to detect market regimes. Inertia: $J(2)=3{,}400$, $J(3)=1{,}200$ (large drop), $J(4)=1{,}050$ (small drop), $J(5)=980$. Elbow at $K=3$. Silhouette: $\bar{s}(2)=0.38$, $\bar{s}(3)=0.51$, $\bar{s}(4)=0.44$. Both methods agree: $K=3$ (bull, bear, crisis) is the natural regime count.

## Remember

In quantitative finance, selecting $K$ is a business decision as much as a statistical one: $K=3$ regime clusters (expansion, contraction, crisis) is a common default in macro strategy because it matches the economic cycle. The silhouette score is preferred when clusters are expected to be of different sizes or shapes, since the elbow method can be ambiguous on financial data (where inertia declines smoothly without a clear kink). Reporting both metrics together is best practice for model documentation under MRM frameworks.
