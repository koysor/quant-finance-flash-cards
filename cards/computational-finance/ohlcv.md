# OHLCV Data

**Topic:** Computational Finance
**Tags:** market data, feature engineering, time series, equities, alternative data
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**OHLCV** stands for Open, High, Low, Close, Volume — the five fields that constitute a standard bar of price data at any time resolution (tick, minute, daily, weekly). It is the canonical input format for technical analysis and financial machine learning pipelines that work with equity or futures price history.

## Key Formula

From a single daily OHLCV bar, derived features commonly used in ML models include:

$$\text{True Range} = \max(H - L,\; |H - C_{\text{prev}}|,\; |L - C_{\text{prev}}|)$$

$$\text{Daily Return} = \frac{C_t - C_{t-1}}{C_{t-1}}, \qquad \text{Log Return} = \ln\!\left(\frac{C_t}{C_{t-1}}\right)$$

$$\text{Intraday Range} = \frac{H - L}{C_{t-1}}, \qquad \text{Body Ratio} = \frac{|C - O|}{H - L}$$

where $O$, $H$, $L$, $C$ are today's open, high, low, and close respectively.

## Example

One NVDA daily bar:

| Field | Value |
|---|---|
| Open | \$876.42 |
| High | \$891.15 |
| Low | \$872.30 |
| Close | \$887.60 |
| Volume | 42,381,000 |

Derived: Daily return $= (887.60 - 876.42)/876.42 \approx +1.28\%$. Intraday range $= (891.15 - 872.30)/876.42 \approx 2.15\%$. Body ratio $= (887.60 - 876.42)/(891.15 - 872.30) \approx 0.59$.

## Remember

OHLCV is the raw material from which all technical indicators are derived. A machine learning model that predicts next-day direction from raw OHLCV features alone will typically underperform one that also includes engineered indicators (RSI, MACD, Bollinger Bands) because the relationships between raw bars and future direction are highly non-linear. However, OHLCV features like intraday range and body ratio encode information that computed indicators miss — specifically, how much of a day's range was directional (large body ratio) versus indecisive (small body ratio, long wicks). These microstructure signals can meaningfully improve classifier performance on liquid equities.
