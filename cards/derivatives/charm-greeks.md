# Charm (Delta Decay)

**Topic:** Derivatives
**Tags:** charm, Greeks, delta, time decay, options, hedging
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Charm** (also called **Delta decay** or **DdeltaDtime**) is the second-order Greek that measures the rate of change of Delta with respect to the passage of time. Formally, $\text{Charm} = -\partial \Delta / \partial t = -\partial^2 V / \partial S \, \partial t$. It tells a trader how much their hedge ratio will drift overnight even if the underlying price does not move.

## Key Formula

For a European call under Black-Scholes:

$$\text{Charm}_{\text{call}} = -N'(d_1)\left[\frac{2(r - q)T - d_2 \sigma \sqrt{T}}{2T\sigma\sqrt{T}}\right]$$

For a non-dividend-paying stock ($q = 0$):

$$\text{Charm}_{\text{call}} = -N'(d_1)\left[\frac{2rT - d_2 \sigma \sqrt{T}}{2T\sigma\sqrt{T}}\right]$$

Key properties:

- Charm is largest in magnitude for **ATM options near expiry**, where Delta is most sensitive to the passage of time.
- For OTM calls, Charm is typically negative — Delta drifts towards zero as expiry nears.
- For ITM calls, Charm is typically positive — Delta drifts towards one.
- Put Charm can be derived from call Charm via put-call parity.

## Example

A trader is delta-hedged on a call position with $\Delta = 0.55$ and $\text{Charm} = -0.03$ per day.

Over the weekend (2 calendar days, no trading), the hedge ratio drifts by:

$$\Delta_{\text{new}} \approx 0.55 + (-0.03) \times 2 = \mathbf{0.49}$$

The trader was hedged by holding 0.55 shares per option, but Monday's correct hedge is only 0.49 shares. Without rebalancing, they are **over-hedged** by 0.06 shares per option — carrying unwanted directional exposure.

## Remember

Charm matters most over weekends and holidays, when time passes but markets are closed and no rebalancing can occur. Options desks adjust their Friday hedges using Charm to anticipate Monday's Delta, reducing the gap that opens from calendar time passing without trading. Near expiry, Charm can be very large for ATM options — Delta swings rapidly between 0 and 1 as time runs out, and Charm quantifies exactly how fast that swing happens per unit of time. It is one of the key "minor Greeks" that separates textbook hedging from real-world risk management.
