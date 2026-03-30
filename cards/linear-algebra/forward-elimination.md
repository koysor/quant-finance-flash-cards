# Forward Elimination

**Topic:** Linear Algebra
**Tags:** forward elimination, gaussian elimination, upper triangular, pivoting, linear systems, numerical methods
**Author:** Claude Opus 4.6

---

## Definition

**Forward elimination** is the first phase of Gaussian elimination in which elementary row operations are applied column by column, from left to right, to zero out all entries below each pivot. The result is an upper triangular matrix whose diagonal entries form the pivot staircase, ready for back substitution.

## Key Formula

At each pivot column $k = 1, 2, \ldots, n-1$, compute the multiplier for every row $i > k$ and subtract to eliminate the entry below the pivot:

$$m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad R_i \leftarrow R_i - m_{ik}\, R_k$$

After processing all $n-1$ columns, the augmented matrix $[A \mid \mathbf{b}]$ has been reduced to $[U \mid \mathbf{c}]$, where $U$ is upper triangular. The total cost is $\frac{2}{3}n^3 + O(n^2)$ floating-point operations.

## Example

Reduce $\begin{pmatrix} 3 & 1 & 2 \\ 6 & 4 & 1 \\ 9 & 2 & 5 \end{pmatrix}$ to upper triangular form.

**Column 1** — pivot is $a_{11} = 3$:

$m_{21} = 6/3 = 2$, $\;R_2 \leftarrow R_2 - 2R_1$; $\;m_{31} = 9/3 = 3$, $\;R_3 \leftarrow R_3 - 3R_1$:

$$\begin{pmatrix} 3 & 1 & 2 \\ 0 & 2 & -3 \\ 0 & -1 & -1 \end{pmatrix}$$

**Column 2** — pivot is $a_{22} = 2$:

$m_{32} = -1/2$, $\;R_3 \leftarrow R_3 - (-\tfrac{1}{2})R_2 = R_3 + \tfrac{1}{2}R_2$:

$$\begin{pmatrix} 3 & 1 & 2 \\ 0 & 2 & -3 \\ 0 & 0 & -5/2 \end{pmatrix}$$

The matrix is now upper triangular. The multipliers $m_{21}=2$, $m_{31}=3$, $m_{32}=-\tfrac{1}{2}$ are exactly the sub-diagonal entries of $L$ in the LU factorisation.

## Remember

Forward elimination dominates the computational cost of solving $A\mathbf{x} = \mathbf{b}$ at $O(n^3)$, whereas back substitution is only $O(n^2)$. In quantitative finance, LU decomposition caches the result of forward elimination: the multipliers are stored in $L$ and the reduced matrix in $U$, so when repricing a portfolio under thousands of stress scenarios (each with a different $\mathbf{b}$), the expensive $O(n^3)$ forward elimination is performed once and each new scenario costs only $O(n^2)$. This separation is what makes large-scale yield curve calibration and risk aggregation computationally feasible.
