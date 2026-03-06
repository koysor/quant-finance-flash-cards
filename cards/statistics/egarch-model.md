# EGARCH Model

**Topic:** Statistics
**Tags:** EGARCH, leverage effect, asymmetric volatility, conditional variance, time series
**Author:** Claude Opus 4.6

---

## Definition

The **Exponential GARCH (EGARCH)** model, introduced by Nelson (1991), extends GARCH to capture the **leverage effect** — the empirical observation that negative return shocks increase volatility more than positive shocks of the same magnitude. It models the logarithm of the conditional variance, which guarantees positivity without requiring non-negativity constraints on the parameters.

## Key Formula

**EGARCH(1,1):**

$$\ln(\sigma_t^2) = \omega + \beta \ln(\sigma_{t-1}^2) + \gamma \frac{\varepsilon_{t-1}}{\sigma_{t-1}} + \alpha \left[\frac{|\varepsilon_{t-1}|}{\sigma_{t-1}} - \sqrt{\frac{2}{\pi}}\right]$$

where:
- $\gamma$ captures the **leverage effect** (typically $\gamma < 0$ for equities)
- $\alpha$ captures the magnitude effect (how the size of the shock affects volatility)
- $\beta$ captures persistence
- The standardised residual $z_{t-1} = \varepsilon_{t-1} / \sigma_{t-1}$ ensures scale-free responses

When $\gamma < 0$: a negative shock ($z < 0$) increases $\ln(\sigma^2)$ by $-\gamma|z| + \alpha(|z| - \sqrt{2/\pi})$, while a positive shock of the same size increases it by only $\gamma|z| + \alpha(|z| - \sqrt{2/\pi})$.

## Example

An EGARCH(1,1) with $\omega = -0.15$, $\alpha = 0.10$, $\beta = 0.98$, $\gamma = -0.08$.

Yesterday's log-variance: $\ln(\sigma_{t-1}^2) = -7.8$ (so $\sigma_{t-1} \approx 2.0\%$).

**Negative shock:** $z_{t-1} = -2.5$ (a 2.5-sigma drop):

$$\ln(\sigma_t^2) = -0.15 + 0.98 \times (-7.8) + (-0.08)(-2.5) + 0.10(2.5 - 0.798)$$

$$= -0.15 - 7.644 + 0.20 + 0.170 = -7.424, \quad \sigma_t \approx 2.42\%$$

**Positive shock:** $z_{t-1} = +2.5$:

$$\ln(\sigma_t^2) = -0.15 + 0.98 \times (-7.8) + (-0.08)(2.5) + 0.10(2.5 - 0.798)$$

$$= -0.15 - 7.644 - 0.20 + 0.170 = -7.824, \quad \sigma_t \approx 1.98\%$$

The same-sized shock increases volatility to 2.42% when negative but only to 1.98% when positive — the leverage effect in action.

## Remember

The leverage effect is one of the most robust stylised facts in equity markets: when stock prices fall, volatility rises disproportionately. The standard explanation is that falling prices increase a firm's financial leverage (debt-to-equity ratio), making the equity riskier. EGARCH captures this asymmetry that symmetric GARCH misses, producing more accurate volatility forecasts during market sell-offs. This matters directly for option pricing — the implied volatility skew reflects precisely this asymmetry, and traders who ignore it systematically misprice downside protection.
