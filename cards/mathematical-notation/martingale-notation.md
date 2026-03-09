# Martingale Notation

**Topic:** Mathematical Notation
**Tags:** martingale, local martingale, filtration, conditional expectation, no-arbitrage
**Created:** 2026-03-09
**Author:** Claude Sonnet 4.6

---

## Definition

A **martingale** $(M_t)_{t \geq 0}$ is a stochastic process whose conditional expectation of any future value equals its present value — it has no predictable trend. The notation $M \in \mathcal{M}^2$ means $M$ is a square-integrable martingale (finite variance at all times).

| Symbol | Read as | Meaning |
|---|---|---|
| $(M_t)_{t \geq 0}$ | "M sub t" | A process indexed by time; values change randomly |
| $M_t = E[M_T \mid \mathcal{F}_t]$ | "M at t equals conditional expectation of M at T" | Defining property: best forecast of the future is today's value |
| $M \in \mathcal{M}^2$ | "M in M-squared" | Square-integrable martingale: $E[M_t^2] < \infty$ for all $t$ |
| $M \in \mathcal{M}^2_{\text{loc}}$ | "local martingale" | A process that is "locally" a martingale; may fail the integrability condition globally |
| $\widetilde{S}_t = e^{-rt} S_t$ | "S-tilde, the discounted price" | The discounted asset price that should be a $\mathbb{Q}$-martingale |

## Key Formula

The **martingale property** under a filtration:

$$E[M_T \mid \mathcal{F}_t] = M_t, \qquad 0 \leq t \leq T$$

**Doob's optional stopping theorem** (value at a stopping time $\tau$):

$$E[M_\tau] = E[M_0] \quad \text{under integrability conditions}$$

**Discounted price as martingale** under the risk-neutral measure $\mathbb{Q}$:

$$E^{\mathbb{Q}}\!\left[e^{-rT} S_T \mid \mathcal{F}_t\right] = e^{-rt} S_t$$

## Example

A fair coin-flip game: start with £0, win £1 if heads, lose £1 if tails. Let $M_n$ be cumulative winnings after $n$ flips. Then $E[M_{n+1} \mid M_1, \ldots, M_n] = M_n$ — knowing the full history, your best forecast of next period's wealth is your current wealth. This is a martingale. If instead the coin is biased (heads more likely), $E[M_{n+1} \mid \mathcal{F}_n] > M_n$ and the process is a **submartingale**.

## Remember

In finance, the **fundamental theorem of asset pricing** says that a market is arbitrage-free if and only if there exists a measure $\mathbb{Q}$ (the risk-neutral measure) under which discounted prices are martingales. Writing $\widetilde{S}_t = e^{-rt}S_t$ as a $\mathbb{Q}$-martingale is the compact notation that encapsulates the entire no-arbitrage pricing framework. The local martingale distinction matters in practice: some replicating strategies are only local martingales, and the Novikov condition $E[\exp(\frac{1}{2}\int_0^T \theta_s^2 \, ds)] < \infty$ is the standard check that a local martingale is a true martingale.
