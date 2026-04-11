# Paired t-Test

**Topic:** Statistics
**Tags:** paired t-test, matched pairs, difference, within-subject, dependent samples
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **paired t-test** tests whether the mean of pairwise **differences** between two related measurements is zero. It applies when observations come in natural pairs — the same asset measured under two conditions, the same portfolio on two dates, or matched before/after readings. By working with differences, it eliminates between-pair variability, giving a more powerful test than an independent-samples t-test when pairs are correlated.

## Key Formula

Let $d_i = X_{i1} - X_{i2}$ be the $i$-th pair difference. With $n$ pairs:

$$\bar{d} = \frac{1}{n}\sum_{i=1}^n d_i, \qquad s_d = \sqrt{\frac{\sum(d_i - \bar{d})^2}{n-1}}$$

**Test statistic:**

$$t = \frac{\bar{d}}{s_d/\sqrt{n}} \sim t_{n-1} \text{ under } H_0: \mu_d = 0$$

**Equivalent to a one-sample t-test on the differences.**

**95% confidence interval for $\mu_d$:**

$$\bar{d} \pm t_{n-1,\,0.025} \cdot \frac{s_d}{\sqrt{n}}$$

## Example

A bank tests whether a new hedging strategy reduces daily P&L volatility. For 50 matched weeks (same market conditions), Strategy A vs Strategy B:

$$\bar{d} = \bar{\sigma}_A - \bar{\sigma}_B = 0.8\%, \quad s_d = 2.1\%, \quad n = 50$$

$$t = \frac{0.8}{2.1/\sqrt{50}} = \frac{0.8}{0.297} = 2.69, \quad p = 0.009$$

Reject $H_0$: the new strategy reduces volatility by a statistically significant 0.8% per week (95% CI: 0.2% to 1.4%).

## Remember

The paired t-test is essential for **comparing execution quality** between two algorithms, brokers, or time periods on the same set of orders — the natural unit is the pair (same trade, two algorithms). Pairing eliminates the effect of trade-specific difficulty: a large, illiquid order will be costly under any algorithm, so comparing across orders without pairing introduces noise. In **model comparison**, pairing the same portfolio on the same date under two risk models (e.g. historical simulation vs Monte Carlo VaR) produces paired observations, and the paired t-test properly accounts for the correlation between the paired estimates.
