# Two-Fund Separation Theorem

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** two-fund separation, capital market line, tangency portfolio, mean-variance, asset allocation
**Author:** Claude Opus 4.6

---

## Definition

The **two-fund separation theorem** states that in a mean-variance world with a risk-free asset, every efficient portfolio can be constructed as a linear combination of just two funds: the **risk-free asset** and the **tangency portfolio** (the risky portfolio with the highest Sharpe ratio). All investors hold the same risky portfolio — they differ only in how much they allocate to the risk-free asset versus the tangency portfolio.

## Key Formula

Any efficient portfolio has weights:

$$\mathbf{w}_p = \alpha \, \mathbf{w}_T + (1 - \alpha) \, \mathbf{w}_f$$

where $\mathbf{w}_T$ is the tangency portfolio, $\mathbf{w}_f$ is the risk-free asset, and $\alpha \in \mathbb{R}$ (may exceed 1 for leveraged portfolios).

The resulting return and risk:

$$\mu_p = (1 - \alpha) \, r_f + \alpha \, \mu_T, \qquad \sigma_p = |\alpha| \, \sigma_T$$

## Example

The tangency portfolio has $\mu_T = 10\%$, $\sigma_T = 15\%$, and the risk-free rate is $r_f = 3\%$.

**Conservative investor** ($\alpha = 0.5$): invests 50% in the tangency portfolio, 50% in the risk-free asset.

$$\mu_p = 0.5 \times 3 + 0.5 \times 10 = 6.5\%, \qquad \sigma_p = 0.5 \times 15 = 7.5\%$$

**Aggressive investor** ($\alpha = 1.5$): borrows 50% at $r_f$ and invests 150% in the tangency portfolio.

$$\mu_p = -0.5 \times 3 + 1.5 \times 10 = 13.5\%, \qquad \sigma_p = 1.5 \times 15 = 22.5\%$$

Both investors hold the same risky assets in the same proportions — only the leverage differs.

## Remember

Two-fund separation is the theoretical foundation of passive index investing. If the market portfolio is the tangency portfolio (as CAPM assumes), then every investor should hold a market-cap-weighted index fund combined with lending or borrowing at the risk-free rate. This is why Jack Bogle's insight — that most active managers cannot beat the index — has a rigorous mathematical basis. The theorem breaks down when investors face different constraints (short-selling restrictions, tax regimes, liability matching), which is why in practice different investors do hold different risky portfolios.
