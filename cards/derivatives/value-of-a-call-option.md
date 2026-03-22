# Value of a Call Option

**Topic:** Derivatives
**Tags:** options, call option, intrinsic value, time value, payoff
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **value of a call option** is the price a holder pays for the right — but not the obligation — to buy an underlying asset at a fixed strike price $K$ by or at expiry. It decomposes into **intrinsic value** (the immediate exercise profit, if any) and **time value** (the premium reflecting the possibility that the option moves further into the money before expiry).

## Key Formula

At expiry, the call payoff is:

$$C_T = \max(S_T - K, \; 0)$$

Before expiry, the call value satisfies:

$$C = \underbrace{\max(S_0 - K, \; 0)}_{\text{intrinsic value}} \;+\; \underbrace{(C - \max(S_0 - K, \; 0))}_{\text{time value}}$$

Under Black–Scholes assumptions the closed-form price is:

$$C = S_0 \, N(d_1) - K e^{-rT} N(d_2)$$

where $d_1 = \dfrac{\ln(S_0 / K) + (r + \sigma^2/2)\,T}{\sigma\sqrt{T}}$ and $d_2 = d_1 - \sigma\sqrt{T}$.

## Example

A European call has $S_0 = £100$, $K = £95$, $r = 5\%$, $\sigma = 20\%$, $T = 0.25$ years.

**Intrinsic value** = $\max(100 - 95, 0) = £5$

**Black–Scholes price:**

$$d_1 = \frac{\ln(100/95) + (0.05 + 0.02) \times 0.25}{0.20 \times 0.5} = \frac{0.0513 + 0.0175}{0.10} = 0.688$$

$$d_2 = 0.688 - 0.10 = 0.588$$

$$C = 100 \times N(0.688) - 95 e^{-0.0125} \times N(0.588) \approx 100(0.754) - 93.82(0.722) \approx \textbf{£7.62}$$

**Time value** = £7.62 − £5.00 = **£2.62**

## Remember

The call's value is always at least its intrinsic value — the gap above intrinsic is the time value, which decays to zero at expiry (theta decay). In quantitative finance, decomposing an option into intrinsic and time value is essential for understanding how Greeks evolve: delta approaches 1 for deep in-the-money calls (all intrinsic, little time value), while at-the-money calls have maximal time value and the highest gamma and theta exposure.
