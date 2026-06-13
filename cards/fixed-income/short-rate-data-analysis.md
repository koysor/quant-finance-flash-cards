# Three-Stage Short-Rate Data Analysis

**Topic:** Fixed Income
**Tags:** data analysis, short rate, volatility estimation, drift estimation, market price of risk, empirical
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **three-stage data analysis framework** is a sequential procedure for deducing a realistic interest rate model directly from data rather than assuming a convenient parametric form. Each stage estimates a different component of the SDE $dr = u(r)\,dt + w(r)\,dW_t$ from the data source that can most cleanly identify it.

## Key Formula

| Stage | Component | Method | Data needed |
|---|---|---|---|
| 1 | Volatility $w(r) = \nu r^\beta$ | Log-log regression of $\mathbb{E}[(\delta r)^2]$ vs $r$ | Short-rate time series |
| 2 | Drift $u(r)$ | Fokker–Planck inversion of fitted steady-state PDF | Short-rate time series |
| 3 | Market price of risk $\lambda(r)$ | Yield-curve slope at short end: slope $\approx \tfrac{u - \lambda w}{2}$ | Bond price data |

The ordering is motivated by statistical efficiency:
- Variance $\propto \delta t$ — well identified from short intervals
- Drift $\propto \delta t$ but noisier — better recovered via the steady-state distribution
- $\lambda$ is **invisible** in spot-rate data — requires yield-curve data

## Example

From US 1-month LIBOR (1985–1997): Stage 1 gives $\beta = 1.13$, $\nu = 0.126$, ruling out Vasicek ($\beta = 0$) and CIR ($\beta = 0.5$). Stage 2 fits a lognormal steady-state PDF with median $\bar{r} = 8\%$ and log-standard deviation $a = 0.40$, giving a nonlinear mean-reverting drift. Stage 3 extracts $\lambda(r)$ from Treasury yield-curve slopes but finds it wildly noisy.

## Remember

The three-stage framework produces a **time-homogeneous model** grounded in empirical data, but this comes at a cost: a time-homogeneous model cannot exactly fit today's market yield curve. The choice between data-driven time-homogeneous models and calibrated time-inhomogeneous models (Ho–Lee, Hull–White) is the central modelling dilemma in interest rate quantitative finance.
