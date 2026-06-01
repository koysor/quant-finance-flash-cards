# Policy Gradient Methods

**Topic:** Computational Finance
**Tags:** reinforcement learning, reinforce, actor-critic, policy optimisation, continuous action, hedging
**Created:** 2026-06-01
**Author:** Claude Sonnet 4.6

---

## Definition

**Policy gradient methods** are a family of reinforcement learning algorithms that directly optimise the parameters $\boldsymbol{\theta}$ of a stochastic policy $\pi_{\boldsymbol{\theta}}(a \mid s)$ by following the gradient of the expected cumulative reward, without first learning a value function — making them naturally suited to problems with continuous action spaces.

## Key Formula

The **Policy Gradient Theorem** gives the gradient of the expected return $J(\boldsymbol{\theta}) = \mathbb{E}_{\pi_\theta}[G_0]$ with respect to the policy parameters:

$$\nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}) = \mathbb{E}_{\pi_\theta}\!\left[\nabla_{\boldsymbol{\theta}} \log \pi_{\boldsymbol{\theta}}(a \mid s) \cdot Q^{\pi}(s, a)\right]$$

The **REINFORCE** update uses Monte Carlo returns $G_t$ as an unbiased estimate of $Q^\pi(s_t, a_t)$:

$$\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} + \alpha\, G_t\, \nabla_{\boldsymbol{\theta}} \log \pi_{\boldsymbol{\theta}}(a_t \mid s_t)$$

The term $\nabla_{\boldsymbol{\theta}} \log \pi_{\boldsymbol{\theta}}(a \mid s)$ is called the **score function** — it points toward making action $a$ more likely in state $s$, scaled by how good $a$ turned out to be.

## Example

An options hedger parameterises its hedge ratio as a Gaussian policy: $\pi_\theta(\Delta \mid s) = \mathcal{N}(\mu_\theta(s),\, \sigma^2)$ where $\mu_\theta$ is a neural network mapping market state to a mean hedge ratio. After an episode where hedging with $\Delta = 0.6$ produced a P&L of $+\$200$, the REINFORCE update increases $\theta$ to make $\Delta \approx 0.6$ more likely in that state. After an episode where $\Delta = 0.6$ produced $-\$300$, it decreases the probability. Over thousands of episodes, the policy converges to the optimal hedge ratio for each market state.

## Remember

Q-learning and SARSA require a discrete action space — they choose from a finite set of actions (buy/hold/sell) by looking up Q-values in a table. Policy gradient methods bypass this limitation by parameterising the policy directly as a continuous function: the hedge ratio, position size, or bid-ask spread can be any real number in a range, and the neural network learns to output the optimal value rather than choosing from a discrete menu. This is why policy gradient methods (especially actor-critic algorithms like PPO and DDPG) dominate research in continuous-control finance problems: dynamic hedging, optimal execution with continuous order sizes, and portfolio allocation with fractional weights.
