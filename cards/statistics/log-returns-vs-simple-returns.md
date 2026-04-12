# Log Returns vs Simple Returns

**Topic:** Statistics
**Tags:** returns, log returns, simple returns, time additivity, geometric brownian motion, lognormal
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **simple return** $R_t$ measures the percentage change in price over one period. The **log return** $r_t$ is the natural logarithm of the price ratio. They are interchangeable for small moves but diverge in multi-period analysis.

- **Simple return:** directly additive across assets in a portfolio (cross-sectionally additive).
- **Log return:** directly additive across time periods (time-additive), making multi-period analysis algebraically clean.

The two are linked by $r_t = \ln(1 + R_t)$, so for small $R_t$ they are approximately equal — the first-order Taylor expansion $\ln(1+x) \approx x$ explains the approximation.

## Key Formula

$$R_t = \frac{S_t - S_{t-1}}{S_{t-1}} = \frac{S_t}{S_{t-1}} - 1 \qquad r_t = \ln\!\left(\frac{S_t}{S_{t-1}}\right) = \ln S_t - \ln S_{t-1}$$

**Conversion:**

$$r_t = \ln(1 + R_t), \qquad R_t = e^{r_t} - 1, \qquad r_t \approx R_t \text{ for small } R_t$$

**Time additivity of log returns** (multi-period return from $t_1$ to $t_n$):

$$r_{t_1 \to t_n} = \sum_{i=1}^{n} r_i = \ln\!\left(\frac{S_{t_n}}{S_{t_1}}\right)$$

**Cross-sectional additivity of simple returns** (portfolio return):

$$R_P = \sum_{i} w_i R_i$$

**Under GBM**, log returns are normally distributed:

$$r_t = \ln\!\left(\frac{S_t}{S_0}\right) \sim \mathcal{N}\!\left(\!\left(\mu - \tfrac{1}{2}\sigma^2\right)t,\; \sigma^2 t\right)$$

so simple returns $R_t = e^{r_t} - 1$ are **lognormally** distributed.

## Example

Suppose an asset moves: $S_0 = 100 \to S_1 = 110 \to S_2 = 99$.

| Period | Simple return | Log return |
|--------|--------------|------------|
| 1 | $R_1 = 10\%$ | $r_1 = \ln(110/100) = 9.53\%$ |
| 2 | $R_2 = -10\%$ | $r_2 = \ln(99/110) = -10.54\%$ |
| 2-period | $R = (1.10)(0.90) - 1 = -1\%$ | $r = 9.53\% + (-10.54\%) = -1.01\%$ |

Log returns sum exactly; simple returns must be compounded ($1.10 \times 0.90 = 0.99$, not $0.10 + (-0.10)$). In portfolio attribution, however, the portfolio weight formula $R_P = \sum w_i R_i$ uses simple returns directly — log returns are not cross-sectionally additive.

## Remember

GBM assumes log returns are normally distributed, which makes simple returns **lognormal** — a convenient mathematical model. In practice, **stylised facts** violate this: empirical return distributions exhibit fat tails (excess kurtosis) and negative skewness, so the normality assumption understates the probability of large losses. Despite this, log returns remain the standard in time-series modelling and stochastic calculus because time additivity simplifies multi-period analysis and fits naturally into Itô's lemma. Portfolio attribution and performance measurement, however, stick to simple returns because the cross-sectional additivity $R_P = \sum w_i R_i$ holds exactly — mixing the two conventions is a common source of error.
