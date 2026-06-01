# Q-Learning

**Topic:** Computational Finance
**Tags:** reinforcement learning, q-value, off-policy, temporal difference, bellman equation, algorithmic trading
**Created:** 2026-06-01
**Author:** Claude Sonnet 4.6

---

## Definition

**Q-learning** is an off-policy temporal-difference control algorithm that directly learns the optimal action-value function $Q^*(s, a)$ by updating Q-values toward the Bellman optimality target — using the greedy action in the next state regardless of which action the agent actually takes during exploration.

## Key Formula

After taking action $a$ in state $s$, receiving reward $R$, and transitioning to state $s'$, the Q-value is updated as:

$$Q(s, a) \leftarrow Q(s, a) + \alpha\!\left[\underbrace{R + \gamma \max_{a'} Q(s', a')}_{\text{TD target}} - Q(s, a)\right]$$

where $\alpha \in (0,1]$ is the **learning rate** and $\gamma$ is the **discount factor**. The term in brackets is the **TD error** $\delta$. The key property is that the target uses $\max_{a'} Q(s', a')$ — the value of the *best* next action — not the value of the action the agent actually follows (making it off-policy).

## Example

An execution algorithm has state $s = (\text{inventory}, \text{spread})$ and actions $a \in \{\text{passive, aggressive}\}$. After 1,000 steps: $Q(\text{high inventory, wide spread}, \text{aggressive}) = -0.12$ (high cost), $Q(\text{high inventory, wide spread}, \text{passive}) = -0.03$. After observing a passive order fills in 2 seconds with reward $R = +0.05$ and the next state has best Q-value 0.04, the update with $\alpha=0.1, \gamma=0.9$ is: $Q \leftarrow -0.03 + 0.1[0.05 + 0.9(0.04) - (-0.03)] = -0.03 + 0.1(0.116) = -0.0184$.

## Remember

Q-learning is the workhorse algorithm behind modern deep reinforcement learning in finance. Its off-policy property is crucial: during training the agent can explore freely (ε-greedy) without biasing the Q-value estimates toward suboptimal exploratory actions — the target always evaluates the *best* known next action. In optimal execution, the Q-table encodes the long-run cost of every (inventory state, order type) pair after accounting for all future market impact; a quant who has learned this table can place orders that minimise total implementation shortfall over the entire liquidation horizon, not just the next trade.
