# Neural SDE

**Topic:** Computational Finance
**Tags:** neural sde, latent sde, generative model, stochastic process, path generation, deep learning
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **Neural SDE** replaces the fixed parametric drift and diffusion coefficients of a classical SDE with neural networks trained to match an observed distribution of paths. The result is a data-driven stochastic process whose sample paths capture stylised facts — fat tails, volatility clustering, jumps — without committing to a specific parametric family such as GBM or Heston.

## Key Formula

The latent state $X_t$ evolves as:

$$dX_t = \underbrace{f_\theta(X_t, t)}_{\text{neural drift}}\,dt + \underbrace{g_\phi(X_t, t)}_{\text{neural diffusion}}\,dW_t$$

where $f_\theta$ and $g_\phi$ are neural networks. Training minimises the discrepancy between the distribution of generated paths $\{X_t^{(j)}\}$ and observed market paths $\{S_t^{(j)}\}$, typically via a **Wasserstein GAN** or **maximum likelihood** objective over the path space:

$$\mathcal{L}(\theta, \phi) = W_1\!\left(\mathcal{L}\!\left(\{X_t\}_{t \le T}\right),\; \mathcal{L}\!\left(\{S_t\}_{t \le T}\right)\right)$$

Euler-Maruyama discretisation is used for backpropagation through the SDE.

## Example

A Neural SDE is trained on 10 years of S&P 500 daily log-returns. After 5,000 training epochs, the generated paths reproduce: (1) excess kurtosis of 4.8 vs 4.6 observed, (2) autocorrelation of squared returns (vol clustering) matching observed ACF at lag 1–20, and (3) a left-skew of $-0.62$ vs $-0.65$ observed. A TDBP pricer trained on Neural SDE paths prices one-month 10-delta puts 18% closer to market quotes than one trained on GBM paths with calibrated $\sigma$.

## Remember

Neural SDEs are the natural path generator for RL pricing agents that want to avoid the **model specification bias** of GBM or Heston: the learned SDE adapts to the actual distribution of the underlying asset, producing training paths that are realistic rather than ideally parametric. The key practical challenge is **risk-neutral adjustment** — Neural SDEs trained on historical P-measure data must be Girsanov-adjusted to produce Q-measure paths suitable for no-arbitrage pricing, otherwise the trained RL pricer will embed a P-measure drift premium into option prices.
