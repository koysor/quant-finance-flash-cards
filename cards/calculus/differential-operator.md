# Differential Operator

**Topic:** Calculus
**Tags:** differential operator, differentiation, linear map, D notation, operator theory
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **differential operator** $D$ (or $\frac{d}{dx}$) is a linear map that takes a differentiable function as its input and returns its derivative as output. Treating differentiation as an operator rather than a process emphasises that it is a rule acting on a function space, and that the standard algebraic properties of linearity — additivity and homogeneity — hold exactly.

## Key Formula

Operator notation for the first and higher derivatives:

$$D f = f', \qquad D^2 f = f'', \qquad D^n f = f^{(n)}$$

Linearity of $D$ (the property that makes it a linear map):

$$D\bigl[a\,f + b\,g\bigr] = a\,Df + b\,Dg \qquad a, b \in \mathbb{R}$$

Polynomial in $D$ — used to express linear ODEs compactly. For constant coefficients $a_n, \ldots, a_0$:

$$\bigl(a_n D^n + a_{n-1} D^{n-1} + \cdots + a_1 D + a_0\bigr) f = 0$$

The partial differential operator for functions of several variables:

$$\frac{\partial}{\partial S}, \qquad \frac{\partial^2}{\partial S^2}, \qquad \frac{\partial}{\partial t}$$

## Example

The Black-Scholes PDE can be written compactly using operator notation. Define:

$$\mathcal{L} = \frac{\partial}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2}{\partial S^2} + rS\frac{\partial}{\partial S} - r$$

Then the PDE becomes $\mathcal{L} V = 0$.

For a portfolio of two options $V = 2C - P$, linearity gives:

$$\mathcal{L} V = 2\,\mathcal{L} C - \mathcal{L} P = 2 \cdot 0 - 0 = 0$$

so the combination satisfies the same PDE without separate verification.

## Remember

The Black-Scholes operator $\mathcal{L}$ is a linear differential operator, which is why any linear combination of solutions (e.g. a portfolio of European options) is also a solution. This **superposition principle** is the mathematical reason that delta-neutral hedges can be constructed by combining positions: linearity of $D$ cascades into linearity of the Greeks, so the portfolio delta, gamma, and vega are all just weighted sums of the individual position Greeks.
