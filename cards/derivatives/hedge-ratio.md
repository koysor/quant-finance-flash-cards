# Hedge Ratio

**Topic:** Derivatives
**Tags:** hedge ratio, delta, replication, binomial model, options, risk management
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **hedge ratio** is the number of units of the underlying asset needed to offset the price risk of one unit of a derivative. In the binomial model it is computed exactly from the spread of option values divided by the spread of stock prices across the two successor nodes. In the continuous-time Black-Scholes framework the hedge ratio equals **delta** ($\Delta = \partial V / \partial S$), the first partial derivative of the option price with respect to the underlying.

## Key Formula

**Binomial (one-step) hedge ratio:**

$$\Delta = \frac{V^{+} - V^{-}}{S^{+} - S^{-}}$$

where $V^{+}$, $V^{-}$ are the option values and $S^{+}$, $S^{-}$ are the stock prices in the up and down states respectively.

**Black-Scholes hedge ratio** for a European call:

$$\Delta_{\text{call}} = N(d_1)$$

where $N(\cdot)$ is the cumulative standard normal distribution function.

**Minimum-variance hedge ratio** (used for futures hedging):

$$h^{*} = \rho \, \frac{\sigma_S}{\sigma_F}$$

where $\rho$ is the correlation between spot and futures price changes, $\sigma_S$ is the standard deviation of spot price changes, and $\sigma_F$ is the standard deviation of futures price changes.

## Example

A one-step binomial tree has $S_0 = \text{£}100$, $S^{+} = 120$, $S^{-} = 80$. A call with strike $K = 105$ has payoffs $V^{+} = 15$ and $V^{-} = 0$.

$$\Delta = \frac{15 - 0}{120 - 80} = \frac{15}{40} = 0.375$$

To replicate the call, buy **0.375 shares** per option. If the stock rises to £120, the share position is worth $0.375 \times 120 = \text{£}45$; if it falls to £80, the position is worth $0.375 \times 80 = \text{£}30$. The difference of £15 matches the option payoff spread exactly, confirming the hedge works.

## Remember

- The hedge ratio is the bridge between derivatives pricing theory and practice: it tells a trader precisely how much of the underlying to hold in order to neutralise directional risk.
- In the binomial model the hedge ratio is a simple ratio of spreads; in continuous time it becomes the partial derivative $\partial V / \partial S$, which is delta.
- For cross-hedging with futures (e.g. hedging jet fuel exposure with crude oil futures), the **minimum-variance hedge ratio** $h^{*} = \rho \, \sigma_S / \sigma_F$ accounts for the imperfect correlation between the hedging instrument and the exposure — ignoring this leads to either under-hedging or over-hedging.
