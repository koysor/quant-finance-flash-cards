# Normal Equations

**Topic:** Computational Finance
**Tags:** normal equations, OLS, linear regression, closed-form, matrix inversion, factor model
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **normal equations** are the closed-form solution to the ordinary least squares (OLS) problem. Setting the gradient of the MSE cost function to zero and solving analytically yields a direct formula for the optimal parameter vector $\hat{\boldsymbol{\theta}}$, requiring no iterative optimisation.

## Key Formula

$$\hat{\boldsymbol{\theta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$$

where $\mathbf{X}$ is the $N \times (p+1)$ design matrix (observations as rows, features plus intercept column as columns) and $\mathbf{y}$ is the $N \times 1$ target vector.

Derived by setting $\nabla_{\boldsymbol{\theta}} J = \frac{2}{N}\mathbf{X}^\top(\mathbf{X}\boldsymbol{\theta}-\mathbf{y}) = \mathbf{0}$.

Computational cost: $\mathcal{O}(p^3)$ for the matrix inversion, where $p$ is the number of features.

## Example

Estimate Fama-French 3-factor loadings for a fund: $N=120$ monthly returns, $p=3$ factors. Design matrix $\mathbf{X}$ is $120\times4$ (3 factors + intercept). Compute $\mathbf{X}^\top\mathbf{X}$ ($4\times4$), invert it, and multiply by $\mathbf{X}^\top\mathbf{y}$ — the result is the vector $(\alpha, \beta_{\text{mkt}}, \beta_{\text{HML}}, \beta_{\text{SMB}})^\top$ in one shot.

## Remember

Normal equations are exact and fast when $p$ is small (up to a few hundred features), but become numerically unstable and computationally prohibitive when $p$ is large — $(\mathbf{X}^\top\mathbf{X})$ can be singular if features are collinear. This is why Ridge regression adds $\lambda\mathbf{I}$ to the matrix before inversion — the regularised normal equations $\hat{\boldsymbol{\theta}} = (\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$ are always invertible and are the standard tool for fitting over-determined factor models.
