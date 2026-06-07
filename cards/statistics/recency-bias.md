# Recency Bias

**Topic:** Statistics
**Tags:** recency bias, model risk, historical simulation, var, behavioural finance, estimation bias
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Recency bias is the tendency to overweight recent observations when estimating statistical parameters or forming expectations, causing models calibrated on short windows to reflect current market conditions rather than the full historical distribution. In quantitative finance, it manifests when risk models trained on calm markets assign low volatility, or when those trained on crises assign excessively high risk.

## Key Formula

A lookback window of $T$ observations assigns uniform weight $\frac{1}{T}$ to every day. Exponentially weighted moving average (EWMA) applies a decay factor $\lambda \in (0,1)$, giving weight $\propto \lambda^{k}$ to data $k$ periods old:

$$\sigma_t^2 = (1-\lambda)\sum_{k=0}^{T-1}\lambda^k r_{t-k}^2$$

The **effective memory** of an EWMA model is approximately $\frac{1}{1-\lambda}$ trading days. At $\lambda = 0.94$ (RiskMetrics), this is roughly 17 days — meaning recent shocks dominate and older data is effectively discarded.

## Example

In 2006, a VaR model estimated using only 250 days of post-2003 data recorded low volatility (say $\sigma = 0.6\%$ daily). After the 2007–2008 crisis, an identical model estimated $\sigma = 2.5\%$. Both estimates were statistically valid for their windows, but a desk relying on the 2006 figure dramatically underestimated tail risk entering the crisis. Similarly, a model recalibrated at the peak of 2008 would have overstated risk for years afterwards.

## Remember

Recency bias is the key failure mode of **historical simulation VaR**: because it replays a fixed recent window (typically 250–500 days), calm periods produce low VaR and crises produce high VaR — exactly the wrong signal for risk management. Regulators address this partly through the **stressed VaR** requirement (Basel 2.5), which forces firms to include a 12-month window containing a significant stress event alongside the current-window VaR. When building any risk or pricing model, always ask whether the calibration window contains a full credit cycle, not just the most recent calm or turbulent period.
