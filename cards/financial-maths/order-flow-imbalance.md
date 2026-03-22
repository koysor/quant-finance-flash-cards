# Order Flow Imbalance

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** order flow imbalance, microstructure, price impact, limit order book, alpha signal
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Order flow imbalance (OFI) measures the net buying or selling pressure in the limit order book over a given interval. It aggregates the changes in the best bid and ask quantities — additions to the bid or removals from the ask indicate buying pressure; removals from the bid or additions to the ask indicate selling pressure. OFI is one of the strongest short-term predictors of price movement, as it directly captures the supply-demand imbalance before the price adjusts.

## Key Formula

The **order flow imbalance** at time $t$:

$$\text{OFI}_t = \sum_{i=1}^{n} e_i$$

where each event $e_i$ is defined as:

$$e_i = \mathbb{1}_{P_{\text{bid}}^i \geq P_{\text{bid}}^{i-1}} \cdot \Delta V_{\text{bid}}^i - \mathbb{1}_{P_{\text{bid}}^i \leq P_{\text{bid}}^{i-1}} \cdot \Delta V_{\text{bid}}^{i-} + \mathbb{1}_{P_{\text{ask}}^i \leq P_{\text{ask}}^{i-1}} \cdot \Delta V_{\text{ask}}^{i-} - \mathbb{1}_{P_{\text{ask}}^i \geq P_{\text{ask}}^{i-1}} \cdot \Delta V_{\text{ask}}^i$$

The **linear price impact** model:

$$\Delta P_{\text{mid}} = \lambda \cdot \text{OFI}_t + \epsilon_t$$

where $\lambda$ is the price impact coefficient (Kyle's lambda).

## Example

Over a 1-minute interval, the following order book changes occur at the best bid/ask:

| Event | Bid change | Ask change | $e_i$ |
|-------|-----------|-----------|-------|
| Bid volume +2,000 (same price) | +2,000 | 0 | +2,000 |
| Market buy lifts 1,500 from ask | 0 | $-1{,}500$ | +1,500 |
| Bid cancelled 3,000 | $-3{,}000$ | 0 | $-3{,}000$ |
| Ask replenished +4,000 | 0 | +4,000 | $-4{,}000$ |

$$\text{OFI} = 2{,}000 + 1{,}500 - 3{,}000 - 4{,}000 = -3{,}500$$

Negative OFI indicates net selling pressure. If $\lambda = 0.0001$ £ per share:

$$\Delta P_{\text{mid}} = 0.0001 \times (-3{,}500) = -£0.35$$

The model predicts the mid price will decline by £0.35 in the next interval.

## Remember

Order flow imbalance is the microstructure signal that connects the limit order book to price movement, and understanding it is essential for any quant developer working on execution or high-frequency strategies. Cont, Kukanov, and Stoikov (2014) showed that OFI explains over 65% of contemporaneous mid-price changes — far more than trade volume or returns alone. In practice, OFI is used for short-term alpha generation (predicting the next price move), optimal execution (timing trades when flow is favourable), and market making (adjusting quotes based on imbalance). The signal decays rapidly (seconds to minutes), so exploiting it requires low-latency infrastructure and direct market data feeds.
