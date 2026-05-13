# Linear Relationships in Multiple Dimensions

**Topic:** Linear Algebra
**Tags:** linear map, matrix, multivariate, factor model, hyperplane, linear system
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **linear relationship in multiple dimensions** expresses one variable as a weighted sum of several others: $y = \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_d x_d$. In matrix form, a set of $n$ such relationships over $d$ inputs is $\mathbf{y} = \mathbf{X}\boldsymbol{\beta}$, where $\mathbf{X}$ is the $n \times d$ design matrix and $\boldsymbol{\beta} \in \mathbb{R}^d$ is the coefficient vector.

## Key Formula

The general multivariate linear relationship:

$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta}, \qquad \mathbf{X} \in \mathbb{R}^{n \times d},\; \boldsymbol{\beta} \in \mathbb{R}^d,\; \mathbf{y} \in \mathbb{R}^n$$

Geometrically, $\mathbf{X}\boldsymbol{\beta}$ traces a $d$-dimensional hyperplane through the origin in $\mathbb{R}^n$. The OLS solution projects $\mathbf{y}$ orthogonally onto this hyperplane:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$$

which exists when the columns of $\mathbf{X}$ are linearly independent (full column rank).

## Example

A three-factor return model for a stock: $r_i = \beta_1 r_M + \beta_2 r_{\text{HML}} + \beta_3 r_{\text{SMB}}$, where each factor is a column of $\mathbf{X}$. With $n = 60$ monthly observations and $d = 3$ factors, $\hat{\boldsymbol{\beta}} = (0.9, \; 0.3, \; -0.1)$ means the stock has: near-market beta, a moderate value tilt, and a slight large-cap bias. The fitted returns $\hat{\mathbf{y}} = \mathbf{X}\hat{\boldsymbol{\beta}}$ lie on a 3-dimensional hyperplane in $\mathbb{R}^{60}$; the residuals $\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}}$ are orthogonal to this hyperplane.

## Remember

The matrix form $\mathbf{y} = \mathbf{X}\boldsymbol{\beta}$ is the universal language of factor models in quantitative finance. Every Fama-French regression, every CAPM beta, every PCA factor loading, and every linear risk attribution is an instance of a linear relationship in multiple dimensions. Understanding this geometrically — fitted values lie on a hyperplane, residuals are perpendicular to it, multicollinearity means near-parallel columns that make $(\mathbf{X}^\top\mathbf{X})^{-1}$ unstable — gives direct insight into why correlated factors produce unreliable betas and why regularisation (ridge, lasso) is needed.
