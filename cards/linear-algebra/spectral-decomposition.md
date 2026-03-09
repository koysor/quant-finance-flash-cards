# Spectral Decomposition

**Topic:** Linear Algebra
**Tags:** spectral decomposition, eigendecomposition, symmetric matrices, PCA, covariance matrix
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The spectral theorem states that every real symmetric matrix $A$ can be decomposed as $A = Q\Lambda Q^\top$, where $Q$ is an orthogonal matrix whose columns are the eigenvectors and $\Lambda$ is a diagonal matrix of the corresponding eigenvalues. This is also called eigendecomposition or diagonalisation.

## Key Formula

The **spectral decomposition** of a real symmetric $n \times n$ matrix:

$$A = Q\Lambda Q^\top$$

where $Q = \begin{pmatrix} \mathbf{q}_1 & \mathbf{q}_2 & \cdots & \mathbf{q}_n \end{pmatrix}$ is orthogonal ($Q^\top Q = I$) and $\Lambda = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$.

Equivalently, the **outer-product form** expresses $A$ as a weighted sum of rank-one matrices:

$$A = \sum_{i=1}^{n} \lambda_i \, \mathbf{q}_i \mathbf{q}_i^\top$$

To reconstruct $A$ from its spectrum, compute each eigenvalue $\lambda_i$ and unit eigenvector $\mathbf{q}_i$, then sum the outer products scaled by the eigenvalues.

## Example

Decompose $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$.

**Step 1 — Eigenvalues.** Solve $\det(A - \lambda I) = 0$:

$$(5 - \lambda)(2 - \lambda) - 4 = \lambda^2 - 7\lambda + 6 = 0$$

$$\lambda_1 = 6, \quad \lambda_2 = 1$$

**Step 2 — Eigenvectors.** For $\lambda_1 = 6$: $(A - 6I)\mathbf{v} = \mathbf{0}$ gives $\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, normalised to $\mathbf{q}_1 = \frac{1}{\sqrt{5}}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

For $\lambda_2 = 1$: $(A - I)\mathbf{v} = \mathbf{0}$ gives $\mathbf{v}_2 = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$, normalised to $\mathbf{q}_2 = \frac{1}{\sqrt{5}}\begin{pmatrix} -1 \\ 2 \end{pmatrix}$.

**Step 3 — Verify.** $Q\Lambda Q^\top = \frac{1}{5}\begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 6 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix} = A \; \checkmark$

## Remember

The covariance matrix $\Sigma$ of asset returns is real and symmetric, so the spectral theorem guarantees $\Sigma = Q\Lambda Q^\top$. This decomposition is exactly **Principal Component Analysis (PCA)** — each eigenvector $\mathbf{q}_i$ is a principal component representing a risk factor (such as "overall market level" or "yield curve slope"), and its eigenvalue $\lambda_i$ is the variance explained by that factor. The decomposition also reveals whether $\Sigma$ is positive semi-definite (all $\lambda_i \ge 0$) and enables **eigenvalue clipping** — setting small or negative eigenvalues to zero — to repair ill-conditioned covariance estimates before feeding them into portfolio optimisation.
