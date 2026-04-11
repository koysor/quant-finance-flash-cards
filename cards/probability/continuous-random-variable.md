# Continuous Random Variable

**Topic:** Probability
**Tags:** continuous random variable, PDF, density, interval probability, support
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **continuous random variable** $X$ takes values on an interval (or union of intervals) and is described by a **probability density function (PDF)** $f_X(x)$. No single point has positive probability; only intervals carry probability.

$$P(X = x) = 0 \quad \text{for every } x, \qquad P(a \leq X \leq b) = \int_a^b f_X(x)\,dx$$

## Key Formula

**PDF properties:**

$$f_X(x) \geq 0, \qquad \int_{-\infty}^{\infty} f_X(x)\,dx = 1$$

**CDF from PDF:**

$$F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t)\,dt, \qquad f_X(x) = F_X'(x)$$

**Expectation and variance:**

$$E[X] = \int_{-\infty}^{\infty} x\,f_X(x)\,dx, \qquad \text{Var}(X) = \int_{-\infty}^{\infty} (x - E[X])^2\,f_X(x)\,dx$$

**Contrast with discrete:**

| | Discrete | Continuous |
|---|---|---|
| Point probability | $P(X=k) = p_X(k) > 0$ | $P(X=x) = 0$ |
| Interval probability | Sum of PMF values | Integral of PDF |
| PDF/PMF value | In $[0,1]$ | $\geq 0$, can exceed 1 |

## Example

A log-return $R \sim \mathcal{N}(0.001, 0.02^2)$. The probability of a loss worse than 3% is:

$$P(R < -0.03) = \Phi\!\left(\frac{-0.03 - 0.001}{0.02}\right) = \Phi(-1.55) \approx 6.1\%$$

Note: $f_R(-0.03)$ is a density value (here $\approx 5.2$ per unit return), not a probability. To get a probability, integrate over an interval.

## Remember

The key insight for continuous random variables is that probability lives in **areas under a curve**, not at individual points. This matters practically: a model that says log-returns are exactly zero is a statement about a zero-probability event. In derivatives pricing, every Black-Scholes integral — computing expected payoffs — is an application of continuous RV theory: the option price is the integral of the payoff function weighted by the risk-neutral PDF of the terminal stock price.
