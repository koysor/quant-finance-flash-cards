# Partial Derivatives

**Topic:** Calculus
**Tags:** calculus, partial derivatives, multivariable, Greeks, Black-Scholes
**Created:** 2026-02-28 20:46:20
**Author:** Claude Opus 4.6

---

## Definition

A **partial derivative** measures how a function of several variables changes when **one** variable changes while all others are held constant. For a function $f(x, y)$, the partial derivative with respect to $x$ is written $\frac{\partial f}{\partial x}$ (or $f_x$) and is computed by differentiating $f$ with respect to $x$, treating $y$ as a constant.

**Second-order partial derivatives** differentiate twice:

- $\frac{\partial^2 f}{\partial x^2}$ — differentiate with respect to $x$ twice.
- $\frac{\partial^2 f}{\partial y \partial x}$ — differentiate first with respect to $x$, then with respect to $y$. This is a **mixed partial**.

**Clairaut's theorem** (symmetry of mixed partials): if $f_{xy}$ and $f_{yx}$ are both continuous, then

$$\frac{\partial^2 f}{\partial x \, \partial y} = \frac{\partial^2 f}{\partial y \, \partial x}$$

## Key Formula

Partial derivative of $f(x, y)$ with respect to $x$:

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x + h,\, y) - f(x,\, y)}{h}$$

Second-order partial:

$$\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\!\left(\frac{\partial f}{\partial x}\right)$$

Mixed partial (Clairaut):

$$\frac{\partial^2 f}{\partial y \, \partial x} = \frac{\partial}{\partial y}\!\left(\frac{\partial f}{\partial x}\right) = \frac{\partial}{\partial x}\!\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial x \, \partial y}$$

## Example

Let $f(x, y) = x^2 y + e^{xy}$.

**First-order partials:**

$$\frac{\partial f}{\partial x} = 2xy + y\,e^{xy}$$

$$\frac{\partial f}{\partial y} = x^2 + x\,e^{xy}$$

**Mixed partial** (differentiating $f_x$ with respect to $y$):

$$\frac{\partial^2 f}{\partial y \, \partial x} = 2x + e^{xy} + xy\,e^{xy}$$

Differentiating $f_y$ with respect to $x$ gives the same result, confirming Clairaut's theorem.

## Remember

In quantitative finance the option price $V(S, t, \sigma, r)$ depends on several variables simultaneously. Each **Greek** is a partial derivative of $V$:

- **Delta** $\Delta = \frac{\partial V}{\partial S}$ — sensitivity to the underlying price.
- **Gamma** $\Gamma = \frac{\partial^2 V}{\partial S^2}$ — the second-order partial, measuring how Delta itself changes.
- **Theta** $\Theta = \frac{\partial V}{\partial t}$ — sensitivity to the passage of time.

The **Black-Scholes PDE** is written entirely in terms of partial derivatives:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

Without partial differentiation you cannot state, derive, or solve this equation. Mastering the notation $\partial f / \partial x$ and the mechanics of holding other variables constant is therefore a prerequisite for all option pricing theory.
