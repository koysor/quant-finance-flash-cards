# Skewness

**Topic:** Statistics
**Tags:** skewness, asymmetry, distributions, moments, returns, risk
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

Skewness is the third standardised moment of a distribution, measuring the degree of asymmetry about the mean. A distribution with negative skew has a longer left tail (more extreme losses), a distribution with positive skew has a longer right tail, and a symmetric distribution has zero skewness.

## Key Formula

The sample skewness for $n$ observations with mean $\bar{x}$ and standard deviation $s$ is:

$$\text{Skewness} = \frac{n}{(n-1)(n-2)} \sum_{i=1}^{n} \left( \frac{x_i - \bar{x}}{s} \right)^3$$

For a random variable $X$ with mean $\mu$ and standard deviation $\sigma$, the population skewness is:

$$\gamma_1 = E\!\left[\left(\frac{X - \mu}{\sigma}\right)^3\right]$$

## Example

Five daily returns (in %): $-3.2,\; -0.5,\; 0.1,\; 0.4,\; 0.8$.

Mean $\bar{x} = -0.48$, standard deviation $s = 1.58$.

Standardised cubes: $(-1.72)^3 + (-0.01)^3 + (0.37)^3 + (0.56)^3 + (0.81)^3$
$= -5.09 + 0.00 + 0.05 + 0.18 + 0.53 = -4.33$

Skewness $= \frac{5}{4 \times 3} \times (-4.33) = -1.80$.

The large negative value confirms the distribution is left-skewed: one extreme loss dominates.

## Remember

Equity returns typically exhibit negative skewness -- markets crash suddenly but rally gradually. This means the normal distribution, which has zero skewness, systematically underestimates the probability of large losses. Risk managers who ignore skewness will understate Value at Risk in the left tail, and option traders observe this effect directly as the implied volatility skew, where out-of-the-money puts are priced higher than symmetric models would suggest.
