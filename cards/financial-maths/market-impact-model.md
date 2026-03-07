# Market Impact Model

**Topic:** Financial Mathematics
**Tags:** market impact, execution, almgren-chriss, transaction costs, optimal trading
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A market impact model quantifies how a large trade moves the price against the trader. The Almgren–Chriss framework decomposes impact into **temporary impact** (which affects only the current trade and dissipates immediately) and **permanent impact** (which shifts the equilibrium price for all subsequent trades).

## Key Formula

The **permanent impact** for a trade of size $Q$:

$$\Delta P_{\text{perm}} = g \times Q$$

where $g$ is the permanent impact coefficient (in £ per share traded).

The **temporary impact** for a trade executed at rate $v_t$ (shares per unit time):

$$\Delta P_{\text{temp}} = h \times v_t$$

The **total execution cost** (implementation shortfall) for a parent order of $X$ shares executed over $T$ periods:

$$\text{Cost} = \sum_{t=1}^{T} v_t \times \left(g \sum_{s=1}^{t} v_s + h \times v_t\right)$$

The **square-root law** approximation for total impact:

$$\text{Impact} \approx \sigma \times \eta \times \sqrt{\frac{X}{V}}$$

where $\sigma$ is daily volatility, $V$ is average daily volume, and $\eta$ is the impact coefficient.

## Example

A fund needs to sell 200,000 shares of a stock with average daily volume of 1 million shares, daily volatility of 2%, and impact coefficient $\eta = 0.5$.

$$\text{Impact} \approx 0.02 \times 0.5 \times \sqrt{\frac{200{,}000}{1{,}000{,}000}} = 0.02 \times 0.5 \times 0.447 = 0.45\%$$

On a £30 stock, the expected impact cost is £0.135 per share, or £27,000 total. If the trade were 2 million shares (2x ADV):

$$\text{Impact} \approx 0.02 \times 0.5 \times \sqrt{2} = 1.41\%$$

The impact triples because of the square-root scaling — large trades are disproportionately expensive.

## Remember

Market impact is the largest hidden cost in quantitative trading and the primary reason why strategies that backtest well can fail in live trading. The Almgren–Chriss framework (2000) formalised the trade-off between urgency and impact: trading slowly reduces market impact but exposes the trader to adverse price drift (timing risk). The optimal execution schedule balances these two costs. For stat arb and high-frequency strategies, impact modelling determines the maximum capacity of a strategy — the point at which the alpha is entirely consumed by the cost of entering and exiting positions. The square-root law, empirically validated across markets and asset classes, implies that impact grows sublinearly with trade size, favouring patient execution.
