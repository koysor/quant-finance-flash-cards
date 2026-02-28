# Volatility Smile

**Topic:** Derivatives
**Tags:** volatility smile, implied volatility, skew, Black-Scholes, options, strike price
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

The **volatility smile** is the empirical pattern where implied volatility varies with strike price for options of the same maturity. Black-Scholes assumes constant volatility across all strikes, but market prices reveal a U-shaped or skewed curve — higher implied volatilities for deep in-the-money and deep out-of-the-money options compared to at-the-money options.

## Key Formula

Implied volatility $\sigma_{\text{imp}}(K)$ is defined implicitly by:

$$C_{\text{market}}(K) = C_{\text{BS}}(S_0, K, r, T, \sigma_{\text{imp}})$$

If Black-Scholes were exact, $\sigma_{\text{imp}}$ would be the same for every strike $K$. In practice:

$$\sigma_{\text{imp}}(K_1) \neq \sigma_{\text{imp}}(K_2) \quad \text{for } K_1 \neq K_2$$

The **skew** is often quantified as the slope:

$$\text{Skew} = \sigma_{\text{imp}}(K_{\text{low}}) - \sigma_{\text{imp}}(K_{\text{ATM}})$$

For equity indices this is typically positive (higher vol for lower strikes), reflecting crash risk.

## Example

Consider three European call options on the same stock ($S_0 = 100$, $T = 0.5$, $r = 4\%$):

| Strike $K$ | Market Price | Implied Vol $\sigma_{\text{imp}}$ |
|---|---|---|
| 90 (ITM) | £14.20 | 24% |
| 100 (ATM) | £6.80 | 20% |
| 110 (OTM) | £2.50 | 22% |

Plotting these three points shows the characteristic U-shape: the ATM option has the lowest implied volatility, while both wings are elevated.

## Remember

The volatility smile is direct market evidence that asset returns are **not lognormally distributed** — real returns have fatter tails and negative skewness. Traders use the smile to price options more accurately than flat Black-Scholes would allow. Models like Heston (stochastic volatility) and Merton (jump-diffusion) were developed specifically to reproduce the smile from first principles, rather than simply fitting it strike by strike.
