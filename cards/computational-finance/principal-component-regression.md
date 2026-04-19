# Principal Component Regression

**Topic:** Computational Finance
**Tags:** PCR, PCA, regression, dimensionality reduction, multicollinearity, factor model
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Principal Component Regression (PCR)** first applies PCA to reduce a high-dimensional, potentially collinear feature matrix to a smaller set of uncorrelated principal components, then fits OLS regression on those components. It avoids the matrix-inversion instability of normal equations when features are collinear.

## Key Formula

**Step 1 — PCA:** decompose $\mathbf{X} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top$, retain the first $k$ principal components: $\mathbf{Z} = \mathbf{X}\mathbf{V}_k$.

**Step 2 — OLS on components:**

$$\hat{\boldsymbol{\alpha}} = (\mathbf{Z}^\top\mathbf{Z})^{-1}\mathbf{Z}^\top\mathbf{y}$$

**Step 3 — back-transform** to original feature space:

$$\hat{\boldsymbol{\beta}} = \mathbf{V}_k\,\hat{\boldsymbol{\alpha}}$$

Since the columns of $\mathbf{Z}$ are orthogonal, $\mathbf{Z}^\top\mathbf{Z}$ is diagonal and always invertible.

## Example

Regressing a fund's returns on 50 correlated macro indicators (yields, spreads, FX, equities). Direct OLS fails — $(\mathbf{X}^\top\mathbf{X})$ is near-singular. PCR retains the top 5 principal components (explaining 85% of variance) and fits OLS on those — producing stable, interpretable factor loadings with no inversion instability.

## Remember

PCR is the systematic answer to multicollinearity in factor models: instead of manually selecting which correlated indicators to include, PCA rotates the feature space to find the directions of maximum variance (which often correspond to recognisable macro regimes — growth, inflation, risk-off) and regression is performed in that clean orthogonal basis. Ridge regression achieves a similar stabilisation but penalises all directions equally; PCR explicitly discards the lowest-variance directions, which in finance often correspond to pure noise.
