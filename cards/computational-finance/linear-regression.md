# Linear Regression

**Topic:** Computational Finance
**Tags:** linear regression, OLS, least squares, factor model, beta, supervised learning
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Linear regression** is a supervised learning algorithm that models the relationship between a continuous target variable $y$ and one or more predictors $\mathbf{x}$ as a weighted linear combination. The weights (coefficients) are estimated by minimising the sum of squared residuals.

## Key Formula

Model: $y = \boldsymbol{\theta}^{\top}\mathbf{x} + \varepsilon$

**OLS normal equation** (closed-form solution):

$$\hat{\boldsymbol{\theta}} = (\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\mathbf{y}$$

**Cost function:**

$$J(\boldsymbol{\theta}) = \frac{1}{2N}\sum_{n=1}^{N}(y^{(n)} - \hat{y}^{(n)})^2$$

## Example

Regress monthly excess returns of a stock on the market excess return, value factor (HML), and momentum factor. The three estimated coefficients are the stock's factor loadings; $R^2$ measures how much return variation is explained.

## Remember

The Fama-French factor model is linear regression at its core: each coefficient $\theta_i$ quantifies systematic exposure to a risk premia. OLS minimises in-sample squared error, but for finance data (non-normal, autocorrelated residuals) practitioners routinely apply Ridge or robust regression to improve out-of-sample stability.
