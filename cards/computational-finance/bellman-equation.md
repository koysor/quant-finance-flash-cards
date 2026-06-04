# Bellman Equation

**Topic:** Computational Finance
**Tags:** bellman equation, dynamic programming, value function, reinforcement learning, optimality
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **Bellman equation** is a recursive relationship that decomposes the value of being in a state into the immediate reward plus the discounted value of the next state. It is the fundamental equation of dynamic programming and reinforcement learning: any optimal policy must satisfy it, and solving it — exactly or approximately — is the core task of every RL algorithm.

## Key Formula

For a policy $\pi$, the **Bellman expectation equation** for the state-value function is:

$$V^\pi(s) = \mathbb{E}_\pi\!\left[r_{t+1} + \gamma\, V^\pi(s_{t+1}) \mid s_t = s\right]$$

The **Bellman optimality equation** gives the value under the best possible policy:

$$V^*(s) = \max_a \mathbb{E}\!\left[r_{t+1} + \gamma\, V^*(s_{t+1}) \mid s_t = s,\, a_t = a\right]$$

Equivalently for Q-values: $Q^*(s,a) = \mathbb{E}\!\left[r_{t+1} + \gamma \max_{a'} Q^*(s_{t+1}, a')\right]$.

The discount factor $\gamma \in [0,1]$ controls how much future rewards are worth relative to immediate ones.

## Example

An execution agent splits a 10,000-share sell order over $T = 5$ periods. State $s_t$ = remaining inventory; reward $r_t$ = P&L minus market impact cost; $\gamma = 0.99$. The Bellman equation says: the value of holding 6,000 shares with 3 periods left equals the best immediate sale profit now plus 0.99 times the value of the resulting inventory next period. Working backwards from the terminal state ($V^*(0) = 0$, no inventory left) gives the optimal sale schedule at each step.

## Remember

The Bellman equation is the bridge between intuition and algorithm in RL-based trading. It says: **you never need to plan the entire future — just compare the immediate reward to the discounted continuation value**. Q-learning approximates $Q^*$ by iterating the Bellman optimality equation; deep Q-networks (DQN) parameterise $Q^*$ with a neural network and minimise the Bellman residual as a loss function. In options pricing, the same structure appears as risk-neutral pricing: $V_t = e^{-r\Delta t}\mathbb{E}^\mathbb{Q}[V_{t+1} \mid \mathcal{F}_t]$ — discounted expected value forward one step, exactly the Bellman form.
