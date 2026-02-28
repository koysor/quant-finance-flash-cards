# Trace

**Topic:** Linear Algebra
**Tags:** trace, matrix, eigenvalues, diagonal, linear algebra
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

The trace of a square matrix $A$ is the sum of its diagonal elements. It is a linear operator that is invariant under cyclic permutations and equals the sum of the matrix's eigenvalues. The trace provides a quick scalar summary of a matrix that appears throughout optimisation and statistics.

## Key Formula

For an $n \times n$ matrix $A$:

$$\operatorname{tr}(A) = \sum_{i=1}^{n} a_{ii} = \sum_{i=1}^{n} \lambda_i$$

Key properties:

$$\operatorname{tr}(A + B) = \operatorname{tr}(A) + \operatorname{tr}(B)$$

$$\operatorname{tr}(cA) = c \cdot \operatorname{tr}(A)$$

$$\operatorname{tr}(AB) = \operatorname{tr}(BA)$$

$$\operatorname{tr}(A^\top) = \operatorname{tr}(A)$$

## Example

Let $A = \begin{pmatrix} 5 & 2 & 1 \\ 0 & 3 & -1 \\ 4 & 7 & 6 \end{pmatrix}$.

$\operatorname{tr}(A) = 5 + 3 + 6 = 14$.

The characteristic polynomial gives eigenvalues $\lambda_1 \approx 8.68$, $\lambda_2 \approx 3.66$, $\lambda_3 \approx 1.66$.

Sum of eigenvalues: $8.68 + 3.66 + 1.66 = 14.00$. ✓

## Remember

The trace of a covariance matrix $\operatorname{tr}(\Sigma) = \sum \sigma_i^2$ gives the **total variance** across all assets — a single number summarising overall market risk. In principal component analysis (PCA), each eigenvalue's share of $\operatorname{tr}(\Sigma)$ tells you how much variance that factor explains. The cyclic property $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ is heavily used in matrix calculus for deriving portfolio optimisation gradients, and the identity $\sigma_p^2 = \operatorname{tr}(\mathbf{w}\mathbf{w}^\top \Sigma)$ provides an alternative way to express portfolio variance that generalises neatly to multi-period settings.
