# Treynor Ratio

**Topic:** Financial Mathematics
**Tags:** treynor ratio, beta, systematic risk, risk-adjusted return, capm, performance
**Author:** Claude Opus 4.6

---

## Definition

The Treynor ratio measures the excess return earned per unit of systematic (market) risk, as measured by beta. Unlike the Sharpe ratio, which divides by total volatility, the Treynor ratio divides by beta alone — making it appropriate for well-diversified portfolios where idiosyncratic risk has been eliminated and only market exposure remains.

## Key Formula

$$\text{Treynor} = \frac{\bar{R}_p - R_f}{\beta_p}$$

where $\bar{R}_p$ is the portfolio return, $R_f$ is the risk-free rate, and $\beta_p$ is the portfolio's beta with respect to the market.

For a portfolio that lies exactly on the Security Market Line, the Treynor ratio equals the market risk premium:

$$\text{Treynor} = E[R_m] - R_f$$

## Example

Two funds both outperform the risk-free rate of 3%:

| Fund | Return | Beta |
|------|--------|------|
| A    | 15%    | 1.5  |
| B    | 11%    | 0.8  |

$$\text{Treynor}_A = \frac{0.15 - 0.03}{1.5} = 0.08$$

$$\text{Treynor}_B = \frac{0.11 - 0.03}{0.8} = 0.10$$

Fund B has the superior Treynor ratio despite lower absolute returns. Fund A earned more only because it took on more market risk (higher beta), not because of superior stock selection. Per unit of systematic risk, Fund B delivered more.

## Remember

The Treynor ratio complements the Sharpe ratio by isolating systematic risk from total risk. For a pension fund evaluating managers who each run a diversified sub-portfolio, the Treynor ratio is the right metric — since the pension fund itself diversifies across managers, the idiosyncratic risk of each sub-portfolio washes out, and only beta exposure matters. The Sharpe ratio is better for evaluating a standalone investment, while the Treynor ratio is better for evaluating one component within a larger diversified allocation.
