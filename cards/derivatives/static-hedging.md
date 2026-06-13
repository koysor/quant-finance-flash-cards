# Static Hedging

**Topic:** Derivatives
**Tags:** static hedging, barrier option, put-call parity, replication, exotic options, model risk
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Static hedging** constructs a fixed portfolio of vanilla instruments at inception that replicates an exotic payoff for the entire life of the trade, with no rebalancing required. It exploits symmetry: if two portfolios have identical payoffs at every boundary, no-arbitrage forces their prices to agree everywhere, so the hedge holds without any intervening trades.

## Key Formula

The simplest static hedge is put-call parity — a European forward is exactly replicated by a long call minus a short put at the same strike, held to expiry with zero rebalancing:

$$F_T = C(K) - P(K)$$

For a **down-and-out call** (DOC) with barrier $B < K$ under zero rates and log-symmetric dynamics, the **reflection hedge** gives:

$$\text{DOC}(S_0, K) = C(S_0, K) - \frac{S_0}{B} \cdot C\!\left(\frac{B^2}{S_0},\; \frac{B^2}{K}\right)$$

where the second term is a scaled vanilla call at the reflected spot $B^2/S_0$ and reflected strike $B^2/K$.

## Example

A trader sells a DOC: $S_0 = 100$, $K = 110$, $B = 90$, $r = 0$. The static hedge is:

- Buy 1 vanilla call struck at 110
- Sell $100/90 \approx 1.11$ vanilla calls struck at $90^2/110 \approx 73.6$, with current spot reflected to $90^2/100 = 81$

Both legs are transacted at inception; no further trading occurs unless spot hits 90, at which point the DOC pays nothing and the static portfolio is unwound.

## Remember

Static hedging matters most on exotic desks where delta hedging becomes prohibitively expensive or unreliable. A barrier option's delta diverges as spot approaches the barrier, so dynamic rebalancing would incur enormous transaction costs right when the hedge is most critical. Locking in a static replica at inception shifts the risk from hedge-slippage costs to model mis-specification — specifically, whether the log-symmetry assumption holds. Desks favour static hedges for illiquid underlyings where the bid–offer cost of continuous rebalancing would consume the entire option premium.
