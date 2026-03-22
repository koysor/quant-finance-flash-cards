# Cross-Sectional vs Time-Series Momentum

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** momentum, cross-sectional, time-series, trend following, relative strength
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Cross-sectional momentum and time-series momentum are two distinct implementations of the momentum effect. **Cross-sectional momentum** ranks assets within a universe by past returns and goes long the top performers while shorting the bottom — the signal is *relative* performance. **Time-series momentum** (trend following) evaluates each asset independently: go long if its own past return is positive, go short if negative — the signal is *absolute* performance. The two approaches have different risk profiles and capture different aspects of return predictability.

## Key Formula

**Cross-sectional signal** for asset $i$:

$$\text{CS}_i = \text{rank}\!\left(\frac{P_{i,t-1}}{P_{i,t-J}} - 1\right) \quad \text{relative to all assets in the universe}$$

Long the top decile, short the bottom decile. The portfolio is always dollar-neutral (zero net investment).

**Time-series signal** for asset $i$:

$$\text{TS}_i = \text{sign}\!\left(\frac{P_{i,t-1}}{P_{i,t-J}} - 1\right)$$

Go long if $\text{TS}_i = +1$, short if $\text{TS}_i = -1$. The portfolio can have net long or short exposure.

The **net market exposure** differs:

$$\text{CS: } \sum_i w_i \approx 0 \qquad \text{TS: } \sum_i w_i \neq 0$$

## Example

Three stocks over the past 12 months: A returned +20%, B returned +5%, C returned $-10\%$.

**Cross-sectional:** rank A > B > C. Long A, short C. B is neutral. Net exposure ≈ 0.

**Time-series:** A is positive → long. B is positive → long. C is negative → short. Net exposure = 2 long, 1 short → net long.

If the entire market then drops 15%, the cross-sectional portfolio is hedged (long and short cancel), but the time-series portfolio suffers because of its net long tilt. Conversely, in a broad downturn where all stocks have negative past returns, time-series momentum goes net short (profiting from the decline), while cross-sectional momentum remains neutral and earns only the spread between relative winners and losers.

## Remember

The distinction matters for portfolio construction and risk management. Cross-sectional momentum is market-neutral and captures relative mispricing, making it suitable for equity long-short funds. Time-series momentum captures absolute trends and provides natural hedging in prolonged bear markets — managed futures (CTA) funds are essentially time-series momentum strategies applied across asset classes. Moskowitz, Ooi, and Pedersen (2012) showed that time-series momentum explains a large fraction of CTA returns. In practice, combining both approaches diversifies across market regimes: cross-sectional momentum performs steadily in dispersed markets, while time-series momentum adds value during strong directional trends.
