# Limit Order Book

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** limit order book, market microstructure, bid, ask, order flow, depth
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The limit order book (LOB) is the electronic record of all outstanding buy and sell limit orders for a security, organised by price level. Buy orders (bids) are ranked from highest to lowest; sell orders (asks) are ranked from lowest to highest. The best bid and best ask form the **top of book** and define the bid-ask spread. When a market order arrives, it is matched against the opposite side of the book at the best available price. The LOB is the fundamental mechanism through which price discovery occurs in modern electronic markets.

## Key Formula

The **mid price**:

$$P_{\text{mid}} = \frac{P_{\text{best bid}} + P_{\text{best ask}}}{2}$$

The **microprice** (volume-weighted mid, a better estimate of fair value):

$$P_{\text{micro}} = \frac{V_{\text{bid}} \cdot P_{\text{ask}} + V_{\text{ask}} \cdot P_{\text{bid}}}{V_{\text{bid}} + V_{\text{ask}}}$$

where $V_{\text{bid}}$ and $V_{\text{ask}}$ are the volumes at the best bid and ask. When there is more volume on the bid side, the microprice shifts towards the ask (predicting upward movement).

The **book depth** at level $k$:

$$D_k = \sum_{i=1}^{k} V_i^{\text{bid}} + \sum_{i=1}^{k} V_i^{\text{ask}}$$

## Example

A stock's order book:

| Level | Bid price | Bid volume | Ask price | Ask volume |
|-------|-----------|-----------|-----------|-----------|
| 1 | £10.00 | 5,000 | £10.02 | 2,000 |
| 2 | £9.98 | 8,000 | £10.04 | 6,000 |
| 3 | £9.96 | 3,000 | £10.06 | 4,000 |

$$P_{\text{mid}} = \frac{£10.00 + £10.02}{2} = £10.01$$

$$P_{\text{micro}} = \frac{5{,}000 \times £10.02 + 2{,}000 \times £10.00}{5{,}000 + 2{,}000} = \frac{£50{,}100 + £20{,}000}{7{,}000} = £10.014$$

The microprice (£10.014) is above the mid (£10.01) because bid volume exceeds ask volume, suggesting buying pressure. A market buy order of 3,000 shares would fill 2,000 at £10.02 and 1,000 at £10.04, for an average price of £10.027.

## Remember

The limit order book is the arena where all trading strategies ultimately execute, and understanding its mechanics is essential for quantitative finance. The LOB reveals supply and demand at every price level, and its dynamics — how orders arrive, cancel, and execute — drive short-term price movements. High-frequency trading strategies use LOB data (order flow imbalance, queue position, depth changes) to predict the next price tick. For lower-frequency strategies, LOB depth determines how much market impact a large order will have and therefore how much it costs to execute. The microprice is a better estimator of fair value than the mid price and is widely used in execution algorithms and market-making strategies.
