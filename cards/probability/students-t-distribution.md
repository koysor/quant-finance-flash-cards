# Student's t-Distribution

**Topic:** Probability
**Tags:** distributions, probability, continuous, fat tails, hypothesis testing
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

The Student's t-distribution is a bell-shaped distribution that resembles the normal but has **heavier tails**. It arises when estimating the mean of a normally distributed population from a small sample, using the sample standard deviation. It is described by one parameter:

- **ν** (nu) — the degrees of freedom

As $\nu \to \infty$, the t-distribution converges to the standard normal $N(0, 1)$.

## Key Formula

The probability density function is:

$$f(x) = \frac{\Gamma\!\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu\pi}\;\Gamma\!\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu + 1}{2}}$$

| Property | Value |
|---|---|
| Mean | $0$ (for $\nu > 1$) |
| Variance | $\frac{\nu}{\nu - 2}$ (for $\nu > 2$) |
| Kurtosis | $\frac{6}{\nu - 4} + 3$ (for $\nu > 4$) |

The kurtosis exceeds 3 (the normal value), confirming heavier tails.

## Example

A sample of 10 daily returns has mean $\bar{x} = 0.002$ and sample standard deviation $s = 0.015$. To test whether the true mean differs from zero:

$$t = \frac{\bar{x} - 0}{s / \sqrt{n}} = \frac{0.002}{0.015 / \sqrt{10}} = \frac{0.002}{0.00474} \approx 0.42$$

With $\nu = 9$ degrees of freedom, $t = 0.42$ is well within the critical values $(\pm 2.26)$, so there is no significant evidence that the mean return differs from zero.

## Remember

The t-distribution is important in quant finance for two reasons. First, it provides the correct **hypothesis test** for whether a trading strategy's mean return is statistically significant when the sample is small. Second, with low degrees of freedom ($\nu \approx 3\text{–}5$), it captures the **fat tails** observed in real asset returns far better than the normal distribution — making it a popular choice for more realistic risk models and value-at-risk calculations.
