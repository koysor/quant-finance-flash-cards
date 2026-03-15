# Matrix Addition

**Topic:** Linear Algebra
**Tags:** matrix addition, element-wise, linear algebra, portfolio returns, covariance matrix
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Matrix addition** combines two matrices of the same dimensions by adding their corresponding entries element-wise. Both matrices must have identical numbers of rows and columns — addition is undefined for matrices of different shapes.

## Key Formula

For matrices $A$ and $B$ of the same size $m \times n$:

$$(A + B)_{ij} = A_{ij} + B_{ij}$$

Key properties:
- **Commutative:** $A + B = B + A$
- **Associative:** $(A + B) + C = A + (B + C)$
- **Identity:** $A + 0 = A$, where $0$ is the zero matrix
- **Inverse:** $A + (-A) = 0$
- **Transpose distributes:** $(A + B)^\top = A^\top + B^\top$
- **Scalar distributes:** $c(A + B) = cA + cB$

## Example

$$\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 2 & 6 \end{pmatrix}$$

The attempt $\begin{pmatrix} 1 & 2 \end{pmatrix} + \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ is **undefined** — a $1 \times 2$ row vector cannot be added to a $2 \times 1$ column vector.

## Remember

Matrix addition appears directly in portfolio aggregation: if $\Sigma_1$ and $\Sigma_2$ are the covariance matrices of two independent sub-portfolios, the combined covariance matrix is $\Sigma_1 + \Sigma_2$. Similarly, when decomposing returns into a factor component and an idiosyncratic component — $R = BFB^\top + D$ — the two matrices are added element-wise, making matrix addition the fundamental operation behind risk aggregation across books or desks.
