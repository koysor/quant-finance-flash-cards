# Market Portfolio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** market portfolio, CAPM, capital market line, tangency portfolio, market capitalisation, equilibrium
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **market portfolio** $M$ contains every risky asset available, held in proportion to its **market capitalisation**. Under CAPM's homogeneous-beliefs assumption, all investors run the same mean–variance optimisation and therefore arrive at the same tangency portfolio. Because supply must equal demand in equilibrium, the tangency portfolio must be the market portfolio — every asset is held by someone, so $M$ holds everything.

Practical proxies (since a true all-asset portfolio is unobservable): the S&P 500, FTSE All-Share, or MSCI World index are commonly used as stand-ins.

## Key Formula

A portfolio $\Pi$ blending $M$ and the risk-free asset with weight $w_M$ in $M$:

$$\mu_\Pi = R + w_M(\mu_M - R), \qquad \sigma_\Pi = w_M \sigma_M$$

The **market price of risk** (slope of the Capital Market Line):

$$\text{Sharpe}_M = \frac{\mu_M - R}{\sigma_M}$$

This is the maximum Sharpe ratio achievable by any portfolio — no combination of risky assets does better.

## Example

Suppose $\mu_M = 8\%$, $\sigma_M = 16\%$, $R = 2\%$.

Market price of risk $= \dfrac{8 - 2}{16} = 0.375$.

An investor who puts $w_M = 1.5$ into $M$ (borrowing at $R$) expects:

$$\mu_\Pi = 2 + 1.5(8 - 2) = 11\%, \qquad \sigma_\Pi = 1.5 \times 16 = 24\%$$

This leveraged position lies on the CML above $M$.

## Remember

Because every investor holds the same market portfolio under CAPM, any asset's contribution to risk is measured only by its **covariance with $M$**, not its standalone volatility. This is why idiosyncratic risk earns no return premium — it diversifies away when everyone holds $M$. In practice, tracking an index fund is the closest real-world implementation of holding the market portfolio.
