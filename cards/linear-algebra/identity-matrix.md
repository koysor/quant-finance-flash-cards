# Identity Matrix

**Topic:** Linear Algebra
**Tags:** identity matrix, matrix multiplication, linear algebra, matrix inverse, transformations
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **identity matrix** $I_n$ is the $n \times n$ square matrix with ones on the main diagonal and zeros everywhere else. It is the multiplicative identity for matrix multiplication: multiplying any compatible matrix by $I$ leaves it unchanged, just as multiplying a number by 1 does.

## Key Formula

$$I_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix}$$

For any $m \times n$ matrix $A$:

$$I_m A = A = A I_n$$

The identity matrix defines the matrix inverse: $A^{-1}$ is the unique matrix satisfying:

$$A A^{-1} = A^{-1} A = I$$

Additional properties:
- $\det(I) = 1$
- $I^\top = I$ (symmetric)
- $I^k = I$ for all $k \geq 1$ (idempotent under powers)
- The columns of $I$ are the **standard basis vectors** $\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n$

## Example

$$I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

$$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 2 & 5 \\ 4 & 0 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 2 & 5 \\ 4 & 0 \end{pmatrix}$$

Verify the inverse relation: if $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ then $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, and $AA^{-1} = I_2$ ✓

## Remember

The identity matrix appears in **regularisation** — one of the most practically important techniques in quantitative finance. Ridge regression adds $\lambda I$ to the Gram matrix before inverting: $\hat{\boldsymbol{\beta}} = (X^\top X + \lambda I)^{-1} X^\top \mathbf{y}$. This shift guarantees invertibility even when $X^\top X$ is singular or near-singular due to correlated risk factors, and shrinks estimated coefficients towards zero. The same $\Sigma + \lambda I$ trick is applied to sample covariance matrices before portfolio optimisation to prevent extreme, unstable weights caused by near-zero eigenvalues.
