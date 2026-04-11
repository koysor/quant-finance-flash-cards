# Maximum Likelihood Estimation

**Topic:** Statistics
**Tags:** maximum likelihood, MLE, likelihood function, parameter estimation, log-likelihood
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Maximum likelihood estimation (MLE)** finds the parameter values that make the observed data most probable. Given a statistical model with parameter vector $\boldsymbol{\theta}$ and observed data $x_1, \ldots, x_n$, the MLE $\hat{\boldsymbol{\theta}}_{\text{MLE}}$ maximises the likelihood function $L(\boldsymbol{\theta})$.

$$\hat{\boldsymbol{\theta}}_{\text{MLE}} = \underset{\boldsymbol{\theta}}{\arg\max}\; L(\boldsymbol{\theta}) = \underset{\boldsymbol{\theta}}{\arg\max}\; \prod_{i=1}^{n} f(x_i;\boldsymbol{\theta})$$

## Key Formula

**Likelihood function** (i.i.d. observations):

$$L(\boldsymbol{\theta}) = \prod_{i=1}^{n} f(x_i;\boldsymbol{\theta})$$

**Log-likelihood** (maximised in practice to avoid numerical underflow):

$$\ell(\boldsymbol{\theta}) = \sum_{i=1}^{n} \ln f(x_i;\boldsymbol{\theta})$$

**First-order condition (score equation):**

$$\frac{\partial\,\ell(\boldsymbol{\theta})}{\partial\,\boldsymbol{\theta}} = \mathbf{0}$$

**MLE for a normal distribution** $N(\mu, \sigma^2)$:

$$\hat{\mu}_{\text{MLE}} = \bar{X} = \frac{1}{n}\sum X_i \quad \text{(unbiased)}$$

$$\hat{\sigma}^2_{\text{MLE}} = \frac{1}{n}\sum(X_i - \bar{X})^2 \quad \text{(biased — uses } n \text{ not } n-1\text{)}$$

## Example

A stock's log-returns $r_1, \ldots, r_{252}$ are assumed i.i.d. $\sim N(\mu, \sigma^2)$. The MLE gives:

$\hat{\mu} = \bar{r} = 0.06\%$ per day, $\hat{\sigma}^2_{\text{MLE}} = 0.000196\,\%^2$, so $\hat{\sigma}_{\text{MLE}} = 1.4\%$ per day.

Annualised: $\hat{\mu}_{\text{annual}} = 252 \times 0.06\% = 15.1\%$, $\hat{\sigma}_{\text{annual}} = 1.4\% \times \sqrt{252} \approx 22.2\%$.

The Sharpe ratio estimate $\approx 15.1\% / 22.2\% \approx 0.68$ — but carries enormous estimation uncertainty since $\hat{\mu}$ has standard error $\approx 22.2\% / \sqrt{252} \approx 1.4\%$.

## Remember

MLE is the workhorse of statistical estimation in finance: it is used to fit GARCH volatility models, calibrate credit default models, estimate copula parameters, and fit distributions to loss data. Its key properties — consistency and asymptotic normality — hold under standard regularity conditions. However, the MLE for variance uses $1/n$ (biased), and MLE is sensitive to distributional misspecification: if returns are truly fat-tailed but a normal MLE is used, the volatility estimate will be too low because the normal model attributes tail observations to variance rather than excess kurtosis.
