# Pivoting Strategies

**Topic:** Linear Algebra
**Tags:** pivoting, numerical stability, gaussian elimination, linear systems, risk models
**Author:** Claude Opus 4.6

---

## Definition

Pivoting strategies are row (or row-and-column) interchange rules applied during Gaussian elimination to avoid dividing by zero or near-zero pivot elements. **Partial pivoting** selects the largest absolute value in the current column below the pivot row and swaps it into the pivot position, while **complete pivoting** searches the entire remaining sub-matrix for the largest entry and swaps both its row and column. Partial pivoting is the standard in practice because it provides excellent numerical stability at negligible extra cost.

## Key Formula

At elimination step $k$, partial pivoting chooses row index $p$ such that

$$|a_{pk}| = \max_{i \ge k} |a_{ik}|$$

then swaps rows $p$ and $k$ before performing the elimination. The resulting factorisation with a permutation matrix $P$ is

$$PA = LU$$

where $P$ records all row swaps, $L$ is unit lower triangular, and $U$ is upper triangular.

## Example

Solve the system where naive elimination would fail:

$$\begin{pmatrix} 0 & 1 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 5 \\ 18 \end{pmatrix}$$

The pivot $a_{11} = 0$, so we cannot divide. Partial pivoting swaps row 1 and row 2:

$$\begin{pmatrix} 3 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 18 \\ 5 \end{pmatrix}$$

Back-substitution gives $x_2 = 5$ and $x_1 = (18 - 4 \times 5) / 3 = -2/3$.

## Remember

Risk engines routinely solve large linear systems — calibrating yield curve models, computing portfolio sensitivities, or inverting covariance matrices for VaR. These systems are often ill-conditioned because nearby maturities produce nearly collinear rows. Without pivoting, tiny pivot elements amplify rounding errors and can produce wildly inaccurate hedging ratios or capital figures. Partial pivoting is the default safeguard in every production-quality linear algebra library (LAPACK, NumPy, MATLAB) precisely because the cost is trivial but the protection against numerical blow-up is essential.
