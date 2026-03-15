# Change of Basis

**Topic:** Linear Algebra
**Tags:** change of basis, coordinates, eigenvectors, PCA, factor models, linear transformations
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **change of basis** re-expresses vectors and linear transformations relative to a new set of basis vectors instead of the standard axes. If $P$ is the matrix whose columns are the new basis vectors, then a vector $\mathbf{x}$ in the original basis has coordinates $\mathbf{x}' = P^{-1}\mathbf{x}$ in the new basis, and a linear transformation $A$ becomes $A' = P^{-1}AP$ in the new basis.

## Key Formula

Given an invertible change-of-basis matrix $P$:

$$\mathbf{x} = P\mathbf{x}' \implies \mathbf{x}' = P^{-1}\mathbf{x}$$

A matrix $A$ in the new basis:

$$A' = P^{-1}AP$$

Two matrices related this way are called **similar** and share the same eigenvalues, determinant, and trace. When $P$ is the matrix of eigenvectors of $A$, the new representation $A' = \Lambda$ is diagonal — this is diagonalisation.

## Example

Let $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$ and change to the basis $P = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ (columns are new basis vectors).

$P^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$

$A' = P^{-1}AP = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix}$

The representation changed but eigenvalues remain $\{3, 2\}$.

## Remember

PCA is a change of basis from the original asset return coordinates to the eigenvector basis of the covariance matrix. In the new basis, each coordinate (principal component) is uncorrelated with the others, and the diagonal entries of $\Lambda$ give each component's variance contribution. Translating factor exposures back to asset weights requires the inverse change of basis $P\mathbf{x}'$, which is how PCA-based risk models convert from factor space back to portfolio weight space for position-level reporting.
