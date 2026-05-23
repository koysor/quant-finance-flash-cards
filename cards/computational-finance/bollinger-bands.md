# Bollinger Bands

**Topic:** Computational Finance
**Tags:** technical analysis, volatility, feature engineering, mean reversion, trading signals
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Bollinger Bands** are a volatility envelope constructed by placing bands two standard deviations above and below a $n$-period simple moving average (SMA) of price. The width of the bands expands during high-volatility regimes and contracts during low-volatility regimes, making them a real-time measure of relative price extremity.

## Key Formula

Over a rolling window of $n$ periods (typically $n = 20$):

$$\text{Middle Band} = \text{SMA}_n = \frac{1}{n}\sum_{i=0}^{n-1} P_{t-i}$$

$$\text{Upper Band} = \text{SMA}_n + k\,\sigma_n, \qquad \text{Lower Band} = \text{SMA}_n - k\,\sigma_n$$

where $k = 2$ (standard) and $\sigma_n$ is the rolling standard deviation of $P$ over the same window. The **%B** indicator normalises the price position within the bands:

$$\%B = \frac{P - \text{Lower Band}}{\text{Upper Band} - \text{Lower Band}}$$

## Example

Suppose NVDA's 20-day SMA is \$880 and 20-day standard deviation is \$15:

| Band | Value |
|---|---|
| Upper | \$910 |
| Middle | \$880 |
| Lower | \$850 |

If today's close is \$905, then $\%B = (905 - 850)/(910 - 850) = 0.917$ — close to the upper band, signalling elevated price relative to recent volatility.

## Remember

Bollinger Bands are valuable as ML features because they encode both trend and volatility simultaneously. The **bandwidth** metric $(\text{Upper} - \text{Lower})/\text{SMA}$ captures regime volatility — a band squeeze often precedes a breakout. The **%B** metric captures where price sits relative to its recent distribution. In a direction-prediction model for a stock like NVDA, these two features (`bb_bandwidth`, `bb_pct_b`) encode information that neither a pure momentum indicator (RSI, MACD) nor a raw price feature can provide alone: how far the stock has deviated from its rolling mean relative to its own recent volatility.
