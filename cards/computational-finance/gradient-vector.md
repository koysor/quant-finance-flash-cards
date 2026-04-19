# Gradient Vector

**Topic:** Computational Finance
**Tags:** gradient, partial derivatives, optimisation, gradient descent, cost function, machine learning
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **gradient vector** $\nabla J(\boldsymbol{\theta})$ is the vector of all partial derivatives of a scalar cost function $J$ with respect to each model parameter $\theta_j$. It points in the direction of steepest ascent of the loss surface; gradient descent subtracts a scaled version of it at each training step.

## Key Formula

For parameters $\boldsymbol{\theta} = (\theta_0, \theta_1, \ldots, \theta_n)^\top$:

$$\nabla J(\boldsymbol{\theta}) = \begin{pmatrix} \dfrac{\partial J}{\partial \theta_0} \\[6pt] \dfrac{\partial J}{\partial \theta_1} \\[4pt] \vdots \\[4pt] \dfrac{\partial J}{\partial \theta_n} \end{pmatrix}$$

For the MSE cost function $J = \frac{1}{N}\|\mathbf{X}\boldsymbol{\theta} - \mathbf{y}\|^2$, the gradient is:

$$\nabla J = \frac{2}{N}\mathbf{X}^\top(\mathbf{X}\boldsymbol{\theta} - \mathbf{y})$$

Setting $\nabla J = \mathbf{0}$ recovers the OLS normal equation.

## Example

Linear regression with two parameters $(\theta_0, \theta_1)$. At the current estimate, $\partial J/\partial \theta_0 = -0.4$ and $\partial J/\partial \theta_1 = 0.8$. The gradient points right-and-down in parameter space, so gradient descent moves $\theta_0$ up and $\theta_1$ down.

## Remember

In quantitative finance, the gradient vector is computed at every iteration of model calibration — fitting Heston parameters to the implied volatility surface, training a credit scoring neural network, or minimising a portfolio tracking error. The matrix form $\nabla J = \frac{2}{N}\mathbf{X}^\top(\mathbf{X}\boldsymbol{\theta} - \mathbf{y})$ shows that the gradient is a linear combination of the residuals weighted by the feature values — exactly the OLS score equations, linking ML optimisation directly to classical econometrics.
