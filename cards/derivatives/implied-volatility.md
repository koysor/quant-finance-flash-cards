# Implied Volatility

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** implied volatility, volatility smile, volatility skew, Black-Scholes, options
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

**Implied volatility** ($\sigma_{\text{impl}}$) is the value of volatility that, when substituted into the Black-Scholes formula, reproduces the observed market price of an option. It is the market's consensus estimate of future volatility embedded in the option price.

Because Black-Scholes has no closed-form inverse for $\sigma$, implied volatility is found numerically (e.g. Newton–Raphson iteration).

## Key Formula

Implied volatility $\hat{\sigma}$ solves:

$$C_{\text{market}} = C_{\text{BS}}\!\left(S_0,\, K,\, r,\, T,\, \hat{\sigma}\right)$$

A fast approximation (at-the-money, short expiry) is:

$$\hat{\sigma} \approx \frac{C}{S_0} \sqrt{\frac{2\pi}{T}}$$

**Vega** (the sensitivity of the option price to $\sigma$) drives the Newton–Raphson update:

$$\hat{\sigma}_{n+1} = \hat{\sigma}_n - \frac{C_{\text{BS}}(\hat{\sigma}_n) - C_{\text{market}}}{\mathcal{V}(\hat{\sigma}_n)}, \qquad \mathcal{V} = S_0 \sqrt{T} \, N'(d_1)$$

## Example

A call is trading at £12. Black-Scholes with $\sigma = 20\%$ gives £10. Vega $= 25$.

$$\hat{\sigma} \leftarrow 0.20 - \frac{10 - 12}{25} = 0.20 + 0.08 = 28\%$$

One Newton–Raphson step moves the implied volatility estimate from 20% to 28%.

## Remember

- If Black-Scholes assumptions held exactly, implied volatility would be **flat** across all strikes and maturities. In practice it forms a **volatility smile** (implied vol is higher for deep in- and out-of-the-money options) or a **volatility skew** (implied vol is higher for low strikes), reflecting fat tails and crash risk.
- Traders do not use Black-Scholes to price options — they use it as a **quoting convention**, expressing option prices in volatility terms so that different strikes and maturities can be compared on a common scale.
- The term structure of implied volatility (vol vs. maturity) and the **vol surface** ($\sigma_{\text{impl}}$ vs. strike and maturity) are key inputs to exotic option pricing.
