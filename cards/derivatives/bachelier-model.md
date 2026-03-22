# Bachelier Model

**Topic:** Derivatives
**Tags:** Bachelier, normal model, option pricing, interest rates, negative rates
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **Bachelier model** (1900) prices options under the assumption that the underlying follows arithmetic Brownian motion — that is, absolute (not proportional) price changes are normally distributed. Unlike Black-Scholes, which assumes lognormal prices and cannot handle negative values, the Bachelier model allows the underlying to go below zero. This makes it the standard pricing framework for interest rate options in a negative-rate environment, where the lognormal assumption breaks down entirely.

## Key Formula

Under Bachelier, the underlying evolves as:

$$dF = \sigma_n \, dW$$

where $F$ is the forward price and $\sigma_n$ is the **normal volatility** (quoted in absolute terms, e.g. basis points per annum).

The price of a European call on a forward:

$$C = (F - K) \, \Phi(d) + \sigma_n \sqrt{T} \, \phi(d)$$

where:

$$d = \frac{F - K}{\sigma_n \sqrt{T}}$$

$\Phi$ is the standard normal CDF and $\phi$ is the PDF. The corresponding put:

$$P = (K - F) \, \Phi(-d) + \sigma_n \sqrt{T} \, \phi(d)$$

## Example

A 1-year European call on a forward rate $F = -0.20\%$ with strike $K = 0.00\%$ and normal volatility $\sigma_n = 0.50\%$ (50 bps/year):

$$d = \frac{-0.0020 - 0}{0.0050 \times 1} = -0.40$$

$$C = (-0.0020) \times \Phi(-0.40) + 0.0050 \times \phi(-0.40)$$

$$= -0.0020 \times 0.3446 + 0.0050 \times 0.3683 = -0.000689 + 0.001842 = 0.00115$$

The call is worth 11.5 basis points, despite the forward being below the strike — the time value from normal diffusion gives the rate a meaningful chance of rising above zero.

## Remember

Louis Bachelier's 1900 thesis was the first mathematical model of financial markets, predating Black-Scholes by 73 years. After decades of obscurity, the Bachelier model returned to prominence when EUR and JPY interest rates turned negative after 2014, rendering the lognormal Black-Scholes formula undefined (you cannot take the log of a negative rate). Swaption and cap/floor markets now routinely quote normal (Bachelier) volatility alongside or instead of lognormal (Black) volatility. The key practical difference: normal vol is quoted in absolute terms (basis points), while Black vol is relative (percentage), so the two are not directly comparable without knowing the level of the underlying.
