# GJR-GARCH Model

**Topic:** Statistics
**Tags:** garch, leverage effect, asymmetric volatility, conditional variance, time series, volatility clustering
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **GJR-GARCH model**, introduced by Glosten, Jagannathan, and Runkle (1993), extends standard GARCH(1,1) to capture the **leverage effect** — the empirical observation that negative return shocks increase volatility more than positive shocks of equal magnitude. It achieves this by adding an indicator term that activates only when the previous period's return was negative, multiplying the squared shock by an additional asymmetry parameter $\gamma$.

Unlike EGARCH (Nelson, 1991), which models the logarithm of the variance and uses standardised residuals, GJR-GARCH models variance directly and uses an indicator function $\mathbf{1}[\cdot]$ to switch the extra shock impact on or off.

## Key Formula

**GJR-GARCH(1,1) variance equation:**

$$\sigma_t^2 = \omega + \alpha \, r_{t-1}^2 + \gamma \, r_{t-1}^2 \, \mathbf{1}[r_{t-1} < 0] + \beta \, \sigma_{t-1}^2$$

where:
- $\omega > 0$: long-run variance intercept
- $\alpha \geq 0$: impact of a positive shock ($r_{t-1} \geq 0$)
- $\alpha + \gamma$: impact of a negative shock ($r_{t-1} < 0$)
- $\gamma > 0$: asymmetry (leverage) parameter — if positive, bad news raises volatility more
- $\beta \geq 0$: persistence of past conditional variance
- $\mathbf{1}[r_{t-1} < 0] = 1$ when last period's return was negative, 0 otherwise

**Stationarity condition:**

$$\alpha + \frac{\gamma}{2} + \beta < 1$$

**Unconditional (long-run) variance:**

$$\bar{\sigma}^2 = \frac{\omega}{1 - \alpha - \tfrac{\gamma}{2} - \beta}$$

When $\gamma = 0$ the model collapses to standard GARCH(1,1).

## Example

Estimated parameters: $\omega = 0.000002$, $\alpha = 0.05$, $\gamma = 0.08$, $\beta = 0.88$.

Persistence check: $0.05 + 0.08/2 + 0.88 = 0.97 < 1$ — stationary.

Yesterday's conditional variance: $\sigma_{t-1}^2 = 0.0004$ (daily vol $\approx 2\%$).

**Negative shock** — yesterday's return $r_{t-1} = -0.03$ (a 3% fall):

$$\sigma_t^2 = 0.000002 + (0.05 + 0.08) \times 0.0009 + 0.88 \times 0.0004$$

$$= 0.000002 + 0.000117 + 0.000352 = 0.000471, \quad \sigma_t \approx 2.17\%$$

**Positive shock** — yesterday's return $r_{t-1} = +0.03$ (a 3% rise):

$$\sigma_t^2 = 0.000002 + 0.05 \times 0.0009 + 0.88 \times 0.0004$$

$$= 0.000002 + 0.000045 + 0.000352 = 0.000399, \quad \sigma_t \approx 2.00\%$$

The same-sized shock produces 2.17% volatility when negative but only 2.00% when positive — the leverage effect is captured by $\gamma$.

## Remember

In risk management, underestimating volatility after a market fall can lead to dangerously understated VaR and Expected Shortfall. Symmetric GARCH treats a 3% gain and a 3% loss identically; GJR-GARCH does not. When computing one-day 99% VaR or a 10-day stressed ES, the extra $\gamma$ term means the model spikes volatility sharply on down-days — producing fatter left-tail estimates that better match realised drawdowns. Banks and hedge funds use GJR-GARCH (or its close rival EGARCH) as a default asymmetric volatility model when backtesting shows symmetric GARCH systematically underestimates tail risk in bear markets.
