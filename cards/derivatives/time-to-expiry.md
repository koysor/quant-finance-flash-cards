# Time to Expiry

**Topic:** Derivatives
**Tags:** options, time to expiry, maturity, theta, Black-Scholes
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Time to expiry** ($T$) is the remaining time, measured in years, from the current date until an option contract expires. It is a key input to every option pricing model: the longer the time remaining, the greater the opportunity for the underlying to move favourably, and the higher the option's time value.

## Key Formula

In the Black–Scholes formula for a European call, $T$ appears in three places:

$$d_1 = \frac{\ln(S/K) + (r + \tfrac{1}{2}\sigma^2)\,T}{\sigma\sqrt{T}}$$

$$d_2 = d_1 - \sigma\sqrt{T}$$

$$C = S\,N(d_1) - K\,e^{-rT}\,N(d_2)$$

where $S$ is the spot price, $K$ is the strike, $r$ is the risk-free rate, $\sigma$ is volatility, and $N(\cdot)$ is the standard normal CDF.

Note the two distinct roles of $T$:

- **Square-root scaling** ($\sigma\sqrt{T}$) — uncertainty grows with the square root of time, not linearly.
- **Exponential discounting** ($e^{-rT}$) — the present value of the strike payment shrinks as $T$ increases.

## Example

A European call has $S = £100$, $K = £100$, $\sigma = 20\%$, $r = 5\%$.

**Converting calendar dates to $T$:** if today is 22 March 2026 and the option expires on 22 June 2026, there are 92 days remaining:

$$T = \frac{92}{365} \approx 0.2521 \text{ years}$$

Using Black–Scholes:

| $T$ (years) | $\sigma\sqrt{T}$ | Call price |
|---|---|---|
| 1.00 | 0.200 | £10.45 |
| 0.25 | 0.100 | £4.62 |
| 0.0625 | 0.050 | £2.09 |

Halving $T$ from 0.25 to 0.0625 reduces the call price by more than half, illustrating the square-root relationship: the option loses time value at an accelerating rate as expiry approaches.

## Remember

Time to expiry is the raw material that gives options their time value. In quantitative finance, $T$ enters pricing through $\sqrt{T}$, which means uncertainty (and therefore option value) grows more slowly than calendar time. This square-root scaling is why a one-year option does not cost four times as much as a three-month option — it costs roughly twice as much. Understanding this relationship is essential for structuring trades: buying longer-dated options gives more "bang per day" of theta, while selling short-dated options harvests the steepest part of the decay curve.
