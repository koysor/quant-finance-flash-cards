# Positive Definite Matrices

**Topic:** Linear Algebra
**Tags:** positive definite, covariance matrix, eigenvalues, Cholesky, quadratic form
**Created:** 2026-02-28 20:46:20
**Author:** Claude Opus 4.6

---

## Definition

A symmetric matrix $A$ is positive definite if $\mathbf{x}^\top A \mathbf{x} > 0$ for every non-zero vector $\mathbf{x}$. Equivalently, all its eigenvalues are strictly positive, and its Cholesky decomposition exists. A matrix is positive semi-definite if $\mathbf{x}^\top A \mathbf{x} \geq 0$ (eigenvalues $\geq 0$).

## Key Formula

Positive definiteness test — for a $2 \times 2$ symmetric matrix $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$:

$$A \text{ is positive definite} \iff a > 0 \text{ and } ac - b^2 > 0$$

General Sylvester's criterion — $A$ is positive definite if and only if all leading principal minors are positive:

$$a_{11} > 0, \quad \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} > 0, \quad \ldots, \quad \det(A) > 0$$

## Example

Test whether $A = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}$ is positive definite.

First minor: $a_{11} = 4 > 0$. ✓

Determinant: $4 \times 3 - 2 \times 2 = 8 > 0$. ✓

Both conditions satisfied, so $A$ is positive definite.

Eigenvalues: $\lambda = \frac{7 \pm \sqrt{17}}{2} \approx 5.56$ and $1.44$ — both positive. ✓

## Remember

Every valid covariance matrix must be positive semi-definite — the quadratic form $\mathbf{w}^\top \Sigma \mathbf{w}$ is the portfolio variance, and variance cannot be negative. When a covariance matrix fails to be positive semi-definite (due to missing data or numerical error), portfolio optimisation breaks down: the optimiser finds positions with apparently negative variance and takes infinite leverage. The Cholesky decomposition of $\Sigma$ is the standard tool for generating correlated random variables in Monte Carlo simulation — it only exists when $\Sigma$ is positive definite, so checking this property is the first step before any simulation.
