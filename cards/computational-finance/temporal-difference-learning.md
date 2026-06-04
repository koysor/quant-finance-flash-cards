# Temporal Difference Learning

**Topic:** Computational Finance
**Tags:** temporal difference, td learning, reinforcement learning, bootstrapping, td error
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Temporal difference (TD) learning** is a model-free reinforcement learning method that updates value estimates by bootstrapping — using the current estimate of the next state's value rather than waiting for the actual episode return. It combines the sample efficiency of Monte Carlo methods (no model needed) with the online learning of dynamic programming (updates after each step, not each episode).

## Key Formula

The **TD(0) update** for the state-value function after observing transition $(s_t, r_{t+1}, s_{t+1})$:

$$V(s_t) \leftarrow V(s_t) + \alpha\,\delta_t$$

where $\alpha \in (0,1]$ is the learning rate and $\delta_t$ is the **TD error**:

$$\delta_t = r_{t+1} + \gamma\, V(s_{t+1}) - V(s_t)$$

The TD error measures the difference between the updated estimate ($r_{t+1} + \gamma V(s_{t+1})$) and the current estimate ($V(s_t)$). The update shrinks this discrepancy at each step.

For action values, **SARSA** (on-policy) updates $Q(s_t, a_t)$ using the next action $a_{t+1}$ chosen by the policy; **Q-learning** (off-policy) uses $\max_{a'} Q(s_{t+1}, a')$ regardless of the action actually taken.

## Example

A portfolio rebalancing agent estimates $V(s)$ where $s$ = (current weights, factor scores). After one step: current weights = [60% equity, 40% bond], reward $r_{t+1} = +0.12\%$ (monthly Sharpe increment), next state value $V(s_{t+1}) = 2.85$, $V(s_t) = 2.70$, $\gamma = 0.95$, $\alpha = 0.1$:

$$\delta_t = 0.0012 + 0.95 \times 2.85 - 2.70 = 0.0012 + 2.7075 - 2.70 = 0.0087$$

$$V(s_t) \leftarrow 2.70 + 0.1 \times 0.0087 = 2.7009$$

The value estimate increases slightly — the outcome was marginally better than expected.

## Remember

TD learning is why Q-learning and SARSA can train in real time, one trade at a time, without waiting for a full trading session to end. The TD error $\delta_t$ is the workhorse signal: positive $\delta_t$ means outcomes were better than expected (reinforce the action); negative $\delta_t$ means they were worse (suppress it). Neuroscience research has found that dopamine neurons in the brain fire in proportion to $\delta_t$ — the same signal evolution found optimal for sequential reward learning. In finance, TD learning underpins online calibration of execution models, where the agent continuously updates its cost estimates as new market data arrives without retraining from scratch.
