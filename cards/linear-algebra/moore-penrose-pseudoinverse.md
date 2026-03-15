# Moore-Penrose Pseudoinverse

**Topic:** Linear Algebra
**Tags:** pseudoinverse, least squares, regression, matrix factorisation, rank-deficient, calibration
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The Moore-Penrose pseudoinverse $A^+$ of a matrix $A$ is the unique matrix that acts as a generalised inverse, providing the minimum-norm least-squares solution to a system of equations even when $A$ is non-square or rank-deficient and therefore has no ordinary inverse.

## Key Formula

For a matrix $A \in \mathbb{R}^{m \times n}$ with singular value decomposition $A = U \Sigma V^\top$, the pseudoinverse is:

$$A^+ = V \Sigma^+ U^\top$$

where $\Sigma^+$ is formed by replacing each non-zero singular value $\sigma_i$ with $\frac{1}{\sigma_i}$ and leaving zero singular values as zero.

The minimum-norm least-squares solution to $A\mathbf{x} = \mathbf{b}$ is then:

$$\mathbf{x}^* = A^+ \mathbf{b}$$

When $A$ has full column rank, this reduces to the familiar normal-equations solution:

$$A^+ = (A^\top A)^{-1} A^\top$$

## Example

Suppose a factor model uses a $3 \times 2$ matrix $A$ with SVD giving singular values $\sigma_1 = 4$ and $\sigma_2 = 2$:

$$\Sigma^+ = \begin{pmatrix} 0.25 & 0 & 0 \\ 0 & 0.5 & 0 \end{pmatrix}$$

The pseudoinverse $A^+ = V \Sigma^+ U^\top$ is then a $2 \times 3$ matrix. Applying it to an observation vector $\mathbf{b}$ yields the best-fit factor exposures — the solution that minimises $\|A\mathbf{x} - \mathbf{b}\|^2$ while keeping $\|\mathbf{x}\|$ as small as possible.

## Remember

In quantitative finance, the pseudoinverse appears whenever you have more instruments than risk factors (underdetermined system) or more observations than parameters (overdetermined system). Portfolio replication with a basket of correlated assets often produces a rank-deficient exposure matrix; applying the pseudoinverse gives the minimum-variance hedge that fits the target payoff as closely as possible. It is also the computational backbone of OLS regression, factor model calibration, and any curve-fitting problem where the design matrix may be ill-conditioned.
