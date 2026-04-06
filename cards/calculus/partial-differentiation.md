# Partial Differentiation

**Topic:** Calculus
**Tags:** partial differentiation, multivariable calculus, chain rule, product rule, finance functions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Partial differentiation** is the technique of differentiating a function of several variables with respect to one variable while treating all other variables as constants. The standard rules of single-variable differentiation — power rule, product rule, chain rule, quotient rule — all apply, but are applied to one variable at a time. Where a variable appears in both a product and a composite expression, the rules must be combined carefully.

## Key Formula

For $f(x, y)$, differentiate with respect to $x$ treating $y$ as a constant:

$$\frac{\partial}{\partial x}\bigl[u(x,y)\cdot v(x,y)\bigr] = \frac{\partial u}{\partial x}v + u\frac{\partial v}{\partial x}$$

Chain rule for a composite — if $f = f(u)$ and $u = u(x, y)$:

$$\frac{\partial f}{\partial x} = \frac{df}{du}\cdot\frac{\partial u}{\partial x}$$

Implicit partial differentiation — if $F(x, y, z) = 0$ defines $z$ implicitly as a function of $x$ and $y$:

$$\frac{\partial z}{\partial x} = -\frac{\partial F/\partial x}{\partial F/\partial z}$$

## Example

The Black-Scholes call price is $C = S\,N(d_1) - K e^{-rT} N(d_2)$, where $d_1 = \dfrac{\ln(S/K) + (r + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$.

Compute Delta $\Delta = \partial C / \partial S$.

1. Differentiate $S\,N(d_1)$ using the product rule:
$$\frac{\partial}{\partial S}\bigl[S\,N(d_1)\bigr] = N(d_1) + S\,n(d_1)\frac{\partial d_1}{\partial S}$$

2. Since $d_1 = \tfrac{\ln S - \ln K + (r + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$, we have $\dfrac{\partial d_1}{\partial S} = \dfrac{1}{S\sigma\sqrt{T}}$.

3. Using the identity $S\,n(d_1) = K e^{-rT} n(d_2)$, the term from $-Ke^{-rT}N(d_2)$ cancels, leaving:
$$\Delta = N(d_1)$$

## Remember

Delta hedging relies entirely on this computation: $\Delta = N(d_1)$ is the quantity of the underlying a trader must hold to hedge one call option. The derivation requires the product rule (the $S \cdot N(d_1)$ term), the chain rule (because $d_1$ is itself a function of $S$), and a cancellation identity. In practice, risk systems compute thousands of such partial derivatives per second to keep hedges current — understanding the mechanics prevents mistaking a numerical approximation for an analytic formula, which matters when Greeks are used in regulatory capital models such as FRTB.
