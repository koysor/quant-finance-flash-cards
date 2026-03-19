# Limits to Arbitrage

**Topic:** Derivatives
**Tags:** arbitrage, transaction costs, market frictions, short-selling, funding constraints, mispricing
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

In a frictionless market, any mispricing would be instantly eliminated by arbitrageurs. In practice, **limits to arbitrage** are the real-world frictions that prevent this, allowing mispricings to persist:

- **Transaction costs** — bid-ask spreads, brokerage commissions, taxes
- **Short-selling constraints** — securities lending fees, inability to borrow stock
- **Funding risk** — arbitrage positions may require capital; margin calls can force early liquidation before the mispricing corrects
- **Noise trader risk** — irrational investors can push prices further from fair value, generating losses before eventual convergence

These frictions create a **band of no-arbitrage** around the theoretical fair value within which mispricings can survive.

## Key Formula

An arbitrage trade between two equivalent assets priced at $P_A$ and $P_B$ ($P_A > P_B$) is profitable only if the gross profit exceeds all costs:

$$P_A - P_B > 2s + c_f$$

where $s$ is the half bid-ask spread on each leg and $c_f$ is the funding cost over the holding period.

More generally, the **no-arbitrage band** around fair value $V$ is:

$$V - (s + c_f) \leq \text{market price} \leq V + (s + c_f)$$

Prices within this band cannot be exploited profitably.

## Example

Suppose a futures contract on an index is theoretically priced at £100 via the cost-of-carry model, but trades at £100.30. The bid-ask spread is £0.20 (£0.10 each side) and borrowing/funding costs are £0.15.

Total friction cost: $0.10 + 0.10 + 0.15 = £0.35$

Since $£0.30 < £0.35$, the mispricing is **not** exploitable — it sits within the no-arbitrage band and will persist.

## Remember

Limits to arbitrage explain why real markets are not perfectly efficient even when smart money exists. In quantitative finance, this underpins phenomena such as the persistent equity premium puzzle, the closed-end fund discount, and why index-futures basis can deviate from theoretical cost-of-carry values, especially during periods of market stress when funding liquidity dries up.
