# Method of Undetermined Coefficients

**Topic:** Calculus
**Tags:** ODE, particular integral, complementary function, forcing term, non-homogeneous
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

To solve a non-homogeneous linear ODE, add the **complementary function** $y_c$ (the general solution of the homogeneous equation: what the system does on its own) to a **particular integral** $y_p$ (any one solution of the full equation: the response to the forcing). The particular integral is found by guessing a trial of the same shape as the forcing term, substituting, and comparing coefficients.

## Key Formula

$$y = y_c + y_p$$

| Forcing term $g(x)$ | Trial $y_p$ |
|---|---|
| $e^{kx}$ | $Ce^{kx}$ |
| Polynomial of degree $n$ | $p_n x^n + \cdots + p_1 x + p_0$ |
| $\sin kx$ or $\cos kx$ | $D\sin kx + E\cos kx$ (both) |
| A sum | The sum of the trials |

## Example

Solve $y'' - 3y' + 2y = e^{5x}$. The auxiliary equation $m^2 - 3m + 2 = 0$ gives $m = 1, 2$, so $y_c = Ae^{x} + Be^{2x}$. Try $y_p = Ce^{5x}$:

$$(25 - 15 + 2)\,C = 1 \;\Longrightarrow\; C = \tfrac{1}{12}$$

so $y = Ae^{x} + Be^{2x} + \tfrac{1}{12}e^{5x}$.

## Remember

The forcing term is the source in the model: a dividend stream, a coupon, an injection of cash. The complementary function is the transient that dies away or oscillates on its own; the particular integral is the long-run response to the source. Separating the two is how you read off the steady state of a funding or mean-reversion model.
