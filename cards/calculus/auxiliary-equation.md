# The Auxiliary Equation

**Topic:** Calculus
**Tags:** ODE, auxiliary equation, characteristic polynomial, complex roots, multiplicity, Euler formula
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

For a linear constant-coefficient ODE of any order, the trial solution $y = e^{mx}$ turns the differential equation into a polynomial in $m$, the **auxiliary equation** (or characteristic equation). Its $n$ roots, counted with multiplicity over the complex numbers, give the $n$ independent solutions. The trial works only for **constant** coefficients.

## Key Formula

$$a_n y^{(n)} + \cdots + a_1 y' + a_0 y = 0 \;\Longrightarrow\; a_n m^n + \cdots + a_1 m + a_0 = 0$$

A root of multiplicity $k$ contributes $(A_0 + A_1 x + \cdots + A_{k-1}x^{k-1})\,e^{mx}$. Complex roots come in conjugate pairs and, by Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$, give a real oscillatory solution:

$$Ce^{(\alpha + i\beta)x} + \bar{C}e^{(\alpha - i\beta)x} = e^{\alpha x}\bigl(A\cos\beta x + B\sin\beta x\bigr)$$

## Example

Solve $y^{(4)} - y = 0$. The auxiliary equation is $m^4 = 1$, so $m = 1, -1, i, -i$ and

$$y = Ae^{x} + Be^{-x} + C\cos x + D\sin x$$

## Remember

Complex numbers pay for themselves here: nearly every closed-form model solution is $e^{mx}$ for some root $m$. In a mean-reversion model the roots set the decay rates, and a rate $\kappa$ corresponds to a half-life of $\ln 2 / \kappa$.
