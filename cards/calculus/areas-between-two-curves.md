# Areas Between Two Curves

**Topic:** Calculus
**Tags:** integration, area, definite integral, bounds, curves, payoff, spread
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **area between two curves** $y = f(x)$ and $y = g(x)$ is found by integrating the difference $f(x) - g(x)$ over the interval where one curve lies above the other. Care is needed when the curves cross — the region must be split at intersection points and absolute values taken.

## Key Formula

If $f(x) \geq g(x)$ on $[a, b]$:

$$A = \int_a^b \bigl[f(x) - g(x)\bigr]\, dx$$

**When curves cross** at $x = c \in (a, b)$:

$$A = \int_a^c \bigl[f(x) - g(x)\bigr]\, dx + \int_c^b \bigl[g(x) - f(x)\bigr]\, dx$$

**Step 1:** Find intersection points by solving $f(x) = g(x)$.

**Step 2:** Determine which curve is on top in each sub-interval.

**Step 3:** Integrate $|f(x) - g(x)|$ over each sub-interval.

## Example

Find the area enclosed between $y = x^2$ and $y = x + 2$.

Intersections: $x^2 = x + 2 \implies x^2 - x - 2 = 0 \implies x = -1$ or $x = 2$.

On $[-1, 2]$: $x + 2 \geq x^2$, so:

$$A = \int_{-1}^{2}(x + 2 - x^2)\, dx = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2} = \left(2 + 4 - \frac{8}{3}\right) - \left(\frac{1}{2} - 2 + \frac{1}{3}\right) = \frac{9}{2}$$

## Remember

The area between two curves is the geometric model for the **payoff of a spread strategy**. A bull spread is long a call at strike $K_1$ and short a call at $K_2 > K_1$; its payoff is the difference between two call-payoff curves, and its expected value under the risk-neutral measure is the integral of that difference over the stock price distribution — an area-between-curves calculation. The **break-even analysis** of any two competing financial models (different yield curves, different pricing models) is determined by the region where one model's value exceeds the other's.
