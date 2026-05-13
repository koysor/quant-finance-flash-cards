# scipy.stats for Finance

**Topic:** Computational Finance
**Tags:** python, scipy, statistics, distributions, hypothesis testing, goodness of fit
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

`scipy.stats` is Python's primary module for statistical distributions, hypothesis tests, and descriptive statistics. In quantitative finance it is used to fit parametric distributions to return data, compute tail probabilities, run normality tests, and price options that depend on normal CDF values.

## Key Formula

**Fitting a distribution and computing tail probabilities:**

```python
from scipy import stats

# Fit a Student-t distribution to daily log-returns
returns = ...  # array of daily log-returns
df, loc, scale = stats.t.fit(returns)

# 1% VaR (left tail)
var_99 = stats.t.ppf(0.01, df, loc, scale)

# Probability of loss exceeding 3%
prob = stats.t.cdf(-0.03, df, loc, scale)
```

**Normality test (Jarque-Bera):**

```python
jb_stat, p_value = stats.jarque_bera(returns)
# p < 0.05 rejects normality
```

## Example

A risk analyst fits 500 days of S&P 500 returns. `stats.t.fit` returns $\hat{\nu} = 4.1$, $\hat{\mu} = 0.0003$, $\hat{\sigma} = 0.0089$. The 1% daily VaR is:

```python
var_99 = stats.t.ppf(0.01, df=4.1, loc=0.0003, scale=0.0089)
# var_99 ≈ -0.0231  →  daily VaR = 2.31% of portfolio value
```

Under the normal distribution (`stats.norm.ppf(0.01)`) the VaR would be only 2.07% — a 12% underestimate, illustrating why fat tails matter for risk management.

## Remember

`scipy.stats` is the bridge between financial theory and data. Every statistical test that validates a model assumption — normality of residuals, equality of variances across regimes, independence of returns — has a one-line implementation here. Critically, `stats.norm.cdf` and `stats.norm.ppf` implement $N(d_1)$ and $N^{-1}(\cdot)$ used in Black-Scholes, making `scipy.stats` the computational backbone of options pricing as well as risk measurement.
