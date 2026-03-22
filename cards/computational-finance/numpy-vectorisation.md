# NumPy Vectorisation

**Topic:** Computational Finance
**Tags:** python, numpy, vectorisation, performance, arrays
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Vectorisation** is the practice of replacing explicit Python loops with NumPy array operations that execute in compiled C code. In quantitative finance, where calculations routinely span millions of scenarios or time steps, vectorised code can be 100× faster than equivalent loop-based Python.

## Key Formula

A simple example: computing daily log returns from a price series.

**Mathematical form:**

$$r_t = \ln\!\left(\frac{S_t}{S_{t-1}}\right)$$

**Vectorised Python:**

```python
import numpy as np

returns = np.log(prices[1:] / prices[:-1])
```

The entire division, logarithm, and slicing happen in a single pass through compiled code — no Python `for` loop touches individual elements.

## Example

Compute log returns for five closing prices: £100, £102, £99, £101, £103.

```python
prices = np.array([100, 102, 99, 101, 103])
returns = np.log(prices[1:] / prices[:-1])
# array([ 0.0198,  -0.0299,  0.0201,  0.0196])
```

The same calculation with a loop:

```python
returns = [np.log(prices[i] / prices[i-1]) for i in range(1, len(prices))]
```

For a universe of 5,000 stocks over 10 years of daily data (~12.5 million returns), the vectorised version runs in milliseconds; the loop version takes seconds.

## Remember

Vectorisation is the single most important performance technique in Python-based quant finance. Every major library — NumPy for arrays, pandas for time series, SciPy for optimisation — is built on this principle. When writing pricing engines, risk aggregations, or backtests, the first question should always be: can this be expressed as an array operation? If a `for` loop iterates over dates, strikes, or scenarios, there is almost certainly a vectorised alternative. The speed difference is not marginal — it determines whether a calculation finishes in time for the trading day.
