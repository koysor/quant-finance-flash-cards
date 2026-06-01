# Ridge Regression (L2 Regularisation)

**Topic:** Computational Finance
**Tags:** ridge regression, l2 regularisation, shrinkage, overfitting, factor model, multicollinearity
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

**Ridge regression** is a regularised extension of ordinary least squares that adds an $\ell_2$ penalty — proportional to the sum of squared coefficients — to the cost function. This penalises large weights, shrinking all coefficients towards zero without eliminating any of them, which reduces variance at the cost of a small increase in bias.

## Key Formula

**Penalised objective:**

$$\hat{\mathbf{w}}_{\text{Ridge}} = \arg\min_{\mathbf{w}} \left\{ \frac{1}{N}\sum_{i=1}^{N}(y_i - \mathbf{w}^\top\mathbf{x}_i)^2 + \lambda \sum_{j=1}^{p} w_j^2 \right\}$$

**Closed-form solution (regularised normal equations):**

$$\hat{\mathbf{w}}_{\text{Ridge}} = (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$$

The scalar $\lambda \geq 0$ controls regularisation strength: $\lambda = 0$ recovers OLS; larger $\lambda$ shrinks all weights towards zero. The matrix $\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}$ is always invertible, even when the original $\mathbf{X}^\top\mathbf{X}$ is singular.

## Example

A factor model uses 20 candidate signals, including several correlated momentum variants. With $\lambda = 0$, OLS assigns extreme, unstable weights that overfit the 3-year training window: in-sample $R^2 = 0.42$, out-of-sample $R^2 = -0.05$.

Setting $\lambda = 0.1$, Ridge shrinks all 20 weights towards zero and distributes loading evenly across the correlated momentum signals. Out-of-sample $R^2$ rises to $0.09$ — a modest but stable positive contribution from the model.

## Remember

Ridge regression is the standard fix for **multicollinearity** in quant factor models. When 10 similar momentum signals are all included, OLS amplifies tiny numerical differences between them into huge opposing weights that cancel in training but destabilise out-of-sample. Ridge's $\lambda\mathbf{I}$ term adds a small positive value to every diagonal entry of $\mathbf{X}^\top\mathbf{X}$, ensuring the matrix is always invertible and that coefficient estimates are stable. In portfolio optimisation, adding $\lambda \lVert\mathbf{w}\rVert^2$ to the objective directly penalises concentrated positions — making Ridge regularisation and long-only constraints two sides of the same stability-seeking idea.
