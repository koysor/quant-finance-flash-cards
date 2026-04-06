# Higher-Order Partial Derivatives

**Topic:** Calculus
**Tags:** partial derivatives, hessian matrix, multivariable calculus, optimisation, gamma
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **higher-order partial derivative** is obtained by partially differentiating a multivariable function more than once. The most important second-order object is the **Hessian matrix** $H$, which collects all second-order partial derivatives of a scalar function $f(x_1, \ldots, x_n)$. The Hessian encodes the local curvature of $f$ in every direction simultaneously, making it the multivariate analogue of the scalar second derivative.

## Key Formula

For $f : \mathbb{R}^n \to \mathbb{R}$, the Hessian is the $n \times n$ symmetric matrix:

$$H_{ij} = \frac{\partial^2 f}{\partial x_i \, \partial x_j}$$

For a two-asset portfolio value $V(S_1, S_2)$, the Hessian of $V$ with respect to the underlying prices is:

$$H = \begin{pmatrix} \dfrac{\partial^2 V}{\partial S_1^2} & \dfrac{\partial^2 V}{\partial S_1 \partial S_2} \\[10pt] \dfrac{\partial^2 V}{\partial S_2 \partial S_1} & \dfrac{\partial^2 V}{\partial S_2^2} \end{pmatrix} = \begin{pmatrix} \Gamma_{11} & \Gamma_{12} \\ \Gamma_{21} & \Gamma_{22} \end{pmatrix}$$

where $\Gamma_{ii}$ is the own-Gamma of asset $i$ and $\Gamma_{ij}$ is the **cross-Gamma** (sensitivity of the delta of asset $i$ to the price of asset $j$).

A critical point $\mathbf{x}^*$ (where $\nabla f = \mathbf{0}$) is:
- a **local minimum** if $H(\mathbf{x}^*)$ is positive definite,
- a **local maximum** if $H(\mathbf{x}^*)$ is negative definite,
- a **saddle point** if $H(\mathbf{x}^*)$ is indefinite.

## Example

Let $V(S_1, S_2) = S_1^2 S_2 + 3 S_1 S_2^2$.

First-order partials:

$$\frac{\partial V}{\partial S_1} = 2S_1 S_2 + 3S_2^2, \qquad \frac{\partial V}{\partial S_2} = S_1^2 + 6S_1 S_2$$

Second-order partials:

$$\frac{\partial^2 V}{\partial S_1^2} = 2S_2, \qquad \frac{\partial^2 V}{\partial S_2^2} = 6S_1, \qquad \frac{\partial^2 V}{\partial S_1 \partial S_2} = 2S_1 + 6S_2$$

At $(S_1, S_2) = (1, 2)$:

$$H = \begin{pmatrix} 4 & 14 \\ 14 & 6 \end{pmatrix}$$

$\det(H) = 24 - 196 = -172 < 0$, so this is a saddle point.

## Remember

In a multi-asset options portfolio, the Hessian of the portfolio value with respect to underlying prices is the **Gamma matrix**. The diagonal entries $\Gamma_{ii}$ are the familiar single-asset Gammas; the off-diagonal entries $\Gamma_{ij}$ are **cross-Gammas** — they capture how the delta of one asset shifts when a different asset moves. Cross-Gammas matter for basket options, spread options, and index derivatives: ignoring them causes systematic under-hedging whenever assets move together. Risk systems at major dealers compute the full Gamma matrix daily to quantify second-order P&L exposure across correlated underlyings.
