# Monte Carlo Simulation in Python

**Topic:** Computational Finance
**Tags:** python, monte carlo, simulation, numpy, option pricing, paths
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Monte Carlo simulation in Python** uses NumPy's vectorised random number generation to simulate thousands or millions of asset price paths simultaneously, then averages discounted payoffs to estimate derivative prices. The key insight is that all paths can be generated and evaluated as matrix operations — no path-by-path loop is needed.

## Key Formula

Under risk-neutral GBM, a single time step for $M$ paths:

$$S_{t+\Delta t} = S_t \exp\!\left[\left(r - \tfrac{\sigma^2}{2}\right)\Delta t + \sigma\sqrt{\Delta t}\,Z\right], \quad Z \sim \mathcal{N}(0,1)$$

**Vectorised Python (all paths at once):**

```python
import numpy as np

def simulate_gbm(S0, r, sigma, T, n_steps, n_paths):
    dt = T / n_steps
    Z = np.random.standard_normal((n_steps, n_paths))
    increments = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
    log_paths = np.cumsum(increments, axis=0)
    return S0 * np.exp(np.vstack([np.zeros(n_paths), log_paths]))
```

## Example

Price a European call ($S_0 = £100$, $K = £105$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year) using 100,000 paths:

```python
paths = simulate_gbm(100, 0.05, 0.20, 1.0, 252, 100_000)
payoffs = np.maximum(paths[-1] - 105, 0)
price = np.exp(-0.05) * payoffs.mean()
# ≈ £8.02 (vs Black-Scholes analytical: £8.02)
```

The 100,000-path simulation runs in under 0.5 seconds on a typical laptop.

## Remember

Monte Carlo is the workhorse of derivatives pricing desks because it scales to any payoff structure — path-dependent exotics, multi-asset baskets, and early-exercise products can all be priced by changing only the payoff function, not the simulation engine. In Python, the critical performance lever is generating the entire $(n\_steps \times n\_paths)$ random matrix in one NumPy call rather than looping over individual paths. Variance reduction techniques (antithetic variates, control variates) further improve convergence, and the $1/\sqrt{N}$ standard error rate means that quadrupling the number of paths halves the pricing error.
