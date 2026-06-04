# Method of Moments

**Topic:** Statistics
**Tags:** method of moments, estimation, moments, parameters, fitting
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

The **method of moments** estimates the parameters of a probability distribution by equating the theoretical moments of the distribution (expressed in terms of the unknown parameters) to the corresponding sample moments computed from observed data. For $p$ parameters, $p$ moment equations are set up and solved simultaneously.

## Key Formula

For a distribution with parameter vector $\theta = (\theta_1, \ldots, \theta_p)$, the $k$-th theoretical moment is:

$$\mu_k(\theta) = \mathbb{E}[X^k]$$

The method of moments sets:

$$\mu_k(\hat{\theta}) = \hat{m}_k = \frac{1}{n}\sum_{i=1}^{n} x_i^k, \quad k = 1, 2, \ldots, p$$

**Example — normal distribution** ($\mu$, $\sigma^2$): equating first two moments gives the closed-form estimators:

$$\hat{\mu} = \bar{x}, \qquad \hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

## Example

A quant fits a gamma distribution (shape $\alpha$, scale $\beta$) to 500 observed credit loss severities. The sample mean is $\bar{x} = \$120{,}000$ and the sample variance is $s^2 = \$9 \times 10^9$.

Using $\mathbb{E}[X] = \alpha\beta$ and $\text{Var}(X) = \alpha\beta^2$:

$$\hat{\beta} = \frac{s^2}{\bar{x}} = \frac{9 \times 10^9}{120{,}000} = \$75{,}000, \qquad \hat{\alpha} = \frac{\bar{x}}{\hat{\beta}} = \frac{120{,}000}{75{,}000} = 1.6$$

The fitted gamma distribution is then used to compute expected loss and loss quantiles for regulatory capital.

## Remember

The method of moments is the simplest way to fit a parametric model to financial data — it is computationally trivial and always produces explicit formulae when moments exist. However, it is generally less statistically efficient than maximum likelihood estimation (MLE): for a normal distribution both methods agree, but for skewed or fat-tailed distributions used in credit and insurance loss modelling (gamma, log-normal, Pareto), MLE will produce narrower confidence intervals for the same sample size. The method of moments is therefore most useful as a quick sanity check or starting point for numerical MLE optimisation.
