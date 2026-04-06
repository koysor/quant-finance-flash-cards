# Implicit Differentiation

**Topic:** Calculus
**Tags:** implicit differentiation, chain rule, partial derivatives, yield, Greeks
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Implicit differentiation** is the technique of finding $\frac{dy}{dx}$ when $y$ is defined implicitly by an equation $F(x, y) = 0$, without first solving for $y$ explicitly. Both sides of the equation are differentiated with respect to $x$, treating $y$ as a function of $x$ and applying the chain rule wherever $y$ appears.

## Key Formula

Given $F(x, y) = 0$, differentiate both sides with respect to $x$:

$$\frac{d}{dx}\bigl[F(x, y)\bigr] = 0$$

Applying the chain rule to any term involving $y$:

$$\frac{\partial F}{\partial x} + \frac{\partial F}{\partial y} \cdot \frac{dy}{dx} = 0$$

Solving for the derivative:

$$\frac{dy}{dx} = -\frac{\partial F / \partial x}{\partial F / \partial y}$$

This requires $\frac{\partial F}{\partial y} \neq 0$ at the point of interest.

## Example

Consider a zero-coupon bond priced at $P = 95$ with face value $F = 100$ and maturity $n = 2$ years. The yield $y$ satisfies:

$$F(P, y) = P - \frac{100}{(1 + y)^2} = 0$$

Differentiate implicitly with respect to $P$:

$$1 + \frac{200}{(1 + y)^3} \cdot \frac{dy}{dP} = 0$$

$$\frac{dy}{dP} = -\frac{(1 + y)^3}{200}$$

With $y \approx 0.0260$ (about 2.60%):

$$\frac{dy}{dP} \approx -\frac{(1.0260)^3}{200} \approx -0.00540$$

A £1 rise in price lowers the yield by approximately 0.54 basis points per unit — the inverse price-yield relationship without ever solving for $y$ directly.

## Remember

In derivatives pricing, implied volatility $\sigma_{\text{imp}}$ is extracted from the Black-Scholes formula by solving $C_{\text{BS}}(S, K, r, T, \sigma) - C_{\text{mkt}} = 0$ implicitly. The Newton-Raphson update step uses implicit differentiation: the step size is $-F / (\partial C_{\text{BS}} / \partial \sigma)$, where $\partial C_{\text{BS}} / \partial \sigma$ is vega. Every iteration of an implied-vol solver is an application of implicit differentiation — the technique converts the intractable question "what $\sigma$ gives this price?" into a computable derivative that guides the numerical search.
