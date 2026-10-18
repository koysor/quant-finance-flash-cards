# Homogeneous Constant-Coefficient Second-Order ODEs

**Topic:** Calculus
**Tags:** ODE, second order, constant coefficients, auxiliary equation, damping, mean reversion
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A homogeneous second-order ODE with constant coefficients, $ay'' + by' + cy = 0$, is solved by trying $y = e^{mx}$. Every derivative of $e^{mx}$ is a multiple of itself, so the differential equation becomes the quadratic **auxiliary equation** $am^2 + bm + c = 0$.

## Key Formula

$$ay'' + by' + cy = 0 \;\longrightarrow\; am^2 + bm + c = 0$$

| Roots | General solution |
|---|---|
| Real and distinct, $m_1 \neq m_2$ | $Ae^{m_1 x} + Be^{m_2 x}$ |
| Repeated, $m$ | $(A + Bx)\,e^{mx}$ |
| Complex, $\alpha \pm i\beta$ | $e^{\alpha x}\bigl(A\cos\beta x + B\sin\beta x\bigr)$ |

## Example

Solve $y'' - 4y' + 13y = 0$. The auxiliary equation $m^2 - 4m + 13 = 0$ has $m = \dfrac{4 \pm \sqrt{16 - 52}}{2} = 2 \pm 3i$, so

$$y = e^{2x}\bigl(A\cos 3x + B\sin 3x\bigr)$$

## Remember

The three root cases are the three regimes of any second-order mean-reverting system: over-damped (real roots, monotone decay), critically damped (repeated root) and oscillatory (complex roots, decaying oscillation). The sign of the discriminant $b^2 - 4ac$ tells you which regime a model sits in, and the real part of the roots sets the speed of reversion.
