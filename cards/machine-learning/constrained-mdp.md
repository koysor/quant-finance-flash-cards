# Constrained MDP

**Topic:** Machine Learning
**Tags:** constrained mdp, lagrangian, risk constraint, drawdown, safe reinforcement learning, portfolio optimisation
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **constrained MDP (CMDP)** is an MDP where the agent must satisfy one or more constraints on expected cumulative costs in addition to maximising the primary reward. Constraints capture regulatory limits, risk mandates, or capital requirements that a pure reward-maximising agent would ignore. The standard solution method converts the CMDP into an unconstrained problem via the **Lagrangian relaxation**, where constraint violations are penalised by a multiplier $\lambda$ that is adjusted until the constraint binds exactly.

## Key Formula

The CMDP problem: maximise expected return subject to a constraint on expected cost:

$$\max_\pi \; \mathbb{E}_\pi\!\left[\sum_{t=0}^T \gamma^t R(s_t, a_t)\right] \quad \text{subject to} \quad \mathbb{E}_\pi\!\left[\sum_{t=0}^T \gamma^t C(s_t, a_t)\right] \leq d$$

**Lagrangian relaxation** — convert to unconstrained problem with penalty $\lambda \geq 0$:

$$\mathcal{L}(\pi, \lambda) = \mathbb{E}_\pi\!\left[\sum_t \gamma^t R(s_t, a_t)\right] - \lambda\left(\mathbb{E}_\pi\!\left[\sum_t \gamma^t C(s_t, a_t)\right] - d\right)$$

**Primal-dual update** (alternating optimisation):
$$\pi_{k+1} = \arg\max_\pi \mathcal{L}(\pi, \lambda_k)$$
$$\lambda_{k+1} = \max\!\left(0,\; \lambda_k + \eta\!\left(\mathbb{E}_{\pi_{k+1}}\!\left[\sum_t \gamma^t C_t\right] - d\right)\right)$$

At convergence, $\lambda^*$ is the shadow price of the constraint: the reward foregone per unit tightening of the constraint.

## Example

**Drawdown-constrained delta hedging:** Primary reward $R_t = \Delta\text{P\&L}_t$ (hedge quality). Constraint: expected maximum drawdown $\leq 5\%$ of portfolio value.

An unconstrained RL hedging agent learns to occasionally take large unhedged positions for higher expected P&L. The CMDP with $d = 0.05$ adds a cost $C_t = \mathbf{1}[\text{drawdown}_t > 0.05]$.

| Agent | Expected P&L (annual) | Max drawdown (95th pctile) |
|---|---|---|
| Unconstrained RL | 2.1% | 12.3% |
| CMDP ($d = 5\%$) | 1.8% | 4.9% |
| Delta-neutral (baseline) | 1.4% | 2.1% |

The Lagrange multiplier converges to $\lambda^* = 3.2$, meaning the agent sacrifices 3.2 units of expected P&L for each 1% tightening of the drawdown constraint — the shadow price of the risk limit.

## Remember

The constrained MDP is the correct formulation for **any regulated trading strategy**. Real desks operate under multiple constraints simultaneously: VaR limits, drawdown limits, position concentration limits, leverage limits. A plain RL agent trained to maximise Sharpe ratio will violate these constraints whenever doing so increases expected reward — exactly what regulators and risk managers prohibit. The CMDP framework encodes these constraints structurally rather than hoping the reward function captures them. The Lagrange multiplier $\lambda^*$ has a direct financial interpretation: it is the **risk premium** the desk is willing to pay for relaxing the constraint by one unit — equivalent to the price a risk manager should charge for granting a limit increase. In practice, constrained RL is implemented via the **Primal-Dual Proximal Policy Optimisation (PDPPO)** algorithm, which updates the policy to maximise the Lagrangian while the multiplier gradient ascends on the constraint violation.
