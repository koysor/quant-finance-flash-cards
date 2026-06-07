# Non-Stationarity

**Topic:** Statistics
**Tags:** non-stationarity, unit root, structural break, cointegration, time series, differencing
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A time series is **non-stationary** if its statistical properties — mean, variance, or autocovariance — change over time. Non-stationarity comes in two main forms: **stochastic trends** (unit root processes, where shocks accumulate permanently) and **deterministic trends** (where the mean drifts linearly with time). A third form, **structural breaks**, occurs when the data-generating process shifts abruptly at a point in time.

## Key Formula

**Trend-stationary (TS) process** — remove a deterministic trend by detrending:

$$X_t = \mu + \beta t + \varepsilon_t \implies \tilde{X}_t = X_t - \mu - \beta t \text{ is stationary}$$

**Difference-stationary (DS) / unit root process** — remove stochastic trend by differencing:

$$X_t = X_{t-1} + \varepsilon_t \implies \Delta X_t = X_t - X_{t-1} = \varepsilon_t \text{ is stationary}$$

An $I(d)$ process requires $d$ differences to achieve stationarity. Log-prices are $I(1)$; log-returns ($\Delta \ln S_t$) are $I(0)$.

**Spurious regression condition:** if $X_t$ and $Y_t$ are independent $I(1)$ series, OLS gives $R^2 \to 1$ and $t$-statistics $\to \infty$ in large samples — a false signal of a relationship.

## Example

Regress the log of UK house prices on the log of FTSE 100 index levels from 1990 to 2020. Both series trend upward, both are $I(1)$. OLS yields $R^2 = 0.87$ and $t = 12.4$ — apparently a strong relationship. But this is a **spurious regression**: two independent random walks appear related because they share a common upward drift. The Augmented Dickey-Fuller test on the residuals fails to reject the unit root, confirming no genuine cointegration. The fix: take first differences of both series (log-returns), which produces $I(0)$ series and yields no significant relationship.

## Remember

Non-stationarity is the single most important data check before building any financial time series model. Virtually all standard econometric tools — OLS, GARCH, VAR models — assume the input series are stationary ($I(0)$). The correct treatment depends on the source: TS processes are detrended; DS processes are differenced. When two $I(1)$ series move together, they may be **cointegrated** (sharing a common stochastic trend), which is the theoretical foundation of **pairs trading** and **relative value** strategies — the spread is stationary even though each leg is not.
