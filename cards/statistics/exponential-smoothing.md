# Exponential Smoothing

**Topic:** Statistics
**Tags:** exponential smoothing, ewma, forecasting, time series, holt-winters, state-space model
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Exponential smoothing is a forecasting method that assigns geometrically decreasing weights to past observations: the most recent observation receives weight $\alpha$, the next most recent $(1-\alpha)\alpha$, and so on. It is equivalent to an ARIMA(0,1,1) model and is the basis of EWMA volatility in risk management. Extensions (Holt, Holt-Winters) add trend and seasonal components.

## Key Formula

**Simple Exponential Smoothing (SES)** — level only:

$$\hat{x}_{t+1} = \alpha\, x_t + (1-\alpha)\, \hat{x}_t = \alpha \sum_{k=0}^{t-1} (1-\alpha)^k x_{t-k}$$

where $\alpha \in (0,1)$ is the smoothing parameter. High $\alpha$: fast adaptation (tracks data closely). Low $\alpha$: smooth, slowly adjusting forecast.

**EWMA volatility** (RiskMetrics, $\lambda = 1 - \alpha$):

$$\hat{\sigma}_t^2 = (1-\lambda)\, r_{t-1}^2 + \lambda\, \hat{\sigma}_{t-1}^2, \qquad \lambda = 0.94$$

Effective memory: $\frac{1}{1-\lambda} \approx 17$ trading days at $\lambda = 0.94$.

**Holt's method** — level $\ell_t$ plus trend $b_t$:

$$\ell_t = \alpha\, x_t + (1-\alpha)(\ell_{t-1} + b_{t-1}), \quad b_t = \beta(\ell_t - \ell_{t-1}) + (1-\beta) b_{t-1}$$
$$\hat{x}_{t+h} = \ell_t + h\, b_t$$

## Example

Monthly equity fund flows (£bn): Jan 2.1, Feb 1.9, Mar 2.4, Apr 2.0. Forecast May with $\alpha = 0.3$:

$$\hat{x}_{\text{Mar}} = 0.3 \times 1.9 + 0.7 \times 2.10 = 2.04$$
$$\hat{x}_{\text{Apr}} = 0.3 \times 2.4 + 0.7 \times 2.04 = 2.15$$
$$\hat{x}_{\text{May}} = 0.3 \times 2.0 + 0.7 \times 2.15 = 2.11$$

The forecast places 30% weight on April's observation and 70% on the smoothed history — dampening the Mar spike while not ignoring it entirely.

## Remember

EWMA volatility is exponential smoothing applied to squared returns, and is the foundation of **RiskMetrics** (J.P. Morgan, 1994), the first widely adopted industry standard for daily VaR. RiskMetrics uses $\lambda = 0.94$ for daily series and $\lambda = 0.97$ for monthly series. Its key advantage over rolling-window volatility is the elimination of the **ghost effect**: when a large return drops out of a fixed window, measured volatility jumps discontinuously even though nothing has changed today. EWMA lets past shocks decay smoothly, producing a more realistic volatility path — but at the cost of under-counting persistent volatility clustering, which is why GARCH models (which estimate $\lambda$ optimally) generally outperform EWMA in formal forecasting comparisons.
