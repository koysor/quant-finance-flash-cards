# Actor-Critic Method

**Topic:** Machine Learning
**Tags:** actor-critic, reinforcement learning, policy gradient, value function, advantage
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

An **actor-critic** method is a reinforcement learning architecture that maintains two components simultaneously: an **actor** (a parameterised policy $\pi_\theta(a \mid s)$) and a **critic** (a parameterised value function $V_\phi(s)$ or $Q_\phi(s,a)$). The critic evaluates the actor's actions by estimating the value function; the actor updates its policy using the critic's feedback rather than raw returns. This reduces the high variance of pure policy gradient methods while avoiding the inflexibility of pure value-based methods.

## Key Formula

The actor is updated using the **advantage function** $A(s, a)$, which measures how much better action $a$ is than the average action in state $s$:

$$A(s_t, a_t) = Q(s_t, a_t) - V(s_t) \approx r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)$$

The right-hand side is the **TD error** $\delta_t$, which serves as a low-variance estimator of the advantage. The actor gradient becomes:

$$\nabla_\theta J(\theta) \approx \mathbb{E}\!\left[\nabla_\theta \log \pi_\theta(a_t \mid s_t) \cdot \delta_t\right]$$

The critic minimises the TD error by updating $\phi$ to minimise $\delta_t^2$.

## Example

A delta-hedging agent uses an actor-critic to hedge a short call option. State: $(S_t, \sigma_{\text{impl}}, \tau, \Delta_{\text{current}})$. Action: change in hedge ratio $\Delta h$.

- **Critic** estimates $V_\phi(s_t)$ = expected future hedging P&L from this state
- **TD error**: $\delta_t = r_t + 0.99\,V_\phi(s_{t+1}) - V_\phi(s_t)$, where $r_t = -(\text{hedge P&L error})^2 - \text{transaction cost}$
- **Actor** shifts the hedge ratio towards actions that produced positive TD errors (better-than-expected outcomes)

After training, the actor learns a data-driven hedging rule that accounts for transaction costs — unlike the Black-Scholes delta, which ignores them.

## Remember

Actor-critic is the architecture behind the most powerful RL algorithms used in quantitative finance: **PPO** (Proximal Policy Optimisation) and **DDPG** (Deep Deterministic Policy Gradient) are both actor-critic variants. PPO is used in portfolio optimisation research; DDPG handles continuous action spaces such as order sizes and hedge ratios. The key advantage over pure REINFORCE (policy gradient) is variance reduction via the critic — in finance, where reward signals are noisy and episodes are short, this matters enormously. The actor-critic split also mirrors the intuition of a trading desk: the actor is the strategy, the critic is the risk manager evaluating expected P&L.
