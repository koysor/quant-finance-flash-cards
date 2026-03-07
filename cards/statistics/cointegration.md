# Cointegration

**Topic:** Statistics
**Tags:** cointegration, stationarity, pairs trading, engle-granger, time series
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Two non-stationary time series are cointegrated if a linear combination of them is stationary. Individually, each series may wander without bound (like a random walk), but together they share a long-run equilibrium — deviations from this equilibrium are temporary and mean-reverting.

## Key Formula

Two series $X_t$ and $Y_t$, each integrated of order 1 (i.e. $I(1)$), are cointegrated if there exists a coefficient $\beta$ such that the residual:

$$\varepsilon_t = Y_t - \beta X_t$$

is stationary ($I(0)$). The **Engle–Granger two-step procedure** is:

1. Estimate $\beta$ by OLS regression: $Y_t = \alpha + \beta X_t + \varepsilon_t$
2. Test $\varepsilon_t$ for stationarity using the Augmented Dickey–Fuller (ADF) test:

$$\Delta \varepsilon_t = \gamma \, \varepsilon_{t-1} + \sum_{i=1}^{p} \delta_i \, \Delta \varepsilon_{t-i} + u_t$$

Reject the null of no cointegration if $\gamma < 0$ and statistically significant (using Engle–Granger critical values, not standard ADF tables).

## Example

Two bank stocks, $A$ and $B$, are each non-stationary with unit roots. Regressing $A$ on $B$ gives $\hat{\beta} = 1.2$ and residuals $\varepsilon_t = A_t - 1.2 B_t$.

The ADF test on $\varepsilon_t$ yields a test statistic of $-3.8$, which exceeds the 5% Engle–Granger critical value of $-3.34$. We reject the null: the two prices are cointegrated.

This means the spread $A_t - 1.2 B_t$ is mean-reverting. When it widens beyond 2 standard deviations, a pairs trader would short $A$ and go long $1.2$ shares of $B$, expecting the spread to close.

## Remember

Cointegration is the statistical foundation of pairs trading and statistical arbitrage. Correlation measures how two series move together in the short run, but cointegration captures whether they are **bound together** in the long run. Two stocks can have low correlation but strong cointegration (they drift apart short-term but always revert), or high correlation but no cointegration (they move in the same direction but can diverge permanently). In quantitative finance, cointegration tests must be re-run regularly because structural breaks — mergers, regulatory changes, business model shifts — can destroy the long-run relationship and turn a profitable pairs trade into a losing one.
