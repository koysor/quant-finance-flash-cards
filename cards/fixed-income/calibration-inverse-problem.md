# Calibration as an Inverse Problem

**Topic:** Fixed Income
**Tags:** calibration, inverse problem, ill-conditioning, yield curve, drift estimation
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

**Calibration as an inverse problem** means recovering the unknown drift function $\eta(t)$ of an interest rate model from observed market bond prices, rather than using $\eta(t)$ to compute prices. The forward problem maps parameters to prices; calibration inverts that map — finding the parameters that produce given prices.

## Key Formula

For the Ho–Lee model, setting model prices equal to market prices $Z_M(t^*;T)$ gives the integral equation:

$$\int_{t^*}^T \eta^*(s)(T-s)\,ds = -\log Z_M(t^*;T) - r^*(T-t^*) + \frac{1}{6}c^2(T-t^*)^3$$

| Direction | Known | Unknown |
|---|---|---|
| Forward problem | $\eta(t)$, $c$ | $Z(r,t;T)$ for each $T$ |
| Inverse problem (calibration) | $Z_M(t^*;T)$ for each $T$, $c$ | $\eta^*(t)$ |

The right-hand side is entirely determined by observable market data; the challenge is recovering the function $\eta^*(t)$ from the left-hand side integral.

## Example

Given $Z_M(0; 1) = 0.962$, $Z_M(0; 2) = 0.925$, $Z_M(0; 5) = 0.815$ and $r^* = 3.5\%$, $c = 1\%$, the integral equation at each maturity gives a constraint on $\eta^*$. Differentiating twice with respect to $T$ produces the explicit formula $\eta^*(T) = c^2(T - t^*) - \partial^2_{TT}\log Z_M(t^*;T)$ at each maturity.

## Remember

Inverse problems in finance are **ill-conditioned**: small measurement errors in bond prices can produce large swings in the recovered drift function $\eta^*(t)$. This is why the volatility $c$ cannot be extracted from the yield curve alone — it needs independent historical estimation — and why calibrated drifts are sensitive to the smoothing method applied to raw bond price data. The ill-conditioning is not a numerical artefact; it reflects a genuine information limit in what today's yield curve can tell you.
