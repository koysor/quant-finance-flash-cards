# Hessian Notation

**Topic:** Mathematical Notation
**Tags:** notation, hessian, second derivatives, matrix, optimisation, convexity
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Hessian** of a scalar function $f(x_1, \ldots, x_n)$ is the $n \times n$ matrix of all second-order partial derivatives, written $H_f$ or $\nabla^2 f$. It is the multivariable analogue of the second derivative, and its sign-definiteness determines whether a critical point is a minimum, maximum, or saddle point.

## Key Formula

$$H_f = \nabla^2 f = \begin{pmatrix} \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1 \partial x_n} \\[8pt] \dfrac{\partial^2 f}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2 \partial x_n} \\[4pt] \vdots & \vdots & \ddots & \vdots \\[4pt] \dfrac{\partial^2 f}{\partial x_n \partial x_1} & \dfrac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_n^2} \end{pmatrix}$$

The $(i,j)$ entry is $H_{ij} = \partial^2 f / \partial x_i \partial x_j$. When $f$ has continuous second partial derivatives, $H$ is symmetric ($H_{ij} = H_{ji}$, by Schwarz's theorem).

**Second-order conditions** at a critical point $\nabla f = 0$:

| Hessian | Conclusion |
|---|---|
| $H \succ 0$ (positive definite) | Local minimum |
| $H \prec 0$ (negative definite) | Local maximum |
| Indefinite (mixed eigenvalues) | Saddle point |

The notation $H \succ 0$ means all eigenvalues of $H$ are strictly positive; equivalently, $\mathbf{v}^\top H \mathbf{v} > 0$ for all non-zero $\mathbf{v}$.

## Example

Portfolio variance $\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$ for a two-asset portfolio with weights $\mathbf{w} = (w_1, w_2)$:

$$\sigma_p^2 = \sigma_1^2 w_1^2 + 2\rho\sigma_1\sigma_2 w_1 w_2 + \sigma_2^2 w_2^2$$

The Hessian with respect to $\mathbf{w}$ is:

$$H = \begin{pmatrix} 2\sigma_1^2 & 2\rho\sigma_1\sigma_2 \\ 2\rho\sigma_1\sigma_2 & 2\sigma_2^2 \end{pmatrix} = 2\boldsymbol{\Sigma}$$

Since $\boldsymbol{\Sigma}$ is a covariance matrix it is positive semi-definite, so $H \succeq 0$ — portfolio variance is a convex function of the weights. This guarantees the Markowitz minimum-variance problem has a unique global minimum, not just a local one.

## Remember

In quantitative finance the Hessian appears in two contexts. In **options**, the matrix $\Gamma_{ij} = \partial^2 V / \partial S_i \partial S_j$ is the multi-asset gamma — the Hessian of the option price with respect to the underlying prices. Delta-gamma hedging requires knowing this full matrix, not just the diagonal entries $\partial^2 V / \partial S_i^2$, because cross-gammas $\Gamma_{ij}$ for $i \neq j$ represent sensitivity to correlated moves in two underlyings simultaneously (crucial for basket and spread options). In **optimisation**, confirming $H \succ 0$ at a portfolio solution proves the solution is a global minimum, not just a saddle point — a check that is particularly important when non-convex regularisation or integer constraints are introduced.
