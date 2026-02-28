# Autocorrelation

**Topic:** Statistics
**Tags:** autocorrelation, time series, serial correlation, stationarity, returns
**Created:** 2026-02-28 20:46:20
**Author:** Claude Opus 4.6

---

## Definition

Autocorrelation (also called serial correlation) measures the linear relationship between a time series and a lagged copy of itself. The autocorrelation at lag $k$ quantifies how strongly today's value is correlated with the value $k$ periods ago.

## Key Formula

The sample autocorrelation at lag $k$ is:

$$\rho_k = \frac{\sum_{t=k+1}^{n}(x_t - \bar{x})(x_{t-k} - \bar{x})}{\sum_{t=1}^{n}(x_t - \bar{x})^2}$$

where $\bar{x}$ is the sample mean, $n$ is the number of observations, and $\rho_0 = 1$ by definition. Values of $\rho_k$ range from $-1$ (perfect negative autocorrelation) to $+1$ (perfect positive autocorrelation).

## Example

Consider five daily log-returns: $x_1 = 0.02$, $x_2 = 0.01$, $x_3 = -0.01$, $x_4 = 0.03$, $x_5 = -0.02$. The sample mean is $\bar{x} = 0.006$. To compute $\rho_1$:

Numerator: $(0.01 - 0.006)(0.02 - 0.006) + (-0.01 - 0.006)(0.01 - 0.006) + (0.03 - 0.006)(-0.01 - 0.006) + (-0.02 - 0.006)(0.03 - 0.006) = 0.000056 - 0.000064 - 0.000384 - 0.000624 = -0.001016$.

Denominator: $\sum(x_t - \bar{x})^2 = 0.001172$.

So $\rho_1 = -0.001016 / 0.001172 \approx -0.87$, indicating strong negative autocorrelation at lag 1 -- a positive return tends to be followed by a negative one.

## Remember

In quantitative finance, daily asset returns typically show near-zero autocorrelation, consistent with weak-form market efficiency. However, **squared** returns exhibit significant positive autocorrelation -- this is volatility clustering, the empirical fact that large moves tend to follow large moves. This pattern is the motivation for GARCH models and is critical for any risk model that needs to capture time-varying volatility rather than assuming it is constant.
