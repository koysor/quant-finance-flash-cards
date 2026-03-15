# Adjoint

**Topic:** Linear Algebra
**Tags:** adjoint, adjugate, cofactor, matrix inverse, determinant
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **adjoint** (or **adjugate**) of a square matrix $A$, written $\text{adj}(A)$, is the transpose of the **cofactor matrix** of $A$. The cofactor $C_{ij}$ is $(-1)^{i+j}$ times the determinant of the submatrix obtained by deleting row $i$ and column $j$ from $A$. The adjoint provides a closed-form expression for the matrix inverse.

## Key Formula

$$A^{-1} = \frac{1}{\det(A)}\,\text{adj}(A)$$

where $\text{adj}(A)_{ij} = C_{ji}$ (note the transposition — row and column indices are swapped).

For a $2 \times 2$ matrix this gives the familiar result directly:

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies \text{adj}(A) = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \implies A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

The adjoint satisfies: $A\,\text{adj}(A) = \text{adj}(A)\,A = \det(A)\,I$.

## Example

Find $\text{adj}(A)$ for $A = \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$.

Cofactors (selected):

$$C_{11} = +\det\begin{pmatrix}1&1\\0&2\end{pmatrix} = 2, \quad C_{12} = -\det\begin{pmatrix}3&1\\0&2\end{pmatrix} = -6, \quad C_{13} = +\det\begin{pmatrix}3&1\\0&0\end{pmatrix} = 0$$

Computing all nine cofactors and transposing gives $\text{adj}(A)$. Then $\det(A) = 1(2) - 2(6) + 0 = -10$, so $A^{-1} = \tfrac{1}{-10}\,\text{adj}(A)$.

## Remember

The adjoint formula $A^{-1} = \frac{1}{\det(A)}\,\text{adj}(A)$ is primarily a theoretical tool rather than a computational one — computing all $n^2$ cofactors costs $O(n^4)$, far worse than the $O(n^3)$ LU decomposition used in practice. Its value in quantitative finance is in **closed-form sensitivity analysis**: Cramer's rule (which uses the adjoint) expresses how the solution $\mathbf{x} = A^{-1}\mathbf{b}$ changes with small perturbations to $A$ or $\mathbf{b}$, providing analytical Greeks for systems where the pricing matrix depends on a risk factor.
