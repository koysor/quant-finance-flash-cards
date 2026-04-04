# GARCH Volatility Forecasting

**Topic:** Statistics
**Tags:** GARCH, volatility forecasting, conditional variance, multi-step forecast, risk management
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

GARCH volatility forecasting uses the GARCH(1,1) model to predict future conditional variance over horizons from one day to several months. While the GARCH model itself describes how today's variance depends on yesterday's shock and variance, the forecasting application extends this to produce a **term structure of expected volatility** by iterating the variance equation forward. Multi-step forecasts are central to risk management (computing VaR over different horizons), option pricing (providing forward volatility inputs), and position sizing (scaling exposure to predicted risk).

## Key Formula

The **one-step-ahead** forecast from GARCH(1,1):

$$\hat{\sigma}_{t+1}^2 = \omega + \alpha \, \varepsilon_t^2 + \beta \, \sigma_t^2$$

The **$h$-step-ahead** forecast (for $h \geq 2$):

$$\hat{\sigma}_{t+h}^2 = \bar{\sigma}^2 + (\alpha + \beta)^{h-1}(\hat{\sigma}_{t+1}^2 - \bar{\sigma}^2)$$

where $\bar{\sigma}^2 = \omega / (1 - \alpha - \beta)$ is the unconditional variance. The cumulative variance over $h$ days (used for $h$-day VaR):

$$\hat{\sigma}_{t,h}^2 = \sum_{k=1}^{h} \hat{\sigma}_{t+k}^2 = h\bar{\sigma}^2 + \frac{1 - (\alpha+\beta)^h}{1 - (\alpha+\beta)}(\hat{\sigma}_{t+1}^2 - \bar{\sigma}^2)$$

## Example

A GARCH(1,1) model fitted to FTSE 100 daily returns has $\omega = 0.000002$, $\alpha = 0.08$, $\beta = 0.91$, giving persistence $\alpha + \beta = 0.99$ and long-run daily variance $\bar{\sigma}^2 = 0.0002$ (daily vol $\approx 1.41\%$).

After a volatile day where $\hat{\sigma}_{t+1}^2 = 0.0006$ (daily vol $\approx 2.45\%$), the 10-day-ahead forecast:

$$\hat{\sigma}_{t+10}^2 = 0.0002 + (0.99)^9 \times (0.0006 - 0.0002) = 0.0002 + 0.913 \times 0.0004 = 0.000565$$

Daily vol in 10 days: $\sqrt{0.000565} \approx 2.38\%$. The cumulative 10-day variance:

$$\hat{\sigma}_{t,10}^2 = 10 \times 0.0002 + \frac{1 - 0.99^{10}}{1 - 0.99} \times 0.0004 = 0.002 + 9.56 \times 0.0004 = 0.005824$$

The 10-day VaR at 99% confidence: $\sqrt{0.005824} \times 2.326 \approx 17.7\%$. Compare with the naive square-root rule: $2.45\% \times \sqrt{10} \times 2.326 \approx 18.0\%$ — the GARCH forecast is slightly lower because it accounts for mean reversion of volatility towards the long-run level.

## Remember

GARCH volatility forecasting is the bridge between the statistical model and real-world risk management. The multi-step forecast formula reveals a crucial insight: because $(\alpha + \beta) < 1$, all GARCH forecasts mean-revert towards the unconditional variance — after a volatility spike, the model predicts that volatility will gradually normalise, unlike the naive square-root-of-time rule which assumes constant volatility. This mean reversion makes GARCH forecasts more accurate than simple scaling for multi-day risk horizons. For quant developers, the practical applications include computing term-structure-aware VaR, generating forward volatility curves for option pricing when implied vol data is sparse, and calibrating volatility-scaling strategies that adjust position sizes based on predicted rather than realised risk.
