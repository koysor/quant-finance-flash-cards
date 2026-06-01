# State and Action Value Functions

**Topic:** Computational Finance
**Tags:** reinforcement learning, value function, q-value, state-value, q-learning
**Author:** Gemini CLI

---

## Definition

In Reinforcement Learning, we use two primary types of value functions to represent how "good" a situation or a move is:

1. **State-Value Function $V(s)$:** The expected total reward an agent will receive starting from state $s$ and following a given policy. It evaluates the "desirability" of being in a certain state.
2. **Action-Value Function $Q(s, a)$:** The expected total reward an agent will receive starting from state $s$, taking action $a$, and then following the policy thereafter. It evaluates the "desirability" of a specific move in a specific state.

## Key Formula

The relationship between $V(s)$ and $Q(s, a)$ for a policy $\pi$ is:

$$V_\pi(s) = \sum_{a \in A} \pi(a|s) Q_\pi(s, a)$$

For the optimal policy $\pi^*$, the value of a state is the value of the best possible action in that state:

$$V^*(s) = \max_{a \in A} Q^*(s, a)$$

## Example

- **$V(s)$:** The expected total P&L of holding a specific portfolio given the current market volatility and interest rates.
- **$Q(s, a)$:** The expected total P&L of *selling* 100 shares right now ($a$), given the current market state ($s$), and continuing to trade optimally afterwards.

## Remember (Finance application)

$Q$-values are the basis for **Q-learning**, one of the most popular RL algorithms. In finance, $Q$-values allow us to compare the long-term impact of different immediate trading decisions (e.g., "Market Order" vs "Limit Order") by accounting for both the immediate price and the future opportunity set.
