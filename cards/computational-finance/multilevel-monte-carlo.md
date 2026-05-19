# Multilevel Monte Carlo

**Topic:** Computational Finance
**Tags:** monte carlo, variance reduction, mlmc, simulation, path-dependent, computational efficiency
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Multilevel Monte Carlo (MLMC) is a variance-reduction technique that estimates an expected value by combining simulations run at multiple levels of time-step resolution. Coarse grids are cheap but noisy; fine grids are accurate but expensive. MLMC combines many coarse-grid samples with progressively fewer fine-grid correction terms, achieving the accuracy of the finest grid at a fraction of the cost.

## Key Formula

Let $P_\ell$ denote the option price approximation using $2^\ell$ time steps. The MLMC estimator telescopes:

$$\mathbb{E}[P_L] = \mathbb{E}[P_0] + \sum_{\ell=1}^{L} \mathbb{E}[P_\ell - P_{\ell-1}]$$

Each correction term $Y_\ell = P_\ell - P_{\ell-1}$ uses **coupled paths** — the same Brownian increments refined to both resolutions — so the variance of $Y_\ell$ shrinks rapidly with $\ell$:

$$\text{Var}(Y_\ell) \approx c \cdot 2^{-\ell}$$

The optimal number of samples at level $\ell$ is:

$$N_\ell \propto \sqrt{\frac{\text{Var}(Y_\ell)}{C_\ell}}$$

Where $C_\ell \propto 2^\ell$ is the cost per sample at level $\ell$. This gives total cost $O(\varepsilon^{-2})$ vs $O(\varepsilon^{-3})$ for standard Monte Carlo to achieve root-mean-square error $\varepsilon$.

## Example

Price an Asian call with 252 daily time steps to 0.1% accuracy. Standard Monte Carlo needs $\sim\!10^7$ paths at the finest grid: cost $\approx 252 \times 10^7 = 2.5 \times 10^9$ operations. MLMC uses levels $\ell = 0, \ldots, 8$ (1 to 256 steps):

| Level | Steps | $N_\ell$ samples |
|-------|-------|-----------------|
| 0 | 1 | 500,000 |
| 4 | 16 | 50,000 |
| 8 | 256 | 5,000 |

Total cost $\approx 10^7$ operations — a **250× speedup** for the same accuracy.

## Remember

MLMC is most valuable for path-dependent products (Asian, barrier, lookback options) where fine time discretisation is essential for accuracy but expensive. In production systems, it complements variance-reduction techniques such as antithetic variates and control variates. The core insight — that correction terms between adjacent levels have rapidly decaying variance — applies to any simulation problem, including stochastic PDE solvers and Bayesian MCMC convergence diagnostics.
