# Two-Factor Short-Rate Models

**Topic:** Fixed Income
**Tags:** two-factor model, Brennan-Schwartz, Fong-Vasicek, Longstaff-Schwartz, G2++, affine model
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

**Two-factor short-rate models** extend one-factor models by introducing a second stochastic state variable to capture yield-curve slope and curvature dynamics. The most tractable members of this family use affine drift and square-root diffusion so that bond prices remain exponential-affine, though at the cost of solving ODEs in three scalar functions $A$, $B$, and $C$.

## Key Formula

For a general two-factor affine model with uncorrelated factors, the bond price is:

$$V(r, l, t) = e^{A(t) - B(t)r - C(t)l}$$

where $A$, $B$, $C$ satisfy a system of three coupled Riccati ODEs — generally solved numerically.

| Model | Factors | Closed form? | Key property |
|---|---|---|---|
| Brennan–Schwartz (1982) | $r$, long rate $l$ | No | Observable factors; can blow up |
| Fong–Vasicek (1991) | $r$, variance $\xi$ | Yes (simple products) | Tractable; $\xi$ unobservable |
| Longstaff–Schwartz (1992) | Two CIR factors $x$, $y$ | Yes | $r = cx + dy$; non-negative |
| G2++ / Two-Factor Hull–White | Two Gaussian OU processes | Yes | Calibrates to yield curve |

**Longstaff–Schwartz factor dynamics:**

$$dx = a(\bar{x} - x)\,dt + \sqrt{x}\,dX_1, \quad dy = b(\bar{y} - y)\,dt + \sqrt{y}\,dX_2$$

$$r = c\,x + d\,y$$

## Example

The G2++ model (two-factor Hull–White) is calibrated to EUR swaptions: parameters $a = 0.15$, $\sigma = 0.008$, $b = 0.90$, $\eta = 0.012$, $\rho = -0.65$. The fast factor ($b = 0.90$) drives the short end; the slow factor ($a = 0.15$) drives the long end. Pricing error on EUR 10Y-into-2Y swaptions drops from 5 bp (one-factor) to 0.3 bp — a 15× improvement in yield-curve option fit.

## Remember

The Brennan–Schwartz model is historically important but practically dangerous: its lognormal-type volatility specification can cause rates to explode to infinity in finite time. The square-root models (Fong–Vasicek, Longstaff–Schwartz) are safer but use unobservable factors. In practice, the G2++ model dominates bank trading desks for Bermudan swaptions because it combines Gaussian tractability, closed-form bond prices, and direct calibration to both the yield curve and the swaption surface.
