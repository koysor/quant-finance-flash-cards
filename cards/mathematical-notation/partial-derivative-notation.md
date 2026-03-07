# Partial Derivative Notation

**Topic:** Mathematical Notation
**Tags:** notation, partial derivatives, nabla, gradient, calculus
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Partial derivative notation** expresses the rate of change of a multivariable function with respect to one variable while holding all others fixed. The symbol $\partial$ (a rounded "d") distinguishes partial derivatives from ordinary derivatives, signalling that the function depends on more than one variable.

| Symbol | Read as | Meaning |
|---|---|---|
| $\dfrac{\partial f}{\partial x}$ | "partial f partial x" | Derivative of $f$ with respect to $x$, other variables held fixed |
| $f_x$ or $f_S$ | "f sub x" | Subscript shorthand for $\partial f / \partial x$ |
| $\dfrac{\partial^2 f}{\partial x^2}$ | "partial squared f partial x squared" | Second partial derivative with respect to $x$ |
| $\dfrac{\partial^2 f}{\partial x \, \partial y}$ | "partial squared f partial x partial y" | Mixed partial derivative |
| $\nabla f$ | "nabla f" or "grad f" | Gradient vector $\left(\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right)$ |

## Key Formula

The **Black–Scholes PDE** uses all these notations simultaneously:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

Here $V = V(S, t)$ depends on two variables. The notation $\partial V / \partial S$ means "how $V$ changes as $S$ moves, holding $t$ fixed" — this is the option's **delta**.

## Example

For $f(x, y) = x^2 y + 3xy^2$:

$$\frac{\partial f}{\partial x} = 2xy + 3y^2 \qquad \frac{\partial f}{\partial y} = x^2 + 6xy$$

$$\frac{\partial^2 f}{\partial x \, \partial y} = 2x + 6y$$

In the Black–Scholes context, if $V(S, t)$ is a call option value, then $\partial V / \partial S = \Delta$, $\partial^2 V / \partial S^2 = \Gamma$, and $\partial V / \partial t = \Theta$.

## Remember

Every Greek letter in options trading is a partial derivative in disguise: Delta ($\partial V / \partial S$), Gamma ($\partial^2 V / \partial S^2$), Theta ($\partial V / \partial t$), Vega ($\partial V / \partial \sigma$), and Rho ($\partial V / \partial r$). When you see the $\partial$ symbol in a quant finance paper, it tells you the author is isolating the effect of one risk factor while freezing all others — the mathematical foundation of sensitivity analysis and hedging.
