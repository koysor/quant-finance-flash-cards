# Matrices: Definition and Notation

**Topic:** Linear Algebra
**Tags:** matrix, notation, order, square matrix, symmetric, identity, covariance
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A **matrix** is a rectangular array of numbers. Its **order** is rows $\times$ columns, and the order decides which products and sums are defined.

## Key Formula

$$A = (a_{ij}), \qquad A \text{ is } m \times n: \; m \text{ rows},\; n \text{ columns}$$

| Term | Meaning |
|---|---|
| $a_{ij}$ | Entry in row $i$, column $j$ |
| Square | $m = n$; only square matrices have a determinant or an inverse |
| Symmetric | $A^{\top} = A$ |
| Diagonal | Zero away from the leading diagonal |
| Identity $I$ | Ones on the diagonal, $AI = IA = A$ |

## Example

$$\Sigma = \begin{pmatrix} 0.04 & 0.012 \\ 0.012 & 0.09 \end{pmatrix}$$

is $2 \times 2$ and symmetric. A $2 \times 3$ matrix cannot be multiplied on the right by another $2 \times 3$ matrix, but it can be multiplied by a $3 \times k$ matrix, giving a $2 \times k$ result.

## Remember

The covariance matrix $\Sigma$ has $\Sigma_{ij} = \mathrm{Cov}(X_i, X_j)$. Because $\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$ it is symmetric by construction, and square because every asset pairs with every asset. It is the central object of portfolio theory and of principal component analysis.
