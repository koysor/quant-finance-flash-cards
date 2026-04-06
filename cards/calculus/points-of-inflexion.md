# Points of Inflexion

**Topic:** Calculus
**Tags:** inflexion, inflection, second derivative, concavity, curvature, gamma, convexity
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **point of inflexion** is a point on a curve where the concavity changes — from concave up (bowl shape, $f'' > 0$) to concave down (arch shape, $f'' < 0$), or vice versa. At such a point $f''(x) = 0$ and $f''$ changes sign. Note: $f''(x) = 0$ alone is necessary but not sufficient — $f''$ must change sign.

## Key Formula

**Conditions for a point of inflexion at $x = a$:**

1. $f''(a) = 0$ (or $f''$ does not exist)
2. $f''$ changes sign at $x = a$

**Concavity:**

$$f''(x) > 0 \implies \text{concave up (convex)}, \qquad f''(x) < 0 \implies \text{concave down (concave)}$$

A **stationary point of inflexion** occurs when simultaneously $f'(a) = 0$ and $f''(a) = 0$ with a sign change in $f''$.

## Example

Find the point of inflexion of $f(x) = x^3 - 3x^2 + 2$.

$f'(x) = 3x^2 - 6x$, $f''(x) = 6x - 6$.

Set $f''(x) = 0$: $x = 1$.

Check sign change: $f''(0) = -6 < 0$ (concave down); $f''(2) = 6 > 0$ (concave up). Sign changes ✓.

Point of inflexion at $(1, f(1)) = (1, 0)$.

## Remember

In options, the **gamma** $\Gamma = \partial^2 V / \partial S^2$ measures the curvature of the option price curve — it is the second derivative of option price with respect to stock price. A point of inflexion of the option price curve occurs where $\Gamma = 0$: the price curve changes from accelerating (positive gamma, long options) to decelerating (negative gamma, short options). For a vanilla call option, gamma is always positive but peaks near the money and decays toward zero deep in- or out-of-the-money — the gamma maximum is where the option price curve has its steepest change of concavity.
