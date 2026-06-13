# G2++ Model

**Topic:** Fixed Income
**Tags:** G2++, two-factor Hull-White, Gaussian, swaption, calibration, mean reversion, Brigo-Mercurio
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The G2++ model (Brigo–Mercurio) is a two-factor Gaussian short-rate model in which the short rate is the sum of two correlated Ornstein–Uhlenbeck processes plus a deterministic shift; it fits any initial yield curve exactly and admits closed-form swaption prices.

## Key Formula

$$r(t) = x(t) + y(t) + \varphi(t)$$

$$dx = -ax\,dt + \sigma\,dW_1, \qquad dy = -by\,dt + \eta\,dW_2, \qquad \mathbb{E}[dW_1\,dW_2] = \rho\,dt$$

with $x(0) = y(0) = 0$ and $\varphi(t)$ determined by the initial yield curve (exact fit).

Zero-coupon bond price: $P(t,T) = \frac{P^M(0,T)}{P^M(0,t)}\exp\!\bigl(A(t,T) - B_a(T-t)\,x(t) - B_b(T-t)\,y(t)\bigr)$

where $B_a(\tau) = (1-e^{-a\tau})/a$, $B_b(\tau) = (1-e^{-b\tau})/b$, and $A$ is a known function of the parameters.

Swaption price: analytical formula via a one-dimensional numerical integration over a Gaussian density.

## Example

EUR swaption calibration: $a = 0.10$, $\sigma = 0.007$, $b = 0.80$, $\eta = 0.013$, $\rho = -0.70$. The slow factor ($a = 0.10$, half-life $\approx 7$ yr) drives the long end; the fast factor ($b = 0.80$, half-life $\approx 0.9$ yr) drives the short end. Negative $\rho = -0.70$ reflects the empirical pattern that short rates and the slope of the curve move in opposite directions.

## Remember

G2++ dominates bank trading desks for Bermudan swaption pricing because it combines three crucial properties in one model: exact fit to today's yield curve (via $\varphi(t)$), closed-form European swaption prices for fast calibration, and enough two-factor richness to capture both level and slope movements. Its Gaussian structure allows rates to go negative — historically a limitation but less so after 2014 when EUR and CHF rates went negative and negative-rate models became a practical requirement.
