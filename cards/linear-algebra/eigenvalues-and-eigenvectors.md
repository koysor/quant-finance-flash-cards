# Eigenvalues and Eigenvectors

**Topic:** Linear Algebra
**Tags:** linear algebra, eigenvalues, eigenvectors, PCA, covariance matrix, risk
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

An **eigenvector** of a square matrix $A$ is a non-zero vector $\mathbf{v}$ that, when multiplied by $A$, changes only in scale — not direction. The scaling factor is the corresponding **eigenvalue** $\lambda$. Eigenvectors reveal the "natural axes" along which a linear transformation acts most simply.

## Key Formula

The eigenvalue equation:

$$A\mathbf{v} = \lambda\mathbf{v}$$

Eigenvalues are found by solving the **characteristic equation**:

$$\det(A - \lambda I) = 0$$

For a $2 \times 2$ matrix, this gives a quadratic in $\lambda$. Each eigenvalue is then substituted back to find the corresponding eigenvector.

## Example

Find the eigenvalues of $A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$.

$$\det(A - \lambda I) = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$$

$$\lambda_1 = 5, \quad \lambda_2 = 2$$

For $\lambda_1 = 5$: solving $(A - 5I)\mathbf{v} = \mathbf{0}$ gives $\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

## Remember

In quantitative finance, **Principal Component Analysis (PCA)** decomposes the covariance matrix of asset returns into its eigenvalues and eigenvectors. Each eigenvector is a risk factor (e.g. "overall market level" or "slope of the yield curve"), and its eigenvalue measures how much variance that factor explains. The largest eigenvalue dominates portfolio risk — this is why PCA is used to reduce high-dimensional risk models to a handful of key drivers.
