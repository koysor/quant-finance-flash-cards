# Cost Function Minimisation

**Topic:** Computational Finance
**Tags:** optimisation, first-order conditions, convexity, gradient, analytical solution, model calibration
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Cost function minimisation** is the process of finding the parameter vector $\boldsymbol{\theta}^*$ that makes a cost function $J(\boldsymbol{\theta})$ as small as possible. It is the mathematical foundation of all model fitting in machine learning and quantitative finance: training a model, calibrating a pricer, or estimating regression coefficients are all instances of the same optimisation problem.

## Key Formula

**First-order necessary condition** (holds at any minimum):

$$\nabla_{\boldsymbol{\theta}}\, J(\boldsymbol{\theta}^*) = \mathbf{0}$$

**Second-order sufficient condition** for a strict local minimum:

$$\mathbf{H}(\boldsymbol{\theta}^*) = \nabla^2 J(\boldsymbol{\theta}^*) \succ 0 \quad \text{(Hessian is positive definite)}$$

For **convex** $J$, every stationary point is a global minimum. Two solution routes:

| Route | When | Formula |
|-------|------|---------|
| Analytical (closed-form) | $\nabla J = 0$ has an explicit solution | e.g. normal equations: $\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ |
| Numerical (iterative) | No closed form, or too expensive to invert | gradient descent: $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta\,\nabla J(\boldsymbol{\theta}_t)$ |

## Example

**OLS regression** (closed-form):  
$J(\boldsymbol{\beta}) = \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2$.  
Setting $\nabla J = -2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) = \mathbf{0}$ gives $\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ — one matrix inversion, exact solution.

**Heston calibration** (numerical):  
$J(\kappa,\theta,\xi,\rho,v_0) = \sum_{i=1}^{20}(C_{\text{model}}^{(i)} - C_{\text{mkt}}^{(i)})^2$.  
No closed form exists; gradient descent (or Nelder–Mead, L-BFGS) iterates to convergence. The cost surface is non-convex, so multiple restarts are used to reduce the risk of a poor local minimum.

## Remember

Every model in quantitative finance is ultimately fitted by solving a cost-function minimisation problem. The critical practical question is **convex or not?**:

- **Convex $J$** (OLS, ridge regression, logistic regression): gradient descent is guaranteed to find the global minimum; closed-form solutions exist for many linear cases and are faster.
- **Non-convex $J$** (Heston, neural networks, SABR): gradient-based methods converge to a **local** minimum; the solution depends on the starting point. Practitioners use multiple restarts, global optimisers, or regularisation to mitigate this.

Adding a regularisation term $\lambda\|\boldsymbol{\theta}\|^2$ to $J$ penalises large parameters, improving out-of-sample performance and often improving the conditioning of the optimisation landscape — the same idea underlies ridge regression and weight decay in neural networks.
