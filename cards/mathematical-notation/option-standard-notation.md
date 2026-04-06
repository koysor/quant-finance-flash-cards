# Option Pricing Standard Notation

**Topic:** Mathematical Notation
**Tags:** notation, options, Black-Scholes, S K T r sigma, d1 d2, call put
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

The Black-Scholes framework introduced a standard notation that is now universal across derivatives. Every practitioner and textbook uses these symbols without definition:

| Symbol | Name | Typical units |
|---|---|---|
| $S$ or $S_t$ | Current (spot) price of the underlying | Currency per share |
| $K$ | Strike price | Currency per share |
| $T$ | Option maturity (time to expiry from inception) | Years |
| $t$ | Current time | Years |
| $\tau = T - t$ | Time to maturity | Years |
| $r$ | Continuously compounded risk-free rate | Per year |
| $\sigma$ | Implied or realised volatility (annualised) | Per year$^{1/2}$ |
| $C$ | Call option price | Currency |
| $P$ | Put option price | Currency |
| $q$ | Continuous dividend yield | Per year |
| $F$ or $F_{t,T}$ | Forward price: $Se^{(r-q)(T-t)}$ | Currency per share |

## Key Formula

**Black-Scholes $d_1$ and $d_2$:**

$$d_1 = \frac{\ln(S/K) + (r + \tfrac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}, \qquad d_2 = d_1 - \sigma\sqrt{\tau}$$

**Call and put prices:**

$$C = S N(d_1) - K e^{-r\tau} N(d_2)$$

$$P = K e^{-r\tau} N(-d_2) - S N(-d_1)$$

**Put-call parity:**

$$C - P = S e^{-q\tau} - K e^{-r\tau}$$

## Example

For a European call with $S = 100$, $K = 105$, $\tau = 0.5$, $r = 0.05$, $\sigma = 0.20$:

$$d_1 = \frac{\ln(100/105) + (0.05 + 0.02) \times 0.5}{0.20 \times \sqrt{0.5}} = \frac{-0.0488 + 0.035}{0.1414} \approx -0.098$$

$$d_2 \approx -0.098 - 0.1414 \approx -0.239$$

$$C = 100 \cdot N(-0.098) - 105 e^{-0.025} \cdot N(-0.239) \approx \textbf{£5.67}$$

## Remember

The choice of $\tau = T - t$ rather than $T$ alone is significant: $T$ is the fixed expiry date on the contract, but $\tau$ is the **remaining time**, which shrinks as the option ages. Theta ($\Theta$) — the time decay of the option — is the derivative with respect to $t$ (not $\tau$), so $\Theta = -\partial C/\partial t = +\partial C/\partial \tau \times (-1)$. In risk systems, options are stored with fixed $T$ and current $t$ is updated daily, which automatically updates $\tau$ — mixing up $T$ and $\tau$ is one of the most common source of sign errors in options risk reports.
