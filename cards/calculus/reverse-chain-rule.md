# Reverse Chain Rule

**Topic:** Calculus
**Tags:** integration, chain rule, reverse chain rule, inspection, composite function, antiderivative
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **reverse chain rule** (also called integration by inspection) is the shortcut for integrating a composite function when the integrand contains a function $f'(g(x))\cdot g'(x)$ — the derivative of an outer function multiplied by the derivative of the inner function. It is the direct reversal of the chain rule without explicitly substituting.

## Key Formula

$$\int f'(g(x))\cdot g'(x)\, dx = f(g(x)) + C$$

**Adjusting for a constant multiple:** if $g'(x)$ is off by a constant factor $k$, multiply inside by $k$ and divide outside:

$$\int f'(g(x))\, dx = \frac{1}{k}\int f'(g(x))\cdot k\, dx \quad \text{when } g'(x) = k$$

## Example

Evaluate $\displaystyle\int 6x^2(x^3 + 4)^5\, dx$.

Identify: inner function $g(x) = x^3 + 4$, so $g'(x) = 3x^2$. Outer function $f(u) = u^5$.

The integrand has $6x^2 = 2 \times 3x^2$, so:

$$\int 6x^2(x^3+4)^5\, dx = 2\int 3x^2(x^3+4)^5\, dx = 2 \cdot \frac{(x^3+4)^6}{6} + C = \frac{(x^3+4)^6}{3} + C$$

## Remember

The reverse chain rule is the integration technique behind every **change-of-measure** calculation in derivative pricing. When computing $E^Q[f(S_T)]$ under the risk-neutral measure, the Radon-Nikodym derivative appears as the "missing factor" $g'(x)$ in the integrand. Recognising this structure — an outer function times the derivative of the inner function — is what allows the change of measure to simplify the integral, ultimately leading to the Black-Scholes formula via a Gaussian integral with a shifted mean.
