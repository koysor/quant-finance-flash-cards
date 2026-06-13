# Truncated Lognormal Distribution

**Topic:** Probability
**Tags:** truncated lognormal, conditional expectation, Black-Scholes, d1, d2, tail probability
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **truncated lognormal distribution** is the distribution of a lognormal random variable $S$ conditional on $S$ exceeding a threshold $K$. It arises directly in option pricing: the expected payoff of a call option is the expected value of $S_T$ on the event $\{S_T > K\}$, multiplied by the probability of that event. The two-term structure of the Black-Scholes formula — $S_0 N(d_1) - K e^{-rT} N(d_2)$ — corresponds exactly to these two quantities.

## Key Formula

Let $S_T \sim \text{Lognormal}$ with $\ln S_T \sim N(m, v^2)$ where $m = \ln S_0 + (r - \tfrac{1}{2}\sigma^2)T$ and $v = \sigma\sqrt{T}$.

**Tail probability** (the $N(d_2)$ term):

$$\Pr(S_T > K) = N(d_2), \qquad d_2 = \frac{m - \ln K}{v} = \frac{\ln(S_0/K) + (r - \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$

**Truncated mean** (the $N(d_1)$ term):

$$E[S_T \,\mathbf{1}_{S_T > K}] = e^{m + \tfrac{1}{2}v^2}\, N(d_1) = S_0 e^{rT}\, N(d_1)$$

where $d_1 = d_2 + v = d_2 + \sigma\sqrt{T}$.

**Conditional mean** of the truncated distribution:

$$E[S_T \mid S_T > K] = \frac{E[S_T \,\mathbf{1}_{S_T > K}]}{\Pr(S_T > K)} = S_0 e^{rT}\,\frac{N(d_1)}{N(d_2)}$$

The call price is then $C = e^{-rT}\!\bigl[E[S_T \mathbf{1}_{S_T>K}] - K\,\Pr(S_T > K)\bigr] = S_0 N(d_1) - Ke^{-rT}N(d_2)$.

## Example

$S_0 = 100$, $K = 105$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year.

$$d_2 = \frac{\ln(100/105) + (0.05 - 0.02)}{0.20} = \frac{-0.0488 + 0.03}{0.20} = -0.094$$

$$d_1 = -0.094 + 0.20 = 0.106$$

$$\Pr^{\mathbb{Q}}(S_1 > 105) = N(-0.094) \approx 46.2\%$$

$$E^{\mathbb{Q}}[S_1 \mid S_1 > 105] = 100\,e^{0.05} \times \frac{N(0.106)}{N(-0.094)} \approx 105.13 \times \frac{0.542}{0.462} \approx £123.3$$

If the call expires in the money (probability 46.2%), the stock is expected to be at £123.3 — well above the £105 strike — giving a risk-neutral expected payoff of £18.3, which is consistent with the Black-Scholes price of $\approx £8.02$ after discounting and weighting.

## Remember

The split between $d_1$ and $d_2$ has a clean financial interpretation that is often lost when Black-Scholes is presented as a formula to memorise: $N(d_2)$ is the risk-neutral probability that the call finishes in the money, and $N(d_1) = \Delta$ (the delta) is the probability-weighted conditional mean of the stock normalised by $S_0 e^{rT}$. The gap $d_1 - d_2 = \sigma\sqrt{T}$ exists because the lognormal distribution is right-skewed: when you condition on finishing in the money, the average stock price is higher than the median, and that convexity correction is exactly $\sigma\sqrt{T}$ in the exponent. Deep in-the-money calls have $d_1 \approx d_2 \approx \infty$, so $N(d_1) \approx N(d_2) \approx 1$ and delta approaches 1; far out-of-the-money calls have $d_1 \approx d_2 \approx -\infty$, so both probabilities go to zero.
