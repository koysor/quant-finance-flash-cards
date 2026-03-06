# Condition Number

**Topic:** Linear Algebra
**Tags:** condition number, numerical stability, matrix inverse, covariance matrix, ill-conditioned
**Author:** Claude Opus 4.6

---

## Definition

The **condition number** of a matrix measures how sensitive its inverse (or the solution of a linear system) is to small perturbations in the input. A matrix with a large condition number is called **ill-conditioned** — tiny changes in data produce large changes in the result. For a symmetric positive definite matrix, the condition number is the ratio of the largest to the smallest eigenvalue.

## Key Formula

$$\kappa(A) = \|A\| \cdot \|A^{-1}\| = \frac{\lambda_{\max}}{\lambda_{\min}}$$

where $\lambda_{\max}$ and $\lambda_{\min}$ are the largest and smallest eigenvalues of $A$.

**Rule of thumb:** if $\kappa(A) \approx 10^k$, you may lose approximately $k$ digits of precision when solving $A\mathbf{x} = \mathbf{b}$.

A **well-conditioned** matrix has $\kappa$ close to 1. An **ill-conditioned** matrix has $\kappa \gg 1$.

## Example

A covariance matrix for two highly correlated assets ($\rho = 0.999$):

$$\Sigma = \begin{pmatrix} 0.04 & 0.03996 \\ 0.03996 & 0.04 \end{pmatrix}$$

Eigenvalues: $\lambda_1 = 0.07996$, $\lambda_2 = 0.00004$.

$$\kappa(\Sigma) = \frac{0.07996}{0.00004} = 1999$$

A 0.1% change in an input could produce a 200% change in the optimised portfolio weights — the matrix is ill-conditioned.

For a moderately correlated pair ($\rho = 0.5$): $\kappa = 3$ — well-conditioned and stable.

## Remember

In portfolio optimisation, the covariance matrix $\Sigma$ must be inverted to find the optimal weights: $\mathbf{w}^* \propto \Sigma^{-1} \boldsymbol{\mu}$. When assets are highly correlated, $\Sigma$ becomes ill-conditioned and the inverse amplifies estimation noise into wildly unstable weights — the optimiser takes enormous long-short positions to exploit tiny estimated return differences. This is the mathematical reason why Markowitz optimisation is often called an "error maximiser". Shrinkage, factor models, and eigenvalue clipping all work by reducing the condition number of $\Sigma$, making the inversion stable and the resulting portfolio weights sensible.
