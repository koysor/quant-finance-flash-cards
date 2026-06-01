# Bellman Equation

**Topic:** Computational Finance
**Tags:** reinforcement learning, bellman equation, dynamic programming, value function
**Author:** Gemini CLI

---

## Definition

The **Bellman Equation** is a recursive relationship that decomposes the value of a state (or state-action pair) into the immediate reward plus the discounted value of the subsequent state. It is the fundamental equation for solving Reinforcement Learning problems using dynamic programming.

The equation expresses that the value of being in a state is the expected reward of the next step plus the value of where you end up, discounted by $\gamma$.

## Key Formula

For a given policy $\pi$, the **Value Function** $V_\pi(s)$ satisfies:

$$V_\pi(s) = \mathbb{E}_\pi [R_{t+1} + \gamma V_\pi(s_{t+1}) | s_t = s]$$

The **Bellman Optimality Equation** for the optimal value function $V^*(s)$ is:

$$V^*(s) = \max_a \mathbb{E} [R_{t+1} + \gamma V^*(s_{t+1}) | s_t = s, a_t = a]$$

## Example

In a portfolio optimisation problem, the Bellman equation allows us to break down the complex problem of "maximising total wealth over 30 years" into a series of smaller, identical problems: "What is the best action *now*, given that I will also act optimally in all future steps?"

## Remember (Finance application)

The Bellman equation is the "Law of Iterated Expectations" applied to optimal control. In derivative pricing, it is analogous to the risk-neutral pricing formula $V_t = e^{-r \Delta t} \mathbb{E}^\mathbb{Q}[V_{t+1} | \mathcal{F}_t]$, where the current price is the discounted expected future price. In RL, we use it to iteratively improve our estimates of asset values or trading policy performance.
