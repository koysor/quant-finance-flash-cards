# Norm Notation

**Topic:** Mathematical Notation
**Tags:** notation, norm, absolute value, Lp norm, Frobenius, distance, risk
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

**Norm notation** measures the "size" of a scalar, vector, or matrix. The vertical bar and double-bar conventions have precise distinct meanings:

| Symbol | Name | Definition |
|---|---|---|
| $\lvert x \rvert$ | Absolute value | $\lvert x \rvert = x$ if $x \geq 0$, else $-x$ |
| $\lVert \mathbf{v} \rVert_2$ | Euclidean (L²) norm | $\sqrt{\sum_i v_i^2}$ |
| $\lVert \mathbf{v} \rVert_1$ | Manhattan (L¹) norm | $\sum_i \lvert v_i \rvert$ |
| $\lVert \mathbf{v} \rVert_p$ | $L^p$ norm | $\left(\sum_i \lvert v_i \rvert^p\right)^{1/p}$ |
| $\lVert \mathbf{v} \rVert_\infty$ | Sup norm | $\max_i \lvert v_i \rvert$ |
| $\lVert \mathbf{A} \rVert_F$ | Frobenius norm | $\sqrt{\sum_{i,j} A_{ij}^2} = \sqrt{\operatorname{tr}(\mathbf{A}^\top \mathbf{A})}$ |

When no subscript is shown, $\lVert \cdot \rVert$ usually denotes the Euclidean norm.

## Key Formula

**Triangle inequality** (holds for all norms):

$$\lVert \mathbf{u} + \mathbf{v} \rVert \leq \lVert \mathbf{u} \rVert + \lVert \mathbf{v} \rVert$$

**Cauchy–Schwarz inequality:**

$$\lvert \mathbf{u}^\top \mathbf{v} \rvert \leq \lVert \mathbf{u} \rVert_2 \lVert \mathbf{v} \rVert_2$$

**$L^1$ regularisation** (LASSO penalty):

$$\min_{\boldsymbol{\beta}} \lVert \mathbf{y} - \mathbf{X}\boldsymbol{\beta} \rVert_2^2 + \lambda \lVert \boldsymbol{\beta} \rVert_1$$

## Example

In **LASSO regression** applied to factor model selection, the $L^1$ penalty $\lambda \lVert \boldsymbol{\beta} \rVert_1 = \lambda \sum_j \lvert \beta_j \rvert$ sets irrelevant factor loadings exactly to zero (sparsity). By contrast, **Ridge regression** uses $\lambda \lVert \boldsymbol{\beta} \rVert_2^2 = \lambda \sum_j \beta_j^2$, which shrinks coefficients towards zero without exact elimination. The choice of norm determines the type of regularisation and the sparsity of the resulting model.

## Remember

The $L^1$ versus $L^2$ norm distinction is fundamental in quantitative risk and factor selection. **Mean Absolute Deviation** (MAD) uses the $L^1$ norm on losses — it is more robust to outliers than variance ($L^2$) because it does not square large deviations. In portfolio optimisation, $L^1$ minimisation of portfolio weights is related to finding sparse portfolios with fewer active positions. The Frobenius norm $\lVert \mathbf{A} \rVert_F$ is the matrix analogue of the Euclidean norm and appears in covariance matrix estimation and shrinkage problems.
