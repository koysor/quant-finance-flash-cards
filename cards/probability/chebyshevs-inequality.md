# Chebyshev's Inequality

**Topic:** Probability
**Tags:** chebyshev, probability bounds, variance, tail probability, distribution-free
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Chebyshev's inequality** provides a universal upper bound on the probability that a random variable deviates from its mean by more than $k$ standard deviations. It applies to any distribution with finite mean and variance — no normality assumption is required.

$$P\!\left(|X - \mu| \ge k\sigma\right) \le \frac{1}{k^2}$$

## Key Formula

**Standard form** ($k > 0$):

$$P\!\left(|X - \mu| \ge k\sigma\right) \le \frac{1}{k^2}$$

**Equivalent form** (using $\varepsilon = k\sigma$):

$$P\!\left(|X - \mu| \ge \varepsilon\right) \le \frac{\text{Var}(X)}{\varepsilon^2}$$

**One-sided (Cantelli's inequality):**

$$P(X - \mu \ge k\sigma) \le \frac{1}{1 + k^2}$$

## Example

A portfolio has expected daily return $\mu = 0.05\%$ and standard deviation $\sigma = 1\%$. What is the maximum probability that the return deviates by more than $3\%$ (i.e. $k = 3$)?

$$P\!\left(|R - 0.05\%| \ge 3\%\right) \le \frac{1}{3^2} = \frac{1}{9} \approx 11.1\%$$

Under the normal distribution assumption the probability would be about $0.26\%$ — Chebyshev's bound is much wider because it makes no distributional assumption. If the true distribution is fat-tailed (leptokurtic), the bound is more realistic than the normal figure.

## Remember

Chebyshev's inequality is a worst-case guarantee. In risk management it matters because real return distributions are not normal: the normal model might say a 3-sigma loss has probability 0.13%, but Chebyshev guarantees no more than 11.1% regardless of the distribution. This is the motivation for distribution-free or robust risk measures. It also underpins the theoretical justification for holding diversified portfolios — as the number of assets $n$ grows, portfolio variance shrinks, and Chebyshev's bound on the probability of a large deviation from the mean tightens accordingly.
