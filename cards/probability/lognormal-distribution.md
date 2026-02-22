# Lognormal Distribution

**Topic:** Probability
**Level:** A Level Mathematics
**Tags:** lognormal, distributions, asset prices, returns, probability

---

## Definition

A random variable $S$ follows a **lognormal distribution** if $\ln S$ is normally distributed. In finance, asset returns are modelled as normally distributed, which means asset prices themselves follow a lognormal distribution. This ensures prices are always positive.

## Key Formula

From the SDE $dS = \mu S \, dt + \sigma S \, dX$, applying Ito's Lemma gives:

$$d(\ln S) = \left(\mu - \tfrac{1}{2}\sigma^2\right) dt + \sigma \, dX$$

So $\ln S$ is normally distributed, and the price at time $T$ is:

$$S(T) = S(0) \exp\!\left(\left(\mu - \tfrac{1}{2}\sigma^2\right)T + \sigma \sqrt{T} \, Z\right)$$

where $Z \sim N(0, 1)$.

## Example

If $S(0) = 100$, $\mu = 0.10$, $\sigma = 0.20$, and $T = 1$ year:

$$\ln S(1) \sim N\!\left(\ln 100 + (0.10 - 0.02) \times 1, \; 0.04\right)$$

The expected price is $100 \times e^{0.10} \approx £110.52$, but the distribution is right-skewed — the median is lower than the mean because of the $-\tfrac{1}{2}\sigma^2$ correction.

## Remember

The lognormal model is why Black-Scholes uses $N(d_1)$ and $N(d_2)$ — these are probabilities computed from the normal distribution of log-prices. The $-\tfrac{1}{2}\sigma^2$ drift correction is the convexity adjustment that distinguishes the arithmetic mean return from the geometric (compounded) return.
