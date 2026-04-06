# Ordinary Derivative

**Topic:** Calculus
**Tags:** derivative, single-variable, dy/dx, ordinary differential equations, partial derivatives
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **ordinary derivative** is the derivative of a function that depends on **one variable only**. Written $\frac{dy}{dx}$, it measures the instantaneous rate of change of $y$ with respect to $x$ when $y = f(x)$ is a single-variable function. The word "ordinary" distinguishes it from a **partial derivative**, which applies when a function depends on two or more variables and only one variable is allowed to change while the others are held fixed.

## Key Formula

For a single-variable function $y = f(x)$, the ordinary derivative is:

$$\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Higher-order ordinary derivatives are written:

$$\frac{d^2y}{dx^2}, \quad \frac{d^3y}{dx^3}, \quad \ldots, \quad \frac{d^n y}{dx^n}$$

**Contrast with partial derivative notation:** if $V$ depends on both $S$ and $t$, write $\frac{\partial V}{\partial S}$ (partial, curly $\partial$); if $f$ depends only on $x$, write $\frac{df}{dx}$ (ordinary, straight $d$).

## Example

Let $y = 3x^2 - 5x + 2$. This is a single-variable function, so use the ordinary derivative:

$$\frac{dy}{dx} = 6x - 5$$

At $x = 4$: $\frac{dy}{dx} = 6(4) - 5 = 19$.

This is a complete description — no other variables are involved, so there is no ambiguity about what is being held constant.

## Remember

In quantitative finance, the distinction between ordinary and partial derivatives separates two classes of equation with very different solution methods. A bond's duration involves $\frac{dP}{dy}$ — an ordinary derivative because the price $P$ is modelled as a function of yield $y$ alone. By contrast, the Black-Scholes PDE uses $\frac{\partial V}{\partial t}$ and $\frac{\partial V}{\partial S}$ because the option price $V$ depends on both time and the underlying simultaneously. Confusing the two notations — writing $d$ instead of $\partial$ — signals a misunderstanding of how many variables the function actually depends on.
