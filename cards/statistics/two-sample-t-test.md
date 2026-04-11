# Two-Sample t-Test

**Topic:** Statistics
**Tags:** two-sample, t-test, independent samples, comparing means, equal variance, Welch
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **two-sample t-test** tests whether the means of two independent groups are equal: $H_0: \mu_1 = \mu_2$ vs $H_1: \mu_1 \neq \mu_2$ (or one-sided). Two versions exist: the **pooled (equal variance) t-test** assumes $\sigma_1^2 = \sigma_2^2$ and the **Welch t-test** does not. Welch's test is more robust and is preferred in practice unless equality of variances has been verified (e.g. via an F-test or Levene's test).

## Key Formula

**Welch t-statistic:**

$$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$$

**Welch–Satterthwaite degrees of freedom:**

$$\nu = \frac{\left(\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1-1} + \dfrac{(s_2^2/n_2)^2}{n_2-1}}$$

**Pooled t-statistic** (equal variances assumed):

$$t = \frac{\bar{X}_1 - \bar{X}_2}{s_p\sqrt{1/n_1 + 1/n_2}}, \qquad s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$$

## Example

Comparing daily returns of two strategies over different periods: Strategy A ($n_1 = 120$, $\bar{X}_1 = 0.10\%$, $s_1 = 1.2\%$) vs Strategy B ($n_2 = 80$, $\bar{X}_2 = 0.04\%$, $s_2 = 0.8\%$).

$$t = \frac{0.10 - 0.04}{\sqrt{1.2^2/120 + 0.8^2/80}} = \frac{0.06}{\sqrt{0.012 + 0.008}} = \frac{0.06}{0.141} = 0.43$$

With $\nu \approx 185$, $p \approx 0.67$: fail to reject $H_0$ — no significant difference between the strategies' mean returns.

## Remember

The two-sample t-test is the standard tool for **comparing alpha across strategies, time periods, or risk models**. In performance attribution, it tests whether a manager's mean return differs significantly from a benchmark. In model validation, it tests whether two VaR models produce significantly different estimates. **The Welch test is almost always preferred** over the pooled test in finance because return volatility differs across regimes, assets, and time periods — the equal variance assumption is rarely justified. The test is also the basis of **A/B testing** in algorithmic trading: split a strategy between two execution algorithms and test whether the difference in achieved prices is statistically significant.
