# Convergence of TD Learning

**Topic:** Computational Finance
**Tags:** td convergence, robbins-monro, step size, stochastic approximation, convergence guarantee, tabular rl
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Convergence of TD learning** refers to the conditions under which temporal difference algorithms provably reach the true value function. In the tabular setting (finite states, exact Q-table), TD(0) and Q-learning converge almost surely to $V^\pi$ and $Q^*$ respectively, provided the step sizes satisfy the **Robbins–Monro conditions** and every state–action pair is visited infinitely often. With function approximation, convergence is not guaranteed and divergence is a genuine practical risk.

## Key Formula

**Robbins–Monro step-size conditions** — necessary for stochastic approximation (and hence TD) convergence:

$$\sum_{t=0}^\infty \alpha_t = \infty \qquad \text{(steps large enough to overcome any initialisation)}$$

$$\sum_{t=0}^\infty \alpha_t^2 < \infty \qquad \text{(steps shrink fast enough to suppress noise)}$$

**Typical schedule:** $\alpha_t = 1/(t+1)$ satisfies both: $\sum 1/(t+1) = \infty$ and $\sum 1/(t+1)^2 = \pi^2/6 < \infty$.

**TD(0) contraction** — in the tabular case, the Bellman operator $\mathcal{T}^\pi$ is a $\gamma$-contraction in $\|\cdot\|_\infty$:

$$\|\mathcal{T}^\pi V - \mathcal{T}^\pi U\|_\infty \leq \gamma \|V - U\|_\infty$$

so repeated application converges geometrically to $V^\pi$ at rate $\gamma^k$ per iteration.

**Deadly triad** — function approximation + bootstrapping + off-policy learning together can cause divergence, even when each pair alone is stable.

| Setting | Convergence | Condition |
|---|---|---|
| Tabular TD(0), on-policy | Almost sure | Robbins–Monro + all states visited |
| Tabular Q-learning, off-policy | Almost sure | Same conditions |
| Linear FA, on-policy TD | Almost sure | Robbins–Monro (Tsitsiklis–Van Roy) |
| Nonlinear FA (DQN), off-policy | Not guaranteed | Target network reduces but doesn't eliminate risk |

## Example

**Step-size effect on a hedging agent:** A delta-hedging RL agent with 100 states (moneyness × time-to-expiry grid), trained on 50,000 simulated episodes.

With constant step size $\alpha = 0.1$: converges quickly but oscillates around the true value; never fully settles (noise term $\sum \alpha_t^2 = \infty$ — second condition violated).

With $\alpha_t = 1/t$: satisfies both conditions; RMS error vs Black–Scholes:

| Episodes | Constant $\alpha=0.1$ | Decaying $\alpha_t=1/t$ |
|---|---|---|
| 5,000 | 0.041 | 0.089 |
| 20,000 | 0.038 | 0.023 |
| 50,000 | 0.037 | 0.008 |

Constant step-size converges faster initially but plateaus at a noise floor; decaying step-size converges to the true value but needs more episodes.

## Remember

The Robbins–Monro conditions explain a puzzling empirical observation in financial RL: **constant learning rate agents perform well on short training runs but degrade over time**, while decaying schedules improve indefinitely. In practice, decaying learning rates are rarely used in deep RL for finance because the function approximator's weights must also adapt to non-stationarity (changing market regimes). The standard solution is a **constant but small** step size (e.g. $\alpha = 10^{-4}$) with a replay buffer and periodic network resets — sacrificing the convergence guarantee for adaptability. The convergence theory tells you why: a constant step size violates $\sum \alpha_t^2 < \infty$, so the agent permanently tracks a noisy estimate rather than the true value function. This is acceptable if the true value function itself is shifting, but catastrophic if you need provably optimal behaviour — for example, in a regulatory-approved automated trading system where the algorithm must be certifiably stable.
