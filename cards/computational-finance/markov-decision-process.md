# Markov Decision Process (MDP)

**Topic:** Computational Finance
**Tags:** reinforcement learning, mdp, stochastic control, states, actions
**Author:** Gemini CLI

---

## Definition

A **Markov Decision Process (MDP)** is a mathematical framework used to model decision-making in environments where outcomes are partially random and partially under the control of an agent. It provides the formal foundation for Reinforcement Learning.

An MDP is defined by a 5-tuple $(S, A, P, R, \gamma)$:
- **States ($S$):** A set of all possible situations the agent can be in.
- **Actions ($A$):** A set of all possible moves the agent can make.
- **Transitions ($P$):** The probability $P(s' | s, a)$ of moving to state $s'$ from state $s$ after taking action $a$.
- **Rewards ($R$):** The immediate reward $R(s, a)$ received after taking action $a$ in state $s$.
- **Discount Factor ($\gamma$):** A value $\gamma \in [0, 1]$ that represents the preference for immediate rewards over future rewards.

## Key Formula

The **Markov Property** states that the future depends only on the current state and action, not on the sequence of events that preceded it:

$$\mathbb{P}(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, \dots) = \mathbb{P}(s_{t+1} | s_t, a_t)$$

## Example

Consider an automated execution algorithm (the agent). The **state** could be the current inventory and the limit order book depth. The **actions** are the sizes and prices of orders to place. The **reward** is the implementation shortfall (difference between execution price and arrival price). The **transitions** are governed by market dynamics and other participants' reactions.

## Remember (Finance application)

MDPs are the core "physics" of reinforcement learning in finance. By framing a trading problem as an MDP, we can use algorithms like Q-learning to find optimal strategies that account for market impact and transaction costs over time, rather than just optimising for the next second.
