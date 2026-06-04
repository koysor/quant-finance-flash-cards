# Markov Decision Process (MDP)

**Topic:** Computational Finance
**Tags:** mdp, reinforcement learning, stochastic control, states, actions, markov property
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **Markov Decision Process (MDP)** is the mathematical framework for sequential decision-making under uncertainty. An agent observes a state, takes an action, receives a reward, and transitions to a new state — with transitions governed by the Markov property: the future depends only on the current state and action, not on any prior history. MDPs are the formal foundation for reinforcement learning.

## Key Formula

An MDP is defined by the 5-tuple $(S, A, P, R, \gamma)$:

| Symbol | Meaning |
|--------|---------|
| $S$ | State space |
| $A$ | Action space |
| $P(s' \mid s, a)$ | Transition probability to state $s'$ from $(s, a)$ |
| $R(s, a)$ | Expected immediate reward for action $a$ in state $s$ |
| $\gamma \in [0,1]$ | Discount factor for future rewards |

The **Markov property**: $P(s_{t+1} \mid s_t, a_t, s_{t-1}, \ldots) = P(s_{t+1} \mid s_t, a_t)$.

The agent's goal is to find a policy $\pi: S \to A$ that maximises the expected discounted return $\mathbb{E}\!\left[\sum_{t=0}^\infty \gamma^t R(s_t, a_t)\right]$.

## Example

An optimal execution agent models its problem as an MDP:
- **State** $s_t$: (remaining inventory $I_t$, time remaining $\tau$, current mid-price $P_t$, bid-ask spread)
- **Action** $a_t$: number of shares to sell in this period
- **Reward** $r_t$: cash received minus market impact cost $= a_t P_t - \eta a_t^2$
- **Transition**: $I_{t+1} = I_t - a_t$; $P_{t+1}$ evolves via GBM
- **Discount**: $\gamma = 0.99$ (slightly penalises delaying sales)

The optimal policy $\pi^*(s_t)$ is the Almgren-Chriss schedule for linear impact — recovered analytically or approximated via Q-learning.

## Remember

Framing a trading problem as an MDP is the first and most important step in applying reinforcement learning to finance. The state design determines what information the agent can use; the reward function determines what the agent optimises. Poor state or reward design produces RL agents that learn to game the reward signal rather than trade well — known as **reward hacking**. In practice, the state must include risk exposures (inventory, Greeks) and market conditions (volatility regime, spread), while the reward must penalise transaction costs and drawdowns, not just raw P&L.
