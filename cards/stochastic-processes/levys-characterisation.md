# Lévy's Characterisation of Brownian Motion

**Topic:** Stochastic Processes
**Tags:** brownian motion, martingale, characterisation, quadratic variation, continuous paths
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Lévy's characterisation** provides an equivalent definition of Brownian motion in terms of martingale properties rather than the classical requirements of independent, normally distributed increments. A continuous process $X_t$ with $X_0 = 0$ is a standard Brownian motion if and only if both $X_t$ and $X_t^2 - t$ are martingales.

## Key Formula

$X_t$ is a Brownian motion if and only if:

1. $X_0 = 0$ a.s. and paths are continuous
2. $X_t$ is a martingale: $\;E[X_t \mid \mathcal{F}_s] = X_s$
3. $X_t^2 - t$ is a martingale: $\;E[X_t^2 - t \mid \mathcal{F}_s] = X_s^2 - s$

| Classical Definition | Lévy's Characterisation |
|---|---|
| Independent increments | $X_t$ is a martingale |
| $X_t - X_s \sim N(0, t - s)$ | $X_t^2 - t$ is a martingale |

## Example

To verify that $X_t^2 - t$ is a martingale, write $X_t = X_s + (X_t - X_s)$ and expand:

$$E[X_t^2 \mid \mathcal{F}_s] = E[(X_s + (X_t - X_s))^2 \mid \mathcal{F}_s] = X_s^2 + 2X_s \cdot 0 + (t - s) = X_s^2 + (t - s)$$

Therefore $E[X_t^2 - t \mid \mathcal{F}_s] = X_s^2 + (t-s) - t = X_s^2 - s$, confirming the martingale property.

## Remember

Lévy's characterisation is the bridge between the abstract martingale theory used in derivative pricing and the concrete properties of Brownian motion. In practice, it allows quants to verify that a process is Brownian motion by checking two martingale conditions rather than proving independence and normality of increments — which is often harder. The second condition ($X_t^2 - t$ is a martingale) encodes that the quadratic variation of Brownian motion is $t$, the fundamental property that drives the Itô correction term $\tfrac{1}{2}\sigma^2 S^2 f_{SS}\,dt$ in stochastic calculus.
