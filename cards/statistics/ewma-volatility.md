# EWMA Volatility

**Topic:** Statistics
**Tags:** EWMA, volatility, time series, RiskMetrics, exponential weighting
**Author:** Claude Opus 4.6

---

## Definition

**Exponentially Weighted Moving Average (EWMA) volatility** estimates current volatility by giving more weight to recent observations and exponentially decaying weight to older ones. Unlike a simple rolling window, EWMA does not treat all past returns equally — it recognises that yesterday's market shock is more informative than one from six months ago.

## Key Formula

$$\sigma_t^2 = (1 - \lambda) \, r_{t-1}^2 + \lambda \, \sigma_{t-1}^2$$

where:
- $\sigma_t^2$ is the variance estimate at time $t$
- $r_{t-1}$ is the previous period's return (demeaned)
- $\lambda$ is the decay factor, $0 < \lambda < 1$

The **effective window length** is approximately $1 / (1 - \lambda)$. J.P. Morgan's RiskMetrics uses $\lambda = 0.94$ for daily data, giving an effective window of about 17 days.

Expanding the recursion shows exponential decay:

$$\sigma_t^2 = (1 - \lambda) \sum_{i=1}^{\infty} \lambda^{i-1} \, r_{t-i}^2$$

## Example

With $\lambda = 0.94$, yesterday's variance estimate $\sigma_{t-1}^2 = 0.0004$ (daily vol $\approx 2\%$), and yesterday's return $r_{t-1} = -0.035$ (a 3.5% drop):

$$\sigma_t^2 = 0.06 \times (-0.035)^2 + 0.94 \times 0.0004$$

$$= 0.06 \times 0.001225 + 0.000376 = 0.0000735 + 0.000376 = 0.000450$$

$$\sigma_t \approx 2.12\%$$

The large negative return has pushed the volatility estimate up from 2.0% to 2.12%.

## Remember

EWMA is the simplest adaptive volatility model and the foundation of J.P. Morgan's RiskMetrics system, which became the industry standard for VaR calculation in the 1990s. It can be viewed as a special case of GARCH(1,1) where $\alpha + \beta = 1$ (no mean reversion), meaning shocks persist indefinitely rather than decaying to a long-run level. This makes EWMA easier to implement but less realistic — in practice, volatility does revert to a long-run average. Despite this limitation, EWMA remains widely used for its simplicity, speed, and the fact that it requires calibrating only a single parameter $\lambda$.
