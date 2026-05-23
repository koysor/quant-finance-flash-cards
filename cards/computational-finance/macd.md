# MACD (Moving Average Convergence Divergence)

**Topic:** Computational Finance
**Tags:** technical analysis, momentum, trend following, feature engineering, trading signals
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**MACD** is a trend-following momentum indicator constructed as the difference between a short-period and a long-period exponential moving average (EMA) of price. It produces three series: the MACD line, a signal line (EMA of the MACD line), and a histogram showing their divergence.

## Key Formula

$$\text{MACD} = \text{EMA}_{12}(P) - \text{EMA}_{26}(P)$$

$$\text{Signal} = \text{EMA}_{9}(\text{MACD})$$

$$\text{Histogram} = \text{MACD} - \text{Signal}$$

where $\text{EMA}_n(P_t) = \alpha P_t + (1-\alpha)\,\text{EMA}_n(P_{t-1})$ with smoothing factor $\alpha = \tfrac{2}{n+1}$.

Standard parameters: fast EMA $= 12$ days, slow EMA $= 26$ days, signal $= 9$ days.

## Example

Suppose NVDA's 12-day EMA is \$890 and 26-day EMA is \$875:

$$\text{MACD} = 890 - 875 = 15$$

If the 9-day EMA of MACD is 10, then:

$$\text{Histogram} = 15 - 10 = +5 \quad \text{(bullish divergence)}$$

A positive and widening histogram conventionally signals strengthening upward momentum. As a machine learning feature (`macd_hist`), this numeric value feeds directly into the classifier without discretisation.

## Remember

MACD captures two distinct signals simultaneously: the MACD line reflects medium-term trend direction (via the EMA spread), while the histogram reflects momentum acceleration or deceleration. In a direction-prediction model for an equity like NVDA, including both `macd` and `macd_hist` as separate features allows the model to distinguish between a stock that is trending up steadily (MACD positive, histogram flat) versus one that is accelerating upward (MACD positive, histogram growing) — an important distinction that a single moving-average feature cannot convey.
