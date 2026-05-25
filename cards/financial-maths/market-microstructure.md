# Market Microstructure

**Topic:** Financial Mathematics
**Tags:** bid-ask spread, market impact, price discovery, liquidity, execution, order book
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Market microstructure** is the study of how the rules and mechanisms of a trading venue determine price formation, bid-ask spreads, market impact, and the distribution of gains between informed and uninformed traders. It bridges economic theory and the practical costs of executing orders in real markets.

## Key Formula

The **bid-ask spread** $s$ can be decomposed into three components under the Glosten-Milgrom model:

$$s = \underbrace{2\lambda\sigma}_{\text{adverse selection}} + \underbrace{2c}_{\text{inventory cost}} + \underbrace{2\phi}_{\text{order processing}}$$

where $\lambda$ is the probability that a trade is from an informed investor, $\sigma$ is the price uncertainty, $c$ is the market maker's inventory holding cost, and $\phi$ is the fixed processing cost. **Market impact** (permanent price effect of a trade of size $Q$):

$$\Delta P = \eta \cdot \text{sign}(Q) \cdot |Q|^\gamma$$

where $\eta$ is the market impact coefficient and $\gamma \approx 0.5$ (square-root law for large orders in liquid markets).

## Example

NVDA at the open with a 100-share order. If the bid is \$886.50 and the ask is \$887.00:

| Component | Value |
|---|---|
| Spread cost per share | \$0.50 (crossing half-spread twice: \$0.25 entry + \$0.25 exit) |
| Round-trip cost (100 shares) | \$50 |
| As % of notional (\$88,700) | 0.056% |

For a daily direction model that trades every day at a signal threshold, 0.056% per round trip compounds to roughly 14% per year in execution drag — enough to erase a modest statistical edge.

## Remember

Microstructure matters for financial ML because the data used for model training (OHLCV daily closes) is the cleaned output of the microstructure process, not the raw order flow. Three practical implications: (1) **daily close prices** are a consensus price that smooths intraday noise, but the model's signals must be executed at the open or close of the next day where spreads and impact apply; (2) **volume patterns** in OHLCV (captured by OBV) are microstructure signals — high volume on up-days reflects institutional demand, which market makers must accommodate by moving prices; (3) **regime changes** in microstructure (widening spreads around announcements, thin books at the open) create non-stationarity that degrades model performance even when the statistical signal remains valid.
