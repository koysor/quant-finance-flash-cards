# Hurst Exponent

**Topic:** Statistics
**Tags:** long memory, persistence, mean reversion, regime filter, rescaled range, self-similarity
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

The Hurst exponent $H$ measures the long-memory behaviour of a time series by the rate at which its dispersion grows with the observation interval. A value of one half corresponds to a random walk; below one half the series is anti-persistent and mean-reverting, above one half it is persistent and trending.

## Key Formula

Dispersion scales as a power law in the lag $\tau$:

$$\mathbb{E}\!\left[\lvert X_{t+\tau} - X_t\rvert^2\right] \propto \tau^{2H}$$

so $H$ is the slope of a log-log regression:

$$\ln\left(\mathrm{Var}\left[X_{t+\tau} - X_t\right]\right) = 2H\ln\tau + c$$

| $H$ | Behaviour | Increments |
|---|---|---|
| $0 < H < 0.5$ | anti-persistent, mean-reverting | negatively correlated |
| $H = 0.5$ | random walk | independent |
| $0.5 < H < 1$ | persistent, trending | positively correlated |

The Hurst exponent relates directly to the variance ratio, since both measure how variance accumulates: $VR(q) = q^{2H-1}$.

## Example

Regress log variance of differences against log lag for a spread series, over lags 2 to 100 days, and obtain a slope of $0.74$.

$$H = \frac{0.74}{2} = 0.37$$

Since $H = 0.37 < 0.5$, the spread is anti-persistent — consistent with a mean-reverting pair. The cross-check against the variance ratio at $q = 5$:

$$VR(5) = 5^{2(0.37)-1} = 5^{-0.26} = 0.66$$

close to the 0.70 a direct variance-ratio computation would give, confirming the two filters agree.

## Remember

Hurst is used on a desk as a **regime gate on a mean-reversion strategy**, computed on a rolling window and required to sit below roughly $0.5 - \delta$ before Bollinger or Z-score entries are allowed to fire. The calibration trade-off is unavoidable and worth stating explicitly in any report: a short window responds quickly but makes $\hat{H}_t$ flip around 0.5 on noise, while a long window gives stable confirmation but lags the regime shift that matters. Note also that $H$ describes the series you feed it, so the answer depends entirely on the input — raw equity prices sit near 0.5 by construction, whereas a cointegrating residual should sit well below it, and finding $H \approx 0.5$ on a supposed spread is evidence the cointegrating relationship has broken. The same exponent appears in rough volatility modelling, where realised volatility shows $H \approx 0.1$, far rougher than Brownian motion.
