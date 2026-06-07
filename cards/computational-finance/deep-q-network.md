# Deep Q-Network (DQN)

**Topic:** Computational Finance
**Tags:** dqn, deep reinforcement learning, experience replay, target network, q-learning, neural network
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Deep Q-Network (DQN)** replaces the tabular Q-table in Q-learning with a neural network $Q(s, a;\, \theta)$ that approximates the action-value function for large or continuous state spaces. Two key stabilisation tricks make neural Q-learning converge: **experience replay** (storing and randomly sampling past transitions to break temporal correlation) and a **target network** (a periodically frozen copy of the network used to compute TD targets, preventing oscillation). DQN was introduced by DeepMind (2015) and is the foundation of modern deep reinforcement learning for sequential decision making.

## Key Formula

**Q-network loss** (mean squared Bellman error over a mini-batch from the replay buffer):

$$\mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}}\!\left[\left(y - Q(s, a;\, \theta)\right)^2\right]$$

where the **TD target** uses the frozen target network $\theta^-$:

$$y = r + \gamma \max_{a'} Q(s', a';\, \theta^-)$$

**Parameter update** via gradient descent:

$$\theta \leftarrow \theta - \alpha \nabla_\theta \mathcal{L}(\theta)$$

**Target network sync:** copy $\theta^- \leftarrow \theta$ every $C$ steps (e.g. $C = 1{,}000$).

**Double DQN** (reduces overestimation bias) splits action selection and evaluation:

$$y^{\text{DDQN}} = r + \gamma\, Q\!\left(s',\; \arg\max_{a'} Q(s', a';\, \theta);\; \theta^-\right)$$

## Example

**Option exercise as DQN:** State $s_t = (S_t, t)$ (stock price, time to expiry). Actions: $a \in \{\text{hold}, \text{exercise}\}$. Reward: $r = \max(K - S_T, 0)$ at terminal step, 0 elsewhere.

Replay buffer stores tuples $(s_t, a_t, r_t, s_{t+1})$ from simulated GBM paths. Network: 2-layer MLP with inputs $(S_t/K, t/T)$, outputs $Q(\cdot, \text{hold})$ and $Q(\cdot, \text{exercise})$.

| Training step | Replay buffer size | RMSE vs binomial |
|---|---|---|
| 10,000 | 5,000 | 0.48 |
| 100,000 | 50,000 | 0.12 |
| 500,000 | 100,000 | 0.04 |

At 500k steps, the DQN exercise boundary closely matches the binomial tree's critical stock price $S^*(t)$ — DQN learns the optimal stopping rule without requiring the Black–Scholes PDE.

## Remember

DQN's two inventions — **experience replay** and the **target network** — solve the same instability problem from opposite directions. Experience replay breaks the temporal correlation in consecutive transitions (a GBM path at $t=1, 2, \ldots, T$ is highly correlated, so training on sequential samples causes the network to overfit each time step). The target network prevents the loss function's goalposts from moving every gradient step, which would cause the Q-values to oscillate or diverge. In finance, DQN is most naturally applied to **discrete-action problems**: American option exercise (hold vs exercise), order placement (post limit vs hit market), and trade scheduling (trade vs wait). For continuous actions like hedge ratios, actor-critic methods (SAC, PPO) are preferred. The key financial insight is that DQN turns the Hamilton–Jacobi–Bellman equation — which requires knowing the dynamics — into a pure data-driven optimisation, making it applicable to real market data where the true price process is unknown.
