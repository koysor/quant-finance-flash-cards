# SciPy Optimisation for Calibration

**Topic:** Computational Finance
**Tags:** python, scipy, optimisation, calibration, model fitting, minimisation
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**SciPy's optimisation module** (`scipy.optimize`) provides numerical minimisation routines used throughout quantitative finance to calibrate models to market data. The most common pattern is minimising the sum of squared differences between model prices and observed market prices — for example, finding the Heston parameters that best fit an observed volatility surface.

## Key Formula

**Calibration objective:**

$$\hat{\theta} = \arg\min_{\theta} \sum_{i=1}^{N} w_i \left( V_i^{\text{model}}(\theta) - V_i^{\text{market}} \right)^2$$

**Python implementation:**

```python
from scipy.optimize import minimize

def objective(params, market_prices, strikes, T):
    model_prices = price_model(params, strikes, T)
    return np.sum((model_prices - market_prices) ** 2)

result = minimize(objective, x0=initial_guess,
                  args=(market_prices, strikes, T),
                  method="Nelder-Mead")
calibrated_params = result.x
```

## Example

Calibrate Black-Scholes implied volatility to three market call prices:

```python
from scipy.optimize import brentq

def bs_call(S, K, r, sigma, T):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    from scipy.stats import norm
    return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

# Find implied vol for a market price of £10.45
iv = brentq(lambda s: bs_call(100, 100, 0.05, s, 1) - 10.45, 0.01, 2.0)
# iv ≈ 0.20 (20%)
```

## Remember

Model calibration is where theory meets trading reality. Every pricing model — Black-Scholes, Heston, SABR, local volatility — has free parameters that must be set to match observable market prices before the model can be used to price or hedge exotic derivatives. SciPy provides the numerical engine: `minimize` for multi-parameter fits, `brentq` for root-finding (implied volatility), and `curve_fit` for regression-style calibration. The choice of optimiser matters — gradient-based methods (`L-BFGS-B`) are fast but require smooth objectives, while simplex methods (`Nelder-Mead`) are more robust to noisy or discontinuous loss surfaces common in exotic calibration.
