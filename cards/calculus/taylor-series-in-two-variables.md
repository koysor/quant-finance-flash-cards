# Taylor Series in Two Variables

**Topic:** Calculus
**Tags:** Taylor series, two variables, partial derivatives, Ito lemma, second-order expansion
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The two-variable Taylor expansion approximates $f(x + \delta x,\; y + \delta y)$ near $(x, y)$ using partial derivatives: a tangent plane (first order) plus curvature terms (second order).

## Key Formula

$$f(x + \delta x,\, y + \delta y) \approx f + f_x\,\delta x + f_y\,\delta y + \tfrac{1}{2}\bigl(f_{xx}\,\delta x^2 + 2f_{xy}\,\delta x\,\delta y + f_{yy}\,\delta y^2\bigr)$$

The factor $\tfrac{1}{2}$ comes from $2!$, and the $2$ on the cross term from the two identical mixed partials $f_{xy} = f_{yx}$.

## Example

Approximate $f(x, y) = xy^2$ at $(1.1,\, 1.1)$ from the point $(1, 1)$. Here $f = 1$, $f_x = y^2 = 1$, $f_y = 2xy = 2$, $f_{xx} = 0$, $f_{xy} = 2y = 2$, $f_{yy} = 2x = 2$, and $\delta x = \delta y = 0.1$:

$$f \approx 1 + 0.1 + 0.2 + \tfrac{1}{2}\bigl(0 + 2(2)(0.01) + 2(0.01)\bigr) = 1.33$$

The exact value is $1.1 \times 1.21 = 1.331$.

## Remember

This is the exact template of Itô's lemma. Expand $V(S + \delta S,\, t + \delta t)$ and ordinarily every second-order term is negligible. But for $dS = \mu S\,dt + \sigma S\,dW$, $(\delta W)^2 \to \delta t$, so the $\delta S^2$ term is of order $\delta t$ and survives, giving the $\tfrac{1}{2}\sigma^2 S^2 V_{SS}$ term in Black-Scholes. The terms $\delta t^2$ and $\delta S\,\delta t$ are higher order and are dropped.
