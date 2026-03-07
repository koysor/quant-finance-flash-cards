# t-Test

**Topic:** Statistics
**Tags:** hypothesis testing, t-distribution, significance, mean, inference, small samples
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A **$t$-test** is a hypothesis test used to determine whether a population mean (or the difference between two means) differs significantly from a hypothesised value, when the population standard deviation is unknown and must be estimated from the sample. The test statistic follows a **Student's $t$-distribution** with $n - 1$ degrees of freedom, which has heavier tails than the normal distribution to account for the additional uncertainty in estimating $\sigma$.

## Key Formula

**One-sample $t$-test:**

$$t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}$$

where $\bar{X}$ is the sample mean, $\mu_0$ is the hypothesised mean, $s$ is the sample standard deviation, and $n$ is the sample size. Under $H_0$, the statistic $t \sim t_{n-1}$.

Reject $H_0$ at significance level $\alpha$ (two-sided) if $|t| > t_{\alpha/2,\, n-1}$.

## Example

A portfolio manager claims her fund generates positive alpha. Over $n = 36$ months, the excess returns have $\bar{X} = 0.5\%$ per month and $s = 2.4\%$.

$$t = \frac{0.005}{0.024 / \sqrt{36}} = \frac{0.005}{0.004} = 1.25$$

The two-sided critical value at $\alpha = 0.05$ with 35 degrees of freedom is $t_{0.025,\,35} \approx 2.03$. Since $1.25 < 2.03$, we fail to reject $H_0$ — there is insufficient evidence that the fund's alpha is non-zero.

## Remember

The $t$-test is the workhorse of quantitative finance research. It is used to test whether a strategy's Sharpe ratio, a factor's risk premium, or a regression coefficient (such as CAPM beta) is statistically significant. Because financial return samples are often moderate in size and the true volatility is unknown, the $t$-distribution's heavier tails provide more honest inference than a $z$-test. A common rule of thumb — a $t$-statistic above 2.0 for significance — comes directly from the $t$-test at the 5% level with reasonably large $n$. When evaluating factor models, quants routinely report $t$-statistics alongside coefficient estimates to distinguish genuine risk premia from sampling noise.
