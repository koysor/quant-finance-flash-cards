# Generalised Advantage Estimation (GAE)

**Topic:** Computational Finance
**Tags:** gae, advantage function, bias-variance trade-off, policy gradient, temporal difference, ppo
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

**Generalised Advantage Estimation (GAE)** is a family of advantage estimators parameterised by $\lambda \in [0, 1]$ that interpolates between the high-variance, low-bias Monte Carlo return and the low-variance, high-bias one-step TD advantage. It weights $n$-step TD errors geometrically by $(\gamma\lambda)^n$, providing a single hyperparameter to tune the bias-variance trade-off in policy gradient algorithms.

## Key Formula

Define the one-step TD error (also called the TD residual):

$$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

The GAE advantage estimate is the exponentially weighted sum of future TD errors:

$$\hat{A}_t^{\text{GAE}(\gamma,\lambda)} = \sum_{k=0}^{\infty} (\gamma\lambda)^k \delta_{t+k}$$

**Special cases:**
- $\lambda = 0$: $\hat{A}_t = \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$ — pure one-step TD (low variance, high bias if $V$ is inaccurate)
- $\lambda = 1$: $\hat{A}_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k} - V(s_t)$ — Monte Carlo return minus baseline (zero bias, high variance)

## Example

A delta-hedging agent uses GAE with $\gamma = 0.99$, $\lambda = 0.95$ (the PPO default). At step $t$ with 5 days to expiry:

| $k$ | $\delta_{t+k}$ | Weight $(\gamma\lambda)^k$ |
|-----|--------------|--------------------------|
| 0 | +0.012 | 1.000 |
| 1 | −0.008 | 0.940 |
| 2 | +0.015 | 0.884 |
| 3 | +0.003 | 0.831 |
| 4 | −0.005 | 0.781 |

$\hat{A}_t \approx 0.012 - 0.0075 + 0.0133 + 0.0025 - 0.0039 = 0.0163$

With $\lambda = 0$ only the first row matters ($\hat{A}_t = 0.012$); with $\lambda = 1$ all future errors contribute equally. The $\lambda = 0.95$ setting discounts future errors quickly enough to reduce variance while remaining nearly unbiased.

## Remember

GAE is the standard advantage estimator in PPO and A2C because $\lambda \approx 0.95$ empirically achieves a near-optimal bias-variance balance for most financial RL tasks. The $\lambda$ parameter has an intuitive financial interpretation: it controls how many time steps of future rewards the agent trusts before defaulting to the critic's value estimate. A high $\lambda$ is appropriate when the critic is inaccurate early in training (trusting the environment more); a low $\lambda$ is better once the critic has converged (trusting the critic's short-run estimate). For option hedging, where the reward at expiry dominates intermediate rewards, $\lambda$ close to 1 is typically preferred.

