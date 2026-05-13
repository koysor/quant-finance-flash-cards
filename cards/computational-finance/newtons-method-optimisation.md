# Newton's Method for Optimisation

**Topic:** Computational Finance
**Tags:** newton's method, hessian, quadratic convergence, portfolio optimisation, l-bfgs, second-order
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Newton's method for optimisation** finds the minimum of a cost function by locally approximating it as a quadratic using second-order information (the Hessian matrix) and jumping directly to that quadratic's minimum. It converges far faster than gradient descent but requires computing and inverting the $n \times n$ Hessian at each step.

## Key Formula

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \mathbf{H}^{-1}(\boldsymbol{\theta}_t)\;\nabla J(\boldsymbol{\theta}_t)$$

where $\mathbf{H}(\boldsymbol{\theta}) = \nabla^2 J(\boldsymbol{\theta})$ is the Hessian matrix of second partial derivatives.

| Method | Step formula | Convergence |
|---|---|---|
| Gradient descent | $\boldsymbol{\theta} - \eta\,\nabla J$ | Linear: fixed fraction per step |
| Newton's method | $\boldsymbol{\theta} - \mathbf{H}^{-1}\nabla J$ | Quadratic: digits correct roughly doubles each step |

For **quadratic** $J$ (e.g. OLS, Markowitz), $\mathbf{H}$ is constant and Newton's method reaches the exact minimum in **one step**.

## Example

**Markowitz mean-variance optimisation:** $J(\mathbf{w}) = \mathbf{w}^\top \Sigma\, \mathbf{w} - \lambda\, \boldsymbol{\mu}^\top \mathbf{w}$.

The Hessian is $\mathbf{H} = 2\Sigma$ (constant), so Newton's method takes a single step:

$$\mathbf{w}^* = \mathbf{w}_0 - (2\Sigma)^{-1}(-\lambda\,\boldsymbol{\mu}) = \frac{\lambda}{2}\,\Sigma^{-1}\boldsymbol{\mu}$$

This is exactly the closed-form Markowitz solution — Newton's method recovers it instantly because the objective is quadratic.

## Remember

Newton's method underpins the most important closed-form results in quantitative finance. OLS normal equations $\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ are a single Newton step on the MSE loss. For non-quadratic problems (Heston calibration, neural network training), computing the full Hessian is prohibitive — so practitioners use **L-BFGS**, which approximates $\mathbf{H}^{-1}$ from recent gradient history, achieving near-quadratic convergence at a fraction of the cost.
