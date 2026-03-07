# Augmented Dickey-Fuller Test

**Topic:** Statistics
**Tags:** unit root, stationarity, time series, adf test, cointegration
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The Augmented Dickey–Fuller (ADF) test is a hypothesis test for determining whether a time series has a unit root — that is, whether it is non-stationary. The null hypothesis is that the series contains a unit root (non-stationary); rejecting the null provides evidence that the series is stationary.

## Key Formula

The ADF test estimates the regression:

$$\Delta y_t = \alpha + \gamma \, y_{t-1} + \sum_{i=1}^{p} \delta_i \, \Delta y_{t-i} + \varepsilon_t$$

where $\Delta y_t = y_t - y_{t-1}$ and the lagged differences $\Delta y_{t-i}$ absorb serial correlation.

- **Null hypothesis** ($H_0$): $\gamma = 0$ (unit root, non-stationary)
- **Alternative** ($H_1$): $\gamma < 0$ (stationary)

The test statistic is $\tau = \hat{\gamma} \, / \, \text{SE}(\hat{\gamma})$, compared against Dickey–Fuller critical values (not standard $t$-distribution tables).

## Example

A quant tests whether a stock's log-price series is stationary. With 500 daily observations and 5 lags:

$$\hat{\gamma} = -0.008, \quad \text{SE}(\hat{\gamma}) = 0.006$$

$$\tau = \frac{-0.008}{0.006} = -1.33$$

The 5% critical value is $-2.87$. Since $-1.33 > -2.87$, we fail to reject the null — the log-price series has a unit root and is non-stationary. This is expected: stock prices follow a random walk.

However, testing the **log-return** series ($\Delta \log P_t$) yields $\tau = -18.2$, far below $-2.87$, confirming that returns are stationary.

## Remember

The ADF test is an essential diagnostic in quantitative finance. Most asset prices are non-stationary (they have unit roots), but returns are stationary — this distinction determines which statistical tools are valid. Applying OLS regression to non-stationary series produces spurious results with inflated $R^2$. In pairs trading, the ADF test is applied to the spread between two prices to confirm cointegration: if the spread is stationary, mean-reversion strategies are justified. The choice of lag length $p$ matters — too few lags leave serial correlation in the residuals, while too many reduce statistical power.
