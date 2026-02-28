# Growth vs Volatility Timescales

**Topic:** Stochastic Processes
**Tags:** drift, volatility, timescales, scaling, noise, trend
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

Drift and volatility scale differently with time: drift grows linearly ($\mu t$) while volatility grows with the square root ($\sigma \sqrt{t}$). Over short periods volatility dominates, making price movements appear random. Over long periods drift overtakes, revealing the underlying trend.

## Key Formula

$$\frac{\text{Drift effect}}{\text{Volatility effect}} = \frac{\mu \, t}{\sigma \sqrt{t}} = \frac{\mu}{\sigma} \sqrt{t}$$

This ratio grows with $\sqrt{t}$, so the signal-to-noise ratio improves as the horizon lengthens.

## Example

For the S&P 500 with $\mu = 8.8\%$ and $\sigma = 14.1\%$:

| Horizon | Drift | Volatility | Ratio |
|---|---|---|---|
| 1 day | 0.035% | 0.89% | 0.04 |
| 1 year | 8.8% | 14.1% | 0.62 |
| 10 years | 88% | 44.6% | 1.97 |

At 10 years the drift is nearly double the volatility — the upward trend is clearly visible through the noise.

## Remember

This is why short-term price forecasting is nearly impossible (noise swamps signal), but long-term equity risk premia are real and measurable. It also explains why hedge funds using daily signals need extremely high Sharpe ratios, while pension funds can rely on long-term drift.
