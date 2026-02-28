# Determinant

**Topic:** Linear Algebra
**Tags:** linear algebra, matrices, determinant, invertibility, covariance matrix
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The **determinant** is a scalar value computed from a square matrix that encodes whether the matrix is invertible and how it scales area (or volume). A matrix with $\det(A) = 0$ is **singular** — it has no inverse and collapses at least one dimension to zero.

## Key Formula

For a $2 \times 2$ matrix:

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

For a $3 \times 3$ matrix, expand along the first row (**cofactor expansion**):

$$\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})$$

Key properties:
- $\det(AB) = \det(A)\det(B)$
- $\det(A^\top) = \det(A)$
- $\det(A^{-1}) = 1/\det(A)$

## Example

$$\det\begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix} = 2(5) - 3(1) = 7$$

Since $\det \neq 0$, this matrix is invertible.

$$\det\begin{pmatrix} 4 & 2 \\ 6 & 3 \end{pmatrix} = 4(3) - 2(6) = 0$$

This matrix is singular — its rows are proportional, meaning one variable is a perfect linear combination of the other.

## Remember

Before inverting a covariance matrix $\Sigma$ for portfolio optimisation or regression, you must check that $\det(\Sigma) \neq 0$. A zero determinant means the assets are perfectly linearly dependent — one asset's returns can be exactly replicated by a combination of the others. In practice, near-zero determinants (ill-conditioning) cause numerically unstable portfolio weights that blow up, which is why regularisation techniques like shrinkage estimators are applied to covariance matrices.
