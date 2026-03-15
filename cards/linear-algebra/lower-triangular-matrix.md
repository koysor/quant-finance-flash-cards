# Lower Triangular Matrix

**Topic:** Linear Algebra
**Tags:** lower triangular, forward substitution, LU decomposition, Cholesky decomposition, simulation
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **lower triangular matrix** is a square matrix where every entry **above** the main diagonal is zero — all non-zero entries sit on or below the diagonal. It arises as the $L$ factor in LU decomposition and as the Cholesky factor of a positive definite matrix.

## Key Formula

$$L = \begin{pmatrix} l_{11} & 0 & \cdots & 0 \\ l_{21} & l_{22} & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ l_{n1} & l_{n2} & \cdots & l_{nn} \end{pmatrix}, \quad l_{ij} = 0 \text{ for } i < j$$

A system $L\mathbf{y} = \mathbf{b}$ is solved by **forward substitution** — starting from the first row and working downward:

$$y_k = \frac{1}{l_{kk}}\!\left(b_k - \sum_{j=1}^{k-1} l_{kj}\, y_j\right), \quad k = 1, 2, \ldots, n$$

Cost: $O(n^2)$.

## Example

Solve $L\mathbf{y} = \mathbf{b}$:

$$\begin{pmatrix} 2 & 0 & 0 \\ 3 & 4 & 0 \\ 1 & 2 & 5 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = \begin{pmatrix} 4 \\ 18 \\ 12 \end{pmatrix}$$

**Row 1:** $2y_1 = 4 \Rightarrow y_1 = 2$

**Row 2:** $3(2) + 4y_2 = 18 \Rightarrow y_2 = 3$

**Row 3:** $1(2) + 2(3) + 5y_3 = 12 \Rightarrow y_3 = \tfrac{4}{5} = 0.8$

## Remember

The lower triangular Cholesky factor $L$ of a covariance matrix ($\Sigma = LL^\top$) is the standard tool for generating correlated asset returns in Monte Carlo simulation. Given a vector $\mathbf{z}$ of independent standard normal draws, $L\mathbf{z}$ produces a vector with the correct covariance structure — the lower triangular structure means each simulated return depends only on itself and the assets above it in the ordering, propagating correlation one step at a time. This makes Cholesky-based simulation both mathematically exact and computationally efficient for pricing multi-asset derivatives.
