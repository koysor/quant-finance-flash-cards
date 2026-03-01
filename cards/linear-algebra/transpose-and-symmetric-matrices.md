# Transpose and Symmetric Matrices

**Topic:** Linear Algebra
**Tags:** linear algebra, matrices, transpose, symmetric, covariance matrix

---

## Definition

The **transpose** of a matrix $A$, written $A^\top$, is formed by swapping rows and columns: the element in row $i$, column $j$ of $A$ becomes the element in row $j$, column $i$ of $A^\top$. A square matrix is **symmetric** if $A^\top = A$ — that is, it equals its own transpose.

## Key Formula

If $A$ is $(m \times n)$, then $A^\top$ is $(n \times m)$:

$$(A^\top)_{ij} = A_{ji}$$

Key properties:
- $(A^\top)^\top = A$
- $(A + B)^\top = A^\top + B^\top$
- $(AB)^\top = B^\top A^\top$ (note the reversal)
- $(cA)^\top = cA^\top$

A real symmetric matrix has the special property that all its **eigenvalues are real** and its eigenvectors are orthogonal.

## Example

$$A = \begin{pmatrix} 1 & 4 \\ 3 & 2 \\ 5 & 6 \end{pmatrix} \implies A^\top = \begin{pmatrix} 1 & 3 & 5 \\ 4 & 2 & 6 \end{pmatrix}$$

A covariance matrix for two assets with $\sigma_1 = 0.2$, $\sigma_2 = 0.3$, and $\rho = 0.5$:

$$\Sigma = \begin{pmatrix} 0.04 & 0.03 \\ 0.03 & 0.09 \end{pmatrix}$$

This is symmetric because $\text{Cov}(X, Y) = \text{Cov}(Y, X)$.

## Remember

The covariance matrix $\Sigma$ is always symmetric and positive semi-definite — these properties guarantee that portfolio variance $\sigma_p^2 = \mathbf{w}^\top \Sigma\,\mathbf{w} \geq 0$ for any weight vector $\mathbf{w}$. The quadratic form $\mathbf{w}^\top \Sigma\,\mathbf{w}$ uses the transpose to convert a matrix equation into a scalar, and symmetry ensures the eigenvectors of $\Sigma$ form an orthogonal basis — which is precisely what makes PCA decomposition clean and interpretable.
