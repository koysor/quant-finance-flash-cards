# Volatility Clustering

**Topic:** Statistics
**Tags:** volatility, clustering, autocorrelation, GARCH, stylised facts, returns
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

**Volatility clustering** is the empirical observation that large price changes tend to be followed by large price changes (of either sign), and small price changes tend to be followed by small price changes. Formally, while returns themselves show little autocorrelation, the absolute or squared returns exhibit significant positive autocorrelation over many lags.

## Key Formula

Volatility clustering is quantified by the autocorrelation of squared returns at lag $k$:

$$\rho_k = \frac{\text{Cov}(R_t^2,\; R_{t-k}^2)}{\text{Var}(R_t^2)}$$

In the simplest GARCH(1,1) model, the conditional variance $\sigma_t^2$ evolves as:

$$\sigma_t^2 = \omega + \alpha \, R_{t-1}^2 + \beta \, \sigma_{t-1}^2$$

where $\omega > 0$, $\alpha \geq 0$, $\beta \geq 0$, and stationarity requires $\alpha + \beta < 1$.

## Example

Suppose a GARCH(1,1) model has $\omega = 0.000002$, $\alpha = 0.08$, $\beta = 0.91$, and the current conditional variance is $\sigma_t^2 = 0.0001$ (i.e. daily vol $= 1\%$). A shock of $R_t = -3\%$ arrives:

$$\sigma_{t+1}^2 = 0.000002 + 0.08 \times (-0.03)^2 + 0.91 \times 0.0001$$

$$= 0.000002 + 0.000072 + 0.000091 = 0.000165$$

The conditional daily volatility jumps from $\sqrt{0.0001} = 1.0\%$ to $\sqrt{0.000165} \approx 1.28\%$. Because $\beta = 0.91$ is large, this elevated volatility persists for many subsequent days before decaying back toward the long-run level.

## Remember

Volatility clustering is one of the most robust stylised facts of financial returns and directly undermines the constant-volatility assumption in Black-Scholes. Risk managers who ignore clustering will underestimate Value at Risk during turbulent periods and overestimate it during calm ones. The GARCH family of models captures this effect and is standard on trading desks for forecasting short-term volatility and setting dynamic position limits.
