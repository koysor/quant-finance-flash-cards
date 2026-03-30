# Pivot

**Topic:** Linear Algebra
**Tags:** pivot, leading entry, echelon form, rank, linear systems
**Author:** Claude Opus 4.6

---

## Definition

A **pivot** (or **leading entry**) is the first non-zero element in each non-zero row of a matrix that has been reduced to row echelon form. Pivots always lie strictly to the right of the pivot in the row above. The number of pivots equals the rank of the matrix, and the columns containing pivots are called **pivot columns** — their corresponding variables are uniquely determined by the system.

## Key Formula

After row reduction of an $m \times n$ matrix $A$, the pivots sit on the staircase of the echelon form:

$$\begin{pmatrix} \boxed{a_{11}} & * & * & * \\ 0 & \boxed{a_{22}} & * & * \\ 0 & 0 & 0 & \boxed{a_{34}} \end{pmatrix}$$

Key relationships:

$$\text{rank}(A) = \text{number of pivots}$$

$$\text{number of free variables} = n - \text{number of pivots}$$

A square $n \times n$ matrix is invertible if and only if it has $n$ pivots — one in every column.

## Example

Row-reduce the coefficient matrix of a three-asset hedging problem:

$$A = \begin{pmatrix} 1 & 3 & 2 \\ 2 & 6 & 5 \\ 1 & 3 & 4 \end{pmatrix}$$

**R2 ← R2 − 2·R1, R3 ← R3 − R1:**

$$\begin{pmatrix} \boxed{1} & 3 & 2 \\ 0 & 0 & \boxed{1} \\ 0 & 0 & 2 \end{pmatrix}$$

**R3 ← R3 − 2·R2:**

$$\begin{pmatrix} \boxed{1} & 3 & 2 \\ 0 & 0 & \boxed{1} \\ 0 & 0 & 0 \end{pmatrix}$$

There are **2 pivots** (in columns 1 and 3), so $\text{rank}(A) = 2$. Column 2 has no pivot, making the second hedge ratio a free variable — one of the three assets is redundant.

## Remember

When constructing a replicating portfolio or calibrating a multi-instrument hedge, each pivot in the echelon form of the constraint matrix corresponds to an instrument whose contribution is uniquely determined. Columns without pivots identify redundant instruments — assets that add no independent hedging power and whose weights can be set freely. Counting pivots before attempting a numerical solve instantly reveals whether the hedging problem is fully determined, underdetermined (fewer pivots than unknowns), or inconsistent (a pivot appears in the augmented column), saving computation and preventing silent failures in production risk systems.
