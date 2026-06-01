# Policy Evaluation vs Control

**Topic:** Computational Finance
**Tags:** reinforcement learning, policy evaluation, control problem, prediction, optimality
**Author:** Gemini CLI

---

## Definition

Reinforcement Learning is typically composed of two distinct but related problems:

1. **Policy Evaluation (Prediction):** Estimating the value function $V_\pi$ for a *given* policy $\pi$. We want to know how much reward we expect to get if we follow a specific fixed strategy.
2. **Control Problem:** Finding the *optimal* policy $\pi^*$ that maximises the expected return. This involves improving the policy based on our evaluations.

## Key Formula

**Policy Evaluation** (Fixed $\pi$):
$$V_\pi(s) = \sum_{a} \pi(a|s) \sum_{s', r} P(s', r | s, a) [r + \gamma V_\pi(s')]$$

**Control Problem** (Optimising $\pi$):
$$\pi^* = \arg\max_\pi V_\pi(s), \quad \forall s \in S$$

## Example

- **Policy Evaluation:** Backtesting a fixed 50/200-day moving average crossover strategy. We aren't changing the strategy; we just want to accurately estimate its expected Sharpe ratio or P&L.
- **Control Problem:** Using a neural network to *learn* when to buy or sell to maximise total return. The agent explores different crossover periods and signal combinations to find the best possible strategy.

## Remember (Finance application)

In quantitative finance, many tasks are pure **Policy Evaluation** (e.g., risk management, where we evaluate the Value-at-Risk of an existing portfolio). However, the ultimate goal of Alpha-seeking strategies is the **Control Problem**: discovering the optimal way to allocate capital and execute trades to outperform the market.
