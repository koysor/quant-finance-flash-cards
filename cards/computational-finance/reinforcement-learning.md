# Reinforcement Learning

**Topic:** Computational Finance
**Tags:** reinforcement learning, agent, reward, policy, Markov decision process, algorithmic trading
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Reinforcement Learning (RL)** is a machine learning paradigm in which an agent learns an optimal decision policy by interacting with an environment, receiving scalar reward signals, and maximising expected cumulative reward over time — without being given labelled examples of correct actions.

## Key Formula

The agent maximises the expected discounted return:

$$G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$$

where $\gamma \in [0,1)$ is the **discount factor** and $R_{t+k}$ is the reward at step $t+k$. The optimal policy $\pi^*$ satisfies the Bellman optimality equation:

$$Q^*(s,a) = \mathbb{E}\!\left[R + \gamma \max_{a'}Q^*(s',a') \mid s, a\right]$$

## Example

An RL agent trades a single stock. State: current position, price, recent returns. Actions: buy, hold, sell. Reward: realised P&L minus transaction costs. After millions of simulated episodes the agent learns a policy that avoids over-trading and adapts to regime changes.

## Remember

RL is the framework behind modern algorithmic execution and dynamic hedging research. The discount factor $\gamma$ has a direct financial interpretation: it is analogous to a time-preference rate, balancing immediate profit against long-term portfolio health. Q-learning and Deep Q-Networks (DQN) are common implementations.
