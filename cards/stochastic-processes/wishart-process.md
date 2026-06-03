# Wishart Process

**Topic:** Stochastic Processes
**Tags:** wishart process, matrix-valued sde, stochastic correlation, multi-asset, covariance dynamics, affine model
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A Wishart process is a matrix-valued stochastic process taking values in the space of symmetric positive definite matrices, extending the scalar Cox-Ingersoll-Ross variance process to a full covariance matrix that evolves stochastically over time.

## Key Formula

The $n \times n$ Wishart process $\Sigma_t$ satisfies:

$$d\Sigma_t = \!\left(\Omega\Omega^\top + M\Sigma_t + \Sigma_t M^\top\right)dt + \sqrt{\Sigma_t}\,dW_t\, Q + Q^\top dW_t^\top\sqrt{\Sigma_t}$$

where $\Omega, M, Q \in \mathbb{R}^{n \times n}$, $W_t$ is a matrix of independent Brownian motions, and $\sqrt{\Sigma_t}$ is the matrix square root. The scalar CIR model $dV_t = \kappa(\theta - V_t)\,dt + \sigma\sqrt{V_t}\,dW_t$ is recovered as the $n = 1$ special case with $M = -\kappa/2$, $\Omega\Omega^\top = \kappa\theta$, and $Q = \sigma/2$.

## Example

A two-asset equity-credit model uses a $2 \times 2$ Wishart process for $\Sigma_t$. At calm times, $\Sigma_t \approx \text{diag}(0.04, 0.09)$ (20% and 30% vol, near-zero correlation). During stress, the off-diagonal element rises to 0.012 (40% equity-credit correlation), accurately capturing the wrong-way risk in which credit spreads widen exactly when equity positions lose most. A static correlation assumption would systematically underprice CVA in this scenario.

## Remember

In multi-asset derivatives, the biggest limitation of applying Heston or SABR independently to each asset is treating correlation as a constant. Wrong-way risk in CVA, basket option skew, and cross-asset variance swaps all depend critically on how correlation changes under stress. The Wishart process models the full covariance matrix as a stochastic object, producing smile-consistent prices across all assets and capturing correlation spikes that constant-correlation models miss.
