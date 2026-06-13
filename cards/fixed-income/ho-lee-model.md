# Ho–Lee Model

**Topic:** Fixed Income
**Tags:** Ho-Lee, short rate, yield curve fitting, time-dependent drift, no mean reversion, calibration
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **Ho–Lee model** is the simplest interest rate model that can be exactly calibrated to any observed yield curve. It achieves this by replacing the constant drift of Brownian motion with a time-dependent function $\eta(t)$ that is tuned to match market bond prices, while keeping the volatility $c$ constant.

## Key Formula

Under the risk-neutral measure:

$$dr = \eta(t)\,dt + c\,dW_t$$

| Parameter | Meaning | How it is set |
|---|---|---|
| $\eta(t)$ | Time-dependent drift | Calibrated to market yield curve |
| $c$ | Constant volatility | Estimated from historical rate data |

The zero-coupon bond price has the closed-form exponential-affine solution:

$$Z(r,t;T) = e^{A(t;T) - r(T-t)}$$

where $A(t;T) = -\int_t^T \eta(s)(T-s)\,ds + \tfrac{1}{6}c^2(T-t)^3$.

## Example

With $c = 1\%$ per year and today's yield curve implying $\eta(t) \approx 0.002 + 0.001t$, the 2-year bond price is $Z = e^{A(0;2) - r \times 2}$ where $A$ is determined by integrating $\eta$ over $[0,2]$. Changing $\eta(t)$ for any future $t$ shifts the yield curve at maturities beyond $t$ without affecting shorter-maturity bonds.

## Remember

Ho–Lee was the first model to establish the key insight of **yield-curve fitting via a time-dependent drift**: one free function of time is enough to match the entire term structure. Its main weakness is the absence of mean reversion — rates can drift to arbitrarily large values. The Hull–White model fixes this by adding a mean-reversion term $-\gamma r$ while keeping the time-dependent drift, inheriting all of Ho–Lee's calibration power.
