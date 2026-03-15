# Upper Triangular Matrix

**Topic:** Linear Algebra
**Tags:** upper triangular, back substitution, gaussian elimination, LU decomposition, QR decomposition
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

An **upper triangular matrix** is a square matrix where every entry **below** the main diagonal is zero — all non-zero entries sit on or above the diagonal. It is the natural output of Gaussian elimination and forward-elimination steps in matrix factorisation.

## Key Formula

$$U = \begin{pmatrix} u_{11} & u_{12} & \cdots & u_{1n} \\ 0 & u_{22} & \cdots & u_{2n} \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & u_{nn} \end{pmatrix}, \quad u_{ij} = 0 \text{ for } i > j$$

A system $U\mathbf{x} = \mathbf{b}$ is solved by **back substitution** — starting from the last row and working upward:

$$x_k = \frac{1}{u_{kk}}\!\left(b_k - \sum_{j=k+1}^{n} u_{kj}\, x_j\right), \quad k = n, n-1, \ldots, 1$$

Cost: $O(n^2)$ — far cheaper than $O(n^3)$ for a general matrix.

## Example

Solve $U\mathbf{x} = \mathbf{b}$:

$$\begin{pmatrix} 2 & 3 & 1 \\ 0 & 4 & 2 \\ 0 & 0 & 5 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 10 \\ 14 \\ 10 \end{pmatrix}$$

**Row 3:** $5x_3 = 10 \Rightarrow x_3 = 2$

**Row 2:** $4x_2 + 2(2) = 14 \Rightarrow x_2 = \tfrac{10}{4} = 2.5$

**Row 1:** $2x_1 + 3(2.5) + 1(2) = 10 \Rightarrow x_1 = \tfrac{0.5}{2} = 0.25$

## Remember

The upper triangular matrix $U$ is the output of Gaussian elimination on $A$ and appears as the $R$ factor in QR decomposition. In quantitative finance, back substitution on $U$ is the final step in solving calibration systems and least-squares problems. Because $U$ can be reused across many right-hand sides $\mathbf{b}$ (different scenario shocks or re-calibration dates), the $O(n^2)$ back substitution cost — after the $O(n^3)$ factorisation is done once — is what makes large-scale risk engine repricing computationally tractable.
