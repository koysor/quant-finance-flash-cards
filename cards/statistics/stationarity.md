# Stationarity

**Topic:** Statistics
**Tags:** stationarity, unit root, covariance stationary, time series, mean reversion, ADF test
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A time series $\{X_t\}$ is **covariance stationary** (weakly stationary) if its first two moments are constant over time: the mean $\mathbb{E}[X_t] = \mu$ and the autocovariance $\text{Cov}(X_t, X_{t+h}) = \gamma(h)$ depend only on the lag $h$, not on $t$. A non-stationary series has time-varying mean or variance, making standard statistical inference invalid.

## Key Formula

**Conditions for covariance stationarity:**

$$\mathbb{E}[X_t] = \mu \quad (\text{constant}), \qquad \text{Cov}(X_t, X_{t+h}) = \gamma(h) \quad (\text{lag only})$$

**Unit root process** (non-stationary random walk):

$$X_t = X_{t-1} + \varepsilon_t \implies \text{Var}(X_t) = t\sigma^2 \to \infty$$

**Log-returns are stationary; log-prices are not:**

$$\text{Non-stationary: } \ln S_t = \ln S_{t-1} + r_t \qquad \text{Stationary: } r_t = \ln S_t - \ln S_{t-1}$$

**Test:** Augmented Dickey-Fuller (ADF) test checks for a unit root — reject $H_0$ (unit root) to confirm stationarity.

## Example

Plot the S&P 500 index level over 20 years: it trends upward with growing variance — **non-stationary**. Plot the daily log-returns: they fluctuate around a constant mean near zero with roughly stable variance — **stationary** (setting aside volatility clustering).

Running the ADF test on log-returns gives $p < 0.01$: reject the unit root hypothesis; log-returns are stationary. Running it on log-prices gives $p > 0.10$: fail to reject; log-prices have a unit root.

## Remember

Stationarity is the **first assumption** to check before applying any time series model in quantitative finance. GARCH models, VaR backtests, factor model regressions, and cointegration-based pairs trading all require the input series (log-returns, spreads, residuals) to be stationary. Using a non-stationary series in regression produces **spurious correlations** — two random walks will appear strongly correlated simply because they both trend, with no causal link. This is why risk models are built on log-returns rather than prices, and why spread trading strategies test for cointegration (a specific form of stationarity in the spread) before committing capital.
