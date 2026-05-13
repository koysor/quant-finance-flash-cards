# Macro Forecasting

**Topic:** Computational Finance
**Tags:** macro forecasting, economic indicators, ar model, tactical asset allocation, time series, ml benchmark
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Macro forecasting** uses historical macroeconomic data and leading indicators to predict future values of aggregate economic variables (GDP growth, inflation, unemployment) or asset class returns. In quantitative finance, ML models are evaluated against simple autoregressive benchmarks to determine whether additional complexity adds genuine out-of-sample predictive value.

## Key Formula

**AR(1) benchmark** — the naive baseline any ML model must beat:
$$Y_t = \phi_0 + \phi_1 Y_{t-1} + \varepsilon_t$$

**Multi-factor ML model** with $K$ macro predictors:
$$Y_t = f_{\boldsymbol{\theta}}(Y_{t-1},\, X_1^{(t-1)},\, \ldots,\, X_K^{(t-1)}) + \varepsilon_t$$

Common regressors $X_k$: yield curve slope ($10y - 2y$), credit spread (IG–Treasury), industrial production growth, ISM manufacturing PMI, non-farm payrolls. Model evaluation uses time-series cross-validation, and out-of-sample $R^2$ relative to the AR(1) is the standard performance measure.

## Example

Forecasting next-quarter S&P 500 returns using 5 macro predictors: term spread, credit spread, payrolls growth, ISM PMI, trailing 12-month momentum. AR(1) benchmark: out-of-sample $R^2 = 2\%$. Ridge regression with macro factors: $R^2 = 6\%$. Random Forest: $R^2 = 7\%$ but higher estimation error in small-sample regime. Conclusion: modest incremental benefit from macro factors; the AR(1) explains most forecastable variance.

## Remember

The AR(1) is the canonical benchmark in macro forecasting because it encodes the insight that the near future looks like the recent past — a hard baseline to beat in financial time series where signal-to-noise ratios are low. Diebold-Mariano tests are used to determine whether the improvement over the AR(1) is statistically significant or within sampling error. In tactical asset allocation, even a small genuine improvement in equity return forecasts (e.g. 2–3% out-of-sample $R^2$ above AR(1)) translates into meaningful risk-adjusted excess returns when compounded across rebalancing periods.
