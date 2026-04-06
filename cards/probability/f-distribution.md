# F-Distribution

**Topic:** Probability
**Tags:** F-distribution, ANOVA, variance ratio, regression, F-test, degrees of freedom
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **F-distribution** $F(d_1, d_2)$ is the ratio of two independent chi-squared random variables, each divided by their degrees of freedom. It arises in hypothesis tests that compare variances or test the overall significance of a regression model. The distribution is right-skewed and defined on $(0, \infty)$.

## Key Formula

If $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$ independently, then:

$$F = \frac{U/d_1}{V/d_2} \sim F(d_1, d_2)$$

**Mean and variance:**

$$\mathbb{E}[F] = \frac{d_2}{d_2 - 2} \; (d_2 > 2), \qquad \text{Var}(F) = \frac{2d_2^2(d_1+d_2-2)}{d_1(d_2-2)^2(d_2-4)} \; (d_2 > 4)$$

**F-test for regression significance:**

$$F = \frac{\text{MSR}}{\text{MSE}} = \frac{SSR/k}{SSE/(n-k-1)} \sim F(k, n-k-1) \text{ under } H_0$$

where $k$ is the number of predictors and $n$ is the sample size.

**Reciprocal:** $1/F(d_1, d_2) \sim F(d_2, d_1)$.

## Example

A factor model regresses excess returns on 3 Fama-French factors, $n = 60$ months. The F-statistic is 8.4 with $F(3, 56)$ degrees of freedom. The critical value at 1% is approximately 4.2. Since $8.4 > 4.2$, we reject $H_0$ (all coefficients zero) — the model has significant explanatory power.

$R^2 = \text{SSR}/\text{SST} = 1 - \text{SSE}/\text{SST}$; the F-statistic is $R^2/(1-R^2) \times (n-k-1)/k$.

## Remember

The F-test is the **omnibus test for any OLS regression** in quantitative finance. Before trusting individual factor loadings, the F-statistic tells you whether the model explains anything at all. A model with high $R^2$ but a low F-statistic signals **overfitting** — many variables added, each contributing little. The F-distribution also arises in **Chow tests** for structural breaks (testing whether regression parameters are stable pre/post a date) and in **ANOVA** comparisons of multiple portfolio strategies, making it essential for model validation in risk and performance attribution.
