# Semidefinite Programming (SDP)

**Topic:** Computational Finance
**Tags:** semidefinite programming, SDP, convex optimisation, positive semidefinite, covariance estimation, factor model
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Semidefinite programming (SDP)** is a class of convex optimisation problems where the decision variable includes a symmetric matrix constrained to be positive semidefinite ($\mathbf{X} \succeq 0$). It generalises both linear programming and second-order cone programming, and is solved in polynomial time by interior-point methods.

## Key Formula

The standard SDP in primal form:

$$\min_{\mathbf{X} \succeq 0} \;\text{tr}(\mathbf{C}\mathbf{X}) \quad \text{subject to} \quad \text{tr}(\mathbf{A}_i \mathbf{X}) = b_i, \quad i = 1, \ldots, m$$

A key special case: finding the nearest positive-semidefinite matrix $\hat{\Sigma}$ to a non-PSD sample covariance $S$ (e.g. from missing data or overlapping windows):

$$\hat{\Sigma} = \arg\min_{\Sigma \succeq 0} \|\Sigma - S\|_F^2$$

which has an analytic solution via eigenvalue clipping: set all negative eigenvalues of $S$ to zero.

## Example

A fixed-income desk estimates a correlation matrix for 30 swap rates from 90 days of overlapping returns. Due to overlapping windows, the matrix has two small negative eigenvalues ($-0.003$ and $-0.007$). Monte Carlo VaR requires a valid (PSD) correlation matrix to generate correlated rate shocks. An SDP projection clips the negative eigenvalues to zero and rescales the eigenvectors, producing the nearest valid correlation matrix. Without this step, the Cholesky decomposition needed for sampling fails entirely.

## Remember

SDP appears in quantitative finance wherever a matrix constraint must be enforced simultaneously with an optimisation objective. The most common cases are: (1) **nearest PSD covariance** — correcting correlation matrices corrupted by missing data, overlapping estimation windows, or rounding; (2) **factor model calibration** — fitting a structured covariance $\Sigma = \mathbf{B}\mathbf{F}\mathbf{B}^\top + \mathbf{D}$ where both $\mathbf{F}$ and $\mathbf{D}$ must be PSD; (3) **robust statistics** — computing minimum-volume ellipsoids that bound a dataset, used in outlier detection for return series. SDP is strictly more expressive than SOCP, but modern solvers (CVXPY with SCS or MOSEK) handle hundreds of variables in seconds.
