# Constant of Integration

**Topic:** Calculus
**Tags:** calculus, integration, antiderivative, indefinite-integral, initial-conditions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

When computing an indefinite integral, the **constant of integration** $C$ represents the family of all possible antiderivatives. Because the derivative of any constant is zero, differentiation destroys constant information; integration therefore recovers a function only up to an unknown additive constant. A specific value of $C$ is pinned down by imposing an initial or boundary condition.

## Key Formula

If $F'(x) = f(x)$, then every antiderivative of $f$ has the form:

$$\int f(x) \, dx = F(x) + C, \qquad C \in \mathbb{R}$$

Given an initial condition $F(x_0) = y_0$, the constant is determined uniquely:

$$C = y_0 - F(x_0)$$

## Example

A continuously compounding account grows at an instantaneous rate $r = 0.05$. The balance $V(t)$ satisfies $V'(t) = 0.05\,V(t)$, which integrates to:

$$V(t) = A \, e^{0.05t} + C$$

However, since the equation is linear and homogeneous, the general solution is:

$$V(t) = C \, e^{0.05t}$$

Imposing the initial condition $V(0) = 1000$ gives $C = 1000$, so:

$$V(t) = 1000 \, e^{0.05t}$$

Without the initial deposit of £1,000, the solution would be undetermined — any starting balance is mathematically valid.

## Remember

In options pricing, the Black-Scholes PDE has infinitely many solutions. The constant of integration (or its PDE analogue, the free function arising from integration) is fixed by the **terminal payoff condition** — for a European call, $V(S, T) = \max(S - K, 0)$. The payoff is not just a boundary detail; it is the unique piece of information that selects one solution from the infinite family, determining the option's fair value at all earlier times.
