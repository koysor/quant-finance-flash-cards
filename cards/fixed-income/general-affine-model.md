# General Affine Model

**Topic:** Fixed Income
**Tags:** general affine model, N-factor, market price of risk, essentially affine, dual measure, term structure
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **general affine model** (Duffie and Kan, 1996) is the N-factor term structure framework in which the short rate and the risk-neutral state dynamics are both affine in the state vector $X_t \in \mathbb{R}^N$, yielding exponential-affine bond prices $P = e^{A(\tau) - B(\tau)^\top X_t}$ with $A$ and $B$ satisfying a vector Riccati ODE system. Bridging the risk-neutral ($\mathbb{Q}$) and physical ($\mathbb{P}$) measures requires specifying the market price of risk $\lambda(X_t)$.

## Key Formula

**Short rate:** $r_t = \delta_0 + \delta_1^\top X_t$

**Risk-neutral dynamics** (pricing measure $\mathbb{Q}$):

$$dX_t = (K_0 + K_1 X_t)\,dt + \Sigma(X_t)\,dW_t^{\mathbb{Q}}$$

where $(\Sigma\Sigma^\top)_{ij}(x) = (H_0)_{ij} + H_{1,ij}^\top x$ (affine variance matrix).

**Vector Riccati ODEs** for $\tau = T - t$:

$$\frac{dB}{d\tau} = \delta_1 - K_1^\top B - \tfrac{1}{2}\,\mathcal{H}_1(B), \quad B(0) = 0$$

$$\frac{dA}{d\tau} = \delta_0 - K_0^\top B + \tfrac{1}{2}\,\mathcal{H}_0(B), \quad A(0) = 0$$

where $\mathcal{H}_1(B) = \sum_i (H_{1,i}^\top B)B_i$ collects the quadratic $B$-terms from each variance factor.

**Essentially affine market price of risk** (Duffee, 2002):

$$\lambda_t = \lambda_0 + \lambda_1 X_t$$

This gives physical dynamics with the same affine structure:

$$dX_t = (\underbrace{K_0 + H_0\lambda_0}_{K_0^{\mathbb{P}}}\! + \underbrace{(K_1 + H_0\lambda_1)}_{K_1^{\mathbb{P}}} X_t)\,dt + \Sigma(X_t)\,dW_t^{\mathbb{P}}$$

## Example

A three-factor $A_0(3)$ (all-Gaussian) model calibrated to G10 government bond curves:

- **State vector:** $X_t = (L_t, S_t, C_t)$ — level, slope, curvature
- **Q-mean reversion:** $K_1 = \text{diag}(0.03, 0.30, 1.20)$ — level is near unit root, curvature reverts fast
- **Essentially affine λ:** $\lambda_0 = (-0.5, 1.2, 0.8)^\top$, $\lambda_1 \neq 0$

Under $\mathbb{P}$, the level factor has mean reversion $K_1^{\mathbb{P}} = K_1 + H_0\lambda_1$, which may differ substantially from $K_1^{\mathbb{Q}}$. The 10-year term premium is then $-B(10)^\top H_0\lambda_t$ — the inner product of the sensitivity vector with the risk compensation — and can be extracted from the estimated state path.

## Remember

The essentially affine specification (Duffee, 2002) is the workhorse of ACM-style term premium models at central banks worldwide. The key insight is that decoupling $\lambda_t = \lambda_0 + \lambda_1 X_t$ from the instantaneous volatility $\Sigma(X_t)$ allows the model to fit **both** the cross-section of bond prices (via $\mathbb{Q}$ parameters) **and** the time-series of yields (via $\mathbb{P}$ parameters) without forcing term premia to move only when volatility spikes — a constraint of the older completely affine specification that produced implausibly volatile term premia.
