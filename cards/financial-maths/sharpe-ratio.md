# Sharpe Ratio

**Topic:** Financial Mathematics
**Tags:** sharpe ratio, risk-adjusted return, portfolio performance, volatility, excess return
**Created:** 2026-03-01
**Author:** Claude Opus 4.6

---

## Definition

The **Sharpe Ratio** measures risk-adjusted performance by dividing the excess return of a portfolio (above the risk-free rate) by its volatility. A higher Sharpe Ratio indicates better compensation per unit of total risk taken, making it the standard metric for comparing portfolios or funds on a like-for-like basis.

## Key Formula

$$S = \frac{R_p - R_f}{\sigma_p}$$

where $R_p$ is the portfolio return, $R_f$ is the risk-free rate, and $\sigma_p$ is the standard deviation of the portfolio's excess returns.

## Example

A portfolio returns 12% per annum with a volatility of 20%. The risk-free rate is 4%.

$$S = \frac{0.12 - 0.04}{0.20} = \frac{0.08}{0.20} = 0.4$$

A second portfolio returns 9% with a volatility of 10%:

$$S = \frac{0.09 - 0.04}{0.10} = \frac{0.05}{0.10} = 0.5$$

Despite delivering a lower absolute return, the second portfolio has a higher Sharpe Ratio and therefore offers better risk-adjusted performance.

## Remember

The Sharpe Ratio is the slope of the Capital Allocation Line from the risk-free asset to the portfolio on a mean-standard-deviation diagram. In mean-variance optimisation the tangency portfolio — the point where this line is tangent to the efficient frontier — maximises the Sharpe Ratio. Practitioners use it routinely to evaluate hedge funds and trading strategies, but it has limitations: it treats upside and downside volatility equally, assumes returns are normally distributed, and can be misleading for strategies with skewed or fat-tailed return profiles.
