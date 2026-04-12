# Optimisation Problem Formulation

**Topic:** Calculus
**Tags:** optimisation, objective function, constraints, decision variables, lagrange multipliers, mean-variance optimisation
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

An **optimisation problem** identifies the values of **decision variables** $\mathbf{x}$ that minimise or maximise an **objective function** $f(\mathbf{x})$, subject to a set of **constraints** $g_j(\mathbf{x})$.

Every optimisation problem has three components:

| Component | Role | Finance example |
|---|---|---|
| Objective function $f(\mathbf{x})$ | What to optimise | Minimise portfolio variance $\mathbf{w}'\Sigma\mathbf{w}$ |
| Decision variables $\mathbf{x}$ | What to choose | Portfolio weights $\mathbf{w}$ |
| Constraints $g_j(\mathbf{x})$ | Rules to obey | Budget $\mathbf{w}'\mathbf{1} = 1$, return target $\mathbf{w}'\boldsymbol{\mu} = \mu^*$ |

**Problem types and solution methods:**

| Type | Constraints | Method |
|---|---|---|
| Unconstrained | None | First-order and second-order conditions (FOC/SOC) |
| Equality-constrained | $g_j(\mathbf{x}) = b_j$ | Lagrange multipliers |
| Inequality-constrained | $g_j(\mathbf{x}) \leq b_j$ | Kuhn–Tucker conditions |

## Key Formula

**General form:**

$$\min_{\mathbf{x}} \; f(\mathbf{x}) \quad \text{subject to} \quad g_j(\mathbf{x}) = b_j \; (j = 1, \ldots, m)$$

or with inequality constraints:

$$\min_{\mathbf{x}} \; f(\mathbf{x}) \quad \text{subject to} \quad g_j(\mathbf{x}) \leq b_j \; (j = 1, \ldots, k)$$

**Canonical mean-variance optimisation (MVO) problem:**

$$\min_{\mathbf{w}} \; \tfrac{1}{2}\mathbf{w}'\Sigma\mathbf{w} \quad \text{subject to} \quad \mathbf{w}'\boldsymbol{\mu} = \mu^*, \quad \mathbf{w}'\mathbf{1} = 1$$

where $\mathbf{w}$ is the vector of portfolio weights, $\Sigma$ the covariance matrix, $\boldsymbol{\mu}$ the vector of expected returns, and $\mu^*$ the target return.

## Example

A fund manager wants to find the minimum-variance portfolio that delivers exactly 8% annual return, with weights summing to 1 (fully invested, no leverage).

- **Objective function:** $f(\mathbf{w}) = \tfrac{1}{2}\mathbf{w}'\Sigma\mathbf{w}$ — minimise portfolio variance.
- **Decision variables:** $\mathbf{w} \in \mathbb{R}^n$ — the allocation to each of $n$ assets.
- **Constraints:** $\mathbf{w}'\boldsymbol{\mu} = 0.08$ (return target) and $\mathbf{w}'\mathbf{1} = 1$ (budget).

This is an equality-constrained problem, solved by introducing two Lagrange multipliers — one for each constraint — forming the Lagrangian $\mathcal{L} = \tfrac{1}{2}\mathbf{w}'\Sigma\mathbf{w} + \lambda(\mathbf{w}'\boldsymbol{\mu} - 0.08) + \gamma(\mathbf{w}'\mathbf{1} - 1)$ and solving the FOC system.

## Remember

The **mean-variance optimisation** problem is the canonical equality-constrained optimisation in finance. Correctly identifying the three components — objective, variables, and constraints — determines which solution technique applies. The budget constraint $\mathbf{w}'\mathbf{1} = 1$ and return constraint $\mathbf{w}'\boldsymbol{\mu} = \mu^*$ are equality constraints, so Lagrange multipliers are the appropriate tool. Adding a no-short-selling restriction $w_i \geq 0$ converts the problem to inequality-constrained, requiring Kuhn–Tucker conditions instead.
