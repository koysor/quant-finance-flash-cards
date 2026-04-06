# Modulus Equations

**Topic:** Calculus
**Tags:** modulus, absolute value, equations, piecewise, two cases, VaR, inequality
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **modulus equation** contains the absolute value of an expression involving the unknown. It is solved by considering two separate cases — one where the expression inside is non-negative, and one where it is negative — and checking all candidate solutions in the original equation.

## Key Formula

$$|f(x)| = g(x) \implies f(x) = g(x) \quad \text{or} \quad f(x) = -g(x)$$

Note: solutions require $g(x) \geq 0$; any candidate solution violating this must be discarded.

**Modulus inequality:**

$$|f(x)| < k \iff -k < f(x) < k, \qquad |f(x)| > k \iff f(x) < -k \text{ or } f(x) > k$$

## Example

Solve $|2x - 1| = x + 2$.

**Case 1:** $2x - 1 = x + 2 \implies x = 3$. Check: $|5| = 5 = 3 + 2$ ✓

**Case 2:** $2x - 1 = -(x + 2) \implies 2x - 1 = -x - 2 \implies 3x = -1 \implies x = -\tfrac{1}{3}$.

Check: $|-\tfrac{5}{3}| = \tfrac{5}{3}$ and $-\tfrac{1}{3} + 2 = \tfrac{5}{3}$ ✓

Solutions: $x = 3$ and $x = -\tfrac{1}{3}$.

## Remember

**Value at Risk** is fundamentally a modulus inequality. A VaR at 99% confidence means we solve $|r| > \text{VaR}_{99\%}$ (or equivalently $r < -\text{VaR}_{99\%}$) has probability 1%. Finding the threshold that is exceeded only 1% of the time is identical to solving a modulus inequality for a boundary value. **Tracking error** constraints in portfolio management — limiting $|r_{\text{portfolio}} - r_{\text{benchmark}}|$ to within a band — are modulus inequalities solved in exactly the same way as the algebraic case above.
