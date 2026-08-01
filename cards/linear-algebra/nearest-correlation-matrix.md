# Nearest Correlation Matrix

**Topic:** Linear Algebra
**Tags:** positive definite, eigenvalue clipping, cholesky, correlation matrix, frobenius norm, matrix repair
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

The nearest correlation matrix problem takes an approximate or inconsistent matrix $A$ — one with unit diagonal but at least one negative eigenvalue — and finds the genuine correlation matrix closest to it. It is the standard repair applied when a matrix assembled from rank correlations or patchy data fails to be positive semi-definite.

## Key Formula

Minimise the Frobenius distance over the set of valid correlation matrices:

$$\min_{X} \lVert A - X\rVert_F \quad \text{subject to} \quad X = X',\ \ X \succeq 0,\ \ X_{ii} = 1$$

where $\lVert M\rVert_F^2 = \sum_{i,j} M_{ij}^2$.

The quick approximate fix is **eigenvalue clipping**. Take the spectral decomposition $A = Q\Lambda Q'$, floor the eigenvalues at zero (or a small $\varepsilon$), rebuild, then rescale to restore the unit diagonal:

$$\tilde{A} = Q\,\max(\Lambda,\varepsilon)\,Q', \qquad X_{ij} = \frac{\tilde{A}_{ij}}{\sqrt{\tilde{A}_{ii}\tilde{A}_{jj}}}$$

Clipping is a projection onto the PSD cone but not the true minimiser, since the rescaling step moves the result; Higham's alternating projections method iterates between the PSD cone and the unit-diagonal set to converge on the exact solution.

## Example

Three assets with pairwise correlations $\rho_{12} = 0.9$, $\rho_{13} = 0.9$, $\rho_{23} = -0.9$:

$$A = \begin{pmatrix} 1 & 0.9 & 0.9 \\ 0.9 & 1 & -0.9 \\ 0.9 & -0.9 & 1\end{pmatrix}$$

This is internally contradictory — if 1 moves with 2 and with 3, then 2 and 3 cannot move oppositely. Its eigenvalues are approximately $(1.90,\ 1.72,\ -0.62)$. The negative one is fatal: Cholesky decomposition fails outright, and a portfolio with weights along that eigenvector would compute a **negative variance**.

Clipping at $\varepsilon = 10^{-8}$ and rescaling returns off-diagonals of roughly $(0.74,\ 0.74,\ -0.55)$ — the contradiction has been shared out across all three entries rather than removed from one.

## Remember

This is the step that makes copula sampling possible at all. Both Gaussian and t copula simulation begin with a Cholesky factorisation $\hat\Sigma = AA'$, which requires positive definiteness, and a matrix built from Kendall's tau or Spearman's rho passed through the $\sin$ conversions is fitted entry by entry with no guarantee that the result is jointly consistent. Missing or asynchronous data produces the same failure. The eigenvalue that goes negative is not noise to be suppressed quietly: it is the market telling you that your pairwise estimates cannot all hold simultaneously, so it is worth recording how far the repair moved the matrix. A large adjustment means the correlation inputs — and therefore the basket spreads that depend on them — deserve re-examination rather than a silent patch.
