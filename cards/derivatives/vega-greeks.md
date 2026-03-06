# Vega (Greeks)

**Topic:** Derivatives
**Tags:** vega, Greeks, sensitivity, options, volatility, implied volatility
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Vega** ($\nu$ or $\mathcal{V}$) is the Greek that measures the rate of change of an option's price with respect to a change in the implied volatility of the underlying. Formally, $\nu = \partial V / \partial \sigma$. Despite its name, Vega is not an actual Greek letter — it is a convention adopted by the finance industry.

## Key Formula

For European options under Black-Scholes (calls and puts have identical Vega):

$$\nu = S \, N'(d_1) \sqrt{T}$$

where $N'(d_1)$ is the standard normal PDF evaluated at $d_1$.

Key properties:

- Vega is **always positive** for long option positions — higher volatility increases the value of both calls and puts.
- ATM options have the largest Vega; deep ITM and OTM options have negligible Vega.
- Vega increases with time to expiry — longer-dated options are more sensitive to volatility changes.
- Vega is typically quoted per **1 percentage point** change in implied volatility.

## Example

A European call has $S = 100$, $K = 100$, $\sigma = 20\%$, $T = 0.25$ years.

With $d_1 = 0.175$ and $N'(0.175) \approx 0.3932$:

$$\nu = 100 \times 0.3932 \times \sqrt{0.25} = 100 \times 0.3932 \times 0.50 = \mathbf{19.66}$$

If implied volatility rises from 20% to 21% (a 1pp increase), the option price increases by approximately £0.20 (since $19.66 \times 0.01 = 0.1966$).

## Remember

Vega is the key Greek for **volatility trading**. When a trader buys a straddle (long call + long put at the same strike), they are primarily expressing a view that implied volatility is too low — the position is long Vega. The **volatility smile** exists precisely because the market prices different strikes at different implied volatilities, meaning Vega exposure varies across the strike spectrum. Traders decompose their book's Vega by tenor and strike to manage exposure to parallel shifts, skew moves, and term-structure changes in the implied volatility surface.
