# Unsupervised Learning

**Topic:** Computational Finance
**Tags:** unsupervised learning, clustering, dimensionality reduction, regime detection, pca, portfolio
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

**Unsupervised learning** is a class of machine learning algorithms that find structure in data without labelled outputs. Rather than learning a mapping from inputs to targets, these methods discover latent patterns — clusters, low-dimensional representations, or generative factors — directly from the raw feature matrix $\mathbf{X}$.

## Key Formula

**PCA reconstruction error** (dimensionality reduction objective): retain the $k$ eigenvectors $\mathbf{V}_k$ of the covariance matrix $\boldsymbol{\Sigma}$ that minimise the expected squared reconstruction error:

$$\min_{\mathbf{V}_k} \mathbb{E}\!\left[\|\mathbf{x} - \mathbf{V}_k\mathbf{V}_k^\top \mathbf{x}\|^2\right]$$

The solution is to choose $\mathbf{V}_k$ as the top $k$ eigenvectors (principal components) — those associated with the $k$ largest eigenvalues of $\boldsymbol{\Sigma}$.

**K-Means clustering objective** (find $K$ cluster assignments $C_k$ and centroids $\boldsymbol{\mu}_k$):

$$\min_{\{C_k, \boldsymbol{\mu}_k\}} \sum_{k=1}^{K} \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \boldsymbol{\mu}_k\|^2$$

## Example

A risk manager applies PCA to the daily returns of 200 stocks over 10 years. The first 5 principal components explain 70% of total variance: component 1 loads uniformly (market beta), component 2 contrasts growth vs. value, and components 3–5 capture sector rotations. She then runs K-Means with $K = 4$ on the rolling 60-day PC scores to label each trading day as one of four market regimes — bull, bear, high-volatility, and low-volatility — obtaining a regime sequence with no manual labelling.

## Remember

Unsupervised learning has two primary roles in quantitative finance. First, **regime detection**: clustering daily return or macro-factor data into regimes enables a portfolio manager to condition risk models and position sizing on the current regime — historical VaR estimated within a cluster is far more relevant than unconditional VaR. Second, **portfolio clustering**: grouping 500 stocks by return correlation or factor exposures identifies natural diversification buckets, so equal-weighting within clusters (rather than across assets) systematically avoids concentration in correlated mega-caps. Neither application requires a labelled training set, making unsupervised methods indispensable when target variables are unavailable or subjective.
