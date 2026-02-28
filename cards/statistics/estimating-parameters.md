# Estimating Parameters from Data

**Topic:** Statistics
**Tags:** estimation, annualisation, drift, volatility, calibration
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

**Parameter estimation** is the process of computing the drift $\mu$ and volatility $\sigma$ from historical price data. Daily returns are calculated first, then their sample mean and standard deviation are annualised using the number of trading days per year (approximately 252).

## Key Formula

**Step 1 — daily returns:**

$$R_i = \frac{S_{i+1} - S_i}{S_i}$$

**Step 2 — annualise:**

$$\mu = \bar{R} \times 252 \qquad \sigma = s \times \sqrt{252}$$

where $\bar{R}$ is the sample mean and $s$ is the sample standard deviation of daily returns.

## Example

From 1,000 daily S&P 500 returns: $\bar{R} = 0.035\%$, $s = 0.89\%$.

$$\mu = 0.00035 \times 252 = 8.82\% \text{ per year}$$

$$\sigma = 0.0089 \times \sqrt{252} = 0.0089 \times 15.87 = 14.1\% \text{ per year}$$

Note: mean scales by 252 (linear), volatility scales by $\sqrt{252}$ (square-root rule).

## Remember

These estimated parameters feed directly into every quantitative model — Monte Carlo simulation, Black-Scholes pricing, and Value at Risk. Getting $\sigma$ right matters far more than $\mu$ for option pricing, because the drift cancels out under risk-neutral pricing while volatility does not.
