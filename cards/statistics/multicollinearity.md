# Multicollinearity

**Topic:** Statistics
**Tags:** regression, linear model, correlation, factor model, coefficient instability, VIF
**Created:** 2026-05-30
**Author:** Claude Sonnet 4.6

---

## Definition

**Multicollinearity** occurs when two or more predictors in a regression are highly linearly correlated, making it difficult to isolate the independent effect of each predictor on the response. The OLS coefficient estimates remain unbiased but their standard errors inflate, reducing statistical power and making the estimates numerically unstable across different samples.

## Key Formula

The variance of the $j$-th OLS coefficient is:

$$\text{Var}(\hat{\beta}_j) = \frac{\sigma^2}{(n-1)\,\text{Var}(x_j)} \cdot \frac{1}{1 - R_j^2}$$

where $R_j^2$ is the $R^2$ from regressing $x_j$ on all other predictors. The factor $1/(1 - R_j^2) = \text{VIF}_j$ is the Variance Inflation Factor: when $R_j^2 \to 1$, the coefficient variance explodes and OLS becomes unreliable.

The OLS normal equations require inverting $\mathbf{X}^\top\mathbf{X}$; near-perfect collinearity makes this matrix near-singular with condition number:

$$\kappa(\mathbf{X}^\top\mathbf{X}) = \frac{\lambda_{\max}}{\lambda_{\min}} \gg 1$$

## Example

A cross-sectional regression of stock returns uses book-to-price ratio ($x_1$) and earnings-to-price ratio ($x_2$) as predictors. These two value signals have correlation $\rho = 0.92$. Regressing $x_1$ on $x_2$ gives $R_1^2 = 0.846$, so:

$$\text{VIF}_1 = \frac{1}{1 - 0.846} = 6.5$$

The standard error of $\hat{\beta}_1$ is inflated by a factor of $\sqrt{6.5} \approx 2.5$ relative to the case of no collinearity. A coefficient that looks statistically insignificant may genuinely matter once the redundant predictor is removed or the two signals are orthogonalised.

## Remember

Multicollinearity is endemic in quantitative finance because financial signals are constructed from overlapping data: different momentum windows, related valuation ratios, or macro variables that all measure credit stress. The symptom to watch for is large swings in factor coefficients between estimation windows — a sign that the model is fitting a linear combination of the predictors, not each one individually. The remedies are: (1) drop one of the collinear predictors; (2) replace them with their principal components (PCA orthogonalisation); or (3) use ridge regression, which handles near-singular $\mathbf{X}^\top\mathbf{X}$ by adding $\lambda \mathbf{I}$ to the matrix before inversion.
