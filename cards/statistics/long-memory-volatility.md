# Long Memory in Volatility

**Topic:** Statistics
**Tags:** long memory, volatility, autocorrelation, FIGARCH, ARCH-LM, time series
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Long memory** (long-range dependence) in volatility refers to the empirical finding that the autocorrelations of squared returns $r_t^2$ and absolute returns $|r_t|$ decay very slowly — hyperbolically rather than exponentially. This means a volatility shock today remains statistically significant for lags of hundreds of trading days.

Standard GARCH(1,1) produces autocorrelations that decay geometrically (short memory): the influence of a shock halves within a fixed number of lags. Empirical data contradicts this: $\text{Corr}(r_t^2,\, r_{t-k}^2)$ remains significant for lags of hundreds of days in daily equity and FX series.

The **ARCH-LM test** (Engle, 1982) detects whether ARCH effects — the raw presence of time-varying volatility — exist before fitting any particular model:

1. Regress the squared residuals $\hat{\varepsilon}_t^2$ on $q$ lags: $\hat{\varepsilon}_t^2 = a_0 + a_1\hat{\varepsilon}_{t-1}^2 + \cdots + a_q\hat{\varepsilon}_{t-q}^2 + u_t$.
2. Compute the test statistic $T \times R^2$, where $T$ is the sample size and $R^2$ is from the auxiliary regression.
3. Under the null of no ARCH effects, $T \times R^2 \sim \chi^2_q$.

A significant result rejects constant variance and motivates a GARCH-type model.

## Key Formula

**Hyperbolic decay of autocorrelations** (long memory):

$$\text{Corr}(r_t^2,\, r_{t-k}^2) \sim C \cdot k^{2d-1} \quad \text{as } k \to \infty$$

where $d \in (0, \tfrac{1}{2})$ is the fractional integration parameter and $C$ is a positive constant. For short-memory processes (GARCH), autocorrelations decay exponentially: $\rho_k \sim \phi^k$.

**FIGARCH** (Baillie, Bollerslev, and Mikkelsen, 1996) introduces fractional differencing into the variance equation:

$$\Phi(L)(1-L)^d \varepsilon_t^2 = \omega + \left[1 - \beta(L)\right]\nu_t$$

where $L$ is the lag operator, $\Phi(L)$ and $\beta(L)$ are lag polynomials, $d \in (0,1)$ governs persistence, and $\nu_t = \varepsilon_t^2 - \sigma_t^2$ is the variance innovation. When $d = 0$ this collapses to GARCH; when $d = 1$ it gives integrated GARCH (IGARCH).

**ARCH-LM test statistic:**

$$\text{LM} = T \times R^2 \;\overset{H_0}{\sim}\; \chi^2_q$$

## Example

A researcher fits GARCH(1,1) to daily S&P 500 returns over 20 years and finds $\hat{\alpha} + \hat{\beta} = 0.985$. Autocorrelations of squared returns at lag $k = 100$ days should be approximately $0.985^{100} \approx 0.22$ under GARCH. In practice the observed autocorrelation is $0.18$, but at lag $k = 500$ GARCH predicts $0.985^{500} \approx 0.0006$ whilst the empirical value is still $0.08$ — thirty times larger. This persistence is consistent with $d \approx 0.35$ in a FIGARCH model.

Running the ARCH-LM test with $q = 10$ lags on the residuals yields $\text{LM} = 250 \times 0.42 = 105$, far exceeding the $\chi^2_{10}$ critical value of $18.3$ at the 1% level. ARCH effects are present, confirming that conditional heteroskedasticity must be modelled.

## Remember

Long memory in volatility means that a large shock — a market crash, a central bank surprise, a geopolitical event — does not simply fade within a few weeks as GARCH implies. The effect lingers for months. For a risk manager, this matters enormously: Value at Risk (VaR) and Expected Shortfall estimates based on short-memory GARCH will underestimate how long elevated volatility persists, causing capital buffers to be released too soon. FIGARCH and related models (HAR-RV, ARFIMA on realised volatility) are used in practice to produce more conservative multi-week horizon risk forecasts. The ARCH-LM test is the standard first diagnostic — run it on model residuals to confirm that heteroskedasticity has been adequately captured before signing off on any volatility model.
