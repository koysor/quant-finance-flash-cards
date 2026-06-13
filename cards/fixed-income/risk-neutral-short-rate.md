# Risk-Neutral Short Rate

**Topic:** Fixed Income
**Tags:** risk-neutral measure, short rate, Q-measure, pricing, Monte Carlo, drift adjustment
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **risk-neutral short rate** is the spot rate process under the risk-neutral measure $\mathbb{Q}$, obtained by subtracting $\lambda w$ from the real-world drift. It is the version of the short-rate SDE used for pricing fixed-income derivatives and for Monte Carlo simulation.

## Key Formula

Starting from the real-world SDE $dr = u(r,t)\,dt + w(r,t)\,dX$, the risk-neutral SDE is:

$$dr = \bigl(u(r,t) - \lambda(r,t)\,w(r,t)\bigr)\,dt + w(r,t)\,dX^{\mathbb{Q}}$$

| Measure | Drift | Brownian motion |
|---|---|---|
| $\mathbb{P}$ (real world) | $u(r,t)$ | $dX^{\mathbb{P}}$ |
| $\mathbb{Q}$ (risk-neutral) | $u - \lambda w$ | $dX^{\mathbb{Q}} = dX^{\mathbb{P}} + \lambda\,dt$ |

**For zero-coupon bond pricing via Monte Carlo:**

1. Simulate the risk-neutral rate: $r_{i+1} = r_i + (u - \lambda w)\Delta t + w\sqrt{\Delta t}\,Z_i$, $Z_i \sim \mathcal{N}(0,1)$
2. Compute the path discount factor: $e^{-\sum_i r_i \Delta t}$
3. Average over paths: $V = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r\,ds}\right]$

## Example

For Vasicek with real drift $u = \eta - \gamma r = 0.03 - 0.5r$ and $w = \sqrt{\beta} = 0.01$ and $\lambda = -2$, the risk-neutral drift is $(0.03 - 0.5r) - (-2)(0.01) = 0.05 - 0.5r$. The long-run risk-neutral mean rises from 6% to 10%, reflecting the negative risk premium (bond investors accept a lower yield than the expected rate would imply).

## Remember

Always simulate the **risk-neutral** rate for pricing: using the physical drift $u$ produces systematically biased prices because it ignores the risk premium. The risk-neutral measure is not about investors being risk-neutral — it is a mathematical device that discounts risky cash flows consistently. Any instrument priced with the physical measure will show apparent arbitrage versus market prices.
