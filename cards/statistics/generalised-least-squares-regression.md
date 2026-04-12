# Generalised Least Squares Regression

**Topic:** Statistics
**Tags:** regression, GLS, heteroskedasticity, autocorrelation, estimation, covariance
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Generalised least squares (GLS) regression** extends OLS to handle violations of the i.i.d. residual assumption. Where OLS assumes $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0},\, \sigma^2 \mathbf{I})$, GLS allows a general error covariance $\boldsymbol{\Omega}$, accommodating:

- **Heteroskedasticity** — each observation has a different residual variance (e.g. high-volatility stocks have noisier returns).
- **Autocorrelation** — residuals are correlated across time (e.g. momentum in pricing errors).

GLS is equivalent to applying OLS to a transformed system where the residuals are i.i.d. The transformation is derived via the Cholesky decomposition $\boldsymbol{\Omega} = \mathbf{C}\mathbf{C}^\top$: pre-multiplying by $\mathbf{C}^{-1}$ whitens the errors.

## Key Formula

Setup: $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, with $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Omega})$ and $\boldsymbol{\Omega}$ known.

Objective — minimise the Mahalanobis distance:

$$\min_{\boldsymbol{\beta}}\;(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top \boldsymbol{\Omega}^{-1}(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})$$

GLS estimator:

$$\hat{\boldsymbol{\beta}}_{\text{GLS}} = \left(\mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{X}\right)^{-1} \mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{Y}$$

Asymptotic distribution:

$$\hat{\boldsymbol{\beta}}_{\text{GLS}} \;\xrightarrow{d}\; \mathcal{N}\!\left(\boldsymbol{\beta},\; \left(\mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{X}\right)^{-1}\right)$$

When $\boldsymbol{\Omega} = \sigma^2 \mathbf{I}$ the GLS estimator reduces exactly to OLS.

## Example

A portfolio manager regresses ten assets' excess returns on a single market factor. The assets have very different volatilities — tech stocks are far noisier than utilities — so the OLS assumption of equal residual variance is violated.

Label the residual covariance $\boldsymbol{\Omega} = \operatorname{diag}(\sigma_1^2, \ldots, \sigma_{10}^2)$ (heteroskedastic, no cross-asset correlation). Then $\boldsymbol{\Omega}^{-1} = \operatorname{diag}(1/\sigma_1^2, \ldots, 1/\sigma_{10}^2)$, and the GLS estimator down-weights noisy assets:

$$\hat{\boldsymbol{\beta}}_{\text{GLS}} = \frac{\sum_i x_i y_i / \sigma_i^2}{\sum_i x_i^2 / \sigma_i^2}$$

Low-volatility assets (small $\sigma_i^2$, large $1/\sigma_i^2$) exert more influence on the estimated slope — intuitively, their signals are more reliable.

## Remember

**Black–Litterman** is applied GLS in disguise. The model blends an equilibrium prior $\boldsymbol{\Pi}$ with investor views $\mathbf{P}\boldsymbol{\mu} = \mathbf{q}$ using Theil's mixed estimation — a form of GLS where $\boldsymbol{\Omega}$ encodes confidence in each view. High uncertainty (large diagonal entry in the view covariance) means the view has little pull; low uncertainty means it dominates. Understanding GLS makes Black–Litterman transparent: the posterior expected returns are simply the GLS estimate of $\boldsymbol{\mu}$ given both the prior "observation" and the investor's view "observations".
