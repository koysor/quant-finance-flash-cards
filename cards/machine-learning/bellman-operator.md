# Bellman Operator

**Topic:** Machine Learning
**Tags:** bellman operator, contraction mapping, fixed point, dynamic programming, value iteration
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **Bellman operator** $\mathcal{T}$ is a mapping on value functions that performs one step of the Bellman update. The **optimality operator** $\mathcal{T}^*$ maps any value function $V$ to a new function $(\mathcal{T}^* V)(s)$ equal to the best achievable one-step return plus the discounted value of the next state. The key theoretical result is that $\mathcal{T}^*$ is a **contraction mapping** with factor $\gamma$, guaranteeing that repeated application converges to the unique optimal value function $V^*$.

## Key Formula

The **Bellman optimality operator** $\mathcal{T}^*$ acts on a value function $V: S \to \mathbb{R}$:

$$(\mathcal{T}^* V)(s) = \max_a \mathbb{E}\!\left[r(s, a) + \gamma\, V(s')\right]$$

$V^*$ is the unique **fixed point**: $\mathcal{T}^* V^* = V^*$.

By the **Banach fixed-point theorem**, since $\|\mathcal{T}^* V - \mathcal{T}^* U\|_\infty \leq \gamma \|V - U\|_\infty$ (i.e. $\mathcal{T}^*$ is a $\gamma$-contraction in the sup-norm), iterating from any starting $V_0$ converges:

$$V_{k+1} = \mathcal{T}^* V_k \;\longrightarrow\; V^* \quad \text{at rate } \gamma^k$$

**Value iteration** is exactly this: apply $\mathcal{T}^*$ repeatedly until $\|V_{k+1} - V_k\|_\infty < \varepsilon$.

## Example

A bond portfolio manager initialises $V_0(s) = 0$ for all states. After one application:

$$V_1(s) = (\mathcal{T}^* V_0)(s) = \max_a \mathbb{E}[r(s,a) + \gamma \cdot 0] = \max_a r(s,a)$$

$V_1$ is just the best one-step reward. After two applications, $V_2$ incorporates two-step lookahead. With $\gamma = 0.95$, the error after $k$ iterations is bounded by $0.95^k \|V_0 - V^*\|_\infty$ — the contraction guarantees convergence regardless of the initial guess.

## Remember

The Bellman operator is why value iteration is guaranteed to work — and why Q-learning converges. The contraction property with factor $\gamma < 1$ is the mathematical certificate that iterating Bellman updates never diverges. In practice, **deep Q-networks (DQN)** approximate the Bellman operator with a neural network, but the contraction guarantee breaks when using function approximation — this is the **deadly triad** (function approximation + bootstrapping + off-policy learning) that makes deep RL unstable. DQN's target network trick (holding a frozen copy of the network for $\gamma V(s')$) partially restores the contraction property by decoupling the target from the current estimate.
