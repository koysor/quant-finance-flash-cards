# European Option Pricing

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** European options, options pricing, Black-Scholes, payoff, exercise
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

A **European option** can only be exercised at expiry. This restriction makes European options analytically tractable — the payoff is a single random variable at time $T$, so the price equals the discounted expected payoff under the risk-neutral measure. Closed-form solutions exist for standard European calls and puts under the Black-Scholes assumptions.

## Key Formula

The price of a European option is the discounted risk-neutral expectation of its payoff:

$$V_0 = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}[\text{payoff at } T]$$

For a European call with strike $K$:

$$C = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}[\max(S_T - K, \, 0)]$$

For a European put:

$$P = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}[\max(K - S_T, \, 0)]$$

Under Black-Scholes assumptions, these evaluate to the well-known closed forms involving $N(d_1)$ and $N(d_2)$.

## Example

A European put has strike $K = 50$, the stock is at $S_0 = 48$, $r = 4\%$, $\sigma = 30\%$, $T = 0.5$ years.

$$d_1 = \frac{\ln(48/50) + (0.04 + 0.045) \times 0.5}{0.30\sqrt{0.5}} = \frac{-0.0408 + 0.0425}{0.2121} = 0.008$$

$$d_2 = 0.008 - 0.2121 = -0.204$$

$$P = 50 e^{-0.02} N(0.204) - 48 N(-0.008) \approx 49.01 \times 0.581 - 48 \times 0.497 \approx \textbf{£4.66}$$

## Remember

European options are the building blocks of derivatives theory. Because the exercise decision is fixed (only at expiry), put-call parity holds exactly, the Black-Scholes formula applies directly, and Greeks have clean closed-form expressions. Most exchange-traded index options are European-style, making this pricing framework immediately practical.
