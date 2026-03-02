# Jensen's Inequality

**Topic:** Probability
**Tags:** Jensen's inequality, convexity, expected value, volatility drag, risk, compounding
**Author:** Claude Opus 4.6

---

## Definition

**Jensen's inequality** states that for a convex function $f$ and a random variable $X$, the expected value of the function is at least as large as the function of the expected value: $\mathbb{E}[f(X)] \geq f(\mathbb{E}[X])$. For a concave function the inequality reverses. It formalises the idea that randomness interacts with curvature to shift expected outcomes.

## Key Formula

For a **convex** function $f$ (where $f'' \geq 0$):

$$\mathbb{E}[f(X)] \geq f\bigl(\mathbb{E}[X]\bigr)$$

For a **concave** function $f$ (where $f'' \leq 0$):

$$\mathbb{E}[f(X)] \leq f\bigl(\mathbb{E}[X]\bigr)$$

Equality holds if and only if $f$ is linear or $X$ is constant (non-random).

| Function | Convexity | Jensen says |
|---|---|---|
| $f(x) = x^2$ | Convex | $\mathbb{E}[X^2] \geq (\mathbb{E}[X])^2$ |
| $f(x) = e^x$ | Convex | $\mathbb{E}[e^X] \geq e^{\mathbb{E}[X]}$ |
| $f(x) = \ln x$ | Concave | $\mathbb{E}[\ln X] \leq \ln(\mathbb{E}[X])$ |

## Example

A stock has equal probability of returning $+30\%$ or $-10\%$. The arithmetic mean return is $\frac{0.30 + (-0.10)}{2} = 10\%$. But the geometric mean (compound) return is $\sqrt{1.30 \times 0.90} - 1 = \sqrt{1.17} - 1 \approx 8.2\%$. The geometric mean is lower because $\ln$ is concave: $\mathbb{E}[\ln(1+R)] < \ln(\mathbb{E}[1+R])$. This gap is the volatility drag.

## Remember

Jensen's inequality is the mathematical reason behind volatility drag: since $\ln$ is concave, the expected log return is always less than the log of the expected return. In quantitative finance, this means that the median compound growth rate is lower than the arithmetic mean return, and the gap grows with volatility ($\frac{1}{2}\sigma^2$). Jensen's inequality also explains why diversification reduces risk — the portfolio variance is a convex function of weights, and averaging across assets reduces it.
