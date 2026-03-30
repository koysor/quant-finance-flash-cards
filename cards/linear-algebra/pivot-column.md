# Pivot Column

**Topic:** Linear Algebra
**Tags:** pivot column, free variable, row reduction, rank, linear independence
**Author:** Claude Opus 4.6

---

## Definition

A **pivot column** of a matrix is any column that contains a pivot position (a leading 1 in reduced row echelon form, or the first non-zero entry in each row of echelon form). Columns that do not contain a pivot are called **non-pivot** or **free columns** — their corresponding variables can take any value, parameterising the solution set. The distinction between pivot and free columns determines which unknowns in a linear system are uniquely constrained and which remain free.

## Key Formula

After row-reducing an $m \times n$ matrix $A$ with rank $r$:

$$\text{number of pivot columns} = r$$

$$\text{number of free columns} = n - r$$

The general solution to $A\mathbf{x} = \mathbf{b}$ can be written as:

$$\mathbf{x} = \mathbf{x}_p + t_1 \mathbf{v}_1 + t_2 \mathbf{v}_2 + \cdots + t_{n-r} \mathbf{v}_{n-r}$$

where $\mathbf{x}_p$ is a particular solution, $t_1, \ldots, t_{n-r}$ are free parameters corresponding to the free columns, and each $\mathbf{v}_i$ is a null-space basis vector.

## Example

Consider a system with coefficient matrix:

$$A = \begin{pmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

This matrix is already in row echelon form with $r = 2$ pivots in columns 1 and 3.

- **Pivot columns:** 1 and 3 — variables $x_1$ and $x_3$ are determined once the free variables are chosen.
- **Free columns:** 2 and 4 — variables $x_2$ and $x_4$ are free parameters.

Setting $x_2 = s$ and $x_4 = t$, back-substitution gives:

$$x_3 = b_2 - 4t, \qquad x_1 = b_1 - 2s - 3t$$

The two free columns produce a two-dimensional family of solutions — the system is underdetermined.

## Remember

In portfolio replication and hedging, the columns of the exposure matrix represent individual instruments. After row reduction, pivot columns identify the instruments whose positions are uniquely determined by the hedging constraints — these are the independent building blocks of the hedge. Free (non-pivot) columns flag redundant instruments whose weights can be chosen freely without affecting the hedge target. Recognising free columns before solving tells a quant which positions are discretionary, enabling cost or liquidity optimisation across the redundant instruments rather than blindly accepting the first numerical solution.
