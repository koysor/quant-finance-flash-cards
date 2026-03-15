# Commutativity

**Topic:** Linear Algebra
**Tags:** commutativity, matrix multiplication, order of operations, linear algebra, non-commutative
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

An operation $\star$ is **commutative** if the order of its operands does not affect the result: $a \star b = b \star a$ for all valid $a$ and $b$. Addition of real numbers and scalars is commutative; **matrix multiplication is generally not**.

## Key Formula

For real scalars: $ab = ba$ ✓

For matrices, in general:

$$AB \neq BA$$

The exception: two matrices commute ($AB = BA$) when:
- One of them is a scalar multiple of the identity: $cI$
- Both are diagonal matrices
- Both are powers of the same matrix: $A^m A^n = A^{m+n} = A^n A^m$
- $B = A^{-1}$ (trivially, $AA^{-1} = I = A^{-1}A$)

Matrix addition **is** commutative: $A + B = B + A$.

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$.

$$AB = \begin{pmatrix} 7 & 2 \\ 3 & 1 \end{pmatrix}, \qquad BA = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$$

$AB \neq BA$ — swapping the order gives a completely different matrix.

## Remember

Non-commutativity of matrix multiplication has direct consequences in quantitative finance. The order of applying risk transformations matters: hedging a portfolio first and then rotating to a new factor basis gives a different result than rotating first and hedging second. Similarly, $(AB)^\top = B^\top A^\top$ — the transpose reverses order — which is why the quadratic form for portfolio variance is $\mathbf{w}^\top \Sigma \mathbf{w}$ and not $\mathbf{w} \Sigma \mathbf{w}^\top$. Always check whether an expression assumes commutativity before rearranging matrix products.
