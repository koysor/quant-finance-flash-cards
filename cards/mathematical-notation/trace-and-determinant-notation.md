# Trace and Determinant Notation

**Topic:** Mathematical Notation
**Tags:** notation, trace, determinant, matrix, covariance, multivariate normal
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **trace** of a square matrix $A$, written $\operatorname{tr}(A)$, is the sum of its diagonal entries. The **determinant** of $A$, written $\det(A)$ or $|A|$, is a scalar that encodes whether $A$ is invertible and captures the "volume scaling" of the linear transformation it represents. Both appear constantly in multivariate probability densities and covariance matrix manipulations.

## Key Formula

For an $n \times n$ matrix $A = (a_{ij})$:

$$\operatorname{tr}(A) = \sum_{i=1}^n a_{ii} = a_{11} + a_{22} + \cdots + a_{nn}$$

$$\det(A) = |A| = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^n a_{i,\sigma(i)}$$

(For $2 \times 2$: $\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc$.)

Key properties used in finance:

| Property | Trace | Determinant |
|---|---|---|
| Cyclic | $\operatorname{tr}(ABC) = \operatorname{tr}(CAB)$ | $\det(AB) = \det(A)\det(B)$ |
| Eigenvalues | $\operatorname{tr}(A) = \sum_i \lambda_i$ | $\det(A) = \prod_i \lambda_i$ |
| Transpose | $\operatorname{tr}(A) = \operatorname{tr}(A^\top)$ | $\det(A) = \det(A^\top)$ |
| Inverse | — | $\det(A^{-1}) = 1/\det(A)$ |

**Multivariate normal density** — both appear together:

$$f(\mathbf{x}) = \frac{1}{(2\pi)^{n/2}\,|\boldsymbol{\Sigma}|^{1/2}} \exp\!\left(-\tfrac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right)$$

## Example

Three-asset covariance matrix $\boldsymbol{\Sigma}$ with variances 0.04, 0.09, 0.01 on the diagonal:

$$\boldsymbol{\Sigma} = \begin{pmatrix} 0.04 & 0.01 & 0.00 \\ 0.01 & 0.09 & 0.02 \\ 0.00 & 0.02 & 0.01 \end{pmatrix}$$

$$\operatorname{tr}(\boldsymbol{\Sigma}) = 0.04 + 0.09 + 0.01 = 0.14 \quad \text{(sum of individual variances)}$$

For an equally-weighted portfolio $\mathbf{w} = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})^\top$:

$$\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w} = \operatorname{tr}(\boldsymbol{\Sigma} \mathbf{w}\mathbf{w}^\top)$$

The cyclic trace identity $\sigma_p^2 = \operatorname{tr}(\boldsymbol{\Sigma}\mathbf{W})$ (where $\mathbf{W} = \mathbf{w}\mathbf{w}^\top$) lets portfolio variance be written as a single trace, which is differentiable with respect to $\mathbf{w}$ using matrix calculus. $\det(\boldsymbol{\Sigma}) \neq 0$ confirms the covariance matrix is invertible (no redundant assets).

## Remember

The determinant $|\boldsymbol{\Sigma}|$ appears in the multivariate normal density as a normalising volume factor — it measures how "spread out" the joint distribution is across all $n$ dimensions simultaneously. A near-zero determinant signals **near-multicollinearity**: two or more assets are almost perfectly correlated, the covariance matrix is nearly singular, and its inverse $\boldsymbol{\Sigma}^{-1}$ becomes numerically unstable. This is the mathematical cause of the Markowitz "optimiser's curse" — small estimation errors in correlations near 1 produce enormous swings in the optimal weights because $\boldsymbol{\Sigma}^{-1}$ amplifies them. The trace gives the total variance (sum of eigenvalues), while the determinant gives the product of eigenvalues (the generalised variance, or "volume" of the confidence ellipsoid). In PCA, the proportion of variance explained by the first $k$ principal components is $\sum_{i=1}^k \lambda_i / \operatorname{tr}(\boldsymbol{\Sigma})$ — a trace ratio.
