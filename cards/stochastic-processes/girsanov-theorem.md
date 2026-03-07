# Girsanov's Theorem

**Topic:** Stochastic Processes
**Tags:** measure change, risk-neutral, brownian motion, drift, market price of risk
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Girsanov's theorem** describes how to change probability measure so that a Brownian motion with drift under one measure becomes a standard (driftless) Brownian motion under another. It is the fundamental tool for moving between the physical measure $\mathbb{P}$ and the risk-neutral measure $\mathbb{Q}$ in derivative pricing.

## Key Formula

Let $\theta(t)$ satisfy the Novikov condition. Define $\mathbb{Q}$ via:

$$\frac{d\mathbb{Q}}{d\mathbb{P}} = \exp\!\left(-\int_0^T \theta_s\,dX_s - \frac{1}{2}\int_0^T \theta_s^2\,ds\right)$$

Then the process:

$$X_t^{\mathbb{Q}} = X_t + \int_0^t \theta(s)\,ds$$

is a **standard Brownian motion** under $\mathbb{Q}$.

Equivalently: $dX_t = dX_t^{\mathbb{Q}} - \theta(t)\,dt$, so under $\mathbb{Q}$, the original $X_t$ has drift $-\theta$.

## Example

A stock follows $dS = \mu S\,dt + \sigma S\,dX_t$ under $\mathbb{P}$. Set $\theta = (\mu - r)/\sigma$ (the market price of risk). Under $\mathbb{Q}$:

$$dS = rS\,dt + \sigma S\,dX_t^{\mathbb{Q}}$$

With $\mu = 12\%$, $r = 5\%$, $\sigma = 20\%$: $\theta = (0.12 - 0.05)/0.20 = 0.35$.

The drift changes from 12% to 5%, making the discounted price $e^{-rt}S_t$ a martingale under $\mathbb{Q}$.

## Remember

Girsanov's theorem is the engine of risk-neutral pricing. It replaces the real-world drift $\mu$ (which differs across assets and is notoriously difficult to estimate) with the risk-free rate $r$ — a single, observable quantity. This is why the Black–Scholes formula does not depend on $\mu$: Girsanov absorbs it into the definition of Brownian motion under $\mathbb{Q}$. The parameter $\theta = (\mu - r)/\sigma$, the market price of risk, measures how much drift per unit of volatility the measure change must remove and connects the physical and risk-neutral worlds.
