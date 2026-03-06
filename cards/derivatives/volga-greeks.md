# Volga (Greeks)

**Topic:** Derivatives
**Tags:** volga, vomma, Greeks, sensitivity, options, volatility
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Volga** (also called **Vomma**) is the second-order Greek that measures the rate of change of Vega with respect to a change in implied volatility. Formally, $\text{Volga} = \partial^2 V / \partial \sigma^2 = \partial \nu / \partial \sigma$. It captures the convexity of the option price as a function of volatility — just as Gamma captures convexity with respect to the underlying price.

## Key Formula

For European options under Black-Scholes:

$$\text{Volga} = \nu \cdot \frac{d_1 \, d_2}{\sigma}$$

where $\nu = S \, N'(d_1)\sqrt{T}$ is Vega and

$$d_1 = \frac{\ln(S/K) + (r + \tfrac{\sigma^2}{2})T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

Key properties:

- Volga is **positive** for out-of-the-money and in-the-money options (where $d_1$ and $d_2$ share the same sign).
- Volga is **near zero** for at-the-money options (where $d_1 \approx -d_2$, so $d_1 d_2 < 0$).
- OTM options have positive Volga — their Vega increases as volatility rises, creating a convex payoff in volatility space.

## Example

A European call has $S = 100$, $K = 110$ (OTM), $\sigma = 25\%$, $T = 0.5$ years, $r = 5\%$.

$$d_1 = \frac{\ln(100/110) + (0.05 + 0.03125)(0.5)}{0.25\sqrt{0.5}} = \frac{-0.09531 + 0.04063}{0.17678} = -0.3094$$

$$d_2 = -0.3094 - 0.17678 = -0.4862$$

$$\nu = 100 \times N'(-0.3094) \times \sqrt{0.5} \approx 100 \times 0.3807 \times 0.7071 = 26.92$$

$$\text{Volga} = 26.92 \times \frac{(-0.3094)(-0.4862)}{0.25} = 26.92 \times 0.6019 = \mathbf{16.20}$$

If implied volatility rises from 25% to 26%, Vega itself increases by approximately $16.20 \times 0.01 = 0.162$. The option's sensitivity to further volatility moves grows — this is volatility convexity.

## Remember

Volga explains why out-of-the-money options trade at a premium to Black-Scholes fair value in practice. An OTM option has positive Volga, meaning it benefits disproportionately from large volatility moves. Since realised volatility exhibits jumps and clustering, traders are willing to pay extra for this convexity — and that premium manifests as the **volatility smile**. Exotic desks use Volga (alongside Vanna) in the **Vanna-Volga method** to adjust Black-Scholes prices for the smile, pricing vanilla options consistently with the observed market skew without a full stochastic volatility model.
