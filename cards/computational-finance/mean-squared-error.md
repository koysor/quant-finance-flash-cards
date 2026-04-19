# Mean Squared Error

**Topic:** Computational Finance
**Tags:** MSE, cost function, loss function, regression, convex optimisation, OLS
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Mean Squared Error (MSE)** is the standard cost function for regression models. It measures the average squared deviation between model predictions $\hat{y}^{(i)}$ and observed targets $y^{(i)}$, penalising large errors disproportionately. Because it is convex and differentiable everywhere, it is well-suited to gradient descent optimisation.

## Key Formula

$$J(\boldsymbol{\theta}) = \frac{1}{N}\sum_{i=1}^{N}\!\left(\hat{y}^{(i)} - y^{(i)}\right)^2$$

Partial derivative with respect to parameter $\theta_j$ (used in gradient descent):

$$\frac{\partial J}{\partial \theta_j} = \frac{2}{N}\sum_{i=1}^{N}\!\left(\hat{y}^{(i)} - y^{(i)}\right) x_j^{(i)}$$

The closed-form OLS minimiser is $\hat{\boldsymbol{\theta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$, equivalent to setting all partial derivatives to zero.

## Example

A model predicts next-month equity returns. True returns: $[2\%, -1\%, 3\%]$; predictions: $[1.5\%, -0.5\%, 2\%]$. Residuals: $[0.5, -0.5, 1.0]$. MSE $= (0.25 + 0.25 + 1.00)/3 = 0.50$ (percentage-squared). The 3% miss contributes 4× more than each 0.5% miss.

## Remember

MSE is the loss function behind OLS regression and the normal equations used everywhere in factor model estimation. Its squared penalty means a prediction error of 2% costs 4× as much as 1%, which is economically sensible in finance: a model that occasionally produces large mispricings is far more dangerous than one with many small errors. This is why MSE-minimising estimators implicitly assume normally distributed residuals.
