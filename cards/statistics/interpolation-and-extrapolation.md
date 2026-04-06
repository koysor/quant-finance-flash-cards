# Interpolation and Extrapolation

**Topic:** Statistics
**Tags:** interpolation, extrapolation, regression, prediction, scatter diagram, linear model
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Interpolation** uses a fitted model to estimate values of the response variable within the range of the observed data; **extrapolation** extends predictions beyond that range. Interpolation is generally reliable; extrapolation is unreliable because the assumed relationship may not hold outside the observed data. For a regression line $\hat{y} = a + bx$, both operations involve substituting a value of $x$ into the fitted equation.

## Key Formula

**Fitted regression line** (least squares):

$$\hat{y} = \hat{a} + \hat{b}x, \qquad \hat{b} = \frac{S_{xy}}{S_{xx}}, \qquad \hat{a} = \bar{y} - \hat{b}\bar{x}$$

**Interpolation:** substitute $x = x^*$ where $x_{\min} \leq x^* \leq x_{\max}$.

**Extrapolation:** substitute $x = x^*$ where $x^* < x_{\min}$ or $x^* > x_{\max}$ — result should be treated with caution.

**Residual:** $e_i = y_i - \hat{y}_i$ — a large residual suggests the model fits poorly at that point.

## Example

A regression of 10-year gilt yield on the Bank Rate, using 20 years of monthly data ($x$: 0.1% to 5.5%), gives $\hat{y} = 0.8 + 0.9x$.

**Interpolation** at Bank Rate = 3%: $\hat{y} = 0.8 + 2.7 = 3.5\%$ — reliable, within sample.

**Extrapolation** at Bank Rate = 8%: $\hat{y} = 0.8 + 7.2 = 8.0\%$ — unreliable; the linear relationship seen at low rates may break down at historically unprecedented rate levels.

## Remember

Interpolation vs extrapolation is the core distinction in **yield curve construction**. A yield curve is estimated from a finite set of liquid bond prices; yields at other maturities are obtained by **interpolation** (e.g. linear, cubic spline, Nelson-Siegel). Extrapolating beyond the longest liquid maturity (typically 30–50 years) to price ultra-long liabilities (pension funds, insurance) is unreliable — small errors in the extrapolated rate produce large differences in liability valuations. Regulators such as EIOPA mandate specific extrapolation methods (Smith-Wilson) precisely to control this risk.
