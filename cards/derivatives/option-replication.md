# Option Replication

**Topic:** Derivatives
**Tags:** replication, hedging, delta, no-arbitrage, self-financing portfolio, derivatives pricing
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Option replication is the construction of a portfolio of simpler instruments — typically shares of the underlying and a risk-free bond — whose value exactly matches the option's payoff in every possible future state. The cost of building this **replicating portfolio** today must equal the option's fair price; any discrepancy creates a riskless arbitrage opportunity. Replication is the foundational pricing mechanism in derivatives: rather than estimating probabilities of future outcomes, we price by finding the cost of manufacturing the same payoff synthetically.

## Key Formula

In a one-period model, a call option with payoffs $C_u$ (up state) and $C_d$ (down state) is replicated by holding $\Delta$ shares and $B$ in the risk-free bond:

$$\Delta = \frac{C_u - C_d}{S_u - S_d}$$

$$B = \frac{C_d - \Delta \cdot S_d}{1 + r}$$

The no-arbitrage option price is the cost of the replicating portfolio:

$$C_0 = \Delta \cdot S_0 + B$$

In continuous time (Black–Scholes), the replicating portfolio is **self-financing** and continuously adjusted:

$$dV = \Delta_t \, dS + r(V - \Delta_t S) \, dt$$

where $\Delta_t = \partial V / \partial S = N(d_1)$ for a European call. Setting this equal to $dV$ from Itô's lemma yields the Black–Scholes PDE.

## Example

A stock trades at £100. In one period it moves to either £120 (up) or £85 (down). The risk-free rate is 4%. A European call with strike £105 pays £15 in the up state and £0 in the down state.

The replicating portfolio:

$$\Delta = \frac{15 - 0}{120 - 85} = \frac{15}{35} = 0.4286$$

$$B = \frac{0 - 0.4286 \times 85}{1.04} = \frac{-36.43}{1.04} = -£35.03$$

The option price:

$$C_0 = 0.4286 \times 100 + (-35.03) = 42.86 - 35.03 = £7.83$$

Verification — in the up state: $0.4286 \times 120 + (-35.03) \times 1.04 = 51.43 - 36.43 = £15.00$ ✓. In the down state: $0.4286 \times 85 + (-35.03) \times 1.04 = 36.43 - 36.43 = £0.00$ ✓.

## Remember

Option replication is the idea that connects all of derivatives pricing. The Black–Scholes equation is not derived from assumptions about where the stock price will go — it is derived from the requirement that a continuously rebalanced portfolio of stock and bonds can perfectly replicate the option payoff. This is why the real-world drift $\mu$ does not appear in the Black–Scholes formula: the replicating portfolio eliminates all exposure to the stock's direction. For quant practitioners, understanding replication reveals why options are priced by hedging cost rather than expected payoff, why delta hedging is not merely risk management but the theoretical foundation of pricing itself, and why incomplete markets (where perfect replication fails) require fundamentally different pricing approaches.
