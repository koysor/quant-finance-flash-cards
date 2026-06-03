# Multi-Asset RL Option Pricing

**Topic:** Computational Finance
**Tags:** multi-asset, basket option, spread option, tdbp, curse of dimensionality, correlated assets
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Multi-asset RL option pricing** extends TDBP and related frameworks to derivatives whose payoff depends on two or more underlying assets — basket options, best-of options, spread options, and rainbow options. The state space grows from $(S_t, \tau)$ to $(S_t^{(1)}, \ldots, S_t^{(n)}, \tau)$, and the neural network must additionally learn the role of cross-asset correlations in determining the option price.

## Key Formula

For $n$ correlated assets with Cholesky-decomposed covariance $\Sigma = LL^\top$, simulated paths follow:

$$dS_t^{(i)} = r S_t^{(i)}\,dt + \sigma_i S_t^{(i)}\sum_{j=1}^{i} L_{ij}\,dW_t^{(j)}$$

The TDBP Bellman step is unchanged in form:

$$f_t\!\left(S_t^{(1)}, \ldots, S_t^{(n)};\,\theta_t\right) = e^{-r\Delta t}\,\mathbb{E}\!\left[f_{t+1}\!\left(S_{t+1}^{(1)}, \ldots, S_{t+1}^{(n)};\,\theta_{t+1}\right) \mid \mathcal{F}_t\right]$$

but the MLP input dimension increases from 2 to $n + 1$, and training path count must scale to cover the higher-dimensional state space adequately.

## Example

A basket call on 5 FTSE 100 stocks (equal weights, $K = 100$, $T = 30$ days, pairwise $\rho = 0.6$). A single-asset MLP requires $\sim$5,000 paths to converge; the 5-asset TDBP requires $\sim$50,000 paths for equivalent accuracy — a $10\times$ increase driven by the higher-dimensional state space. Adding attention across assets (attending to all 5 prices simultaneously) recovers accuracy with 20,000 paths because cross-asset attention captures correlation structure that independent per-asset MLPs must learn separately for each asset combination.

## Remember

Multi-asset RL option pricing is where **attention architectures become necessary rather than optional**: for $n \le 3$ assets a wide MLP manages, but for $n \ge 5$ the curse of dimensionality means the MLP either underfits (too narrow) or overfits (too wide, too few paths). Self-attention handles arbitrary $n$ by operating on the set of asset states rather than a fixed-length vector — the same attention weights that learned 3-asset basket pricing can be applied to 10-asset baskets without architectural changes, only additional training paths. Correlation is the critical new state variable: a pricer trained at $\rho = 0.6$ substantially mispricices at $\rho = 0.2$ and should include $\rho$ (or realised correlation) as an explicit input dimension.
