# Gradient

**Topic:** Calculus
**Tags:** gradient, multivariable calculus, partial derivatives, optimisation, risk sensitivity
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **gradient** of a scalar function $f(x_1, x_2, \ldots, x_n)$ is the vector of all its partial derivatives. It points in the direction of steepest increase of $f$ and its magnitude gives the rate of that increase. At any point, the gradient is perpendicular to the level curves (contours) of $f$.

## Key Formula

$$\nabla f = \left(\frac{\partial f}{\partial x_1},\, \frac{\partial f}{\partial x_2},\, \ldots,\, \frac{\partial f}{\partial x_n}\right)$$

In two dimensions, for $f(x, y)$:

$$\nabla f = \left(\frac{\partial f}{\partial x},\, \frac{\partial f}{\partial y}\right)$$

The **directional derivative** in the direction of unit vector $\hat{u}$ is:

$$D_{\hat{u}} f = \nabla f \cdot \hat{u}$$

At a local minimum or maximum, the gradient is zero: $\nabla f = \mathbf{0}$.

## Example

Let $f(x, y) = x^2 + 4y^2$ represent a simplified quadratic loss surface (e.g. a portfolio variance as a function of two weights). Then:

$$\nabla f = (2x,\, 8y)$$

At the point $(3, 1)$: $\nabla f = (6, 8)$, with magnitude $\|\nabla f\| = \sqrt{36 + 64} = 10$.

The gradient $(6, 8)$ tells us the direction of steepest ascent — to minimise $f$, gradient descent takes a step in the opposite direction: $(-6, -8)$.

## Remember

In quantitative finance, the gradient of a portfolio's loss function with respect to its weights is the core object in **gradient descent** optimisation — the iterative algorithm used to calibrate model parameters, fit risk factor exposures, and train machine learning models for pricing. The condition $\nabla f = \mathbf{0}$ identifies candidate optima and is directly used when solving for minimum-variance portfolio weights in mean-variance optimisation.
