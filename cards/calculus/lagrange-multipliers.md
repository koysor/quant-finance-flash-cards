# Lagrange Multipliers

**Topic:** Calculus
**Tags:** optimisation, constrained optimisation, shadow price, portfolio selection, lagrangian, first-order conditions
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Lagrange multipliers** convert a constrained optimisation problem into an unconstrained one by forming the **Lagrangian**. Given $m$ equality constraints $g_j(\mathbf{x}) = b_j$, the method introduces one multiplier $\lambda_j$ per constraint and defines:

$$\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_{j=1}^{m} \lambda_j \bigl(g_j(\mathbf{x}) - b_j\bigr)$$

Setting all partial derivatives to zero yields the **first-order conditions (FOC)**: $n$ equations from $\partial \mathcal{L}/\partial x_i = 0$ and $m$ equations from $\partial \mathcal{L}/\partial \lambda_j = 0$, which recover the original constraints. This gives $n + m$ equations in $n + m$ unknowns.

Each $\lambda_j$ is the **shadow price** of constraint $j$: the rate at which the optimal objective value changes as $b_j$ is relaxed by one unit.

## Key Formula

**Lagrangian:**

$$\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_{j=1}^{m} \lambda_j \bigl(g_j(\mathbf{x}) - b_j\bigr)$$

**FOC system:**

$$\frac{\partial \mathcal{L}}{\partial x_i} = 0 \; (i = 1,\ldots,n), \qquad \frac{\partial \mathcal{L}}{\partial \lambda_j} = 0 \iff g_j(\mathbf{x}) = b_j \; (j = 1,\ldots,m)$$

**Mean-variance portfolio Lagrangian** — minimise $\mathbf{w}'\Sigma\mathbf{w}$ subject to $\mathbf{w}'\boldsymbol{\mu} = \mu^*$ and $\mathbf{w}'\mathbf{1} = 1$:

$$\mathcal{L} = \mathbf{w}'\Sigma\mathbf{w} + \lambda(\mathbf{w}'\boldsymbol{\mu} - \mu^*) + \gamma(\mathbf{w}'\mathbf{1} - 1)$$

FOC gives $2\Sigma\mathbf{w} + \lambda\boldsymbol{\mu} + \gamma\mathbf{1} = \mathbf{0}$, so the optimal weights are:

$$\mathbf{w}^* = -\tfrac{1}{2}\Sigma^{-1}(\lambda\boldsymbol{\mu} + \gamma\mathbf{1})$$

## Example

Minimise $f(x, y) = x^2 + y^2$ subject to $x + y = 1$.

Form $\mathcal{L} = x^2 + y^2 + \lambda(x + y - 1)$.

FOC: $2x + \lambda = 0$, $2y + \lambda = 0$, $x + y = 1$.

From the first two equations $x = y$, so $2x = 1 \Rightarrow x = y = \tfrac{1}{2}$, $\lambda = -1$.

The shadow price $\lambda = -1$ means tightening the constraint from $x + y = 1$ to $x + y = 1 - \varepsilon$ reduces the minimum objective value by approximately $\varepsilon$.

## Remember

In **mean-variance optimisation**, $\lambda$ is the shadow price of the return constraint: increasing the target return $\mu^*$ by 1 percentage point raises the minimum achievable portfolio variance by $|\lambda|$. A large $|\lambda|$ signals that the return target is expensive to achieve — the investor is being pushed far from the global minimum-variance portfolio. This gives the shadow price direct economic content: it quantifies the cost, in units of variance, of demanding higher return.
