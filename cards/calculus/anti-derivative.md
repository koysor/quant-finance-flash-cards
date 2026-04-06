# Anti-Derivative

**Topic:** Calculus
**Tags:** calculus, integration, antiderivative, indefinite integral, constant of integration
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **anti-derivative** (or primitive) of a function $f(x)$ is any function $F(x)$ such that $F'(x) = f(x)$. Because the derivative of any constant is zero, anti-derivatives are not unique — they form a family $F(x) + C$, where $C$ is an arbitrary constant of integration. Finding an anti-derivative is the core operation of indefinite integration.

## Key Formula

$$F'(x) = f(x) \implies \int f(x)\, dx = F(x) + C$$

**Power rule anti-derivative** (for $n \neq -1$):

$$\int x^n\, dx = \frac{x^{n+1}}{n+1} + C$$

**Exponential anti-derivative:**

$$\int e^{ax}\, dx = \frac{1}{a} e^{ax} + C, \qquad a \neq 0$$

**Logarithmic anti-derivative:**

$$\int \frac{1}{x}\, dx = \ln|x| + C$$

## Example

Find the anti-derivative of $f(x) = 3x^2 + 2x - 5$.

Apply the power rule term by term:

$$F(x) = \int (3x^2 + 2x - 5)\, dx = x^3 + x^2 - 5x + C$$

**Verification:** Differentiate $F(x)$:

$$F'(x) = 3x^2 + 2x - 5 = f(x) \checkmark$$

The constant $C$ is fixed once a boundary condition is known — for example, if $F(0) = 4$, then $C = 4$.

## Remember

The constant of integration $C$ is not a technicality — in finance it carries real economic meaning. When solving an ordinary differential equation for a bond price or an option value, $C$ is determined by the **boundary condition**: the option's payoff at expiry, or the face value of the bond at maturity. Without pinning $C$ to a boundary condition the solution is not unique and has no financial content. The whole machinery of solving Black-Scholes (which reduces to finding an anti-derivative once transformed to the heat equation) rests on this step.
