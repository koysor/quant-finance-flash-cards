# LU Decomposition

**Topic:** Linear Algebra
**Tags:** lu decomposition, matrix factorisation, gaussian elimination, numerical methods, linear systems, triangular matrices
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

**LU decomposition** factorises a square matrix $A$ into the product of a lower triangular matrix $L$ (with ones on the diagonal) and an upper triangular matrix $U$: $A = LU$. It is the matrix encoding of Gaussian elimination and is the standard numerical method for solving systems of linear equations efficiently.

## Key Formula

$$A = LU$$

where $L$ is lower triangular with $L_{ii} = 1$, and $U$ is upper triangular. To solve $A\mathbf{x} = \mathbf{b}$, substitute $LU\mathbf{x} = \mathbf{b}$ and solve in two steps:

1. **Forward substitution:** solve $L\mathbf{y} = \mathbf{b}$ for $\mathbf{y}$
2. **Back substitution:** solve $U\mathbf{x} = \mathbf{y}$ for $\mathbf{x}$

In practice, **partial pivoting** is used: $PA = LU$, where $P$ is a permutation matrix that reorders rows to keep the algorithm numerically stable.

## Example

Decompose $A = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}$.

Eliminate below the pivot in column 1: subtract $\frac{4}{2} = 2$ times row 1 from row 2.

$$L = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$$

Verify: $LU = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix} = A$ ✓

To solve $A\mathbf{x} = \begin{pmatrix} 5 \\ 11 \end{pmatrix}$: forward substitution gives $\mathbf{y} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$; back substitution gives $\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

## Remember

In quantitative finance, yield curve calibration and portfolio optimisation both require solving $A\mathbf{x} = \mathbf{b}$ many times — once per security or per simulation path. LU decomposition pays for itself because $L$ and $U$ are computed once at cost $O(n^3)$, then each new right-hand side $\mathbf{b}$ is solved at only $O(n^2)$. When repricing a portfolio of $n$ instruments under thousands of stress scenarios, this reuse is precisely what makes the computation tractable.
