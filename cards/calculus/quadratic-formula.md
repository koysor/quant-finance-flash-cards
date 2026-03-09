# Quadratic Formula

**Topic:** Calculus
**Tags:** quadratic, discriminant, roots, polynomial, algebraic equations
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The quadratic formula gives the roots of any quadratic equation $ax^2 + bx + c = 0$ where $a \neq 0$. The discriminant $\Delta = b^2 - 4ac$ determines the nature and number of real roots.

## Key Formula

**The quadratic formula:**

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Discriminant conditions:**

$$\Delta = b^2 - 4ac \quad \Rightarrow \quad \begin{cases} \Delta > 0 & \text{two distinct real roots} \\ \Delta = 0 & \text{one repeated real root} \\ \Delta < 0 & \text{no real roots (two complex conjugate roots)} \end{cases}$$

**Vieta's formulas** — for roots $x_1$ and $x_2$:

$$x_1 + x_2 = -\frac{b}{a}, \qquad x_1 \cdot x_2 = \frac{c}{a}$$

## Example

Solve $x^2 - 6x + 4 = 0$.

Here $a = 1$, $b = -6$, $c = 4$. Compute the discriminant:

$$\Delta = (-6)^2 - 4(1)(4) = 36 - 16 = 20 > 0$$

Since $\Delta > 0$, there are two distinct real roots:

$$x = \frac{6 \pm \sqrt{20}}{2} = \frac{6 \pm 2\sqrt{5}}{2} = 3 \pm \sqrt{5}$$

So $x_1 = 3 + \sqrt{5} \approx 5.236$ and $x_2 = 3 - \sqrt{5} \approx 0.764$.

**Check with Vieta's formulas:** $x_1 + x_2 = 6 = -(-6)/1$ and $x_1 \cdot x_2 = 9 - 5 = 4 = 4/1$. Correct.

## Remember

Quadratic equations arise naturally in quantitative finance. In mean-variance portfolio optimisation, solving for the portfolio weights that minimise variance subject to a target return leads to a quadratic in the Lagrange multiplier. The characteristic equation of a $2 \times 2$ matrix is a quadratic whose roots are the eigenvalues — essential for principal component analysis of covariance matrices. The discriminant also appears in closed-form solutions for barrier option pricing, where $\Delta < 0$ signals that no real break-even level exists. Whenever you encounter a squared term in a pricing or calibration equation, recognise that the quadratic formula provides an exact analytical solution.
