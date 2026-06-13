# Garman-Kohlhagen Model

**Topic:** Derivatives
**Tags:** FX options, Garman-Kohlhagen, Black-Scholes, foreign exchange, two interest rates, interest rate parity
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Garman–Kohlhagen (1983) model prices European FX options by treating the foreign interest rate $r_f$ as a continuous dividend yield on the spot exchange rate $S$ (units of domestic per foreign currency).

## Key Formula

$$C = S_0 e^{-r_f T} N(d_1) - K e^{-r_d T} N(d_2)$$

$$P = K e^{-r_d T} N(-d_2) - S_0 e^{-r_f T} N(-d_1)$$

$$d_1 = \frac{\ln(S_0/K) + (r_d - r_f + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

where $r_d$ = domestic risk-free rate, $r_f$ = foreign risk-free rate, $\sigma$ = FX vol.

## Example

EUR/USD: $S = 1.10$, $K = 1.12$, $r_d = 5\%$ (USD), $r_f = 3\%$ (EUR), $\sigma = 10\%$, $T = 0.5$yr. $d_1 = (\ln(1.10/1.12) + (0.02 + 0.005) \times 0.5) / (0.1\sqrt{0.5}) = -0.09$. $C \approx 1.10 \times e^{-0.015} \times 0.464 - 1.12 \times e^{-0.025} \times 0.436 \approx 0.027$ (2.7 USD cents per EUR).

## Remember

Garman–Kohlhagen is Black–Scholes with $r_f$ substituted for the continuous dividend yield $q$ — this works because holding foreign currency earns $r_f$ continuously, exactly like a dividend-paying stock. Covered interest rate parity pins the forward to $F = S e^{(r_d - r_f)T}$, so pricing is equivalent to a Black formula on the FX forward.
