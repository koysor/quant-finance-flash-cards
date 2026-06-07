# Double Q-Learning

**Topic:** Computational Finance
**Tags:** double q-learning, overestimation bias, double dqn, value estimation, reinforcement learning
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Double Q-Learning** decouples the two roles combined in standard Q-learning — selecting the best action and evaluating its value — by using two independent Q-networks for each task. Standard Q-learning uses $\max_{a'} Q(s', a')$ for both selection and evaluation, which causes systematic upward bias because the maximum of noisy estimates is always larger than the true maximum. Double Q-learning selects the action using one network but evaluates it using a second, independent network, eliminating the overestimation bias.

## Key Formula

**Standard Q-learning target** (biased — same network selects and evaluates):

$$y = r + \gamma\, Q_\theta\!\left(s',\; \arg\max_{a'} Q_\theta(s', a')\right)$$

**Double Q-learning target** (unbiased — network $A$ selects, network $B$ evaluates):

$$y^{\text{double}} = r + \gamma\, Q_{\theta_B}\!\left(s',\; \arg\max_{a'} Q_{\theta_A}(s', a')\right)$$

**Overestimation bias** in standard Q-learning: for $n$ actions with i.i.d. noise $\epsilon_a \sim N(0, \sigma^2)$ added to true Q-values $q_a$:

$$\mathbb{E}\!\left[\max_a (q_a + \epsilon_a)\right] \geq \max_a q_a$$

with equality only when $\sigma = 0$ (no noise). The bias grows with $n$ (more actions) and $\sigma^2$ (more estimation noise).

**Double DQN** (practical implementation): use the online network $\theta$ for selection and the frozen target network $\theta^-$ for evaluation:

$$y^{\text{DDQN}} = r + \gamma\, Q_{\theta^-}\!\left(s',\; \arg\max_{a'} Q_\theta(s', a')\right)$$

## Example

**American put pricing with 3 actions** — $\{$hold, exercise, delta-hedge$\}$. State: $(S_t/K, \tau)$. True optimal Q-values at $(S = 95, \tau = 0.5)$: $Q^*(\text{hold}) = 5.80$, $Q^*(\text{exercise}) = 5.00$, $Q^*(\text{hedge}) = 5.40$.

With estimation noise $\sigma = 0.5$ after 10,000 training steps:

| Method | Estimated $\max_a Q$ | Bias | Implied option price |
|---|---|---|---|
| True Q-values | 5.80 | 0 | 5.80 |
| Standard Q-learning | 6.42 | +0.62 | 6.42 (overpriced) |
| Double Q-learning | 5.84 | +0.04 | 5.84 (accurate) |

Overestimated continuation values make the agent less likely to exercise — the option appears worth more to hold than it truly is, causing under-exercise and systematic mispricing.

## Remember

Overestimation bias in Q-learning has a direct financial consequence: **the agent thinks holding is always better than it really is**. For an American option pricer, this means the RL agent will under-exercise: it delays exercise even when the intrinsic value exceeds the continuation value, because the continuation Q-value is inflated by the max-bias. The resulting price is systematically too high — the agent overestimates the value of flexibility. Double Q-learning fixes this by separating the "which action is best?" question from "how good is that action?" — analogous to the Chinese Wall between research analysts recommending stocks and trading desks pricing those same positions. In practice, Double DQN costs essentially nothing (the target network is already maintained in DQN) and consistently reduces overestimation by 30–60% across financial RL applications, making it the default choice over vanilla DQN for any option pricing or execution agent.
