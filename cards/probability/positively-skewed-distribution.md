# Positively Skewed Distribution

**Topic:** Probability
**Tags:** positive skew, right skew, skewness, asymmetry, tail risk, distribution shape
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **positively skewed** (right-skewed) distribution has a long tail on the right side and most mass concentrated on the left. The mean is pulled above the median by the rare but large positive outcomes.

$$\gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3} > 0$$

$$\text{Mode} \leq \text{Median} \leq \text{Mean}$$

## Key Formula

For a lognormal distribution $X = e^Y$ where $Y \sim \mathcal{N}(\mu, \sigma^2)$:

$$\gamma_1 = (e^{\sigma^2} + 2)\sqrt{e^{\sigma^2} - 1}$$

This is always positive — the lognormal is inherently right-skewed.

**Mean and median diverge due to skewness:**

$$E[X] = e^{\mu + \sigma^2/2}, \qquad \text{Median}(X) = e^{\mu}$$

$$E[X] > \text{Median}(X) \text{ when } \sigma > 0$$

## Example

Asset prices follow a lognormal distribution with $\mu = 0.07$, $\sigma = 0.2$ annually. The expected asset price exceeds the median: $E[S_T] = S_0 e^{0.07 + 0.02} = S_0 e^{0.09}$ vs $\text{Median}(S_T) = S_0 e^{0.07}$ — a gap of about 2% driven by positive skewness.

Venture capital returns are strongly positively skewed: most investments return little or nothing, but rare successes (the "right tail") produce outsized gains that lift the mean far above the median.

## Remember

Positive skewness creates an asymmetry where the mean overstates the typical outcome. In derivatives, positive skew in the underlying creates a premium on out-of-the-money call options relative to the Black-Scholes price (which assumes zero skew). Commodity prices, venture capital returns, and insurance losses are all right-skewed. A fund with positive return skew is desirable — large gains are more likely than symmetry would predict.
