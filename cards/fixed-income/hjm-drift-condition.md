# HJM No-Arbitrage Drift Condition

**Topic:** Fixed Income
**Tags:** hjm, no-arbitrage, forward rate, drift condition, volatility, term structure
**Created:** 2026-06-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **HJM drift condition** states that, under the risk-neutral measure, the drift of every instantaneous forward rate is entirely determined by its own volatility and the volatilities of all shorter-maturity forward rates. You cannot freely choose both drift and volatility — the no-arbitrage constraint fixes one once the other is specified.

## Key Formula

**Single-factor drift condition:**

$$m(t, T) = \sigma(t, T) \int_{t}^{T} \sigma(t, s) \, ds$$

**Multi-factor generalisation** (with $N$ independent Brownian drivers):

$$m(t, T) = \sum_{i=1}^{N} \sigma_i(t, T) \int_{t}^{T} \sigma_i(t, s) \, ds$$

Here $\sigma_i(t, T)$ is the volatility of $f(t,T)$ due to the $i$-th factor, and the integral accumulates the total "covariance exposure" from $t$ to $T$.

## Example

Suppose $\sigma(t, T) = 0.01$ (1% flat volatility, constant in both arguments). Then for a 2-year forward rate starting today ($t = 0$, $T = 2$):

$$m(0, 2) = 0.01 \times \int_{0}^{2} 0.01 \, ds = 0.01 \times 0.02 = 0.0002$$

The risk-neutral drift is 2 basis points per year — a small positive convexity adjustment that grows with maturity and with the square of volatility.

## Remember

In practice, a quant building an HJM model for exotic interest rate derivatives only needs to calibrate the volatility surface $\sigma(t, T)$ to market cap/floor prices. The entire risk-neutral drift is then computed automatically from the formula — there are no additional free parameters. This is why HJM is said to "fit the initial curve by construction" and why over-specified short-rate models (where drift and volatility are independent) can produce arbitrage if not carefully constrained.
