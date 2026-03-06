# Rho (Greeks)

**Topic:** Derivatives
**Tags:** rho, Greeks, sensitivity, options, interest rates
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Rho** ($\rho$) is the first-order Greek that measures the rate of change of an option's price with respect to a change in the risk-free interest rate. Formally, $\rho = \partial V / \partial r$. It quantifies how much the option value shifts when interest rates move by one percentage point.

## Key Formula

For European options under Black-Scholes:

$$\rho_{\text{call}} = K T e^{-rT} N(d_2)$$

$$\rho_{\text{put}} = -K T e^{-rT} N(-d_2)$$

Key properties:

- Call Rho is **always positive** — higher rates increase call values because the present value of the strike payment falls.
- Put Rho is **always negative** — higher rates decrease put values for the same reason.
- Rho increases with **time to expiry** — longer-dated options are more sensitive to rate changes.
- Rho is typically the smallest of the first-order Greeks for short-dated equity options, but dominates for long-dated options and interest rate derivatives.

## Example

A European call has $S = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year.

With $d_2 = 0.15$ and $N(0.15) \approx 0.5596$:

$$\rho_{\text{call}} = 100 \times 1 \times e^{-0.05} \times 0.5596 = 95.12 \times 0.5596 = \mathbf{53.23}$$

If rates rise from 5% to 6% (a 1pp increase), the call price increases by approximately £0.53 (since $53.23 \times 0.01 = 0.5323$).

## Remember

Rho is often dismissed as negligible for short-dated equity options, but this is dangerous for long-dated positions. A 2-year LEAPS option can have substantial Rho, and ignoring it during a rate-hiking cycle leads to unexplained P&L. For interest rate derivatives — swaptions, caps, floors — Rho (or its analogues like DV01) is the **primary risk measure**, not a secondary one. Put-call parity also links Rho across calls and puts: $\rho_{\text{call}} - \rho_{\text{put}} = KTe^{-rT}$, providing a useful consistency check.
