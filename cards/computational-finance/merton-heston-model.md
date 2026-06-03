# Merton-Heston Model

**Topic:** Computational Finance
**Tags:** merton-heston, stochastic volatility, jump diffusion, hybrid model, option pricing, vol-of-vol
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Merton-Heston model** is a hybrid stochastic model combining **Heston stochastic volatility** (mean-reverting CIR variance process) with **Merton jump diffusion** (Poisson-distributed price jumps). It captures both the persistent volatility clustering and sudden price gaps that arise in equity markets from news events or macroeconomic shocks.

## Key Formula

**Stock price** (with Poisson jumps):

$$\frac{dS_t}{S_{t^-}} = \mu\,dt + \sqrt{V_t}\,dW_t^S + (J - 1)\,dN_t - \lambda\,\mathbb{E}[J-1]\,dt$$

**Variance process** (CIR / Heston):

$$dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V, \qquad \text{corr}(dW^S, dW^V) = \rho\,dt$$

where $N_t$ is a Poisson process with intensity $\lambda$ (jumps per year), $J$ is the log-normal jump multiplier, $\kappa$ is mean-reversion speed, $\theta$ is long-run variance, and $\xi$ is the volatility of variance. The term $-\lambda\,\mathbb{E}[J-1]\,dt$ compensates the drift for the expected jump.

## Example

Parameters: $\sigma_0 = 0.20$, $\xi = 0.30$, $\lambda = 4$, $\mathbb{E}[\ln J] = -0.02$. A 1-month 5-delta put is priced at £0.45 under pure Heston. Adding Merton jumps raises it to £0.72 — a 60% increase driven by the heavier left tail from clustered negative jumps, which the Heston diffusion alone cannot produce.

## Remember

Merton-Heston is the benchmark "realistic" model for stress-testing RL pricing agents: a TDBP model trained on Merton-Heston paths prices options under simultaneous stochastic vol and jumps without solving the costly characteristic-function integrals (Carr-Madan FFT) that traditional calibration requires. The negative Heston correlation $\rho < 0$ (leverage effect) combined with negatively skewed Merton jumps reproduces the steep left skew of equity implied volatility surfaces that simpler models cannot match.
