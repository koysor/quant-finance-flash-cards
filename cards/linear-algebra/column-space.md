# Column Space

**Topic:** Linear Algebra
**Tags:** column space, image, range, rank, regression, reachable payoffs
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **column space** of a matrix $A$ (also called the **image** or **range** of $A$) is the set of all vectors that can be expressed as $A\mathbf{x}$ for some $\mathbf{x}$ — equivalently, all linear combinations of the columns of $A$. It is a subspace whose dimension equals the rank of $A$.

## Key Formula

$$\text{col}(A) = \{A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n\} = \text{span}\{\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n\}$$

where $\mathbf{a}_1, \ldots, \mathbf{a}_n$ are the columns of $A$. Key facts:

- $\dim(\text{col}(A)) = \text{rank}(A)$
- The system $A\mathbf{x} = \mathbf{b}$ is **consistent** (has at least one solution) if and only if $\mathbf{b} \in \text{col}(A)$
- The column space and left null space of $A$ are orthogonal complements in $\mathbb{R}^m$: $\text{col}(A) \oplus \text{null}(A^\top) = \mathbb{R}^m$
- Row reduction preserves the column space dimension (rank) but not the column space itself

## Example

For $A = \begin{pmatrix}1&2\\2&4\end{pmatrix}$, the columns are $\begin{pmatrix}1\\2\end{pmatrix}$ and $\begin{pmatrix}2\\4\end{pmatrix} = 2\begin{pmatrix}1\\2\end{pmatrix}$.

The column space is just the line $\text{span}\left\{\begin{pmatrix}1\\2\end{pmatrix}\right\}$ — a 1-dimensional subspace of $\mathbb{R}^2$.

$A\mathbf{x} = \begin{pmatrix}3\\5\end{pmatrix}$ has no solution because $\begin{pmatrix}3\\5\end{pmatrix}$ is not a multiple of $\begin{pmatrix}1\\2\end{pmatrix}$ and thus not in $\text{col}(A)$.

## Remember

In derivatives pricing, the column space of the payoff matrix determines which contingent claims are **replicable**. If rows are states of the world and columns are asset payoffs, then $\text{col}(A)$ is the set of all payoffs that can be synthesised as a portfolio — a market is complete if and only if $\text{col}(A) = \mathbb{R}^m$ (every claim can be replicated). In regression, $\hat{\mathbf{y}} = X\hat{\boldsymbol{\beta}}$ is the projection of $\mathbf{y}$ onto $\text{col}(X)$ — the fitted values always lie in the column space of the design matrix, and $R^2$ measures how much of $\mathbf{y}$ lies there.
