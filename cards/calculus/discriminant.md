# Discriminant

**Topic:** Calculus
**Tags:** discriminant, quadratic, roots, nature of roots, repeated roots, complex roots
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **discriminant** of a quadratic $ax^2 + bx + c$ is the quantity $\Delta = b^2 - 4ac$. It determines the nature of the roots — real and distinct, real and repeated, or complex conjugate pairs — without requiring the full quadratic formula.

## Key Formula

$$\Delta = b^2 - 4ac$$

| Discriminant | Nature of roots |
|---|---|
| $\Delta > 0$ | Two distinct real roots |
| $\Delta = 0$ | One repeated (equal) real root |
| $\Delta < 0$ | Two complex conjugate roots (no real roots) |

**Condition for exactly one solution:** $\Delta = 0$ iff $b^2 = 4ac$.

**Discriminant of a cubic** $ax^3 + bx^2 + cx + d$:

$$\Delta = 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2$$

(positive → three distinct real roots; negative → one real, two complex).

## Example

For which values of $k$ does $kx^2 + 3x + 1 = 0$ have real solutions?

Condition: $\Delta = 9 - 4k \geq 0 \implies k \leq \frac{9}{4}$.

Also need $k \neq 0$ for it to be a quadratic; if $k = 0$ the equation is linear with one real root.

So real solutions exist for $k \leq \frac{9}{4}$.

## Remember

The discriminant governs the structure of solutions in many finance models. The **CIR model** bond pricing ODE has a characteristic equation whose discriminant determines whether the general solution involves real exponentials or oscillatory (complex) terms — a negative discriminant produces complex roots and oscillatory bond prices, which is economically unacceptable and constrains the parameter space. Similarly, the **Heston model's** characteristic function involves a square root $\sqrt{b^2 - 4ac}$; when this discriminant changes sign, the principal branch of the square root must be tracked carefully to avoid discontinuities in the pricing formula.
