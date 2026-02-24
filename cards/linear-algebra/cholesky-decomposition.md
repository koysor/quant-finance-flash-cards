# Cholesky Decomposition

**Topic:** Linear Algebra
**Level:** A Level Mathematics
**Tags:** linear algebra, matrices, Cholesky, Monte Carlo, correlation, simulation

---

## Definition

The **Cholesky decomposition** factorises a symmetric, positive-definite matrix $A$ into the product of a lower triangular matrix $L$ and its transpose: $A = LL^\top$. It is the matrix equivalent of taking a square root — and it is the standard method for introducing correlations into Monte Carlo simulations.

## Key Formula

$$A = LL^\top$$

where $L$ is lower triangular. The elements are computed recursively:

$$L_{jj} = \sqrt{A_{jj} - \sum_{k=1}^{j-1} L_{jk}^2}$$

$$L_{ij} = \frac{1}{L_{jj}}\left(A_{ij} - \sum_{k=1}^{j-1} L_{ik}L_{jk}\right) \quad \text{for } i > j$$

To generate correlated random variables: if $\mathbf{z}$ is a vector of independent standard normals, then $\mathbf{x} = L\mathbf{z}$ has covariance matrix $A$.

## Example

Decompose $\Sigma = \begin{pmatrix} 1 & 0.6 \\ 0.6 & 1 \end{pmatrix}$ (a correlation matrix with $\rho = 0.6$):

$$L_{11} = \sqrt{1} = 1, \quad L_{21} = \frac{0.6}{1} = 0.6, \quad L_{22} = \sqrt{1 - 0.36} = 0.8$$

$$L = \begin{pmatrix} 1 & 0 \\ 0.6 & 0.8 \end{pmatrix}$$

Given independent draws $z_1 = 0.5$, $z_2 = -1.2$:

$$\mathbf{x} = L\mathbf{z} = \begin{pmatrix} 0.5 \\ 0.6(0.5) + 0.8(-1.2) \end{pmatrix} = \begin{pmatrix} 0.5 \\ -0.66 \end{pmatrix}$$

The outputs $x_1$ and $x_2$ are now correlated with $\rho = 0.6$.

## Remember

Multi-asset Monte Carlo simulation requires correlated random shocks — you cannot simply draw independent normals for each asset. The Cholesky decomposition of the correlation matrix converts independent draws into correctly correlated ones in a single matrix multiplication. Without it, a simulation of a two-stock portfolio would ignore diversification effects entirely, producing wrong prices for basket options, worst-of options, and portfolio VaR.
