# Proximal Policy Optimisation (PPO)

**Topic:** Computational Finance
**Tags:** ppo, policy gradient, clipping, continuous action, deep reinforcement learning, hedging
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Proximal Policy Optimisation (PPO)** is a policy gradient algorithm that prevents destructively large policy updates by clipping the objective function whenever the new policy deviates too far from the old one. It achieves near-TRPO performance with a simpler implementation — no second-order optimisation or Lagrangian constraint — making it the de-facto standard for continuous-action RL problems such as dynamic option hedging.

## Key Formula

PPO maximises the **clipped surrogate objective**:

$$\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[\min\!\left(r_t(\theta)\,\hat{A}_t,\;\operatorname{clip}(r_t(\theta),\,1-\epsilon,\,1+\epsilon)\,\hat{A}_t\right)\right]$$

where the **probability ratio** $r_t(\theta) = \dfrac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_\text{old}}(a_t \mid s_t)}$ measures how much the policy has changed, $\hat{A}_t$ is the estimated advantage, and $\epsilon \approx 0.2$ is the clip threshold. The $\min$ operator means: take the unclipped objective when the policy moves in the right direction, but cap the gain when the ratio strays outside $[1-\epsilon, 1+\epsilon]$.

## Example

A PPO agent learns to hedge a short straddle by outputting a continuous hedge ratio $\delta_t \in [-2, 2]$ at each of 30 daily steps. Reward: daily hedged P&L minus proportional transaction costs. Without clipping (vanilla policy gradient), large gradient steps occasionally flip the hedge from long to short in a single update, destabilising training. With PPO ($\epsilon = 0.2$): updates are bounded, training converges in 800 episodes to a Sharpe ratio of 1.4, versus 600 episodes of divergence then reset without clipping.

## Remember

PPO's clipping solves the **step-size problem** that makes vanilla policy gradient unreliable for financial RL: in derivatives hedging, a single over-sized policy update can produce a hedge ratio that oscillates between ±100% delta, making the portfolio impossible to trade. The clip threshold $\epsilon$ is a direct regularisation hyperparameter — larger $\epsilon$ allows faster learning but risks instability on volatile market days, while smaller $\epsilon$ is more stable but slower to adapt. PPO dominates REINFORCE for option hedging because the hedge ratio is continuous (not discrete), making the importance sampling ratio $r_t$ well-defined and the clipped objective smooth to optimise.
