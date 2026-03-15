# Gaussian Elimination

**Topic:** Linear Algebra
**Tags:** gaussian elimination, linear systems, back substitution, pivoting, numerical methods
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Gaussian elimination** is a systematic algorithm that uses row reduction to transform the augmented matrix $[A \mid \mathbf{b}]$ into upper triangular form, after which the solution to $A\mathbf{x} = \mathbf{b}$ is found by **back substitution**. It is the foundation of nearly all direct linear solvers used in numerical computing.

## Key Formula

The algorithm proceeds in two phases:

**Forward elimination** — for each pivot column $k$, eliminate all entries below the pivot by subtracting a multiple of row $k$ from each lower row:

$$R_i \leftarrow R_i - \frac{a_{ik}}{a_{kk}} R_k, \quad i > k$$

This reduces $[A \mid \mathbf{b}]$ to upper triangular form $[U \mid \mathbf{c}]$.

**Back substitution** — solve from the bottom row upward:

$$x_k = \frac{1}{u_{kk}}\!\left(c_k - \sum_{j=k+1}^{n} u_{kj}\, x_j\right)$$

**Partial pivoting** reorders rows at each step to place the largest available pivot on the diagonal, preventing division by near-zero values.

## Example

Solve $\begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}\mathbf{x} = \begin{pmatrix} 5 \\ 11 \end{pmatrix}$.

**Forward elimination** (R2 ← R2 − 2·R1):

$$\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 0 & 1 & 1 \end{array}\right]$$

**Back substitution:** $x_2 = 1$, then $2x_1 + 1 = 5 \Rightarrow x_1 = 2$.

Solution: $\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

## Remember

Gaussian elimination is at the core of every linear solver in quantitative finance. Calibrating an interest rate curve to $n$ market instruments requires solving an $n \times n$ system; pricing a book of swaps under thousands of scenarios requires solving the same system repeatedly with different right-hand sides $\mathbf{b}$. In practice, solvers factorise the matrix into $LU$ once (via Gaussian elimination) and then exploit the triangular structure for each scenario — this is why LU decomposition and Gaussian elimination are the same algorithm viewed from different angles.
