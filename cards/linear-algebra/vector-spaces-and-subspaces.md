# Vector Spaces and Subspaces

**Topic:** Linear Algebra
**Tags:** vector space, subspace, column space, row space, linear algebra, factor models
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **vector space** is a set of vectors closed under addition and scalar multiplication — any linear combination of vectors in the space stays in the space. A **subspace** is a subset of a vector space that is itself a vector space (it must contain the zero vector and be closed under the same operations).

## Key Formula

Four fundamental subspaces are associated with any $m \times n$ matrix $A$:

| Subspace | Definition | Dimension |
|---|---|---|
| Column space $\text{col}(A)$ | All vectors $A\mathbf{x}$, $\mathbf{x} \in \mathbb{R}^n$ | $\text{rank}(A)$ |
| Row space $\text{row}(A)$ | All vectors $A^\top\mathbf{y}$, $\mathbf{y} \in \mathbb{R}^m$ | $\text{rank}(A)$ |
| Null space $\text{null}(A)$ | All $\mathbf{x}$ such that $A\mathbf{x} = \mathbf{0}$ | $n - \text{rank}(A)$ |
| Left null space | All $\mathbf{y}$ such that $A^\top\mathbf{y} = \mathbf{0}$ | $m - \text{rank}(A)$ |

The **rank-nullity theorem** states: $\text{rank}(A) + \text{nullity}(A) = n$.

## Example

For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the column space is all scalar multiples of $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ — a line through the origin in $\mathbb{R}^2$. Since $\text{rank}(A) = 1$, the null space has dimension $2 - 1 = 1$: it is all multiples of $\begin{pmatrix} -2 \\ 1 \end{pmatrix}$ (check: $A\begin{pmatrix} -2 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$).

## Remember

In regression, the column space of the design matrix $X$ is the space of all fitted values $\hat{\mathbf{y}} = X\hat{\boldsymbol{\beta}}$. If two predictor columns are collinear, the column space has lower dimension than expected — the system is rank-deficient and OLS has no unique solution. Understanding the four subspaces of $X$ tells you exactly which directions of $\mathbf{y}$ can be explained by the model and which cannot, which is the geometric foundation of the $R^2$ statistic.
