# Criteria for Invertibility

**Topic:** Linear Algebra
**Tags:** invertibility, determinant, rank, singular matrix, eigenvalues, covariance matrix
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A square matrix $A$ is **invertible** (non-singular) exactly when any one of several equivalent conditions holds. When one fails, they all fail.

## Key Formula

$$|A| \neq 0 \iff A^{-1} \text{ exists} \iff \text{rows are independent (full rank)} \iff A\mathbf{x} = \mathbf{0} \text{ has only } \mathbf{x} = \mathbf{0} \iff \text{no zero eigenvalue}$$

The last condition follows because $|A| = \prod_i \lambda_i$, the product of the eigenvalues.

## Example

$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$$

has $|A| = 4 - 4 = 0$. The second row is twice the first, so the rank is 1, $A(2, -1)^{\top} = \mathbf{0}$ has a non-trivial solution, and the eigenvalues are $0$ and $5$ (trace $5$, determinant $0$). The matrix is singular, and $A^{-1}$ does not exist.

## Remember

The commonest practical failure in portfolio work: estimating an $n \times n$ covariance matrix from $T$ observations. If $T < n$ then $\Sigma$ is singular and $\Sigma^{-1}$, needed for minimum-variance weights, does not exist. Five hundred stocks need more than 500 return observations (about two years of daily data) before $\Sigma$ is even invertible, which is why shrinkage and factor models are used.
