# Stylized Facts of Asset Returns

**Topic:** Statistics
**Tags:** stylised facts, returns, fat tails, volatility clustering, non-normality, empirical finance
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Stylised facts** are empirical regularities of financial asset returns that appear consistently across markets, instruments, and time periods. Cont (2001) catalogued eight such facts that any credible returns model must reproduce. They are called "stylised" because they describe the broad statistical shape of return behaviour rather than exact numerical values.

| # | Fact | Description |
|---|------|-------------|
| 1 | **Non-normality** | Return distributions have fat tails (leptokurtosis); large moves occur far more often than a normal model predicts |
| 2 | **Negative skewness** | Large losses are more frequent than large gains of equal magnitude — the left tail is heavier |
| 3 | **No return autocorrelation** | Daily log-returns are approximately unpredictable: $\rho_k \approx 0$ for $k \geq 1$ |
| 4 | **Volatility clustering** | Turbulent periods cluster in time — large moves beget large moves |
| 5 | **Long memory in volatility** | Squared and absolute returns show significant positive autocorrelation over hundreds of lags |
| 6 | **Leverage effect** | Negative returns increase future volatility more than positive returns of equal size |
| 7 | **Aggregational Gaussianity** | Return distributions become closer to normal as the sampling horizon lengthens (daily → monthly) |
| 8 | **Intraday U-shape** | Intraday volatility is highest near market open and close, lowest around midday |

## Key Formula

There is no single formula — each fact is an empirical regularity. The clearest diagnostic pair:

**Return autocorrelation** (Fact 3): for lag $k$,
$$\rho_k^{(r)} = \text{Corr}(R_t,\, R_{t-k}) \approx 0$$

**Squared-return autocorrelation** (Facts 4 & 5): volatility clustering and long memory mean,
$$\rho_k^{(r^2)} = \text{Corr}(R_t^2,\, R_{t-k}^2) > 0 \quad \text{for many lags } k$$

The contrast between $\rho_k^{(r)} \approx 0$ and $\rho_k^{(r^2)} > 0$ is the defining empirical signature: returns are unpredictable but their *magnitude* is not.

## Example

**FTSE 100 daily returns (1984–2020):**

| Statistic | Observed value | Normal prediction |
|-----------|---------------|-------------------|
| Excess kurtosis | ≈ 5–8 | 0 |
| Skewness | ≈ −0.3 to −0.7 | 0 |
| $\rho_1^{(r)}$ (return) | ≈ 0.00–0.02 | 0 |
| $\rho_1^{(r^2)}$ (squared return) | ≈ 0.15–0.30 | 0 |

The excess kurtosis of 5–8 means the probability of a move beyond three standard deviations is roughly ten times what a normal distribution implies — a "once-in-100-years" event under normality occurs several times a decade in practice.

## Remember

Simple **Geometric Brownian Motion** (GBM) — the foundation of Black-Scholes — assumes constant volatility and normally distributed returns. It fails to reproduce *any* of the eight stylised facts: returns are leptokurtic and negatively skewed (Facts 1–2), squared returns autocorrelate (Facts 4–5), and negative shocks raise volatility more than positive ones (Fact 6). This is not a minor model imperfection — it means GBM systematically underprices deep out-of-the-money puts, underestimates crash risk, and ignores volatility regimes. Models developed to address these shortcomings include **GARCH** (Facts 4–5), **GJR-GARCH** (Fact 6), and **stochastic volatility** models such as Heston (Facts 1, 4–6). Understanding the stylised facts is the first step in choosing the right model for the right purpose.
