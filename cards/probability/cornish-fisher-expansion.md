# Cornish–Fisher Expansion

**Topic:** Probability
**Tags:** quantile, skewness, kurtosis, VaR, non-normal, risk adjustment
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **Cornish–Fisher expansion** adjusts a standard normal quantile $z_\alpha$ to account for skewness and excess kurtosis in a distribution. It provides a corrected quantile $z_{CF}$ without requiring the full distribution — only its first four moments. This makes it a practical tool for computing risk measures when returns are approximately, but not exactly, normal.

## Key Formula

$$z_{CF} = z_\alpha + \frac{1}{6}(z_\alpha^2 - 1)\,S + \frac{1}{24}(z_\alpha^3 - 3z_\alpha)\,K - \frac{1}{36}(2z_\alpha^3 - 5z_\alpha)\,S^2$$

where:
- $z_\alpha = \Phi^{-1}(\alpha)$ is the standard normal quantile
- $S$ is the skewness of the return distribution
- $K$ is the **excess** kurtosis (kurtosis minus 3)

The adjusted VaR is then:

$$\text{VaR}_\alpha = \mu + \sigma \times z_{CF}$$

## Example

A hedge fund's monthly returns have $\mu = 0.8\%$, $\sigma = 4\%$, skewness $S = -0.6$, and excess kurtosis $K = 2.0$. Compute the 99% monthly VaR.

The normal quantile is $z_{0.01} = -2.326$:

$$z_{CF} = -2.326 + \frac{1}{6}((-2.326)^2 - 1)(-0.6) + \frac{1}{24}((-2.326)^3 - 3(-2.326))(2.0) - \frac{1}{36}(2(-2.326)^3 - 5(-2.326))(-0.6)^2$$

$$z_{CF} = -2.326 + \frac{1}{6}(4.410)(-0.6) + \frac{1}{24}(-5.588)(2.0) - \frac{1}{36}(-13.54)(0.36)$$

$$z_{CF} = -2.326 - 0.441 - 0.466 + 0.135 = -3.098$$

$$\text{VaR}_{99\%} = -(0.008 + 0.04 \times (-3.098)) = -(0.008 - 0.1239) = 11.59\%$$

The Cornish–Fisher VaR of 11.59% is substantially larger than the Gaussian VaR of $-(0.008 + 0.04 \times (-2.326)) = 8.50\%$, reflecting the negative skewness and fat tails.

## Remember

The Cornish–Fisher expansion is the industry-standard quick fix for non-normality in risk management. When a portfolio exhibits negative skewness (large losses more likely than large gains) and excess kurtosis (fat tails), the Gaussian VaR systematically underestimates risk. The expansion corrects for this using only moments that are straightforward to estimate from historical data. It is widely used in hedge fund risk reporting, UCITS fund risk disclosures, and modified VaR calculations where fitting a full parametric distribution would be impractical. The key limitation is that it is an asymptotic expansion — for extremely skewed or heavy-tailed distributions, it can produce non-monotonic quantiles.
