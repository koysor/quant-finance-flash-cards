# Row Vector

**Topic:** Linear Algebra
**Tags:** row vector, transpose, matrix multiplication, linear combination, portfolio return
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **row vector** is a matrix with a single row — a $1 \times n$ array of numbers. It is written horizontally and is the transpose of a column vector. Row vectors arise naturally when a quantity is expressed as a weighted sum of components, such as a portfolio return or a linear combination of factor exposures.

## Key Formula

$$\mathbf{w}^\top = \begin{pmatrix} w_1 & w_2 & \cdots & w_n \end{pmatrix} \quad (1 \times n)$$

**Row vector times column vector** (dot product, produces a scalar):

$$\mathbf{w}^\top \mathbf{r} = w_1 r_1 + w_2 r_2 + \cdots + w_n r_n \in \mathbb{R}$$

**Row vector times matrix** (produces a row vector):

$$\mathbf{w}^\top A = \text{row vector} \quad (1 \times n)(n \times m) = (1 \times m)$$

**Transpose relationship:** $(\mathbf{w}^\top)^\top = \mathbf{w}$ (column vector).

## Example

A portfolio holds three assets with weights $\mathbf{w}^\top = (0.5,\; 0.3,\; 0.2)$ and today's returns $\mathbf{r} = (0.02,\; -0.01,\; 0.03)^\top$.

$$r_P = \mathbf{w}^\top \mathbf{r} = 0.5(0.02) + 0.3(-0.01) + 0.2(0.03) = 0.010 - 0.003 + 0.006 = 0.013$$

The portfolio returned 1.3% today. The row-times-column multiplication is the natural linear algebra expression for a weighted average.

## Remember

In portfolio mathematics, **the portfolio return is always written as a row vector times a column vector**: $r_P = \mathbf{w}^\top \mathbf{r}$. The convention is that weights $\mathbf{w}$ are stored as a column vector (the natural default), and the transpose $\mathbf{w}^\top$ converts it into a row vector for multiplication against the return column. The portfolio variance $\sigma_P^2 = \mathbf{w}^\top \Sigma \mathbf{w}$ is a row vector times a matrix times a column vector — a scalar — where the row vector on the left and column vector on the right are the same transposed weight vector.
