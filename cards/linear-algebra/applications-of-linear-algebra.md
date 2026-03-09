# Applications of Linear Algebra

**Topic:** Linear Algebra
**Tags:** linear algebra, portfolio theory, regression, PCA, Monte Carlo, calibration
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

**Applications of linear algebra** in quantitative finance refers to the use of matrices, vectors, and their operations to express and solve core problems in portfolio construction, risk modelling, regression, and simulation. Nearly every quantitative model reduces to a linear algebra operation — matrix multiplication for portfolio variance, matrix inversion for regression, eigendecomposition for risk factors, and triangular factorisation for correlated simulation.

## Key Formula

**Portfolio variance** (covariance matrix times weight vector):

$$\sigma_p^2 = \mathbf{w}^\top \Sigma \, \mathbf{w}$$

**Ordinary least squares** (regression coefficients):

$$\hat{\boldsymbol{\beta}} = (X^\top X)^{-1} X^\top \mathbf{y}$$

**Principal Component Analysis** (eigendecomposition of covariance matrix):

$$\Sigma = Q \Lambda Q^\top$$

where $Q$ contains eigenvectors (risk factors) and $\Lambda$ the diagonal matrix of eigenvalues (variance explained).

**Correlated simulation** (Cholesky factorisation):

$$\mathbf{z}_{\text{correlated}} = L \, \mathbf{z}_{\text{independent}}, \quad \text{where } \Sigma = L L^\top$$

## Example

A risk manager holds a two-asset portfolio with weights $\mathbf{w} = (0.6, \; 0.4)^\top$ and covariance matrix:

$$\Sigma = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix}$$

Portfolio variance via matrix multiplication:

$$\sigma_p^2 = \begin{pmatrix} 0.6 & 0.4 \end{pmatrix} \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix} \begin{pmatrix} 0.6 \\ 0.4 \end{pmatrix} = 0.6(0.024 + 0.004) + 0.4(0.006 + 0.036) = 0.0168 + 0.0168 = 0.0336$$

$$\sigma_p = \sqrt{0.0336} \approx 18.3\%$$

The same $\Sigma$ would be eigendecomposed for PCA, Cholesky-factorised for simulation, or inverted for minimum-variance optimisation — one matrix, four distinct applications.

## Remember

Linear algebra is the computational language of quantitative finance. Portfolio optimisation is a quadratic form $\mathbf{w}^\top \Sigma \, \mathbf{w}$; factor models express returns as $\mathbf{r} = B \mathbf{f} + \boldsymbol{\varepsilon}$; yield curve bootstrapping solves $A\mathbf{x} = \mathbf{b}$; and multi-asset Monte Carlo simulation begins with a Cholesky decomposition. Understanding how these applications map onto the same handful of matrix operations — multiplication, inversion, decomposition — reveals why linear algebra is the single most useful branch of mathematics for a working quant.
