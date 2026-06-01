# Lasso Regression (L1 Regularisation)

**Topic:** Computational Finance
**Tags:** lasso, l1 regularisation, feature selection, sparse model, factor model, shrinkage
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

**Lasso regression** (Least Absolute Shrinkage and Selection Operator) minimises the ordinary least-squares loss augmented with an $\ell_1$ penalty on the coefficient vector. Unlike Ridge regression, the $\ell_1$ penalty produces **exact zeros**, performing automatic feature selection by eliminating irrelevant predictors entirely.

## Key Formula

$$\hat{\mathbf{w}} = \arg\min_{\mathbf{w}} \left\{ \frac{1}{n}\sum_{i=1}^{n}(y_i - \mathbf{w}^\top \mathbf{x}_i)^2 + \lambda \sum_{j=1}^{p} \lvert w_j \rvert \right\}$$

The $\ell_1$ penalty $\lambda \sum_j \lvert w_j \rvert$ has a diamond-shaped constraint region in coefficient space. Its corners lie on the axes, so the optimum frequently falls at a corner where several $w_j = 0$ exactly — this is why Lasso selects features.

The **soft-thresholding** solution for orthogonal predictors is:

$$\hat{w}_j = \text{sign}(\hat{w}_j^{\text{OLS}})\max\!\left(\lvert \hat{w}_j^{\text{OLS}} \rvert - \lambda,\, 0\right)$$

where $\lambda \geq 0$ is chosen by cross-validation.

## Example

A quant builds a cross-sectional equity return model with 40 candidate factors: value, momentum, quality, and 32 sentiment and alternative-data signals. OLS uses all 40 and overfits severely.

Fitting Lasso with $\lambda = 0.02$ (chosen by 5-fold cross-validation):
- 11 factors retain non-zero coefficients (value ×3, momentum ×2, quality ×2, sentiment ×4)
- 29 coefficients are driven exactly to zero
- Out-of-sample information coefficient rises from 0.03 to 0.09

The model is sparse, interpretable, and avoids in-sample data mining.

## Remember

In quantitative equity research, signal discovery generates dozens of correlated factor candidates. Lasso acts as an automatic **factor selector**: it identifies the smallest subset of signals that explains return variation, zeroing out noise and near-duplicate signals. This is particularly valuable when alternative data vendors supply many overlapping sentiment scores — Lasso retains the most informative one and discards the rest, preventing double-counting of the same underlying information.
