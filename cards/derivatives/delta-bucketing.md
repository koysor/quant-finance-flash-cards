# Delta Bucketing

**Topic:** Derivatives
**Tags:** delta bucket, hedging effectiveness, moneyness, regression, options book, sample size
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

Delta bucketing groups option observations by Black-Scholes delta and by maturity before any statistic is estimated or reported. It replaces strike as the grouping variable because a delta band automatically rescales with volatility and time to expiry, keeping each bucket economically comparable across the whole surface.

## Key Formula

Observations are assigned to a two-dimensional grid of buckets:

$$\text{bucket}(i) = \left(\left\lfloor \frac{\lvert \delta_{BS,i}\rvert}{0.1} \right\rfloor,\ \tau\text{-band}\right)$$

with typical bands $1$–$2$ months and $5$–$6$ months, and the range restricted to $0.1 < \lvert\delta_{BS}\rvert < 0.9$.

Delta is the natural coordinate because it is a monotone function of standardised moneyness:

$$\delta_{BS} = N(d_1), \qquad d_1 = \frac{\ln(S/K) + (r + \tfrac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$$

so a fixed delta band corresponds to a strike width that scales with $\sigma\sqrt{\tau}$ — narrow for a one-week option, wide for a one-year option.

Within each bucket a separate regression is fitted, for example the Hull-White minimum-variance specification:

$$\Delta f - \delta_{BS}\Delta S = \frac{\mathcal{V}_{BS}}{S\sqrt{\tau}}\left(a + b\,\delta_{BS} + c\,\delta_{BS}^2\right)\Delta S + \varepsilon$$

## Example

A one-year SPX sample of 42,000 daily option observations, restricted to two maturity bands:

| $\lvert\delta_{BS}\rvert$ | 1–2M count | 5–6M count | Share of squared error |
|---|---|---|---|
| 0.1–0.3 | 6,400 | 3,100 | 11% |
| 0.3–0.5 | 5,900 | 2,800 | 27% |
| 0.5–0.7 | 5,700 | 2,700 | 38% |
| 0.7–0.9 | 4,300 | 2,100 | 24% |

Three regression coefficients fitted on the smallest bucket's 2,100 points is comfortable; splitting the same data into twenty finer buckets would leave a few hundred points each and the estimates of $a$, $b$ and $c$ would jump around from month to month.

## Remember

Bucketing is what turns a hedging backtest into a usable result rather than a single misleading number. The squared-error mass is heavily concentrated near the forward — the 0.5–0.7 bucket above carries 38% of it on 20% of the observations — so an aggregate effectiveness statistic is essentially a report on at-the-money options, and a strategy that improves the wings dramatically can still show zero blended gain. Reporting by bucket also exposes where a model breaks: a surface-derived delta typically helps out-of-the-money, where the smile slope is steep, and hurts near-the-money, where it is nearly flat and the correction is mostly noise. The tension in choosing bucket width is standard: narrow buckets capture the delta-dependence of the correction but leave too few observations to estimate it stably, which is why practitioners keep the bucket coarse and let the quadratic in $\delta_{BS}$ do the interpolating within it.
