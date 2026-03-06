# Covariance

**Topic:** Statistics
**Tags:** statistics, covariance, correlation, portfolio theory, risk
**Author:** Claude Opus 4.6

---

## Definition

**Covariance** measures the degree to which two random variables move together. A positive covariance indicates the variables tend to increase and decrease in tandem, while a negative covariance indicates they move in opposite directions. Unlike correlation, covariance is not normalised — its magnitude depends on the scales of the variables.

## Key Formula

**Population covariance:**

$$\text{Cov}(X, Y) = E\!\left[(X - \mu_X)(Y - \mu_Y)\right] = E[XY] - E[X]\,E[Y]$$

**Sample covariance** (unbiased):

$$s_{XY} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

**Key properties:**

- $\text{Cov}(X, X) = \text{Var}(X)$
- $\text{Cov}(X, Y) = \text{Cov}(Y, X)$
- $\text{Cov}(aX, bY) = ab\,\text{Cov}(X, Y)$
- If $X$ and $Y$ are independent, $\text{Cov}(X, Y) = 0$ (but not vice versa)

## Example

Two stocks have the following monthly returns over four months:

| Month | Stock A | Stock B |
|-------|---------|---------|
| 1     | 3%      | 2%      |
| 2     | −1%     | −2%     |
| 3     | 4%      | 1%      |
| 4     | 2%      | 3%      |

Means: $\bar{x}_A = 2\%$, $\bar{x}_B = 1\%$

$$s_{AB} = \frac{(3-2)(2-1) + (-1-2)(-2-1) + (4-2)(1-1) + (2-2)(3-1)}{4-1}$$

$$= \frac{1 + 9 + 0 + 0}{3} = \frac{10}{3} \approx 3.33 \; (\%^2)$$

The positive covariance confirms that A and B tend to move in the same direction.

## Remember

Covariance is the building block of portfolio risk. The variance of a two-asset portfolio is $\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \, \text{Cov}(R_1, R_2)$. In matrix form, portfolio variance is $\mathbf{w}^\top \Sigma \, \mathbf{w}$, where $\Sigma$ is the covariance matrix. Every mean-variance optimisation, from Markowitz to risk parity, is fundamentally driven by the covariance structure of asset returns — estimating $\Sigma$ accurately is one of the hardest practical problems in quantitative finance.
