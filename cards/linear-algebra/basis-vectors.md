# Basis Vectors

**Topic:** Linear Algebra
**Tags:** basis, basis vectors, dimension, coordinates, PCA, factor models
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **basis** for a vector space (or subspace) is a set of vectors that is both **linearly independent** and **spans** the space — every vector in the space can be written as a unique linear combination of the basis vectors. The number of vectors in any basis is the **dimension** of the space.

## Key Formula

A set $\{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_k\}$ is a basis for a subspace $V$ if:

1. **Spans:** every $\mathbf{v} \in V$ can be written as $\mathbf{v} = c_1\mathbf{b}_1 + \cdots + c_k\mathbf{b}_k$
2. **Independent:** $c_1\mathbf{b}_1 + \cdots + c_k\mathbf{b}_k = \mathbf{0}$ implies $c_1 = \cdots = c_k = 0$

The **standard basis** of $\mathbb{R}^n$ uses the unit coordinate vectors:

$$\mathbf{e}_1 = \begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},\quad \mathbf{e}_2 = \begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix},\quad \ldots,\quad \mathbf{e}_n = \begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}$$

Any vector space has infinitely many possible bases, but all have the same number of elements — the dimension.

## Example

In $\mathbb{R}^2$, the standard basis $\left\{\begin{pmatrix}1\\0\end{pmatrix}, \begin{pmatrix}0\\1\end{pmatrix}\right\}$ and the rotated basis $\left\{\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}, \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}\right\}$ both span $\mathbb{R}^2$ and are linearly independent.

In the rotated basis, the vector $\mathbf{v} = \begin{pmatrix}3\\1\end{pmatrix}$ has coordinates $c_1 = \frac{3+1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} = 2$ and $c_2 = \frac{3-1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} = 1$ — the same vector, different coordinates.

## Remember

PCA replaces the standard basis of asset returns with the **eigenvector basis** of the covariance matrix. In this new basis, each coordinate (principal component) is uncorrelated with the others and has variance equal to the corresponding eigenvalue. The first few basis vectors capture most of the variance — in a 200-asset portfolio, the top 5 principal components might explain 80% of the risk, reducing the effective dimension of the problem from 200 to 5. Choosing the right basis is the core idea behind dimensionality reduction in risk management.
