# Vanna (Greeks)

**Topic:** Derivatives
**Tags:** vanna, Greeks, sensitivity, options, delta, volatility
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Vanna** is the second-order cross Greek that measures the sensitivity of Delta to changes in implied volatility, or equivalently the sensitivity of Vega to changes in the underlying price. Formally, $\text{Vanna} = \partial^2 V / \partial S \, \partial \sigma = \partial \Delta / \partial \sigma = \partial \nu / \partial S$. It links directional risk to volatility risk.

## Key Formula

For European options under Black-Scholes:

$$\text{Vanna} = -\frac{N'(d_1) \, d_2}{\sigma}$$

or equivalently:

$$\text{Vanna} = \frac{\nu}{S}\left(1 - \frac{d_1}{\sigma\sqrt{T}}\right)$$

Key properties:

- Vanna is **positive** for OTM calls and ITM puts (where $d_2 < 0$).
- Vanna is **negative** for ITM calls and OTM puts (where $d_2 > 0$).
- ATM options have Vanna close to zero when $d_2 \approx 0$.
- As volatility rises, the Delta of an OTM call increases (positive Vanna) — the option moves closer to ATM in volatility-adjusted terms.

## Example

A European call has $S = 100$, $K = 105$ (slightly OTM), $\sigma = 20\%$, $T = 0.5$ years, $r = 5\%$.

$$d_1 = \frac{\ln(100/105) + (0.05 + 0.02)(0.5)}{0.20\sqrt{0.5}} = \frac{-0.04879 + 0.035}{0.14142} = -0.0975$$

$$d_2 = -0.0975 - 0.14142 = -0.2389$$

$$N'(-0.0975) \approx 0.3970$$

$$\text{Vanna} = -\frac{0.3970 \times (-0.2389)}{0.20} = \frac{0.0949}{0.20} = \mathbf{0.474}$$

If implied volatility rises by 1pp (from 20% to 21%), Delta increases by approximately $0.474 \times 0.01 = 0.0047$. The option becomes slightly more sensitive to the underlying as volatility rises.

## Remember

Vanna is critical for understanding how the **volatility skew** creates directional exposure. When the market falls sharply, implied volatility typically spikes (the leverage effect). For a portfolio of OTM puts with positive Vanna magnitude, this simultaneous drop in $S$ and rise in $\sigma$ amplifies Delta changes beyond what Gamma alone predicts. Dealers hedging large OTM put positions must account for Vanna flows — as volatility rises, their put Deltas become more negative, forcing them to sell more of the underlying, which can accelerate the sell-off. This **Vanna-driven feedback loop** is a key mechanism behind sharp market dislocations and is closely monitored by systematic volatility traders.
