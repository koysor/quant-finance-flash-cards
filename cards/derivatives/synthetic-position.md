# Synthetic Position

**Topic:** Derivatives
**Tags:** synthetic position, put-call parity, replication, arbitrage, options strategy
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

A synthetic position replicates the payoff of one instrument using a combination of other instruments. The most common examples use put-call parity to construct synthetic stock, synthetic calls, or synthetic puts from combinations of options and the underlying. Synthetic positions allow traders to achieve equivalent exposures when the desired instrument is unavailable, illiquid, or more expensive than its synthetic equivalent — and any price discrepancy between an instrument and its synthetic creates an arbitrage opportunity.

## Key Formula

From put-call parity ($C - P = S - Ke^{-rT}$), the three core synthetics:

**Synthetic long stock:**

$$S = C - P + Ke^{-rT}$$

Buy a call, sell a put at the same strike and expiry, and invest the present value of the strike in the risk-free bond.

**Synthetic long call:**

$$C = S + P - Ke^{-rT}$$

Buy the stock, buy a put, and borrow the present value of the strike.

**Synthetic long put:**

$$P = C - S + Ke^{-rT}$$

Buy a call, short the stock, and invest the present value of the strike.

## Example

A stock trades at £50. The 3-month ATM call (strike £50) is priced at £3.20 and the ATM put at £2.50. The risk-free rate is 4%. The present value of the strike is:

$$Ke^{-rT} = 50 \times e^{-0.04 \times 0.25} = £49.50$$

A synthetic long stock costs: $C - P + Ke^{-rT} = £3.20 - £2.50 + £49.50 = £50.20$.

The actual stock costs £50.00, so the synthetic is £0.20 more expensive. A trader can arbitrage this by buying the real stock at £50.00, selling the synthetic (sell call, buy put, borrow £49.50), and locking in a riskless profit of £0.20 per share. At expiry, whichever way the stock moves, the positions cancel out perfectly.

## Remember

Synthetic positions are one of the most practical applications of put-call parity on trading desks. In practice, traders use synthetics when borrowing stock for a short sale is difficult or expensive — a synthetic short (short call + long put) achieves the same economic exposure without actually borrowing shares. Structured product desks routinely construct synthetic exposures to embed within notes. For quant finance, the key insight is that synthetics make the concept of replication tangible: if you can replicate an instrument from simpler parts, the prices must be consistent — and when they are not, the discrepancy is a measurable, tradeable mispricing.
