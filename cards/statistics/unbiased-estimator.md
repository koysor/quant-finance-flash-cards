# Unbiased Estimator

**Topic:** Statistics
**Tags:** bias, estimator, sample mean, sample variance, estimation, statistics
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

An **unbiased estimator** $\hat{\theta}$ of a parameter $\theta$ is one whose expected value equals the true parameter — on average, across all possible samples, the estimator neither overshoots nor undershoots the truth. Formally:

$$E[\hat{\theta}] = \theta$$

The **bias** of an estimator is $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$; an unbiased estimator has zero bias.

## Key Formula

**Sample mean** — unbiased estimator of the population mean $\mu$:

$$\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i, \qquad E[\bar{X}] = \mu$$

**Sample variance** — unbiased estimator of the population variance $\sigma^2$, using $n-1$ (Bessel's correction):

$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2, \qquad E[s^2] = \sigma^2$$

The naive version $\frac{1}{n}\sum(X_i - \bar{X})^2$ has $E[\cdot] = \frac{n-1}{n}\sigma^2$ — it underestimates $\sigma^2$ because it uses the sample mean $\bar{X}$ rather than the true mean $\mu$.

**Bias-variance decomposition of mean squared error:**

$$\text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + \left[\text{Bias}(\hat{\theta})\right]^2$$

## Example

A fund manager estimates the daily return variance from 21 trading days of data: $\sum(R_i - \bar{R})^2 = 0.0420$.

Biased estimate (dividing by $n = 21$): $\hat{\sigma}^2 = 0.0420 / 21 = 0.00200$

Unbiased estimate (dividing by $n - 1 = 20$): $s^2 = 0.0420 / 20 = 0.00210$

The biased estimate would give a daily volatility of $\sqrt{0.00200} \approx 4.47\%$ vs. $\sqrt{0.00210} \approx 4.58\%$ — a 2.5% underestimate of risk, which compounds when annualised.

## Remember

In risk management, using the biased $1/n$ variance systematically underestimates volatility, leading to VaR models that are too optimistic. The correction from $n$ to $n-1$ is small when $n$ is large (hundreds of days) but material for short estimation windows — exactly the windows used for short-term risk monitoring. Unbiasedness is also not the only goal: the bias-variance trade-off means a slightly biased estimator with much lower variance (e.g. the James-Stein shrinkage estimator of the mean vector, or Ledoit-Wolf for the covariance matrix) can have lower mean squared error than the unbiased version, which is why practitioners often deliberately use biased estimators.
