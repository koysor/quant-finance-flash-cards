# Sample Variance

**Topic:** Statistics
**Tags:** sample variance, estimator, Bessel's correction, unbiased, standard deviation
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **sample variance** $s^2$ is the standard unbiased estimator of the population variance $\sigma^2$, computed from $n$ observed values. It uses $n-1$ in the denominator (Bessel's correction) to correct for the downward bias introduced by using the sample mean $\bar{X}$ in place of the unknown population mean $\mu$.

$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2, \qquad E[s^2] = \sigma^2$$

## Key Formula

**Sample variance (unbiased):**

$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$$

**Why $n-1$:** estimating $\bar{X}$ from the same data uses up one degree of freedom. The naive $1/n$ version gives $E[\cdot] = \frac{n-1}{n}\sigma^2$, underestimating $\sigma^2$ by a factor of $\frac{n-1}{n}$.

**Sample standard deviation:**

$$s = \sqrt{s^2}$$

Note: $s$ is a biased estimator of $\sigma$ even though $s^2$ is unbiased for $\sigma^2$, because $E[\sqrt{s^2}] \ne \sqrt{E[s^2]}$ (Jensen's inequality).

**Computational shortcut:**

$$s^2 = \frac{1}{n-1}\!\left(\sum_{i=1}^n X_i^2 - n\bar{X}^2\right)$$

## Example

Five daily returns (%): $1.2,\; -0.8,\; 2.1,\; -1.5,\; 0.5$.

$\bar{X} = (1.2 - 0.8 + 2.1 - 1.5 + 0.5)/5 = 1.5/5 = 0.3\%$

$$\sum(X_i - \bar{X})^2 = 0.81 + 1.21 + 3.24 + 3.24 + 0.04 = 8.54$$

$$s^2 = 8.54 / 4 = 2.135\,\%^2, \qquad s = \sqrt{2.135} \approx 1.46\%$$

Using $n=5$ instead of $n-1=4$ would give $s^2 = 8.54/5 = 1.708\,\%^2$ — a 20% underestimate with only 5 observations.

## Remember

The distinction between $n$ and $n-1$ matters most with small samples — exactly the regime used in high-frequency risk monitoring (e.g. a 10-day rolling window). With $n = 10$, the biased estimator underestimates variance by 10%. Annualised, this translates directly into a 10% underestimate of volatility, and thus a 10% underestimate of VaR. Most financial software defaults to $n-1$; always check which convention a system uses before comparing volatility estimates across platforms.
