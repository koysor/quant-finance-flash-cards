# Type I and Type II Error

**Topic:** Statistics
**Tags:** hypothesis testing, false positive, false negative, significance, power, inference
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A **Type I error** (false positive) occurs when the null hypothesis is rejected even though it is true. A **Type II error** (false negative) occurs when the null hypothesis is not rejected even though it is false. The probability of a Type I error is the significance level $\alpha$; the probability of a Type II error is denoted $\beta$, and $1 - \beta$ is called the **power** of the test.

## Key Formula

$$\alpha = P(\text{reject } H_0 \mid H_0 \text{ true}) \qquad \beta = P(\text{fail to reject } H_0 \mid H_0 \text{ false})$$

$$\text{Power} = 1 - \beta = P(\text{reject } H_0 \mid H_0 \text{ false})$$

For a one-sided $z$-test with true mean $\mu_1 \neq \mu_0$:

$$\beta = \Phi\!\left(z_{\alpha} - \frac{\mu_1 - \mu_0}{\sigma / \sqrt{n}}\right)$$

where $z_{\alpha}$ is the critical value at significance level $\alpha$.

## Example

A quant tests whether a strategy's mean daily return exceeds zero ($H_0: \mu = 0$, $H_1: \mu > 0$) at $\alpha = 0.05$. Suppose $\sigma = 1\%$, $n = 250$ days, and the true mean is $\mu_1 = 0.04\%$.

$$z_{\alpha} = 1.645 \qquad \frac{\mu_1 - \mu_0}{\sigma / \sqrt{n}} = \frac{0.0004}{0.01 / \sqrt{250}} = \frac{0.0004}{0.000632} = 0.633$$

$$\beta = \Phi(1.645 - 0.633) = \Phi(1.012) \approx 0.844$$

Power $= 1 - 0.844 = 0.156$, meaning there is only a 15.6% chance of detecting this small positive return — the test has low power.

## Remember

In quantitative finance, the trade-off between Type I and Type II errors is central to strategy selection. A Type I error means deploying capital on a strategy that has no genuine edge — leading to trading costs and losses. A Type II error means discarding a profitable strategy as noise. Backtesting hundreds of strategies at $\alpha = 0.05$ virtually guarantees Type I errors (roughly 5% of null strategies will appear significant), which is why quants apply multiple testing corrections. Conversely, demanding very low $\alpha$ reduces false discoveries but increases the risk of missing real signals, especially when returns are small relative to volatility — the low signal-to-noise ratio typical of financial markets makes power a persistent concern.
