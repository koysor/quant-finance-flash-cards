# Kurtosis

**Topic:** Statistics
**Tags:** kurtosis, tail risk, distributions, moments, fat tails

---

## Definition

Kurtosis is the fourth standardised moment of a distribution. It measures the heaviness of the tails relative to the overall shape — distributions with high kurtosis produce more extreme outliers than a normal distribution with the same variance. **Excess kurtosis** subtracts 3 (the kurtosis of a normal distribution) so that a normal has excess kurtosis of zero.

## Key Formula

The kurtosis of a random variable $X$ with mean $\mu$ and standard deviation $\sigma$ is:

$$\text{Kurt}[X] = \frac{E\left[(X - \mu)^4\right]}{\sigma^4}$$

Excess kurtosis (the form most commonly used in finance):

$$\text{Excess Kurt}[X] = \frac{E\left[(X - \mu)^4\right]}{\sigma^4} - 3$$

For a sample of $n$ observations $x_1, x_2, \ldots, x_n$ with sample mean $\bar{x}$ and sample standard deviation $s$:

$$\hat{\kappa} = \frac{1}{n} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{s}\right)^4 - 3$$

## Example

Suppose daily returns over five days are $-3\%$, $1\%$, $0\%$, $1\%$, $-2\%$.

Sample mean: $\bar{x} = (-3 + 1 + 0 + 1 - 2) / 5 = -0.6\%$.

Sample standard deviation: $s \approx 1.67\%$.

Standardised values: $z_i = (x_i - \bar{x}) / s$ gives approximately $-1.44$, $0.96$, $0.36$, $0.96$, $-0.84$.

Fourth powers: $4.30$, $0.85$, $0.02$, $0.85$, $0.50$.

Mean of fourth powers: $(4.30 + 0.85 + 0.02 + 0.85 + 0.50) / 5 = 1.30$.

Excess kurtosis: $1.30 - 3 = -1.70$.

The negative value indicates lighter tails than a normal distribution — unsurprising for only five observations with no extreme outlier.

## Remember

Financial return distributions are famously **leptokurtic** (positive excess kurtosis): large moves happen far more often than a normal model predicts. Ignoring this leads to systematic underestimation of tail risk — VaR models calibrated to a normal distribution understate the probability of crashes. The volatility smile in options markets exists precisely because traders price in the fat tails that kurtosis quantifies. Always check kurtosis alongside variance when assessing risk; two portfolios with identical standard deviations can have very different probabilities of extreme loss.
