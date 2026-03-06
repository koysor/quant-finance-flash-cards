# GARCH Model

**Topic:** Statistics
**Tags:** GARCH, volatility clustering, conditional variance, time series, risk
**Author:** Claude Opus 4.6

---

## Definition

The **Generalised Autoregressive Conditional Heteroskedasticity (GARCH)** model, introduced by Bollerslev (1986), captures the empirical fact that financial volatility changes over time and tends to cluster — periods of high volatility are followed by more high volatility, and vice versa. GARCH models the conditional variance as a function of past squared returns and past variance.

## Key Formula

**GARCH(1,1):**

$$\sigma_t^2 = \omega + \alpha \, \varepsilon_{t-1}^2 + \beta \, \sigma_{t-1}^2$$

where:
- $\sigma_t^2$ is the conditional variance at time $t$
- $\varepsilon_{t-1} = r_{t-1} - \mu$ is the previous period's return shock
- $\omega > 0$, $\alpha \geq 0$, $\beta \geq 0$, and $\alpha + \beta < 1$ for stationarity

**Unconditional (long-run) variance:**

$$\bar{\sigma}^2 = \frac{\omega}{1 - \alpha - \beta}$$

**Persistence:** the sum $\alpha + \beta$ measures how slowly volatility decays back to the long-run level. Typical equity estimates give $\alpha + \beta \approx 0.95\text{--}0.99$.

## Example

A GARCH(1,1) model has $\omega = 0.000002$, $\alpha = 0.08$, $\beta = 0.91$.

Yesterday's return shock was $\varepsilon_{t-1} = -0.03$ (a 3% drop) and yesterday's conditional variance was $\sigma_{t-1}^2 = 0.0004$ (daily vol $\approx 2\%$).

$$\sigma_t^2 = 0.000002 + 0.08 \times (-0.03)^2 + 0.91 \times 0.0004$$

$$= 0.000002 + 0.000072 + 0.000364 = 0.000438$$

$$\sigma_t = \sqrt{0.000438} \approx 2.09\%$$

The large negative shock has pushed today's conditional volatility up from 2.0% to 2.09%.

Long-run variance: $\bar{\sigma}^2 = 0.000002 / (1 - 0.08 - 0.91) = 0.0002$, so long-run daily vol $\approx 1.41\%$.

## Remember

GARCH is the workhorse model for time-varying volatility in quantitative finance. Banks use it to compute conditional VaR that adapts to current market conditions rather than relying on a fixed historical volatility. Option traders use GARCH forecasts as inputs to pricing models when implied volatility data is sparse. The key practical insight is that $\alpha + \beta$ close to 1 means volatility shocks persist for a long time — a single large market move can elevate the risk estimate for weeks, which directly affects position sizing and margin requirements.
