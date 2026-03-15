# Associativity

**Topic:** Linear Algebra
**Tags:** associativity, matrix multiplication, order of operations, linear algebra, grouping
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

An operation $\star$ is **associative** if the grouping of operands does not affect the result: $(a \star b) \star c = a \star (b \star c)$. Unlike commutativity, **matrix multiplication is associative** — you can regroup factors freely, though you cannot reorder them.

## Key Formula

For matrices of compatible dimensions:

$$(AB)C = A(BC)$$

This holds even though $AB \neq BA$ in general. The result is independent of how you bracket the product, so the following are all equal:

$$ABCD = (AB)(CD) = A(BC)D = A(BCD)$$

Matrix addition is also associative: $(A + B) + C = A + (B + C)$.

Associativity enables choosing the most **computationally efficient grouping**. For column vector $\mathbf{x}$:

$$A(B\mathbf{x}) \quad \text{costs } O(n^2) \text{ — prefer this}$$
$$(AB)\mathbf{x} \quad \text{requires forming } AB \text{ first at } O(n^3)$$

## Example

Let $A = \begin{pmatrix}1&2\\0&1\end{pmatrix}$, $B = \begin{pmatrix}2&0\\1&3\end{pmatrix}$, $C = \begin{pmatrix}1\\2\end{pmatrix}$.

**(AB)C:**  $AB = \begin{pmatrix}4&6\\1&3\end{pmatrix}$, then $(AB)C = \begin{pmatrix}16\\7\end{pmatrix}$

**A(BC):**  $BC = \begin{pmatrix}2\\7\end{pmatrix}$, then $A(BC) = \begin{pmatrix}16\\7\end{pmatrix}$ ✓

Same result, but $A(BC)$ required two matrix-vector products rather than one matrix-matrix product followed by a matrix-vector product — fewer operations overall.

## Remember

Associativity is what makes efficient computation of expressions like $X^\top X$ in OLS regression tractable. When computing the hat matrix $H = X(X^\top X)^{-1}X^\top$ applied to a vector $\mathbf{y}$, you should evaluate as $X\bigl((X^\top X)^{-1}(X^\top \mathbf{y})\bigr)$ — working right to left — rather than explicitly forming the $n \times n$ matrix $H$ first. This reduces cost from $O(n^2)$ to $O(np)$ where $p \ll n$, a critical saving when $n$ is the number of daily observations and $p$ is the number of factors.
