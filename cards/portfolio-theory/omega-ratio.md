# Omega Ratio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** omega ratio, return distribution, downside risk, threshold, performance, higher moments
**Author:** Claude Opus 4.6

---

## Definition

The Omega ratio is a performance measure that compares the probability-weighted gains above a chosen threshold to the probability-weighted losses below it. Unlike the Sharpe ratio, which relies only on mean and variance, the Omega ratio captures the entire return distribution — including skewness, kurtosis, and fat tails — making it a more complete measure for strategies with non-normal returns.

## Key Formula

$$\Omega(\tau) = \frac{\int_{\tau}^{\infty} [1 - F(r)]\, dr}{\int_{-\infty}^{\tau} F(r)\, dr}$$

where $F(r)$ is the cumulative distribution function of returns and $\tau$ is the threshold return (often set to the risk-free rate or zero).

For discrete returns, this simplifies to:

$$\Omega(\tau) = \frac{\displaystyle\sum_{R_t > \tau} (R_t - \tau)}{\displaystyle\sum_{R_t < \tau} (\tau - R_t)}$$

An Omega ratio greater than 1 means the weighted gains exceed the weighted losses at that threshold.

## Example

A fund has monthly returns (%): 5, $-2$, 8, $-1$, 3, $-4$, 6, 1, $-3$, 7, 2, 4. Using a threshold of $\tau = 0\%$:

Gains above zero: $5 + 8 + 3 + 6 + 1 + 7 + 2 + 4 = 36$

Losses below zero: $2 + 1 + 4 + 3 = 10$

$$\Omega(0) = \frac{36}{10} = 3.6$$

For every unit of loss below the threshold, the fund generated 3.6 units of gain — a strong result. If the threshold were raised to 2%, the gains would shrink and the losses would grow, reducing the ratio.

## Remember

The Omega ratio addresses a key limitation of mean-variance analysis: real financial returns are not normally distributed. Hedge fund strategies involving options, trend following, or event-driven bets often have skewed or fat-tailed return profiles where variance alone is misleading. By incorporating every moment of the return distribution through the CDF, the Omega ratio provides a single number that respects the full shape of returns. It is particularly useful when comparing strategies with similar Sharpe ratios but very different tail behaviour.
