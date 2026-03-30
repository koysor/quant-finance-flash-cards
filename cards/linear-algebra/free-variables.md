# Free Variables

**Topic:** Linear Algebra
**Tags:** free variables, pivot, rank, null space, calibration, underdetermined systems
**Author:** Claude Opus 4.6

---

## Definition

A **free variable** is a variable in a system of linear equations whose corresponding column in the row echelon form contains no pivot. Free variables can take any real value and parameterise the solution set — each free variable adds one degree of freedom, so the number of free variables equals the dimension of the null space (the nullity).

## Key Formula

After row-reducing the coefficient matrix $A \in \mathbb{R}^{m \times n}$, let $r$ denote the number of pivots. The number of free variables is:

$$\text{free variables} = n - r = n - \text{rank}(A) = \text{nullity}(A)$$

If the system $A\mathbf{x} = \mathbf{b}$ is consistent and has $k$ free variables, the general solution is:

$$\mathbf{x} = \mathbf{x}_p + c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$$

where $\mathbf{x}_p$ is a particular solution, $\mathbf{v}_1, \ldots, \mathbf{v}_k$ are null-space basis vectors, and $c_1, \ldots, c_k \in \mathbb{R}$ are arbitrary constants.

## Example

Solve $A\mathbf{x} = \mathbf{b}$ where $A = \begin{pmatrix} 1 & 3 & 1 \\ 2 & 6 & 4 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 4 \\ 12 \end{pmatrix}$.

Row-reduce the augmented matrix:

$$\begin{pmatrix} 1 & 3 & 1 & 4 \\ 2 & 6 & 4 & 12 \end{pmatrix} \xrightarrow{R_2 - 2R_1} \begin{pmatrix} 1 & 3 & 1 & 4 \\ 0 & 0 & 2 & 4 \end{pmatrix}$$

Pivots are in columns 1 and 3, so $x_1$ and $x_3$ are **pivot variables** and $x_2$ is the **free variable**. From row 2: $x_3 = 2$. From row 1: $x_1 = 4 - 3x_2 - 2 = 2 - 3x_2$. Setting $x_2 = t$:

$$\mathbf{x} = \begin{pmatrix} 2 \\ 0 \\ 2 \end{pmatrix} + t\begin{pmatrix} -3 \\ 1 \\ 0 \end{pmatrix}, \quad t \in \mathbb{R}$$

The system has one free variable ($x_2$), confirming nullity $= 3 - 2 = 1$.

## Remember

In quantitative finance, free variables arise whenever a problem is **underdetermined** — more unknowns than independent constraints. When calibrating a volatility surface model with fewer liquid market quotes than model parameters, the free variables represent the directions in parameter space that market data leaves unconstrained. A hedger constructing a delta-gamma-neutral portfolio from more instruments than Greeks to match also faces free variables: the extra degrees of freedom can be used to minimise transaction costs or maximise carry. Recognising how many free variables exist — and what they represent — is the first step toward imposing sensible regularisation or secondary objectives.
