# Minor

**Topic:** Linear Algebra
**Tags:** minor, determinant, submatrix, cofactor, matrix inverse
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **minor** $M_{ij}$ of a square matrix $A$ is the determinant of the submatrix formed by deleting row $i$ and column $j$ from $A$. Minors are the building blocks of cofactor expansion, which is the standard recursive method for computing determinants of matrices larger than $2 \times 2$.

## Key Formula

For an $n \times n$ matrix $A$, the minor $M_{ij}$ is:

$$M_{ij} = \det(A_{\hat{i}\hat{j}})$$

where $A_{\hat{i}\hat{j}}$ is the $(n-1) \times (n-1)$ submatrix obtained by removing row $i$ and column $j$.

The determinant of $A$ expanded along row $i$:

$$\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$$

The sign factor $(-1)^{i+j}$ follows a checkerboard pattern:

$$\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}$$

## Example

For $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$, find $M_{12}$ (delete row 1, column 2):

$$M_{12} = \det\begin{pmatrix} 4 & 6 \\ 7 & 9 \end{pmatrix} = 4(9) - 6(7) = 36 - 42 = -6$$

Expanding along row 1:

$$\det(A) = 1\cdot M_{11} - 2\cdot M_{12} + 3\cdot M_{13} = 1(−3) − 2(−6) + 3(−3) = 0$$

The zero determinant confirms the rows are linearly dependent ($\text{row}_3 = 2\cdot\text{row}_2 - \text{row}_1$).

## Remember

Minors appear in quantitative finance primarily through the adjoint and Cramer's rule, but their deeper importance is that the **rank of a matrix** can be characterised by its minors: the rank equals the size of the largest non-zero minor. This provides a theoretical test for linear independence — a set of $k$ asset return series is linearly independent if and only if some $k \times k$ submatrix of their data matrix has a non-zero determinant (non-zero minor).
