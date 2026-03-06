# Hedge Funds

**Topic:** Financial Mathematics
**Tags:** hedge funds, alternative investments, leverage, absolute return, portfolio management, risk
**Author:** Claude Opus 4.6

---

## Definition

A hedge fund is a pooled investment vehicle that employs a range of strategies — including leverage, short selling, and derivatives — to generate absolute returns regardless of market direction. Unlike traditional funds that benchmark against an index, hedge funds aim to deliver positive returns in both rising and falling markets.

## Key Formula

A common measure of hedge fund performance is the **Sharpe ratio**, which quantifies risk-adjusted return:

$$S = \frac{R_p - R_f}{\sigma_p}$$

where $R_p$ is the portfolio return, $R_f$ is the risk-free rate, and $\sigma_p$ is the standard deviation of portfolio returns.

Many hedge funds also employ **leverage**, amplifying both returns and losses:

$$R_{\text{leveraged}} = L \cdot R_{\text{unlevered}} - (L - 1) \cdot R_f$$

where $L$ is the leverage ratio (e.g. $L = 2$ means £1 of capital controls £2 of assets).

## Example

A hedge fund raises £100 million and borrows an additional £100 million at 5% per annum, giving a leverage ratio of $L = 2$. If the fund's unlevered return is 12%:

$$R_{\text{leveraged}} = 2 \times 0.12 - (2 - 1) \times 0.05 = 0.24 - 0.05 = 0.19$$

The leveraged return is 19%, compared to 12% without borrowing. However, if the unlevered return were $-8\%$:

$$R_{\text{leveraged}} = 2 \times (-0.08) - 1 \times 0.05 = -0.16 - 0.05 = -0.21$$

The loss is amplified to $-21\%$, illustrating how leverage magnifies risk in both directions.

## Remember

Hedge funds sit at the intersection of portfolio theory, derivatives, and risk management. Quantitative hedge funds rely heavily on mathematical models — from mean-variance optimisation to stochastic processes — to identify mispricings and manage exposure. Understanding how leverage, short selling, and the Sharpe ratio interact is essential for anyone working in quantitative finance, because hedge fund strategies are where theoretical models meet real capital allocation decisions.
