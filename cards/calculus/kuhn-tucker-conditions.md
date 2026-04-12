# Kuhn-Tucker Conditions

**Topic:** Calculus
**Tags:** optimisation, inequality-constraints, lagrange-multipliers, portfolio-optimisation, convex-optimisation, complementary-slackness
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

The Kuhn-Tucker (KKT) conditions generalise Lagrange multipliers to handle **inequality constraints**. They are the first-order necessary conditions for a point $x^*$ to be a local minimum of $f(x)$ subject to $g_j(x) \leq b_j$.

Three conditions must hold simultaneously:

1. **Stationarity** — the gradient of the Lagrangian vanishes with respect to each decision variable.
2. **Complementary slackness** — for each constraint, either the constraint is active (binding) or its multiplier is zero.
3. **Non-negativity** — each multiplier $\lambda_j \geq 0$.

The conditions are **necessary** in general. They are **necessary and sufficient** when $f$ is convex and all constraints are linear — the standard portfolio optimisation case.

## Key Formula

For $\min f(x)$ subject to $g_j(x) \leq b_j$, form the Lagrangian:

$$\mathcal{L}(x, \lambda) = \lambda_0 f(x) + \sum_j \lambda_j \bigl(g_j(x) - b_j\bigr)$$

The three KKT conditions are:

$$\text{(1) Stationarity: } \lambda_0 \frac{\partial f}{\partial x_i} + \sum_j \lambda_j \frac{\partial (g_j - b_j)}{\partial x_i} = 0 \quad \forall\, i$$

$$\text{(2) Complementary slackness: } \lambda_j \bigl(g_j(x) - b_j\bigr) = 0 \quad \forall\, j$$

$$\text{(3) Non-negativity: } \lambda_j \geq 0 \quad \forall\, j$$

Complementary slackness means each $\lambda_j$ and $g_j(x) - b_j$ cannot both be non-zero — either the constraint is active ($g_j = b_j$, multiplier free) or it is slack ($g_j < b_j$, so $\lambda_j = 0$).

## Example

**130-30 portfolio with short-sale constraints.**

Allow limited short selling: each asset weight $w_i \geq -0.30$, rewritten as the inequality constraint $-w_i \leq 0.30$.

Because the objective (minimise portfolio variance) is convex and the constraints are linear, KKT conditions are both necessary and sufficient.

**Applying complementary slackness:** if asset $i$ is NOT at its lower bound (i.e.\ $w_i > -0.30$), then the shadow price $\lambda_i = 0$ — the short-sale constraint for that asset costs nothing. Only assets pinned at $-30\%$ carry a positive $\lambda_i$, which represents the marginal cost of tightening that bound.

## Remember

KKT conditions are the mathematical foundation for **constrained mean-variance optimisation (MVO)**. Whenever a portfolio has inequality constraints — short-sale limits, position caps, regulatory thresholds — the optimal solution is characterised by KKT. Complementary slackness gives economic insight: a zero multiplier means the constraint is non-binding and "free"; a positive multiplier measures how much the objective would improve if the constraint were relaxed by one unit. This is the shadow price a portfolio manager places on regulatory limits.
