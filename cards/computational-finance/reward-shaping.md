# Reward Shaping

**Topic:** Computational Finance
**Tags:** reinforcement learning, reward function, potential-based shaping, risk-adjusted return, sharpe ratio, training
**Created:** 2026-06-01
**Author:** Claude Sonnet 4.6

---

## Definition

**Reward shaping** is the technique of augmenting the environment's sparse or delayed reward signal $R(s, a, s')$ with an auxiliary shaping term $F(s, a, s')$ to accelerate learning, where **potential-based shaping** $F = \gamma\Phi(s') - \Phi(s)$ guarantees the optimal policy is unchanged.

## Key Formula

The shaped reward is:

$$R'(s, a, s') = R(s, a, s') + F(s, a, s')$$

For **potential-based** shaping (Ng, Harada, Russell 1999), $F$ takes the form:

$$F(s, a, s') = \gamma\,\Phi(s') - \Phi(s)$$

where $\Phi: S \to \mathbb{R}$ is any real-valued **potential function** over states. The telescoping property means the shaped and original problems have identical optimal policies: the extra terms cancel across any complete trajectory.

A common finance-specific shaping term adds a per-step risk penalty:

$$R'_t = \underbrace{\Delta\text{P\&L}_t}_{\text{environment reward}} - \underbrace{\lambda\,\lvert\Delta w_t\rvert}_{\text{transaction cost}} - \underbrace{\mu\,\sigma_t^2}_{\text{variance penalty}}$$

## Example

An RL hedger receives only a sparse terminal reward (total hedging error over 30 days). Without shaping, the agent explores blindly for thousands of episodes before the reward signal improves. By adding $F_t = -0.01 \cdot \lvert\Delta_t\rvert^2$ (penalise large instantaneous delta imbalance), the agent receives immediate feedback on each step's hedging quality, reducing training time by 10×. The potential function $\Phi(s) = -\lvert\Delta_t\rvert^2 / 0.01$ confirms this is a valid potential-based shape and the optimal terminal hedging policy is unchanged.

## Remember

The reward function is the most consequential design decision in any finance RL problem — it encodes what the agent is actually optimising. Using raw P&L as the reward produces an agent that maximises expected wealth but ignores volatility, drawdown, and transaction costs. Shaping the reward to include a Sharpe-like term ($R' = \Delta P - \lambda\sigma$) produces a risk-adjusted trader; adding a drawdown penalty produces a capital-preservation-focused agent. The practical danger is **reward hacking**: an agent may find unexpected ways to maximise the shaped reward that technically satisfy the formula but violate the intent — a common failure mode in financial RL where the agent learns to exploit backtest data artefacts rather than real market structure.
