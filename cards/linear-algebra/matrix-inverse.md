# Matrix Inverse

**Topic:** Linear Algebra
**Tags:** linear algebra, matrices, inverse, regression, portfolio optimisation
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

The **inverse** of a square matrix $A$ is a matrix $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$, where $I$ is the identity matrix. A matrix has an inverse if and only if its determinant is non-zero; such a matrix is called **non-singular** or **invertible**.

## Key Formula

For a $2 \times 2$ matrix:

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

The general system $A\mathbf{x} = \mathbf{b}$ has the unique solution:

$$\mathbf{x} = A^{-1}\mathbf{b}$$

## Example

Solve $A\mathbf{x} = \mathbf{b}$ where $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$.

$$\det(A) = 3(4) - 1(2) = 10$$

$$A^{-1} = \frac{1}{10}\begin{pmatrix} 4 & -1 \\ -2 & 3 \end{pmatrix}$$

$$\mathbf{x} = A^{-1}\mathbf{b} = \frac{1}{10}\begin{pmatrix} 4(5) - 1(6) \\ -2(5) + 3(6) \end{pmatrix} = \begin{pmatrix} 1.4 \\ 0.8 \end{pmatrix}$$

## Remember

The matrix inverse appears throughout quantitative finance. The OLS regression formula $\hat{\boldsymbol{\beta}} = (X^\top X)^{-1} X^\top \mathbf{y}$ requires inverting the Gram matrix. In mean-variance optimisation, the optimal portfolio weights are $\mathbf{w} = \Sigma^{-1}\boldsymbol{\mu}$ (up to a scalar), which requires inverting the covariance matrix. If $\Sigma$ is singular — meaning some assets are perfectly correlated — the inverse does not exist and the optimisation breaks down, signalling redundant positions.
