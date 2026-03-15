# Projection Matrices

**Topic:** Linear Algebra
**Tags:** projection, hat matrix, regression, OLS, residuals, linear algebra
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **projection matrix** (or **orthogonal projector**) $P$ maps any vector onto a subspace along the perpendicular direction. It satisfies two defining properties: $P^2 = P$ (idempotent) and $P^\top = P$ (symmetric). The complementary matrix $I - P$ projects onto the orthogonal complement of that subspace.

## Key Formula

The projection onto the column space of a full-rank matrix $X \in \mathbb{R}^{m \times n}$ is:

$$P = X(X^\top X)^{-1}X^\top$$

This is the **hat matrix** in OLS regression: $\hat{\mathbf{y}} = P\mathbf{y} = X\hat{\boldsymbol{\beta}}$.

The **residual projector** $M = I - P$ produces the residuals:

$$\hat{\mathbf{e}} = M\mathbf{y} = (I - P)\mathbf{y}$$

Key properties:
- $P$ has eigenvalues 0 and 1 only
- $\text{rank}(P) = \text{tr}(P) = n$ (number of predictors)
- $PM = MP = 0$ (fitted values and residuals are orthogonal)

## Example

With $X = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ (intercept-only model), the hat matrix is:

$$P = X(X^\top X)^{-1}X^\top = \frac{1}{3}\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}$$

Then $\hat{\mathbf{y}} = P\mathbf{y}$ gives each observation replaced by $\bar{y}$ — the mean. The residuals $\hat{\mathbf{e}} = \mathbf{y} - \bar{y}\mathbf{1}$ are the deviations from the mean, orthogonal to $X$.

## Remember

In factor model attribution, the hat matrix $P = X(X^\top X)^{-1}X^\top$ decomposes each return into an explained component $P\mathbf{y}$ (factor-driven) and an unexplained component $(I-P)\mathbf{y}$ (idiosyncratic). The trace of $P$ equals the number of factors, providing a measure of model complexity. Leverage points — assets with high diagonal entries $p_{ii}$ of $P$ — have outsized influence on estimated factor loadings, a key diagnostic when building return-based style analysis models.
