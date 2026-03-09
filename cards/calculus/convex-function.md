# Convex Function

**Topic:** Calculus
**Tags:** convexity, second derivative, curvature, jensen, optimisation
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

A function $f$ is **convex** if the line segment between any two points on its graph lies on or above the graph. Equivalently, $f$ is convex if its second derivative is non-negative everywhere: $f''(x) \geq 0$. A function is **concave** if $-f$ is convex, i.e. $f''(x) \leq 0$. Convexity captures the idea of "curving upward" — the slope is increasing.

## Key Formula

**Algebraic definition** (for all $x, y$ and $\lambda \in [0, 1]$):

$$f\bigl(\lambda x + (1 - \lambda)y\bigr) \leq \lambda\,f(x) + (1 - \lambda)\,f(y)$$

**Second-derivative test:**

$$f''(x) \geq 0 \;\text{for all } x \quad \Longrightarrow \quad f \text{ is convex}$$

$$f''(x) \leq 0 \;\text{for all } x \quad \Longrightarrow \quad f \text{ is concave}$$

| Function | $f''(x)$ | Convexity |
|---|---|---|
| $x^2$ | $2 > 0$ | Convex |
| $e^x$ | $e^x > 0$ | Convex |
| $\ln x$ | $-1/x^2 < 0$ | Concave |
| $\sqrt{x}$ | $-1/(4x^{3/2}) < 0$ | Concave |

## Example

Consider $f(x) = x^2$ with two points $x = 2$ and $y = 8$. The midpoint ($\lambda = 0.5$):

**Left side:** $f\!\left(\frac{2 + 8}{2}\right) = f(5) = 25$

**Right side:** $\frac{f(2) + f(8)}{2} = \frac{4 + 64}{2} = 34$

Since $25 \leq 34$, the function value at the midpoint lies below the chord — confirming convexity. The gap ($34 - 25 = 9$) grows with the distance between the points and the curvature of $f$.

## Remember

Convexity is one of the most consequential properties in quantitative finance. An option's value is a convex function of the underlying price — this is why gamma (the second derivative $\partial^2 V / \partial S^2$) is positive for long option positions, and why a delta-hedged option holder profits from large moves in either direction. Jensen's inequality says $E[f(X)] \geq f(E[X])$ for convex $f$, which is the mathematical reason that optionality has value: the expected payoff of a convex function of a random variable exceeds the payoff at the expected value. This same principle explains volatility drag ($\ln$ is concave, so $E[\ln(1+R)] < \ln(E[1+R])$), the convexity adjustment in bond pricing, and why diversification reduces portfolio variance.
