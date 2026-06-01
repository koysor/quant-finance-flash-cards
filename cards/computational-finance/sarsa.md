# SARSA

**Topic:** Computational Finance
**Tags:** reinforcement learning, on-policy, temporal difference, q-value, risk-averse, algorithmic trading
**Created:** 2026-06-01
**Author:** Claude Sonnet 4.6

---

## Definition

**SARSA** (State-Action-Reward-State-Action) is an **on-policy** temporal-difference control algorithm that updates Q-values using the actual next action taken by the agent — including exploratory moves — rather than the hypothetical best action, making it safer in environments where exploration is costly.

## Key Formula

The SARSA update uses the quintuple $(s_t, a_t, R_{t+1}, s_{t+1}, a_{t+1})$ sampled under the current policy:

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha\!\left[R_{t+1} + \gamma\, Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t)\right]$$

The difference from Q-learning is the TD target: SARSA uses $Q(s_{t+1}, a_{t+1})$ — the value of the action the agent *will actually take* — rather than $\max_{a'} Q(s_{t+1}, a')$. Under an ε-greedy policy, $a_{t+1}$ is occasionally a random exploratory action, so SARSA's Q-values incorporate the expected cost of exploration.

## Example

A hedging algorithm uses ε-greedy with $\varepsilon = 0.1$. State: current delta exposure. Actions: hedge (rebalance) or hold. A "hedge" action in a high-delta state may occasionally be replaced by a random exploratory "hold" during training. Q-learning ignores this and targets the greedy value; SARSA penalises the high-delta "hedge" state because it accounts for the 10\% chance of accidentally holding (incurring extra risk). The SARSA policy avoids building up large delta positions even during training, producing safer hedging behaviour.

## Remember

The on-policy vs off-policy distinction has a direct analogue in finance: Q-learning is the aggressive trader who learns the best strategy in theory, while SARSA is the risk-manager who accounts for the strategy actually executed in practice. In a live trading context where exploration means placing real orders in the market, SARSA learns to avoid states where occasional exploratory actions cause large losses — it builds a "cushion" against its own imperfect behaviour. This is why SARSA (and its continuous variant, Expected SARSA) is preferred for hedging and market-making applications where the downside of a bad exploratory trade is asymmetric.
