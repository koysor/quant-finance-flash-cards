# A3C (Asynchronous Advantage Actor-Critic)

**Topic:** Machine Learning
**Tags:** a3c, actor-critic, asynchronous, parallel workers, policy gradient, deep reinforcement learning
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

**A3C (Asynchronous Advantage Actor-Critic)** is a deep RL algorithm in which multiple worker threads run independent copies of the environment in parallel, compute local gradients using the advantage function, and asynchronously push gradient updates to a shared global network. Workers periodically pull the latest global weights and resume collecting experience, creating natural decorrelation of training data without requiring an experience replay buffer.

## Key Formula

Each worker $i$ computes the actor gradient over a local rollout of length $t_{\max}$:

$$\nabla_{\theta_i}\mathcal{L}_i = \sum_{t=0}^{t_{\max}} \nabla_{\theta_i}\log\pi_{\theta_i}(a_t \mid s_t)\cdot\hat{A}_t - c_e\nabla_{\theta_i}\mathcal{H}(\pi_{\theta_i}(\cdot \mid s_t))$$

where $\hat{A}_t = \sum_{k=0}^{n-1}\gamma^k r_{t+k} + \gamma^n V(s_{t+n}) - V(s_t)$ is the $n$-step advantage estimate and $c_e$ controls the entropy bonus. The worker pushes $\nabla_{\theta_i}\mathcal{L}_i$ to the global network and applies it to $\theta_{\text{global}}$ with RMSProp, then pulls fresh weights $\theta_i \leftarrow \theta_{\text{global}}$.

## Example

Sixteen worker threads each simulate a different GBM path for a delta-hedging task. Each worker steps forward 20 time steps (one rollout), computes the 20-step advantage using a local copy of the shared critic, and pushes gradients to the global actor and critic networks. Workers update asynchronously: worker 3 may push its gradient while worker 7 is still mid-rollout. The asynchrony means the global network sees gradients computed under slightly stale weights — a form of implicit regularisation that prevents overfitting to any single market trajectory. Training converges in approximately 2 hours of wall-clock time across 16 threads, versus 8 hours with a single worker.

## Remember

A3C replaced DQN's experience replay with asynchronous parallelism as the decorrelation mechanism — instead of randomly sampling from a replay buffer (which requires memory and off-policy correction), it runs multiple workers simultaneously so consecutive gradient updates are computed in different parts of the state space. In finance, the key drawback is **non-reproducibility**: because workers update in random order, two training runs with identical seeds diverge — a significant problem for regulatory backtesting and model validation. This is why A2C (the synchronous variant) became preferred in quantitative research, sacrificing some wall-clock speed for reproducible, auditable training runs. A3C was superseded by PPO for most financial RL tasks.

