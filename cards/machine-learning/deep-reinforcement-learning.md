# Deep Reinforcement Learning

**Topic:** Machine Learning
**Tags:** deep reinforcement learning, dqn, neural network, q-learning, function approximation, algorithmic trading
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Deep Reinforcement Learning (Deep RL)** combines reinforcement learning's trial-and-error optimisation with deep neural networks as function approximators. Instead of a tabular lookup for every state, a neural network with parameters $\theta$ estimates the value function $Q(s,a;\theta) \approx Q^*(s,a)$ across the entire continuous state space. The **Deep Q-Network (DQN)** is the canonical deep RL algorithm: it applies Q-learning updates but with two stabilising components — a **replay buffer** and a **target network** — that make neural network training converge reliably.

## Key Formula

DQN trains $\theta$ by minimising the **Bellman residual loss**:

$$\mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}}\!\left[\Bigl(y - Q(s, a;\,\theta)\Bigr)^2\right]$$

where the **TD target** uses a frozen copy of the network parameters $\theta^-$ (the target network):

$$y = r + \gamma \max_{a'} Q(s',\, a';\,\theta^-)$$

Gradient descent on $\mathcal{L}(\theta)$ updates the online network $\theta$; the target network $\theta^-$ is synchronised to $\theta$ every $C$ steps to prevent the moving-target instability that causes tabular updates to diverge when parameterised.

## Example

An options pricing agent has state $s = (S_t,\, K,\, \tau,\, \sigma_{\text{impl}})$ and actions $a \in \{$price low, price mid, price high$\}$. The replay buffer $\mathcal{D}$ stores 100,000 past $(s, a, r, s')$ tuples. At each training step:

1. Sample a mini-batch of 64 tuples from $\mathcal{D}$.
2. Compute targets: $y_i = r_i + 0.99 \cdot \max_{a'} Q(s_i', a'; \theta^-)$.
3. Update: $\theta \leftarrow \theta - \alpha \nabla_\theta \mathcal{L}(\theta)$ via Adam.
4. Every $C = 1{,}000$ steps, copy $\theta \to \theta^-$.

After training, $\arg\max_a Q(s, a; \theta)$ gives the pricing action for any market state.

## Remember

Deep RL is the architecture behind most neural-network-based trading and pricing agents in academic finance research. Where tabular Q-learning requires a separate entry for every $(s, a)$ pair — impossible when state includes continuous prices, volatilities, and time-to-maturity — DQN generalises across similar states automatically. The replay buffer prevents the network from overfitting to the most recent market regime (non-stationarity), and the target network stops the Bellman targets from shifting every gradient step. In practice, DQN and its extensions (Double DQN, Duelling DQN) are the starting point for RL-based execution, options pricing, and market-making agents before more advanced policy-gradient methods are applied.
