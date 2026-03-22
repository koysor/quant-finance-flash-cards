# VIX Index

**Topic:** Volatility
**Tags:** VIX, implied volatility, fear gauge, S&P 500, variance swap, volatility index
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **VIX** (CBOE Volatility Index) measures the market's expectation of 30-day annualised volatility of the S&P 500, derived from the prices of near-term SPX options. Often called the "fear gauge", a high VIX signals elevated uncertainty and demand for downside protection. The VIX is not a forecast of direction — it measures the expected magnitude of price moves regardless of sign.

## Key Formula

The VIX is calculated as:

$$\text{VIX}^2 = \frac{2}{T} \sum_i \frac{\Delta K_i}{K_i^2} \, e^{rT} \, Q(K_i) - \frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2$$

where $T$ is time to expiry (30 days), $F$ is the forward index level, $K_0$ is the first strike below $F$, $\Delta K_i$ is the strike spacing, and $Q(K_i)$ is the mid-price of the out-of-the-money option at strike $K_i$ (puts below $K_0$, calls above).

The VIX is reported in annualised percentage points:

$$\text{VIX} = 100 \times \sqrt{\text{VIX}^2}$$

## Example

If VIX $= 20$, the market expects the S&P 500 to move within a daily range of approximately:

$$\text{Daily move} \approx \frac{20\%}{\sqrt{252}} \approx 1.26\%$$

Over 30 days, the expected range (one standard deviation) is:

$$\text{30-day move} \approx 20\% \times \sqrt{\frac{30}{365}} \approx 5.7\%$$

If the S&P 500 is at 5,000, the market implies a one-standard-deviation 30-day band of roughly 4,715 to 5,285.

## Remember

The VIX formula is essentially the fair strike of a 30-day variance swap on the S&P 500, derived from the same replicating portfolio of out-of-the-money options. This connection means the VIX embeds the full shape of the volatility smile, not just ATM vol. The VIX itself is not directly tradeable, but VIX futures and options are — and VIX futures typically trade above the spot VIX (contango), reflecting the cost of rolling variance exposure. This term structure is the reason that long-VIX ETPs like VXX systematically lose value over time, while inverse products like SVXY earn a roll yield. Understanding the VIX is essential for volatility trading, portfolio hedging, and interpreting market sentiment.
