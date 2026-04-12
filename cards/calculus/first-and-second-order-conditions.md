# First- and Second-Order Conditions

**Topic:** Calculus
**Tags:** optimisation, gradient, hessian, positive definite, multivariate, critical point
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

For an unconstrained function $f(\mathbf{x})$ with $\mathbf{x} \in \mathbb{R}^n$, a **stationary point** $\mathbf{x}^*$ satisfies the **first-order condition (FOC)**: the gradient vanishes at $\mathbf{x}^*$. The **second-order condition (SOC)** uses the **Hessian matrix** — the matrix of all second partial derivatives — to classify the stationary point as a minimum, maximum, or saddle point.

The Hessian $H$ evaluated at $\mathbf{x}^*$ encodes local curvature in every direction: positive definite means the function curves upward in all directions (minimum), negative definite means it curves downward everywhere (maximum), and indefinite means it curves upward in some directions and downward in others (saddle).

## Key Formula

**FOC (necessary):**

$$\nabla_{\mathbf{x}} f(\mathbf{x}^*) = \mathbf{0}$$

**Hessian (second partial derivatives):**

$$H_{ij} = \frac{\partial^2 f}{\partial x_i \, \partial x_j}, \qquad H = \nabla^2 f(\mathbf{x}^*)$$

**SOC (sufficient) — classification at $\mathbf{x}^*$:**

$$H \succ 0 \text{ (positive definite)} \implies \mathbf{x}^* \text{ is a local minimum}$$

$$H \prec 0 \text{ (negative definite)} \implies \mathbf{x}^* \text{ is a local maximum}$$

$$H \text{ indefinite} \implies \mathbf{x}^* \text{ is a saddle point}$$

**Useful identity:** for $f(\mathbf{x}) = \mathbf{x}^\top A \mathbf{x}$ with symmetric $A$:

$$\nabla f = 2A\mathbf{x}, \qquad H = 2A$$

## Example

**Mean-variance portfolio optimisation.** Maximise the utility $f(\mathbf{w}) = \mathbf{w}^\top \boldsymbol{\mu} - \tfrac{\lambda}{2}\,\mathbf{w}^\top \Sigma \mathbf{w}$, where $\boldsymbol{\mu} \in \mathbb{R}^n$ is the vector of expected returns, $\Sigma$ is the $n \times n$ covariance matrix, and $\lambda > 0$ is risk aversion.

**FOC:** differentiate with respect to $\mathbf{w}$ and set to zero:

$$\boldsymbol{\mu} - \lambda \Sigma \mathbf{w} = \mathbf{0} \implies \mathbf{w}^* = \frac{1}{\lambda}\Sigma^{-1}\boldsymbol{\mu}$$

**SOC:** the Hessian of $f$ with respect to $\mathbf{w}$ is $H = -\lambda \Sigma$. Since $\Sigma$ is positive definite (all portfolio variances are strictly positive) and $\lambda > 0$, we have $H \prec 0$ — negative definite — confirming $\mathbf{w}^*$ is a **global maximum**.

## Remember

The FOC/SOC framework is the engine behind every closed-form portfolio solution. In mean-variance optimisation (MVO), setting $\nabla f = \mathbf{0}$ gives the optimal weights $\mathbf{w}^* = \frac{1}{\lambda}\Sigma^{-1}\boldsymbol{\mu}$ directly — no numerical search required. The SOC check reduces to asking whether $\Sigma$ is positive definite, which it always is for non-redundant assets. In practice, if $\Sigma$ is nearly singular (highly correlated assets), the inversion is numerically unstable and the optimum is poorly determined — a real-world reminder that the second-order conditions matter beyond mere formality.
