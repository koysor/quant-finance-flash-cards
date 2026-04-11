# Consistent Estimator

**Topic:** Statistics
**Tags:** consistency, convergence, estimator, law of large numbers, asymptotic statistics
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

An estimator $\hat{\theta}_n$ is **consistent** if it converges in probability to the true parameter $\theta$ as the sample size $n \to \infty$. Consistency is an asymptotic property — the estimator gets arbitrarily close to the truth given enough data, even if it is biased for any finite $n$.

$$\hat{\theta}_n \xrightarrow{p} \theta \quad \text{as } n \to \infty$$

Formally: for every $\varepsilon > 0$, $P(|\hat{\theta}_n - \theta| > \varepsilon) \to 0$ as $n \to \infty$.

## Key Formula

**Sufficient condition for consistency:**

$$\text{Bias}(\hat{\theta}_n) \to 0 \quad \text{and} \quad \text{Var}(\hat{\theta}_n) \to 0 \quad \text{as } n \to \infty$$

Equivalently: $\text{MSE}(\hat{\theta}_n) = \text{Bias}^2 + \text{Var} \to 0$.

**Biased but consistent — MLE variance:**

$$\hat{\sigma}^2_{\text{MLE}} = \frac{1}{n}\sum(X_i - \bar{X})^2, \qquad \text{Bias} = -\frac{\sigma^2}{n} \to 0$$

**Consistent and unbiased — sample variance:**

$$s^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2 \xrightarrow{p} \sigma^2$$

## Example

Estimating daily volatility from rolling windows of size $n$:

| $n$ | Bias of $\hat{\sigma}^2_{\text{MLE}}$ | $\text{Var}(\hat{\sigma}^2_{\text{MLE}})$ proportional to |
|---|---|---|
| 10 | $-10\%$ of $\sigma^2$ | $1/10$ |
| 60 | $-1.7\%$ of $\sigma^2$ | $1/60$ |
| 252 | $-0.4\%$ of $\sigma^2$ | $1/252$ |

As $n$ grows, both bias and variance shrink to zero: the MLE variance is consistent (but not unbiased for finite $n$). The sample variance $s^2$ is both unbiased and consistent.

## Remember

Consistency tells you where the estimator is heading; unbiasedness tells you where it is right now. In practice, consistency matters more than unbiasedness for large samples — but finance often uses short windows (10–60 days), where bias can be material. An important practical implication: GARCH and EWMA volatility estimators are consistent for the true conditional variance under their model assumptions, but they are biased in finite samples and sensitive to model misspecification. When a model is misspecified, consistency guarantees convergence to the "best" parameter within the model class, not to the true underlying parameter.
