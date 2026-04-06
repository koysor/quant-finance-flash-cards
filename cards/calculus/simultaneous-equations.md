# Simultaneous Equations

**Topic:** Calculus
**Tags:** simultaneous equations, systems, elimination, substitution, linear, intersection
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Simultaneous equations** are a set of equations in multiple unknowns that must all be satisfied at the same time. For two equations in two unknowns, the solution is the point(s) of intersection of the corresponding curves. Systems of linear equations are solved by elimination or substitution; one linear and one quadratic may have 0, 1, or 2 solutions.

## Key Formula

**Elimination method:** multiply equations so that a variable has matching coefficients, then add or subtract to eliminate it.

**Substitution method:** express one variable in terms of the other from the simpler equation, substitute into the second.

**Consistency conditions** (two linear equations in two unknowns):

$$a_1x + b_1y = c_1 \quad \text{and} \quad a_2x + b_2y = c_2$$

- Unique solution if $a_1 b_2 \neq a_2 b_1$ (lines intersect).
- No solution if parallel lines; infinitely many if coincident.

## Example

Solve: $2x + y = 7$ and $x^2 + y = 10$.

From the first: $y = 7 - 2x$. Substitute into the second:

$$x^2 + 7 - 2x = 10 \implies x^2 - 2x - 3 = 0 \implies (x-3)(x+1) = 0$$

So $x = 3, y = 1$ or $x = -1, y = 9$.

## Remember

Simultaneous equations are the algebraic core of **portfolio construction**. Finding a portfolio with target return $\mu_P$ and minimum variance requires solving the Lagrangian first-order conditions — a linear system of $n + 2$ equations in $n + 2$ unknowns (portfolio weights plus two multipliers). The **Markowitz two-fund separation theorem** states that all efficient portfolios are linear combinations of just two mutual funds, which is found by solving a $2 \times 2$ simultaneous system. Every quant who has derived the efficient frontier has solved simultaneous equations at its core.
