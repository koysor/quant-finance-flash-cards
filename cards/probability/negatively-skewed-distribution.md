# Negatively Skewed Distribution

**Topic:** Probability
**Tags:** negative skew, left skew, skewness, asymmetry, tail risk, equity returns
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **negatively skewed** (left-skewed) distribution has a long tail on the left side. Large negative outcomes — crashes, drawdowns — are more common than a symmetric distribution would predict. The mean is dragged below the median by infrequent but severe losses.

$$\gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3} < 0$$

$$\text{Mean} \leq \text{Median} \leq \text{Mode}$$

## Key Formula

**Sample skewness estimator:**

$$\hat{\gamma}_1 = \frac{\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^3}{\left(\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2\right)^{3/2}}$$

**Effect on option pricing (volatility skew):**

Negative skewness in equity returns implies that the market assigns higher probability to large downward moves than the normal distribution predicts. This creates a **volatility skew**: implied volatility of out-of-the-money puts exceeds that of out-of-the-money calls.

## Example

Empirical daily S&P 500 log-returns (2000–2020) exhibit $\hat{\gamma}_1 \approx -0.7$ to $-1.0$. The mean daily return is slightly below the median, and the left tail (crash days) is heavier than the right tail.

A covered call strategy (long stock + short call) has **negative return skewness**: you collect small premiums regularly but occasionally suffer large losses when the stock crashes while the call expires worthless.

## Remember

Negative skewness is the most common distributional shape for equity returns and many hedge fund strategies — small steady gains punctuated by occasional large losses. This is why strategies that appear to have attractive Sharpe ratios can destroy value in tail events: the Sharpe ratio ignores skewness entirely. In risk management, negative skewness means that normal-distribution VaR underestimates tail losses, and CVaR (which averages the tail) is the more appropriate measure.
