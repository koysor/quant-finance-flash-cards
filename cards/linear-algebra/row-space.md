# Row Space

**Topic:** Linear Algebra
**Tags:** row space, fundamental subspaces, rank, transpose, factor models, dimensionality
**Author:** Claude Opus 4.6

---

## Definition

The **row space** of a matrix $A$ is the set of all linear combinations of its rows — equivalently, the column space of $A^\top$. Together with the column space, null space, and left null space, it forms one of the **four fundamental subspaces** of a matrix. Its dimension equals the rank of $A$.

## Key Formula

$$\text{row}(A) = \text{col}(A^\top) = \text{span}\{\mathbf{r}_1, \mathbf{r}_2, \ldots, \mathbf{r}_m\}$$

where $\mathbf{r}_1, \ldots, \mathbf{r}_m$ are the rows of $A$. Key facts:

- $\dim(\text{row}(A)) = \text{rank}(A) = \dim(\text{col}(A))$
- Row reduction **preserves** the row space: if $R$ is the row echelon form of $A$, then $\text{row}(R) = \text{row}(A)$
- The row space and null space are **orthogonal complements** in $\mathbb{R}^n$: $\text{row}(A) \oplus \text{null}(A) = \mathbb{R}^n$
- Every $\mathbf{x} \in \mathbb{R}^n$ decomposes uniquely as $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ where $\mathbf{x}_r \in \text{row}(A)$ and $\mathbf{x}_n \in \text{null}(A)$

## Example

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$. Row reduction gives $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{pmatrix}$, so $\text{rank}(A) = 1$.

The row space is the line:

$$\text{row}(A) = \text{span}\!\left\{\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}\right\} \subset \mathbb{R}^3$$

The null space has dimension $3 - 1 = 2$. Every vector in $\mathbb{R}^3$ splits into a component along $(1, 2, 3)$ and a component orthogonal to it, confirming $\text{row}(A) \oplus \text{null}(A) = \mathbb{R}^3$.

## Remember

In factor models such as PCA-based risk decomposition, the row space of the factor loading matrix $B$ spans the directions in asset space that are **explained by the factors**. If $B$ is $k \times n$ (factors by assets), then $\text{row}(B)$ is the $k$-dimensional subspace of $\mathbb{R}^n$ capturing systematic risk, while the null space of $B$ contains the portfolio weights that are **factor-neutral** — immune to all modelled risk factors. Identifying the row space tells a portfolio manager exactly which dimensions of risk the model can see.
