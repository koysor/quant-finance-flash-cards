# Colour (Greeks)

**Topic:** Derivatives
**Tags:** colour, color, Greeks, sensitivity, options, gamma, time decay
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Colour** (also spelled **Color** in American English) is the third-order Greek that measures the rate of change of Gamma with respect to the passage of time. Formally, $\text{Colour} = \partial \Gamma / \partial t$. It tells a trader how their Gamma exposure will evolve as time passes, even if the underlying price stays unchanged — the Gamma analogue of Charm (which measures Delta decay).

## Key Formula

For European options under Black-Scholes:

$$\text{Colour} = -\frac{N'(d_1)}{2S\sigma T\sqrt{T}}\left[2qT + 1 + d_1\left(\frac{2(r-q)T - d_2\sigma\sqrt{T}}{\sigma\sqrt{T}}\right)\right]$$

For a non-dividend-paying stock ($q = 0$):

$$\text{Colour} = -\frac{N'(d_1)}{2S\sigma T\sqrt{T}}\left[1 + d_1\left(\frac{2rT - d_2\sigma\sqrt{T}}{\sigma\sqrt{T}}\right)\right]$$

Key properties:

- For ATM options, Colour is typically **negative** — Gamma increases as expiry approaches (the payoff kink sharpens).
- For deep OTM/ITM options, Colour can be positive — Gamma may decrease as time erodes any remaining curvature.
- Colour is most significant near expiry for near-the-money strikes.

## Example

A trader holds a Gamma-hedged portfolio with net $\Gamma = 500$ and $\text{Colour} = -120$ per year.

Over a 1-day period ($\Delta t = 1/365 \approx 0.00274$):

$$\Delta\Gamma \approx -120 \times 0.00274 = \mathbf{-0.33}$$

Gamma shifts from 500 to approximately 500.33 in magnitude (since Colour is negative, ATM Gamma is growing). By Friday, the drift accumulates to roughly $-120 \times 5/365 = -1.64$. The trader's Gamma hedge drifts by more than one unit over the week, requiring rebalancing even if the spot does not move.

## Remember

Colour is the time dimension of Gamma risk. Near expiry, ATM Gamma can spike dramatically — a phenomenon called the **Gamma pin risk** — and Colour quantifies how fast that spike is developing. Options desks managing large inventories of short-dated options track Colour to anticipate how their risk profile will evolve overnight and over weekends. Combined with Charm (Delta decay) and Veta (Vega decay), Colour completes the picture of how all the major Greeks drift with calendar time alone, independent of any market move.
