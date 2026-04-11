# Central Moments

**Topic:** Probability
**Tags:** central moments, variance, skewness, kurtosis, higher moments, distribution shape
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **$k$-th central moment** of a random variable $X$ measures the expected value of the $k$-th power of the deviation from the mean. Central moments describe the shape of a distribution around its centre, independently of location.

$$\mu_k = E\!\left[(X - \mu)^k\right], \qquad \mu = E[X]$$

## Key Formula

| Order | Central moment | Name | Value for $\mathcal{N}(\mu,\sigma^2)$ |
|---|---|---|---|
| $k=1$ | $\mu_1 = E[X-\mu] = 0$ | Always zero | 0 |
| $k=2$ | $\mu_2 = E[(X-\mu)^2] = \sigma^2$ | **Variance** | $\sigma^2$ |
| $k=3$ | $\mu_3 = E[(X-\mu)^3]$ | Third central moment | 0 |
| $k=4$ | $\mu_4 = E[(X-\mu)^4]$ | Fourth central moment | $3\sigma^4$ |

**Standardised central moments** (scale-free):

$$\tilde{\mu}_k = \frac{\mu_k}{\sigma^k}, \qquad \tilde{\mu}_3 = \text{skewness} = \gamma_1, \qquad \tilde{\mu}_4 = \text{kurtosis} = \gamma_2$$

**Computing from raw moments:**

$$\mu_2 = \mu_2' - (\mu_1')^2, \qquad \mu_3 = \mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3$$

where $\mu_k' = E[X^k]$ are raw moments.

## Example

For daily equity returns: suppose $\mu = 0.05\%$, $\sigma = 1.5\%$. The second central moment is $\mu_2 = (0.015)^2 = 2.25 \times 10^{-4}$.

Empirically, $\mu_3 < 0$ (negative skewness — large falls are more common than large rises) and $\mu_4 > 3\sigma^4$ (positive excess kurtosis — fat tails). Plugging into $\tilde{\mu}_3 = \mu_3/\sigma^3$ and $\tilde{\mu}_4 = \mu_4/\sigma^4$ gives the standardised shape statistics used in the Jarque-Bera test.

## Remember

Central moments are the building blocks of all distribution shape statistics. The second ($\sigma^2$) measures spread; the standardised third (skewness) measures asymmetry; the standardised fourth (kurtosis) measures tail weight. In a normal distribution all odd central moments are zero and $\mu_4 = 3\sigma^4$ — any departure from these values signals non-normality and means that VaR computed assuming normality will be inaccurate.
