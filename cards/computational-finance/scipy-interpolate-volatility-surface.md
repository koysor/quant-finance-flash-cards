# scipy.interpolate for Volatility Surfaces

**Topic:** Computational Finance
**Tags:** python, scipy, interpolation, volatility surface, implied volatility, options
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

`scipy.interpolate` provides tools to construct smooth continuous functions from discrete data points. In options markets, implied volatilities are only observed at traded strikes and expiries; `scipy.interpolate` turns those sparse market quotes into a smooth volatility surface that can be evaluated at any strike-expiry pair needed for pricing or hedging.

## Key Formula

**Bivariate interpolation of an implied-vol grid:**

```python
from scipy.interpolate import RectBivariateSpline
import numpy as np

strikes    = np.array([80, 90, 100, 110, 120])   # £
expiries   = np.array([0.25, 0.5, 1.0, 2.0])     # years
ivol_grid  = ...   # shape (4, 5) — market implied vols

spline = RectBivariateSpline(expiries, strikes, ivol_grid, kx=3, ky=3)

# Query at any (T, K)
iv_at_105_6m = spline(0.5, 105)[0, 0]   # e.g. 0.187 → 18.7%
```

**1-D cubic spline along a single expiry slice:**

```python
from scipy.interpolate import CubicSpline

cs = CubicSpline(strikes, ivol_grid[2])   # T = 1 year slice
iv_105 = cs(105)
```

## Example

A derivatives desk quotes implied vols for 5 strikes × 4 expiries (20 data points). To price a barrier option at $K = 97$, $T = 9$ months — a point not in the market grid — the desk fits a `RectBivariateSpline` and queries it: `spline(0.75, 97) ≈ 0.194`. This 19.4% vol is fed into the pricing model. Without interpolation, the desk would need to use the nearest quoted strike, introducing a mispricing of several basis points.

## Remember

A smooth, arbitrage-free volatility surface is essential for consistent derivatives pricing: if the surface has kinks or is not monotone in certain directions, it admits calendar spreads or butterfly arbitrages that sophisticated counterparties will exploit. `scipy.interpolate` provides the numerical smoothing, but the quant must also enforce no-arbitrage constraints (Gatheral's SVI parameterisation or Dupire's local volatility condition) on top of the interpolated surface.
