# Optimal Stopping Time

**Topic:** Stochastic Processes
**Tags:** optimal stopping, stopping time, american option, value function, dynamic programming, free boundary
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **optimal stopping time** $\tau^*$ is the stopping time that maximises the expected discounted reward from a stochastic process. The holder of an American-style contract faces this decision at every instant: stop now (exercise) or continue (hold). The key constraint is that $\tau^*$ must be adapted — the decision to stop at time $t$ may depend only on information available up to $t$, not the future.

## Key Formula

The value function is the supremum over all stopping times $\mathcal{T}$:

$$V(t, S) = \sup_{\tau \geq t} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(\tau-t)}\,g(S_\tau) \mid S_t = S\right]$$

where $g(S)$ is the immediate reward (e.g. $\max(K - S, 0)$). The **optimal stopping time** is the first instant the value equals the immediate reward:

$$\tau^* = \inf\!\left\{t \geq 0 : V(t, S_t) = g(S_t)\right\}$$

In discrete time, the Bellman recursion gives the value function directly:

$$V_t = \max\!\left(g(S_t),\; e^{-r\Delta t}\,\mathbb{E}^{\mathbb{Q}}\!\left[V_{t+1} \mid \mathcal{F}_t\right]\right), \qquad V_T = g(S_T)$$

## Example

American put: $K = 100$, $r = 5\%$, solved by backward induction at $t = 0.5$:

| $S$ | Payoff $g$ | Continuation $V$ | Action |
|---|---|---|---|
| 70 | 30 | 27 | **Stop** — $V = g$, exercise now |
| 90 | 10 | 11 | Continue — $V > g$, hold |
| 110 | 0 | 0 | Continue — $V = g = 0$, no benefit |

At $S = 70$, the payoff dominates the continuation value, so $\tau^* = 0.5$ in this path. The **free exercise boundary** $S^*(t)$ is the stock price at which $V(t, S) = g(S)$ for each $t$ — any stock price below $S^*(t)$ triggers immediate exercise.

## Remember

The optimal stopping time $\tau^*$ is the random clock ticking inside every American option. The quant's job is to locate the **exercise boundary** $S^*(t)$ — the curve separating the holding region (where $V > g$) from the exercise region (where $V = g$). All American-option algorithms — binomial trees, finite-difference PDEs, Longstaff–Schwartz Monte Carlo, and OST-TDBP — solve the same underlying problem: computing $V(t, S)$ by backward induction from $V_T = g(S_T)$, and reading off $\tau^*$ as the first time the boundary is crossed.
