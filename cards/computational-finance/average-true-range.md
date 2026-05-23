# ATR (Average True Range)

**Topic:** Computational Finance
**Tags:** technical analysis, volatility, feature engineering, risk management, trading signals
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

The **Average True Range (ATR)** is a volatility indicator that measures the average size of price moves over a lookback window by computing the mean of the True Range — a gap-adjusted measure of the day's price span that accounts for overnight gaps between the previous close and today's open.

## Key Formula

The **True Range** for day $t$ is:

$$\text{TR}_t = \max\!\bigl(H_t - L_t,\;\lvert H_t - C_{t-1}\rvert,\;\lvert L_t - C_{t-1}\rvert\bigr)$$

The ATR uses Wilder's exponential smoothing over $n$ periods (typically $n = 14$):

$$\text{ATR}_t = \frac{(n-1)\,\text{ATR}_{t-1} + \text{TR}_t}{n}$$

where $H$, $L$, $C$ are high, low, and close respectively.

## Example

NVDA daily bars over two consecutive days:

| Day | High | Low | Close | $C_{t-1}$ | True Range |
|---|---|---|---|---|---|
| $t-1$ | \$891 | \$872 | \$888 | — | \$19 |
| $t$ | \$880 | \$855 | \$862 | \$888 | $\max(25, 8, 33) = \$33$ |

Day $t$'s True Range is \$33 — the gap from the previous close (\$888) to today's low (\$855) was larger than the intraday range (\$880 − \$855 = \$25). If ATR$_{t-1}$ = \$20, then ATR$_t = (13 \times 20 + 33)/14 \approx \$21.6$.

## Remember

ATR is preferred over simple high-minus-low range as a volatility feature in ML models because it handles overnight gaps that are common in equity markets around earnings announcements and index events. In a direction-prediction model for NVDA, the feature `atr_14` directly measures the market's expectation of daily volatility — a high ATR period means the stock is moving sharply and the signal-to-noise ratio for directional prediction is typically lower. ATR is also used in position sizing (risk-adjusted position size $= \text{capital} \times \text{risk}/\text{ATR}$) and stop-loss placement, making it a bridge between technical ML features and practical risk management.
