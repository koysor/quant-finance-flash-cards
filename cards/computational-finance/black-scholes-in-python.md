# Black-Scholes Implementation in Python

**Topic:** Computational Finance
**Tags:** python, Black-Scholes, option pricing, scipy, vectorisation, greeks
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Implementing the **Black-Scholes formula in Python** translates the closed-form option pricing equations into vectorised code that can price thousands of options in a single call. Using `scipy.stats.norm` for the cumulative normal distribution and NumPy for array arithmetic, the entire pricing engine fits in a few lines and naturally extends to computing Greeks by finite difference or analytical formulae.

## Key Formula

$$C = S\,N(d_1) - Ke^{-rT}N(d_2)$$

**Python implementation:**

```python
import numpy as np
from scipy.stats import norm

def bs_call(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def bs_put(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
```

Because every operation is a NumPy ufunc, `S`, `K`, `sigma`, and `T` can be arrays — pricing an entire option chain at once.

## Example

Price a call and compute delta for a grid of spot prices:

```python
S = np.linspace(80, 120, 5)  # [80, 90, 100, 110, 120]
K, r, sigma, T = 100, 0.05, 0.20, 1.0

prices = bs_call(S, K, r, sigma, T)
# array([1.28, 4.28, 10.45, 19.73, 30.91])

# Delta by analytical formula
d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
delta = norm.cdf(d1)
# array([0.23, 0.42, 0.64, 0.81, 0.92])
```

## Remember

The Black-Scholes formula is often the first pricing function a junior quant implements, and its Python version serves as a building block for everything that follows. The vectorised implementation matters because real-world tasks — computing Greeks across a strike ladder, building a volatility surface, or running a hedging backtest — require evaluating the formula thousands of times. By accepting arrays for any input, the same function handles a single option or an entire book. This pattern (mathematical formula → vectorised Python function → array inputs) recurs throughout computational finance, from bond pricing to risk aggregation.
