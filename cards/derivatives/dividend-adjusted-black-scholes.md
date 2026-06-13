# Dividend-Adjusted Black-Scholes

**Topic:** Derivatives
**Tags:** dividends, Black-Scholes, option pricing, continuous dividend yield, discrete dividends, Merton 1973
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

When the underlying pays dividends, Black-Scholes must be adjusted: a continuous dividend yield $q$ is incorporated into the drift, while discrete dividends $D_i$ are subtracted from the current spot price before applying the standard formula.

## Key Formula

**Continuous dividend yield (Merton 1973):** replace $S$ with $S e^{-qT}$:

$$d_1 = \frac{\ln(S/K) + (r - q + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

$$C = S e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$

**Discrete dividends:** use $S^* = S - \sum_i D_i e^{-r t_i}$ in place of $S$.

## Example

$S = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$yr, $q = 3\%$. Without dividend: $d_1 = (0 + 0.07)/0.2 = 0.35$, $C \approx 10.45$. With $q = 3\%$: $d_1 = (0 + 0.04)/0.2 = 0.20$, $C \approx 9.12$ — lower because dividends reduce the expected stock price.

## Remember

For index options (FTSE 100, S&P 500), using a continuous dividend yield $q$ is standard and accurate. For single-stock equity options near known ex-dividend dates, discrete dividend adjustment matters most — models must subtract the present value of expected dividends from the spot before computing $d_1$. Failure to adjust can cause significant mispricing of deep in-the-money options and early exercise decisions for Americans.
