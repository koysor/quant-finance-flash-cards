# The Leverage Effect

**Topic:** Statistics
**Tags:** leverage effect, asymmetric volatility, skewness, GARCH, volatility smirk, stylised facts
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **leverage effect** is the empirical observation that negative returns increase future volatility more than positive returns of the same magnitude. For equity indices, the correlation between today's return and tomorrow's volatility is approximately $-0.7$.

The classical explanation (Black, 1976) is mechanical: when a stock price falls, the firm's equity value shrinks whilst debt remains fixed, so financial leverage rises. Greater leverage makes the equity riskier, and riskier equity means higher volatility. A secondary driver is the **risk premium channel** — falling prices trigger investor fear, causing a flight to safety that amplifies volatility further.

**Consequences for markets:**
- Produces **negative skewness** in return distributions: falling prices feed higher volatility, which amplifies the left tail
- Explains the **volatility smirk** in equity options: implied volatility is higher for downside strikes than upside strikes
- Represents a fundamental failure of Black-Scholes, which assumes constant, symmetric volatility
- Symmetric GARCH(1,1) cannot capture it; asymmetric models such as **GJR-GARCH** or **EGARCH** are required

## Key Formula

**GJR-GARCH(1,1)** captures the leverage effect via an indicator term:

$$\sigma_t^2 = \omega + \alpha \, \varepsilon_{t-1}^2 + \gamma \, \varepsilon_{t-1}^2 \cdot \mathbf{1}[\varepsilon_{t-1} < 0] + \beta \, \sigma_{t-1}^2$$

where:
- $\omega > 0$, $\alpha \geq 0$, $\beta \geq 0$
- $\mathbf{1}[\varepsilon_{t-1} < 0]$ is an indicator that equals 1 when the previous return shock was negative
- $\gamma > 0$ confirms the leverage effect: a negative shock raises volatility by an extra $\gamma \varepsilon_{t-1}^2$ compared with a positive shock of the same size

The **total** impact of a negative shock on conditional variance is $(\alpha + \gamma)\varepsilon_{t-1}^2$; for a positive shock it is only $\alpha \varepsilon_{t-1}^2$.

## Example

A GJR-GARCH(1,1) model has $\omega = 0.000001$, $\alpha = 0.06$, $\gamma = 0.08$, $\beta = 0.90$. Current conditional variance is $\sigma_{t-1}^2 = 0.0004$ (daily vol $= 2\%$). Yesterday's shock was $\varepsilon_{t-1} = -0.02$ (a $-2\%$ return).

$$\sigma_t^2 = 0.000001 + 0.06 \times (-0.02)^2 + 0.08 \times (-0.02)^2 + 0.90 \times 0.0004$$

$$= 0.000001 + 0.000024 + 0.000032 + 0.000360 = 0.000417$$

$$\sigma_t = \sqrt{0.000417} \approx 2.04\%$$

Had the shock been $+2\%$ (positive, so $\gamma$ term drops out):

$$\sigma_t^2 = 0.000001 + 0.06 \times (0.02)^2 + 0.90 \times 0.0004 = 0.000385, \quad \sigma_t \approx 1.96\%$$

The negative shock raises conditional volatility to 2.04% whilst the positive shock of equal magnitude leaves it at 1.96% — the leverage effect in action.

## Remember

The leverage effect explains the **volatility smirk** that equity options traders observe every day: out-of-the-money puts carry higher implied volatility than equivalent calls because the market knows that a sharp downward move will send realised volatility surging. A risk manager using symmetric GARCH or a Black-Scholes delta hedge will systematically underprice downside protection and underestimate tail risk in falling markets. Under FRTB's Internal Models Approach, firms must demonstrate that their volatility model captures asymmetric responses to negative shocks — a symmetric GARCH(1,1) will typically fail the profit-and-loss attribution test during stress periods precisely because it ignores the leverage effect.
