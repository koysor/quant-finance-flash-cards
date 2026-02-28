# Central Limit Theorem

**Topic:** Statistics
**Tags:** CLT, convergence, normal distribution, sampling, estimation
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The **Central Limit Theorem** (CLT) states that the sum (or average) of a large number of independent, identically distributed random variables with finite variance is approximately normally distributed, regardless of the underlying distribution.

## Key Formula

If $X_1, X_2, \dots, X_n$ are i.i.d. with mean $\mu$ and variance $\sigma^2$, then the standardised sample mean converges in distribution to the standard normal:

$$\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty$$

where $\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$.

## Example

Suppose daily returns on a stock have mean $\mu = 0.04\%$ and standard deviation $\sigma = 1.5\%$. Over $n = 25$ trading days, the average daily return $\bar{X}$ has:

- Mean: $0.04\%$
- Standard error: $1.5\% / \sqrt{25} = 0.3\%$

By the CLT, $\bar{X}$ is approximately normal. The probability that the average exceeds $0.64\%$ is:

$$P(\bar{X} > 0.64\%) = P\!\left(Z > \frac{0.64 - 0.04}{0.3}\right) = P(Z > 2) \approx 2.3\%$$

## Remember

The CLT is the reason the normal distribution appears everywhere in quantitative finance. Even when individual returns are not perfectly normal — exhibiting skewness or fat tails — the average return over many periods, or the aggregate loss across many independent positions, tends towards normality. This underpins parametric VaR calculations, the validity of confidence intervals for estimated drift and volatility, and the convergence of binomial tree models to the Black-Scholes price as the number of steps grows.
