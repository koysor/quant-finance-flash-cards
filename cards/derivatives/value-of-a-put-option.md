# Value of a Put Option

**Topic:** Derivatives
**Tags:** options, put option, intrinsic value, time value, payoff
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **value of a put option** is the price a holder pays for the right — but not the obligation — to sell an underlying asset at a fixed strike price $K$ by or at expiry. Like a call, it decomposes into **intrinsic value** (the immediate exercise profit, if any) and **time value** (the premium reflecting the chance the option moves further into the money before expiry).

## Key Formula

At expiry, the put payoff is:

$$P_T = \max(K - S_T, \; 0)$$

Before expiry, the put value satisfies:

$$P = \underbrace{\max(K - S_0, \; 0)}_{\text{intrinsic value}} \;+\; \underbrace{(P - \max(K - S_0, \; 0))}_{\text{time value}}$$

Under Black–Scholes assumptions the closed-form price is:

$$P = K e^{-rT} N(-d_2) - S_0 \, N(-d_1)$$

where $d_1 = \dfrac{\ln(S_0 / K) + (r + \sigma^2/2)\,T}{\sigma\sqrt{T}}$ and $d_2 = d_1 - \sigma\sqrt{T}$.

## Example

A European put has $S_0 = £100$, $K = £105$, $r = 5\%$, $\sigma = 20\%$, $T = 0.25$ years.

**Intrinsic value** = $\max(105 - 100, 0) = £5$

**Black–Scholes price:**

$$d_1 = \frac{\ln(100/105) + (0.05 + 0.02) \times 0.25}{0.20 \times 0.5} = \frac{-0.0488 + 0.0175}{0.10} = -0.313$$

$$d_2 = -0.313 - 0.10 = -0.413$$

$$P = 105 e^{-0.0125} \times N(0.413) - 100 \times N(0.313) \approx 103.69 \times 0.660 - 100 \times 0.623 \approx \textbf{£6.14}$$

**Time value** = £6.14 − £5.00 = **£1.14**

## Remember

A put option gains intrinsic value as the underlying falls below the strike — it acts as portfolio insurance. In quantitative finance, the put's value is linked to the call's via put–call parity ($P = C - S_0 + K e^{-rT}$), so mispricing one immediately creates an arbitrage in the other. Deep in-the-money puts have delta approaching $-1$ and nearly all intrinsic value, while at-the-money puts carry the most time value and are the most sensitive to changes in volatility (highest vega per unit of premium).
