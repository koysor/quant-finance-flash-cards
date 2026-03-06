# Capital Market Line

**Topic:** Financial Mathematics
**Tags:** capital market line, risk-free rate, tangency portfolio, Sharpe ratio, efficient frontier
**Author:** Claude Opus 4.6

---

## Definition

The **Capital Market Line (CML)** is the straight line in mean-variance space that connects the risk-free rate to the **tangency portfolio** — the portfolio on the efficient frontier with the highest Sharpe ratio. Every point on the CML represents a combination of the risk-free asset and the tangency portfolio, and the CML dominates the curved efficient frontier at every risk level.

## Key Formula

$$\mu_p = r_f + \frac{\mu_T - r_f}{\sigma_T} \cdot \sigma_p$$

where:
- $r_f$ is the risk-free rate
- $\mu_T$ and $\sigma_T$ are the return and volatility of the tangency portfolio
- The slope $(\mu_T - r_f) / \sigma_T$ is the **maximum Sharpe ratio**

**Tangency portfolio weights:**

$$\mathbf{w}_T = \frac{\Sigma^{-1}(\boldsymbol{\mu} - r_f \mathbf{1})}{\mathbf{1}^\top \Sigma^{-1}(\boldsymbol{\mu} - r_f \mathbf{1})}$$

## Example

The risk-free rate is $r_f = 3\%$, and the tangency portfolio has $\mu_T = 11\%$, $\sigma_T = 16\%$.

CML slope (maximum Sharpe ratio): $(11 - 3) / 16 = 0.50$.

An investor wanting $\sigma_p = 10\%$ volatility:

$$\mu_p = 3 + 0.50 \times 10 = 8.0\%$$

They allocate $10/16 = 62.5\%$ to the tangency portfolio and $37.5\%$ to the risk-free asset.

An aggressive investor wanting $\sigma_p = 24\%$ (above the tangency portfolio):

$$\mu_p = 3 + 0.50 \times 24 = 15.0\%$$

They borrow at $r_f$ and invest $24/16 = 150\%$ in the tangency portfolio — this is leveraged investing.

## Remember

The CML embodies the **two-fund separation theorem**: every rational investor should hold the same tangency portfolio of risky assets, differing only in how much they lever or delever by mixing with the risk-free asset. This is the theoretical foundation of index fund investing — if the market portfolio is the tangency portfolio (as CAPM assumes), then passive market-cap-weighted index funds are optimal for all investors. The CML also shows that the Sharpe ratio of the tangency portfolio is the price of risk in the economy: the additional return earned per unit of volatility taken.
