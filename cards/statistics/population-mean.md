# Population Mean

**Topic:** Statistics
**Tags:** mean, expectation, population, central tendency, statistics
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **population mean** $\mu$ is the true average value of a random variable across the entire population — every possible observation. It is the theoretical quantity that sample-based estimators attempt to approximate. In probability terms, it is the expectation $\mu = E[X]$.

$$\mu = \frac{1}{N}\sum_{i=1}^{N} x_i \quad \text{(finite population)}$$

$$\mu = E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx \quad \text{(continuous distribution)}$$

## Key Formula

**Finite population of size $N$:**

$$\mu = \frac{1}{N}\sum_{i=1}^{N} x_i$$

**Continuous random variable with PDF $f(x)$:**

$$\mu = \int_{-\infty}^{\infty} x\,f(x)\,dx$$

**Key property — linearity:**

$$E[aX + b] = a\mu + b$$

## Example

A stock's daily log-return follows $X \sim N(\mu, \sigma^2)$ with $\mu = 0.05\%$ per day. This is the population mean — the true expected return in the data-generating process. Over 252 trading days the expected annual return is $252 \times 0.05\% = 12.6\%$.

In practice $\mu$ is unknown. With 5 years of data (1,260 observations), the sample mean $\bar{X}$ estimates it, but typical standard error is $\sigma/\sqrt{n} \approx 1\%/\sqrt{1260} \approx 0.028\%$ per day — so the 95% confidence interval for $\mu$ spans roughly $\pm 0.056\%$, more than the mean itself. Estimating expected returns precisely is very hard.

## Remember

The population mean is almost never observable in finance — we only ever have samples. This creates a fundamental asymmetry: portfolio variance can be estimated with reasonable precision from daily returns over a few years, but the population mean return cannot. This is why modern portfolio construction often sets all expected returns equal (global minimum variance) or uses factor models to impose structure, rather than relying on noisy sample mean estimates.
