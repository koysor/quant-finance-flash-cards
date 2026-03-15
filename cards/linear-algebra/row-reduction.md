# Row Reduction

**Topic:** Linear Algebra
**Tags:** row reduction, elementary row operations, echelon form, rank, linear systems
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Row reduction** is the process of applying elementary row operations to a matrix to transform it into **row echelon form** (REF) or **reduced row echelon form** (RREF). The three elementary operations are: swapping two rows, multiplying a row by a non-zero scalar, and adding a multiple of one row to another — none of which changes the solution set of the corresponding linear system.

## Key Formula

A matrix is in **row echelon form** when:

1. All zero rows are at the bottom.
2. Each leading entry (pivot) is strictly to the right of the pivot in the row above.

$$\begin{pmatrix} \mathbf{2} & 3 & -1 \\ 0 & \mathbf{4} & 5 \\ 0 & 0 & \mathbf{7} \end{pmatrix}$$

In **reduced** row echelon form (RREF), each pivot is 1 and is the only non-zero entry in its column. The rank of a matrix equals the number of non-zero rows after row reduction.

## Example

Reduce $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 0 & 1 & 2 \end{pmatrix}$ to row echelon form.

**R2 ← R2 − 2·R1:**

$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}$$

**R3 ← R3 − R2:**

$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$

Three non-zero rows → $\text{rank}(A) = 3$, so $A$ is invertible.

## Remember

Row reduction is the computational workhorse behind many operations in quantitative finance. When calibrating a multi-factor yield curve model, you must solve a system of equations matching market prices to model outputs; row reduction reveals both the solution and whether the system is underdetermined (fewer pivots than unknowns), which would signal that your factors are redundant. The pivot count directly gives the rank, which in portfolio theory tells you how many independent risk factors are genuinely present in your asset returns.
