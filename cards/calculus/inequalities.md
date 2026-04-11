# Inequalities

**Topic:** Calculus
**Tags:** inequalities, linear inequality, quadratic inequality, sign table, critical values
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

An **inequality** states that one expression is greater than (or less than, or equal to) another. Solving an inequality produces a **set of values** rather than a single solution. For **linear inequalities**, the method mirrors equation solving, but multiplying or dividing by a **negative number reverses the inequality sign**. For **quadratic inequalities**, find the critical values (roots) then use a sign table or sketch to determine which intervals satisfy the inequality.

## Key Formula

**Linear inequality:** treat like an equation but flip the sign when multiplying/dividing by a negative.

**Quadratic inequality** $ax^2 + bx + c > 0$:
1. Find roots $\alpha, \beta$ where $\alpha < \beta$.
2. If $a > 0$: solution is $x < \alpha$ or $x > \beta$ (curve opens upward, positive outside the roots).
3. If $a > 0$: for $ax^2 + bx + c < 0$, solution is $\alpha < x < \beta$.

**Modulus inequality:** $|x - a| < b \iff a - b < x < a + b$.

**Interval notation:** $(a, b) = \{x : a < x < b\}$, $[a, b] = \{x : a \leq x \leq b\}$.

## Example

Solve $x^2 - 5x + 6 > 0$.

Roots: $x = 2, x = 3$. Coefficient of $x^2$ is positive, so the parabola opens upward.

Solution: $x < 2$ or $x > 3$.

**Modulus example:** $|2x - 1| \leq 3 \iff -3 \leq 2x - 1 \leq 3 \iff -1 \leq x \leq 2$.

## Remember

Inequalities are the language of **risk constraints and regulatory limits** in quantitative finance. A portfolio is feasible if weights satisfy $w_i \geq 0$ (long-only constraint) and $\sum w_i = 1$ — the feasible region is an intersection of linear inequalities defining the **simplex**. VaR limits, leverage caps, and concentration limits are all inequalities on portfolio statistics. Quadratic inequality thinking also underpins **option moneyness**: $S_T > K$ (call expires in the money) defines a region of the sample space, and its probability $Q(S_T > K) = N(d_2)$ is the integral over that inequality region.
