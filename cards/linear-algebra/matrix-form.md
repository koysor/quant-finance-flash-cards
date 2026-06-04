# Matrix Form

**Topic:** Linear Algebra
**Tags:** matrix form, linear system, ax=b, vector notation, linear algebra
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Matrix form** is the representation of a system of linear equations — or a linear model with multiple variables — as a single matrix equation $A\mathbf{x} = \mathbf{b}$, where $A$ is a matrix of coefficients, $\mathbf{x}$ is a column vector of unknowns, and $\mathbf{b}$ is a column vector of constants. It compresses arbitrarily many equations into one compact expression and enables the full toolkit of linear algebra (inverses, decompositions, eigenvalues) to be applied.

## Key Formula

A system of $m$ equations in $n$ unknowns:

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\ \quad\vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$

is written in matrix form as $A\mathbf{x} = \mathbf{b}$:

$$\underbrace{\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}}_{A \in \mathbb{R}^{m \times n}} \underbrace{\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}}_{\mathbf{x}} = \underbrace{\begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}}_{\mathbf{b}}$$

If $A$ is square and invertible, the unique solution is $\mathbf{x} = A^{-1}\mathbf{b}$.

## Example

Ordinary least squares regression of returns $\mathbf{r}$ on $k$ factors $F_1, \ldots, F_k$ across $T$ observations is written in matrix form as:

$$\mathbf{r} = F\boldsymbol{\beta} + \boldsymbol{\varepsilon}$$

With $T = 3$, $k = 2$ (market return, SMB):

$$\begin{pmatrix} 0.02 \\ -0.01 \\ 0.03 \end{pmatrix} = \begin{pmatrix} 1 & 0.8 & 0.3 \\ 1 & -0.5 & 0.1 \\ 1 & 1.2 & -0.2 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta_{\text{mkt}} \\ \beta_{\text{smb}} \end{pmatrix} + \boldsymbol{\varepsilon}$$

The OLS solution $\hat{\boldsymbol{\beta}} = (F^\top F)^{-1}F^\top \mathbf{r}$ is computed in one matrix expression rather than solving three equations simultaneously.

## Remember

Matrix form is the language in which quantitative finance is actually implemented. Factor models, portfolio optimisation (mean-variance with constraints), OLS regression, PCA, and Kalman filters are all expressed as $A\mathbf{x} = \mathbf{b}$ or $A\mathbf{x} \leq \mathbf{b}$ under the hood. Libraries such as NumPy (`np.linalg.solve`), SciPy, and LAPACK solve these systems efficiently using LU decomposition rather than computing $A^{-1}$ explicitly — inverting large matrices is numerically unstable and slow. In risk systems, the covariance matrix $\Sigma$ of factor returns appears constantly in matrix form: portfolio variance $= \mathbf{w}^\top \Sigma \mathbf{w}$, and optimisation constraints are written as $A\mathbf{w} = \mathbf{b}$ (e.g. weights sum to one).
