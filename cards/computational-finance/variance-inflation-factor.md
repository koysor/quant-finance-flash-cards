# Variance Inflation Factor (VIF)

**Topic:** Computational Finance
**Tags:** variance inflation factor, multicollinearity, regression, factor model, feature selection, ols
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Variance Inflation Factor (VIF)** measures how much the variance of an estimated regression coefficient is inflated due to multicollinearity with the other predictors. A high VIF indicates that a feature can be largely predicted from the others, contributing little independent information and making coefficient estimates unstable.

## Key Formula

For predictor $X_j$, regress it on all other predictors and compute the resulting $R_j^2$:

$$\text{VIF}_j = \frac{1}{1 - R_j^2}$$

| VIF | Interpretation |
|---|---|
| 1 | No multicollinearity |
| 1–5 | Moderate (usually acceptable) |
| 5–10 | High — consider removing or combining |
| $>10$ | Severe — predictor is near-redundant |

When $R_j^2 \to 1$ (perfect linear dependence), $\text{VIF}_j \to \infty$ and the OLS matrix $(\mathbf{X}^\top\mathbf{X})$ becomes near-singular.

## Example

A factor model includes both 3-month momentum ($X_1$) and 6-month momentum ($X_2$). Regressing $X_1$ on $X_2$ yields $R_1^2 = 0.95$. $\text{VIF}_1 = 1/(1-0.95) = 20$ — far above the danger threshold. The model "knows" combined momentum predicts returns but cannot reliably split the effect between the two signals; their coefficient estimates flip sign between estimation windows. Solution: drop one signal, use 12-month minus 1-month momentum to decorrelate, or apply PCA.

## Remember

Multicollinearity is endemic in quantitative finance because factors are often built from overlapping windows, similar data sources, or correlated asset classes — short-term and long-term momentum, different credit spread tenors, multiple macro indicators. When VIF exceeds 10, coefficient estimates become numerically unreliable: their standard errors inflate, significance tests lose power, and the coefficients change dramatically between periods. VIF screening is a standard pre-processing step before any factor model estimation, and Ridge regression or PCA are the two standard remedies when high VIF is unavoidable.
