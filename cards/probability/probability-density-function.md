# Probability Density Function

**Topic:** Probability
**Tags:** distributions, probability, continuous, density, integration
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The probability density function (PDF) describes the relative likelihood of a continuous random variable taking a particular value. Unlike a discrete probability, the PDF value at a single point is **not** a probability — instead, probabilities are obtained by integrating the PDF over an interval:

$$P(a \leq X \leq b) = \int_a^b f(x)\,dx$$

A valid PDF must satisfy two conditions:

- $f(x) \geq 0$ for all $x$
- $\displaystyle\int_{-\infty}^{\infty} f(x)\,dx = 1$

## Key Formula

The PDF of the standard normal distribution $Z \sim N(0, 1)$ is:

$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$$

For any continuous distribution, the expected value is computed from the PDF:

$$E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx$$

## Example

A stock's log-return $X$ has PDF $f(x) = 2e^{-2x}$ for $x \geq 0$ (an exponential distribution with $\lambda = 2$). What is the probability the return exceeds 0.5?

$$P(X > 0.5) = \int_{0.5}^{\infty} 2e^{-2x}\,dx = e^{-1} \approx 0.368$$

There is roughly a 36.8% chance the return exceeds 0.5.

## Remember

The PDF is the starting point for every continuous model in quantitative finance. Option pricing formulas like Black-Scholes are derived by integrating the payoff function weighted by the PDF of the underlying's return distribution. When the PDF changes shape — fatter tails, skewness — so do the fair prices of options, which is why understanding the density is essential for accurate pricing and risk measurement.
