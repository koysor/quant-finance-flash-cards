# Jarque-Bera Test

**Topic:** Statistics
**Tags:** hypothesis testing, normality, skewness, kurtosis, goodness of fit, returns
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

The Jarque-Bera (JB) test is a goodness-of-fit test that checks whether a data sample has the skewness and kurtosis consistent with a normal distribution. The null hypothesis is that the data are normally distributed; a large JB statistic leads to rejection, indicating significant departure from normality.

## Key Formula

$$JB = \frac{n}{6}\!\left(S^{2} + \frac{(K - 3)^{2}}{4}\right)$$

where $n$ is the sample size, $S$ is the sample skewness, and $K$ is the sample excess kurtosis plus 3 (i.e. the raw kurtosis). Under the null hypothesis of normality, $JB \sim \chi^{2}(2)$.

Equivalently, writing $\hat{S}$ for skewness and $\hat{K}$ for excess kurtosis:

$$JB = \frac{n}{6}\!\left(\hat{S}^{2} + \frac{\hat{K}^{2}}{4}\right)$$

## Example

Suppose you collect $n = 200$ daily log-returns and compute sample skewness $\hat{S} = -0.6$ and sample excess kurtosis $\hat{K} = 1.8$.

$$JB = \frac{200}{6}\!\left((-0.6)^{2} + \frac{(1.8)^{2}}{4}\right) = 33.33 \times \left(0.36 + 0.81\right) = 33.33 \times 1.17 = 39.0$$

The 5% critical value for $\chi^{2}(2)$ is $5.99$. Since $39.0 \gg 5.99$, you reject the null hypothesis and conclude that these returns are not normally distributed.

## Remember

In quantitative finance, many pricing and risk models (Black-Scholes, parametric VaR) assume returns are normally distributed. The Jarque-Bera test is the standard diagnostic applied to historical return series to check whether this assumption holds. When the test rejects normality -- as it almost always does for equity returns, which exhibit negative skewness and excess kurtosis -- it signals that fat-tailed models (Student's t, jump-diffusion, or GARCH) should be used instead, and that naive Gaussian VaR will underestimate tail risk.
