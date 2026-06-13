# Fixed-Income Pricing PDE

**Topic:** Fixed Income
**Tags:** pricing PDE, interest rate, bond pricing, short rate, no-arbitrage, Black-Scholes analogy
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **fixed-income pricing PDE** is the parabolic partial differential equation that every interest rate derivative must satisfy under the no-arbitrage condition derived from hedging one bond against another. It is structurally identical to the Black–Scholes equation, with the spot rate $r$ playing the role of the underlying and the market price of risk $\lambda$ adjusting the drift.

## Key Formula

$$\frac{\partial V}{\partial t} + \frac{1}{2}w^2\frac{\partial^2 V}{\partial r^2} + (u - \lambda w)\frac{\partial V}{\partial r} - rV = 0$$

where $u(r,t)$ is the real-world drift of $r$, $w(r,t)$ is the volatility of $r$, and $\lambda(r,t)$ is the market price of interest rate risk.

| Term | Financial meaning |
|---|---|
| $\partial V/\partial t$ | Time decay (theta) |
| $\tfrac{1}{2}w^2\,\partial^2 V/\partial r^2$ | Convexity in $r$ (gamma) |
| $(u - \lambda w)\,\partial V/\partial r$ | Delta in $r$ under the risk-neutral drift |
| $-rV$ | Discounting at the spot rate |

**Zero-coupon bond boundary condition:** $V(r, T) = 1$

## Example

For Vasicek ($u = \eta - \gamma r$, $w = \sqrt{\beta}$, $\lambda$ absorbed into $\eta$), the PDE becomes:

$$\frac{\partial V}{\partial t} + \frac{\beta}{2}\frac{\partial^2 V}{\partial r^2} + (\eta - \gamma r)\frac{\partial V}{\partial r} - rV = 0$$

Trying $V = e^{A(\tau) - B(\tau)r}$ (exponential-affine ansatz) reduces this PDE to two ODEs in the single variable $\tau = T - t$.

## Remember

This PDE is the workhorse of one-factor interest rate modelling. The $-rV$ term discounts at the stochastic spot rate — it does not come from a drift term — and the drift appearing is the **risk-neutral** drift $u - \lambda w$, not the physical drift $u$. Using $u$ instead of $u - \lambda w$ is a common exam error that produces systematically wrong bond prices.
