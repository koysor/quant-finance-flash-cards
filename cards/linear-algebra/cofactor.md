# Cofactor

**Topic:** Linear Algebra
**Tags:** cofactor, determinant, cofactor expansion, adjoint, matrix inverse
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **cofactor** $C_{ij}$ of a square matrix $A$ is the signed minor of the $(i,j)$ entry — the determinant of the submatrix formed by deleting row $i$ and column $j$, multiplied by $(-1)^{i+j}$. Cofactors give a systematic way to expand a determinant along any row or column, and they are the entries of the matrix used to construct the adjoint.

## Key Formula

$$C_{ij} = (-1)^{i+j} M_{ij}$$

where $M_{ij}$ is the corresponding minor. The sign $(-1)^{i+j}$ is $+1$ when $i+j$ is even, $-1$ when odd.

**Cofactor expansion** along row $i$:

$$\det(A) = \sum_{j=1}^{n} a_{ij}\, C_{ij}$$

**Cofactor expansion** along column $j$:

$$\det(A) = \sum_{i=1}^{n} a_{ij}\, C_{ij}$$

The **adjoint** is the transpose of the cofactor matrix:

$$\text{adj}(A)_{ij} = C_{ji}$$

## Example

For $A = \begin{pmatrix} 2 & 1 & 0 \\ 3 & 4 & 1 \\ 0 & 2 & 3 \end{pmatrix}$, compute $C_{11}$ and $C_{12}$:

$$C_{11} = (+1)\det\begin{pmatrix}4&1\\2&3\end{pmatrix} = 12 - 2 = 10$$

$$C_{12} = (-1)\det\begin{pmatrix}3&1\\0&3\end{pmatrix} = -(9 - 0) = -9$$

Expanding along row 1:

$$\det(A) = 2(10) + 1(-9) + 0(\cdot) = 20 - 9 = 11$$

Since $\det(A) = 11 \neq 0$, the matrix is invertible.

## Remember

Cofactors provide the link between the determinant and the matrix inverse through $A^{-1} = \frac{1}{\det(A)}\,\text{adj}(A)$. In quantitative finance, cofactor expansion is rarely used numerically — LU decomposition is far more efficient. However, cofactors appear analytically in **sensitivity analysis of small systems**: for a $2 \times 2$ or $3 \times 3$ pricing or calibration problem, differentiating the inverse with respect to a parameter (e.g. a yield or volatility) can be done in closed form using cofactors, yielding exact analytical Greeks without finite differencing.
