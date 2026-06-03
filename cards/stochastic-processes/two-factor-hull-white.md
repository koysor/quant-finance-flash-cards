# Two-Factor Hull-White Model

**Topic:** Stochastic Processes
**Tags:** g2++, two-factor hull-white, short rate, gaussian, swaption, affine model
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The two-factor Hull-White model (G2++) decomposes the short rate into two correlated mean-reverting Gaussian factors plus a deterministic shift calibrated to today's yield curve, capturing both level and slope dynamics and producing a richer swaption volatility structure than the single-factor model.

## Key Formula

The short rate is:

$$r_t = x_t + y_t + \varphi(t)$$

where $x_t$ and $y_t$ are correlated Ornstein-Uhlenbeck processes:

$$dx_t = -a\,x_t\,dt + \sigma\,dW_t^1, \qquad dy_t = -b\,y_t\,dt + \eta\,dW_t^2$$

with $\text{corr}(dW^1, dW^2) = \rho\,dt$ and five parameters $(a, b, \sigma, \eta, \rho)$. Zero-coupon bond prices remain in closed exponential-affine form:

$$P(t,T) = \exp\!\left(A(t,T) - B_a(t,T)\,x_t - B_b(t,T)\,y_t\right)$$

where $B_a(\tau) = (1-e^{-a\tau})/a$ and $B_b(\tau) = (1-e^{-b\tau})/b$ are solutions to decoupled linear Riccati ODEs.

## Example

EUR swaption calibration: $a = 0.15$, $\sigma = 0.008$, $b = 0.90$, $\eta = 0.012$, $\rho = -0.65$. The fast-reverting $y$-factor ($b = 0.90$) drives short-rate humps visible in 1-year swaption vols; the slow $x$-factor ($a = 0.15$) controls long-run level. Negative $\rho$ captures the empirical tendency for short and long rate shocks to partially offset. Pricing error on 10Y-into-2Y swaptions: 0.3bp (G2++) versus 5bp (one-factor Hull-White) — a 15× improvement.

## Remember

A single-factor interest rate model implies that all yield curve movements are perfectly correlated — if the 2-year rate rises, the 30-year rate always rises by a proportional amount. Real yield curves exhibit steepening and flattening where short and long rates move independently. The G2++ model's two factors explicitly capture this: the fast factor drives short-maturity vol while the slow factor drives long-maturity level, jointly producing the correlation structure between 1-year and 10-year swaption vols that banks need to price and hedge callable bonds and Bermudan swaptions.
