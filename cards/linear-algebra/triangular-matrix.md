# Triangular Matrix

**Topic:** Linear Algebra
**Tags:** triangular matrix, determinant, matrix factorisation, linear systems, diagonal
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **triangular matrix** is a square matrix where all entries either above or below the main diagonal are zero. An **upper triangular** matrix has zeros below the diagonal; a **lower triangular** matrix has zeros above it. A diagonal matrix is both upper and lower triangular simultaneously.

## Key Formula

Upper triangular $U$ and lower triangular $L$:

$$U = \begin{pmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33} \end{pmatrix}, \qquad L = \begin{pmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{pmatrix}$$

Key properties shared by both types:
- **Determinant** = product of diagonal entries: $\det(U) = u_{11} u_{22} \cdots u_{nn}$
- **Eigenvalues** are the diagonal entries $u_{11}, u_{22}, \ldots, u_{nn}$
- **Product** of two upper triangular matrices is upper triangular (and likewise for lower)
- **Inverse** of a triangular matrix is triangular of the same type (if it exists)

## Example

$$\det\begin{pmatrix} 3 & 1 & 5 \\ 0 & 2 & 4 \\ 0 & 0 & -1 \end{pmatrix} = 3 \times 2 \times (-1) = -6$$

No cofactor expansion needed — the determinant is simply the product of diagonal entries.

## Remember

Triangular matrices are the workhorses of numerical linear algebra because they enable **fast solving** of $A\mathbf{x} = \mathbf{b}$ in $O(n^2)$ rather than $O(n^3)$. Nearly every matrix factorisation used in quantitative finance produces triangular factors: LU decomposition splits $A$ into $L$ and $U$; Cholesky writes $\Sigma = LL^\top$; QR decomposition produces an upper triangular $R$. Once a matrix is factorised into triangular form, solving many pricing or optimisation problems reduces to cheap forward and back substitution.
