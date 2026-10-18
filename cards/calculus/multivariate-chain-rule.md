# The Multivariate Chain Rule

**Topic:** Calculus
**Tags:** chain rule, partial derivatives, total derivative, Ito lemma, multivariate
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

When a function $U(x, y, z)$ depends on intermediate variables that all depend on a common parameter $t$, the **total derivative** $dU/dt$ is the sum of one term per dependency path: the partial derivative of $U$ with respect to each intermediate variable, times that variable's derivative with respect to $t$.

## Key Formula

$$\frac{dU}{dt} = \frac{\partial U}{\partial x}\frac{dx}{dt} + \frac{\partial U}{\partial y}\frac{dy}{dt} + \frac{\partial U}{\partial z}\frac{dz}{dt}$$

Each partial derivative holds the other variables fixed; the total derivative on the left treats $t$ as the only free variable. Drawing the dependency tree and summing every route avoids missing a term.

## Example

Let $f(x, y) = x^2 + y^2$ with $x = \sin 2\theta$ and $y = \cos 2\theta$.

$$\frac{df}{d\theta} = 2x \cdot 2\cos 2\theta + 2y \cdot (-2\sin 2\theta) = 4\sin 2\theta\cos 2\theta - 4\cos 2\theta\sin 2\theta = 0$$

This is geometrically obvious: $x^2 + y^2 = 1$ for every $\theta$, so $f$ is constant.

## Remember

Itô's lemma is the multivariate chain rule applied to $V(S, t)$ where $S$ is stochastic, with one extra term from the random part. Ordinary calculus gives $dV = V_t\,dt + V_S\,dS$; the stochastic version adds $\tfrac{1}{2}\sigma^2 S^2 V_{SS}\,dt$. Knowing the deterministic rule cold is what lets you see exactly what the stochastic one adds.
