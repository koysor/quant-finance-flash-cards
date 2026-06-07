# Parkinson Volatility

**Topic:** Volatility
**Tags:** parkinson volatility, high-low range, volatility estimator, efficiency, historical volatility
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

Parkinson volatility is a historical volatility estimator that uses each period's high and low prices rather than just the closing price. Because the high-low range captures price movement throughout the day — not just the net change from close to close — it is substantially more efficient than the close-to-close estimator, requiring fewer data points to achieve the same estimation accuracy for a given true volatility level.

## Key Formula

$$\sigma_P = \sqrt{\frac{1}{4n\ln 2} \sum_{i=1}^{n} \left(\ln\frac{H_i}{L_i}\right)^2}$$

where $H_i$ and $L_i$ are the high and low prices in period $i$, and $n$ is the number of periods. The factor $4\ln 2 \approx 2.773$ normalises the estimator so it is unbiased for a continuous GBM with no drift.

**Relative efficiency** compared to close-to-close: approximately $5\times$ — Parkinson achieves the same variance of estimate as close-to-close with roughly one-fifth the number of observations.

## Example

Five days of FTSE 100 data:

| Day | High | Low | $\ln(H/L)$ | $[\ln(H/L)]^2$ |
|-----|------|-----|------------|----------------|
| 1 | 7,620 | 7,510 | 0.01454 | 0.000211 |
| 2 | 7,580 | 7,430 | 0.01990 | 0.000396 |
| 3 | 7,560 | 7,500 | 0.00798 | 0.0000637 |
| 4 | 7,610 | 7,470 | 0.01856 | 0.000344 |
| 5 | 7,590 | 7,520 | 0.00928 | 0.0000861 |

Sum of squares $= 0.001101$

$$\sigma_P = \sqrt{\frac{0.001101}{4 \times 5 \times 0.6931}} = \sqrt{\frac{0.001101}{13.863}} = \sqrt{0.0000794} = 0.00891 \approx 0.89\%\text{ daily}$$

Annualised: $0.89\% \times \sqrt{252} \approx 14.1\%$ — identical to the close-to-close estimate but computed using high-low ranges rather than closing returns.

## Remember

Parkinson volatility is the workhorse high-frequency volatility estimator used by risk managers who have access to intraday OHLC data but not tick-by-tick prices. It is unbiased only when prices follow a pure diffusion with no drift and no overnight gaps — in practice, gap openings (common around earnings or macro announcements) cause the estimator to understate true volatility by missing the gap move. For this reason, the **Yang-Zhang** estimator extends Parkinson by explicitly accounting for overnight returns. In derivatives market-making, Parkinson vol computed over 20–30 days is the standard input for checking whether implied volatility is rich or cheap relative to the intraday realised movement of the underlying.

