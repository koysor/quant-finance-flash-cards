# QuantStats

**Topic:** Computational Finance
**Tags:** portfolio analytics, tear sheet, sharpe ratio, omega ratio, backtesting, performance metrics
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**QuantStats** is an actively maintained open-source Python library for portfolio performance and risk analytics that generates HTML tear sheets and computes a comprehensive set of risk-adjusted metrics — including the Omega ratio, tail ratio, and Kelly criterion — from a daily return series.

## Key Formula

The **Omega ratio** at threshold $\theta$ (typically 0) captures the full return distribution rather than just mean and variance:

$$\Omega(\theta) = \frac{\int_\theta^\infty [1 - F(r)]\,dr}{\int_{-\infty}^\theta F(r)\,dr} = \frac{E\!\left[\max(r - \theta,\, 0)\right]}{E\!\left[\max(\theta - r,\, 0)\right]}$$

where $F$ is the empirical CDF of returns. $\Omega > 1$ means the probability-weighted gains above $\theta$ exceed the probability-weighted losses below $\theta$. The **tail ratio** measures right-tail vs. left-tail asymmetry:

$$\text{Tail Ratio} = \frac{r_{0.95}}{\lvert r_{0.05} \rvert}$$

A tail ratio above 1 indicates the strategy generates larger upside outliers than downside outliers.

## Example

```python
import quantstats as qs

qs.extend_pandas()
qs.reports.html(returns, benchmark='^GSPC', output='tearsheet.html')
```

A momentum strategy with annualised return 14\%, volatility 10\%, and skewed right returns: Sharpe = 1.4, Omega = 1.8 (gains outweigh losses by 80\% above the zero threshold), tail ratio = 1.3 (the best 5\% of days are 30\% larger than the worst 5\%). All three agree the strategy has positive asymmetry — something a Sharpe ratio alone cannot confirm.

## Remember

The Sharpe ratio assumes returns are normally distributed, which they are not in practice — financial returns have fat tails and skewness. A strategy can have a Sharpe of 1.2 whilst occasionally producing catastrophic drawdowns if it is short volatility (collecting small premiums but occasionally losing everything). The Omega ratio and tail ratio are the corrective lenses: Omega weights every moment of the return distribution equally, and a tail ratio below 1 (left tail larger than right) is an immediate warning sign of a strategy that sells insurance. QuantStats is the go-to tool for computing all these metrics in a single shareable HTML report.
