# OBV (On-Balance Volume)

**Topic:** Computational Finance
**Tags:** technical analysis, volume, momentum, feature engineering, trading signals
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**On-Balance Volume (OBV)** is a cumulative volume momentum indicator that adds the day's total volume when price closes higher and subtracts it when price closes lower, producing a running total that reflects whether volume is flowing into or out of an asset. It was developed by Joseph Granville on the premise that volume precedes price.

## Key Formula

$$\text{OBV}_t = \text{OBV}_{t-1} + \begin{cases} +V_t & \text{if } C_t > C_{t-1} \\ 0 & \text{if } C_t = C_{t-1} \\ -V_t & \text{if } C_t < C_{t-1} \end{cases}$$

where $V_t$ is the trading volume on day $t$ and $C_t$ is the closing price. The absolute level of OBV is arbitrary; its direction and divergence from price are the signals of interest.

## Example

NVDA over five days (OBV starts at 0):

| Day | Close | Direction | Volume | OBV |
|---|---|---|---|---|
| 1 | \$880 | — | — | 0 |
| 2 | \$887 | Up | 45M | +45M |
| 3 | \$883 | Down | 30M | +15M |
| 4 | \$890 | Up | 60M | +75M |
| 5 | \$885 | Down | 20M | +55M |

Rising price with rising OBV confirms the uptrend — heavy volume on up-days dominates. As an ML feature, the one-day OBV difference (`obv_diff = OBV_t − OBV_{t-1}`) is often more informative than the level because it is stationary.

## Remember

OBV encodes information that price-only indicators miss: whether big moves are accompanied by conviction (high volume) or indifference (low volume). In a direction-prediction model for a liquid stock like NVDA, the feature `obv_diff` can detect institutional accumulation — large buy orders spread over several days push OBV higher even before price reacts strongly. The divergence signal (price makes new high but OBV does not) is a classic warning that the rally lacks volume support. Including `obv_diff` alongside price-based features like RSI and MACD gives the classifier access to the demand-side information that price alone cannot reveal.
