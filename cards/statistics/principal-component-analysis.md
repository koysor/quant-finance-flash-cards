# Principal Component Analysis

**Topic:** Statistics
**Tags:** PCA, dimensionality reduction, eigenvalues, covariance matrix, factor models
**Author:** Claude Opus 4.6

---

## Definition

**Principal Component Analysis (PCA)** is a technique that transforms a set of correlated variables into a smaller set of uncorrelated variables called **principal components**. It works by finding the eigenvectors of the covariance matrix — these eigenvectors point in the directions of greatest variance, and the corresponding eigenvalues measure how much variance each direction explains. In finance, PCA reveals the dominant risk factors driving a portfolio of correlated assets.

## Key Formula

Given the covariance matrix $\Sigma$ of $n$ asset returns, PCA solves the eigenvalue problem:

$$\Sigma \, \mathbf{v}_k = \lambda_k \, \mathbf{v}_k$$

where $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0$ are the eigenvalues and $\mathbf{v}_k$ are the orthonormal eigenvectors (principal components).

**Proportion of variance explained by the $k$-th component:**

$$\text{PVE}_k = \frac{\lambda_k}{\sum_{i=1}^{n} \lambda_i} = \frac{\lambda_k}{\text{tr}(\Sigma)}$$

## Example

A three-asset covariance matrix has eigenvalues $\lambda_1 = 0.045$, $\lambda_2 = 0.012$, $\lambda_3 = 0.003$. Total variance $= 0.060$.

| Component | Eigenvalue | PVE | Cumulative |
|-----------|-----------|------|-----------|
| PC1 | 0.045 | 75.0% | 75.0% |
| PC2 | 0.012 | 20.0% | 95.0% |
| PC3 | 0.003 | 5.0% | 100.0% |

The first two components explain 95% of total variance — the three-dimensional risk can be approximated with just two factors.

## Remember

In fixed income, PCA on the yield-curve covariance matrix consistently finds that three factors — **level**, **slope**, and **curvature** — explain over 95% of yield movements. In equities, the first principal component is typically a market factor explaining 40–60% of variance across stocks. PCA is the foundation of statistical factor models used in risk decomposition: instead of tracking $n(n+1)/2$ covariance entries, a portfolio manager can monitor a handful of principal components to understand where their risk is concentrated. It also enables dimensionality reduction when estimating covariance matrices, mitigating the curse of dimensionality that plagues large portfolios.
