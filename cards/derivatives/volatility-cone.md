# Volatility Cone

**Topic:** Derivatives
**Tags:** volatility cone, realised volatility, percentile, rich-cheap, options, historical
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **volatility cone** is a visualisation that plots the percentile range of historical realised volatility across multiple measurement windows (e.g. 10-day, 30-day, 60-day, 90-day). For each window length, the cone shows statistics such as the minimum, 25th percentile, median, 75th percentile, and maximum of past realised volatility. By overlaying the current implied volatility term structure on the cone, traders can assess whether options at each maturity are cheap or expensive relative to history.

## Key Formula

For a given window length $n$ days, compute rolling realised volatility over the historical sample:

$$\sigma_{\text{real},t}^{(n)} = \sqrt{\frac{252}{n} \sum_{i=0}^{n-1} r_{t-i}^2}$$

Then calculate percentiles across all dates $t$:

$$P_q^{(n)} = \text{quantile}_q\!\left(\left\{\sigma_{\text{real},t}^{(n)}\right\}_{t}\right)$$

The cone plots $P_{25}^{(n)}$, $P_{50}^{(n)}$, $P_{75}^{(n)}$ (and optionally min/max) against $n$ on the x-axis. Current implied vol for maturity $\approx n$ days is then compared against these bands.

## Example

A trader constructs a volatility cone for the FTSE 100 using 5 years of data:

| Window | Min | 25th | Median | 75th | Max | Current IV |
|---|---|---|---|---|---|---|
| 30-day | 7% | 10% | 13% | 18% | 45% | 20% |
| 60-day | 8% | 11% | 14% | 17% | 38% | 18% |
| 90-day | 9% | 12% | 14% | 17% | 35% | 17% |

The 30-day implied vol (20%) sits above the 75th percentile (18%), suggesting 1-month options are **rich** relative to history. The 90-day implied vol (17%) is right at the 75th percentile — still elevated but less extreme. The trader might sell 1-month straddles and buy 3-month straddles to exploit the relative richness.

## Remember

The volatility cone is one of the simplest and most practical tools on a vol trading desk. It answers the question "is implied vol high or low?" not in absolute terms but relative to the historical distribution of realised volatility at each horizon. The cone shape arises because short-window realised vol is more dispersed than long-window vol (extreme readings are more likely over short periods), so the percentile bands narrow as the window lengthens. This is the same square-root-of-time scaling that governs volatility across horizons, manifesting in the funnel-like shape that gives the tool its name.
