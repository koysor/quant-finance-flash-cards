# Statistical Properties of Returns

**Topic:** Statistics
**Tags:** returns, mean, standard deviation, standardisation, volatility

---

## Definition

The **statistical properties of returns** refer to the sample mean and sample standard deviation of an asset's daily returns. Standardising returns by subtracting the mean and dividing by the standard deviation reveals that daily returns closely follow a normal distribution.

## Key Formula

**Sample mean:**

$$\bar{R} = \frac{1}{M} \sum_{i=1}^{M} R_i$$

**Sample standard deviation (Bessel-corrected):**

$$s = \sqrt{\frac{1}{M-1} \sum_{i=1}^{M}(R_i - \bar{R})^2}$$

**Standardised return:**

$$Z_i = \frac{R_i - \bar{R}}{s}$$

## Example

For the S&P 500 (1950-2006), the daily mean return is approximately $\bar{R} \approx 0.035\%$ and the daily standard deviation is $s \approx 0.89\%$. Standardising all daily returns and plotting them produces a histogram that closely matches the standard normal bell curve.

## Remember

Standardised returns fitting the normal distribution is the empirical justification for the entire random walk model of asset prices. Without this observation, the assumption that $dS = \mu S \, dt + \sigma S \, dX$ would have no basis in real market data.
