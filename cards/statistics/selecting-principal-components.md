# Selecting Principal Components

**Topic:** Statistics
**Tags:** principal components, scree plot, variance explained, kaiser criterion, dimensionality reduction, pca
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Selecting the number of principal components** determines how many PCs to retain after PCA decomposition, balancing dimensionality reduction against information loss. Three standard criteria are used: a **cumulative variance threshold**, the **scree plot elbow**, and the **Kaiser criterion**.

## Key Formula

**Proportion of variance explained (PVE)** by the first $k$ components:

$$\text{Cumulative PVE}(k) = \frac{\sum_{j=1}^{k} \lambda_j}{\sum_{j=1}^{p} \lambda_j}$$

| Method | Rule | Use case |
|---|---|---|
| Cumulative threshold | Retain $k$ s.t. $\text{PVE}(k) \geq$ 80–95% | General purpose |
| Scree plot | Retain components before the "elbow" in the $\lambda_j$ plot | Visual inspection |
| Kaiser criterion | Retain components with $\lambda_j > 1$ (standardised data) | When data is Z-scored |

The Kaiser criterion ($\lambda > 1$) means: only retain components that explain more variance than a single original variable — a natural minimum threshold.

## Example

Yield curve PCA on 10 maturities: eigenvalues $\lambda_1 = 8.2$, $\lambda_2 = 1.1$, $\lambda_3 = 0.4$, remaining $\leq 0.1$. Total = 10.

- Cumulative PVE: PC1 = 82%, PC1+PC2 = 93%, PC1+PC2+PC3 = 97%.
- Scree plot: sharp drop after PC3, flat thereafter — elbow at 3.
- Kaiser: $\lambda_1 = 8.2 > 1$, $\lambda_2 = 1.1 > 1$, $\lambda_3 = 0.4 < 1$ — keep 2.

Practice: retain 3 PCs (level, slope, curvature) to capture 97% of yield curve movement.

## Remember

In fixed income, retaining 3 yield-curve PCs (level, slope, curvature) is near-universal practice — these three factors consistently explain 95–98% of yield curve variance across markets and time periods. In equity risk models, the cumulative 95% threshold is standard: typically 5–20 PCs explain 95% of the return covariance matrix, enabling a massive reduction from the $p(p+1)/2$ entries in the full covariance matrix to a low-rank factor structure. The Kaiser criterion is conservative and can under-retain components in financial data where many small eigenvalues share genuine variance.
