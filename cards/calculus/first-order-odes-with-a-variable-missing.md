# First-Order ODEs with One Variable Missing

**Topic:** Calculus
**Tags:** ODE, first order, direct integration, general solution, particular solution
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The simplest first-order equations are those in which the right-hand side contains only one of the two variables, so the equation is an integral in disguise. If $y$ is missing, integrate in $x$ directly. If $x$ is missing, invert the derivative and integrate in $y$.

## Key Formula

$$\frac{dy}{dx} = f(x) \;\Longrightarrow\; y = \int f(x)\,dx \qquad\qquad \frac{dy}{dx} = f(y) \;\Longrightarrow\; x = \int \frac{dy}{f(y)}$$

The **general solution** contains one arbitrary constant; a condition such as $y(x_0) = y_0$ fixes it to give the **particular solution**.

## Example

Solve $\dfrac{dy}{dx} = 3x^2 - 4$ with $y(1) = 2$.

$$y = x^3 - 4x + c, \qquad 2 = 1 - 4 + c \;\Longrightarrow\; c = 5, \qquad y = x^3 - 4x + 5$$

For the $x$-missing case, $\dfrac{dy}{dx} = y$ gives $x = \ln y + c$, i.e. $y = Ae^{x}$.

## Remember

The money-market account $B(t)$ grows at the continuously compounded rate $r$: $\dfrac{dB}{dt} = rB$. With $x$ (here $t$) missing, $t = \tfrac{1}{r}\ln B + c$, so $B(t) = B_0 e^{rt}$. This is the simplest case, and seeing it clearly makes the structure of the harder equations visible.
