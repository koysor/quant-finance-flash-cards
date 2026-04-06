# Tangents and Normals

**Topic:** Calculus
**Tags:** tangent, normal, gradient, derivative, linear approximation, delta, hedging
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **tangent** to a curve $y = f(x)$ at the point $(a, f(a))$ is the straight line that touches the curve at that point with gradient $f'(a)$. The **normal** is the line through the same point perpendicular to the tangent, with gradient $-1/f'(a)$.

## Key Formula

**Tangent at $(a, f(a))$:**

$$y - f(a) = f'(a)(x - a)$$

**Normal at $(a, f(a))$:**

$$y - f(a) = -\frac{1}{f'(a)}(x - a)$$

If $f'(a) = 0$ (stationary point), the tangent is horizontal and the normal is vertical.

## Example

Find the tangent and normal to $y = x^2$ at the point $(3, 9)$.

$f'(x) = 2x$, so $f'(3) = 6$.

**Tangent:** $y - 9 = 6(x - 3)$ → $y = 6x - 9$.

**Normal:** $y - 9 = -\tfrac{1}{6}(x - 3)$ → $y = -\tfrac{1}{6}x + \tfrac{19}{2}$.

## Remember

The tangent approximation is the mathematical foundation of **delta hedging**. The Black-Scholes delta $\Delta = \partial C/\partial S$ is the gradient of the option price curve at the current stock price — exactly the tangent-line slope. When a trader holds $-\Delta$ shares per option, they are locally replacing the curved option payoff with its tangent line, making the portfolio instantaneously insensitive to small moves in $S$. The hedging error (gamma P&L) comes from the curvature of the curve away from the tangent — a second-order effect captured by gamma, just as the tangent line ignores the second derivative.
