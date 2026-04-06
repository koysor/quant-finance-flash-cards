# Stationary Points

**Topic:** Calculus
**Tags:** stationary point, maximum, minimum, inflection, second derivative, optimisation, critical point
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **stationary point** of $f(x)$ is a point where $f'(x) = 0$ — the tangent to the curve is horizontal. Stationary points are classified as **local maxima**, **local minima**, or **points of inflection** using the second derivative test.

## Key Formula

**First derivative test:** set $f'(x) = 0$ to find stationary points.

**Second derivative test:**

$$f''(x) > 0 \implies \text{local minimum}, \qquad f''(x) < 0 \implies \text{local maximum}$$

$$f''(x) = 0 \implies \text{inconclusive} \text{ — check sign of } f'(x) \text{ either side}$$

A **point of inflection** occurs where $f''(x) = 0$ and $f''$ changes sign.

## Example

Find and classify the stationary points of $f(x) = x^3 - 3x$.

$f'(x) = 3x^2 - 3 = 0 \implies x = \pm 1$.

$f''(x) = 6x$.

At $x = 1$: $f''(1) = 6 > 0$ → local minimum, $f(1) = -2$.

At $x = -1$: $f''(-1) = -6 < 0$ → local maximum, $f(-1) = 2$.

## Remember

Portfolio optimisation is fundamentally about finding stationary points. The **Markowitz mean-variance problem** minimises portfolio variance subject to a target return by setting the derivative of the Lagrangian to zero — a higher-dimensional version of $f'(x) = 0$. The second-order condition ($f'' > 0$) corresponds to the covariance matrix being positive definite, which guarantees the stationary point is a genuine minimum and not a saddle. Every efficient frontier point is a stationary point of this Lagrangian.
