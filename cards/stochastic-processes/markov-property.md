# Markov Property

**Topic:** Stochastic Processes
**Tags:** markov, memoryless, martingale, state dependence, stochastic process
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A stochastic process has the **Markov property** if its future evolution depends only on its current state, not on its past history. Formally, the conditional distribution of $M_{t+1}$ given the entire filtration $\mathcal{F}_t$ equals the conditional distribution given only $M_t$. The Markov property means **memoryless**; this is independent of the martingale property, which means **driftless**.

## Key Formula

$$E[f(M_{t+1}) \mid \mathcal{F}_t] = E[f(M_{t+1}) \mid M_t]$$

for all measurable functions $f$.

| Property | Martingale | Markov |
|---|---|---|
| Key word | Driftless | Memoryless |
| Constrains | Conditional mean equals current value | Distribution depends only on current state |
| Drift allowed? | No | Yes |
| Path dependence? | Allowed | Not allowed |

## Example

| Process | Martingale? | Markov? |
|---|---|---|
| Standard Brownian motion $X_t$ | Yes | Yes |
| $X_t + 4t$ (BM with drift) | No (drift $= 4$) | Yes |
| $\max_{s \leq t} X_s$ (running maximum) | No | No |

Brownian motion with drift $X_t + 4t$ is Markov because its future depends only on its current level, but it is not a martingale because its expected value increases over time.

## Remember

The distinction between Markov and martingale properties matters for model selection in quantitative finance. Standard models (GBM, Vasicek, CIR) are both Markov and martingale-compatible, enabling PDE-based pricing where the option value depends only on the current state $(S, t)$. Path-dependent derivatives like Asian or lookback options break the Markov property because their payoffs depend on the entire price history — requiring either augmented state spaces or Monte Carlo simulation rather than simple backward-induction PDEs.
