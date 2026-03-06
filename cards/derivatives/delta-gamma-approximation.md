# Delta-Gamma Approximation

**Topic:** Derivatives
**Tags:** delta, gamma, Taylor series, P&L, risk management, options
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

The **Delta-Gamma approximation** uses a second-order Taylor expansion to estimate the change in an option's price for a given move in the underlying. It improves on the linear Delta approximation by incorporating the curvature captured by Gamma, giving a more accurate estimate for larger price moves.

## Key Formula

$$\Delta V \approx \Delta \cdot \Delta S + \tfrac{1}{2} \, \Gamma \cdot (\Delta S)^2$$

where $\Delta V$ is the change in option value, $\Delta S$ is the change in the underlying price, $\Delta$ is the first-order sensitivity, and $\Gamma$ is the second-order sensitivity.

The full Taylor expansion including Theta and Vega:

$$\Delta V \approx \Delta \cdot \Delta S + \tfrac{1}{2} \, \Gamma \cdot (\Delta S)^2 + \Theta \cdot \Delta t + \nu \cdot \Delta \sigma$$

## Example

A call option has $\Delta = 0.50$, $\Gamma = 0.04$, and the stock moves from £100 to £103 ($\Delta S = 3$).

**Delta-only estimate:**

$$\Delta V \approx 0.50 \times 3 = £1.50$$

**Delta-Gamma estimate:**

$$\Delta V \approx 0.50 \times 3 + \tfrac{1}{2} \times 0.04 \times 9 = 1.50 + 0.18 = \mathbf{£1.68}$$

The Gamma term adds £0.18, reflecting the option's convexity. The Delta-only estimate understates the gain because Delta itself increases as the stock rises.

## Remember

The Delta-Gamma approximation is the workhorse of daily **P&L attribution** on trading desks. Risk managers decompose each day's profit or loss into components: how much came from Delta (directional), Gamma (convexity), Theta (time decay), and Vega (volatility). The residual — the gap between the Taylor approximation and the actual P&L — is called **unexplained P&L** and flags model risk or missing risk factors. Value-at-Risk models also use the Delta-Gamma approach to estimate portfolio losses under large moves without repricing every option.
