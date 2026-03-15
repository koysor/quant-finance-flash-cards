# Matrix Subtraction

**Topic:** Linear Algebra
**Tags:** matrix subtraction, element-wise, linear algebra, tracking error, hedging
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Matrix subtraction** subtracts the corresponding entries of one matrix from another, element-wise. As with addition, both matrices must have identical dimensions. Subtraction is not commutative — the order matters.

## Key Formula

For matrices $A$ and $B$ of the same size $m \times n$:

$$(A - B)_{ij} = A_{ij} - B_{ij}$$

Equivalently, $A - B = A + (-B)$, where $-B$ is formed by negating every entry of $B$.

Key properties:
- **Not commutative:** $A - B \neq B - A$ in general
- **Associative with care:** $(A - B) - C = A - B - C$, but $A - (B - C) = A - B + C$
- **Relation to addition:** $A - B = A + (-1)B$

## Example

$$\begin{pmatrix} 5 & 3 \\ 1 & 4 \end{pmatrix} - \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ -2 & 2 \end{pmatrix}$$

Note: $B - A = \begin{pmatrix} -3 & -2 \\ 2 & -2 \end{pmatrix} \neq A - B$.

## Remember

Matrix subtraction is the foundation of **tracking error** analysis. If $\Sigma_p$ is the covariance matrix of a portfolio and $\Sigma_b$ is the covariance matrix of its benchmark, the active covariance matrix is $\Sigma_p - \Sigma_b$, whose diagonal entries measure the variance contribution of each active bet. Similarly, when hedging a bond portfolio, the DV01 vector of the hedge is subtracted from the DV01 vector of the book: $\mathbf{d}_{\text{hedged}} = \mathbf{d}_{\text{book}} - \mathbf{d}_{\text{hedge}}$, with a zero result indicating a perfect hedge.
