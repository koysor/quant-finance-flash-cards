# Diffusion Coefficient

**Topic:** Stochastic Processes
**Tags:** diffusion, volatility, SDE, stochastic processes, noise, sigma
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

The **diffusion coefficient** is the function that multiplies the random (Brownian) term in a stochastic differential equation. It controls the magnitude of random fluctuations in the process. In the standard asset price SDE $dS = \mu S \, dt + \sigma S \, dW$, the diffusion coefficient is $\sigma S$ — the product of volatility and the current price.

## Key Formula

For a general SDE:

$$dX = a(X, t) \, dt + b(X, t) \, dW$$

$b(X, t)$ is the **diffusion coefficient**. For geometric Brownian motion:

$$b(S, t) = \sigma S$$

The diffusion coefficient determines the **instantaneous variance** of the process:

$$\text{Var}(dS) = b(S, t)^2 \, dt = \sigma^2 S^2 \, dt$$

## Example

A stock trades at $S = 80$ with annualised volatility $\sigma = 0.25$. The diffusion coefficient is:

$$b(80) = 0.25 \times 80 = 20$$

Over a time step $dt = 0.01$ years, the standard deviation of the price change is:

$$\sqrt{\sigma^2 S^2 \, dt} = 20 \times \sqrt{0.01} = £2.00$$

A second stock at $S = 200$ with the same $\sigma$ has diffusion coefficient $b(200) = 50$, giving a standard deviation of £5.00 over the same interval — larger in pound terms but the same 2.5% in percentage terms.

## Remember

The diffusion coefficient is why GBM produces **proportional** rather than **fixed-size** price moves — because $b(S) = \sigma S$ scales with the price, a £1 stock and a £1,000 stock with the same volatility experience the same percentage fluctuations. This multiplicative structure is what keeps simulated prices positive and ensures that the $\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}$ term appears in the Black-Scholes PDE.
