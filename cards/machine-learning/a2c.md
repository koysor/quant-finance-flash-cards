# A2C (Advantage Actor-Critic)

**Topic:** Machine Learning
**Tags:** a2c, actor-critic, synchronous, parallel workers, policy gradient, reinforcement learning
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

**A2C (Advantage Actor-Critic)** is a synchronous, parallel variant of the actor-critic algorithm in which multiple independent worker environments collect experience simultaneously, and all gradient updates are batched and applied to a single shared network after each round of collection. It is the synchronous counterpart to A3C (Asynchronous Advantage Actor-Critic) and a direct predecessor to PPO, combining the variance reduction of the advantage function with stable, reproducible training via synchronised updates.

## Key Formula

A2C minimises a combined loss over a mini-batch of transitions collected from $N$ parallel workers:

$$\mathcal{L}(\theta, \phi) = \mathcal{L}_{\text{actor}}(\theta) + c_v\,\mathcal{L}_{\text{critic}}(\phi) - c_e\,\mathcal{H}(\pi_\theta)$$

**Actor loss** (policy gradient with advantage):

$$\mathcal{L}_{\text{actor}}(\theta) = -\mathbb{E}_t\!\left[\log\pi_\theta(a_t \mid s_t)\cdot\hat{A}_t\right]$$

**Critic loss** (mean squared TD error):

$$\mathcal{L}_{\text{critic}}(\phi) = \mathbb{E}_t\!\left[\left(r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)\right)^2\right]$$

**Advantage estimate** (single-step TD):

$$\hat{A}_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)$$

where $c_v$ weights the critic loss and $c_e$ controls the entropy bonus $\mathcal{H}$ that encourages exploration.

## Example

A trading signal agent runs $N = 8$ parallel simulated markets (e.g. eight synthetic GBM paths with different drift and volatility regimes). Each worker steps forward one day, records $(s_t, a_t, r_t, s_{t+1})$, and pauses. The coordinator collects all 8 transitions, computes advantage estimates using a shared critic $V_\phi$, updates both the actor $\pi_\theta$ and critic $V_\phi$ with one gradient step, then broadcasts the updated weights to all workers.

| Workers $N$ | Steps to convergence | Wall-clock time |
|-------------|---------------------|-----------------|
| 1 | 50,000 | 120 s |
| 4 | 28,000 | 38 s |
| 8 | 22,000 | 24 s |

More workers reduce wall-clock time by decorrelating experience across market regimes.

## Remember

A2C sits between two extremes in the RL algorithm family: A3C (asynchronous workers, faster but non-reproducible due to stale gradients) and PPO (clips the policy update ratio for greater stability). In quantitative finance, synchronous collection is valuable because **reproducibility matters**: a quant must be able to confirm that the same training run produces the same strategy, which is impossible with A3C's race conditions. A2C is less sample-efficient than PPO but simpler to implement and debug — in practice, PPO with GAE has superseded A2C for most financial RL applications, but A2C remains the cleanest illustration of how parallel simulation accelerates training for market environments where episodes are cheap to generate.

