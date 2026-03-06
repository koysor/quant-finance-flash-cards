# Theta (Greeks)

**Topic:** Derivatives
**Tags:** theta, Greeks, sensitivity, options, time decay
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Theta** ($\Theta$) is the Greek that measures the rate of change of an option's price with respect to the passage of time, holding all else constant. Formally, $\Theta = \partial V / \partial t$. It quantifies how much value an option loses each day purely from moving closer to expiry — commonly called **time decay**.

## Key Formula

For a European call under Black-Scholes:

$$\Theta_{\text{call}} = -\frac{S \, N'(d_1) \, \sigma}{2\sqrt{T}} - r K e^{-rT} N(d_2)$$

For a European put:

$$\Theta_{\text{put}} = -\frac{S \, N'(d_1) \, \sigma}{2\sqrt{T}} + r K e^{-rT} N(-d_2)$$

Key properties:

- Theta is **almost always negative** for long option positions — options lose value as time passes.
- ATM options have the largest Theta (most time value to lose).
- Theta accelerates as expiry approaches, roughly proportional to $1/\sqrt{T}$.
- Deep ITM European puts can have **positive Theta** because the present value of the strike payment increases as $T$ shrinks.

## Example

A European call has $S = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 0.25$ years.

Using $d_1 = 0.175$, $d_2 = 0.075$, $N'(0.175) \approx 0.3932$, $N(0.075) \approx 0.5299$:

$$\Theta = -\frac{100 \times 0.3932 \times 0.20}{2 \times 0.50} - 0.05 \times 100 \times e^{-0.0125} \times 0.5299$$

$$\Theta \approx -7.86 - 2.63 = \mathbf{-10.49} \text{ per year}$$

Per calendar day: $-10.49 / 365 \approx -£0.029$. The option loses about 3p per day from time decay alone.

## Remember

Theta is the price an option holder pays for the **optionality** — the right to benefit from favourable moves without obligation. It is inextricably linked to Gamma via the Black-Scholes PDE: for a delta-hedged portfolio, $\Theta + \tfrac{1}{2}\Gamma \sigma^2 S^2 = rV$. When realised volatility exceeds implied, the Gamma gains outweigh the Theta bleed, and the hedger profits. Options desks track their daily Theta as the "carry cost" of their book — it tells them how much the market must move each day just to break even.
