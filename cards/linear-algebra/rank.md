# Rank

**Topic:** Linear Algebra
**Tags:** linear algebra, matrices, rank, nullity, invertibility, portfolio optimisation
**Created:** 2026-02-28 20:46:20
**Author:** Claude Opus 4.6

---

## Definition

The **rank** of a matrix $A$ is the maximum number of linearly independent rows (or, equivalently, columns). It equals the dimension of the **column space** (the span of the columns). A matrix is **full rank** if its rank equals the smaller of its row and column counts; otherwise it is **rank-deficient**. For a square $n \times n$ matrix, full rank means $\text{rank}(A) = n$, which is equivalent to the matrix being invertible.

## Key Formula

**Rank–nullity theorem** — for any $m \times n$ matrix $A$:

$$\text{rank}(A) + \text{nullity}(A) = n$$

where $\text{nullity}(A)$ is the dimension of the null space $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$.

Key equivalences for an $n \times n$ square matrix $A$:

$$\text{rank}(A) = n \iff \det(A) \neq 0 \iff A^{-1} \text{ exists} \iff \text{nullity}(A) = 0$$

## Example

Find the rank of

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 1 \end{pmatrix}$$

**Row-reduce.** Subtract $2 \times R_1$ from $R_2$:

$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

Swap $R_2$ and $R_3$:

$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

There are **2 non-zero rows**, so $\text{rank}(A) = 2$. The matrix is rank-deficient (not full rank for a $3 \times 3$ matrix). By the rank–nullity theorem, $\text{nullity}(A) = 3 - 2 = 1$, confirming a one-dimensional null space.

## Remember

In portfolio optimisation the covariance matrix $\Sigma$ must be inverted to compute optimal weights ($\mathbf{w} \propto \Sigma^{-1}\boldsymbol{\mu}$). If the number of assets $p$ exceeds the number of return observations $T$, the sample covariance matrix has at most rank $T$, making it rank-deficient and singular — the inverse does not exist. This is why practitioners apply **regularisation** (shrinkage estimators such as Ledoit–Wolf), **factor models** (reducing dimensionality so that $\Sigma$ is full rank by construction), or **pseudo-inverses** to stabilise the optimisation.
