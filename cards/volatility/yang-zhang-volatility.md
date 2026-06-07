# Yang-Zhang Volatility

**Topic:** Volatility
**Tags:** yang-zhang, ohlc volatility, overnight gaps, volatility estimator, efficiency, realised volatility
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

Yang-Zhang volatility is a historical volatility estimator that combines three components — overnight return variance, open-to-close variance, and Rogers-Satchell variance (which handles intraday drift) — to produce an estimator that is unbiased for volatility even in the presence of drift and overnight price gaps. It is the minimum-variance estimator within the OHLC (open, high, low, close) class and achieves roughly 7× the efficiency of the close-to-close estimator.

## Key Formula

$$\sigma_{YZ}^2 = \sigma_o^2 + k\,\sigma_c^2 + (1-k)\,\sigma_{RS}^2$$

where:
- $\sigma_o^2 = \dfrac{1}{n-1}\displaystyle\sum_{i=1}^n\!\left(\ln\dfrac{O_i}{C_{i-1}} - \overline{\ln\dfrac{O}{C}}\right)^2$ — overnight variance
- $\sigma_c^2 = \dfrac{1}{n-1}\displaystyle\sum_{i=1}^n\!\left(\ln\dfrac{C_i}{O_i} - \overline{\ln\dfrac{C}{O}}\right)^2$ — open-to-close variance
- $\sigma_{RS}^2 = \dfrac{1}{n}\displaystyle\sum_{i=1}^n\!\left[\ln\dfrac{H_i}{C_i}\ln\dfrac{H_i}{O_i} + \ln\dfrac{L_i}{C_i}\ln\dfrac{L_i}{O_i}\right]$ — Rogers-Satchell variance (drift-invariant)
- $k = \dfrac{0.34}{1.34 + (n+1)/(n-1)}$ — optimal weighting of open-to-close versus RS component

## Example

Using 5 days of S&P 500 OHLC data with non-trivial overnight gaps (e.g. post-earnings season), the three components might estimate:

- Overnight variance: $\sigma_o = 0.62\%$ daily (captures after-hours moves)
- Open-to-close variance: $\sigma_c = 0.71\%$ daily
- Rogers-Satchell: $\sigma_{RS} = 0.68\%$ daily (unbiased under drift)

Yang-Zhang combined (with $k \approx 0.13$): $\sigma_{YZ} \approx 0.70\%$ daily, annualised $\approx 11.1\%$. A close-to-close estimator using only the 5 closing returns might give $0.65\%$ or $0.79\%$ depending on the sequence of closes — the Yang-Zhang estimate is more stable and uses all available price information.

## Remember

Yang-Zhang volatility is the preferred OHLC estimator when overnight gaps are material — for example, in single-stock volatility estimation around earnings, dividends, or macro announcements, where the close-to-open return can be several percent. In FX markets, where trading is nearly 24 hours and overnight gaps are small, Parkinson or Rogers-Satchell suffices. The key advantage over Parkinson is that Yang-Zhang explicitly decomposes volatility into overnight and intraday components, allowing risk managers to diagnose whether elevated volatility is driven by after-hours information (corporate events) or by intraday price discovery (macro uncertainty) — a distinction that matters for options market-making and position sizing.

