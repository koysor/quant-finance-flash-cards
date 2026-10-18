# Moving-Average and Autoregressive Models

**Topic:** Statistics
**Tags:** time series, AR(1), moving average, ARMA, stationarity, mean reversion, persistence
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Time-series models describe a series by its own past. A **moving-average** model, MA($q$), writes the series as a weighted sum of current and past shocks. An **autoregressive** model, AR($p$), predicts the series from its own previous values. Together they form ARMA.

## Key Formula

$$\mathrm{MA}(q):\; x_t = \varepsilon_t + \theta_1\varepsilon_{t-1} + \cdots + \theta_q\varepsilon_{t-q} \qquad\qquad \mathrm{AR}(1):\; x_t = \phi\,x_{t-1} + \varepsilon_t$$

For AR(1), $\phi$ is the **persistence**. If $|\phi| < 1$ the series is stationary and mean-reverting with variance $\dfrac{\sigma_\varepsilon^2}{1 - \phi^2}$. If $\phi = 1$ it is a random walk and shocks never decay. $\phi$ is estimated by regressing $x_t$ on $x_{t-1}$.

## Example

With $\phi = 0.9$: the stationary variance is $\dfrac{\sigma_\varepsilon^2}{1 - 0.81} \approx 5.26\,\sigma_\varepsilon^2$, and a shock halves after $\dfrac{\ln 0.5}{\ln 0.9} \approx 6.6$ periods.

## Remember

AR(1) is discretised mean reversion. The Ornstein-Uhlenbeck process $dx = \kappa(\theta - x)\,dt + \sigma\,dW$ discretises to an AR(1) with $\phi = 1 - \kappa\,\Delta t$, so the mean-reversion speed $\kappa$ and the persistence $\phi$ are the same parameter. Spreads in pairs trading and short-rate models are modelled this way, and the $|\phi| < 1$ stationarity condition is what unit-root tests probe. AR and MA are also the building blocks that GARCH extends to the variance.
