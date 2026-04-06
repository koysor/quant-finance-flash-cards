# Stopping Time Notation

**Topic:** Mathematical Notation
**Tags:** notation, stopping time, hitting time, optional stopping, American option, tau
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

A **stopping time** $\tau$ is a random variable that represents the time at which a decision is made or an event is triggered, based only on information available up to that time (i.e., $\tau$ is adapted to the filtration $\{\mathcal{F}_t\}$).

| Symbol | Read as | Meaning |
|---|---|---|
| $\tau$ | "tau" | A stopping time (generic) |
| $\tau^*$ | "optimal tau" | The optimal stopping time |
| $T_H$ or $\tau_H$ | "first hitting time of $H$" | First time the process reaches level $H$ |
| $\tau_b = \inf\{t > 0 : X_t \leq b\}$ | "first passage time below $b$" | First time process falls below barrier $b$ |
| $\tau \wedge T$ | "tau min T" | $\min(\tau, T)$ — stopped at the earlier of $\tau$ or $T$ |

The condition that $\tau$ is a stopping time is written: $\{\tau \leq t\} \in \mathcal{F}_t$ for all $t \geq 0$.

## Key Formula

**American option price** as supremum over stopping times:

$$V_0^{\text{Am}} = \sup_{\tau \in \mathcal{T}} E^{\mathbb{Q}}\!\left[e^{-r\tau}(S_\tau - K)^+\right]$$

**First passage time** (Brownian motion hitting level $b$ from 0):

$$\tau_b = \inf\{t \geq 0 : W_t = b\}$$

**Optional Stopping Theorem** — for a martingale $M_t$ and bounded stopping time $\tau$:

$$E[M_\tau] = E[M_0]$$

## Example

A knock-out barrier option expires worthless if the spot price $S_t$ hits barrier $H = 90$ before maturity $T$. The knock-out time is:

$$\tau_H = \inf\{t \in [0,T] : S_t \leq H\}$$

The option payoff is $(S_T - K)^+ \cdot \mathbf{1}_{\tau_H > T}$ — the vanilla payoff multiplied by the indicator that the barrier was never breached. Pricing requires computing the joint distribution of $S_T$ and $\tau_H$ under $\mathbb{Q}$.

## Remember

The **Optional Stopping Theorem** is why American options are harder to price than European options. The American holder can choose $\tau^*$ — the optimal exercise time — which makes the price a supremum rather than a simple expectation. Early exercise of an American call on a non-dividend-paying stock is never optimal (the supremum is attained at $\tau^* = T$), but for American puts the early exercise boundary is non-trivial and requires a free-boundary PDE or dynamic programming to characterise. The symbol $\tau$ is reserved almost universally in stochastic calculus for stopping times, making it one of the most recognisable single-letter conventions in quant finance.
