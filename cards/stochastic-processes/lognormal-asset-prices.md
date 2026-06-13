# Lognormal Asset Prices

**Topic:** Stochastic Processes
**Tags:** lognormal, asset prices, GBM, moments, conditional expectation, Black-Scholes
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Under the **lognormal asset price model**, the stock price at time $T$ is:

$$S_T = S_0 \exp\!\left(\left(\mu - \tfrac{1}{2}\sigma^2\right)T + \sigma\sqrt{T}\,Z\right), \qquad Z \sim N(0,1)$$

so $\ln S_T \sim N\!\bigl(\ln S_0 + (\mu - \tfrac{1}{2}\sigma^2)T,\; \sigma^2 T\bigr)$. The $-\tfrac{1}{2}\sigma^2$ Itô correction ensures the expected price grows at rate $\mu$, not at $\mu + \tfrac{1}{2}\sigma^2$: without it the model would overstate expected returns.

## Key Formula

**Moments of $S_T$** (using the moment-generating function of the normal):

$$E[S_T] = S_0\, e^{\mu T}, \qquad \text{Var}[S_T] = S_0^2 e^{2\mu T}\!\left(e^{\sigma^2 T} - 1\right)$$

**Conditional expectation** (the key building block of Black-Scholes):

$$E\!\left[S_T \,\middle|\, S_T > K\right] = \frac{S_0\, e^{\mu T}\, N(d_1)}{N(d_2)}$$

where $d_1 = \dfrac{\ln(S_0/K) + (\mu + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$ and $d_2 = d_1 - \sigma\sqrt{T}$.

Under the **risk-neutral measure** $\mathbb{Q}$, replace $\mu$ with $r$. The discounted call price then becomes:

$$C = e^{-rT} E^{\mathbb{Q}}\!\left[\max(S_T - K, 0)\right] = S_0 N(d_1) - K e^{-rT} N(d_2)$$

because $E^{\mathbb{Q}}[S_T \mathbf{1}_{S_T>K}] = S_0 e^{rT} N(d_1)$ and $E^{\mathbb{Q}}[\mathbf{1}_{S_T>K}] = N(d_2)$.

## Example

$S_0 = 100$, $\mu = 10\%$, $\sigma = 25\%$, $T = 2$ years.

$$E[S_2] = 100\,e^{0.20} \approx £122.14$$

$$\text{SD}[S_2] = 100\,e^{0.20}\sqrt{e^{0.0625 \times 2} - 1} \approx 122.14 \times 0.372 \approx £45.44$$

The wide standard deviation relative to the mean (37% of expected price) reflects the right skew of the lognormal: extreme upside moves are possible but the downside is bounded at zero. If $K = 120$:

$$d_1 = \frac{\ln(100/120) + (0.10 + 0.03125)(2)}{0.25\sqrt{2}} = \frac{-0.182 + 0.263}{0.354} \approx 0.228$$

$$d_2 \approx 0.228 - 0.354 = -0.126$$

$$\Pr^{\mathbb{Q}}(S_2 > 120) \approx N(-0.126) \approx 45.0\%$$

## Remember

The split between $N(d_1)$ and $N(d_2)$ in the Black-Scholes formula has a clean probabilistic interpretation: $N(d_2)$ is the risk-neutral probability of finishing in the money; $N(d_1)$ is the delta, which equals $N(d_2)$ adjusted upward by the conditional mean of $S_T$ given expiry in the money. The $-\tfrac{1}{2}\sigma^2$ correction that separates $d_1$ from $d_2$ is not a modelling choice — it is a mathematical consequence of applying Itô's lemma and using the lognormal MGF. Confusing arithmetic mean return ($\mu$) with geometric mean return ($\mu - \tfrac{1}{2}\sigma^2$) is a common source of error when back-of-envelope estimating long-horizon portfolio values.
