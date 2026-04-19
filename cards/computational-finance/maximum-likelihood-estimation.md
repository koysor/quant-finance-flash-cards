# Maximum Likelihood Estimation

**Topic:** Computational Finance
**Tags:** MLE, likelihood, parameter estimation, log-likelihood, calibration, statistical inference
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Maximum Likelihood Estimation (MLE)** finds the parameter values $\hat{\boldsymbol{\theta}}$ that make the observed data most probable under a chosen distributional model. It is the standard method for calibrating parametric models to financial data.

## Key Formula

**Likelihood:** $L(\boldsymbol{\theta}) = \prod_{i=1}^{N} f(x_i;\boldsymbol{\theta})$

**Log-likelihood (used in practice):**

$$\ell(\boldsymbol{\theta}) = \sum_{i=1}^{N} \ln f(x_i;\boldsymbol{\theta})$$

**MLE estimate:** $\hat{\boldsymbol{\theta}} = \arg\max_{\boldsymbol{\theta}}\; \ell(\boldsymbol{\theta})$

## Example

Assume daily log-returns follow $\mathcal{N}(\mu, \sigma^2)$. The log-likelihood is maximised analytically: $\hat{\mu} = \bar{x}$ (sample mean), $\hat{\sigma}^2 = \frac{1}{N}\sum(x_i - \bar{x})^2$ (biased sample variance).

## Remember

MLE is the engine behind GARCH calibration, copula fitting, and stochastic volatility model parameter estimation. Log-likelihood is preferred over likelihood because summing logs is numerically stable and differentiable — the same score function forms the basis of the information matrix used to construct confidence intervals around calibrated parameters.
