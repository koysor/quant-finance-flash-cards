# Gamma Function

**Topic:** Probability
**Tags:** gamma function, factorial, distributions, calculus, continuous
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The Gamma function $\Gamma(z)$ is a continuous extension of the factorial to all positive real numbers (and complex numbers with positive real part). For positive integers it satisfies $\Gamma(n) = (n-1)!$, so it generalises the discrete factorial to a smooth, continuous function.

## Key Formula

The integral definition for $z > 0$:

$$\Gamma(z) = \int_0^{\infty} t^{z-1} e^{-t}\, dt$$

Key identities:

$$\Gamma(z + 1) = z\,\Gamma(z) \qquad \text{(recurrence relation)}$$

$$\Gamma(n) = (n-1)! \quad \text{for positive integers } n$$

$$\Gamma\!\left(\tfrac{1}{2}\right) = \sqrt{\pi}$$

The Gamma function appears in the normalisaton constants of many probability distributions. For the chi-squared distribution with $k$ degrees of freedom:

$$f(x) = \frac{x^{k/2 - 1}\,e^{-x/2}}{2^{k/2}\,\Gamma(k/2)}, \quad x > 0$$

## Example

Compute $\Gamma(5)$ using the recurrence relation:

$$\Gamma(5) = 4! = 4 \times 3 \times 2 \times 1 = 24$$

Now use the half-integer value to find the normalisation constant for a chi-squared distribution with $k = 3$ degrees of freedom:

$$\Gamma\!\left(\tfrac{3}{2}\right) = \tfrac{1}{2}\,\Gamma\!\left(\tfrac{1}{2}\right) = \tfrac{1}{2}\sqrt{\pi} \approx 0.886$$

This normalisation ensures the chi-squared PDF integrates to 1.

## Remember

The Gamma function is the hidden normalisation engine behind the distributions used in quantitative finance hypothesis testing. Every time you test whether a portfolio's variance has changed (chi-squared test) or whether a trading strategy's mean return is statistically significant with a small sample (t-test), the Gamma function ensures the probability density integrates correctly to one. Without it, the PDFs of the t- and chi-squared distributions — both built from sums of squared normal random variables — would not be valid probability distributions.
