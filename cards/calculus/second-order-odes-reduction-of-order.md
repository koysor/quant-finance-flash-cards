# Second-Order ODEs: Reduction of Order

**Topic:** Calculus
**Tags:** ODE, second order, reduction of order, substitution, non-linear
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A second-order ODE that is missing either $x$ or $y$ explicitly can be reduced to a first-order equation by the substitution $p = y'$. Solve for $p$, then integrate once more to recover $y$.

## Key Formula

$$p = \frac{dy}{dx} \;\Longrightarrow\; \frac{d^2y}{dx^2} = \frac{dp}{dx} \quad (y \text{ missing}), \qquad \frac{d^2y}{dx^2} = p\,\frac{dp}{dy} \quad (x \text{ missing})$$

Choose the form by which variable is absent. The case $y'' = f(x)$ is simply integrated twice.

## Example

Solve $y'' + 2x(y')^2 = 0$ with $y(0) = 0$ and $y'(0) = 1$. Here $y$ is missing, so with $p = y'$:

$$\frac{dp}{dx} = -2xp^2 \;\Longrightarrow\; \int \frac{dp}{p^2} = -\int 2x\,dx \;\Longrightarrow\; -\frac{1}{p} = -x^2 + c$$

$p(0) = 1$ gives $c = -1$, so $p = \dfrac{1}{1 + x^2}$ and, integrating, $y = \arctan x$.

## Remember

Reduction of order is the escape route when an equation is second order but not linear, so the standard methods for linear equations do not apply. It appears whenever a PDE is reduced to an ODE by a similarity or travelling-wave substitution.
