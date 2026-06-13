# Advantage Function

**Topic:** Machine Learning
**Tags:** advantage function, actor-critic, ppo, value function, variance reduction, reinforcement learning
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **advantage function** $A^\pi(s, a)$ measures how much better action $a$ is compared to the average action taken by policy $\pi$ from state $s$. It decomposes the action-value function into a baseline (the state value) and a relative action quality, dramatically reducing gradient variance in policy gradient and actor-critic algorithms.

## Key Formula

$$A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)$$

where $Q^\pi(s,a)$ is the expected return from taking action $a$ in state $s$ and following $\pi$ thereafter, and $V^\pi(s) = \mathbb{E}_{a \sim \pi}[Q^\pi(s,a)]$ is the baseline. By construction $\mathbb{E}_{a \sim \pi}[A^\pi(s,a)] = 0$.

In practice, the **Generalised Advantage Estimate (GAE)** is used, combining multi-step TD errors $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$:

$$\hat{A}_t^{\text{GAE}(\gamma, \lambda)} = \sum_{k=0}^{\infty} (\gamma\lambda)^k\,\delta_{t+k}$$

This is the $\hat{A}_t$ term inside PPO's clipped objective.

## Example

An RL hedging agent reaches state $s_t$: ATM call with 5 days to expiry, current delta = 0.52. The state value $V(s_t) = -£0.15$ (average hedging P&L from this state under current policy). Two candidate actions:
- Rebalance to delta = 0.55: $Q = -£0.08$, $A = +£0.07$ (better than average)
- Hold delta = 0.52: $Q = -£0.22$, $A = -£0.07$ (worse than average)

The policy gradient update reinforces the rebalance action and discourages holding, using the advantage signal rather than the raw Q value — the baseline $V(s_t)$ cancels out common noise across actions.

## Remember

Using raw returns as the policy gradient signal is like a trader evaluating each trade on its absolute P&L rather than asking "was this better than my alternative?" — good days produce uniformly positive gradients that fail to distinguish lucky actions from skilled ones. The advantage function isolates the **relative quality** of each action, making gradient estimates far more informative per sample. For option hedging, this means the agent learns to distinguish hedging decisions that outperformed the baseline policy from those that merely benefited from favourable market moves that any action would have captured.
