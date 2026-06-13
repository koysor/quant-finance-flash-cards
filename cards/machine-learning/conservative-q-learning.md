# Conservative Q-Learning (CQL)

**Topic:** Machine Learning
**Tags:** conservative q-learning, cql, offline rl, out-of-distribution, overestimation, historical data
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Conservative Q-Learning (CQL)** is an offline reinforcement learning algorithm that penalises Q-values for state–action pairs not seen in the training dataset, preventing the policy from exploiting spuriously high Q-values in under-covered regions. Standard Q-learning extrapolates aggressively into unvisited state–action pairs, producing overestimated Q-values that cause the learned policy to take actions never observed in the data. CQL adds a regularisation term that pushes Q-values down for out-of-distribution actions while pushing them up for actions in the dataset, resulting in a conservative lower bound on the true Q-function.

## Key Formula

**CQL objective** — standard Bellman loss plus a conservatism penalty:

$$\mathcal{L}_{\text{CQL}}(\theta) = \underbrace{\mathcal{L}_{\text{Bellman}}(\theta)}_{\text{standard Q-learning}} + \alpha \underbrace{\left(\mathbb{E}_{s \sim \mathcal{D},\, a \sim \pi_\theta}\!\left[Q_\theta(s,a)\right] - \mathbb{E}_{(s,a) \sim \mathcal{D}}\!\left[Q_\theta(s,a)\right]\right)}_{\text{conservatism penalty}}$$

The penalty term:
- **Maximises** $\mathbb{E}_\pi[Q(s,a)]$ — pushes up Q-values under the learned policy (standard RL objective)
- **Minimises** $\mathbb{E}_\mathcal{D}[Q(s,a)]$ — no, actually it **minimises** $\mathbb{E}_\pi[Q]$ and **maximises** $\mathbb{E}_\mathcal{D}[Q]$

Rearranged to show the conservative direction:

$$\min_\theta \; \alpha\!\left(\mathbb{E}_{\pi}\!\left[Q_\theta(s,a)\right] - \mathbb{E}_{\mathcal{D}}\!\left[Q_\theta(s,a)\right]\right) + \mathcal{L}_{\text{Bellman}}(\theta)$$

The coefficient $\alpha > 0$ controls conservatism: larger $\alpha$ shrinks Q-values for out-of-distribution actions more aggressively.

**Guarantee:** CQL produces a lower bound on $Q^\pi$ — it underestimates rather than overestimates, so the policy is safe to deploy: it cannot exploit phantom opportunities.

## Example

**Offline execution agent trained on historical VWAP logs.** Dataset: 2 years of sell orders; the historical algorithm only placed orders in the first 2 hours of the day. Standard Q-learning on this data assigns high Q-values to afternoon selling (never observed, so Bellman targets are extrapolated from the network rather than ground truth). The agent learns to sell aggressively in the afternoon — where it has no data — and performs poorly in deployment.

CQL adds the penalty $\alpha(\mathbb{E}_\pi[Q] - \mathbb{E}_\mathcal{D}[Q])$ which suppresses Q-values for afternoon actions:

| Method | In-sample performance | Out-of-sample (live) |
|---|---|---|
| Standard Q-learning | 98% of VWAP benchmark | 71% — exploits data gaps |
| CQL ($\alpha = 1.0$) | 94% of VWAP benchmark | 91% — conservative extrapolation |
| CQL ($\alpha = 5.0$) | 88% of VWAP benchmark | 93% — very conservative |

Higher $\alpha$ sacrifices in-sample performance for out-of-sample robustness.

## Remember

CQL solves the **distributional shift** problem that makes naive offline RL dangerous in finance. When a bank trains a hedging or execution agent on historical logs, the historical policy's action distribution is narrow — it always did the same thing. The RL agent, optimising Q-values, will find that deviating from the historical policy looks artificially rewarding (because the Q-network has no data there and extrapolates optimistically). CQL's conservatism penalty forces the agent to stay close to the behaviour implicit in the historical data, producing a policy that is safer to deploy. The tuning parameter $\alpha$ encodes the risk manager's trust in the historical data: $\alpha \to 0$ recovers standard Q-learning; $\alpha \to \infty$ recovers behaviour cloning (copying the historical policy exactly). In practice, $\alpha$ is set by cross-validating on a held-out period of the historical log.
