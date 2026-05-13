# Eigenvalue Deflation

**Topic:** Linear Algebra
**Tags:** eigenvalue deflation, pca, power iteration, eigenvectors, factor models, dimensionality reduction
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Eigenvalue deflation** removes the contribution of a known eigenpair from a matrix, exposing the next dominant eigenvalue to power iteration. Applied repeatedly, it transforms the iterative algorithm into a full eigenvector extraction procedure, extracting principal components one at a time.

## Key Formula

Given the dominant eigenpair $(\lambda_1, \mathbf{v}_1)$ of a symmetric matrix $\mathbf{A}$, with $\mathbf{v}_1$ normalised ($\|\mathbf{v}_1\| = 1$), the **deflated matrix** is:

$$\mathbf{A}' = \mathbf{A} - \lambda_1\, \mathbf{v}_1 \mathbf{v}_1^\top$$

$\mathbf{A}'$ shares all eigenvectors with $\mathbf{A}$ but with the first eigenvalue zeroed out — the spectrum shifts from $\{\lambda_1, \lambda_2, \ldots\}$ to $\{0, \lambda_2, \ldots\}$. Power iteration on $\mathbf{A}'$ now converges to $(\lambda_2, \mathbf{v}_2)$.

## Example

A $3 \times 3$ covariance matrix of equity returns has eigenpairs $(\lambda_1 = 5.2, \mathbf{v}_1)$, $(\lambda_2 = 1.8, \mathbf{v}_2)$, $(\lambda_3 = 0.4, \mathbf{v}_3)$.

**Step 1:** Power iteration → $(\lambda_1 = 5.2, \mathbf{v}_1)$.  
**Step 2:** Deflate: $\mathbf{A}' = \mathbf{A} - 5.2\,\mathbf{v}_1\mathbf{v}_1^\top$. Spectrum of $\mathbf{A}'$: $\{0, 1.8, 0.4\}$.  
**Step 3:** Power iteration on $\mathbf{A}'$ → $(\lambda_2 = 1.8, \mathbf{v}_2)$.  
**Step 4:** Deflate again to expose $\lambda_3 = 0.4$.

## Remember

Deflation is the operation that makes iterative PCA a practical algorithm for financial risk management. The first principal component of an asset return covariance matrix typically captures the broad market factor; deflating it away exposes the second component (often a size or sector factor); further deflations reveal additional factors. Without deflation, power iteration would return the same dominant market factor on every run. The deflation formula $\mathbf{A} - \lambda_1 \mathbf{v}_1 \mathbf{v}_1^\top$ is one term of the spectral decomposition $\mathbf{A} = \sum_i \lambda_i \mathbf{v}_i \mathbf{v}_i^\top$ being peeled off iteratively.
