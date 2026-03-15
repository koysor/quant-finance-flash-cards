# Orthogonal Matrices

**Topic:** Linear Algebra
**Tags:** orthogonal matrix, rotation, linear algebra, PCA, matrix decomposition, covariance matrix
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A square matrix $Q$ is **orthogonal** if its transpose equals its inverse: $Q^\top Q = Q Q^\top = I$. Geometrically, orthogonal matrices represent rigid transformations — rotations and reflections — that preserve vector lengths and angles.

## Key Formula

The defining condition:

$$Q^\top Q = I \implies Q^{-1} = Q^\top$$

Consequences:

- $\det(Q) = \pm 1$ (rotation if $+1$, reflection if $-1$)
- $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ for all vectors $\mathbf{x}$ (length-preserving)
- The columns of $Q$ form an **orthonormal basis**: $\mathbf{q}_i \cdot \mathbf{q}_j = \delta_{ij}$

where $\delta_{ij} = 1$ if $i = j$ and $0$ otherwise.

## Example

The $2 \times 2$ rotation matrix through angle $\theta = 45°$:

$$Q = \begin{pmatrix} \cos 45° & -\sin 45° \\ \sin 45° & \cos 45° \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$$

Verify orthogonality:

$$Q^\top Q = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I \checkmark$$

The vector $\mathbf{x} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$ has $\|\mathbf{x}\| = 3$, and $Q\mathbf{x} = \frac{1}{\sqrt{2}}\begin{pmatrix} 3 \\ 3 \end{pmatrix}$ also has $\|Q\mathbf{x}\| = 3$.

## Remember

In quantitative finance, orthogonal matrices appear at the heart of principal component analysis of the covariance matrix: $\Sigma = Q\Lambda Q^\top$, where the columns of $Q$ are orthonormal eigenvectors (principal components). Because $Q$ is orthogonal, the change of basis is numerically clean — no stretching or distortion — which is why PCA factors are uncorrelated and their variance contributions sum exactly to the total portfolio variance. The same property means $Q^{-1} = Q^\top$, making the inverse trivially cheap to compute.
