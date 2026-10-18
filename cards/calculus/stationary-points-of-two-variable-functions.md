# Stationary Points of Functions of Two Variables

**Topic:** Calculus
**Tags:** stationary points, second derivative test, saddle point, Hessian, optimisation, partial derivatives
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A **stationary point** of $z = f(x, y)$ is a point where both first partial derivatives vanish. The second derivatives then classify it as a local minimum, a local maximum, or a **saddle point** (up in one direction, down in another).

## Key Formula

$$f_x = f_y = 0, \qquad D = f_{xx}\,f_{yy} - f_{xy}^2$$

| Test | Verdict |
|---|---|
| $D > 0$ and $f_{xx} > 0$ | Local minimum |
| $D > 0$ and $f_{xx} < 0$ | Local maximum |
| $D < 0$ | Saddle point |
| $D = 0$ | Test inconclusive; argue another way |

$D$ is the determinant of the Hessian matrix.

## Example

For $f(x, y) = x^3 - 3x + y^2$: $f_x = 3x^2 - 3$ and $f_y = 2y$ vanish at $(1, 0)$ and $(-1, 0)$. With $f_{xx} = 6x$, $f_{yy} = 2$, $f_{xy} = 0$:

- At $(1, 0)$: $D = 12 > 0$ and $f_{xx} = 6 > 0$, a local minimum.
- At $(-1, 0)$: $D = -12 < 0$, a saddle point.

## Remember

Markowitz's minimum-variance portfolio and every multi-parameter maximum likelihood fit (for instance $\mu$ and $\sigma^2$ together) are stationary-point problems in more than one variable. The saddle point is the case a one-variable instinct misses: a point where the gradient is zero but the objective is not at a minimum, which is why optimisers check the Hessian.
