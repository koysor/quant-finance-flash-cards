# Beta Hedging

**Topic:** Financial Mathematics
**Tags:** beta hedging, market exposure, portfolio construction, index futures, risk management
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Beta hedging is the practice of offsetting a portfolio's exposure to broad market movements by taking an opposing position — typically by shorting index futures or ETFs — sized so that the combined portfolio beta equals zero (or a target level).

## Key Formula

The **hedge notional** required to neutralise market exposure:

$$H = -\beta_p \times V_p$$

where $\beta_p$ is the portfolio beta and $V_p$ is the portfolio value.

If hedging with an instrument of beta $\beta_h$ (e.g. an index future with $\beta_h = 1$):

$$\text{Number of contracts} = \frac{\beta_p \times V_p}{\beta_h \times \text{Contract Notional}}$$

After hedging, the **residual beta** is:

$$\beta_{\text{hedged}} = \beta_p + \frac{H \times \beta_h}{V_p} = 0$$

## Example

A £10 million equity portfolio has $\beta_p = 1.2$. Each FTSE 100 future has a notional of £100,000 and $\beta_h = 1.0$.

$$\text{Contracts to short} = \frac{1.2 \times 10{,}000{,}000}{1.0 \times 100{,}000} = 120$$

By shorting 120 futures contracts, the portfolio's net beta is zero. If the market falls 5%, the portfolio loses approximately $1.2 \times 5\% = 6\%$ on stocks but gains $1.0 \times 5\% \times (120 \times 100{,}000 / 10{,}000{,}000) = 6\%$ on futures, netting to roughly zero.

## Remember

Beta hedging is the practical mechanism that makes market neutral strategies possible. Unlike delta hedging (which hedges option price sensitivity), beta hedging targets the portfolio's sensitivity to the overall equity market. The key challenge is that beta is **estimated, not observed** — it drifts over time, varies with market regime, and is measured with statistical error. Successful quant funds rebalance their beta hedge frequently (often daily) and use rolling-window or Bayesian estimates to adapt to changing betas. During market crises, betas tend to spike as correlations increase, which can leave an apparently hedged portfolio with significant residual market exposure.
