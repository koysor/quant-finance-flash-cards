# Cumulative Distribution Function

**Topic:** Probability
**Tags:** distributions, probability, quantiles, CDF
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

The cumulative distribution function (CDF) gives the probability that a random variable $X$ takes a value less than or equal to $x$:

$$F(x) = P(X \leq x)$$

Every CDF has three properties:

- $F(x)$ is non-decreasing
- $\displaystyle\lim_{x \to -\infty} F(x) = 0$ and $\displaystyle\lim_{x \to \infty} F(x) = 1$
- For continuous distributions, $F(x) = \displaystyle\int_{-\infty}^{x} f(t)\,dt$, where $f$ is the PDF

## Key Formula

The CDF of the standard normal distribution is denoted $\Phi(z)$:

$$\Phi(z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-t^2/2}\,dt$$

The **quantile function** (inverse CDF) reverses this: given a probability $p$, it returns the value $z$ such that $\Phi(z) = p$.

$$z_p = \Phi^{-1}(p)$$

## Example

A portfolio's daily return is modelled as $X \sim N(0.001, 0.02^2)$. What is the probability of a negative return?

Standardise: $z = \frac{0 - 0.001}{0.02} = -0.05$

$$P(X < 0) = \Phi(-0.05) \approx 0.480$$

There is roughly a 48% chance of a negative daily return.

## Remember

The CDF appears throughout quantitative finance. The Black-Scholes formula uses $\Phi(d_1)$ and $\Phi(d_2)$ — cumulative normal probabilities — to price options. Value at Risk is defined as a quantile of the loss distribution, which is the inverse CDF evaluated at the confidence level. Monte Carlo simulation uses the inverse CDF to transform uniform random numbers into any target distribution. Mastering the CDF and its inverse is essential for pricing, risk, and simulation.
