# Volatility Term Structure

**Topic:** Volatility
**Tags:** volatility term structure, implied volatility, mean reversion, term structure, options
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **volatility term structure** is the curve of at-the-money implied volatility plotted against option maturity. It captures how the market's expectation of future volatility varies across time horizons. The shape of the term structure — upward-sloping, downward-sloping (inverted), or humped — provides information about whether the market expects current volatility conditions to persist, intensify, or mean-revert.

## Key Formula

If volatility mean-reverts to a long-run level $\bar{\sigma}$ with speed $\kappa$, the term structure of implied variance satisfies approximately:

$$\sigma_{\text{impl}}^2(T) \approx \bar{\sigma}^2 + (\sigma_0^2 - \bar{\sigma}^2) \times \frac{1 - e^{-2\kappa T}}{2\kappa T}$$

where $\sigma_0$ is the current instantaneous volatility.

**Key relationships:**

- When $\sigma_0 > \bar{\sigma}$: term structure is **downward-sloping** (inverted) — current vol is elevated and expected to fall
- When $\sigma_0 < \bar{\sigma}$: term structure is **upward-sloping** — current vol is low and expected to rise
- As $T \to \infty$: $\sigma_{\text{impl}}(T) \to \bar{\sigma}$

## Example

During a market sell-off, 1-month ATM implied vol on the S&P 500 spikes to 35%, while 1-year ATM vol rises to only 22%. The term structure is steeply inverted:

| Maturity | Implied Vol |
|---|---|
| 1 month | 35% |
| 3 months | 28% |
| 6 months | 24% |
| 1 year | 22% |

The market is saying: volatility is high now but will mean-revert. A trader who believes the crisis will persist longer than the market expects might buy 3-month options (relatively cheap at 28%) rather than 1-month options (expensive at 35%).

## Remember

The volatility term structure is the time dimension of the volatility surface (the smile/skew is the strike dimension). In calm markets the term structure is typically gently upward-sloping, reflecting uncertainty about future shocks. During crises it inverts sharply, as near-term fear dominates. The speed at which the term structure flattens out reveals the market's implied mean-reversion speed $\kappa$ — a key calibration input for stochastic volatility models like Heston. Calendar spread strategies (buying one expiry, selling another) are direct bets on the shape of the term structure.
