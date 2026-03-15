# Linear Combinations

**Topic:** Linear Algebra
**Tags:** linear combination, scalars, vectors, span, portfolio weights, factor models
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **linear combination** of vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$ is any vector of the form $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$, where $c_1, c_2, \ldots, c_k$ are real scalars. Linear combinations are the fundamental building block of linear algebra — every operation (span, subspaces, matrix-vector products) is ultimately a statement about which linear combinations are possible.

## Key Formula

$$\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \sum_{i=1}^k c_i \mathbf{v}_i$$

Matrix-vector multiplication is a compact expression for a linear combination of the columns of $A$:

$$A\mathbf{x} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n$$

where $\mathbf{a}_j$ is the $j$-th column of $A$ and $x_j$ is the $j$-th entry of $\mathbf{x}$. The system $A\mathbf{x} = \mathbf{b}$ has a solution if and only if $\mathbf{b}$ can be written as a linear combination of the columns of $A$.

## Example

Are $\mathbf{b} = \begin{pmatrix}5\\7\end{pmatrix}$ a linear combination of $\mathbf{v}_1 = \begin{pmatrix}1\\2\end{pmatrix}$ and $\mathbf{v}_2 = \begin{pmatrix}3\\1\end{pmatrix}$?

Solve $c_1 + 3c_2 = 5$ and $2c_1 + c_2 = 7$. From the second: $c_2 = 7 - 2c_1$. Substituting: $c_1 + 3(7-2c_1) = 5 \Rightarrow -5c_1 = -16 \Rightarrow c_1 = 3.2$, $c_2 = 0.6$.

Check: $3.2\begin{pmatrix}1\\2\end{pmatrix} + 0.6\begin{pmatrix}3\\1\end{pmatrix} = \begin{pmatrix}5\\7\end{pmatrix}$ ✓

## Remember

A portfolio is literally a linear combination of asset return vectors: $r_p = w_1 r_1 + w_2 r_2 + \cdots + w_n r_n$, where the weights $w_i$ are the scalars. Factor models express each asset return as a linear combination of factor returns plus an idiosyncratic term: $r_i = \beta_{i1}f_1 + \beta_{i2}f_2 + \cdots + \varepsilon_i$. The question of whether a target payoff can be replicated by a portfolio is precisely the question of whether it lies in the span — the set of all linear combinations — of the available assets.
