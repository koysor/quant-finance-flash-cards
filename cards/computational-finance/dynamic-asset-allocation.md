# Dynamic Asset Allocation

**Topic:** Computational Finance
**Tags:** dynamic allocation, portfolio management, reinforcement learning, optimal control, sharpe ratio
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**Dynamic asset allocation** treats portfolio management as a sequential optimal control problem: an RL agent continuously adjusts asset weights $w_t$ at each time step in response to changing market conditions, seeking to maximise a long-term risk-adjusted objective rather than solving a single static optimisation.

## Key Formula

The agent follows a policy $\pi$ that maps the current state $s_t$ (prices, volatility, current weights) to an action $a_t$ (new asset weights). The Bellman optimality equation for the portfolio value function is:

$$V_t(s_t) = \max_{a_t} \left\{ r(s_t, a_t) + \gamma\, \mathbb{E}\!\left[V_{t+1}(s_{t+1}) \mid s_t, a_t\right] \right\}$$

The per-step reward $r(s_t, a_t)$ typically penalises risk and transaction costs:

$$r_t = \mu_p - \tfrac{1}{2}\lambda\,\sigma_p^2 - c\,\lVert w_t - w_{t-1} \rVert_1$$

where $\mu_p$ and $\sigma_p^2$ are the portfolio return and variance, $\lambda$ is risk aversion, and $c$ is the proportional transaction cost per unit weight change.

## Example

An RL agent manages a three-asset portfolio (UK equities, gilts, cash). The state includes realised volatility, the current weight vector, and a momentum signal. During a volatility spike, the agent's learned policy shifts from $w = (0.7, 0.2, 0.1)$ to $w = (0.3, 0.5, 0.2)$, reducing equity exposure and boosting gilts. The reward is computed as the Sharpe ratio contribution of that rebalancing step minus transaction costs.

## Remember

Static mean-variance optimisation solves once using historical estimates and never adapts; the resulting portfolio drifts as markets change. Dynamic allocation using RL learns a rebalancing *policy* — a rule for every market state — that implicitly accounts for regime changes, autocorrelation in volatility, and transaction costs. In practice, this is why systematic macro funds increasingly frame portfolio management as an RL problem: the policy generalises to market conditions never seen in the training data, rather than refitting a static model each month.
