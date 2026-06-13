# Hull-White Volatility Calibration to Caps

**Topic:** Fixed Income
**Tags:** Hull-White, volatility calibration, cap, caplet, swaption, mean reversion, sigma, alpha, implied vol
**Created:** 2026-06-14
**Author:** Claude Sonnet 4.6

---

## Definition

Yield-curve calibration of Hull-White pins the time-dependent drift $\theta(t)$ from bond prices alone, but the two volatility parameters — mean-reversion speed $\alpha$ and short-rate volatility $\sigma$ — are **invisible in the yield curve**. They must be fitted separately to the cap or swaption volatility surface so the model reproduces option market prices as well as bond prices.

## Key Formula

Under Hull-White, a caplet resetting at $T_1$ and paying at $T_2$ equals a put on a zero-coupon bond. Its Black-formula implied vol is:

$$\sigma_P = \frac{\sigma}{\alpha}\!\left(1 - e^{-\alpha(T_2-T_1)}\right)\sqrt{\frac{1 - e^{-2\alpha T_1}}{2\alpha}}$$

Volatility calibration minimises the sum of squared implied-vol errors across observed cap maturities:

$$\min_{\alpha,\,\sigma}\;\sum_{i}\!\left(\sigma^{market}_i - \sigma^{model}_i(\alpha,\sigma)\right)^2$$

This is a **two-parameter nonlinear least-squares** problem. In practice $\alpha$ is often fixed from historical rate data (time-series estimate) and only $\sigma$ is fitted to each vol tenor.

## Example

ATM 1y cap Black vol = 80 bps, 5y cap vol = 55 bps. With $\alpha = 0.05$, fitting $\sigma$ matches the 5y point at $\sigma = 0.010$ but overestimates the 1y vol by 12 bps. Reducing $\alpha$ to 0.02 flattens the $\sigma_P(T)$ curve and halves the 1y error. A joint fit over a grid of cap tenors converges to $\alpha = 0.03$, $\sigma = 0.009$.

## Remember

Hull-White calibration has two legs: **first**, fit $\theta(t)$ to the yield curve (bond prices); **second**, fit $(\alpha,\sigma)$ to the cap or swaption vol surface (option prices). Without the second leg the model mis-hedges rate options even when bond prices are correct — the rate distribution is mis-specified in width and shape.
