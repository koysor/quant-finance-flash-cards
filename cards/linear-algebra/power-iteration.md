# Power Iteration

**Topic:** Linear Algebra
**Tags:** power iteration, eigenvalues, eigenvectors, pca, convergence, numerical methods
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Power iteration** is a simple numerical algorithm for finding the dominant eigenpair of a matrix: the eigenvalue $\lambda_1$ with the largest absolute value and its corresponding eigenvector $\mathbf{v}_1$. Starting from a random vector, repeated multiplication by the matrix amplifies the component in the dominant eigenvector direction.

## Key Formula

Initialise $\mathbf{b}_0$ randomly. At each step, multiply by $\mathbf{A}$ and normalise:

$$\mathbf{b}_{k+1} = \frac{\mathbf{A}\, \mathbf{b}_k}{\|\mathbf{A}\, \mathbf{b}_k\|}$$

The corresponding eigenvalue estimate (Rayleigh quotient) at step $k$:

$$\lambda_1 \approx \mathbf{b}_k^\top \mathbf{A}\, \mathbf{b}_k$$

Convergence rate: the error in the eigenvector decays as $\left|\lambda_2 / \lambda_1\right|^k$, so the algorithm is fast when the dominant eigenvalue is well-separated from the second-largest.

## Example

A $3 \times 3$ covariance matrix of equity returns has eigenvalues $\{5.2,\, 1.8,\, 0.4\}$. After 15 iterations of power iteration from a random starting vector, $\mathbf{b}_{15}$ converges to within $10^{-6}$ of the first principal component (the direction of maximum variance). The ratio $|1.8/5.2| \approx 0.35$ means each iteration reduces the error by 65%, giving rapid convergence.

## Remember

Power iteration is the computational engine behind PCA in financial risk management: the first principal component of a covariance matrix of asset returns — found iteratively — typically captures the broad market factor. Deflation (subtracting the contribution of the dominant component) then yields subsequent components for style factors. The same algorithm computes Google PageRank: web pages are scored by the dominant eigenvector of the web's transition matrix, making power iteration one of the most consequential algorithms in applied mathematics.
