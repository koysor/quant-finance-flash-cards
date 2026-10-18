# Vector Arithmetic

**Topic:** Linear Algebra
**Tags:** vectors, addition, scalar multiplication, linear combination, portfolio
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Vectors are added and scaled **componentwise**. Any vector built by scaling and adding others is a **linear combination** of them.

## Key Formula

$$\lambda\mathbf{u} + \mu\mathbf{v} = (\lambda u_1 + \mu v_1,\; \dots,\; \lambda u_n + \mu v_n)$$

Addition is commutative, $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$. Vectors are **linearly independent** if none is a linear combination of the others.

## Example

For $\mathbf{u} = (1, -2, 3)$ and $\mathbf{v} = (4, 0, -1)$:

$$3\mathbf{u} - 2\mathbf{v} = (3 - 8,\; -6 - 0,\; 9 + 2) = (-5, -6, 11)$$

The vectors $(1, 2, 3)$ and $(2, 4, 6)$ are **dependent**: the second is twice the first.

## Remember

A portfolio is a linear combination of asset return vectors, with the weights as the scalars $\lambda, \mu$; a long-short portfolio simply has some negative weights. Hedging is finding the weights that make a combination zero, which is possible exactly when the instruments are linearly dependent.
