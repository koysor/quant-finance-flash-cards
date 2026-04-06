# Indefinite Integral

**Topic:** Calculus
**Tags:** calculus, integration, antiderivative, constant of integration, differential equations
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **indefinite integral** is the general antiderivative of a function: it finds a family of functions $F(x)$ whose derivative equals the integrand $f(x)$. Because any constant vanishes on differentiation, the result always includes an arbitrary constant $C$, representing infinitely many antiderivatives shifted vertically.

## Key Formula

$$\int f(x)\,dx = F(x) + C \qquad \text{where } F'(x) = f(x)$$

Common antiderivatives:

$$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1), \qquad \int e^{ax}\,dx = \frac{1}{a}e^{ax} + C$$

$$\int \frac{1}{x}\,dx = \ln|x| + C, \qquad \int e^x\,dx = e^x + C$$

## Example

Find $\displaystyle\int (3x^2 + 2x - 5)\,dx$.

Apply the power rule term by term:

$$\int 3x^2\,dx = x^3, \qquad \int 2x\,dx = x^2, \qquad \int -5\,dx = -5x$$

$$\therefore \int (3x^2 + 2x - 5)\,dx = x^3 + x^2 - 5x + C$$

**Verify:** $\dfrac{d}{dx}(x^3 + x^2 - 5x + C) = 3x^2 + 2x - 5$ ✓

## Remember

In quantitative finance, the constant $C$ is pinned down by an **initial or boundary condition**. When solving the Black-Scholes PDE for a derivative price $V(S, t)$, integrating with respect to $S$ introduces a constant that is fixed by the option's terminal payoff at expiry — without the boundary condition the solution is indeterminate, just as the indefinite integral alone does not specify a unique function.
