# Soft Actor-Critic (SAC)

**Topic:** Machine Learning
**Tags:** soft actor-critic, maximum entropy, entropy bonus, exploration, continuous action, stochastic policy
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Soft Actor-Critic (SAC)** augments the standard RL objective with an entropy bonus, training the agent to simultaneously maximise cumulative reward and the entropy of its policy. This produces stochastic policies that maintain calibrated uncertainty over actions — preventing the collapse to a single deterministic hedge ratio that can occur in PPO when the optimal action is ambiguous or the reward landscape is flat.

## Key Formula

The **maximum-entropy objective** augments the return with policy entropy $\mathcal{H}(\pi(\cdot \mid s))$:

$$J(\pi) = \mathbb{E}\!\left[\sum_{t=0}^{T} \gamma^t \Bigl(r_t + \alpha\,\mathcal{H}\!\left(\pi(\cdot \mid s_t)\right)\Bigr)\right]$$

where $\alpha > 0$ is the **temperature** parameter controlling the exploration-exploitation trade-off. The resulting **soft Bellman equation** is:

$$Q_\text{soft}(s, a) = r + \gamma\,\mathbb{E}_{s'}\!\left[V_\text{soft}(s')\right], \quad V_\text{soft}(s) = \mathbb{E}_{a \sim \pi}\!\left[Q_\text{soft}(s, a) - \alpha \log\pi(a \mid s)\right]$$

SAC automatically tunes $\alpha$ by treating it as a Lagrange multiplier constrained to maintain a target entropy $\mathcal{H}_\text{target}$.

## Example

A SAC agent and a PPO agent both learn to hedge a short straddle. Near expiry with spot exactly at the strike, both policies face genuine uncertainty: small hedge adjustments in either direction are nearly equivalent. PPO collapses to a deterministic policy (always buy 0.03 delta) due to gradient pressure. SAC maintains a Gaussian policy with std = 0.02 delta, effectively spreading the hedge across a range of small adjustments — better representing the genuine indifference between nearby actions and avoiding over-trading costs from unnecessarily precise but arbitrary hedging decisions.

## Remember

SAC's entropy bonus is the RL equivalent of **regularisation**: just as L2 weight decay prevents a neural network from committing too strongly to any single feature, the entropy term prevents the policy from committing too strongly to any single action when the evidence is weak. For derivatives hedging this is financially meaningful — a stochastic SAC policy naturally implements a **band-of-indifference** around the target delta, only rebalancing when the expected gain from trading exceeds the entropy cost, which corresponds directly to transaction-cost-aware hedging without explicitly modelling costs as a penalty.
