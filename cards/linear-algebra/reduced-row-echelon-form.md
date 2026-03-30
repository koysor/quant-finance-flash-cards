# Reduced Row Echelon Form

**Topic:** Linear Algebra
**Tags:** reduced row echelon form, gauss-jordan elimination, pivot variables, free variables, calibration, linear systems
**Author:** Claude Opus 4.6

---

## Definition

Reduced row echelon form (RREF) is the canonical end-state of Gauss-Jordan elimination: a matrix in which every leading entry (pivot) is 1, each pivot is the only non-zero entry in its column, and pivot columns move strictly to the right as you move down the rows. Any zero rows sit at the bottom.

## Key Formula

A matrix is in RREF when it satisfies all four conditions simultaneously:

1. Every leading entry in a non-zero row is $1$.
2. Each leading $1$ is the only non-zero entry in its column.
3. The leading $1$ in each row is to the right of the leading $1$ in the row above.
4. All zero rows are at the bottom.

For example, the $3 \times 4$ augmented matrix below is in RREF:

$$
\begin{bmatrix} 1 & 0 & 2 & 3 \\ 0 & 1 & -1 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Columns 1 and 2 are **pivot columns** (corresponding to pivot variables), while column 3 is a **free column** (the associated variable can take any value).

## Example

Solve $x_1 + 2x_2 + x_3 = 5$ and $2x_1 + 5x_2 + 3x_3 = 13$ by reducing the augmented matrix to RREF.

$$
\begin{bmatrix} 1 & 2 & 1 & 5 \\ 2 & 5 & 3 & 13 \end{bmatrix}
\xrightarrow{R_2 \to R_2 - 2R_1}
\begin{bmatrix} 1 & 2 & 1 & 5 \\ 0 & 1 & 1 & 3 \end{bmatrix}
\xrightarrow{R_1 \to R_1 - 2R_2}
\begin{bmatrix} 1 & 0 & -1 & -1 \\ 0 & 1 & 1 & 3 \end{bmatrix}
$$

The RREF reveals two pivot variables ($x_1$, $x_2$) and one free variable ($x_3 = t$). The general solution is $x_1 = -1 + t$, $x_2 = 3 - t$, $x_3 = t$.

## Remember

In quantitative finance, underdetermined systems appear whenever you calibrate a model with more parameters than constraints -- for instance, fitting a volatility surface with more knot points than market quotes. RREF cleanly separates pivot variables (uniquely determined by the data) from free variables (degrees of freedom you must fix by adding regularisation or economic judgement). If the system reaches RREF with no zero row contradicting the right-hand side, a solution exists; the number of free columns tells you exactly how many additional constraints you need to pin down a unique calibration.
