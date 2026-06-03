# Convexity Bias

**Topic:** Fixed Income
**Tags:** convexity bias, jensen's inequality, forward rates, expected spot rates, term premium, futures
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Convexity bias is the systematic wedge between a forward interest rate and the expected future spot rate, arising from Jensen's inequality applied to the convex bond price-yield relationship; it causes long-dated forward rates to exceed expected future short rates and makes term premium estimates from DNS models appear smaller than the true risk compensation.

## Key Formula

For a zero-coupon bond, price is a convex function of yield: $P = e^{-y\tau}$. By Jensen's inequality $\mathbb{E}[f(X)] \geq f(\mathbb{E}[X])$ for convex $f$, the forward rate exceeds the expected future short rate. The convexity bias on a forward rate starting at time $T$ for tenor $\delta$ is approximately:

$$f(0, T, T+\delta) - \mathbb{E}_0[r_T] \approx \frac{1}{2}\sigma_r^2\, T\, \delta$$

where $\sigma_r$ is the short rate volatility. The bias grows quadratically with maturity $T$ and linearly with rate variance $\sigma_r^2$.

## Example

Short rate volatility $\sigma_r = 1\%$ (100bp annualised). Convexity bias on the 10-year forward rate (1-year tenor): $\frac{1}{2}(0.01)^2 \times 10 \times 1 = 5\text{bp}$. For $\sigma_r = 2\%$, the same forward carries 20bp of bias. Over a 30-year forward curve, the cumulative bias at the long end reaches 50-100bp depending on volatility regime. A DNS model that ignores this adjustment will attribute these 50-100bp to the term premium — producing a "term premium" estimate that is 50-100bp smaller than the true risk compensation.

## Remember

Convexity bias explains why SOFR futures prices differ from OIS-implied forward rates at long maturities: futures settle to the arithmetic average of overnight rates (no convexity), while OIS forward rates are priced from bonds whose convexity creates Jensen's inequality bias. At 5-year horizons this difference is roughly 10-20bp — small in isolation but large enough to matter for term premium estimation. A DNS model that attributes all of this bias to the term premium will systematically understate the risk premium demanded by long-bond investors, potentially misleading central banks about the true cost of long-duration financing.
