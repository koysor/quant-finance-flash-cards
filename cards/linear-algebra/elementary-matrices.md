# Elementary Matrices

**Topic:** Linear Algebra
**Tags:** elementary matrices, row operations, lu decomposition, matrix factorisation, gaussian elimination, linear systems
**Author:** Claude Opus 4.6

---

## Definition

An **elementary matrix** is a square matrix obtained by performing a single elementary row operation on the identity matrix $I_n$. There are three types: row swaps, row scaling, and adding a scalar multiple of one row to another. Left-multiplying any matrix $A$ by an elementary matrix $E$ applies the corresponding row operation to $A$.

## Key Formula

If $A$ is reduced to row echelon form $U$ by a sequence of $k$ row operations, each encoded by an elementary matrix $E_i$, then:

$$E_k \cdots E_2 \, E_1 \, A = U$$

Equivalently:

$$A = E_1^{-1} \, E_2^{-1} \cdots E_k^{-1} \, U = LU$$

where $L = E_1^{-1} \, E_2^{-1} \cdots E_k^{-1}$ is lower triangular. Each elementary matrix is invertible, and its inverse is also an elementary matrix — reversing the original row operation.

## Example

Start with $A = \begin{pmatrix} 2 & 6 \\ 1 & 4 \end{pmatrix}$. To eliminate the entry below the pivot, subtract $\tfrac{1}{2}$ times row 1 from row 2.

The corresponding elementary matrix is:

$$E = \begin{pmatrix} 1 & 0 \\ -\tfrac{1}{2} & 1 \end{pmatrix}$$

Applying it: $EA = \begin{pmatrix} 1 & 0 \\ -\tfrac{1}{2} & 1 \end{pmatrix} \begin{pmatrix} 2 & 6 \\ 1 & 4 \end{pmatrix} = \begin{pmatrix} 2 & 6 \\ 0 & 1 \end{pmatrix} = U$.

The inverse is $E^{-1} = \begin{pmatrix} 1 & 0 \\ \tfrac{1}{2} & 1 \end{pmatrix} = L$, giving $A = LU$.

## Remember

Elementary matrices are the bridge between the row operations you perform by hand and the matrix factorisations used in production solvers. In quantitative finance, LU decomposition is the workhorse behind portfolio optimisation, yield curve calibration, and risk system linear solves. The $L$ factor is literally the product of inverted elementary matrices from Gaussian elimination — understanding this link clarifies why pivoting strategies (row swaps) affect numerical stability, which matters when solving thousands of pricing equations each day.
