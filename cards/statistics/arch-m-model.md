# ARCH-M Model

**Topic:** Statistics
**Tags:** arch-m, risk premium, conditional volatility, garch, leverage effect, time series
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **ARCH-in-Mean (ARCH-M) model**, introduced by Engle, Lilien, and Robins (1987), extends GARCH by feeding the current conditional volatility $\sqrt{h_t}$ directly into the **mean equation**. This links expected returns to time-varying risk: when markets are more volatile, the model predicts a higher expected return as compensation — formalising the intuition behind the Capital Asset Pricing Model (CAPM) in a dynamic, time-varying setting.

The key addition is the risk premium parameter $\lambda$: every extra unit of conditional standard deviation raises the expected return by $\lambda$. A positive and statistically significant $\lambda$ confirms that investors require higher returns for bearing higher conditional risk — the central claim of mean-variance asset pricing.

The variance equation can take any GARCH family form; GJR-GARCH is commonly used because it also captures the **leverage effect** — the empirical finding that negative shocks raise volatility more than positive shocks of the same magnitude.

## Key Formula

**Mean equation (ARCH-M):**

$$\mu_t = \mu + \lambda \sqrt{h_t} + \Theta \varepsilon_{t-1}$$

where:
- $\mu$: unconditional mean return
- $\lambda$: risk premium — extra return per unit of conditional standard deviation
- $\sqrt{h_t}$: conditional standard deviation (today's volatility forecast)
- $\Theta \varepsilon_{t-1}$: optional MA(1) correction for short-run mean dynamics

**Variance equation (GJR-GARCH form):**

$$h_t = \omega + \alpha^+ \varepsilon_{t-1}^2 \,\mathbf{1}[\varepsilon_{t-1} \geq 0] + \alpha^- \varepsilon_{t-1}^2 \,\mathbf{1}[\varepsilon_{t-1} < 0] + \beta h_{t-1}$$

where $\alpha^-$ captures the extra variance impact of negative shocks (leverage effect).

**Empirical estimates:**

| Market | Sample | $\alpha^+$ | $\alpha^-$ | $\alpha^- / \alpha^+$ | $\lambda$ |
|---|---|---|---|---|---|
| S&P 100 | 1991–2000 | $\approx 0.02$ | $\approx 0.18$ | $\approx 9\times$ | positive |
| FTSE 100 | 2008–2025 | $\approx 0$ | $> 0$ | only $\alpha^-$ active | positive |

The S&P 100 result shows extreme asymmetry: negative shocks drive almost all variance dynamics. The FTSE 100 result shows $\alpha^+ \approx 0$ — positive shocks have virtually no impact on variance; only negative shocks matter.

## Example

Parameters: $\mu = 0.0003$, $\lambda = 0.15$, $\Theta = 0$, and $h_t = 0.0004$ (conditional variance).

Conditional standard deviation: $\sqrt{h_t} = \sqrt{0.0004} = 0.02$ (2% daily volatility).

$$\mu_t = 0.0003 + 0.15 \times 0.02 = 0.0003 + 0.003 = 0.0033$$

The model predicts a daily expected return of **0.33%** — ten times the unconditional mean — purely because today's conditional volatility is elevated. On a calm day with $\sqrt{h_t} = 0.005$ (0.5% vol):

$$\mu_t = 0.0003 + 0.15 \times 0.005 = 0.0003 + 0.00075 = 0.00105$$

Only **0.105%** expected return — the risk premium collapses with volatility.

## Remember

ARCH-M provides a formal, time-varying implementation of the CAPM risk-return trade-off. In practice: when the VIX spikes above 30, ARCH-M predicts meaningfully higher expected equity returns as compensation for the elevated risk. Risk managers and portfolio managers use this property to **dynamically adjust hurdle rates** — requiring higher expected alpha during turbulent regimes before deploying capital. The empirical finding that $\alpha^- \approx 9 \times \alpha^+$ on the S&P 100 is also a stark reminder that standard symmetric GARCH grossly underestimates the volatility impact of market sell-offs, with direct implications for VaR and Expected Shortfall models.
