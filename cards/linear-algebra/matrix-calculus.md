# Matrix Calculus

**Topic:** Linear Algebra
**Tags:** gradient, hessian, optimisation, mvo, ols, portfolio-theory
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Matrix calculus extends ordinary differentiation to scalar functions of vectors and matrices. When $f(\mathbf{x})$ is a scalar and $\mathbf{x} \in \mathbb{R}^n$, the **gradient** $\frac{\partial f}{\partial \mathbf{x}}$ is the column vector of partial derivatives — it points in the direction of steepest ascent and has the same shape as $\mathbf{x}$.

The **Hessian** $\mathbf{H}$ collects all second-order partial derivatives:

$$H_{ij} = \frac{\partial^2 f}{\partial x_i \, \partial x_j}$$

For a symmetric matrix $\mathbf{A}$, the Hessian of $\mathbf{x}'\mathbf{A}\mathbf{x}$ is $2\mathbf{A}$. If $\mathbf{A}$ is **positive definite**, the Hessian is positive definite, confirming that any stationary point is a **global minimum**.

## Key Formula

| Function $f(\mathbf{x})$ | Gradient $\dfrac{\partial f}{\partial \mathbf{x}}$ |
|---|---|
| $\mathbf{a}'\mathbf{x}$ (linear) | $\mathbf{a}$ |
| $\mathbf{x}'\mathbf{A}\mathbf{x}$ ($\mathbf{A}$ symmetric, quadratic) | $2\mathbf{A}\mathbf{x}$ |
| $\mathbf{x}'\boldsymbol{\Sigma}\mathbf{x}$ (portfolio variance) | $2\boldsymbol{\Sigma}\mathbf{x}$ |

**OLS normal equations** — minimise the residual sum of squares $(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})'(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})$:

$$\frac{\partial}{\partial \boldsymbol{\beta}} = -2\mathbf{X}'(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) = \mathbf{0} \implies \hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$$

## Example

In **unconstrained mean–variance optimisation (MVO)**, portfolio variance is:

$$\sigma_p^2 = \mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}$$

where $\mathbf{w} \in \mathbb{R}^n$ is the weight vector and $\boldsymbol{\Sigma}$ is the $n \times n$ covariance matrix.

Applying the quadratic gradient rule:

$$\frac{\partial \sigma_p^2}{\partial \mathbf{w}} = 2\boldsymbol{\Sigma}\mathbf{w}$$

Setting this to zero gives the **first-order condition (FOC)**: $\boldsymbol{\Sigma}\mathbf{w}^* = \mathbf{0}$ (trivial solution; in practice, a budget constraint $\mathbf{1}'\mathbf{w} = 1$ is added via Lagrange multipliers).

The second derivative (Hessian) is $2\boldsymbol{\Sigma}$. Because a valid covariance matrix is **positive definite**, the Hessian is positive definite, confirming $\mathbf{w}^*$ is a minimum, not a maximum or saddle point.

## Remember

Two of the most important results in quantitative finance fall straight out of matrix calculus:

1. **MVO** — differentiating $\mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}$ with respect to $\mathbf{w}$ gives $2\boldsymbol{\Sigma}\mathbf{w}$. Set to zero (with constraints) to find the minimum-variance portfolio; the positive-definite Hessian $2\boldsymbol{\Sigma}$ guarantees a true minimum.
2. **OLS** — differentiating the sum of squared residuals with respect to $\boldsymbol{\beta}$ and setting to zero yields the closed-form estimator $\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$, the workhorse of factor-model estimation and beta calibration.
