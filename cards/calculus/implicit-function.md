# Implicit Function

**Topic:** Calculus
**Tags:** implicit function, implicit differentiation, yield, calibration, root finding
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A function is **implicit** when the relationship between variables is given by an equation $F(x, y) = 0$ rather than by an isolated expression $y = f(x)$. The dependent variable cannot always be written in explicit closed form; instead, its existence and derivative are inferred from the constraint equation.

## Key Formula

**Implicit form:**

$$F(x, y) = 0$$

**Implicit differentiation** — differentiate both sides with respect to $x$, treating $y$ as a function of $x$:

$$\frac{\partial F}{\partial x} + \frac{\partial F}{\partial y} \cdot \frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{\partial F / \partial x}{\partial F / \partial y}$$

**Implicit Function Theorem:** if $F(x_0, y_0) = 0$ and $\frac{\partial F}{\partial y}(x_0, y_0) \neq 0$, then near $(x_0, y_0)$ there exists a unique explicit function $y = f(x)$ satisfying $F(x, f(x)) = 0$.

## Example

The yield-to-maturity $y$ of a coupon bond is defined implicitly by the pricing equation:

$$P = \sum_{k=1}^{n} \frac{C}{(1+y)^k} + \frac{F}{(1+y)^n}$$

Rearranging: $F(P, y) = P - \sum_{k=1}^{n} \frac{C}{(1+y)^k} - \frac{F}{(1+y)^n} = 0$.

There is no explicit formula for $y$ in terms of $P$ — yield must be found numerically (e.g. via Newton-Raphson). The modified duration is the implicit derivative $-\frac{1}{P}\frac{dP}{dy}$, obtained by differentiating the constraint equation implicitly.

## Remember

Implied volatility is the most important **implicit function** in derivatives. Given a market price $C_{\text{mkt}}$, implied volatility $\sigma_{\text{imp}}$ solves $C_{\text{BS}}(S, K, r, T, \sigma_{\text{imp}}) - C_{\text{mkt}} = 0$ — there is no closed-form inverse, so it is computed numerically for each option. The vega $\partial C / \partial \sigma$ is $\partial F / \partial \sigma$ evaluated at $\sigma_{\text{imp}}$, giving the Newton-Raphson update step. Understanding that implied volatility is an implicit function explains why calibrating a vol surface requires iterative root-finding rather than a single formula.
