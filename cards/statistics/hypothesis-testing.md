# Hypothesis Testing

**Topic:** Statistics
**Tags:** hypothesis testing, p-value, significance, null hypothesis, test statistic, inference
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A hypothesis test is a formal statistical procedure for deciding whether observed data provide sufficient evidence to reject a stated assumption (the **null hypothesis**, $H_0$) in favour of an **alternative hypothesis** ($H_1$). The decision is based on the probability of observing data at least as extreme as the sample, assuming $H_0$ is true.

## Key Formula

The **test statistic** for a two-sided test of a population mean is:

$$z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$$

where $\bar{X}$ is the sample mean, $\mu_0$ is the hypothesised mean, $\sigma$ is the population standard deviation, and $n$ is the sample size. The **p-value** is:

$$p = 2\,\Phi(-|z|)$$

where $\Phi$ is the standard normal CDF. Reject $H_0$ at significance level $\alpha$ if $p < \alpha$.

## Example

A hedge fund claims its strategy produces a mean daily return of $\mu_0 = 0$. From $n = 100$ trading days you observe $\bar{X} = 0.08\%$ with known $\sigma = 1.2\%$.

$$z = \frac{0.0008 - 0}{0.012 / \sqrt{100}} = \frac{0.0008}{0.0012} = 0.667$$

$$p = 2\,\Phi(-0.667) \approx 2 \times 0.2525 = 0.505$$

Since $p = 0.505 > 0.05$, you fail to reject $H_0$ — there is insufficient evidence that the strategy's mean return differs from zero.

## Remember

Hypothesis testing is fundamental to quantitative finance research and model validation. When a quant backtests a trading strategy, the null hypothesis is typically that the strategy has zero expected return; only if the test rejects at a chosen significance level should the signal be considered genuine. The Jarque-Bera test (normality), ADF test (stationarity), and $t$-tests of factor loadings all follow this framework. Critically, multiple hypothesis testing across many strategies inflates Type I error — a $p$-value of 0.05 tested across 100 strategies will produce roughly 5 false positives — so corrections such as Bonferroni or false discovery rate control are essential to avoid overfitting.
