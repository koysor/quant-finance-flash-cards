# Variable Separable Equations

**Topic:** Calculus
**Tags:** ODE, separation of variables, first order, geometric Brownian motion, drift
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A first-order ODE is **separable** when the right-hand side factorises into a function of $x$ times a function of $y$. The variables are then moved to opposite sides and both sides are integrated.

## Key Formula

$$\frac{dy}{dx} = f(x)\,g(y) \;\Longrightarrow\; \int \frac{dy}{g(y)} = \int f(x)\,dx$$

Combine the two constants of integration into a single $c$. Where $g(y) = 0$ the division loses the constant solutions, so check for them separately.

## Example

Solve $\dfrac{dy}{dx} = xy$ with $y(0) = 2$.

$$\int \frac{dy}{y} = \int x\,dx \;\Longrightarrow\; \ln y = \frac{x^2}{2} + c$$

so $y = Ae^{x^2/2}$, and $y(0) = 2$ gives $A = 2$: $\;y = 2e^{x^2/2}$.

## Remember

The deterministic part of a stock price is separable. From $\dfrac{dS}{dt} = \mu S$, $\int \dfrac{dS}{S} = \int \mu\,dt$ gives $\ln S = \mu t + c$, so $S = S_0 e^{\mu t}$: continuous compounding at rate $\mu$, and the drift term of geometric Brownian motion. Get all the $y$ terms on one side and all the $x$ terms on the other, then integrate.
