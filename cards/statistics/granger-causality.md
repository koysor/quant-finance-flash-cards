# Granger Causality

**Topic:** Statistics
**Tags:** granger causality, time series, forecasting, var model, macro forecasting, predictability
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Granger causality** is a statistical test of whether the past values of one time series $X$ provide statistically significant additional predictive power for a second series $Y$, over and above $Y$'s own past values. $X$ "Granger-causes" $Y$ if knowing $X$'s history improves forecasts of $Y$ — it is a test of **predictability**, not true causation.

## Key Formula

Fit two regressions and compare:

**Restricted model** (Y predicts itself):
$$Y_t = \alpha_0 + \sum_{k=1}^{p} \alpha_k Y_{t-k} + \varepsilon_t$$

**Unrestricted model** (X also included):
$$Y_t = \alpha_0 + \sum_{k=1}^{p} \alpha_k Y_{t-k} + \sum_{k=1}^{p} \beta_k X_{t-k} + u_t$$

$X$ Granger-causes $Y$ if the F-test rejects $H_0: \beta_1 = \beta_2 = \cdots = \beta_p = 0$.

$$F = \frac{(RSS_R - RSS_U)/p}{RSS_U/(n - 2p - 1)} \sim F_{p,\, n-2p-1}$$

## Example

Testing whether the credit spread (IG-Treasury) Granger-causes S&P 500 returns. Restricted model: S&P regressed on its own 3 lags ($p=3$). Unrestricted: add 3 lags of credit spread. $F = 4.2 > F_{0.05} = 2.7$. Conclusion: lagged credit spreads contain significant incremental information for predicting equity returns — consistent with credit leading equities in risk-off episodes.

## Remember

Granger causality is widely used in macro forecasting to determine which economic indicators (credit spreads, yield curve slope, PMI) provide genuine incremental predictive power for asset returns or macro variables. The critical caveat is that Granger causality is a test of predictability in-sample, not true economic causation — a spurious relationship from a third confounding variable can produce a significant F-statistic. Both series must also be stationary before the test; applying it to non-stationary price levels (rather than returns or spreads) produces spurious F-statistics.
