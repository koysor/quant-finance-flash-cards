# Empirical Bayes

**Topic:** Statistics
**Tags:** empirical bayes, hierarchical model, shrinkage, prior estimation, factor model, cross-sectional
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Empirical Bayes** (also called Type II maximum likelihood) estimates the prior distribution's hyperparameters from the data itself, rather than specifying them subjectively. The estimated prior is then used in a fully Bayesian update. It is a pragmatic compromise: the structure of Bayesian shrinkage without the burden of eliciting a prior.

## Key Formula

In a hierarchical model with observations $y_i \sim \mathcal{N}(\theta_i, \sigma^2)$ and prior $\theta_i \sim \mathcal{N}(\mu, \tau^2)$, the empirical Bayes estimator for each $\theta_i$ is the James–Stein shrinkage estimator:

$$\hat{\theta}_i^{\text{EB}} = \hat{\mu} + \left(1 - \frac{\sigma^2}{\sigma^2 + \hat{\tau}^2}\right)(y_i - \hat{\mu})$$

where $\hat{\mu}$ and $\hat{\tau}^2$ are estimated from the cross-sectional distribution of all $y_i$.

## Example

A fund estimates expected returns for 500 stocks using 12 months of returns. Raw OLS estimates have huge estimation error (especially for small-cap stocks). Empirical Bayes shrinks each estimate towards the cross-sectional mean $\hat{\mu}$: stocks with volatile returns get shrunk more (shrinkage factor near 1), while stocks with stable returns are shrunk less. In practice this reduces out-of-sample tracking error by 20–40% relative to using raw sample means as expected return inputs.

## Remember

Empirical Bayes is the statistical engine behind the **Black–Litterman model** and **Fama–French cross-sectional factor regressions**. In both cases, individual asset estimates are unreliable because the time series is short relative to the estimation uncertainty, so pooling information across assets via a hierarchical prior dramatically improves out-of-sample performance. The key insight is that even if you cannot specify the prior from theory, you can estimate it from the cross-section — turning a pure inference problem into a regularisation problem that beats both raw OLS and fully subjective Bayesian priors.
