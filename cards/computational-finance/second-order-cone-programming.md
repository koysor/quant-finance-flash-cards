# Second-Order Cone Programming (SOCP)

**Topic:** Computational Finance
**Tags:** socp, convex optimisation, robust portfolio, conic programme, quadratic constraint, tractable
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Second-order cone programming (SOCP)** is a class of convex optimisation problems where the feasible region is defined by second-order (Lorentz) cone constraints: $\|\mathbf{A}\mathbf{x} + \mathbf{b}\|_2 \leq \mathbf{c}^\top \mathbf{x} + d$. It generalises linear programming and is solved in polynomial time by interior-point methods.

## Key Formula

The standard SOCP problem:

$$\min_{\mathbf{x}} \;\mathbf{f}^\top \mathbf{x} \quad \text{subject to} \quad \|\mathbf{A}_i \mathbf{x} + \mathbf{b}_i\|_2 \leq \mathbf{c}_i^\top \mathbf{x} + d_i, \quad i = 1, \ldots, m$$

A quadratic constraint $\mathbf{x}^\top \mathbf{Q} \mathbf{x} \leq t$ with $\mathbf{Q} \succeq 0$ is reformulated as an SOCP cone constraint via the Cholesky factor $\mathbf{L}$ of $\mathbf{Q}$: $\|\mathbf{L}^\top \mathbf{x}\|_2 \leq \sqrt{t}$.

## Example

Robust mean-variance optimisation:

$$\max_{\mathbf{w}}\; \hat{\boldsymbol{\mu}}^\top \mathbf{w} - \kappa \|\boldsymbol{\Theta}^{1/2} \mathbf{w}\|_2 - \frac{\gamma}{2}\mathbf{w}^\top \hat{\Sigma} \mathbf{w}$$

The term $-\kappa \|\boldsymbol{\Theta}^{1/2} \mathbf{w}\|_2$ penalises estimation uncertainty (the norm is the SOCP cone); the variance term is handled via a standard QP reformulation. The combined problem is an SOCP solvable with CVXPY in milliseconds for hundreds of assets.

## Remember

SOCP is the mathematical reason that robust portfolio optimisation is computationally feasible at institutional scale. The worst-case return deduction $\kappa\|\boldsymbol{\Theta}^{1/2}\mathbf{w}\|_2$ looks like it would require an expensive inner minimisation, but its convex structure means it can be expressed as a single cone constraint and solved as efficiently as a standard quadratic programme. This is why robust optimisation is not just theoretically appealing but practically deployable — interior-point SOCP solvers handle 1,000-asset universes in under a second.
