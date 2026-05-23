# RSI (Relative Strength Index)

**Topic:** Computational Finance
**Tags:** technical analysis, momentum, oscillator, feature engineering, trading signals
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

The **Relative Strength Index (RSI)** is a bounded momentum oscillator that measures the speed and magnitude of recent price changes by comparing average gains to average losses over a lookback window, returning a value between 0 and 100. Values above 70 are conventionally interpreted as overbought and values below 30 as oversold.

## Key Formula

Over a window of $n$ periods (typically $n = 14$), compute average gain $\bar{G}$ and average loss $\bar{L}$:

$$\text{RS} = \frac{\bar{G}}{\bar{L}}, \qquad \text{RSI} = 100 - \frac{100}{1 + \text{RS}}$$

Wilder's smoothing uses an exponential moving average rather than a simple mean:

$$\bar{G}_t = \frac{(n-1)\,\bar{G}_{t-1} + G_t}{n}, \quad \bar{L}_t = \frac{(n-1)\,\bar{L}_{t-1} + L_t}{n}$$

where $G_t = \max(\Delta P_t, 0)$ and $L_t = \max(-\Delta P_t, 0)$ for daily close-to-close return $\Delta P_t$.

## Example

NVDA daily closes over 15 days. Suppose the 14-day average gain is 1.20 and average loss is 0.80:

$$\text{RS} = \frac{1.20}{0.80} = 1.5, \qquad \text{RSI} = 100 - \frac{100}{2.5} = 60$$

An RSI of 60 signals moderate bullish momentum — above the neutral 50 mark but not yet in overbought territory. A machine learning classifier trained to predict next-day direction would receive 60 as an input feature (`rsi_14`).

## Remember

RSI is one of the most common features in price-direction classification models because it compresses multi-day momentum into a bounded $[0, 100]$ range that requires no further normalisation. In a model predicting whether NVDA closes up or down tomorrow, `rsi_14` captures whether the stock has been on a recent winning streak (high RSI, potential mean-reversion risk) or losing streak (low RSI, potential bounce). The overbought/oversold thresholds are heuristics — a gradient boosting model learns the actual predictive thresholds from the data rather than hard-coding 70/30.
