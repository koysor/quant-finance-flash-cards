# Reduction to Constant Coefficients

**Topic:** Calculus
**Tags:** ODE, Euler equation, substitution, change of variable, Black-Scholes, heat equation
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The substitution $t = \ln x$ (equivalently $x = e^{t}$) turns an Euler equation into a constant-coefficient equation, which can then be solved by the auxiliary-equation method. The answer must be re-expressed in $x$ at the end.

## Key Formula

$$t = \ln x \;\Longrightarrow\; x\frac{dy}{dx} = \frac{dy}{dt}, \qquad x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} - \frac{dy}{dt}$$

These follow from the chain rule, $\dfrac{dy}{dx} = \dfrac{1}{x}\dfrac{dy}{dt}$, differentiated a second time.

## Example

Solve $x^2 y'' - 2xy' + 2y = 4x^3$. With $t = \ln x$ it becomes $(\ddot{y} - \dot{y}) - 2\dot{y} + 2y = 4e^{3t}$, i.e.

$$\ddot{y} - 3\dot{y} + 2y = 4e^{3t}$$

The complementary function is $Ae^{t} + Be^{2t}$; the trial $Ce^{3t}$ gives $2C = 4$, so $C = 2$. Back-substituting $e^{t} = x$:

$$y = Ax + Bx^2 + 2x^3$$

## Remember

This is the same change of variable, $S = e^{x}$, that turns the Black-Scholes equation into a constant-coefficient PDE and then, with a further transformation, into the heat equation. Rehearsing it on a tractable ODE makes the PDE version routine.
