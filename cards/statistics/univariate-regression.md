# Univariate Regression

**Topic:** Statistics
**Tags:** regression, linear model, slope, R-squared, least squares
**Created:** 2026-05-30
**Author:** Claude Sonnet 4.6

---

## Definition

**Univariate regression** (or simple linear regression) fits a straight line $\hat{y}_i = \hat{\alpha} + \hat{\beta} x_i$ to a single predictor $x$ and response $y$ by minimising the sum of squared residuals. It produces closed-form estimators for slope and intercept without requiring matrix algebra, making it the entry point to regression analysis.

## Key Formula

OLS slope and intercept:

$$\hat{\beta} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\text{Cov}(x, y)}{\text{Var}(x)} = r_{xy} \cdot \frac{\sigma_y}{\sigma_x}$$

$$\hat{\alpha} = \bar{y} - \hat{\beta}\,\bar{x}$$

Coefficient of determination — in the univariate case this equals the square of the Pearson correlation:

$$R^2 = r_{xy}^2$$

Residual standard error with $n - 2$ degrees of freedom:

$$s = \sqrt{\frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{n - 2}}$$

## Example

Regress a stock's monthly excess return $y$ on the market's monthly excess return $x$ using summary statistics: $r_{xy} = 0.87$, $\sigma_y = 4.2\%$, $\sigma_x = 3.0\%$, $\bar{x} = 0.8\%$, $\bar{y} = 1.1\%$.

$$\hat{\beta} = 0.87 \times \frac{4.2}{3.0} = 0.87 \times 1.4 = 1.22$$

$$\hat{\alpha} = 1.1 - 1.22 \times 0.8 = 1.1 - 0.976 = 0.124\%$$

$$R^2 = 0.87^2 = 0.757$$

The market explains 75.7% of variance in the stock's excess returns; the estimated alpha of 0.12% per month represents unexplained outperformance.

## Remember

Univariate regression is the engine behind CAPM beta estimation: regress excess stock returns on excess market returns and the slope is the market beta. The identity $R^2 = r_{xy}^2$ is especially useful — a correlation of $\lvert 0.7 \rvert$ explains exactly 49% of return variance, showing why even strongly correlated factors leave substantial idiosyncratic risk unexplained. The slope formula $\hat{\beta} = r_{xy}(\sigma_y / \sigma_x)$ shows that beta scales correlation by the volatility ratio, so a high-volatility stock can carry a large beta even with only moderate market correlation.
