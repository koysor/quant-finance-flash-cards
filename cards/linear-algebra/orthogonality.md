# Orthogonality

**Topic:** Linear Algebra
**Tags:** orthogonality, perpendicular, dot product, subspaces, PCA, uncorrelated factors
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

Two vectors are **orthogonal** if their dot product is zero — they meet at a right angle. More generally, a vector is orthogonal to a subspace if it is orthogonal to every vector in that subspace. An **orthogonal set** is a collection of vectors that are pairwise orthogonal; if each also has unit length, the set is **orthonormal**.

## Key Formula

Vectors $\mathbf{u}$ and $\mathbf{v}$ are orthogonal if and only if:

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = 0$$

The **orthogonal complement** of a subspace $V$ is the set of all vectors perpendicular to every vector in $V$:

$$V^\perp = \{\mathbf{x} : \mathbf{x} \cdot \mathbf{v} = 0 \text{ for all } \mathbf{v} \in V\}$$

Key results:
- $(V^\perp)^\perp = V$
- $\dim(V) + \dim(V^\perp) = n$
- The column space and null space of $A^\top$ are orthogonal complements in $\mathbb{R}^m$
- **Pythagoras:** if $\mathbf{u} \perp \mathbf{v}$ then $\|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$

## Example

Are $\mathbf{u} = \begin{pmatrix} 3 \\ -1 \\ 2 \end{pmatrix}$ and $\mathbf{v} = \begin{pmatrix} 1 \\ 5 \\ 1 \end{pmatrix}$ orthogonal?

$$\mathbf{u} \cdot \mathbf{v} = 3(1) + (-1)(5) + 2(1) = 3 - 5 + 2 = 0 \checkmark$$

Yes — orthogonal. The residual vector in OLS regression is orthogonal to every column of $X$ by the same condition: $X^\top \hat{\mathbf{e}} = \mathbf{0}$.

## Remember

Orthogonality is the geometric reason why PCA factors are uncorrelated. In the eigenvector basis of the covariance matrix, each principal component is orthogonal to every other — their dot products are zero — which translates directly to zero covariance between factors. This makes orthogonal factors the gold standard for risk decomposition: each factor explains a distinct, non-overlapping portion of total variance, and the contributions sum exactly to total portfolio variance by Pythagoras. Whenever two risk factors are "orthogonalised", the process is literally rotating one to be perpendicular to the other.
