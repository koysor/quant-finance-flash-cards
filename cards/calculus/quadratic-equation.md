# Quadratic Equation

**Topic:** Calculus
**Tags:** quadratic equation, discriminant, roots, parabola, payoff, bond pricing
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A **quadratic equation** is a polynomial equation of degree 2:

$$ax^2 + bx + c = 0, \qquad a \neq 0$$

It has exactly two roots in $\mathbb{C}$ (counting multiplicity). The roots may be two distinct real numbers, one repeated real number, or a pair of complex conjugates — determined entirely by the **discriminant** $\Delta = b^2 - 4ac$.

## Key Formula

**Quadratic formula** — the roots are:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Discriminant:**

| $\Delta = b^2 - 4ac$ | Nature of roots |
|---|---|
| $> 0$ | Two distinct real roots |
| $= 0$ | One repeated real root |
| $< 0$ | Two complex conjugate roots |

**Vieta's formulas** — if roots are $x_1$ and $x_2$:

$$x_1 + x_2 = -\frac{b}{a}, \qquad x_1 \cdot x_2 = \frac{c}{a}$$

## Example

In the CIR (Cox-Ingersoll-Ross) interest rate model, the characteristic equation for the bond price exponent involves a quadratic. More directly, find when the portfolio value $V = 2r^2 - 9r + 9$ equals zero (i.e. at which yields $r$ the portfolio breaks even):

$$2r^2 - 9r + 9 = 0 \implies r = \frac{9 \pm \sqrt{81 - 72}}{4} = \frac{9 \pm 3}{4}$$

Roots: $r = 3$ or $r = 1.5$. The portfolio is profitable for $1.5 < r < 3$.

## Remember

The quadratic equation is the simplest non-linear pricing relationship in finance. The Black-Scholes PDE for barrier options and the bond pricing ODEs in affine term structure models both reduce to Riccati equations — a type of first-order ODE with a quadratic non-linearity. Solving these Riccati equations algebraically involves finding roots of an associated quadratic, so fluency with the quadratic formula underpins closed-form bond and option prices in the CIR and Vasicek models.
