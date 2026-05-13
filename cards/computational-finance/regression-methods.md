# Regression Methods

**Topic:** Computational Finance
**Tags:** regression, supervised learning, prediction, factor model, OLS, regularisation
**Author:** Claude Sonnet 4.6

---

## Definition

Regression methods are supervised learning techniques that model the relationship between a continuous or categorical target variable and one or more predictor features, estimating parameters that minimise a chosen loss function over training data.

## Key Formula

The general linear regression model for target $y$ with feature matrix $\mathbf{X}$ and coefficient vector $\boldsymbol{\beta}$:

$$y = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}, \qquad \boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})$$

The OLS estimator minimises squared residuals; regularised variants add a penalty term $\lambda\|\boldsymbol{\beta}\|_p^p$:

| Method | Loss | Use case |
|---|---|---|
| OLS | $\|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2$ | Low-dimensional, uncorrelated factors |
| Ridge | $\|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda\|\boldsymbol{\beta}\|_2^2$ | Many correlated predictors |
| Lasso | $\|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda\|\boldsymbol{\beta}\|_1$ | Sparse factor selection |
| Logistic | Cross-entropy | Binary classification (default, direction) |

## Example

Estimating a two-factor return model on 60 months of data: regress stock excess returns $r_i$ on market excess return $r_M$ and HML factor $r_{HML}$. OLS gives $\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$. If the market factor and HML are correlated (e.g. $\rho = 0.6$), OLS coefficient estimates are unstable; ridge regression with $\lambda = 0.1$ shrinks both towards zero and reduces variance, at the cost of introducing a small bias.

## Remember

Regression is the workhorse of quantitative factor investing. OLS is used to estimate factor loadings (betas) in the Fama-French and Carhart models; lasso performs automatic factor selection from a large universe of candidate signals, keeping only those with genuine predictive power; logistic regression scores counterparties by probability of default in credit risk models. The choice of regression method — and the regularisation strength $\lambda$ — directly determines which risk factors a portfolio is exposed to and how much idiosyncratic noise survives into the final position.
