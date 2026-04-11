# Sample Mean

**Topic:** Statistics
**Tags:** sample mean, estimator, unbiased, central tendency, statistics
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **sample mean** $\bar{X}$ is the arithmetic average of $n$ observed values drawn from a population. It is an unbiased estimator of the population mean $\mu$: on average across all possible samples of size $n$, $\bar{X}$ equals $\mu$.

$$\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$$

## Key Formula

$$\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i, \qquad E[\bar{X}] = \mu, \qquad \text{Var}(\bar{X}) = \frac{\sigma^2}{n}$$

**Standard error** (precision of the estimate):

$$\text{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}}$$

**Standardised sample mean** (by the CLT, approximately normal for large $n$):

$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0, 1)$$

## Example

A portfolio has 60 monthly returns. Sample mean: $\bar{R} = 0.8\%$ per month. Population standard deviation assumed $\sigma = 4\%$.

Standard error: $\text{SE} = 4\% / \sqrt{60} \approx 0.516\%$.

95% confidence interval for $\mu$: $0.8\% \pm 1.96 \times 0.516\% = [-0.21\%,\; 1.81\%]$.

The interval includes zero — there is insufficient evidence that the true mean return is positive. Five years of monthly data is rarely enough to detect genuine alpha with statistical confidence.

## Remember

The sample mean halves in standard error every time the sample size quadruples ($\text{SE} \propto 1/\sqrt{n}$). In finance, where daily returns have high volatility relative to expected returns, reaching a standard error small enough to distinguish genuine alpha from luck requires decades of data — far longer than most strategies survive. This is the "estimation error" problem in portfolio construction, and it motivates techniques such as Black-Litterman (which blends sample means with prior views) and minimum-variance portfolios (which avoid estimating means entirely).
