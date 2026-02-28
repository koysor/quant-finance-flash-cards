# Drift and Volatility Parameters

**Topic:** Stochastic Processes
**Tags:** drift, volatility, parameters, annualisation, mu, sigma
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

**Drift** ($\mu$) and **volatility** ($\sigma$) are the two parameters that define the random walk model of asset prices. Drift is the annualised expected return (the deterministic trend), and volatility is the annualised standard deviation of returns (the size of random fluctuations). Both are expressed in units of "per year."

## Key Formula

Over a time step $\delta t$ (as a fraction of a year):

$$\text{Mean of return} = \mu \, \delta t$$

$$\text{Std dev of return} = \sigma \sqrt{\delta t}$$

**Annualising from daily data:**

$$\mu = \bar{R}_{\text{daily}} \times 252 \qquad \sigma = s_{\text{daily}} \times \sqrt{252}$$

## Example

For the S&P 500 (1950-2006):

| Parameter | Daily | Annualised |
|---|---|---|
| Drift $\mu$ | 0.035% | 8.82% |
| Volatility $\sigma$ | 0.89% | 14.1% |

The volatility is larger than the drift, meaning in any single year the random noise is bigger than the expected return.

## Remember

$\mu$ and $\sigma$ are the only two inputs needed to simulate asset price paths via Monte Carlo or to price options via Black-Scholes. Getting them right — especially $\sigma$ — is the central calibration challenge in quantitative finance.
