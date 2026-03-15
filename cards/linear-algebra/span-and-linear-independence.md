# Span and Linear Independence

**Topic:** Linear Algebra
**Tags:** linear independence, span, basis, rank, factor models, redundancy
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A set of vectors is **linearly independent** if no vector in the set can be written as a linear combination of the others — equivalently, $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$ only when every $c_i = 0$. The **span** of a set of vectors is the collection of all possible linear combinations of those vectors; it is the smallest subspace containing them all.

## Key Formula

Vectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$ are linearly independent if and only if:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0} \implies c_1 = c_2 = \cdots = c_n = 0$$

Equivalently, the matrix $A = [\mathbf{v}_1 \mid \mathbf{v}_2 \mid \cdots \mid \mathbf{v}_n]$ has full column rank: $\text{rank}(A) = n$.

A **basis** for a subspace is a set of vectors that is both linearly independent and spans the subspace. The number of basis vectors is the **dimension** of the subspace.

## Example

Are $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ and $\mathbf{v}_2 = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$ linearly independent?

Check: $\mathbf{v}_2 = 2\mathbf{v}_1$, so $2\mathbf{v}_1 - \mathbf{v}_2 = \mathbf{0}$ with $c_1 = 2$, $c_2 = -1 \neq 0$. **Linearly dependent.**

Their span is just the line through $\mathbf{v}_1$ — a 1-dimensional subspace, not the full plane.

## Remember

In factor investing, linear independence determines whether your risk factors are genuinely distinct. If a "quality" factor is a linear combination of "value" and "momentum", the three factors are linearly dependent — the covariance matrix is singular, portfolio optimisation breaks down, and you are not actually diversifying across three independent sources of return. Checking for linear independence (via rank) before building a factor model is a standard sanity check in quant research.
