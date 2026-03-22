# Bid-Ask Spread

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** bid-ask spread, market microstructure, liquidity, transaction cost, market maker
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The bid-ask spread is the difference between the highest price a buyer is willing to pay (the bid) and the lowest price a seller is willing to accept (the ask or offer). It represents the cost of immediacy — a trader who wants to buy or sell immediately must cross the spread, paying the ask to buy or receiving the bid to sell. The spread compensates market makers for inventory risk, adverse selection risk (trading against informed counterparties), and order-processing costs.

## Key Formula

The **absolute spread**:

$$S = P_{\text{ask}} - P_{\text{bid}}$$

The **relative (percentage) spread**:

$$S_{\%} = \frac{P_{\text{ask}} - P_{\text{bid}}}{P_{\text{mid}}} \times 100$$

where $P_{\text{mid}} = \frac{P_{\text{ask}} + P_{\text{bid}}}{2}$ is the mid price.

The **half-spread cost** per trade (the cost of crossing the spread once):

$$C_{\text{half}} = \frac{S}{2} = \frac{P_{\text{ask}} - P_{\text{bid}}}{2}$$

## Example

A stock has a bid of £49.80 and an ask of £50.20:

$$S = £50.20 - £49.80 = £0.40$$

$$P_{\text{mid}} = \frac{£50.20 + £49.80}{2} = £50.00$$

$$S_{\%} = \frac{£0.40}{£50.00} \times 100 = 0.80\%$$

A trader buying 10,000 shares pays £50.20 (the ask), not the mid price. The implicit cost:

$$C = 10{,}000 \times £0.20 = £2{,}000$$

For a round trip (buy then sell), the trader crosses the spread twice, paying approximately £4,000, or 0.80% of the trade value.

## Remember

The bid-ask spread is the most fundamental transaction cost in financial markets and a key measure of liquidity. Narrow spreads indicate liquid, competitive markets; wide spreads signal illiquidity or information asymmetry. In quantitative finance, the spread directly affects strategy profitability — a high-frequency strategy that earns 1 basis point per trade is worthless if the spread is 5 basis points. The spread also contains information: academic research shows that spread widening precedes periods of higher volatility and that stocks with wider spreads tend to earn higher returns (the liquidity premium). Any realistic backtest must account for spread costs, and execution algorithms like VWAP and TWAP exist specifically to minimise the cost of crossing the spread on large orders.
