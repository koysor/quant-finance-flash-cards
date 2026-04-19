# Diffusion Processes

**Topic:** Stochastic Processes
**Tags:** diffusion, SDE, drift, volatility, Itô process, Brownian motion, continuous path
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

A **diffusion process** is a continuous-time stochastic process whose sample paths are continuous (no jumps) and whose dynamics are governed by a stochastic differential equation (SDE) with a drift term and a diffusion term driven by Brownian motion. The class includes Brownian motion, geometric Brownian motion, and mean-reverting processes such as Ornstein-Uhlenbeck.

## Key Formula

General Itô diffusion (one-dimensional):

$$dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t$$

where:
- $\mu(X_t, t)$ — **drift function**: determines the average direction of movement
- $\sigma(X_t, t)$ — **diffusion coefficient**: controls the instantaneous volatility
- $W_t$ — standard Brownian motion (the source of randomness)

The transition density $p(x, t \mid x_0, t_0)$ satisfies the **Fokker-Planck equation**:

$$\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}[\mu\, p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 p]$$

## Example

Geometric Brownian Motion: $\mu(S,t) = \mu S$, $\sigma(S,t) = \sigma S$. CIR interest rate model: $\mu(r,t) = \kappa(\bar{r}-r)$, $\sigma(r,t) = \sigma\sqrt{r}$. Both are diffusions — continuous paths, no jumps, fully characterised by their drift and diffusion functions.

## Remember

Virtually every continuous-time asset pricing model in quantitative finance is a diffusion process: the choice of drift and diffusion functions encodes the economic assumptions. GBM (constant proportional volatility) gives Black-Scholes. Mean-reverting drift gives Vasicek/CIR for rates. State-dependent volatility $\sigma(S,t)$ gives local volatility models. The Fokker-Planck equation is the forward equation governing the evolution of the risk-neutral density used to price path-dependent derivatives.
