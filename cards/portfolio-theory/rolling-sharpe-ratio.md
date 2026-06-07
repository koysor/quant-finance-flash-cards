# Rolling Sharpe Ratio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** rolling sharpe ratio, performance measurement, regime detection, strategy decay, time series
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

The rolling Sharpe ratio is the Sharpe ratio computed over a fixed-width moving window that advances one period at a time, producing a time series of Sharpe estimates rather than a single static figure. It reveals whether a strategy's risk-adjusted performance is stable across different market conditions or concentrated in a specific regime, and is one of the primary tools for detecting strategy decay in live trading.

## Key Formula

At time $t$ with window width $W$:

$$\text{SR}_t = \frac{\bar{r}^{\text{excess}}_{t-W+1:t}}{\hat{\sigma}_{t-W+1:t}} \times \sqrt{N}$$

where $\bar{r}^{\text{excess}}_{t-W+1:t}$ is the mean excess return over the window, $\hat{\sigma}_{t-W+1:t}$ is the standard deviation of excess returns over the same window, and $N$ is the annualisation factor (252 for daily, 12 for monthly).

Common window widths:
- **12 months** (monthly returns): low noise, slow signal — misses short regime shifts
- **6 months** (monthly) / **126 days** (daily): standard pyfolio default; balanced
- **1 month** (daily): noisy but responsive — used for tactical monitoring

## Example

A trend-following strategy's 6-month rolling Sharpe (monthly returns, 6-month window):

| Period | Rolling SR | Regime |
|--------|-----------|--------|
| 2020 Q1–Q2 | +2.1 | COVID crisis — strong trends |
| 2020 Q3–2021 Q2 | −0.3 | Low-vol recovery — chop |
| 2022 Q1–Q3 | +1.8 | Inflation regime — clear directional moves |
| 2023 Q1–Q4 | +0.2 | Mixed signals — range-bound |

A static full-period Sharpe of 0.9 masks the strategy's extreme regime sensitivity. The rolling version reveals the live decision: reduce exposure in choppy low-vol periods.

## Remember

A rolling Sharpe ratio that degrades from 1.5 to 0.2 over 12 months — while volatility stays constant — is the earliest systematic indicator of **alpha decay**: the signal the strategy exploits is being arbitraged away or the market regime it was calibrated to has ended. Quants at systematic funds use rolling Sharpe monitoring as a live circuit-breaker: if a 6-month rolling Sharpe falls below a pre-set threshold (often 0 or the risk-free equivalent), capital is reduced or the strategy is put on paper trading until the regime recovers. The key limitation is that rolling estimates are noisy and serially correlated — the Probabilistic Sharpe Ratio is the statistically rigorous complement.

