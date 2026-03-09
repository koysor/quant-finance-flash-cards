# Singular Value Decomposition

**Topic:** Linear Algebra
**Tags:** SVD, dimensionality reduction, pseudoinverse, noise filtering, matrix factorisation
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

Singular Value Decomposition (SVD) factorises any $m \times n$ matrix $A$ into the product $A = U\Sigma V^\top$, where $U$ is an $m \times m$ orthogonal matrix, $\Sigma$ is an $m \times n$ diagonal matrix of non-negative **singular values**, and $V$ is an $n \times n$ orthogonal matrix. It generalises eigendecomposition to non-square matrices, making it the most broadly applicable matrix factorisation.

## Key Formula

The SVD factorisation:

$$A = U \Sigma V^\top$$

The singular values $\sigma_i$ are the square roots of the eigenvalues of $A^\top A$:

$$\sigma_i = \sqrt{\lambda_i(A^\top A)}$$

The **pseudoinverse** (Moore–Penrose inverse) is constructed via SVD:

$$A^+ = V \Sigma^+ U^\top$$

where $\Sigma^+$ replaces each non-zero singular value $\sigma_i$ with $1/\sigma_i$.

The **truncated SVD** (best rank-$k$ approximation by the Eckart–Young theorem):

$$A_k = U_k \Sigma_k V_k^\top = \sum_{i=1}^{k} \sigma_i \, \mathbf{u}_i \, \mathbf{v}_i^\top$$

## Example

Decompose $A = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$.

Compute $A^\top A = \begin{pmatrix} 9 & 0 \\ 0 & 1 \end{pmatrix}$, which has eigenvalues $\lambda_1 = 9$ and $\lambda_2 = 1$.

The singular values are $\sigma_1 = 3$ and $\sigma_2 = 1$.

Since $A$ is already diagonal with positive entries, $U = I$, $V = I$, and:

$$A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

The largest singular value $\sigma_1 = 3$ tells us the matrix stretches the most in the first coordinate direction — the ratio $\sigma_1 / \sigma_2 = 3$ is the condition number.

## Remember

SVD is the workhorse behind several key techniques in quantitative finance. When the design matrix $X^\top X$ is singular due to multicollinearity among factors, SVD computes the pseudoinverse to produce a least-squares solution without requiring the matrix to be invertible. Truncating small singular values of a sample covariance matrix removes estimation noise, yielding more stable portfolio weights — this is the Eckart–Young theorem applied as a denoising tool. SVD also provides a direct route to PCA: the right singular vectors of the centred returns matrix are the principal components, and the singular values give the standard deviations along each component, all without ever forming the covariance matrix explicitly. For large portfolios where the number of assets exceeds the sample size, this SVD-based PCA is both faster and more numerically stable than eigendecomposing the covariance matrix.
