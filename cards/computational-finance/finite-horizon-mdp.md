# Finite-Horizon MDP

**Topic:** Computational Finance
**Tags:** finite horizon, mdp, backward induction, time-dependent policy, option pricing, optimal execution
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **finite-horizon MDP** is an MDP with a fixed terminal time $T$ and no discounting ($\gamma = 1$), where the agent maximises total reward over exactly $T$ steps. Unlike the infinite-horizon discounted MDP, the optimal policy is **time-dependent**: the best action at state $s$ at time $t$ changes as the deadline approaches, because there are fewer remaining steps to recover from a suboptimal choice. Finite-horizon MDPs are solved by **backward induction**, sweeping from $t = T$ back to $t = 0$.

## Key Formula

**Value function** at time $t$ (maximum expected total reward from $t$ to $T$):

$$V_t(s) = \max_a \left[ R(s, a, t) + \sum_{s'} P(s' \mid s, a)\, V_{t+1}(s') \right]$$

**Terminal condition:**

$$V_T(s) = R_T(s)$$

(the terminal payoff — e.g. option payoff, liquidation value).

**Optimal policy** (time-indexed):

$$\pi^*_t(s) = \arg\max_a \left[ R(s, a, t) + \sum_{s'} P(s' \mid s, a)\, V_{t+1}(s') \right]$$

**Comparison with infinite-horizon MDP:**

| Property | Finite-horizon | Infinite-horizon |
|---|---|---|
| Horizon | Fixed $T$ | $T \to \infty$ |
| Discount | $\gamma = 1$ (no discount) | $\gamma < 1$ required |
| Policy | Time-dependent $\pi_t(s)$ | Stationary $\pi(s)$ |
| Solution | Backward induction | Value iteration / policy iteration |
| Finance use | Options, execution | Inventory management, AMM |

## Example

**American put exercise (finite-horizon MDP):** State $s_t = S_t$ (stock price at step $t$), $T = 5$ steps (monthly), $K = 100$, $r = 0.05$, $\sigma = 0.2$. Actions: $\{$hold, exercise$\}$.

**Backward induction from $t = T = 5$:**

$V_5(S) = \max(K - S, 0)$ (intrinsic value at expiry)

$V_4(S) = \max\!\left(K - S,\; e^{-r\Delta t}\,\mathbb{E}[V_5(S')]\right)$ (hold vs exercise)

| $t$ | $S^*(t)$ (exercise boundary) |
|---|---|
| 5 | 100.0 |
| 4 | 95.3 |
| 3 | 91.8 |
| 2 | 88.6 |
| 1 | 85.4 |

The time-dependent policy reveals the free exercise boundary: below $S^*(t)$, exercise immediately; above it, hold. The finite-horizon MDP recovers the same boundary as the binomial tree — because the binomial tree *is* backward induction on a finite-horizon MDP.

## Remember

The finite-horizon MDP is the **unifying framework for all backward-induction-based pricing methods** in quantitative finance. The binomial tree for American options, the Longstaff–Schwartz algorithm for Bermudan options, and backward-in-time dynamic programming for optimal execution are all finite-horizon MDP backward inductions with different state spaces and payoff functions. The critical insight is that **time is part of the state** in a finite-horizon MDP: the same inventory level $I$ demands a different action at $t = T-1$ (sell everything — deadline approaching) versus $t = 1$ (sell gradually — plenty of time). This time-dependency is encoded in the non-stationary optimal policy $\pi^*_t(s)$ and is what distinguishes finite-horizon problems from the stationary policies of infinite-horizon MDPs used for perpetual American options or long-run inventory management.
