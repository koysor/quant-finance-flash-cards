# F-Test (Regression)

**Topic:** Statistics
**Tags:** regression, hypothesis testing, F-statistic, model selection, joint significance
**Created:** 2026-05-30
**Author:** Claude Sonnet 4.6

---

## Definition

The **F-test for regression** tests the null hypothesis that all $k$ slope coefficients are simultaneously zero — i.e. the model explains no more variance than the mean alone. A significant F-statistic is the omnibus check that at least one predictor is useful, and should be evaluated before inspecting individual t-statistics.

## Key Formula

The F-statistic:

$$F = \frac{R^2 / k}{(1 - R^2)/(n - k - 1)} = \frac{\text{MSR}}{\text{MSE}}$$

where MSR is the mean regression sum of squares and MSE is the mean squared error. Under $H_0: \beta_1 = \cdots = \beta_k = 0$, $F$ follows an $F(k,\; n-k-1)$ distribution.

Equivalently:

$$F = \frac{(\text{TSS} - \text{RSS})/k}{\text{RSS}/(n - k - 1)}$$

The F-test is related to the t-test: with $k = 1$ predictor, $F = t^2$.

## Example

A three-factor model ($k = 3$) is fitted to $n = 60$ monthly returns and achieves $R^2 = 0.65$:

$$F = \frac{0.65/3}{(1 - 0.65)/(60 - 3 - 1)} = \frac{0.2167}{0.35/56} = \frac{0.2167}{0.00625} = 34.7$$

The critical value at the 1% level for $F(3, 56)$ is approximately 4.15. With $F = 34.7 \gg 4.15$, we strongly reject $H_0$: the three factors jointly explain a significant portion of return variation.

## Remember

The F-test is the first diagnostic to run when evaluating a new quantitative factor model — a non-significant F-statistic means the entire regression is statistically worthless, regardless of how any individual coefficient looks. In multi-factor equity models, practitioners also use partial F-tests to compare nested models: testing whether adding a new factor (e.g. a sentiment score) to an existing three-factor model provides a statistically significant improvement, with the partial F-statistic measuring the incremental explanatory power. This is more rigorous than simply noting that $R^2$ increased, since $R^2$ always rises with additional predictors.
