# Linear Independence

**Topic:** Linear Algebra
**Tags:** linear independence, rank, basis, redundancy, factor models, multicollinearity
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ is **linearly independent** if no vector in the set can be written as a linear combination of the others. Equivalently, the only solution to $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$ is $c_1 = c_2 = \cdots = c_n = 0$.

## Key Formula

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0} \implies c_1 = c_2 = \cdots = c_n = 0$$

Equivalently, the matrix $A = [\mathbf{v}_1 \mid \cdots \mid \mathbf{v}_n]$ has full column rank:

$$\text{rank}(A) = n$$

If $\text{rank}(A) < n$, the vectors are **linearly dependent** — at least one is redundant and can be removed without changing the span.

## Example

A quant researcher proposes three risk factors with monthly returns over four months:

$$\mathbf{f}_1 = \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}, \quad \mathbf{f}_2 = \begin{pmatrix} 2 \\ 4 \\ 6 \\ 8 \end{pmatrix}, \quad \mathbf{f}_3 = \begin{pmatrix} 0 \\ 1 \\ -1 \\ 2 \end{pmatrix}$$

Since $\mathbf{f}_2 = 2\mathbf{f}_1$, we have $2\mathbf{f}_1 - \mathbf{f}_2 + 0\mathbf{f}_3 = \mathbf{0}$ with non-zero coefficients. The set is **linearly dependent** — only two of the three factors are genuinely distinct. The matrix $[\mathbf{f}_1 \mid \mathbf{f}_2 \mid \mathbf{f}_3]$ has rank 2, not 3.

## Remember

In factor investing, linear independence determines whether your risk factors carry genuinely distinct information. If a "quality" factor is a linear combination of "value" and "momentum", the covariance matrix becomes singular, regression coefficients blow up (multicollinearity), and portfolio optimisation fails. Checking rank before building a factor model is a standard sanity check — it tells you how many independent sources of risk you actually have, not just how many labels you assigned.
