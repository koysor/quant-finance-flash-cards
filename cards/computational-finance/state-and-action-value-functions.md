# State and Action Value Functions

**Topic:** Computational Finance
**Tags:** value function, q-value, state value, reinforcement learning, bellman equation
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

In reinforcement learning, the **state-value function** $V^\pi(s)$ measures the expected discounted return when starting from state $s$ and following policy $\pi$ thereafter. The **action-value function** $Q^\pi(s,a)$ measures the expected return after taking action $a$ in state $s$ and then following $\pi$. Together, they quantify how good it is to be in a given situation and how good each available action is from that situation.

## Key Formula

$$V^\pi(s) = \mathbb{E}_\pi\!\left[\sum_{k=0}^{\infty} \gamma^k r_{t+k} \;\Big|\; s_t = s\right]$$

$$Q^\pi(s, a) = \mathbb{E}_\pi\!\left[\sum_{k=0}^{\infty} \gamma^k r_{t+k} \;\Big|\; s_t = s,\, a_t = a\right]$$

The two functions are linked by:

$$V^\pi(s) = \sum_a \pi(a \mid s)\, Q^\pi(s, a)$$

The **advantage function** $A^\pi(s,a) = Q^\pi(s,a) - V^\pi(s)$ measures how much better action $a$ is than the average — the quantity used by actor-critic algorithms to update the policy.

## Example

A delta-hedging agent operates with state $s = (\Delta_{\text{current}}, S_t, \sigma_{\text{impl}}, \tau)$. Suppose two actions are available: hedge (adjust $\Delta$ to Black-Scholes delta) or do nothing. After training:

- $Q^\pi(s, \text{hedge}) = -\$230$ (expected hedging P&L net of transaction costs)
- $Q^\pi(s, \text{do nothing}) = -\$580$ (expected loss from growing hedge error)
- $V^\pi(s) = -\$230$ (agent follows the better action on average)
- $A^\pi(s, \text{hedge}) = 0$, $A^\pi(s, \text{do nothing}) = -\$350$

The negative advantage of "do nothing" drives the actor to suppress that action.

## Remember

Value functions are the quantities that RL algorithms estimate in order to make decisions in finance. Q-learning builds a table or neural network approximating $Q^*(s,a)$ — the action to take is simply $\arg\max_a Q^*(s,a)$. In portfolio management, $Q^*(s,a)$ has a direct interpretation: the risk-adjusted P&L the agent expects to earn from state $s$ (e.g. current weights, factor exposures) by taking action $a$ (e.g. rebalancing to a target allocation), accounting for all future transaction costs and market dynamics. The advantage function $A$ is central to actor-critic methods like PPO and DDPG, which are the RL architectures most widely used in quantitative finance research.
