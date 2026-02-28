# American vs European Options

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** American options, European options, early exercise, options pricing, comparison
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The distinction between **American** and **European** options lies in when the holder may exercise. A European option can only be exercised at expiry; an American option can be exercised at any time up to expiry. This single difference has profound consequences for pricing methodology, put-call parity, and optimal hedging strategy.

## Key Formula

The early-exercise premium is the difference in value:

$$\text{Early-exercise premium} = V_{\text{American}} - V_{\text{European}} \geq 0$$

Key relationships:

$$C_{\text{American}} = C_{\text{European}} \quad \text{(non-dividend-paying stock)}$$

$$P_{\text{American}} \geq P_{\text{European}}$$

Put-call parity holds exactly only for European options:

$$C_E - P_E = S_0 - K e^{-rT}$$

For American options, the relationship becomes an inequality:

$$S_0 - K \leq C_A - P_A \leq S_0 - K e^{-rT}$$

## Example

Consider two puts with $K = 100$, $S_0 = 85$, $r = 5\%$, $\sigma = 25\%$, $T = 1$ year.

The European put price (via Black-Scholes) is approximately £12.58. The American put price (via binomial tree) is approximately £15.00.

Early-exercise premium = £15.00 − £12.58 = **£2.42**

The premium is significant here because the put is deep in the money — exercising now yields £15 in cash that earns interest, versus waiting for a payoff that may shrink.

## Remember

The choice between American and European pricing is not academic — it determines which tools you can use. European options admit closed-form Black-Scholes prices and exact put-call parity. American options require numerical methods (trees, PDE grids, or Monte Carlo with regression) and break put-call parity into bounds. In practice, equity options are mostly American and index options are mostly European, so a quant must be fluent in both frameworks.
