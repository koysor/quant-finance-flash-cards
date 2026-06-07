# RL Convergence Guarantees

**Topic:** Computational Finance
**Tags:** convergence, deadly triad, function approximation, divergence, theoretical rl, stability
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**RL convergence guarantees** are the theoretical conditions under which reinforcement learning algorithms provably converge to the optimal value function or policy. In the tabular setting (finite states, exact lookup tables), convergence is well-established under mild conditions. With **function approximation** (neural networks, linear approximators), three properties — **bootstrapping**, **off-policy data**, and **function approximation** — interact to form the **deadly triad**: any two are safe together, but all three simultaneously can cause divergence, even with a simple linear function approximator.

## Key Formula

**Tabular Q-learning convergence theorem** (Watkins & Dayan, 1992): Q-learning converges to $Q^*$ almost surely if:
- All state–action pairs are visited infinitely often
- Step sizes satisfy $\sum_t \alpha_t = \infty$ and $\sum_t \alpha_t^2 < \infty$
- Rewards are bounded

**Linear TD with on-policy data** (Tsitsiklis & Van Roy, 1997): TD(0) with linear function approximation $V_\theta(s) = \theta^\top \phi(s)$ converges to:

$$\theta^* = \arg\min_\theta \|V_\theta - V^\pi\|_{\mu}^2 \quad \text{(projection of } V^\pi \text{ onto linear span of } \phi\text{)}$$

provided data is on-policy. The **deadly triad** shows each pair is stable but all three together are not:

| Bootstrapping | Off-policy | Function approx | Convergence |
|---|---|---|---|
| ✓ | ✗ | ✓ | Stable (on-policy linear TD) |
| ✓ | ✓ | ✗ | Stable (tabular Q-learning) |
| ✗ | ✓ | ✓ | Stable (Monte Carlo + FA) |
| ✓ | ✓ | ✓ | **Can diverge** (DQN regime) |

**DQN's mitigation** (not a fix — a reduction in divergence risk): target network + experience replay reduce non-stationarity but do not restore the convergence guarantee.

## Example

**Baird's counterexample** (a classic divergence case): a 7-state MDP with linear function approximation and off-policy data. The TD update rule:

$$\theta \leftarrow \theta + \alpha \cdot \delta_t \cdot \phi(s_t)$$

With on-policy data: $\|\theta_t\|$ stays bounded, converges to fixed point.

With off-policy data (uniform random exploration): $\|\theta_t\| \to \infty$ — the parameters diverge to infinity even though the MDP is simple and the linear approximator has enough capacity.

**Practical finance implication:** a DQN hedging agent trained off-policy with a neural network is in the deadly triad regime. Without target network stabilisation:

| Training step | Max Q-value | Hedging RMSE |
|---|---|---|
| 10,000 | 4.2 | 0.031 |
| 50,000 | 18.7 | 0.051 |
| 100,000 | 412 | 0.19 |

Q-values explode; the policy degenerates. With target network ($C = 1{,}000$ step freeze): Q-values stabilise below 6.0 and RMSE converges to 0.018.

## Remember

The deadly triad is the reason **every practical deep RL algorithm for finance uses at least one stabilisation trick**. DQN uses a target network and experience replay; PPO avoids off-policy data entirely (on-policy); SAC uses entropy regularisation that implicitly damps the Bellman bootstrap. The convergence theory tells you *which* of these tricks is essential for *which* algorithm. For a new financial RL application, the question to ask is: "Am I in the deadly triad?" — if the answer is yes (neural network + TD bootstrapping + historical replay buffer), you must use target networks or some form of behavioural regularisation, and you should treat convergence as an empirical matter validated by monitoring Q-value magnitudes, not a mathematical certainty.
