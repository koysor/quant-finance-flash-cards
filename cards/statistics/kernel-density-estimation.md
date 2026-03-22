# Kernel Density Estimation

**Topic:** Statistics
**Tags:** KDE, density estimation, non-parametric, bandwidth, return distribution
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Kernel density estimation** (KDE) is a non-parametric method for estimating the probability density function of a random variable from observed data. Instead of assuming a specific distribution (e.g. normal), KDE places a smooth "kernel" (typically a Gaussian bump) at each data point and sums them to produce a continuous density estimate. The **bandwidth** $h$ controls the smoothness of the result.

## Key Formula

Given $n$ observations $x_1, x_2, \ldots, x_n$, the KDE at any point $x$ is:

$$\hat{f}(x) = \frac{1}{nh}\sum_{i=1}^{n} K\!\left(\frac{x - x_i}{h}\right)$$

where $K$ is the **kernel function** (satisfying $\int K(u)\,du = 1$) and $h > 0$ is the **bandwidth**.

**Gaussian kernel** (most common):

$$K(u) = \frac{1}{\sqrt{2\pi}}\,e^{-u^2/2}$$

**Silverman's rule of thumb** for bandwidth:

$$h = 1.06\,\hat{\sigma}\,n^{-1/5}$$

where $\hat{\sigma}$ is the sample standard deviation.

## Example

An analyst has 500 daily returns for a stock and wants to visualise the distribution without assuming normality.

With $\hat{\sigma} = 1.2\%$ and $n = 500$:

$$h = 1.06 \times 0.012 \times 500^{-0.2} = 0.01272 \times 0.2885 = 0.00367$$

The bandwidth is about 0.37 percentage points. Each of the 500 returns gets a Gaussian bump of width $h = 0.37\%$; summing them reveals the empirical density — including any skewness, fat tails, or bimodality that a normal fit would miss.

## Remember

KDE lets the data speak for itself when parametric assumptions are suspect — a common situation in finance, where return distributions exhibit fat tails, skewness, and regime changes. Traders use KDE to visualise the "true" shape of the P&L distribution from historical data, revealing risks that a Gaussian model would understate. The bandwidth is critical: too small and the estimate is noisy; too large and it oversmooths real features like bimodality. In practice, KDE is used alongside parametric models as a diagnostic — if the KDE and the fitted normal disagree in the tails, it signals that VaR or option pricing based on normality may be unreliable.
