# d₁ and d₂ in Black–Scholes

**Topic:** Derivatives
**Tags:** Black-Scholes, d1, d2, options pricing, normal distribution, moneyness
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

In the Black–Scholes formula, $d_1$ and $d_2$ are the two arguments passed to the standard normal CDF $N(\cdot)$. They encode how far the current stock price is from the strike in standardised units, adjusted for drift and volatility over the option's remaining life. The difference between them is always exactly $\sigma\sqrt{T}$.

## Key Formula

$$d_1 = \frac{\ln(S_0 / K) + \left(r + \tfrac{\sigma^2}{2}\right)T}{\sigma\sqrt{T}}$$

$$d_2 = d_1 - \sigma\sqrt{T} = \frac{\ln(S_0 / K) + \left(r - \tfrac{\sigma^2}{2}\right)T}{\sigma\sqrt{T}}$$

**Interpretation:**

- $N(d_2)$ is the **risk-neutral probability** that the call expires in the money: $P^{\mathbb{Q}}(S_T > K)$
- $N(d_1)$ is the **delta** of the call — the hedge ratio — which equals the probability of finishing ITM under a measure where the stock is the numeraire
- The gap $d_1 - d_2 = \sigma\sqrt{T}$ reflects the **volatility adjustment** between the two probability measures

## Example

$S_0 = £100$, $K = £105$, $r = 4\%$, $\sigma = 25\%$, $T = 0.5$ years.

$$d_1 = \frac{\ln(100/105) + (0.04 + 0.03125) \times 0.5}{0.25 \times \sqrt{0.5}} = \frac{-0.0488 + 0.0356}{0.1768} = \frac{-0.0132}{0.1768} = -0.075$$

$$d_2 = -0.075 - 0.1768 = -0.252$$

$$N(d_1) = N(-0.075) = 0.470, \qquad N(d_2) = N(-0.252) = 0.401$$

The call delta is 0.47, and there is a 40.1% risk-neutral probability of the option expiring in the money.

## Remember

The numerator of $d_1$ and $d_2$ measures log-moneyness plus a drift term — when $S_0 = K$ and rates are zero, both reduce to $\pm\frac{1}{2}\sigma\sqrt{T}$, showing that even an ATM option has $d_1 > 0$ (delta above 0.5) because the lognormal distribution is right-skewed. The $\sigma^2/2$ term that distinguishes $d_1$ from $d_2$ is the same volatility drag that appears in geometric Brownian motion: $\mathbb{E}[\ln S_T] = \ln S_0 + (r - \sigma^2/2)T$. Understanding $d_1$ and $d_2$ is essential for building intuition about how moneyness, time, and volatility jointly determine option prices and hedge ratios.
