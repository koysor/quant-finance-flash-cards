# Ordinary Least Squares Regression

**Topic:** Statistics
**Tags:** regression, OLS, linear model, factor model, estimation
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

**Ordinary least squares (OLS) regression** finds the coefficient vector $\hat{\boldsymbol{\beta}}$ that minimises the sum of squared residuals in the linear model $\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$. It is the most widely used method for fitting linear relationships and, under the Gauss–Markov assumptions, produces the best linear unbiased estimator (BLUE).

## Key Formula

The OLS estimator:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$$

The residual sum of squares (RSS):

$$\text{RSS} = \sum_{i=1}^{n} (y_i - \mathbf{x}_i^\top \hat{\boldsymbol{\beta}})^2 = (\mathbf{y} - \mathbf{X}\hat{\boldsymbol{\beta}})^\top (\mathbf{y} - \mathbf{X}\hat{\boldsymbol{\beta}})$$

The coefficient of determination:

$$R^2 = 1 - \frac{\text{RSS}}{\text{TSS}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

The standard error of $\hat{\beta}_j$:

$$\text{SE}(\hat{\beta}_j) = \hat{\sigma} \sqrt{[(\mathbf{X}^\top \mathbf{X})^{-1}]_{jj}}, \quad \hat{\sigma}^2 = \frac{\text{RSS}}{n - k}$$

where $n$ is the number of observations and $k$ is the number of estimated parameters.

## Example

Fit $y = a + bx$ to four data points: $(1, 2)$, $(2, 3)$, $(3, 5)$, $(4, 4)$.

Summary statistics: $\bar{x} = 2.5$, $\bar{y} = 3.5$, $\sum (x_i - \bar{x})(y_i - \bar{y}) = 3.0$, $\sum (x_i - \bar{x})^2 = 5.0$.

The slope:

$$\hat{b} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{3.0}{5.0} = 0.6$$

The intercept:

$$\hat{a} = \bar{y} - \hat{b}\,\bar{x} = 3.5 - 0.6 \times 2.5 = 2.0$$

The fitted line is $\hat{y} = 2.0 + 0.6x$. The residuals are $(2 - 2.6, \; 3 - 3.2, \; 5 - 3.8, \; 4 - 4.4) = (-0.6, -0.2, 1.2, -0.4)$ and the RSS is $0.36 + 0.04 + 1.44 + 0.16 = 2.0$.

## Remember

OLS is the workhorse of quantitative finance. Regressing excess asset returns on excess market returns yields the CAPM beta as the slope coefficient — this is how practitioners estimate systematic risk from historical data. In multi-factor models (Fama–French, Barra), OLS simultaneously estimates an asset's exposure to each factor. The Gauss–Markov theorem guarantees that OLS is BLUE when residuals are homoskedastic and uncorrelated, but financial returns typically exhibit heteroskedasticity and autocorrelation, so robust standard errors (Newey–West, White) are essential in practice. Always check residual diagnostics before trusting OLS inference on market data.
