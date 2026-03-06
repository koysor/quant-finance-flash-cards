# Efficient Frontier

**Topic:** Financial Mathematics
**Tags:** efficient frontier, mean-variance, portfolio optimisation, Markowitz, diversification
**Author:** Claude Opus 4.6

---

## Definition

The **efficient frontier** is the set of portfolios that offer the highest expected return for each level of risk (standard deviation), or equivalently, the lowest risk for each level of return. It forms the upper boundary of the feasible set in mean-variance space. Any portfolio below the frontier is suboptimal — a better portfolio exists with either higher return at the same risk, or lower risk at the same return.

## Key Formula

The efficient frontier solves the Markowitz optimisation for every target return $\mu^*$:

$$\min_{\mathbf{w}} \; \mathbf{w}^\top \Sigma \, \mathbf{w} \quad \text{subject to} \quad \mathbf{w}^\top \boldsymbol{\mu} = \mu^*, \quad \mathbf{w}^\top \mathbf{1} = 1$$

The frontier is a **hyperbola** (parabola in variance-return space). With a risk-free asset at rate $r_f$, the efficient frontier becomes a straight line — the **Capital Market Line (CML)**:

$$\mu_p = r_f + \frac{\mu_T - r_f}{\sigma_T} \sigma_p$$

where $T$ is the **tangency portfolio** (maximum Sharpe ratio).

## Example

Two assets: $\mu_A = 12\%$, $\sigma_A = 20\%$, $\mu_B = 6\%$, $\sigma_B = 10\%$, $\rho = 0.2$.

| $w_A$ | $\mu_p$ | $\sigma_p$ |
|-------|---------|-----------|
| 0.0 | 6.0% | 10.0% |
| 0.2 | 7.2% | 10.2% |
| 0.4 | 8.4% | 12.0% |
| 0.6 | 9.6% | 14.7% |
| 0.8 | 10.8% | 17.7% |
| 1.0 | 12.0% | 20.0% |

The minimum-variance portfolio is near $w_A \approx 0.18$, $\sigma_p \approx 9.9\%$. Portfolios on the upper branch (above the minimum) form the efficient frontier.

## Remember

The efficient frontier is the geometric output of Markowitz optimisation and the foundation of modern asset allocation. In practice, the frontier is highly sensitive to its inputs — small changes in expected returns or the covariance matrix can shift the optimal weights dramatically. This "estimation error amplification" is why naive diversification (equal weight) often outperforms optimised portfolios out of sample. Robust methods like Black-Litterman, resampled frontiers, and shrinkage estimators were developed specifically to stabilise the frontier against noisy inputs.
