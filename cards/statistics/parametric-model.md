# Parametric Model

**Topic:** Statistics
**Tags:** parametric, distribution, maximum likelihood, model assumptions, estimation
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

A **parametric model** is a statistical model that assumes data is drawn from a probability distribution of a known family, fully characterised by a finite set of parameters $\theta$. Once the family is chosen (e.g. normal, log-normal, Student's $t$), fitting the model reduces to estimating those parameters from data — typically via maximum likelihood estimation. This contrasts with non-parametric models, which make no such distributional assumption.

## Key Formula

A parametric model specifies a likelihood function $L(\theta)$. For $n$ independent observations $x_1, \ldots, x_n$ from a normal distribution:

$$L(\mu, \sigma) = \prod_{i=1}^{n} \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right)$$

The maximum likelihood estimates $\hat{\mu}$ and $\hat{\sigma}$ maximise this function, giving the sample mean and (biased) standard deviation:

$$\hat{\mu} = \frac{1}{n}\sum_{i=1}^{n} x_i, \qquad \hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \hat{\mu})^2$$

## Example

A risk analyst models daily equity returns as normally distributed. Using 250 trading days of data, she estimates $\hat{\mu} = 0.05\%$ per day and $\hat{\sigma} = 1.2\%$ per day. The parametric model is then fully specified: any probability statement about future returns — such as the 99% one-day VaR — can be computed analytically without simulation:

$$\text{VaR}_{99\%} = -(0.05\% - 2.326 \times 1.2\%) = 2.74\%$$

A non-parametric approach would instead read the 99th percentile directly from the empirical return distribution, making no normality assumption.

## Remember

Parametric models underpin much of quantitative finance: Black-Scholes assumes log-normal returns; GARCH assumes a conditional normal (or Student's $t$) distribution for innovations; Parametric VaR assumes normally distributed portfolio P&L. Their strength is analytic tractability — closed-form prices, Greeks, and risk measures follow directly from the parameter estimates. Their weakness is model risk: if the assumed distribution family is wrong (e.g. real returns have fat tails), every downstream calculation inherits that error. This is why regulators under **FRTB** require stress scenarios that go beyond parametric assumptions.
