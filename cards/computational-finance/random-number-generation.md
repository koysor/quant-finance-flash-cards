# Random Number Generation for Simulation

**Topic:** Computational Finance
**Tags:** python, numpy, random numbers, simulation, reproducibility, seed
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Random number generation** in NumPy provides the stochastic inputs for Monte Carlo simulation, bootstrapping, and scenario analysis. The modern API (`numpy.random.Generator`) uses the PCG64 algorithm to produce high-quality pseudorandom numbers from a deterministic seed, and offers methods for drawing from any distribution needed in finance — normal, lognormal, Poisson, uniform, and more.

## Key Formula

**Standard normal draws** for $M$ simulation paths over $N$ time steps:

$$Z_{ij} \sim \mathcal{N}(0, 1), \quad i = 1, \dots, N, \; j = 1, \dots, M$$

**Python implementation:**

```python
import numpy as np

rng = np.random.default_rng(seed=42)  # reproducible
Z = rng.standard_normal((n_steps, n_paths))
```

**Correlated draws** via Cholesky decomposition:

```python
L = np.linalg.cholesky(correlation_matrix)
Z_corr = Z @ L.T
```

## Example

Generate 100,000 standard normal draws and verify the distribution:

```python
rng = np.random.default_rng(seed=42)
Z = rng.standard_normal(100_000)

print(f"Mean: {Z.mean():.4f}")    # ≈ 0.0000
print(f"Std:  {Z.std():.4f}")     # ≈ 1.0000
print(f"Skew: {scipy.stats.skew(Z):.4f}")  # ≈ 0.00
```

Setting the seed ensures that every run produces identical paths — critical for debugging pricing models and for regulatory reproducibility requirements.

## Remember

Reproducibility is not optional in production quant systems. Regulators and risk committees require that a VaR number or model price can be exactly reproduced months later, which means every simulation must be seeded and the seed must be logged. The modern `numpy.random.Generator` API (introduced in NumPy 1.17) replaces the legacy `np.random.seed()` global state with explicit generator objects, making it safe to run independent simulations in parallel without seed collisions. In multi-asset simulations, the Cholesky decomposition of the correlation matrix transforms independent normal draws into correlated ones — this is the standard technique for generating realistic joint returns across a portfolio.
